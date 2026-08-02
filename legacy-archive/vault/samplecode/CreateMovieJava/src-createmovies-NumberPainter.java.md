---
title: CreateMovieJava
apple_id: DTS10000933
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovieJava/Listings/src_createmovies_NumberPainter_java.html
archived_at: '2026-07-18T03:05:13.947861Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovieJava](CreateMovieJava.md)


[Next](Document%20Revision%20History.md)[Previous](src-CreateMovie.java.md)

# src/createmovies/NumberPainter.java

```
/*
 * QuickTime for Java SDK Sample Code

   Usage subject to restrictions in SDK License Agreement
 * Copyright: © 1996-1999 Apple Computer, Inc.

 */
package createmovies;

import java.awt.*;
import quicktime.app.image.*;
/**
 * One based frame counting
 */
public class NumberPainter implements Paintable {
    public NumberPainter (int n) {
        numFrames = n;
    }

    private int width, height;
    private int numFrames;
    private int loopslot = 1;
    private int topInset, leftInset;
    private Font theFont = new Font (new String("Courier"), Font.PLAIN, 48);
    private boolean firstTime;
    private Rectangle[] ret = new Rectangle[1];
    private Rectangle dirtyDrawRect;
    /**
     * Returns the number of images
     */
    public int getNumberOfFrames () { return numFrames; }

    public void setCurrentFrame (int frame) {
        loopslot = frame;
        if (loopslot < 1) loopslot = 1;
        if (loopslot > numFrames) loopslot = numFrames;
    }

    /** 
     * Sets the current frame - zero based
     */
    public int getCurrentFrame () {
        return numFrames;
    }

    /**
     * The Parent object of the Paintable tell the paintable object the size of its available
     * drawing surface. Any drawing done outside of these bounds (originating at 0,0) will
     * be clipped.
     */
    public void newSizeNotified (QTImageDrawer drawer, Dimension d) {
        width = d.width;
        height = d.height;
        dirtyDrawRect = new Rectangle(width/2 - 25, height/2 - 20, 64, 44);
        ret[0] = new Rectangle (width, height);
        firstTime = true;
    }

    /**
     * Paint on the graphics. The supplied component is the component from which
     * the graphics object was derived or related to and is also the component
     * that is the object that paint was called upon that has called this method.
     * The Graphics object is what you should paint on.
     * This maybe an on or off screen graphics.
     * You should not cache this graphics object as it can be different
     * between different calls.
     * @param comp the component from which the Graphics object was derived or 
     * related too.
     * @param g the graphics to paint on.
     */
    public Rectangle[] paint (Graphics g) {
        if (firstTime) {
            g.setColor (Color.red);
            g.fillRect (0, 0, width, height);

            g.setColor (Color.green);
            g.fillRect (0, 0, 8, 8);
            g.fillRect (width - 8, 0, 8, 8);
            g.fillRect (0, height - 8, 8, 8);
            g.fillRect (width - 8, height - 8, 8, 8);
        }

        g.setColor (Color.red);
        g.fillRect (dirtyDrawRect.x, dirtyDrawRect.y, dirtyDrawRect.width, dirtyDrawRect.height);
        g.setColor (Color.blue);
        g.setFont (theFont);        
        g.drawString (String.valueOf (loopslot), width/2 - 25, height/2 + 20);

        if (firstTime)
            firstTime = false;  //we have done the first time now don't do it again
        else
            ret[0] = dirtyDrawRect; 
        return ret;
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](src-CreateMovie.java.md)

