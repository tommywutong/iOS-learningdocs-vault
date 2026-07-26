---
title: supportsSecureCoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssecurecoding/supportssecurecoding
source_url: 'https://developer.apple.com/documentation/foundation/nssecurecoding/supportssecurecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssecurecoding/supportssecurecoding.json'
content_hash: 'sha256:7784c5322e3623be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSecureCoding](../nssecurecoding.md)

# supportsSecureCoding

<sub>Type Property</sub>

A Boolean value that indicates whether or not the class supports secure coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var supportsSecureCoding: Bool { get }
```

## Discussion

When you write a class that supports secure coding, ensure that this class property’s getter returns [true](../../swift/true.md).
