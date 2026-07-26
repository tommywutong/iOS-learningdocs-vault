---
title: 'subscript(section:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabviewcustomization/subscript(section:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(section:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/subscript%28section%3A%29.json'
content_hash: 'sha256:000c6d23e5057c39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewCustomization](../tabviewcustomization.md)

# subscript(section:)

<sub>Instance Subscript</sub>

The customization of the section, identified by its customization identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
subscript(section id: String) -> TabViewCustomization.SectionCustomization { get set }
```

## Overview

Section tab order can be read by subscripting with the tab section’s id:

```swift
let order = customization[section: "com.myApp.categories"].tabOrder
```

To reset the order of an individual section, use [resetTabOrder()](<sectioncustomization/resettaborder().md>). To reset the order of all sections, use [resetSectionOrder()](<resetsectionorder().md>).
