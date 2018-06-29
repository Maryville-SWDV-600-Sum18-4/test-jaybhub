# Create a window

# Make eye class if needed
# Draw eye in window - oval object
# Draw iris/pupil in eye - black circle on colored circle

# Get mouse click

# Undraw iris/pupil
# Redraw with x value of center point equal to mouseclick.getX plus radius

from graphics import *

class Eye:
    def __init__( self, centerPointX, centerPointY, window ):
        self.eyeLeftEdge = Point( centerPointX - 50, centerPointY - 25 )
        self.eyeRightEdge = Point( centerPointX + 50, centerPointY + 25)
        self.outerEye = Oval( self.eyeLeftEdge, self.eyeRightEdge )
        self.iris = Circle( Point(centerPointX, centerPointY), 20)
        self.pupil = Circle( Point(centerPointX, centerPointY), 8)
        
        self.outerEye.setWidth( 2 )
        self.outerEye.draw( window )
        
        self.iris.setFill( 'blue' )
        self.iris.draw( window )
        
        self.pupil.setFill( 'black' )
        self.pupil.draw( window )
        
    def lookAtMouse( self, X ):
        #self.iris.undraw()
        #self.pupil.undraw()
        if X < self.eyeRightEdge and X > self.eyeLeftEdge:
            self.iris.move( )
            self.pupil.move( )
        

def main():
    win = GraphWin( 'All Eyes On You', 400, 400 )
    
    leftEye = Eye( 125, 200, win )
    rightEye = Eye( 275, 200, win )
    
    while True:
        clickPoint = getMouse()
        leftEye.lookAtMouse( clickPoint.getX() )
        rightEye.lookAtMouse( clickPoint.getX() )

    
main()