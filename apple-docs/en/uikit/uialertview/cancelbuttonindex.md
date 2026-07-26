---
title: cancelButtonIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uialertview/cancelbuttonindex
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/cancelbuttonindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/cancelbuttonindex.json'
content_hash: 'sha256:9e23d3e2e811204f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# cancelButtonIndex

<sub>Instance Property</sub>

The index number of the cancel button.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cancelButtonIndex: Int { get set }
```

## Discussion

The button indices start at `0`. If `-1`, then the index is not set.

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a button to the receiver with the given title. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the alert view. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the given index. _(deprecated)_
- [- textFieldAtIndex:](<textfield(at_).md>) — Returns the text field at the given index _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first other button. _(deprecated)_
