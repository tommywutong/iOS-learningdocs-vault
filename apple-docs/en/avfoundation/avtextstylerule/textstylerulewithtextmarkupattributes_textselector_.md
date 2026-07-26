---
title: 'textStyleRuleWithTextMarkupAttributes:textSelector:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes:textselector:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes:textselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes%3Atextselector%3A.json'
content_hash: 'sha256:b85f8b12cbbbc775'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# textStyleRuleWithTextMarkupAttributes:textSelector:

<sub>Type Method</sub>

Creates a new text style rule object using the specified style attributes and text range information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (AVTextStyleRule *) textStyleRuleWithTextMarkupAttributes:(NSDictionary<NSString *,id> *) textMarkupAttributes textSelector:(NSString *) textSelector;
```

## Parameters

- `textMarkupAttributes` — A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see `CMTextMarkup.h`.

- `textSelector` — A string contains an identifier for the ranges of text to which the style attributes should be applied. Eligible identifiers are determined by the media format and its corresponding text content. For example, the string could contain the CSS selectors used by the corresponding text in Web Video Text Tracks (WebVTT) markup. Specify `nil` if you want the style attributes to apply to all text in the item.

## Return Value

A new text style rule object with the specified attributes and range information.

## See Also

### Creating and initializing style rules

- [+ textStyleRulesFromPropertyList:](<textstylerules(frompropertylist_).md>) — Creates an array of text style rule objects from the specified property-list object.
- [textStyleRuleWithTextMarkupAttributes:](textstylerulewithtextmarkupattributes_.md) — Creates a new text style rule object using the style attributes in the specified dictionary.
- [- initWithTextMarkupAttributes:](<init(textmarkupattributes_).md>) — Creates a text style rule object with the specified style attributes.
- [- initWithTextMarkupAttributes:textSelector:](<init(textmarkupattributes_textselector_).md>) — Creates a text style rule object with the specified style attributes and text range information.
