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
doc_path: /documentation/swift/mainactor/shared
source_url: 'https://developer.apple.com/documentation/swift/mainactor/shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mainactor/shared.json'
content_hash: 'sha256:497ffacf894179e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MainActor](../mainactor.md)

# shared

<sub>Type Property</sub>

The shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let shared: MainActor
```

## Discussion

The value of this property must always evaluate to the same actor instance.
