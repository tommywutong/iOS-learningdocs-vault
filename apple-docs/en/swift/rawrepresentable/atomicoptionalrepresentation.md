---
title: RawRepresentable.AtomicOptionalRepresentation
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rawrepresentable/atomicoptionalrepresentation
source_url: 'https://developer.apple.com/documentation/swift/rawrepresentable/atomicoptionalrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawrepresentable/atomicoptionalrepresentation.json'
content_hash: 'sha256:e14129c84ddf57fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawRepresentable](../rawrepresentable.md)

# RawRepresentable.AtomicOptionalRepresentation

<sub>Type Alias</sub>

The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias AtomicOptionalRepresentation = Self.RawValue.AtomicOptionalRepresentation
```
