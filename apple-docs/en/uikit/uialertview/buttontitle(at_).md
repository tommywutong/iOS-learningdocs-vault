---
title: 'buttonTitle(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertview/buttontitle(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/buttontitle(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/buttontitle%28at%3A%29.json'
content_hash: 'sha256:4f475a7b29024dbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# buttonTitle(at:)

<sub>Instance Method</sub>

Returns the title of the button at the given index.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func buttonTitle(at buttonIndex: Int) -> String?
```

## Parameters

- `buttonIndex` — The index of the button. The button indices start at `0`.

## Return Value

The title of the button specified by index `buttonIndex`.

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a button to the receiver with the given title. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the alert view. _(deprecated)_
- [- textFieldAtIndex:](<textfield(at_).md>) — Returns the text field at the given index _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first other button. _(deprecated)_
