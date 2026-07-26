---
title: capacity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managedbuffer/capacity
source_url: 'https://developer.apple.com/documentation/swift/managedbuffer/capacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbuffer/capacity.json'
content_hash: 'sha256:77e4d7c3c68ecff3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBuffer](../managedbuffer.md)

# capacity

<sub>Instance Property</sub>

The actual number of elements that can be stored in this object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var capacity: Int { get }
```

## Discussion

This header may be nontrivial to compute; it is usually a good idea to store this information in the “header” area when an instance is created.
