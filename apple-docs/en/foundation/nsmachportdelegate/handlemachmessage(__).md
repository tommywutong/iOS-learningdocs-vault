---
title: 'handleMachMessage(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachportdelegate/handlemachmessage(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachportdelegate/handlemachmessage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachportdelegate/handlemachmessage%28_%3A%29.json'
content_hash: 'sha256:e30b916c579e01c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPortDelegate](../nsmachportdelegate.md)

# handleMachMessage(_:)

<sub>Instance Method</sub>

Process an incoming Mach message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func handleMachMessage(_ msg: UnsafeMutableRawPointer)
```

## Parameters

- `msg` — A pointer to a Mach message, cast as a pointer to void.

## Discussion

The delegate should interpret this data as a pointer to a Mach message beginning with a msg_header_t structure and should handle the message appropriately.

The delegate should implement either `handleMachMessage:` or the [PortDelegate](../portdelegate.md) protocol method handlePortMessage:.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
