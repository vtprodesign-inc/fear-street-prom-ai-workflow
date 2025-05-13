def onInit(info, mc, macro):
	#mc.Subscribe(macro, 'all')
	mc.Subscribe(macro, 'photo_loaded')
	return

def onTrigger(info, mc, macro, comps, args):
	comps.op('PhotoCompositor').GenerateComfyUI()
	return