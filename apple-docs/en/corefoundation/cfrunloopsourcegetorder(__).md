---
title: 'CFRunLoopSourceGetOrder(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopsourcegetorder(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcegetorder(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcegetorder%28_%3A%29.json'
content_hash: 'sha256:d6727ffaca2577bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceGetOrder(_:)

<sub>Function</sub>

Returns the ordering parameter for a CFRunLoopSource object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopSourceGetOrder(_ source: CFRunLoopSource!) -> CFIndex
```

## Parameters

- `source` — The run loop source to examine.

## Return Value

The ordering parameter for `source`, which the run loop uses (for version 0 sources only) to determine the order in which sources are processed when multiple sources are firing.

## See Also

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) — Creates a CFRunLoopSource object.
- [CFRunLoopSourceGetContext](<cfrunloopsourcegetcontext(____).md>) — Returns the context information for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceInvalidate](<cfrunloopsourceinvalidate(__).md>) — Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [CFRunLoopSourceIsValid](<cfrunloopsourceisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) — Signals a CFRunLoopSource object, marking it as ready to fire.
