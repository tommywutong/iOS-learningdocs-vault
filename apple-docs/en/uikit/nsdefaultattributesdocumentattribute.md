---
title: NSDefaultAttributesDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdefaultattributesdocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nsdefaultattributesdocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdefaultattributesdocumentattribute.json'
content_hash: 'sha256:8b884d2476944aa8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDefaultAttributesDocumentAttribute

<sub>Global Variable</sub>

The default document attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSDefaultAttributesDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSDictionary](../foundation/nsdictionary.md) object containing attributes to be applied to plain files. Used by reader methods. This key in options can specify the default attributes applied to the entire document contents. Upon return, the document attributes can contain this key indicating the actual attributes used.

The string constant in macOS 10.3 and earlier is `@"DefaultAttributes"`.
