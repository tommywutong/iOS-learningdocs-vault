---
title: 'baseWritingDirection(for:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/basewritingdirection(for:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/basewritingdirection(for:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/basewritingdirection%28for%3Ain%3A%29.json'
content_hash: 'sha256:6657c9b0181bdfce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# baseWritingDirection(for:in:)

<sub>Instance Method</sub>

Returns the base writing direction for a position in the text going in a certain direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func baseWritingDirection(for position: UITextPosition, in direction: UITextStorageDirection) -> NSWritingDirection
```

## Parameters

- `position` — An object that identifies a location in a document.

- `direction` — A constant that indicates a direction of storage (forward or backward).

## Return Value

A constant that represents a writing direction (for example, left-to-right or right-to-left).

## Discussion

The base writing direction is set previously when the text input system sends a [- setBaseWritingDirection:forRange:](<setbasewritingdirection(__for_).md>) message to the conforming document object.

## See Also

### Determining layout and writing direction

- [- positionWithinRange:farthestInDirection:](<position(within_farthestin_).md>) — Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [- characterRangeByExtendingPosition:inDirection:](<characterrange(byextending_in_).md>) — Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [- setBaseWritingDirection:forRange:](<setbasewritingdirection(__for_).md>) — Sets the base writing direction for a specified range of text in a document.
