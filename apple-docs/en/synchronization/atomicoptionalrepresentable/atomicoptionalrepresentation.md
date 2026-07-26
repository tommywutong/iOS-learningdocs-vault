---
title: AtomicOptionalRepresentation
framework: Synchronization
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicoptionalrepresentable/atomicoptionalrepresentation
source_url: 'https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable/atomicoptionalrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicoptionalrepresentable/atomicoptionalrepresentation.json'
content_hash: 'sha256:b3510fb79d7dd0a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicOptionalRepresentable](../atomicoptionalrepresentable.md)

# AtomicOptionalRepresentation

<sub>Associated Type</sub>

The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype AtomicOptionalRepresentation : BitwiseCopyable
```
