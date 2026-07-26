---
title: editAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewcell/editaction
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/editaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/editaction.json'
content_hash: 'sha256:c43483a2a6721934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# editAction

<sub>Instance Property</sub>

The selector defining the action message to invoke when users tap the insert or delete button.

> [!warning] Deprecated
> Instead, use [- tableView:commitEditingStyle:forRowAtIndexPath:](<../uitableviewdatasource/tableview(__commit_forrowat_).md>) or [- tableView:accessoryButtonTappedForRowWithIndexPath:](<../uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) for handling taps on cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, nullable) SEL editAction;
```

## Discussion

When the cell’s table is in editing mode, the cell displays a green insert control or a red delete control to the left of it. (The [selectedBackgroundView](selectedbackgroundview.md) constant applied to the cell via the [editingStyle](editingstyle-swift.property.md) property determines which control is used.) Typically, the associated [UITableView](../uitableview.md) object sets the editing action for all cells; you can use this property to alter the editing action for individual cells. If the value of this property is `NULL`, no action message is sent.

## See Also

### Deprecated

- [textLabel](textlabel.md) — The label to use for the main textual content of the table cell. _(deprecated)_
- [detailTextLabel](detailtextlabel.md) — The secondary label of the table cell, if one exists. _(deprecated)_
- [imageView](imageview.md) — The image view of the table cell. _(deprecated)_
- [initWithFrame:reuseIdentifier:](initwithframe_reuseidentifier_.md) — Initializes and returns a table cell object. _(deprecated)_
- [text](text.md) — The text of the cell. _(deprecated)_
- [font](font.md) — The font of the title. _(deprecated)_
- [textAlignment](textalignment.md) — A constant that specifies the alignment of text in the cell. _(deprecated)_
- [textColor](textcolor.md) — The color of the title text. _(deprecated)_
- [selectedTextColor](selectedtextcolor.md) — The color of the title text when the cell is selected. _(deprecated)_
- [lineBreakMode](linebreakmode.md) — The mode for wrapping and truncating text in the cell. _(deprecated)_
- [image](image.md) — The image to use as content for the cell. _(deprecated)_
- [selectedImage](selectedimage.md) — The image to use a cell content when the cell is selected. _(deprecated)_
- [hidesAccessoryWhenEditing](hidesaccessorywhenediting.md) — A Boolean value that determines whether the accessory view is hidden when the cell is being edited. _(deprecated)_
- [target](target.md) — The target object to receive action messages. _(deprecated)_
- [accessoryAction](accessoryaction.md) — The selector defining the action message to invoke when users tap the accessory view. _(deprecated)_
