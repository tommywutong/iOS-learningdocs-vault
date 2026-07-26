---
title: 'initWithFrame:reuseIdentifier:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableviewcell/initwithframe:reuseidentifier:'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/initwithframe:reuseidentifier:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/initwithframe%3Areuseidentifier%3A.json'
content_hash: 'sha256:5c2f721a1f0d85cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# initWithFrame:reuseIdentifier:

<sub>Instance Method</sub>

Initializes and returns a table cell object.

> [!warning] Deprecated
> Use [- initWithStyle:reuseIdentifier:](<init(style_reuseidentifier_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (id) initWithFrame:(CGRect) frame reuseIdentifier:(NSString *) reuseIdentifier;
```

## Parameters

- `frame` — The frame rectangle of the cell. Because the table view automatically positions the cell and makes it the optimal size, you can pass in `CGRectZero` in most cases. However, if you have a custom cell with multiple subviews, each with its own autoresizing mask, you must specify a non-zero frame rectangle; this allows the table view to position the subviews automatically as the cell changes size.

- `reuseIdentifier` — A string used to identify the cell object if it is to be reused for drawing multiple rows of a table view. Pass `nil` if the cell object is not to be reused.

## Return Value

An initialized [UITableViewCell](../uitableviewcell.md) object or `nil` if the object could not be created.

## Discussion

This method is the designated initializer for the class. The reuse identifier is associated with those cells (rows) of a table view that have the same general configuration, minus cell content. In its implementation of [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>), the table view’s delegate calls the `UITableView` method [- dequeueReusableCellWithIdentifier:](<../uitableview/dequeuereusablecell(withidentifier_).md>), passing in a reuse identifier, to obtain the cell object to use as the basis for the current row.

## See Also

### Related Documentation

- [reuseIdentifier](reuseidentifier.md) — A string for identifying a reusable cell.

### Deprecated

- [textLabel](textlabel.md) — The label to use for the main textual content of the table cell. _(deprecated)_
- [detailTextLabel](detailtextlabel.md) — The secondary label of the table cell, if one exists. _(deprecated)_
- [imageView](imageview.md) — The image view of the table cell. _(deprecated)_
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
- [editAction](editaction.md) — The selector defining the action message to invoke when users tap the insert or delete button. _(deprecated)_
- [accessoryAction](accessoryaction.md) — The selector defining the action message to invoke when users tap the accessory view. _(deprecated)_
