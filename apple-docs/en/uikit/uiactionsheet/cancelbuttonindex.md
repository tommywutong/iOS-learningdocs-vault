---
title: cancelButtonIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheet/cancelbuttonindex
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/cancelbuttonindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/cancelbuttonindex.json'
content_hash: 'sha256:020c4c70c5a34ddf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# cancelButtonIndex

<sub>Instance Property</sub>

The index number of the cancel button.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cancelButtonIndex: Int { get set }
```

## Discussion

Button indices start at `0`. The default value of this property is normally `-1`, which indicates that no cancel button has been set. However, a cancel button may be created and set automatically by the [- initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:](<init(title_delegate_cancelbuttontitle_destructivebuttontitle_).md>) method. If you use that method to create a cancel button, you should not change the value of this property.

When presenting an action sheet on an iPad, there are times when you should not include a cancel button. For more information on when you should include a cancel button, see the class overview or [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a custom button to the action sheet. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the action sheet. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the specified index. _(deprecated)_
- [destructiveButtonIndex](destructivebuttonindex.md) — The index number of the destructive button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first custom button. _(deprecated)_
