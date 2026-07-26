---
title: 'addButton(withTitle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertview/addbutton(withtitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/addbutton(withtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/addbutton%28withtitle%3A%29.json'
content_hash: 'sha256:70b0215e3bb7da59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# addButton(withTitle:)

<sub>Instance Method</sub>

Adds a button to the receiver with the given title.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func addButton(withTitle title: String?) -> Int
```

## Parameters

- `title` — The title of the new button.

## Return Value

The index of the new button. Button indices start at `0` and increase in the order they are added.

## Discussion

Adding too many buttons can cause the alert view to scroll. For guidelines on the best ways to use an alert in an app, see [Temporary Views](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/Alerts.html#//apple_ref/doc/uid/TP40006556-CH14).

## See Also

### Related Documentation

- [message](message.md) — Descriptive text that provides more details than the title. _(deprecated)_

### Configuring buttons

- [numberOfButtons](numberofbuttons.md) — The number of buttons on the alert view. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the given index. _(deprecated)_
- [- textFieldAtIndex:](<textfield(at_).md>) — Returns the text field at the given index _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first other button. _(deprecated)_
