---
title: shared
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/globalactor/shared
source_url: 'https://developer.apple.com/documentation/swift/globalactor/shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/globalactor/shared.json'
content_hash: 'sha256:257b562141fbe340'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [GlobalActor](../globalactor.md)

# shared

<sub>Type Property</sub>

The shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var shared: Self.ActorType { get }
```

## Discussion

The value of this property must always evaluate to the same actor instance.
