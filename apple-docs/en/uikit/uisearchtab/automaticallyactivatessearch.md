---
title: automaticallyActivatesSearch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtab/automaticallyactivatessearch
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtab/automaticallyactivatessearch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtab/automaticallyactivatessearch.json'
content_hash: 'sha256:19eb869a3a399bea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTab](../uisearchtab.md)

# automaticallyActivatesSearch

<sub>Instance Property</sub>

Determines if the search tab should automatically activate the embedded search field when the tab becomes visible.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var automaticallyActivatesSearch: Bool { get set }
```

## Discussion

When this property is set to `YES`, the search field will be activated when the tab is selected. Moreover, when search is cancelled, the previously selected tab in the tab bar will be restored and selected. The default value is `NO`.
