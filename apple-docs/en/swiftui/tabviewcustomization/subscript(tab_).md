---
title: 'subscript(tab:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabviewcustomization/subscript(tab:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(tab:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/subscript%28tab%3A%29.json'
content_hash: 'sha256:1c44efe89d6bc03b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewCustomization](../tabviewcustomization.md)

# subscript(tab:)

<sub>Instance Subscript</sub>

The customization of the tab, identified by its customization identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
subscript(tab id: String) -> TabViewCustomization.TabCustomization { get set }
```

## Overview

You can imperatively set properties by subscripting with the tab ID. The following example sets the tab’s sidebar visibility:

```swift
customization[tab: "com.myApp.alerts"].sidebarVisibility = .hidden
```
