def onInit(info, mc, macro):
	#mc.Subscribe(macro, 'all')
	return

def onTrigger(info, mc, macro, comps, args):
	comps.op('moviefileout1').par.addframe.pulse()
	return