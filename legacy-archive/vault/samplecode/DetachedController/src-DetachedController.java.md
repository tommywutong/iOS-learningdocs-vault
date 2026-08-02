---
title: DetachedController
apple_id: DTS10000940
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DetachedController/Listings/src_DetachedController_java.html
archived_at: '2026-07-18T03:06:47.691689Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DetachedController](DetachedController.md)


[Next](Document%20Revision%20History.md)[Previous](Readme.txt.md)

# src/DetachedController.java

```
/*
 * QuickTime for Java SDK Sample Code

   Usage subject to restrictions in SDK License Agreement
 * Copyright: © 1996-1999 Apple Computer, Inc.

 */
import java.awt.*;
import java.io.*;
import java.awt.event.*;

import quicktime.std.*;
import quicktime.std.movies.*;
import quicktime.app.display.*;
import quicktime.io.*;
import quicktime.std.StdQTConstants;
import quicktime.app.players.*;
import quicktime.*;
import quicktime.std.clocks.*;
import quicktime.qd.*;


public class DetachedController extends Frame implements StdQTConstants{
    public static void main(String args[]) {
        try {
            QTSession.open();
            QTFile file = QTFile.standardGetFilePreview(new int[] { kQTFileTypeMovie });
            new DetachedController(Movie.fromFile(OpenMovieFile.asRead(file)));

        } catch (Exception e) {
            e.printStackTrace();
        }

    }   

    DetachedController(Movie mMovie) throws QTException{
        super ("QT in Java");

            // Create the movie and its player - detach movie from controller       
        setControllerCanvas(mMovie);            

            // Create the movie controller and the detached canvas.                         
        setMovieCanvas(mMovie);

        add (new Label("DETACHED CONTROLLER"), "Center");

        addWindowListener(new WindowAdapter () {
            public void windowClosing (WindowEvent e) {
                QTSession.close();
                dispose();
            }

            public void windowClosed (WindowEvent e) { 
                System.exit(0);
            }
        });

        pack();
        show();     
        toFront();
    }

    void setControllerCanvas(Movie mMovie) throws QTException {
        QTCanvas controllerCanvas = new QTCanvas(); 

        MovieController mController = new MovieController(mMovie, mcScaleMovieToFit);

        //detach the movie from its controller
        mController.setAttached(false);

        QTPlayer qtPlayer = new QTPlayer(mController);

        add(controllerCanvas, "North");
        controllerCanvas.setClient(qtPlayer, true);     
    }

    void setMovieCanvas(Movie mMovie) throws QTException{   
        QTCanvas movieCanvas = new QTCanvas();

        MoviePlayer mPlayer = new MoviePlayer(mMovie);

        add(movieCanvas, "South");          
        movieCanvas.setClient(mPlayer, true);               
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Readme.txt.md)

