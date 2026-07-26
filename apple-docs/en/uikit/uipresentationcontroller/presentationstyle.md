---
title: presentationStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/presentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/presentationstyle.json'
content_hash: 'sha256:ce18381540dd0986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# presentationStyle

<sub>Instance Property</sub>

The presentation style of the presented view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var presentationStyle: UIModalPresentationStyle { get }
```

## Discussion

This property is set to the presentation style of the presented view controller. The presentation controller uses this style to determine the initial appearance of the presented content.

## See Also

### Getting the presentation attributes

- [- adaptivePresentationStyleForTraitCollection:](<adaptivepresentationstyle(for_).md>) — Returns the presentation style to use for the specified set of traits.
- [adaptivePresentationStyle](adaptivepresentationstyle.md) — Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [shouldPresentInFullscreen](shouldpresentinfullscreen.md) — A Boolean value indicating whether the presentation covers the entire screen.
- [shouldRemovePresentersView](shouldremovepresentersview.md) — A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.
