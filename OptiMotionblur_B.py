import nuke

# DeactivateMotionblur tool for nuke
# By Gonzalo G. Campos
# This tool is usefull for optimize your nuke script when compositing.
# It memorizes the current value of motionblur for each node and sets it to 0
# Then when you reactivate the motionblur recovers the last value.

#DEACTIVATION
def optiMotionblur():
    for node in nuke.allNodes():
        if node.Class() == 'Transform' or node.Class() == 'CornerPin2D':
            was = True
            if not node.knob('aux_motionblur'):
                auxKnob = nuke.Double_Knob('aux_motionblur', 'Aux Motionblur')
                auxKnob.setEnabled(False)
                node.addKnob(auxKnob)
                node.knob('aux_motionblur').setValue(node.knob('motionblur').getValue())
                was = False

            if not nuke.root().knob('root_motionblur').getValue():
                node.knob('aux_motionblur').setValue(node.knob('motionblur').getValue())
                node.knob('motionblur').setValue(0)
                node.knob('motionblur').setEnabled(False)
            else:
                node.knob('motionblur').setValue(node.knob('aux_motionblur').getValue())
                node.knob('motionblur').setEnabled(True)

def knobCallback():
    try:
        if nuke.thisKnob() == nuke.root().knob('root_motionblur'):
            optiMotionblur()
    except:
        pass

def defineRoot():
    bk = nuke.Boolean_Knob('root_motionblur', 'Motionblur')
    nuke.root().addKnob(bk)
    nuke.root().knob('root_motionblur').setDefaultValue([1])
    nuke.addKnobChanged(knobCallback, node=nuke.root())


def onNodeCreate():
    node = nuke.thisNode()

    if not node.knob('aux_motionblur'):
            auxKnob = nuke.Double_Knob('aux_motionblur', 'Aux Motionblur')
            auxKnob.setEnabled(False)
            auxKnob.setValue(node.knob('motionblur').getValue())
            node.addKnob(auxKnob)

    if not nuke.root().knob('root_motionblur').getValue():
        node.knob('motionblur').setValue(0)
        node.knob('motionblur').setEnabled(False)

def conmuteOptiMotionblur():
    nuke.root().knob('root_motionblur').setValue(not nuke.root().knob('root_motionblur').getValue())


defineRoot()
nuke.addOnUserCreate(onNodeCreate, nodeClass="Transform")
nuke.addOnUserCreate(onNodeCreate, nodeClass="CornerPin2D")
