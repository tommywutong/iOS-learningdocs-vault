---
title: 'create(minimumCapacity:makingHeaderWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/managedbuffer/create(minimumcapacity:makingheaderwith:)'
source_url: 'https://developer.apple.com/documentation/swift/managedbuffer/create(minimumcapacity:makingheaderwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbuffer/create%28minimumcapacity%3Amakingheaderwith%3A%29.json'
content_hash: 'sha256:57cbb77852fac528'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBuffer](../managedbuffer.md)

# create(minimumCapacity:makingHeaderWith:)

<sub>Type Method</sub>

Create a new instance of the most-derived class, calling `factory` on the partially-constructed object to generate an initial `Header`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class func create(minimumCapacity: Int, makingHeaderWith factory: (ManagedBuffer<Header, Element>) throws -> Header) rethrows -> ManagedBuffer<Header, Element>
```
