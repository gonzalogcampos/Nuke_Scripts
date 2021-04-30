import nuke

# RotoLifetime tool for Nuke
# By Gonzalo G. Campos
# Tool for change lifetime of a shape or layer in a roto.
# It is usefull for set the frame to start, frame to end or frame to frame when roto.
# Seting faster the lifetime without puting the shapes out of the frame.
# I put hotkeys ctrl+shift+i ctrl+shift+o ctrl+shift+p


# Sets the lifetime from the first key to the last
def RotoLifetime():

    sel = None
    try:
        sel = nuke.selectedNode()
    except ValueError:
        pass
    if sel == None:
        return

    if sel.Class() == 'Roto':
        for shape in sel['curves'].getSelected():
            kf = shape[0].center.getControlPointKeyTimes()
            kfs = [int(i) for i in kf]
            start = (min(kfs))
            end = (max(kfs))

            sel['lifetime_type'].setValue(4)

            sel['lifetime_start'].setValue(start)
            sel['lifetime_end'].setValue(end)


# Sets the lifetime from current frame
def RotoLifetime_I():

    sel = None
    try:
        sel = nuke.selectedNode()
    except ValueError:
        pass
    if sel == None:
        return

    if sel.Class() == 'Roto':
        for shape in sel['curves'].getSelected():

            start = sel['lifetime_start'].getValue()
            end = sel['lifetime_end'].getValue()
            ty = sel['lifetime_type'].getValue()

            if ty == 0:
                sel['lifetime_type'].setValue(3) #FRAME TO END
            elif ty == 1:
                sel['lifetime_type'].setValue(4) #FRAME TO FRAME
            elif ty == 2:
                sel['lifetime_type'].setValue(3) #FRAME TO END

            sel['lifetime_start'].setValue(nuke.frame())
            sel['lifetime_end'].setValue(end)

# Sets the lifetime to current frame
def RotoLifetime_O():

    sel = None
    try:
        sel = nuke.selectedNode()
    except ValueError:
        pass
    if sel == None:
        return

    if sel.Class() == 'Roto':
        for shape in sel['curves'].getSelected():

            start = sel['lifetime_start'].getValue()
            end = sel['lifetime_end'].getValue()
            ty = sel['lifetime_type'].getValue()

            if ty == 0:
                sel['lifetime_type'].setValue(1) #END TO FRAME
            elif ty == 2:
                sel['lifetime_type'].setValue(1) #END TO FRAME
            elif ty == 3:
                sel['lifetime_type'].setValue(4) #FRAME TO FRAME

            sel['lifetime_start'].setValue(start)
            sel['lifetime_end'].setValue(nuke.frame())
