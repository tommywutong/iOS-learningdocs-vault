---
title: Run Loops
apple_id: 10000135i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFRunLoops/Concepts/InputModes.html
archived_at: '2026-07-15T07:22:48.511777Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Running%20the%20Run%20Loop.md)[Previous](About%20Run%20Loops.md)

# Input Modes

Each run loop can have different modes, each identified with an arbitrary string name, in which it can run. Each mode has its own set of sources, timers, and observers associated with it. A run loop is run—in a named mode—to have it monitor the objects that have been registered in that mode. Examples of modes include the default mode, which a process would normally spend most of its time in, and a modal panel mode, which might be run when a modal panel is up, to restrict the set of input sources that are allowed to “fire.” Modes do not provide the granularity of, for example, what type of user input events are interesting, however. That sort of finer-grained granularity is given by higher-level frameworks, such as Cocoa and Carbon, with “get next event matching mask” or similar functionality.

To receive callbacks when a run loop source, timer, or observer needs processing, you must first place the object into a run loop mode, using the appropriate `CFRunLoopAdd...` function. You can later remove an object from a run loop mode, using the appropriate `CFRunLoopRemove...` function or by invalidating the object, to stop receiving its callback.

Core Foundation defines a default mode to hold objects that should be monitored while the application (or thread) is sitting idle. For example, Carbon and Cocoa applications place run loop sources for user events into this mode of their main thread’s run loop. You access this default mode using the `kCFRunLoopDefaultMode` constant for the mode name. Additional modes are created automatically when an object is added to an unrecognized mode.

Each run loop has its own independent set of modes. Multiple run loops can have modes with the same name, but they do not share the objects placed into them. In fact, every run loop has a default mode named with the `kCFRunLoopDefaultMode` constant, but each can, and usually will, have different sets of objects in them.

Core Foundation also defines a special pseudo-mode to hold objects that should be shared by a set of “common” modes. Common modes are a set of run loop modes for which you can define a set of sources, timers, and observers that are shared by these modes. Instead of registering a source, for example, to each specific run loop mode, you can register it once to the run loop’s common pseudo-mode and the source will be automatically registered in each run loop mode in the common mode set. The default mode, `kCFRunLoopDefaultMode`, is always a member of the set of common modes. Additional modes are added to the set of common modes by calling the `CFRunLoopAddCommonMode` function.

Objects are added and removed from a run loop’s common pseudo-mode the same as a regular mode; you merely use the `kCFRunLoopCommonModes` constant for the mode name. To monitor these objects, however, you do not then run the run loop in the common pseudo-mode. You instead run the run loop in one of modes that is a member of the set of common modes. The `kCFRunLoopCommonModes` constant is never passed to the `CFRunLoopRunInMode` function.

Each run loop has its own independent list of modes that are in the set of common modes. Adding a mode to one run loop’s set of common modes does not add it to every run loop’s set, even when other run loops have a mode with the same name.

[Next](Running%20the%20Run%20Loop.md)[Previous](About%20Run%20Loops.md)

