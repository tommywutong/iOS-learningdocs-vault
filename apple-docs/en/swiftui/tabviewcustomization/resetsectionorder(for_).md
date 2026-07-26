---
title: 'resetSectionOrder(for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 18.0+（27.0 起废弃）, macOS 15.0+（27.0 起废弃）, visionOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/tabviewcustomization/resetsectionorder(for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/resetsectionorder(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/resetsectionorder%28for%3A%29.json'
content_hash: 'sha256:c0c4a991e9b75825'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewCustomization](../tabviewcustomization.md)

# resetSectionOrder(for:)

<sub>Instance Method</sub>

Resets ordering back to the default for the section with `sectionID`, preserving any customized tab visibilities.

> [!warning] Deprecated
> Use the `section` subscript and call `resetTabOrder` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
mutating func resetSectionOrder(for sectionID: String)
```
