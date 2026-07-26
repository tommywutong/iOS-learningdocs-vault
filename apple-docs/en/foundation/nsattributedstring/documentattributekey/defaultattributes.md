---
title: defaultAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/defaultattributes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/defaultattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/defaultattributes.json'
content_hash: 'sha256:4b1a556add15fed1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# defaultAttributes

<sub>Type Property</sub>

The default document attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let defaultAttributes: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSDictionary](../../nsdictionary.md) object containing attributes to be applied to plain files. Used by reader methods. This key in options can specify the default attributes applied to the entire document contents. Upon return, the document attributes can contain this key indicating the actual attributes used.

The string constant in macOS 10.3 and earlier is `@"DefaultAttributes"`.
