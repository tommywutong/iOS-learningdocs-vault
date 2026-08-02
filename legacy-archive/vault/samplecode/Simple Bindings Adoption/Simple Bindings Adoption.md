---
title: Simple Bindings Adoption
apple_id: DTS10004326
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2014-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleBindingsAdoption/Introduction/Intro.html
archived_at: '2026-07-18T03:23:53.826795Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Simple Bindings Adoption

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-07-08 Upgrade for Xcode 5.0, OS X 10.9, now uses ARC (Automatic Reference Counting) and properties, document now reads and writes volume setting. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzsgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.0, OS X 10.9 or later |
| __Runtime Requirements:__ | OS X 10.7 or later |

This simple example illustrates the adoption of Cocoa Bindings to manage synchronization of values between models and views.

The example is a simple document-based application. Each document has a window with a text field, slider, and button. The values of the text field and slider represent the volume in a Track object managed by the document. The Mute button sets the volume to zero.

There are three versions of the application:

1. Using target-action to update the track's volume when the user presses Enter in the text field or moves the slider. The user interface is updated programmatically.

2. Programmatically: creating an object controller; binding its content to the track object; and binding the values of the text field and slider to the track's volume. The user interface is updated using bindings.

3. In Interface Builder: creating an object controller; binding its content to the track object; and binding the values of the text field and slider to the track's volume. The user interface is updated using bindings.

[Next](ReadMe.txt.md)

