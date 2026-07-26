---
title: separatorInset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/separatorinset
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/separatorinset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/separatorinset.json'
content_hash: 'sha256:9dc36ec0faba2267'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# separatorInset

<sub>Instance Property</sub>

The default inset of cell separators.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var separatorInset: UIEdgeInsets { get set }
```

## Discussion

In iOS 7 and later, cell separators don’t extend all the way to the edge of the table view. This property sets the default inset for all cells in the table, much as [rowHeight](rowheight.md) sets the default height for cells. It’s also used for managing the “extra” separators drawn at the bottom of plain style tables.

For example, to specify a table view where the default left separator inset is 3 points and the default right separator inset is 11, you’d write:

```objc
tableView.separatorInset = UIEdgeInsetsMake(0, 3, 0, 11);
```

If every cell in a table contains an image view of the same size, by default iOS vertically aligns the leading edge of all separators. In a table that mixes text-only cells with cells that contain image views, you can use the [separatorInset](separatorinset.md) property to ensure that the separators are vertically aligned.

In a right-to-left user interface, an inset that you set using the [separatorInset](separatorinset.md) property automatically flips its left and right measurements.

### Special considerations

Only left and right insets are honored. In a right-to-left user interface, the inset measurements are automatically flipped.

## See Also

### Customizing the separator appearance

- [separatorStyle](separatorstyle.md) — The style for table cells to use as separators.
- [SeparatorStyle](../uitableviewcell/separatorstyle.md) — The style for cells to use as separators.
- [separatorColor](separatorcolor.md) — The color of separator rows in the table view.
- [separatorEffect](separatoreffect.md) — The effect to apply to table separators.
- [separatorInsetReference](separatorinsetreference-swift.property.md) — An indicator of how to interpret the separator inset value.
- [SeparatorInsetReference](separatorinsetreference-swift.enum.md) — Constants that indicate how to interpret the separator inset value of a table view.
