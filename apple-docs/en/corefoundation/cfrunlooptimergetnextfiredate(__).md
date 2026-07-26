---
title: 'CFRunLoopTimerGetNextFireDate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunlooptimergetnextfiredate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimergetnextfiredate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimergetnextfiredate%28_%3A%29.json'
content_hash: 'sha256:1c85c011de20260d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimerGetNextFireDate(_:)

<sub>Function</sub>

Returns the next firing time for a CFRunLoopTimer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopTimerGetNextFireDate(_ timer: CFRunLoopTimer!) -> CFAbsoluteTime
```

## Parameters

- `timer` — The run loop timer to examine.

## Return Value

The next firing time for `timer`. This time could be a date in the past if a run loop has not been able to process the timer since the firing time arrived.

## See Also

### CFRunLoopTimer Miscellaneous Functions

- [CFRunLoopTimerCreateWithHandler](<cfrunlooptimercreatewithhandler(____________).md>) — Creates a new CFRunLoopTimer object with a block-based handler.
- [CFRunLoopTimerCreate](<cfrunlooptimercreate(______________).md>) — Creates a new CFRunLoopTimer object with a function callback.
- [CFRunLoopTimerDoesRepeat](<cfrunlooptimerdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopTimer object repeats.
- [CFRunLoopTimerGetContext](<cfrunlooptimergetcontext(____).md>) — Returns the context information for a CFRunLoopTimer object.
- [CFRunLoopTimerGetInterval](<cfrunlooptimergetinterval(__).md>) — Returns the firing interval of a repeating CFRunLoopTimer object.
- [CFRunLoopTimerGetOrder](<cfrunlooptimergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopTimer object.
- [CFRunLoopTimerGetTypeID](<cfrunlooptimergettypeid().md>) — Returns the type identifier of the CFRunLoopTimer opaque type.
- [CFRunLoopTimerInvalidate](<cfrunlooptimerinvalidate(__).md>) — Invalidates a CFRunLoopTimer object, stopping it from ever firing again.
- [CFRunLoopTimerIsValid](<cfrunlooptimerisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [CFRunLoopTimerSetNextFireDate](<cfrunlooptimersetnextfiredate(____).md>) — Sets the next firing date for a CFRunLoopTimer object .
