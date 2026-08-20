---
title: JISApplet
apple_id: DTS10000961
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JISApplet/Listings/src_JISApplet_java.html
archived_at: '2026-07-18T03:13:09.713544Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JISApplet](JISApplet.md)


[Next](Document%20Revision%20History.md)[Previous](classes-test.html.md)

# src/JISApplet.java

```
/*
 * QuickTime for Java SDK Sample Code

   Usage subject to restrictions in SDK License Agreement
 * Copyright: © 1996-1999 Apple Computer, Inc.

 */
import java.net.*;
import java.applet.Applet;
import java.awt.*;
import java.io.*;

import quicktime.*;
import quicktime.io.QTFile;

import quicktime.app.QTFactory;
import quicktime.app.display.*;
import quicktime.app.image.ImageDrawer;
import quicktime.std.StdQTConstants;

// plays sound from a zip file asynchronously, i.e., in a Thread

import quicktime.*;

public class JISApplet extends Applet {
    private Drawable myQTContent;
    private QTCanvas myQTCanvas;

    public void init () {
        try {
            // this is a workaround required by a bug in the loading
            // mechanism of applets using the JavaPlugin on Netscape on Win
            if (QTSession.isInitialized() == false)
                QTSession.open();

                // set up a QTCanvas which will disply its content 
                // at its original size of smaller and centered in the space given
                // to the QTCanvas when the applet is layed out
            setLayout (new BorderLayout());
            myQTCanvas = new QTCanvas (QTCanvas.kInitialSize, 0.5F, 0.5F);
            add (myQTCanvas, "Center");     

                //our media is in the local directory
            QTFile file = new QTFile (getCodeBase().getFile() + getParameter("media"));
            myQTContent = QTFactory.makeDrawable (new FileInputStream(file), StdQTConstants.kDataRefFileExtensionTag, getParameter("ext"));
        } catch (QTException qtE) {
            qtE.printStackTrace();
                // something wrong with the content but QT itself is OK
            if (QTSession.isInitialized())
                myQTContent = ImageDrawer.getQTLogo();
            else
                throw new RuntimeException (qtE.getMessage());
        } catch (IOException ioE) {
            ioE.printStackTrace();
            myQTContent = ImageDrawer.getQTLogo();
        }
    }   

    public void start () { 
        try { // if QT was not successfully initialized the QTCanvas will be null
            if (myQTCanvas != null)
                myQTCanvas.setClient (myQTContent, true);           
        } catch (QTException e) {
            e.printStackTrace();
        }
    }

    public void stop () { 
        if (myQTCanvas != null)
            myQTCanvas.removeClient();
    }

    public void destroy () {
        QTSession.close();
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](classes-test.html.md)

