---
title: search
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabrole/search
source_url: 'https://developer.apple.com/documentation/swiftui/tabrole/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabrole/search.json'
content_hash: 'sha256:fb9b7b559d06c866'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabRole](../tabrole.md)

# search

<sub>Type Property</sub>

The search role.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var search: TabRole { get }
```

## Discussion

Searchable tab views will prefer to have the first tab with this role implement search. If no tabs are specified as the search tab, the tab view will apply search to all tabs, resetting search state as the selected tab changes.
