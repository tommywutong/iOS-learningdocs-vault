---
title: 'CFSocketCreateRunLoopSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketcreaterunloopsource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcreaterunloopsource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcreaterunloopsource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8c232abf9936f8ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCreateRunLoopSource(_:_:_:)

<sub>Function</sub>

Creates a CFRunLoopSource object for a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketCreateRunLoopSource(_ allocator: CFAllocator!, _ s: CFSocket!, _ order: CFIndex) -> CFRunLoopSource!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `s` — The CFSocket object for which to create a run loop source.

- `order` — A priority index indicating the order in which run loop sources are processed. When multiple run loop sources are firing in a single pass through the run loop, the sources are processed in increasing order of this parameter. If the run loop is set to process only one source per loop, only the highest priority source, the one with the lowest `order` value, is processed.

## Return Value

The new CFRunLoopSource object for `s`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [CFRunLoopAddSource](<cfrunloopaddsource(______).md>).

## See Also

### Using Sockets

- [CFSocketConnectToAddress](<cfsocketconnecttoaddress(______).md>) — Opens a connection to a remote socket.
- [CFSocketGetTypeID](<cfsocketgettypeid().md>) — Returns the type identifier for the CFSocket opaque type.
- [CFSocketInvalidate](<cfsocketinvalidate(__).md>) — Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [CFSocketIsValid](<cfsocketisvalid(__).md>) — Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [CFSocketSendData](<cfsocketsenddata(________).md>) — Sends data over a CFSocket object.
