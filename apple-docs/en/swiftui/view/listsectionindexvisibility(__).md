---
title: 'listSectionIndexVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listsectionindexvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listsectionindexvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listsectionindexvisibility%28_%3A%29.json'
content_hash: 'sha256:e397f930e24a0da7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listSectionIndexVisibility(_:)

<sub>Instance Method</sub>

Changes the visibility of the list section index.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
nonisolated func listSectionIndexVisibility(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The visibility of the list section index.

## Discussion

The section index shows the section index labels of sections, which are set using the `sectionIndexLabel` modifier. These are typically the letters of the alphabet, used for sorted sections.

```swift
List(sections) { section in
    Section(section.title) {
        ForEach(section.rows) { row in
            // ...
        }
    }
    .sectionIndexLabel(section.indexTitle)
}
.listSectionIndexVisibility(.visible)
```

On iOS, the section index is displayed as a number of vertically stacked letters on the trailing side of the list. Users can jump to a specific section in the list by tapping on the corresponding index label.

On watchOS, the index of the section currently visible is displayed next to the scroll indicator when the user is scrolling through the list using the crown.

By default, the list section index is visible if the list contains any sections with an index label.

The index only shows labels for sections with a `sectionIndexLabel` modifier. This can be used to hide certain sections from the index.

By hiding section headers of empty sections with an index label, a list section index can be made to show index labels without a corresponding section.

## See Also

### Configuring a section index

- [sectionIndexLabel(_:)](<sectionindexlabel(__).md>) — Sets the label that is used in a section index to point to this section, typically only a single character long.
