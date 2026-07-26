---
title: CFRunLoopTimer
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooptimer
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimer.json'
content_hash: 'sha256:80f79b05dd2ca4b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimer

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFRunLoopTimer
```

## Overview

A CFRunLoopTimer object represents a specialized run loop source that fires at a preset time in the future. Timers can fire either only once or repeatedly at fixed time intervals. Repeating timers can also have their next firing time manually adjusted.

A timer is not a real-time mechanism; it fires only when one of the run loop modes to which the timer has been added is running and able to check if the timer’s firing time has passed. If a timer’s firing time occurs while the run loop is in a mode that is not monitoring the timer or during a long callout, the timer does not fire until the next time the run loop checks the timer. Therefore, the actual time at which the timer fires potentially can be a significant period of time after the scheduled firing time.

A repeating timer reschedules itself based on the scheduled firing time, not the actual firing time. For example, if a timer is scheduled to fire at a particular time and every 5 seconds after that, the scheduled firing time will always fall on the original 5 second time intervals, even if the actual firing time gets delayed. If the firing time is delayed so far that it passes one or more of the scheduled firing times, the timer is fired only once for that time period; the timer is then rescheduled, after firing, for the next scheduled firing time in the future.

Each run loop timer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

CFRunLoopTimer is “toll-free bridged” with its Cocoa Foundation counterpart, [Timer](../foundation/timer.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSTimer *` parameter, you can pass in a `CFRunLoopTimerRef`, and in a function where you see a `CFRunLoopTimerRef` parameter, you can pass in an `NSTimer` instance. This also applies to concrete subclasses of `NSTimer`. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFRunLoopTimer Miscellaneous Functions

- [CFRunLoopTimerCreateWithHandler](<cfrunlooptimercreatewithhandler(____________).md>) — Creates a new CFRunLoopTimer object with a block-based handler.
- [CFRunLoopTimerCreate](<cfrunlooptimercreate(______________).md>) — Creates a new CFRunLoopTimer object with a function callback.
- [CFRunLoopTimerDoesRepeat](<cfrunlooptimerdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopTimer object repeats.
- [CFRunLoopTimerGetContext](<cfrunlooptimergetcontext(____).md>) — Returns the context information for a CFRunLoopTimer object.
- [CFRunLoopTimerGetInterval](<cfrunlooptimergetinterval(__).md>) — Returns the firing interval of a repeating CFRunLoopTimer object.
- [CFRunLoopTimerGetNextFireDate](<cfrunlooptimergetnextfiredate(__).md>) — Returns the next firing time for a CFRunLoopTimer object.
- [CFRunLoopTimerGetOrder](<cfrunlooptimergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopTimer object.
- [CFRunLoopTimerGetTypeID](<cfrunlooptimergettypeid().md>) — Returns the type identifier of the CFRunLoopTimer opaque type.
- [CFRunLoopTimerInvalidate](<cfrunlooptimerinvalidate(__).md>) — Invalidates a CFRunLoopTimer object, stopping it from ever firing again.
- [CFRunLoopTimerIsValid](<cfrunlooptimerisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [CFRunLoopTimerSetNextFireDate](<cfrunlooptimersetnextfiredate(____).md>) — Sets the next firing date for a CFRunLoopTimer object .

### Callbacks

- [CFRunLoopTimerCallBack](cfrunlooptimercallback.md) — Callback invoked when a CFRunLoopTimer object fires.

### Data Types

- [CFRunLoopTimerContext](cfrunlooptimercontext.md) — A structure that contains program-defined data and callbacks with which you can configure a CFRunLoopTimer’s behavior.

## See Also

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
