---
title: textLabel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（27.0 起废弃）, iPadOS 3.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewcell/textlabel
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/textlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/textlabel.json'
content_hash: 'sha256:802bd6ca0eac40d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# textLabel

<sub>Instance Property</sub>

The label to use for the main textual content of the table cell.

> [!warning] Deprecated
> Use a content configuration to manage the cell’s text instead. Use [defaultContentConfiguration()](<defaultcontentconfiguration().md>) to get a default list content configuration, set your primary text to the [text](../uilistcontentconfiguration-swift.struct/text.md) property of the configuration, and apply the configuration by setting it to the [contentConfiguration](contentconfiguration-9ktox.md) property of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textLabel: UILabel? { get }
```

## Discussion

This property holds the main label of the cell. [UITableViewCell](../uitableviewcell.md) adds an appropriate label when you create the cell in a particular cell style. See [CellStyle](cellstyle.md) for descriptions of the main label in currently defined cell styles.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [contentConfiguration](contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

### Related Documentation

- [- initWithStyle:reuseIdentifier:](<init(style_reuseidentifier_).md>) — Initializes a table cell with a style and a reuse identifier and returns it to the caller.

### Deprecated

- [detailTextLabel](detailtextlabel.md) — The secondary label of the table cell, if one exists. _(deprecated)_
- [imageView](imageview.md) — The image view of the table cell. _(deprecated)_
