---
title: NSTargetTextScalingDocumentOption
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstargettextscalingdocumentoption
source_url: 'https://developer.apple.com/documentation/uikit/nstargettextscalingdocumentoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstargettextscalingdocumentoption.json'
content_hash: 'sha256:fcb38273ea3c754b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTargetTextScalingDocumentOption

<sub>Global Variable</sub>

The text scaling mode to use after reading the text from disk.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentReadingOptionKey const NSTargetTextScalingDocumentOption;
```

## Discussion

The value of this property is one of the options of the [NSTextScalingType](nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this option to specify the text-scaling mode you want to use for the document you read.

## See Also

### Getting the font-scaling options

- [NSSourceTextScalingDocumentOption](nssourcetextscalingdocumentoption.md) — The text-scaling mode to associate with the document’s content.
