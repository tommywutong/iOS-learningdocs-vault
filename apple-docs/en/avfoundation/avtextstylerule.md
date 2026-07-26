---
title: AVTextStyleRule
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avtextstylerule
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule.json'
content_hash: 'sha256:7d8fe035ef9304b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVTextStyleRule

<sub>Class</sub>

An object that represents the text styling rules to apply to a media item’s textual content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVTextStyleRule
```

## Overview

You use text style objects to format subtitles, closed captions, and other text-related content of the item. The system applies these rules to all or part of the text of the media item.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and initializing style rules

- [+ textStyleRulesFromPropertyList:](<avtextstylerule/textstylerules(frompropertylist_).md>) — Creates an array of text style rule objects from the specified property-list object.
- [- initWithTextMarkupAttributes:](<avtextstylerule/init(textmarkupattributes_).md>) — Creates a text style rule object with the specified style attributes.
- [- initWithTextMarkupAttributes:textSelector:](<avtextstylerule/init(textmarkupattributes_textselector_).md>) — Creates a text style rule object with the specified style attributes and text range information.

### Accessing the style attributes

- [textMarkupAttributes](avtextstylerule/textmarkupattributes.md) — A dictionary of text style attributes to apply to the text.
- [textSelector](avtextstylerule/textselector.md) — A string that identifies the text to which the attributes should apply.

### Exporting the style rules

- [+ propertyListForTextStyleRules:](<avtextstylerule/propertylist(for_).md>) — Converts one or more text style rules into a serializable property list object.

## See Also

### Accessing text style rules

- [textStyleRules](avplayeritem/textstylerules.md) — An array of text style rules that specify the formatting and presentation of Web Video Text Tracks (WebVTT) subtitles.
