---
title: 'animateChanges(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisheetpresentationcontroller/animatechanges(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/animatechanges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/animatechanges%28_%3A%29.json'
content_hash: 'sha256:d840ba598cf5e505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# animateChanges(_:)

<sub>Instance Method</sub>

Animates the UI changes to the sheet’s properties.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func animateChanges(_ changes: () -> Void)
```

## Parameters

- `changes` — A block where you change the sheet’s properties to animate them.

## Discussion

To animate changes to any of the sheet’s properties, set them inside the block that you pass to this method. By the time this method returns, layout finishes for the sheet, all adjacent sheets in the sheet stack, and their subviews.
