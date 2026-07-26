---
title: user
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/morphology/user
source_url: 'https://developer.apple.com/documentation/foundation/morphology/user'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/user.json'
content_hash: 'sha256:df5d9fd5313912c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Morphology](../morphology.md)

# user

<sub>Type Property</sub>

The addressing preferences of the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let user: Morphology
```

## Discussion

If the user hasn’t specified preferences, or chose not to share them with this app, the [isUnspecified](isunspecified.md) property is `true`.

This value doesn’t change throughout the lifetime of the process.
