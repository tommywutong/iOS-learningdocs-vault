---
title: 'textStyleRules(fromPropertyList:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtextstylerule/textstylerules(frompropertylist:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/textstylerules(frompropertylist:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/textstylerules%28frompropertylist%3A%29.json'
content_hash: 'sha256:92885227f74ca00a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# textStyleRules(fromPropertyList:)

<sub>Type Method</sub>

Creates an array of text style rule objects from the specified property-list object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func textStyleRules(fromPropertyList plist: Any) -> [AVTextStyleRule]?
```

## Parameters

- `plist` — A property-list object containing the text style data.

## Return Value

An array of `AVTextStyleRule` objects corresponding to the style information in the property-list object.

## Discussion

Use this method to create new text style rule objects based on data you previously converted to a property-list format using the [+ propertyListForTextStyleRules:](<propertylist(for_).md>) class method.

## See Also

### Creating and initializing style rules

- [- initWithTextMarkupAttributes:](<init(textmarkupattributes_).md>) — Creates a text style rule object with the specified style attributes.
- [- initWithTextMarkupAttributes:textSelector:](<init(textmarkupattributes_textselector_).md>) — Creates a text style rule object with the specified style attributes and text range information.
