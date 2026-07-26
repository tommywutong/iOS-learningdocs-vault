---
title: searchTabSelection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabsearchactivation/searchtabselection
source_url: 'https://developer.apple.com/documentation/swiftui/tabsearchactivation/searchtabselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabsearchactivation/searchtabselection.json'
content_hash: 'sha256:53f3296d9ae06b23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabSearchActivation](../tabsearchactivation.md)

# searchTabSelection

<sub>Type Property</sub>

Links the search tab’s selection to search activation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static var searchTabSelection: TabSearchActivation { get }
```

## Discussion

When the search tab is selected, search will activate. When the user dismisses search, the search tab will be deselected and the previously selected tab will be reselected.
