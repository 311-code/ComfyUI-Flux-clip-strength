![ComfyUI-flux-clip-strength](https://github.com/user-attachments/assets/9309f3a4-201f-4594-8127-0575537112f7)

This is experimental code I just made for Comfyui's nodes_flux.py let's allows yout to control the strength of clip_l and t5xxl clip, and also increase guidance past 100.

**Instructions:** Replace ComfyUI\comfy_extras\nodes_flux.py with this code for strength control of clip_l and t5xxl in the nodes_flux.py in Comfyui. 

*If you want to make your own clip_l model from another sdxl checkpoint use the saveclip node on your sdxl model and place the new clip_l output from /comfyui/outputs/checkpoints into /comfyui/models/clip*

We aren't just doing 1 or 10, **We have 100,000 max strength! (for excessive experimentation)**

Please support my custom development efforts for ![311_code on](https://ko-fi.com/311_code)
