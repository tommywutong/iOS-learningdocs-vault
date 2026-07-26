---
title: 'CFMessagePortCreateRemote(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportcreateremote(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportcreateremote(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportcreateremote%28_%3A_%3A%29.json'
content_hash: 'sha256:73e143a693212f58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortCreateRemote(_:_:)

<sub>Function</sub>

Returns a CFMessagePort object connected to a remote port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortCreateRemote(_ allocator: CFAllocator!, _ name: CFString!) -> CFMessagePort!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `name` — The name of the remote message port to which to connect.

## Return Value

The new CFMessagePort object, or `NULL` on failure. If a message port has already been created for the remote port, the pre-existing object is returned. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This method is not available on iOS 7 and later—it will return `NULL` and log a sandbox violation in `syslog`. See [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091) for possible replacement technologies.

## See Also

### Creating a CFMessagePort Object

- [CFMessagePortCreateLocal](<cfmessageportcreatelocal(__________).md>) — Returns a local CFMessagePort object.
