---
title: 'accessibilityDropPoint(_:description:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilitydroppoint(_:description:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilitydroppoint(_:description:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilitydroppoint%28_%3Adescription%3Aisenabled%3A%29.json'
content_hash: 'sha256:f53eb99799a762ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityDropPoint(_:description:isEnabled:)

<sub>Instance Method</sub>

The point an assistive technology should use to end a drag interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func accessibilityDropPoint(_ point: UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `point` — The point the assistive technology will perform a drop interaction.

- `description` — The description of the drop interaction.

- `isEnabled` — If true the accessibility drop point is applied; otherwise the accessibility drop point is unchanged.

## Discussion

Use this modifier when you need to provide a description to users when prompted end a drag interaction.

```swift
struct FolderView: View {
    var folderName: String

    var body: some View {
        FolderIcon(folderName: folderName)
            .accessibilityDropPoint(
                .center, description: Text("Move to \(folderName)"))
    }
}
```

By default, if an accessible view or its subtree has drag and/or drop interactions, they will be automatically exposed by assistive technologies. However, if there is more than one such interaction, each drag or drop should have a description to disambiguate it and give a good user experience.

> [!note] Note
> An accessibility element can have multiple points for a drop, provided they have different descriptions.
