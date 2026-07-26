---
title: 'init(textMarkupAttributes:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtextstylerule/init(textmarkupattributes:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/init(textmarkupattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/init%28textmarkupattributes%3A%29.json'
content_hash: 'sha256:e2cf45590796c45b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# init(textMarkupAttributes:)

<sub>Initializer</sub>

Creates a text style rule object with the specified style attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(textMarkupAttributes: [String : Any] = [:])
```

## Parameters

- `textMarkupAttributes` — A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see `CMTextMarkup.h`.

## Return Value

A text style rule object initialized with the specified attributes.

## Discussion

This method sets the [textSelector](textselector.md) property of the style object to `nil`, which causes the rules to be applied to all of the text in the media item.

## See Also

### Creating and initializing style rules

- [+ textStyleRulesFromPropertyList:](<textstylerules(frompropertylist_).md>) — Creates an array of text style rule objects from the specified property-list object.
- [- initWithTextMarkupAttributes:textSelector:](<init(textmarkupattributes_textselector_).md>) — Creates a text style rule object with the specified style attributes and text range information.
