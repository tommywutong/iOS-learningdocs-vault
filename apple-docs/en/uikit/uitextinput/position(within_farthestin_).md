---
title: 'position(within:farthestIn:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/position(within:farthestin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/position(within:farthestin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/position%28within%3Afarthestin%3A%29.json'
content_hash: 'sha256:52cd25cf4133259b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# position(within:farthestIn:)

<sub>Instance Method</sub>

Returns the text position that is at the farthest extent in a specified layout direction within a range of text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func position(within range: UITextRange, farthestIn direction: UITextLayoutDirection) -> UITextPosition?
```

## Parameters

- `range` — A text-range object that demarcates a range of text in a document.

- `direction` — A constant that indicates a direction of layout (right, left, up, down).

## Return Value

A text-position object that identifies a location in the visible text.

## See Also

### Determining layout and writing direction

- [- characterRangeByExtendingPosition:inDirection:](<characterrange(byextending_in_).md>) — Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [- baseWritingDirectionForPosition:inDirection:](<basewritingdirection(for_in_).md>) — Returns the base writing direction for a position in the text going in a certain direction.
- [- setBaseWritingDirection:forRange:](<setbasewritingdirection(__for_).md>) — Sets the base writing direction for a specified range of text in a document.
