---
title: largeTitleTextAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/largetitletextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/largetitletextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/largetitletextattributes.json'
content_hash: 'sha256:ac5bbc41f427f232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# largeTitleTextAttributes

<sub>Instance Property</sub>

Display attributes for the bar’s large title text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var largeTitleTextAttributes: [NSAttributedString.Key : Any]? { get set }
```

## Discussion

You can specify the font, text color, text shadow color, and text shadow offset for the title in the text attributes dictionary, using the text attribute keys described in [NSAttributedString.Key](../../foundation/nsattributedstring/key.md).

## See Also

### Configuring the title

- [titleTextAttributes](titletextattributes.md) — Display attributes for the bar’s title text.
- [- titleVerticalPositionAdjustmentForBarMetrics:](<titleverticalpositionadjustment(for_).md>) — Returns the title’s vertical position adjustment for given bar metrics.
- [- setTitleVerticalPositionAdjustment:forBarMetrics:](<settitleverticalpositionadjustment(__for_).md>) — Sets the title’s vertical position adjustment for given bar metrics.
