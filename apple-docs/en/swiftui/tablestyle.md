---
title: TableStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablestyle
source_url: 'https://developer.apple.com/documentation/swiftui/tablestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablestyle.json'
content_hash: 'sha256:203620119dd1e34a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableStyle

<sub>Protocol</sub>

A type that applies a custom appearance to all tables within a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol TableStyle
```

## Overview

To configure the current table style for a view hierarchy, use the [tableStyle(_:)](<view/tablestyle(__).md>) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [AutomaticTableStyle](automatictablestyle.md), [BorderedTableStyle](borderedtablestyle.md), [InsetTableStyle](insettablestyle.md)

## Topics

### Getting built-in table styles

- [automatic](tablestyle/automatic.md) — The default table style in the current context.
- [inset](tablestyle/inset.md) — The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [bordered](tablestyle/bordered.md) — The table style that describes the behavior and appearance of a table with standard border.

### Creating custom table styles

- [makeBody(configuration:)](<tablestyle/makebody(configuration_).md>) — Creates a view that represents the body of a table.
- [Configuration](tablestyle/configuration.md) — The properties of a table.
- [Body](tablestyle/body.md) — A view that represents the body of a table.

### Deprecated styles

- [inset(alternatesRowBackgrounds:)](<tablestyle/inset(alternatesrowbackgrounds_).md>) — The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges. _(deprecated)_
- [bordered(alternatesRowBackgrounds:)](<tablestyle/bordered(alternatesrowbackgrounds_).md>) — The table style that describes the behavior and appearance of a table with standard border. _(deprecated)_

### Supporting types

- [AutomaticTableStyle](automatictablestyle.md) — The default table style in the current context.
- [InsetTableStyle](insettablestyle.md) — The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [BorderedTableStyle](borderedtablestyle.md) — The table style that describes the behavior and appearance of a table with standard border.

## See Also

### Styling collection views

- [listStyle(_:)](<view/liststyle(__).md>) — Sets the style for lists within this view.
- [ListStyle](liststyle.md) — A protocol that describes the behavior and appearance of a list.
- [tableStyle(_:)](<view/tablestyle(__).md>) — Sets the style for tables within this view.
- [TableStyleConfiguration](tablestyleconfiguration.md) — The properties of a table.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.
- [DisclosureGroupStyle](disclosuregroupstyle.md) — A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.
