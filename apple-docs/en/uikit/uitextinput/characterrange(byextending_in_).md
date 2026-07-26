---
title: 'characterRange(byExtending:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/characterrange(byextending:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/characterrange(byextending:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/characterrange%28byextending%3Ain%3A%29.json'
content_hash: 'sha256:3887b5ebd2bcb1a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# characterRange(byExtending:in:)

<sub>Instance Method</sub>

Returns a text range from a specified text position to its farthest extent in a certain direction of layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func characterRange(byExtending position: UITextPosition, in direction: UITextLayoutDirection) -> UITextRange?
```

## Parameters

- `position` — A text-position object that identifies a location in a document.

- `direction` — A constant that indicates a direction of layout (right, left, up, down).

## Return Value

A text-range object that represents the distance from `position` to the farthest extent in `direction`.

## See Also

### Determining layout and writing direction

- [- positionWithinRange:farthestInDirection:](<position(within_farthestin_).md>) — Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [- baseWritingDirectionForPosition:inDirection:](<basewritingdirection(for_in_).md>) — Returns the base writing direction for a position in the text going in a certain direction.
- [- setBaseWritingDirection:forRange:](<setbasewritingdirection(__for_).md>) — Sets the base writing direction for a specified range of text in a document.
