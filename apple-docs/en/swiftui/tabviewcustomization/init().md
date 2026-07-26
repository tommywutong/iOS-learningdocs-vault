---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewcustomization/init()
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/init%28%29.json'
content_hash: 'sha256:5271469d20ad1029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewCustomization](../tabviewcustomization.md)

# init()

<sub>Initializer</sub>

Creates an empty tab sidebar customization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init()
```

## Discussion

To set this customization on a tab view, use the [tabViewCustomization(_:)](<../view/tabviewcustomization(__).md>) modifier.

With an empty customization, tabs will be visible according to the default builder visibilities, and sections will be ordered in the order declared in the tab view’s tab builder.

You can specify a default visibility for the tab in the tab bar and sidebar by attaching [defaultVisibility(_:for:)](<../tabcontent/defaultvisibility(__for_).md>) to the tab.

You can change the default section order by changing the order in the builder. If there’s an existing persisted customization, reset the order by calling [resetTabOrder()](<sectioncustomization/resettaborder().md>) when you change the order.
