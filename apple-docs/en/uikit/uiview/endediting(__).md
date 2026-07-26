---
title: 'endEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/endediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/endediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/endediting%28_%3A%29.json'
content_hash: 'sha256:3dabc1ebb9c2cf95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# endEditing(_:)

<sub>Instance Method</sub>

Causes the view (or one of its embedded text fields) to resign the first responder status.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func endEditing(_ force: Bool) -> Bool
```

## Parameters

- `force` — Specify [true](../../swift/true.md) to force the first responder to resign, regardless of whether it wants to do so.

## Return Value

[true](../../swift/true.md) if the view resigned the first responder status or [false](../../swift/false.md) if it did not.

## Discussion

This method looks at the current view and its subview hierarchy for the text field that is currently the first responder. If it finds one, it asks that text field to resign as first responder. If the `force` parameter is set to [true](../../swift/true.md), the text field is never even asked; it is forced to resign.
