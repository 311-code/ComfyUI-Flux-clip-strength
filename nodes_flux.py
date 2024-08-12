# Please support my custom development on 311_code on https://ko-fi.com/311_code

# Instructions: Replace ComfyUI\comfy_extras\nodes_flux.py with this code for strength control of clip_l and t5xxl in the nodes_flux.py in Comfyui. 
# If you want to make your own clip_l model from another sdxl checkpoint use the saveclip node on your sdxl model and place the new clip_l output from /comfyui/outputs/checkpoints into /comfyui/models/clip

# We aren't just doing 1 or 10, We have 100,000 max strength! (for excessive experimentation)

import node_helpers

class CLIPTextEncodeFlux:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": ("CLIP", ),
                "clip_l": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "t5xxl": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "clip_l_strength": ("FLOAT", {"default": 500.0, "min": 0.0, "max": 100000.0, "step": 0.01}),
                "t5xxl_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 100000.0, "step": 0.01}),
                "guidance": ("FLOAT", {"default": 3.5, "min": 0.0, "max": 100000.0, "step": 0.01}),
            }
        }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "advanced/conditioning/flux"

    def encode(self, clip, clip_l, t5xxl, clip_l_strength, t5xxl_strength, guidance):
        print("Tokenizing clip_l and t5xxl texts")
        tokens_l = clip.tokenize(clip_l)["l"]
        print(f"tokens_l: {tokens_l}")
        tokens_t5 = clip.tokenize(t5xxl)["t5xxl"]
        print(f"tokens_t5: {tokens_t5}")
    
        print("Combining tokens into token_weights dictionary")
        token_weights = {"l": tokens_l, "t5xxl": tokens_t5}
        print(f"token_weights: {token_weights}")
    
        print("Encoding tokens with clip.encode_from_tokens")
        output = clip.encode_from_tokens(token_weights, return_pooled=True, return_dict=True)
        print(f"output: {output}")
    
        # Apply strengths
        cond = output.pop("cond")
        print(f"cond before strength adjustment: {cond}")
    
        # Apply strengths to tensors directly
        if cond.dim() == 3:  # Check if the cond tensor has the correct dimensions
            cond[:, :, :1] *= clip_l_strength
            cond[:, :, 1:] *= t5xxl_strength
    
        print(f"cond after strength adjustment: {cond}")
        output["guidance"] = guidance
        return ([[cond, output]], )


class FluxGuidance:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", ),
                "guidance": ("FLOAT", {"default": 3.5, "min": 0.0, "max": 100000.0, "step": 0.1}),
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "append"

    CATEGORY = "advanced/conditioning/flux"

    def append(self, conditioning, guidance):
        c = node_helpers.conditioning_set_values(conditioning, {"guidance": guidance})
        return (c, )

NODE_CLASS_MAPPINGS = {
    "CLIPTextEncodeFlux": CLIPTextEncodeFlux,
    "FluxGuidance": FluxGuidance,
}
           
