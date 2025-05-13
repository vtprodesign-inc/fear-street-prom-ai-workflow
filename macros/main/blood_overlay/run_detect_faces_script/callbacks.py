def onInit(info, mc, macro):
	#mc.Subscribe(macro, 'all')
	mc.Subscribe(macro, 'comfyui_completed')
	return

def onTrigger(info, mc, macro, comps, args):
	comps.op('BloodOverlayCompositor').DetectFaces()
	return