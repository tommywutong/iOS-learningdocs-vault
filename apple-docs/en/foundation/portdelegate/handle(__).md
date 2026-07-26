---
title: 'handle(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/portdelegate/handle(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/portdelegate/handle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portdelegate/handle%28_%3A%29.json'
content_hash: 'sha256:7408b746d9774d39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PortDelegate](../portdelegate.md)

# handle(_:)

<sub>Instance Method</sub>

Processes a given incoming message on the port.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
optional func handle(_ message: NSPortMessage)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func handle(_ message: PortMessage)
```

## Parameters

- `message` — An incoming port message.

## Discussion

See [Port](../port.md) for more information.

The delegate should implement either [- handlePortMessage:](<handle(__).md>) or the [NSMachPortDelegate](../nsmachportdelegate.md) protocol method [- handleMachMessage:](<../nsmachportdelegate/handlemachmessage(__).md>). You must not implement both delegate methods.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
