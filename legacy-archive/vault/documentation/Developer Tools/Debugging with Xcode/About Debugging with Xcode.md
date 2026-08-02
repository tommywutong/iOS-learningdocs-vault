---
title: Debugging with Xcode
apple_id: TP40015022
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/about_debugging_w_xcode.html
archived_at: '2026-07-27T06:57:09.304293Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Quick%20Start.md)

# About Debugging with Xcode

Finding and eliminating problems in your code is a critical part of the development process. The Xcode debugger is preset with useful features for general purpose debugging and runs automatically when your app is launched. The debugger helps you:

- Identify and locate the problem
- Examine the control flow and data structures of running code to find the cause
- Devise a solution and edit your code accordingly
- Run the revised app and confirm that the fix works

## Prerequisites

You should be familiar with app design and programming concepts. Some familiarity with Xcode is also recommended; see _[Xcode Overview](../../Tools%20Languages/Xcode%20Overview/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjv)_.

## See Also

Every year, several sessions at the Apple Worldwide Developer Conference are devoted to debugging that expand upon the material in this guide and add to it with useful techniques. These sessions are available for you in the Apple developer libraries at the [Apple Developer website](https://developer.apple.com) and are easy to find by filtering on “debug.”

The following recent WWDC presentations focus on using the Xcode debugger and related tools:

- [WWDC 2013: Debugging with Xcode](https://developer.apple.com/videos/wwdc/2013/?include=407#407): Detect and fix performance problems using the Xcode graphical debugger.
- [WWDC 2013: Advanced Debugging with LLDB](https://developer.apple.com/videos/wwdc/2013/?include=413#413): Debug using Terminal and the Xcode graphical debugger.
- [WWDC 2014: Debugging with Xcode 6](https://developer.apple.com/videos/wwdc/2014/?include=413#413): Learn how apps enqueue work, explore and fix user interfaces, add custom Quick Look support.
- [WWDC 2015: Advanced Debugging and the Address Sanitizer](https://developer.apple.com/videos/wwdc/2015/?id=413): Learn how to use advanced breakpoint actions to explore and fix your app, and see how the Address Sanitizer finds memory corruption bugs at run time.
- [WWDC 2016: Visual Debugging with Xcode](https://developer.apple.com/videos/play/wwdc2016/410/): Discover new enhancements for debugging autolayout issues at run time, how issues inside complex objects can be easily debugged, and see how the enhanced FPS gauge find bottlenecks with SpriteKit and SceneKit apps. Find and fix leaked or abandoned memory from within your debugging workflow with memory graph debugging.
- [WWDC 2016: Thread Sanitizer and Static Analysis](https://developer.apple.com/videos/play/wwdc2016/412/): Learn how to use the Thread Sanitizer to find data races and other concurrency bugs. See how the static analyzer can now search for localizability issues, check nullability, and find memory leaks.

A good primer on debugging in general is _The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems_ by David J. Agans.

[Next](Quick%20Start.md)
