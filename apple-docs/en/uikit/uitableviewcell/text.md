---
title: text
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewcell/text
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/text.json'
content_hash: 'sha256:a1cb2dcd1c8ca797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# text

<sub>Instance Property</sub>

The text of the cell.

> [!warning] Deprecated
> Use the [textLabel](textlabel.md) and [detailTextLabel](detailtextlabel.md) properties instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) NSString * text;
```

## Discussion

The default is `nil` (no text).

## See Also

### Deprecated

- [textLabel](textlabel.md) — The label to use for the main textual content of the table cell. _(deprecated)_
- [detailTextLabel](detailtextlabel.md) — The secondary label of the table cell, if one exists. _(deprecated)_
- [imageView](imageview.md) — The image view of the table cell. _(deprecated)_
- [initWithFrame:reuseIdentifier:](initwithframe_reuseidentifier_.md) — Initializes and returns a table cell object. _(deprecated)_
- [font](font.md) — The font of the title. _(deprecated)_
- [textAlignment](textalignment.md) — A constant that specifies the alignment of text in the cell. _(deprecated)_
- [textColor](textcolor.md) — The color of the title text. _(deprecated)_
- [selectedTextColor](selectedtextcolor.md) — The color of the title text when the cell is selected. _(deprecated)_
- [lineBreakMode](linebreakmode.md) — The mode for wrapping and truncating text in the cell. _(deprecated)_
- [image](image.md) — The image to use as content for the cell. _(deprecated)_
- [selectedImage](selectedimage.md) — The image to use a cell content when the cell is selected. _(deprecated)_
- [hidesAccessoryWhenEditing](hidesaccessorywhenediting.md) — A Boolean value that determines whether the accessory view is hidden when the cell is being edited. _(deprecated)_
- [target](target.md) — The target object to receive action messages. _(deprecated)_
- [editAction](editaction.md) — The selector defining the action message to invoke when users tap the insert or delete button. _(deprecated)_
- [accessoryAction](accessoryaction.md) — The selector defining the action message to invoke when users tap the accessory view. _(deprecated)_
