---
title: QTButtonDemo
apple_id: DTS10000978
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTButtonDemo/Listings/README_txt.html
archived_at: '2026-07-18T03:20:00.558330Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTButtonDemo](QTButtonDemo.md)


[Next](src-QTButtonDemo.java.md)[Previous](QTButtonDemo.md)

# README.txt

```
=============================================================================
QuickTime for Java SDK                              Updated: 17 Sept 1999

Read Me Notes to "QTButtonDemo" Demo and Sample Code

=============================================================================
This demo program shows how to use the quicktime.ui Package classes. These classes demonstrate the usage of QTJava for making Custom UI elements. This demo shows the custom button classes of QTJava.

=============================================================================
The minimum runtime requirements for this Sample Code are:

- Common
    - Sun Compliant Java Runtime Environment 1.1
    - QuickTime 3 Streaming for URL DataRefs
    - QTJava.zip

- MacOS:
    - System 8 or later
    - Macintosh Runtime for Java (MRJ) 2.1

- Mac OS X
    - 10.0 or later

- Windows 95, 98, NT, 2000 or XP.
    - JRE/JDK from Sun Microsystems, Inc. recommended

=============================================================================
Media requirements for this Sample Code:

(1) QuickTime movie files of the user's choice

=============================================================================
Notes & Comments

The user is shown a dialog box to choose a movie. This movie is then presented to the user in a frame .
The movies are embedded in a compositor which is added as a client to the QTCanvas. Two buttons are added to the compositor. A Release action button and a Press action button.
The release action button upon activation starts playing the movie and again on activation stops the current movie.
The PressAction button upon activation starts playing the movie in the reverse direction and plays until the mousebutton is released or the mouse moves out of the button.
Both the buttons display a different image upon activation. User can use images instead as input to the QTButton classes.

=============================================================================
General Comments

- QTSession.open and close:

A QTSession.open will perform a gestalt check to ensure that QuickTime is present and is initialized. This is a required call before any QuickTime Java classes can be used.

When the user closes the window the program will quit, first calling QTSession.close to terminate QuickTime. It is necessary for programs to call QTSession.close if they have previously called QTSession.open in order to shut down QuickTime properly.


=============================================================================

QuickTime and QuickTime for Java are trademarks of Apple Computer, Inc.
(c) 1998 Apple Computer Inc. All rights reserved.
```

[Next](src-QTButtonDemo.java.md)[Previous](QTButtonDemo.md)

