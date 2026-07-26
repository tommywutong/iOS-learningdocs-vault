---
title: 'rangeEnclosingPosition(_:with:inDirection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputtokenizer/rangeenclosingposition(_:with:indirection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtokenizer/rangeenclosingposition(_:with:indirection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtokenizer/rangeenclosingposition%28_%3Awith%3Aindirection%3A%29.json'
content_hash: 'sha256:3d39dfc05ad01f51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTokenizer](../uitextinputtokenizer.md)

# rangeEnclosingPosition(_:with:inDirection:)

<sub>Instance Method</sub>

Return the range for the text enclosing a text position in a text unit of a given granularity in a given direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func rangeEnclosingPosition(_ position: UITextPosition, with granularity: UITextGranularity, inDirection direction: UITextDirection) -> UITextRange?
```

## Parameters

- `position` — A text-position object that represents a location in a document.

- `granularity` — A constant that indicates a certain granularity of text unit.

- `direction` — A constant that indicates a direction relative to `position`. The constant can be of type UITextStorageDirection or UITextLayoutDirection.

## Return Value

A text-range representing a text unit of the given granularity in the given direction, or `nil` if there is no such enclosing unit.  Whether a boundary position is enclosed depends on the given direction, using the same rule as the [- isPosition:withinTextUnit:inDirection:](<isposition(__withintextunit_indirection_).md>) method.

## Discussion

In this method, return the range for the text enclosing a text position in a text unit of the given granularity, or `nil` if there is no such enclosing unit.  If the text position is entirely enclosed within a text unit of the given granularity, it is considered enclosed. If the text position is at a text-unit boundary, it is considered enclosed only if the next position in the given direction is entirely enclosed.
