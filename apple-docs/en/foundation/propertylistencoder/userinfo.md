---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/propertylistencoder/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/propertylistencoder/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistencoder/userinfo.json'
content_hash: 'sha256:ed458d0b30dcb10a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListEncoder](../propertylistencoder.md)

# userInfo

<sub>Instance Property</sub>

A dictionary you use to customize the encoding process by providing contextual information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency var userInfo: [CodingUserInfoKey : any Sendable] { get set }
```

## See Also

### Customizing Encoding

- [outputFormat](outputformat.md) — A value that determines which property list format is used during encoding.
