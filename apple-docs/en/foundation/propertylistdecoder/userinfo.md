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
doc_path: /documentation/foundation/propertylistdecoder/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/propertylistdecoder/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistdecoder/userinfo.json'
content_hash: 'sha256:df2a8de857aecf47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListDecoder](../propertylistdecoder.md)

# userInfo

<sub>Instance Property</sub>

A dictionary you use to customize decoding by providing contextual information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency var userInfo: [CodingUserInfoKey : any Sendable] { get set }
```

## See Also

### Customizing Decoding

- [decode(_:from:format:)](<decode(__from_format_).md>) — Returns a value of the specified type by decoding a property list using the supplied format.
