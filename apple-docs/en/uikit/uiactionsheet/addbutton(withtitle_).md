---
title: 'addButton(withTitle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/addbutton(withtitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/addbutton(withtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/addbutton%28withtitle%3A%29.json'
content_hash: 'sha256:04bc15dd45513d85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# addButton(withTitle:)

<sub>Instance Method</sub>

Adds a custom button to the action sheet.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func addButton(withTitle title: String?) -> Int
```

## Parameters

- `title` — The title of the new button.

## Return Value

The index of the new button. Button indices start at `0` and increase in the order they are added.

## See Also

### Related Documentation

- [UIActionSheet](../uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_

### Configuring buttons

- [numberOfButtons](numberofbuttons.md) — The number of buttons on the action sheet. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the specified index. _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [destructiveButtonIndex](destructivebuttonindex.md) — The index number of the destructive button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first custom button. _(deprecated)_
