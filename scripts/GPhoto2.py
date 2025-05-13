from json import loads, dumps
import traceback

import uuid
import subprocess
#import queue

from CallbacksExt import CallbacksExt
from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class GPhoto2(CallbacksExt):
    """  """

    def __init__(self, ownerComp):
        # the component to which this extension is attached
        self.ownerComp = ownerComp

        # init callbacks
        self.callbackDat = self.ownerComp.par.Callbackdat.eval()
        try:
            CallbacksExt.__init__(self, ownerComp)
        except:
            self.ownerComp.addScriptError(traceback.format_exc() + \
                    "Error in CallbacksExt __init__. See textport.")
            print()
            print("Error initializing callbacks - " + self.ownerComp.path)
            print(traceback.format_exc())
        # run onInit callback
        try:
            self.DoCallback('onInit', {'ownerComp':self.ownerComp})
        except:
            self.ownerComp.addScriptError(traceback.format_exc() + \
                    "Error in custom onInit callback. See textport.")
            print(traceback.format_exc())



        # the component to which data is stored
        self.dataComp = ownerComp.op('data')

        # stored items (persistent across saves and re-initialization):
        storedItems = [
            # Only 'name' is required...
            # {'name': 'PhotoQueue', 'default': queue.Queue(), 'readOnly': False, 'property': True, 'dependable': True},
            {'name': 'CurrentPhotoUUID', 'default': '', 'readOnly': False, 'property': True, 'dependable': True},
        ]
        self.stored = StorageManager(self, self.dataComp, storedItems)

    # pulse parameter to open extension
    def pulse_Editextension(self):
        self.ownerComp.op('GPhoto2').par.edit.pulse()
    
    def pulse_Capturephoto(self):
        self.CapturePhoto()
    
    def pulse_Loadphoto(self):
        self.LoadPhoto(self.ownerComp.par.loadphoto.eval())

    def CapturePhoto(self):
        id = uuid.uuid4()
        base = project.folder.split('C:')[1]
        # TODO Implement a queue at some point
        # self.PhotoQueue.put(id)
        self.CurrentPhotoUUID = id
        subprocess.run(['wsl', 'gphoto2', "--capture-image-and-download", f"--filename=/mnt/c{base}/capture/{id}.jpg"])
    
    def LoadPhoto(self, path):
        movieFileOp = self.ownerComp.op('moviefilein1')
        movieFileOp.par.file = f"capture/{path}.jpg"
        movieFileOp.par.reloadpulse.pulse()

        op.MC.Emit('photo_loaded')

    def _handleFolderOnFound(self, info, row):
        baseName = info.baseName
        path = info.path
        if baseName == self.CurrentPhotoUUID:
            self.LoadPhoto(path)
    
