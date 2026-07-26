---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilityactioncategory/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityactioncategory/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityactioncategory/init%28_%3A%29.json'
content_hash: 'sha256:2fef4e71a7370d97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityActionCategory](../accessibilityactioncategory.md)

# init(_:)

<sub>Initializer</sub>

Creates a custom action category labeled by `nameResource`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ nameResource: LocalizedStringResource)
```

## Discussion

Extension AccessibilityActionCategory { static let table = AccessibilityActionCategory(“Table Options”) }

var body: some View { TableCellView() .accessibilityActions(category: .table) { ForEach(tableCellActions) { action in Button(action.title) { action() } } } }

- Parameter:

    - nameResource: The name for the category of the accessibility actions.
