---
title: 'textStyleRuleWithTextMarkupAttributes:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes%3A.json'
content_hash: 'sha256:3ddfdad4bd7d8ffe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# textStyleRuleWithTextMarkupAttributes:

<sub>Type Method</sub>

Creates a new text style rule object using the style attributes in the specified dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (AVTextStyleRule *) textStyleRuleWithTextMarkupAttributes:(NSDictionary<NSString *,id> *) textMarkupAttributes;
```

## Parameters

- `textMarkupAttributes` — A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see `CMTextMarkup.h`.

## Return Value

A new text style rule object with the specified attributes.

## Discussion

This method sets the [textSelector](textselector.md) property of the style object to `nil`, which causes the rules to be applied to all of the text in the media item.

## See Also

### Creating and initializing style rules

- [+ textStyleRulesFromPropertyList:](<textstylerules(frompropertylist_).md>) — Creates an array of text style rule objects from the specified property-list object.
- [textStyleRuleWithTextMarkupAttributes:textSelector:](textstylerulewithtextmarkupattributes_textselector_.md) — Creates a new text style rule object using the specified style attributes and text range information.
- [- initWithTextMarkupAttributes:](<init(textmarkupattributes_).md>) — Creates a text style rule object with the specified style attributes.
- [- initWithTextMarkupAttributes:textSelector:](<init(textmarkupattributes_textselector_).md>) — Creates a text style rule object with the specified style attributes and text range information.
