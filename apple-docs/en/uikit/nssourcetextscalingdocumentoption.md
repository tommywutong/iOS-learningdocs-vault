---
title: NSSourceTextScalingDocumentOption
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nssourcetextscalingdocumentoption
source_url: 'https://developer.apple.com/documentation/uikit/nssourcetextscalingdocumentoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nssourcetextscalingdocumentoption.json'
content_hash: 'sha256:d63500eec353aa12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSSourceTextScalingDocumentOption

<sub>Global Variable</sub>

The text-scaling mode to associate with the document’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentReadingOptionKey const NSSourceTextScalingDocumentOption;
```

## Discussion

The value of this property is one of the options of the [NSTextScalingType](nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this option to specify the text-scaling mode to associate with the document’s contents on disk.

## See Also

### Getting the font-scaling options

- [NSTargetTextScalingDocumentOption](nstargettextscalingdocumentoption.md) — The text scaling mode to use after reading the text from disk.
