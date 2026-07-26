---
title: TableColumnCustomizationBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumncustomizationbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncustomizationbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncustomizationbehavior.json'
content_hash: 'sha256:048906eb91383254'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableColumnCustomizationBehavior

<sub>Structure</sub>

A set of customization behaviors of a column that a table can offer to a user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct TableColumnCustomizationBehavior
```

## Overview

This is used as a value provided to [disabledCustomizationBehavior(_:)](<tablecolumncontent/disabledcustomizationbehavior(__).md>).

Setting any of these values as the `disabledCustomizationBehavior(_:)` doesn’t have any effect on iOS.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting the customization behavior

- [all](tablecolumncustomizationbehavior/all.md) — All customization behaviors.
- [reorder](tablecolumncustomizationbehavior/reorder.md) — A behavior that allows the column to be reordered by the user.
- [resize](tablecolumncustomizationbehavior/resize.md) — A behavior that allows the column to be resized by the user.
- [visibility](tablecolumncustomizationbehavior/visibility.md) — A behavior that allows the column to be hidden or revealed by the user.

### Creating a behavior

- [init()](<tablecolumncustomizationbehavior/init().md>) — Creates an empty customization behavior, representing no customization

## See Also

### Customizing columns

- [tableColumnHeaders(_:)](<view/tablecolumnheaders(__).md>) — Controls the visibility of a `Table`’s column header views.
- [TableColumnCustomization](tablecolumncustomization.md) — A representation of the state of the columns in a table.
