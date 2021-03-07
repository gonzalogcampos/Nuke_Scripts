import nuke

#NewRefFrame tool for nuke
#By Gonzalo G. Campos
#Tool for change the reference frame of animation in a transform node.
#It is usefull for copy-pasate transform nodes created from a traker.
#And change the reference frame without the traker node.

def NewRefFrame():
    count = 0
    for n in nuke.selectedNodes():
        if n.Class() == 'Transform':

            count += 1

            msg = '%s changed reference frame to: %i in:' % (n.knob('name').getText() , nuke.frame())

            #TRANSLATE ANIMATION
            translate = n.knob('translate')

            xRef = translate.getValue()[0]
            yRef = translate.getValue()[1]

            if(translate.isAnimated()):

                msg += ' Translate'

                tanslateXCurve = translate.animation(0)
                tanslateYCurve = translate.animation(1)

                for key in tanslateXCurve.keys():
                    tanslateXCurve.setKey( key.x, key.y - xRef)

                for key in tanslateYCurve.keys():
                    tanslateYCurve.setKey( key.x, key.y - yRef)

            #ROTATE ANIMATION
            rotate = n.knob('rotate')

            if(rotate.isAnimated()):

                msg += ' Rotate'

                rotateCurve = rotate.animation(0)
                rRef = rotate.getValue()
                for key in rotateCurve.keys():
                    rotateCurve.setKey( key.x, key.y - rRef)

            #SCALE ANIMATION
            scale = n.knob('scale')

            if(scale.isAnimated()):

                msg += ' Scale'

                if ( scale.getValue().__class__ == list().__class__ ):
                    scaleWCurve = scale.animation(0)
                    scaleHCurve = scale.animation(1)
                    wRef = scale.getValue()[0]
                    hRef = scale.getValue()[1]
                    for key in scaleWCurve.keys():
                        scaleWCurve.setKey( key.x, key.y/wRef)
                    for key in scaleHCurve.keys():
                        scaleHCurve.setKey( key.x, key.y/hRef)

                else:
                    scaleCurve = scale.animation(0)
                    sRef = scale.getValue()
                    for key in scaleCurve.keys():
                        scaleCurve.setKey( key.x, key.y/sRef)
            

            #CENTER ANIMATION
            center = n.knob('center')

            if(center.isAnimated()):

                msg += ' Center'

                centerXCurve = center.animation(0)
                centerYCurve = center.animation(1)

                for key in centerXCurve.keys():
                    centerXCurve.setKey( key.x, key.y + xRef )

                for key in centerYCurve.keys():
                    centerYCurve.setKey( key.x, key.y + yRef )
        

            
            print msg

    print '%i nodes modified!' % (count)


