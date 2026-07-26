---
title: 'CFRunLoopSourceIsValid(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopsourceisvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourceisvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourceisvalid%28_%3A%29.json'
content_hash: 'sha256:81c28bc1076e9582'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceIsValid(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopSourceIsValid(_ source: CFRunLoopSource!) -> Bool
```

## Parameters

- `source` — The run loop source to examine.

## Return Value

`true` if `source` is valid, otherwise `false`.

## See Also

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) — Creates a CFRunLoopSource object.
- [CFRunLoopSourceGetContext](<cfrunloopsourcegetcontext(____).md>) — Returns the context information for a CFRunLoopSource object.
- [CFRunLoopSourceGetOrder](<cfrunloopsourcegetorder(__).md>) — Returns the ordering parameter for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceInvalidate](<cfrunloopsourceinvalidate(__).md>) — Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) — Signals a CFRunLoopSource object, marking it as ready to fire.
