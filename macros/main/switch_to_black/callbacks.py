def onInit(info, mc, macro):
	#mc.Subscribe(macro, 'all')
	return

def onTrigger(info, mc, macro, comps, args):
	comps.op('switch_blackout').par.switch = 0
	return