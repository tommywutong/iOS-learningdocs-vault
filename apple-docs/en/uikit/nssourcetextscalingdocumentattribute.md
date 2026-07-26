---
title: NSSourceTextScalingDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nssourcetextscalingdocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nssourcetextscalingdocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nssourcetextscalingdocumentattribute.json'
content_hash: 'sha256:79b0f6cfe68ce849'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSSourceTextScalingDocumentAttribute

<sub>Global Variable</sub>

The text-scaling mode you used when creating the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSSourceTextScalingDocumentAttribute;
```

## Discussion

The value of this property is one of the options of the [NSTextScalingType](nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this attribute to specify the original text-scaling mode you used to create the text.

## See Also

### Getting the font-scaling options

- [NSTextScalingDocumentAttribute](nstextscalingdocumentattribute.md) — The text-scaling mode to use when displaying the text.
