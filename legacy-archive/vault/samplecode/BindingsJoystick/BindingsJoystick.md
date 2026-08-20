---
title: BindingsJoystick
apple_id: DTS10003684
resource_type: Sample Code
platform: macOS
topic: General
technology: AppKit
published: '2012-04-09'
source_url: https://developer.apple.com/library/archive/samplecode/BindingsJoystick/Introduction/Intro.html
archived_at: '2026-07-18T03:01:53.344233Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# BindingsJoystick

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2012-04-09 Updated project to Xcode 4.4; now uses ARC. Moved the unbinding code from dealloc to viewWillMoveToSuperview: and updated to use -infoForBinding:. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrygqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.4, OS X v10.8. |
| __Runtime Requirements:__ | OS X v10.7. |

This sample contains a "joystick" view that shows how you can implement a bindings-enabled subclass of NSView.

In addition to supporting basic binding for a sigle value, it responds properly to multiple selection markers. It is discussed in greater detail in "Cocoa Bindings Programming Topics > How Do Bindings Work?" (http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/HowDoBindingsWork.html).

User Interface -------------- The user interface is contained in MainMenu.xib. The main objects instantiated in the nib file are: \* A window that contains - A table view to display Position objects. - A Joystick view. - Text fields to display and edit angle and offset values of the currently-selected Position object. \* An instance of AppController to manage the view and a collection of Position objects. \* An array controller for the App Controller's Position objects.

Classes ------- The classes used in the sample are as follows:

AppController: A simple controller object that manages a collection of Position objects containing offset and angle values. It is also responsible for establishing the bindings from the joystick view to the array controller.

JoystickView: The main focus of the sample: A view that displays the angle and offset of an object, and allows those values to be edited graphically. These features also support bindings.

Position: A trivial model class to encapsulate an angle and an offset.

[Next](ReadMe.txt.md)

