import uuid
import subprocess

def onInit(info, mc, macro):
	#mc.Subscribe(macro, 'all')
	return

def onTrigger(info, mc, macro, comps, args):
	id = uuid.uuid4()
	subprocess.run(['wsl', 'gphoto2', "--capture-image-and-download", f"--filename=/mnt/c/Projects/fear-street-prom-ai-workflow/capture/{id}.jpg"])
	comps.op('Macrocosm').TriggerMacro('loadImage', args=[str(id)], delayMilliSeconds=3000)
	return