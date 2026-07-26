---
title: 'reloadComponent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerview/reloadcomponent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/reloadcomponent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/reloadcomponent%28_%3A%29.json'
content_hash: 'sha256:06f1cc8ecff70663'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# reloadComponent(_:)

<sub>Instance Method</sub>

Reloads a particular component of the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func reloadComponent(_ component: Int)
```

## Parameters

- `component` — A zero-indexed number identifying a component of the picker view.

## Discussion

Calling this method causes the picker view to query the delegate for new data for the given component.

## See Also

### Reloading the picker view

- [- reloadAllComponents](<reloadallcomponents().md>) — Reloads all components of the picker view.
