---
title: InsetTableStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/insettablestyle
source_url: 'https://developer.apple.com/documentation/swiftui/insettablestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/insettablestyle.json'
content_hash: 'sha256:712994b31b3376b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# InsetTableStyle

<sub>Structure</sub>

The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct InsetTableStyle
```

## Overview

You can also use [inset](tablestyle/inset.md) to construct this style.

## Relationships

- **Conforms To**: [TableStyle](tablestyle.md)

## Topics

### Creating the table style

- [init()](<insettablestyle/init().md>) — Creates a default inset table style, with alternating row backgrounds.
- [init(alternatesRowBackgrounds:)](<insettablestyle/init(alternatesrowbackgrounds_).md>) — Creates an inset table style with optional alternating row backgrounds. _(deprecated)_

## See Also

### Supporting types

- [AutomaticTableStyle](automatictablestyle.md) — The default table style in the current context.
- [BorderedTableStyle](borderedtablestyle.md) — The table style that describes the behavior and appearance of a table with standard border.
