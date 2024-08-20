![ComfyUI-flux-clip-strength](https://github.com/user-attachments/assets/9309f3a4-201f-4594-8127-0575537112f7)

This is some experimental code I made real fast for Comfyui's nodes_flux.py. it lets control the strength of clip_l and t5xxl clip. it also allows increasings guidance past 100. It may or may not work as intended, but it seems to have an affect on the output. Please feel free to improve it!

**Instructions:** 

1. (Make backup copy of nodes_flux.py first)
2. Replace ComfyUI\comfy_extras\nodes_flux.py with this code for strength control of clip_l and t5xxl in the nodes_flux.py in Comfyui.
3. Add a ClipTextEncodeflux node to your workflow instead of regular default cliptextencode node. 

4. *If you want to make your own clip_l model from another sdxl checkpoint: Use the saveclip node on your sdxl model and place the new clip_l output from /comfyui/outputs/checkpoints into /comfyui/models/clip* and load it as your new clip_l in the dualcliploader node.

Ps. We aren't just doing 1 or 10 strength, **We have 100,000 max strength! (for max experimentation)**

Please support custom node development efforts for 311_code on https://ko-fi.com/311_code
