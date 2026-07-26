---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/delegate.json'
content_hash: 'sha256:c043d1c95e92f340'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# delegate

<sub>Instance Property</sub>

The delegate for the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIPickerViewDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UIPickerViewDelegate](../uipickerviewdelegate.md) protocol and implement the required methods to return the drawing rectangle for rows in each component. It also provides the content for each component’s row, either as a string or a view, and it typically responds to new selections or deselections.

## See Also

### Customizing the picker behavior

- [UIPickerViewDelegate](../uipickerviewdelegate.md) — The interface for a picker view’s delegate.
