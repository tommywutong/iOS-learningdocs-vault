---
title: NSAttachmentAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsattachmentattributename
source_url: 'https://developer.apple.com/documentation/uikit/nsattachmentattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsattachmentattributename.json'
content_hash: 'sha256:c15c7d1bcc913bfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSAttachmentAttributeName

<sub>Global Variable</sub>

The attachment for the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSAttachmentAttributeName;
```

## Discussion

The value of this attribute is an [NSTextAttachment](nstextattachment.md) object. The default value of this property is `nil`, indicating no attachment.

## See Also

### Getting attachment attribute keys

- [NSAdaptiveImageGlyphAttributeName](nsadaptiveimageglyphattributename.md) — The adaptive image glyph for the text.
