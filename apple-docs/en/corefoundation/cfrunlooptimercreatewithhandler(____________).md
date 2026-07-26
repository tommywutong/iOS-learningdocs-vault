---
title: 'CFRunLoopTimerCreateWithHandler(_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunlooptimercreatewithhandler(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimercreatewithhandler(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimercreatewithhandler%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:93ff6fe746a7fa4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimerCreateWithHandler(_:_:_:_:_:_:)

<sub>Function</sub>

Creates a new CFRunLoopTimer object with a block-based handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopTimerCreateWithHandler(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ block: ((CFRunLoopTimer?) -> Void)!) -> CFRunLoopTimer!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `fireDate` — The time at which the timer should first fire. The fine precision (sub-millisecond at most) of the fire date may be adjusted slightly by the timer if there are implementation reasons to do so.

- `interval` — The firing interval of the timer. If `0` or negative, the timer fires once and then is automatically invalidated. The fine precision (sub-millisecond at most) of the interval may be adjusted slightly by the timer if implementation reasons to do so exist.

- `flags` — Currently ignored. Pass `0` for future compatibility.

- `order` — A priority index indicating the order in which run loop timers are processed. Run loop timers currently ignore this parameter. Pass `0`.

- `block` — The block invoked when the timer fires. The block takes one argument: - **`timer`** — The run loop timer that is firing.

## Return Value

The new CFRunLoopTimer object. Ownership follows the Create Rule described in [Ownership Policy](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148).

## Discussion

A timer needs to be added to a run loop mode before it will fire. To add the timer to a run loop, use [CFRunLoopAddTimer](<cfrunloopaddtimer(______).md>). A timer can be registered to only one run loop at a time, although it can be in multiple modes within that run loop.

## See Also

### CFRunLoopTimer Miscellaneous Functions

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
