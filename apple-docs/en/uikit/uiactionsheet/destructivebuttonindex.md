---
title: destructiveButtonIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheet/destructivebuttonindex
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/destructivebuttonindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/destructivebuttonindex.json'
content_hash: 'sha256:edc7dee6524042d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# destructiveButtonIndex

<sub>Instance Property</sub>

The index number of the destructive button.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var destructiveButtonIndex: Int { get set }
```

## Discussion

Button indices start at `0`. The default value of this property is normally `-1`, which indicates that no destructive button has been set. However, a destructive button may be created and set automatically by the [- initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:](<init(title_delegate_cancelbuttontitle_destructivebuttontitle_).md>) method. If you use that method to create a destructive button, you should not change the value of this property.

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a custom button to the action sheet. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the action sheet. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the specified index. _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first custom button. _(deprecated)_
