---
title: JScriptApplet
apple_id: DTS10000962
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JScriptApplet/Listings/src_JScriptApplet_java.html
archived_at: '2026-07-18T03:13:14.130605Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JScriptApplet](JScriptApplet.md)


[Next](Document%20Revision%20History.md)[Previous](classes-QTMovie.html.md)

# src/JScriptApplet.java

```
/*
 * QuickTime for Java SDK Sample Code

   Usage subject to restrictions in SDK License Agreement
 * Copyright: © 1996-1999 Apple Computer, Inc.

 */
import java.applet.*;
import java.awt.*;

import quicktime.*;
import quicktime.app.*;
import quicktime.io.*;
import quicktime.std.movies.*;
import quicktime.app.players.*;
import quicktime.app.display.*;

public class JScriptApplet extends Applet {
    private QTCanvas myCanvas;
    private MoviePlayer myPlayer;

    public void init() {
        try {
        // IMPORTANT, You should not call QTSession.open
        //  multiple times, otherwise you you will need to call QTSession.close the same
        //  number of times to properly shutdown. There appears to be a side effect in Windows 95/98
        //  With the Netscape browser and sun Java plugin where
        //  the Init method could get called Multiple times
        //  Checking the session to see if it is already initialised is tbe correct
        //  method safeguard against this.
            if (QTSession.isInitialized() == false)
            {
                QTSession.open();
            }
        }
        catch (Exception e) {
            e.printStackTrace();
            QTSession.close();
        }
    }

    public void start () {
        try {
            myCanvas = new QTCanvas(QTCanvas.kInitialSize, 0.5F, 0.5F);
            add("Center", myCanvas);
            QTFile qtf = new QTFile(getCodeBase().getFile() + getParameter("file"));
            OpenMovieFile movieFile = OpenMovieFile.asRead (qtf);
            Movie myMovie = Movie.fromFile(movieFile);
            myPlayer = new MoviePlayer(myMovie);

            myCanvas.setClient(myPlayer, true);
        }
        catch (Exception e) {
            e.printStackTrace();
            QTSession.close();
        }
    }

    public void stop () {
        myCanvas.removeClient();
    }

    public void destroy () {
        QTSession.close();
    }

    public void resetTime (int time) {
        try {
            myPlayer.setRate(0);
            myPlayer.setTime(time);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void pause () {
        try {
            if (myPlayer.getRate() == 0)
                myPlayer.setRate(1);
            else
                myPlayer.setRate(0);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public boolean isPlaying () {
        try {
            return myPlayer.getRate() != 0;
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public int getMaxTime () {
        try {
            return myPlayer.getDuration();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        return 0;
    }

    public int getMovieTime () {
        try {
            return myPlayer.getTime();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        return 0;
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](classes-QTMovie.html.md)

