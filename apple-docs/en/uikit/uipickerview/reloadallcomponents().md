---
title: reloadAllComponents()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerview/reloadallcomponents()
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/reloadallcomponents()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/reloadallcomponents%28%29.json'
content_hash: 'sha256:3913f2da413f163a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# reloadAllComponents()

<sub>Instance Method</sub>

Reloads all components of the picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func reloadAllComponents()
```

## Discussion

Calling this method causes the picker view to query the delegate for new data for all components.

## See Also

### Reloading the picker view

- [- reloadComponent:](<reloadcomponent(__).md>) — Reloads a particular component of the picker view.
