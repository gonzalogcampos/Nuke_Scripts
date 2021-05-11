import nuke

# DeactivateMotionblur tool for nuke
# By Gonzalo G. Campos
# This tool is usefull for optimize your nuke script when compositing.
# It memorizes the current value of motionblur for each node and sets it to 0
# Then when you reactivate the motionblur recovers the last value.

#DEACTIVATION
def OptiMotionblur_D():
    for node in nuke.allNodes():
        if node.Class() == 'Transform' or node.Class() == 'CornerPin2D':
            if not node.knob('aux_motionblur'):
                auxKnob = nuke.Double_Knob('aux_motionblur', 'Aux Motionblur')
                auxKnob.setEnabled(False)
                auxKnob.setValue(node.knob('motionblur').getValue())
                node.addKnob(auxKnob)
                node.knob('motionblur').setValue(0)
                node.knob('motionblur').setEnabled(False)

#REACTIVATION
def OptiMotionblur_A():
    for node in nuke.allNodes():
        if node.Class() == 'Transform' or node.Class() == 'CornerPin2D':
            if node.knob('aux_motionblur'):
                node.knob('motionblur').setValue(node.knob('aux_motionblur').getValue())
                node.knob('motionblur').setEnabled(True)
                node.removeKnob(node.knob('aux_motionblur'))