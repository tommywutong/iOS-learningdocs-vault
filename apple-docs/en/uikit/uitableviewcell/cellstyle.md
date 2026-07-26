---
title: UITableViewCell.CellStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/cellstyle
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/cellstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/cellstyle.json'
content_hash: 'sha256:78dbcddde42308b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.CellStyle

<sub>Enumeration</sub>

An enumeration for the various styles of cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum CellStyle
```

## Overview

In all these cell styles, the larger of the text labels is accessed using the [textLabel](textlabel.md) property and the smaller using the [detailTextLabel](detailtextlabel.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Cell styles

- [UITableViewCellStyleDefault](cellstyle/default.md) — A simple style for a cell with a text label (black and left-aligned) and an optional image view.
- [UITableViewCellStyleValue1](cellstyle/value1.md) — A style for a cell with a label on the left side of the cell with left-aligned and black text; on the right side is a label that has smaller blue text and is right-aligned.
- [UITableViewCellStyleValue2](cellstyle/value2.md) — A style for a cell with a label on the left side of the cell with text that’s right-aligned and blue; on the right side of the cell is another label with smaller text that’s left-aligned and black.
- [UITableViewCellStyleSubtitle](cellstyle/subtitle.md) — A style for a cell with a left-aligned label across the top and a left-aligned label below it in smaller gray text.

### Initializers

- [init(rawValue:)](<cellstyle/init(rawvalue_).md>)

## See Also

### Creating a table view cell

- [- initWithStyle:reuseIdentifier:](<init(style_reuseidentifier_).md>) — Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [- initWithCoder:](<init(coder_).md>) — Creates a table view from data in an unarchiver.
