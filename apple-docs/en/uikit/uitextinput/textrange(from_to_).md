---
title: 'textRange(from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/textrange(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/textrange(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/textrange%28from%3Ato%3A%29.json'
content_hash: 'sha256:a35ed1cad5874775'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# textRange(from:to:)

<sub>Instance Method</sub>

Returns the range between two text positions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textRange(from fromPosition: UITextPosition, to toPosition: UITextPosition) -> UITextRange?
```

## Parameters

- `fromPosition` — An object that represents a location in a document.

- `toPosition` — An object that represents another location in a document.

## Return Value

An object that represents the range between `fromPosition` and `toPosition`.

## See Also

### Computing text ranges and text positions

- [- positionFromPosition:offset:](<position(from_offset_).md>) — Returns the text position at a specified offset from another text position.
- [- positionFromPosition:inDirection:offset:](<position(from_in_offset_).md>) — Returns the text position at a specified offset in a specified direction from another text position.
- [beginningOfDocument](beginningofdocument.md) — The text position for the beginning of a document.
- [endOfDocument](endofdocument.md) — The text position for the end of a document.
