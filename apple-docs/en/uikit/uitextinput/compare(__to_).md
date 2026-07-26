---
title: 'compare(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/compare(_:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/compare(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/compare%28_%3Ato%3A%29.json'
content_hash: 'sha256:d332d081035c3bff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# compare(_:to:)

<sub>Instance Method</sub>

Returns how one text position compares to another text position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func compare(_ position: UITextPosition, to other: UITextPosition) -> ComparisonResult
```

## Parameters

- `position` — A custom object that represents a location within a document.

- `other` — A custom object that represents another location within a document.

## Return Value

A value that indicates whether the two text positions are identical or whether one is before the other.

## See Also

### Evaluating text positions

- [- offsetFromPosition:toPosition:](<offset(from_to_).md>) — Returns the number of UTF-16 characters between one text position and another text position.
