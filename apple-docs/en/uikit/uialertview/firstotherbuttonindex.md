---
title: firstOtherButtonIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uialertview/firstotherbuttonindex
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/firstotherbuttonindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/firstotherbuttonindex.json'
content_hash: 'sha256:f50a7d80b62e8f6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# firstOtherButtonIndex

<sub>Instance Property</sub>

The index of the first other button.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var firstOtherButtonIndex: Int { get }
```

## Discussion

The button indices start at `0`. If `-1`, then the index is not set. This property is ignored if there are no other buttons. The default value is `-1`.

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a button to the receiver with the given title. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the alert view. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the given index. _(deprecated)_
- [- textFieldAtIndex:](<textfield(at_).md>) — Returns the text field at the given index _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
