# Create a window

# Make eye class
    # Draw eyes in window - oval object
    # Draw irises/pupils in eye - black circle on colored circle

# Indefinite loop
    # Get mouse click

    # Undraw iris/pupil
    # Redraw with x value of center point equal to mouseclick.getX plus radius
        #Do not allow to extend beyond boundary of eye

from graphics import *

class Eye:
    def __init__( self, centerPointX, centerPointY, window ):
        self.centerPointX = centerPointX
        self.centerPointY = centerPointY
        self.window = window
        
        self.eyeLeftEdge = Point( centerPointX - 50, centerPointY - 25 )
        self.eyeRightEdge = Point( centerPointX + 50, centerPointY + 25)
        self.outerEye = Oval( self.eyeLeftEdge, self.eyeRightEdge )
        self.outerEye.setWidth( 2 )
        self.outerEye.draw( window )
        
        self.iris = Circle( Point(centerPointX, centerPointY), 20)
        self.iris.setFill( 'blue' )
        self.iris.draw( window )
        
        self.pupil = Circle( Point(centerPointX, centerPointY), 8)
        self.pupil.setFill( 'black' )
        self.pupil.draw( window )
              
    def changeIris( self, newX ):
        self.iris = Circle( Point( newX, self.centerPointY ), 20)
        self.iris.setFill( 'blue' )
        self.iris.draw( self.window )
        
    def changePupil( self, newX ):
        self.pupil = Circle( Point( newX, self.centerPointY ), 8)
        self.pupil.setFill( 'black' )
        self.pupil.draw( self.window )
    
    def lookAtMouse( self, X ):
        self.iris.undraw()
        self.pupil.undraw()
        
        if X < self.eyeRightEdge.getX() - 10 and X > self.eyeLeftEdge.getX() + 10:
            self.changeIris( X )
            self.changePupil( X )
            
        elif X < self.eyeLeftEdge.getX() + 10:
            self.changeIris( self.centerPointX - 27 )
            self.changePupil( self.centerPointX - 27 )
            
        elif X > self.eyeRightEdge.getX() - 10:
            self.changeIris( self.centerPointX + 27 )
            self.changePupil( self.centerPointX + 27 )
            

def main():
    win = GraphWin( 'All Eyes On You', 400, 400 )
    
    leftEye = Eye( 125, 200, win )
    rightEye = Eye( 275, 200, win )
    
    while True:
        clickPoint = win.getMouse()
        leftEye.lookAtMouse( clickPoint.getX() )
        rightEye.lookAtMouse( clickPoint.getX() )

    
main()