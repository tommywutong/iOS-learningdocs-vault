---
title: 'CFRunLoopTimerIsValid(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunlooptimerisvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimerisvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimerisvalid%28_%3A%29.json'
content_hash: 'sha256:2ea03cb0d742beb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimerIsValid(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopTimerIsValid(_ timer: CFRunLoopTimer!) -> Bool
```

## Parameters

- `timer` — The run loop timer to examine.

## Return Value

`true` if `timer` is valid; otherwise `false`.

## Discussion

A non-repeating timer is automatically invalidated after it fires.

## See Also

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
- [CFRunLoopTimerSetNextFireDate](<cfrunlooptimersetnextfiredate(____).md>) — Sets the next firing date for a CFRunLoopTimer object .
