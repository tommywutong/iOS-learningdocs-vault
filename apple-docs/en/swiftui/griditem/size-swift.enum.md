---
title: GridItem.Size
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/griditem/size-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/griditem/size-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/griditem/size-swift.enum.json'
content_hash: 'sha256:1e04746079361ea8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GridItem](../griditem.md)

# GridItem.Size

<sub>Enumeration</sub>

The size in the minor axis of one or more rows or columns in a grid layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Size
```

## Overview

Use a `Size` instance when you create a [GridItem](../griditem.md). The value tells a [LazyHGrid](../lazyhgrid.md) how to size its rows, or a [LazyVGrid](../lazyvgrid.md) how to size its columns.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the sizes

- [GridItem.Size.adaptive(minimum:maximum:)](<size-swift.enum/adaptive(minimum_maximum_).md>) — Multiple items in the space of a single flexible item.
- [GridItem.Size.fixed(_:)](<size-swift.enum/fixed(__).md>) — A single item with the specified fixed size.
- [GridItem.Size.flexible(minimum:maximum:)](<size-swift.enum/flexible(minimum_maximum_).md>) — A single flexible item.

## See Also

### Inspecting grid item properties

- [alignment](alignment.md) — The alignment to use when placing each view.
- [spacing](spacing.md) — The spacing to the next item.
- [size](size-swift.property.md) — The size of the item, which is the width of a column item or the height of a row item.
