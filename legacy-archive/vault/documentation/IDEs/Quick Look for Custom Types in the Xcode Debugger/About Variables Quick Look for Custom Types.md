---
title: Quick Look for Custom Types in the Xcode Debugger
apple_id: TP40014001
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/CustomClassDisplay_in_QuickLook/Introduction/Introduction.html
archived_at: '2026-07-15T07:41:25.366396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Enabling%20Quick%20Look%20for%20Custom%20Types.md)

# About Variables Quick Look for Custom Types

The debugger in Xcode includes the variables Quick Look feature, a way to view variables in your app by displaying their contents graphically in a pop-up display. Quick Look lets you display a graphical rendering of object contents by pressing the Space bar with a variable selected in the debugger variables view.

The Xcode 5 debugger gave you the ability to dynamically visualize selected operating system class types with the variables Quick Look feature. This document addresses two important enhancements to this capability that were introduced with Xcode 5.1:

- Variables instantiated from your custom types can render a Quick Look display.
- Additional operating system classes now support Quick Look display.

Together these two enhancements provide flexibilty in how you display your variables when debugging. To provide your custom class with a Quick Look display in the debugger, you provide a method for Quick Look to use in the object class. The method, called by Xcode, returns an object with a type matching one of the operating system classes supported by Quick Look display.

A customized Quick Look method for each of your custom object classes can be implemented, each rendering a live representation of the underlying variable in the way that makes best sense for the type. For example, a `Person` object could show an image of the person, or perhaps a map with a pin on a person’s home address, whichever is relevant to the implementation of the custom class in your context. You choose the operating system object type to return depending upon what best fits a rendering of your custom class objects.

Apple provides the following video presentations that show more about using the Xcode debugger:

- [WWDC 2014: Debugging with Xcode 6](https://developer.apple.com/videos/wwdc/2014/#413): Learn how apps enqueue work, explore and fix user interfaces, add custom Quick Look support.
- [WWDC 2013: Debugging with Xcode](https://developer.apple.com/wwdc/videos/?id=407): Detect and fix performance problems using the Xcode graphical debugger.
- [WWDC 2013: Advanced Debugging with LLDB](https://developer.apple.com/wwdc/videos/?id=413): Debug using Terminal and the Xcode graphical debugger.
[Next](Enabling%20Quick%20Look%20for%20Custom%20Types.md)

