def onInit(info, mc, macro):
	#mc.Subscribe(macro, 'all')
	return

def onTrigger(info, mc, macro, comps, args):
	print('load image')
	print(args)
	op('/components/image').par.file = f"capture/{args[0]}.jpg"
	op('/components/image').par.reloadpulse.pulse()
	return