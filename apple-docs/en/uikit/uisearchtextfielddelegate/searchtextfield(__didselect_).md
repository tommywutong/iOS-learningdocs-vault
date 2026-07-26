---
title: 'searchTextField(_:didSelect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfielddelegate/searchtextfield(_:didselect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfielddelegate/searchtextfield(_:didselect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfielddelegate/searchtextfield%28_%3Adidselect%3A%29.json'
content_hash: 'sha256:935bd30f248c012f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextFieldDelegate](../uisearchtextfielddelegate.md)

# searchTextField(_:didSelect:)

<sub>Instance Method</sub>

Tells the delegate when a person selects a search suggestion in the search text field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func searchTextField(_ searchTextField: UISearchTextField, didSelect suggestion: any UISearchSuggestion)
```

## Parameters

- `searchTextField` — The search text field displaying search suggestions.

- `suggestion` — The suggestion a person selects.

## Discussion

Implement this method to execute any necessary updates when a person chooses a search suggestion.
