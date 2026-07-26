---
title: UIPress.PressType.pageUp
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [tvOS 14.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/presstype/pageup
source_url: 'https://developer.apple.com/documentation/uikit/uipress/presstype/pageup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/presstype/pageup.json'
content_hash: 'sha256:f1b15d1218a59155'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPress](../../uipress.md) · [PressType](../presstype.md)

# UIPress.PressType.pageUp

<sub>Case</sub>

A constant that represents the page up button.

<sub>tvOS</sub>

```swift
case pageUp
```

## Discussion

Add gesture recognizers for [UIPressTypePageDown](pagedown.md) and [UIPressTypePageUp](pageup.md) to navigate content in your app.

In an electronic program guide, select the item above the current one in response to [UIPressTypeUpArrow](uparrow.md), and display the previous screen of items in response to [UIPressTypePageUp](pageup.md). While your content plays, change the channel when your app receives [UIPressTypePageUp](pageup.md) or [UIPressTypePageDown](pagedown.md).

For more details on browsing multichannel content, see [Providing Channel Navigation](../../../tvservices/providing-channel-navigation.md).

## See Also

### Navigation

- [UIPressTypeUpArrow](uparrow.md) — A constant that represents the up arrow button.
- [UIPressTypeDownArrow](downarrow.md) — A constant that represents the down arrow button.
- [UIPressTypeLeftArrow](leftarrow.md) — A constant that represents the left arrow button.
- [UIPressTypeRightArrow](rightarrow.md) — A constant that represents the right arrow button.
- [UIPressTypePageDown](pagedown.md) — A constant that represents the page down button.
