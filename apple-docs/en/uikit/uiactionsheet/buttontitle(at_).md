---
title: 'buttonTitle(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/buttontitle(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/buttontitle(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/buttontitle%28at%3A%29.json'
content_hash: 'sha256:0b8762fd1d02f50e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# buttonTitle(at:)

<sub>Instance Method</sub>

Returns the title of the button at the specified index.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func buttonTitle(at buttonIndex: Int) -> String?
```

## Parameters

- `buttonIndex` — The index of the button. The button indices start at `0`.

## Return Value

The title of the button specified by index `buttonIndex`.

## See Also

### Related Documentation

- [- showInView:](<show(in_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a custom button to the action sheet. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the action sheet. _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [destructiveButtonIndex](destructivebuttonindex.md) — The index number of the destructive button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first custom button. _(deprecated)_
