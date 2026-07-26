---
title: usesBottomSafeArea
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyboardlayoutguide/usesbottomsafearea
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/usesbottomsafearea'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardlayoutguide/usesbottomsafearea.json'
content_hash: 'sha256:ff4eda65cf439571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyboardLayoutGuide](../uikeyboardlayoutguide.md)

# usesBottomSafeArea

<sub>Instance Property</sub>

A Boolean value that indicates whether the layout guide uses the view’s safe area layout guide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var usesBottomSafeArea: Bool { get set }
```

## Discussion

Defaults to [true](../../swift/true.md), indicating that the layout guide ties to the [bottomAnchor](../uilayoutguide/bottomanchor.md) of the view’s [safeAreaLayoutGuide](../uiview/safearealayoutguide.md).

Set to [false](../../swift/false.md) to tie the layout guide to the [bottomAnchor](../uiview/bottomanchor.md) of the view instead.
