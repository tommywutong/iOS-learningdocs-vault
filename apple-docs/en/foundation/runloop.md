---
title: RunLoop
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop
source_url: 'https://developer.apple.com/documentation/foundation/runloop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop.json'
content_hash: 'sha256:9272539db131f596'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# RunLoop

<sub>Class</sub>

The programmatic interface to objects that manage input sources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class RunLoop
```

## Overview

A [RunLoop](runloop.md) object processes input for sources, such as mouse and keyboard events from the window system and [Port](port.md) objects. A [RunLoop](runloop.md) object also processes [Timer](timer.md) events.

Your application neither creates nor explicitly manages [RunLoop](runloop.md) objects. The system creates a [RunLoop](runloop.md) object as needed for each [Thread](thread.md) object, including the application’s main thread. If you need to access the current thread’s run loop, use the class method [currentRunLoop](runloop/current.md).

Note that from the perspective of [RunLoop](runloop.md), [Timer](timer.md) objects aren’t “input”—they’re a special type, and they don’t cause the run loop to return when they fire.

> [!warning] Warning
> The [RunLoop](runloop.md) class is generally not thread-safe, and you must call its methods only within the context of the current thread. Don’t call the methods of a [RunLoop](runloop.md) object running in a different thread, which might cause unexpected results.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Scheduler](../combine/scheduler.md)

## Topics

### Accessing Run Loops and Modes

- [currentRunLoop](runloop/current.md) — Returns the run loop for the current thread.
- [currentMode](runloop/currentmode.md) — The receiver’s current input mode.
- [- limitDateForMode:](<runloop/limitdate(formode_).md>) — Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [mainRunLoop](runloop/main.md) — Returns the run loop of the main thread.
- [- getCFRunLoop](<runloop/getcfrunloop().md>) — Returns the receiver’s underlying run loop object.
- [Mode](runloop/mode.md) — Modes that a run loop operates in.

### Managing Timers

- [- addTimer:forMode:](<runloop/add(__formode_)-392ag.md>) — Registers a given timer with a given input mode.

### Managing Ports

- [- addPort:forMode:](<runloop/add(__formode_)-6z982.md>) — Adds a port as an input source to the specified mode of the run loop.
- [- removePort:forMode:](<runloop/remove(__formode_).md>) — Removes a port from the specified input mode of the run loop.

### Running a Loop

- [- run](<runloop/run().md>) — Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
- [- runMode:beforeDate:](<runloop/run(mode_before_).md>) — Runs the loop once, blocking for input in the specified mode until a given date.
- [- runUntilDate:](<runloop/run(until_).md>) — Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [- acceptInputForMode:beforeDate:](<runloop/acceptinput(formode_before_).md>) — Runs the loop once or until the specified date, accepting input only for the specified mode.

### Scheduling and Canceling Tasks

- [- performBlock:](<runloop/perform(__).md>) — Schedules a block that the run loop invokes.
- [- performInModes:block:](<runloop/perform(inmodes_block_).md>) — Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [- performSelector:target:argument:order:modes:](<runloop/perform(__target_argument_order_modes_).md>) — Schedules the sending of a message on the receiver.
- [- cancelPerformSelector:target:argument:](<runloop/cancelperform(__target_argument_).md>) — Cancels the sending of a previously scheduled message.
- [- cancelPerformSelectorsWithTarget:](<runloop/cancelperformselectors(withtarget_).md>) — Cancels all outstanding ordered performs scheduled with a given target.

### Scheduling Combine Publishers

- [schedule(options:_:)](<runloop/schedule(options___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [schedule(after:tolerance:options:_:)](<runloop/schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, using the specified tolerance and options.
- [schedule(after:interval:tolerance:options:_:)](<runloop/schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [minimumTolerance](runloop/minimumtolerance.md) — The minimum tolerance the run loop scheduler allows.
- [now](runloop/now.md) — The run loop scheduler’s definition of the current moment in time.
- [SchedulerTimeType](runloop/schedulertimetype.md) — The scheduler time type that the run loop uses.
- [SchedulerOptions](runloop/scheduleroptions.md) — A set of options that affect the operation of the run loop scheduler.

### Default Implementations

- [Scheduler Implementations](runloop/scheduler-implementations.md)

## See Also

### Run Loop Scheduling

- [Timer](timer.md) — A timer that fires after a certain time interval has elapsed, sending a specified message to a target object.
