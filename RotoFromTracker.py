import nuke

# RotoFromTracker tool for Nuke
# By Gonzalo G. Campos
# Tool for create a roto whith the same transform animation of the selected tracker node.
# This way you can track and create a roto with correct motion blur faster.

#Creates a roto with the transform of selected tracker
def RotoFromTracker():

	sel = None
	try:
	    sel = nuke.selectedNode()
	except ValueError:
	    pass
	if sel == None:
        return

	if sel.Class() == 'Tracker4':
		r = nuke.nodes.Roto().setInput(0, None)
		r.setXYpos(sel.xpos()+70,sel.ypos()+70)
		r.knob('tile_color').setValue(0x226e22ff)
		r.knob('label').setValue('From %s' % sel.knob('name').getValue())
		r['translate'].fromScript(sel['translate'].toScript())
		r['rotate'].fromScript(sel['rotate'].toScript())
		r['scale'].fromScript(sel['scale'].toScript())
		r['center'].fromScript(sel['center'].toScript())
