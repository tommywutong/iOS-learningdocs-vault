---
title: textMarkupAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avtextstylerule/textmarkupattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/textmarkupattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/textmarkupattributes.json'
content_hash: 'sha256:c0b9f57777945095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# textMarkupAttributes

<sub>Instance Property</sub>

A dictionary of text style attributes to apply to the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textMarkupAttributes: [String : Any] { get }
```

## Discussion

The supported keys for this dictionary are defined in `CMTextMarkup.h`.

## See Also

### Accessing the style attributes

- [textSelector](textselector.md) — A string that identifies the text to which the attributes should apply.
