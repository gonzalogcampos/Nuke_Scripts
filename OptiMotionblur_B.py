import nuke

# DeactivateMotionblur tool for nuke
# By Gonzalo G. Campos
# This tool is usefull for optimize your nuke script when compositing.
# It memorizes the current value of motionblur for each node and sets it to 0
# Then when you reactivate the motionblur recovers the last value.

transform = True
motionblur = True
cornerpin = True
roto = True



#DEACTIVATION
def OptiMotionblur_D():
    for node in nuke.allNodes():
        if (node.Class() == 'Transform' and transform) or (node.Class() == 'CornerPin2D' and cornerpin):
            if not node.knob('aux_motionblur'):
                auxKnob = nuke.Double_Knob('aux_motionblur', 'Aux Motionblur')
                auxKnob.setEnabled(False)
                auxKnob.setValue(node.knob('motionblur').getValue())
                node.addKnob(auxKnob)
                node.knob('motionblur').setValue(0)
                node.knob('motionblur').setEnabled(False)
        elif roto and node.Class() == 'Roto' and node.knob('motionblur_mode').getValue()==1:
            if not node.knob('aux_motionblur'):
                auxKnob = nuke.Double_Knob('aux_motionblur', 'Aux Motionblur')
                auxKnob.setEnabled(False)
                auxKnob.setValue(node.knob('global_motionblur').getValue())
                node.addKnob(auxKnob)
                node.knob('global_motionblur').setValue(0)
                node.knob('global_motionblur').setEnabled(False)
        elif motionblur and node.Class() == 'MotionBlur':
            if not node.knob('aux_motionblur'):
                auxKnob = nuke.Boolean_Knob('aux_motionblur', 'Aux Motionblur')
                auxKnob.setEnabled(False)
                auxKnob.setValue(node.knob('disable').getValue())
                node.addKnob(auxKnob)
                node.knob('disable').setValue(True)
                node.knob('disable').setEnabled(False)


#REACTIVATION
def OptiMotionblur_A():
    for node in nuke.allNodes():
        if node.Class() == 'Transform' or node.Class() == 'CornerPin2D':
            if node.knob('aux_motionblur'):
                node.knob('motionblur').setValue(node.knob('aux_motionblur').getValue())
                node.knob('motionblur').setEnabled(True)
                node.removeKnob(node.knob('aux_motionblur'))
        elif node.Class() == 'Roto' and node.knob('motionblur_mode').getValue()==1:
            if node.knob('aux_motionblur'):
                node.knob('global_motionblur').setValue(node.knob('aux_motionblur').getValue())
                node.knob('global_motionblur').setEnabled(True)
                node.removeKnob(node.knob('aux_motionblur'))
        elif node.Class() == 'MotionBlur':
            if node.knob('aux_motionblur'):
                node.knob('disable').setValue(node.knob('aux_motionblur').getValue())
                node.knob('disable').setEnabled(True)
                node.removeKnob(node.knob('aux_motionblur'))
