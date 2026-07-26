---
title: shouldRemovePresentersView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/shouldremovepresentersview
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/shouldremovepresentersview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/shouldremovepresentersview.json'
content_hash: 'sha256:bf62488621944fa9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# shouldRemovePresentersView

<sub>Instance Property</sub>

A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shouldRemovePresentersView: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the view should be removed or [false](../../swift/false.md) if it should not.

## Discussion

The default implementation of this method returns [false](../../swift/false.md). If you implement a presentation that does not cover the presenting view controller’s content entirely, override this method and return [false](../../swift/false.md).

If you override this method, do not call `super`.

## See Also

### Getting the presentation attributes

- [presentationStyle](presentationstyle.md) — The presentation style of the presented view controller.
- [- adaptivePresentationStyleForTraitCollection:](<adaptivepresentationstyle(for_).md>) — Returns the presentation style to use for the specified set of traits.
- [adaptivePresentationStyle](adaptivepresentationstyle.md) — Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [shouldPresentInFullscreen](shouldpresentinfullscreen.md) — A Boolean value indicating whether the presentation covers the entire screen.
