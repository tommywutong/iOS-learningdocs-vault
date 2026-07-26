---
title: imageView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（27.0 起废弃）, iPadOS 3.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewcell/imageview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/imageview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/imageview.json'
content_hash: 'sha256:1274e94cd31b62b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# imageView

<sub>Instance Property</sub>

The image view of the table cell.

> [!warning] Deprecated
> Use a content configuration to manage the cell’s image instead. Use [defaultContentConfiguration()](<defaultcontentconfiguration().md>) to get a default list content configuration, set your image to the [image](../uilistcontentconfiguration-swift.struct/image.md) property of the configuration, and apply the configuration by setting it to the [contentConfiguration](contentconfiguration-9ktox.md) property of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var imageView: UIImageView? { get }
```

## Discussion

Returns the image view ([UIImageView](../uiimageview.md) object) of the table view, which initially has no image set. If an image is set, it appears on the left side of the cell, before any label. `UITableViewCell` creates the image-view object when you create the cell.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [contentConfiguration](contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

### Related Documentation

- [- initWithStyle:reuseIdentifier:](<init(style_reuseidentifier_).md>) — Initializes a table cell with a style and a reuse identifier and returns it to the caller.

### Deprecated

- [textLabel](textlabel.md) — The label to use for the main textual content of the table cell. _(deprecated)_
- [detailTextLabel](detailtextlabel.md) — The secondary label of the table cell, if one exists. _(deprecated)_
