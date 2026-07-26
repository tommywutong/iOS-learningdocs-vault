---
title: 'characterOffset(of:within:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/characteroffset(of:within:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/characteroffset(of:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/characteroffset%28of%3Awithin%3A%29.json'
content_hash: 'sha256:13ca229e1e08cd7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# characterOffset(of:within:)

<sub>Instance Method</sub>

Returns the character offset of a position in a document’s text that falls within a specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func characterOffset(of position: UITextPosition, within range: UITextRange) -> Int
```

## Parameters

- `position` — An object that identifies a location in a document’s text.

- `range` — An object that specifies a range of text in a document.

## Return Value

The number of characters in a document’s text that occur between `position` and the beginning of `range`.

## Discussion

You should implement this method if you don’t have a one-to-one correspondence between [UITextPosition](../uitextposition.md) objects within the given range and character offsets into a document string.

## See Also

### Reconciling text position and character offset

- [- positionWithinRange:atCharacterOffset:](<position(within_atcharacteroffset_).md>) — Returns the position within a range of a document’s text that corresponds to the character offset from the start of that range.
