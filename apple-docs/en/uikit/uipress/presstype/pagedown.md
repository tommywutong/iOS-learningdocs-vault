---
title: UIPress.PressType.pageDown
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [tvOS 14.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/presstype/pagedown
source_url: 'https://developer.apple.com/documentation/uikit/uipress/presstype/pagedown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/presstype/pagedown.json'
content_hash: 'sha256:38e4e5e87579ac45'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPress](../../uipress.md) · [PressType](../presstype.md)

# UIPress.PressType.pageDown

<sub>Case</sub>

A constant that represents the page down button.

<sub>tvOS</sub>

```swift
case pageDown
```

## Discussion

Add gesture recognizers for [UIPressTypePageDown](pagedown.md) and [UIPressTypePageUp](pageup.md) to navigate content in your app.

In an electronic program guide, select the item below the current one in response to [UIPressTypeDownArrow](downarrow.md), and display the next screen of items in response to [UIPressTypePageDown](pagedown.md). While your content plays, change the channel when your app receives [UIPressTypePageUp](pageup.md) or [UIPressTypePageDown](pagedown.md).

For more details on browsing multichannel content, see [Providing Channel Navigation](../../../tvservices/providing-channel-navigation.md).

## See Also

### Navigation

- [UIPressTypeUpArrow](uparrow.md) — A constant that represents the up arrow button.
- [UIPressTypeDownArrow](downarrow.md) — A constant that represents the down arrow button.
- [UIPressTypeLeftArrow](leftarrow.md) — A constant that represents the left arrow button.
- [UIPressTypeRightArrow](rightarrow.md) — A constant that represents the right arrow button.
- [UIPressTypePageUp](pageup.md) — A constant that represents the page up button.
