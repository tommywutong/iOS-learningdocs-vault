---
title: 'position(from:toBoundary:inDirection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputtokenizer/position(from:toboundary:indirection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtokenizer/position(from:toboundary:indirection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtokenizer/position%28from%3Atoboundary%3Aindirection%3A%29.json'
content_hash: 'sha256:5a341b2cbe73defb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTokenizer](../uitextinputtokenizer.md)

# position(from:toBoundary:inDirection:)

<sub>Instance Method</sub>

Return the next text position at a boundary of a text unit of the given granularity in a given direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func position(from position: UITextPosition, toBoundary granularity: UITextGranularity, inDirection direction: UITextDirection) -> UITextPosition?
```

## Parameters

- `position` — A text-position object that represents a location in a document.

- `granularity` — A constant that indicates a certain granularity of text unit.

- `direction` — A constant that indicates a direction relative to `position`. The constant can be of type UITextStorageDirection or UITextLayoutDirection.

## Return Value

The next boundary position of a text unit of the given granularity in the given direction, or `nil` if there is no such position.
