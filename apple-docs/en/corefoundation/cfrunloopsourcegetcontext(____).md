---
title: 'CFRunLoopSourceGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopsourcegetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcegetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcegetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:3748de0d0da4d571'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceGetContext(_:_:)

<sub>Function</sub>

Returns the context information for a CFRunLoopSource object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopSourceGetContext(_ source: CFRunLoopSource!, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>!)
```

## Parameters

- `source` — The run loop source to examine.

- `context` — A pointer to the structure into which the context information for `source` is to be copied. The information being returned is the same information passed to [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) when creating `source`.

## Discussion

Run loop sources come in two versions with different-sized context structures. `context` must point to the correct version of the structure for `source`. Before calling this function, you need to initialize the `version` member of `context` with the version number (either 0 or 1) of `source`.

## See Also

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) — Creates a CFRunLoopSource object.
- [CFRunLoopSourceGetOrder](<cfrunloopsourcegetorder(__).md>) — Returns the ordering parameter for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceInvalidate](<cfrunloopsourceinvalidate(__).md>) — Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [CFRunLoopSourceIsValid](<cfrunloopsourceisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) — Signals a CFRunLoopSource object, marking it as ready to fire.
