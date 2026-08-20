---
title: Sproing
apple_id: DTS10000408
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-08-24'
source_url: https://developer.apple.com/library/archive/samplecode/Sproing/Listings/README_txt.html
archived_at: '2026-07-18T03:25:29.119777Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Sproing](Sproing.md)


[Next](Sproing-Controller.h.md)[Previous](Sproing.md)

# README.txt

```
Sproing
=======

ABOUT:

Sproing is a Cocoa application which shows how "springs" work to control view resizing when a window (or, more generally, a parent view) resizes. You can use it to explore springs by seeing what they do, to generate the code for a particular set of springs, or to encode or decode springs in hex.

Using the application

Learning about springs
* Resize the Sproing window. Notice how the box inside it expands, keeping constant "margins" on all sides.
* Click on the lines or springs in the Info window to change the spring settings for the box. Now resize the Sproing window again. Notice how the box inside it reacts differently, because you've changed the springs.
* If you get tired of going back and forth between windows, changing springs in one window and then resizing the other, check the “Animate window resize” box to make the window "resize" by itself.
* If the Sproing window's box gets off-center, click Re-center to put it back.

More details
* Click "Geeky stuff" to show more details in a drawer.
* This shows you the bits for the current mask, in hexadecimal.
* You can type in your own mask (with or without the leading "0x") to set the springs. This can be a handy way to decode a mask you obtain during debugging.
* The code to programmatically set the current mask also appears in the drawer. You can copy this and paste it into your code, for the rare occasions when you want to control springs dynamically instead of just using what you load from a nib.
* The "Flipped Coordinates" checkbox controls whether the view being resized is within a flipped view (origin at the top left) or non-flipped (origin at bottom left).
* Notice that flipping the coordinates affects the autoresizing mask only if the springs include the top or bottom spring, but not both. In other words, it swaps NSViewMinYMargin and NSViewMaxYMargin, but doesn't change anything else.

Inside the application

This application tries to be a useful tool for writing spring-related code as well as a source code example, so it has a little more complexity than is needed just to illustrate the function of springs.

If you would like to concentrate on just the spring-demonstrating functionality inside the application (this is not code which you would use in a typical AppKit application), the following methods in Controller.m may provide more insight than most:
    getAutoresizingMaskForButton:isFlipped:
    getAutoresizingMaskForFlipped:
    getAutoresizingMask
    installAutoresizingMask:
    symbolsForMask:
    controlTextDidChange:


About springs in the AppKit

For more information about springs and resizing, see "Autoresizing of Subviews" under "Moving and Resizing a View" in the programming topic Drawing and Views.

Keep in mind that if you create views and set springs programmatically, you should send setAutoresizesSubviews: to the view's superview. If you don't, the springs on your view have no effect.

===========================================================================
BUILD REQUIREMENTS:

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X 10.6 Snow Leopard or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.1
- Fixed an issue with automatic animation with 64-bit builds.
- Project updated for Xcode 4.
Version 1.0
- First version.

===========================================================================
Copyright (C) 2003-2011 Apple Inc. All rights reserved.
```

[Next](Sproing-Controller.h.md)[Previous](Sproing.md)

