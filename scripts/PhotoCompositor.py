from json import loads, dumps
import traceback

from CallbacksExt import CallbacksExt
from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class PhotoCompositor(CallbacksExt):
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
            {'name': 'Data', 'default': None, 'readOnly': False,
                                     'property': True, 'dependable': True},
        ]
        self.stored = StorageManager(self, self.dataComp, storedItems)



    # pulse parameter to open extension
    def pulse_Editextension(self):
        self.ownerComp.op('PhotoCompositor').par.edit.pulse()
    
    def pulse_GenerateComfyUI(self):
        self.GenerateComfyUI()

    def GenerateComfyUI(self):
        comfyUIOp = self.ownerComp.op('TDComfyUI')
        comfyUIOp.par.Generate.pulse()
    
    def GenerateBloodOverlay(self):
        bloodOverlayOp = self.ownerComp.op('BloodOverlayCompositor')
        bloodOverlayOp.DetectFaces()


