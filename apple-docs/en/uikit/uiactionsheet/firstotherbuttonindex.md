---
title: firstOtherButtonIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheet/firstotherbuttonindex
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/firstotherbuttonindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/firstotherbuttonindex.json'
content_hash: 'sha256:4c0f450d7b45cdcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# firstOtherButtonIndex

<sub>Instance Property</sub>

The index of the first custom button.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var firstOtherButtonIndex: Int { get }
```

## Discussion

Button indices start at `0`. The default value of this property is `-1`, which indicates that there are no other custom buttons.

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a custom button to the action sheet. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the action sheet. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the specified index. _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [destructiveButtonIndex](destructivebuttonindex.md) — The index number of the destructive button. _(deprecated)_
