---
title: 'isPosition(_:withinTextUnit:inDirection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputtokenizer/isposition(_:withintextunit:indirection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtokenizer/isposition(_:withintextunit:indirection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtokenizer/isposition%28_%3Awithintextunit%3Aindirection%3A%29.json'
content_hash: 'sha256:5e3e5c0244cc3ed0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTokenizer](../uitextinputtokenizer.md)

# isPosition(_:withinTextUnit:inDirection:)

<sub>Instance Method</sub>

Return whether a text position is within a text unit of a specified granularity in a specified direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func isPosition(_ position: UITextPosition, withinTextUnit granularity: UITextGranularity, inDirection direction: UITextDirection) -> Bool
```

## Parameters

- `position` — A text-position object that represents a location in a document.

- `granularity` — A constant that indicates a certain granularity of text unit.

- `direction` — A constant that indicates a direction relative to `position`. The constant can be of type UITextStorageDirection or UITextLayoutDirection.

## Return Value

[true](../../swift/true.md) if the text position is within a text unit of the specified granularity in the specified direction; otherwise, return [false](../../swift/false.md). If the text position is _at_ a boundary, return [true](../../swift/true.md) only if the boundary is part of the text unit in the given direction.

## See Also

### Determining text positions relative to unit boundaries

- [- isPosition:atBoundary:inDirection:](<isposition(__atboundary_indirection_).md>) — Return whether a text position is at a boundary of a text unit of a specified granularity in a specified direction.
