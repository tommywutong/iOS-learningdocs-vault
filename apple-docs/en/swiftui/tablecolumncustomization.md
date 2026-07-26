---
title: TableColumnCustomization
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumncustomization
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncustomization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncustomization.json'
content_hash: 'sha256:cbfe95021fb8c75d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableColumnCustomization

<sub>Structure</sub>

A representation of the state of the columns in a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct TableColumnCustomization<RowValue> where RowValue : Identifiable
```

## Overview

`TableColumnCustomization` can be created and provided to a table to enable column reordering and column visibility. The state can be queried and updated programmatically, as well as bound to persistent app or scene storage.

```swift
struct BugReportTable: View {
    @ObservedObject var dataModel: DataModel
    @Binding var selectedBugReports: Set<BugReport.ID>

    @SceneStorage("BugReportTableConfig")
    private var columnCustomization: TableColumnCustomization<BugReport>

    var body: some View {
        Table(dataModel.bugReports, selection: $selectedBugReports,
            sortOrder: $dataModel.sortOrder,
            columnCustomization: $columnCustomization
        ) {
            TableColumn("Title", value: \.title)
                .customizationID("title")
            TableColumn("ID", value: \.id) {
                Link("\($0.id)", destination: $0.url)
            }
            .customizationID("id")
            TableColumn("Number of Reports", value: \.duplicateCount) {
                Text($0.duplicateCount, format: .number)
            }
            .customizationID("duplicates")
        }
    }
}
```

The above example creates a table with three columns. On macOS, these columns can be reordered or hidden and shown by the user of the app. Their configuration will be saved and restored with the window on relaunches of the app, using the “BugReportTableConfig” scene storage identifier.

The state of a specific column is stored relative to its customization identifier, using using the value from the [customizationID(_:)](<tablecolumncontent/customizationid(__).md>) modifier. When column customization is encoded and decoded, it relies on stable identifiers to restore the associate the saved state with a specific column. If a table column does not have a customization identifier, it will not be customizable.

These identifiers can also be used to programmatically change column customizations, such as programmatically hiding a column:

```swift
columnCustomization[visibility: "duplicates"] = .hidden
```

With a binding to the overall customization, a binding to the visibility of a column can be accessed using the same subscript syntax:

```swift
struct BugReportTable: View {
    @SceneStorage("BugReportTableConfig")
    private var columnCustomization: TableColumnCustomization<BugReport>

    var body: some View {
        ...
        MyVisibilityView($columnCustomization[visibility: "duplicates"])
    }
}

struct MyVisibilityView: View {
    @Binding var visibility: Visibility
    ...
}
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a table column customization

- [init()](<tablecolumncustomization/init().md>) — Creates an empty table column customization.

### Managing the customization

- [resetOrder()](<tablecolumncustomization/resetorder().md>) — Resets the column order back to the default, preserving the customized visibility and size.
- [subscript(visibility:)](<tablecolumncustomization/subscript(visibility_).md>) — The visibility of the column identified by its identifier.

## See Also

### Customizing columns

- [tableColumnHeaders(_:)](<view/tablecolumnheaders(__).md>) — Controls the visibility of a `Table`’s column header views.
- [TableColumnCustomizationBehavior](tablecolumncustomizationbehavior.md) — A set of customization behaviors of a column that a table can offer to a user.
