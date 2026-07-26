---
title: 'subscript(visibility:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumncustomization/subscript(visibility:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncustomization/subscript(visibility:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncustomization/subscript%28visibility%3A%29.json'
content_hash: 'sha256:6cbf283bb2f91fa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnCustomization](../tablecolumncustomization.md)

# subscript(visibility:)

<sub>Instance Subscript</sub>

The visibility of the column identified by its identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
subscript(visibility id: String) -> Visibility { get set }
```

## Overview

Explicit identifiers can be associated with a `TableColumn` using the `customizationID(_:)` modifier.

```swift
TableColumn("Number of Reports", value: \.duplicateCount) {
    Text($0.duplicateCount, format: .number)
}
.customizationID("numberOfReports")

...

columnsCustomization[visibility: "numberOfReports"] = .hidden
```

If the ID isn’t associated with the state, a default value of `.automatic` is returned.

## See Also

### Managing the customization

- [resetOrder()](<resetorder().md>) — Resets the column order back to the default, preserving the customized visibility and size.
