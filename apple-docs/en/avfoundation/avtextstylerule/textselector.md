---
title: textSelector
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avtextstylerule/textselector
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/textselector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/textselector.json'
content_hash: 'sha256:9789ff3e88ce6024'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# textSelector

<sub>Instance Property</sub>

A string that identifies the text to which the attributes should apply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textSelector: String? { get }
```

## Discussion

The contents of the string are determined by the format of the legible media. For example, the string could contain the CSS selectors used by the corresponding text in Web Video Text Tracks (WebVTT) markup.

If the value of this property is `nil`, the text style attributes apply to all text in the media item.

## See Also

### Accessing the style attributes

- [textMarkupAttributes](textmarkupattributes.md) — A dictionary of text style attributes to apply to the text.
