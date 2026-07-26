---
title: NSTextBlock
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextblock
source_url: 'https://developer.apple.com/documentation/uikit/nstextblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextblock.json'
content_hash: 'sha256:38e820fbaab0954d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextBlock

<sub>Class</sub>

An object that defines the size, spacing, and appearance of a block of text in an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextBlock
```

## Overview

A text block lets you control how a paragraph looks and where it sits — you can configure its content dimensions, margin, border, padding, and colors.

You create a text block, configure its properties, then assign it to a paragraph by setting the [textBlocks](nsparagraphstyle/textblocks.md) property on an [NSMutableParagraphStyle](nsmutableparagraphstyle.md) and applying that style to a range in an `NSMutableAttributedString`. To represent a cell inside a table, use [NSTextTableBlock](nstexttableblock.md) instead.

### Understand content dimensions

Each text block has three layers around its content: padding, border, and margin. You can configure the width of each layer per edge using [- setWidth:type:forLayer:rectEdge:](<nstextblock/setwidth(__type_for_rectedge_).md>), or set all edges at once using [- setWidth:type:forLayer:](<nstextblock/setwidth(__type_for_).md>). Use [Dimension](nstextblock/dimension.md) to set the content area’s width, height, and minimum or maximum constraints. Use [ValueType](nstextblock/valuetype.md) to specify whether a dimension is an absolute point value or a percentage.

### Configure visual appearance

Set a background color using [backgroundColor](nstextblock/backgroundcolor.md). Configure border colors per edge using `setBorderColor(_:for:)`, or apply a single color to all four edges at once using [- setBorderColor:](<nstextblock/setbordercolor(__).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSTextTable](nstexttable.md), [NSTextTableBlock](nstexttableblock.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Initializing a text block

- [- init](<nstextblock/init().md>)
- [- initWithCoder:](<nstextblock/init(coder_).md>)

### Setting content dimensions

- [- setValue:type:forDimension:](<nstextblock/setvalue(__type_for_).md>)
- [- valueForDimension:](<nstextblock/value(for_).md>)
- [- valueTypeForDimension:](<nstextblock/valuetype(for_).md>)
- [- setContentWidth:type:](<nstextblock/setcontentwidth(__type_).md>)
- [contentWidth](nstextblock/contentwidth.md)
- [contentWidthValueType](nstextblock/contentwidthvaluetype.md)

### Setting layer widths

- [- setWidth:type:forLayer:](<nstextblock/setwidth(__type_for_).md>)
- [- setWidth:type:forLayer:rectEdge:](<nstextblock/setwidth(__type_for_rectedge_).md>) _(beta)_
- [- widthForLayer:rectEdge:](<nstextblock/width(for_rectedge_).md>) _(beta)_
- [- widthValueTypeForLayer:rectEdge:](<nstextblock/widthvaluetype(for_rectedge_).md>) _(beta)_

### Configuring appearance

- [verticalAlignment](nstextblock/verticalalignment-swift.property.md)
- [backgroundColor](nstextblock/backgroundcolor.md)
- [- setBorderColor:](<nstextblock/setbordercolor(__).md>)
- [- setBorderColor:rectEdge:](<nstextblock/setbordercolor(__rectedge_).md>) _(beta)_
- [- borderColorForRectEdge:](<nstextblock/bordercolor(for_).md>) _(beta)_

### Supporting types

- [ValueType](nstextblock/valuetype.md)
- [Dimension](nstextblock/dimension.md)
- [Layer](nstextblock/layer.md)
- [VerticalAlignment](nstextblock/verticalalignment-swift.enum.md)

## See Also

### Tables

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
- [NSTextTable](nstexttable.md) — An object that represents a table of rows and columns in an attributed string.
- [NSTextTableBlock](nstexttableblock.md) — A text block that represents a single cell in a text table.
