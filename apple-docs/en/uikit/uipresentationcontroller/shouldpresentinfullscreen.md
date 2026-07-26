---
title: shouldPresentInFullscreen
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/shouldpresentinfullscreen
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/shouldpresentinfullscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/shouldpresentinfullscreen.json'
content_hash: 'sha256:c91aac8dc85c0a2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# shouldPresentInFullscreen

<sub>Instance Property</sub>

A Boolean value indicating whether the presentation covers the entire screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shouldPresentInFullscreen: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the presentation covers the screen or [false](../../swift/false.md) if it covers all or part of the current view controller only.

## Discussion

The default implementation of this method returns [true](../../swift/true.md), indicating that the presentation covers the entire screen. You can override this method and return [false](../../swift/false.md) to force the presentation to display only in the current context.

If you override this method, do not call `super`.

## See Also

### Getting the presentation attributes

- [presentationStyle](presentationstyle.md) — The presentation style of the presented view controller.
- [- adaptivePresentationStyleForTraitCollection:](<adaptivepresentationstyle(for_).md>) — Returns the presentation style to use for the specified set of traits.
- [adaptivePresentationStyle](adaptivepresentationstyle.md) — Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [shouldRemovePresentersView](shouldremovepresentersview.md) — A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.
