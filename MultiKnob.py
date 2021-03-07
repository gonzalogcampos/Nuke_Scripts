import nuke
import copy

#MultiKnob tool for nuke
#By Gonzalo G. Campos
#This tool allows to change the value of same knob in multiple nodes.
#It's too easy to use, just select all nodes you want to change and run
#the tool. A panel will appear. Then select the node class you want to 
#modify, and the knob name. A copy of the knob will appear. Modify it
#and click ok.

#Multiknob panel class
class Multiknob_panel(nukescripts.PythonPanel):

    #Init
    def __init__(self, nodes):

        nukescripts.PythonPanel.__init__(self, 'Multiknob')

        self.nodes = nodes

        self.classKnob = nuke.Enumeration_Knob('class', 'Class', self.getClases(nodes))
        self.knobKnob  = nuke.Enumeration_Knob('knob', 'Knob', [])
        self.valueKnob = nuke.Boolean_Knob('value', 'Value')
        self.addKnob(self.classKnob)
        self.addKnob(self.knobKnob)
        #self.addKnob(self.valueKnob)

        self.changeKnob()
    
    #Change the knob nama
    def changeKnob(self):
        for n in self.nodes:
            if(self.classKnob.value() == n.Class()):
                self.knobKnob.setValues(n.knobs().keys())
                break

    #Change the value knob
    def changeValue(self):
        for n in self.nodes:
            if(self.classKnob.value() == n.Class()):
                try:
                    self.removeKnob(self.valueKnob)
                except:
                    pass
                self.removeKnob(self.okButton)
                self.removeKnob(self.cancelButton)
                try:
                    self.valueKnob = copy.copy(n.knob(self.knobKnob.value()))
                    self.addKnob(self.valueKnob)
                except:
                    pass
                self.addKnob(self.okButton)
                self.addKnob(self.cancelButton)
                break
    
    #Modify all the values in the nodes
    def updateValues(self):
        for n in self.nodes:
            if(self.classKnob.value() == n.Class()):
                try:
                    n.knob(self.knobKnob.value()).setValue(self.valueKnob.getValue())
                except:
                    pass
    
    #Returns a list of clases in selected nodes
    def getClases(self, nodes):
        classes = list()
        for n in nodes:
            classes.append(n.Class())
        return list(dict.fromkeys(classes))

    #Knob changed function
    def knobChanged(self, knob):
        if knob is self.classKnob:
            self.changeKnob()
            self.changeValue()
        elif knob is self.knobKnob:
            self.changeValue()
        elif knob is self.okButton:
            self.updateValues()

#Multi knob
def multiKnob():
    nodes = nuke.selectedNodes()
    p = Multiknob_panel(nodes)
    p.showModalDialog()