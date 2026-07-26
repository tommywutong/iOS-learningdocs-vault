---
title: 'CFRunLoopSourceInvalidate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopsourceinvalidate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourceinvalidate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourceinvalidate%28_%3A%29.json'
content_hash: 'sha256:8d61e0bf660e3fac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceInvalidate(_:)

<sub>Function</sub>

Invalidates a CFRunLoopSource object, stopping it from ever firing again.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopSourceInvalidate(_ source: CFRunLoopSource!)
```

## Parameters

- `source` — The run loop source to invalidate.

## Discussion

Once invalidated, `source` will never fire and call its perform callback function again. This function automatically removes `source` from all the run loop modes in which it was registered. If `source` is a version 0 source, this function calls its `cancel` callback function as it is removed from each run loop mode. The memory for `source` is not deallocated unless the run loop held the only reference to `source`.

## See Also

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) — Creates a CFRunLoopSource object.
- [CFRunLoopSourceGetContext](<cfrunloopsourcegetcontext(____).md>) — Returns the context information for a CFRunLoopSource object.
- [CFRunLoopSourceGetOrder](<cfrunloopsourcegetorder(__).md>) — Returns the ordering parameter for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceIsValid](<cfrunloopsourceisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) — Signals a CFRunLoopSource object, marking it as ready to fire.
