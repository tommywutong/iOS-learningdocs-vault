---
title: 'position(from:offset:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/position(from:offset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/position(from:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/position%28from%3Aoffset%3A%29.json'
content_hash: 'sha256:1b3086c706bd6dad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# position(from:offset:)

<sub>Instance Method</sub>

Returns the text position at a specified offset from another text position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func position(from position: UITextPosition, offset: Int) -> UITextPosition?
```

## Parameters

- `position` — A custom [UITextPosition](../uitextposition.md) object that represents a location in a document.

- `offset` — A character offset from `position`. It can be a positive or negative value.

## Return Value

A custom [UITextPosition](../uitextposition.md) object that represents the location in a document that is at the specified offset from `position`. Return `nil` if the computed text position is less than 0 or greater than the length of the backing string.

## Discussion

For an example of an implementation of this method, see [Using Text Kit to Draw and Manage Text](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/CustomTextProcessing/CustomTextProcessing.html#//apple_ref/doc/uid/TP40009542-CH4) in [Text Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009542).

## See Also

### Computing text ranges and text positions

- [- textRangeFromPosition:toPosition:](<textrange(from_to_).md>) — Returns the range between two text positions.
- [- positionFromPosition:inDirection:offset:](<position(from_in_offset_).md>) — Returns the text position at a specified offset in a specified direction from another text position.
- [beginningOfDocument](beginningofdocument.md) — The text position for the beginning of a document.
- [endOfDocument](endofdocument.md) — The text position for the end of a document.
