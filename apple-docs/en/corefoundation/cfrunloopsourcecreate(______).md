---
title: 'CFRunLoopSourceCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopsourcecreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcecreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c0366f6b96ca7b8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceCreate(_:_:_:)

<sub>Function</sub>

Creates a CFRunLoopSource object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopSourceCreate(_ allocator: CFAllocator!, _ order: CFIndex, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `order` — A priority index indicating the order in which run loop sources are processed. When multiple run loop sources are firing in a single pass through the run loop, the sources are processed in increasing order of this parameter. If the run loop is set to process only one source per loop, only the highest priority source, the one with the lowest `order` value, is processed. This value is ignored for version 1 sources. Pass 0 unless there is a reason to do otherwise.

- `context` — A structure holding contextual information for the run loop source. The function copies the information out of the structure, so the memory pointed to by `context` does not need to persist beyond the function call.

## Return Value

The new CFRunLoopSource object. You are responsible for releasing this object.

## Discussion

The run loop source is not automatically added to a run loop. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceGetContext](<cfrunloopsourcegetcontext(____).md>) — Returns the context information for a CFRunLoopSource object.
- [CFRunLoopSourceGetOrder](<cfrunloopsourcegetorder(__).md>) — Returns the ordering parameter for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceInvalidate](<cfrunloopsourceinvalidate(__).md>) — Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [CFRunLoopSourceIsValid](<cfrunloopsourceisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) — Signals a CFRunLoopSource object, marking it as ready to fire.
