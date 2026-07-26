---
title: UIPageControl.Direction.natural
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/direction-swift.enum/natural
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/direction-swift.enum/natural'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/direction-swift.enum/natural.json'
content_hash: 'sha256:e21204a0b7e6097b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPageControl](../../uipagecontrol.md) · [Direction](../direction-swift.enum.md)

# UIPageControl.Direction.natural

<sub>Case</sub>

A direction that infers the lay out from the system’s locale.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case natural
```

## Discussion

Use this case to lay out the page control’s indicators in the natural direction of the system’s locale. By default, this means [UIPageControlDirectionLeftToRight](lefttoright.md) for left-to-right languages and [UIPageControlDirectionRightToLeft](righttoleft.md) for right-to-left languages.

## See Also

### Directions

- [UIPageControlDirectionLeftToRight](lefttoright.md) — A direction that lays out the page indicators from left to right.
- [UIPageControlDirectionRightToLeft](righttoleft.md) — A direction that lays out the page indicators from right to left.
- [UIPageControlDirectionTopToBottom](toptobottom.md) — A direction that lays out the page indicators from top to bottom.
- [UIPageControlDirectionBottomToTop](bottomtotop.md) — A direction that lays out the page indicators from bottom to top.
