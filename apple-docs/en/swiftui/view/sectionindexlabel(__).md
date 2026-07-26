---
title: 'sectionIndexLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/sectionindexlabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sectionindexlabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sectionindexlabel%28_%3A%29.json'
content_hash: 'sha256:f3be57293fcc06e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sectionIndexLabel(_:)

<sub>Instance Method</sub>

Sets the label that is used in a section index to point to this section, typically only a single character long.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func sectionIndexLabel(_ label: Text?) -> some View

```

## Parameters

- `label` — The label to display in the section index, or `nil` to display no label for this section.

## Discussion

- See also `listSectionIndexVisibility(_:)`

## See Also

### Configuring a section index

- [listSectionIndexVisibility(_:)](<listsectionindexvisibility(__).md>) — Changes the visibility of the list section index.
