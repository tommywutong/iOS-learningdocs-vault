---
title: 'CFMessagePortCreateRunLoopSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportcreaterunloopsource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportcreaterunloopsource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportcreaterunloopsource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:238f1ab325bc5862'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortCreateRunLoopSource(_:_:_:)

<sub>Function</sub>

Creates a CFRunLoopSource object for a CFMessagePort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortCreateRunLoopSource(_ allocator: CFAllocator!, _ local: CFMessagePort!, _ order: CFIndex) -> CFRunLoopSource!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `local` — The message port for which to create a run loop source.

- `order` — A priority index indicating the order in which run loop sources are processed. `order` is currently ignored by CFMessagePort object run loop sources. Pass `0` for this value.

## Return Value

The new CFRunLoopSource object for `ms`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [CFRunLoopAddSource](<cfrunloopaddsource(______).md>).

### Special Considerations

This method is not available on iOS 7 and later—it will return `NULL` and log a sandbox violation in `syslog`. See [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091) for possible replacement technologies.

## See Also

### Configuring a CFMessagePort Object

- [CFMessagePortSetInvalidationCallBack](<cfmessageportsetinvalidationcallback(____).md>) — Sets the callback function invoked when a CFMessagePort object is invalidated.
- [CFMessagePortSetName](<cfmessageportsetname(____).md>) — Sets the name of a local CFMessagePort object.
