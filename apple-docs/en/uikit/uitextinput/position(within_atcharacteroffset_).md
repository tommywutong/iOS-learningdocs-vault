---
title: 'position(within:atCharacterOffset:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/position(within:atcharacteroffset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/position(within:atcharacteroffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/position%28within%3Aatcharacteroffset%3A%29.json'
content_hash: 'sha256:9864e4a57d3ec853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# position(within:atCharacterOffset:)

<sub>Instance Method</sub>

Returns the position within a range of a document’s text that corresponds to the character offset from the start of that range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func position(within range: UITextRange, atCharacterOffset offset: Int) -> UITextPosition?
```

## Parameters

- `range` — An object that specifies a range of text in a document.

- `offset` — A character offset from the start of `range`.

## Return Value

An object that represents a position in a document’s visible text.

## Discussion

You should implement this method if you don’t have a one-to-one correspondence between [UITextPosition](../uitextposition.md) objects within the given range and character offsets into a document string.

## See Also

### Reconciling text position and character offset

- [- characterOffsetOfPosition:withinRange:](<characteroffset(of_within_).md>) — Returns the character offset of a position in a document’s text that falls within a specified range.
