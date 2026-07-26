---
title: detailTextLabel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（27.0 起废弃）, iPadOS 6.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewheaderfooterview/detailtextlabel
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/detailtextlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/detailtextlabel.json'
content_hash: 'sha256:617e9af9b1d847d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# detailTextLabel

<sub>Instance Property</sub>

A detail text label for the view.

> [!warning] Deprecated
> Use a content configuration to manage the view’s text instead. Use [defaultContentConfiguration()](<defaultcontentconfiguration().md>) to get a default list content configuration, set your secondary text to the [secondaryText](../uilistcontentconfiguration-swift.struct/secondarytext.md) property of the configuration, and apply the configuration by setting it to the [contentConfiguration](contentconfiguration-6b4eg.md) property of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var detailTextLabel: UILabel? { get }
```

## Discussion

This property is only for tables configured with [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md).

Accessing the value in this property causes the view to create a default label for displaying a detail text string. If you are managing the content of the view yourself by adding subviews to the [contentView](contentview.md) property, you should not access this property.

The label sizes to fit the content view area in the best way possible according to the size of the string. Its size also adjusts depending on whether there is a primary text label present.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [contentConfiguration](contentconfiguration-6b4eg.md) resets this property to `nil`.

## See Also

### Deprecated

- [textLabel](textlabel.md) — A primary text label for the view. _(deprecated)_
