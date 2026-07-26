---
title: 'CFRunLoopTimerDoesRepeat(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunlooptimerdoesrepeat(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimerdoesrepeat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimerdoesrepeat%28_%3A%29.json'
content_hash: 'sha256:ea86c104a927d6b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimerDoesRepeat(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFRunLoopTimer object repeats.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopTimerDoesRepeat(_ timer: CFRunLoopTimer!) -> Bool
```

## Parameters

- `timer` — The run loop timer to test.

## Return Value

`true` if `timer` repeats, or has a periodicity; otherwise `false`.

## See Also

### CFRunLoopTimer Miscellaneous Functions

- [CFRunLoopTimerCreateWithHandler](<cfrunlooptimercreatewithhandler(____________).md>) — Creates a new CFRunLoopTimer object with a block-based handler.
- [CFRunLoopTimerCreate](<cfrunlooptimercreate(______________).md>) — Creates a new CFRunLoopTimer object with a function callback.
- [CFRunLoopTimerGetContext](<cfrunlooptimergetcontext(____).md>) — Returns the context information for a CFRunLoopTimer object.
- [CFRunLoopTimerGetInterval](<cfrunlooptimergetinterval(__).md>) — Returns the firing interval of a repeating CFRunLoopTimer object.
- [CFRunLoopTimerGetNextFireDate](<cfrunlooptimergetnextfiredate(__).md>) — Returns the next firing time for a CFRunLoopTimer object.
- [CFRunLoopTimerGetOrder](<cfrunlooptimergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopTimer object.
- [CFRunLoopTimerGetTypeID](<cfrunlooptimergettypeid().md>) — Returns the type identifier of the CFRunLoopTimer opaque type.
- [CFRunLoopTimerInvalidate](<cfrunlooptimerinvalidate(__).md>) — Invalidates a CFRunLoopTimer object, stopping it from ever firing again.
- [CFRunLoopTimerIsValid](<cfrunlooptimerisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [CFRunLoopTimerSetNextFireDate](<cfrunlooptimersetnextfiredate(____).md>) — Sets the next firing date for a CFRunLoopTimer object .
