---
title: NSTextScalingDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextscalingdocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nstextscalingdocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextscalingdocumentattribute.json'
content_hash: 'sha256:31b1aa93fa646fa4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextScalingDocumentAttribute

<sub>Global Variable</sub>

The text-scaling mode to use when displaying the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSTextScalingDocumentAttribute;
```

## Discussion

The value of this property is one of the options of the [NSTextScalingType](nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. When saving a document, include this attribute to specify the type of scaling to apply to the text at display time.

## See Also

### Getting the font-scaling options

- [NSSourceTextScalingDocumentAttribute](nssourcetextscalingdocumentattribute.md) — The text-scaling mode you used when creating the text.
