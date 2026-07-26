---
title: 'CFRunLoopSourceSignal(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopsourcesignal(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcesignal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcesignal%28_%3A%29.json'
content_hash: 'sha256:fc67cd48ff44ce41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceSignal(_:)

<sub>Function</sub>

Signals a CFRunLoopSource object, marking it as ready to fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopSourceSignal(_ source: CFRunLoopSource!)
```

## Parameters

- `source` — The run loop source to signal.

## Discussion

This function has no effect on version 1 sources, which are automatically handled when Mach messages arrive for them. After signaling a version 0 source, you need to call [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) on one of the run loops in which the source is registered to get the source handled immediately.

## See Also

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) — Creates a CFRunLoopSource object.
- [CFRunLoopSourceGetContext](<cfrunloopsourcegetcontext(____).md>) — Returns the context information for a CFRunLoopSource object.
- [CFRunLoopSourceGetOrder](<cfrunloopsourcegetorder(__).md>) — Returns the ordering parameter for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceInvalidate](<cfrunloopsourceinvalidate(__).md>) — Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [CFRunLoopSourceIsValid](<cfrunloopsourceisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
