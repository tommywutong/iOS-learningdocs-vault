---
title: 'setBaseWritingDirection(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/setbasewritingdirection(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/setbasewritingdirection(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/setbasewritingdirection%28_%3Afor%3A%29.json'
content_hash: 'sha256:f8d85aaff8d0b863'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# setBaseWritingDirection(_:for:)

<sub>Instance Method</sub>

Sets the base writing direction for a specified range of text in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, for range: UITextRange)
```

## Parameters

- `writingDirection` — A constant that represents a writing direction (for example, left-to-right or right-to-left)

- `range` — An object that represents a range of text in a document.

## See Also

### Determining layout and writing direction

- [- positionWithinRange:farthestInDirection:](<position(within_farthestin_).md>) — Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [- characterRangeByExtendingPosition:inDirection:](<characterrange(byextending_in_).md>) — Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [- baseWritingDirectionForPosition:inDirection:](<basewritingdirection(for_in_).md>) — Returns the base writing direction for a position in the text going in a certain direction.
