---
title: DisclosureTableRow
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/disclosuretablerow
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuretablerow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuretablerow.json'
content_hash: 'sha256:a2a42257238aaf4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DisclosureTableRow

<sub>Structure</sub>

A kind of table row that shows or hides additional rows based on the state of a disclosure control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct DisclosureTableRow<Label, Content> where Label : TableRowContent, Content : TableRowContent, Label.TableRowValue == Content.TableRowValue
```

## Overview

A disclosure group row consists of a label row that is always visible, and some content rows that are conditionally visible depending on the state. Toggling the control will flip the state between “expanded” and “collapsed”.

In the following example, a disclosure group has `allDevices` as the label row, and exposes its expanded state with the bound property, `expanded`. Upon toggling the disclosure control, the user can update the expanded state which will in turn show or hide the three content rows for `iPhone`, `iPad`, and `Mac`.

```swift
private struct DeviceStats: Identifiable {
    // ...
}
@State private var expanded: Bool = true
@State private var allDevices: DeviceStats = /* ... */
@State private var iPhone: DeviceStats = /* ... */
@State private var iPad: DeviceStats = /* ... */
@State private var Mac: DeviceStats = /* ... */

var body: some View {
    Table(of: DeviceStats.self) {
        // ...
    } rows: {
        DisclosureTableRow(allDevices, isExpanded: $expanded) {
            TableRow(iPhone)
            TableRow(iPad)
            TableRow(Mac)
        }
    }
}
```

## Relationships

- **Conforms To**: [TableRowContent](tablerowcontent.md)

## Topics

### Creating a disclosure table row

- [init(_:isExpanded:content:)](<disclosuretablerow/init(__isexpanded_content_).md>) — Creates a disclosure group with the given value and table rows, and a binding to the expansion state (expanded or collapsed).

## See Also

### Adding progressive disclosure

- [TableOutlineGroupContent](tableoutlinegroupcontent.md) — An opaque table row type created by a table’s hierarchical initializers.
