---
title: 'isPosition(_:atBoundary:inDirection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputtokenizer/isposition(_:atboundary:indirection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtokenizer/isposition(_:atboundary:indirection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtokenizer/isposition%28_%3Aatboundary%3Aindirection%3A%29.json'
content_hash: 'sha256:f0b00b5224f634cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTokenizer](../uitextinputtokenizer.md)

# isPosition(_:atBoundary:inDirection:)

<sub>Instance Method</sub>

Return whether a text position is at a boundary of a text unit of a specified granularity in a specified direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func isPosition(_ position: UITextPosition, atBoundary granularity: UITextGranularity, inDirection direction: UITextDirection) -> Bool
```

## Parameters

- `position` — A text-position object that represents a location in a document.

- `granularity` — A constant that indicates a certain granularity of text unit.

- `direction` — A constant that indicates a direction relative to `position`. The constant can be of type UITextStorageDirection or UITextLayoutDirection.

## Return Value

[true](../../swift/true.md) if the text position is at the given text-unit boundary in the given direction; [false](../../swift/false.md) if it is not at the boundary.

## See Also

### Determining text positions relative to unit boundaries

- [- isPosition:withinTextUnit:inDirection:](<isposition(__withintextunit_indirection_).md>) — Return whether a text position is within a text unit of a specified granularity in a specified direction.
