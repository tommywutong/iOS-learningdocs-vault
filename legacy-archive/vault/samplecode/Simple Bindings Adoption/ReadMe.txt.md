---
title: Simple Bindings Adoption
apple_id: DTS10004326
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2014-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleBindingsAdoption/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:53.856488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple Bindings Adoption](Simple%20Bindings%20Adoption.md)


[Next](SimpleBindingsAdoption01-main.m.md)[Previous](Simple%20Bindings%20Adoption.md)

# ReadMe.txt

```
Simple Bindings Adoption
------------------------

This simple example illustrates the adoption of Cocoa Bindings to manage synchronization of values between models and views.

The example is a simple document-based application.  Each document has a window with a text field, slider, and button.  The values of the text field and slider represent the volume in a Track object managed by the document.  The Mute button sets the volume to zero.

There are three versions of the application:

1. Using target-action to update the track's volume when the user presses Enter in the text field or moves the slider.  The user interface is updated programmatically.

2. Programmatically: creating an object controller; binding its content to the track object; and binding the values of the text field and slider to the track's volume.  The user interface is updated using bindings.

3. In Interface Builder: creating an object controller; binding its content to the track object; and binding the values of the text field and slider to the track's volume.  The user interface is updated using bindings.


Sample Requirements
========================================================
The supplied Xcode project was created using Xcode v5.0 running under Mac OS X 10.9 or later.


Copyright © 2007-2014 Apple Inc. All rights reserved.
```

[Next](SimpleBindingsAdoption01-main.m.md)[Previous](Simple%20Bindings%20Adoption.md)

