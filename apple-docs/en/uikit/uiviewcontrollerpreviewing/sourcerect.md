---
title: sourceRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontrollerpreviewing/sourcerect
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/sourcerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewing/sourcerect.json'
content_hash: 'sha256:54cdf07cea8b4863'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md)

# sourceRect

<sub>Instance Property</sub>

The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.

> [!warning] Deprecated
> For more information, see [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sourceRect: CGRect { get set }
```

## Discussion

Use this property if you want to specify a preview indication area that is different than the bounds of the view in the [sourceView](sourceview.md) property. Set this property’s value in your object’s [- previewingContext:viewControllerForLocation:](<../uiviewcontrollerpreviewingdelegate/previewingcontext(__viewcontrollerforlocation_).md>) method.

The default value of this property corresponds to the bounds of the view in the [sourceView](sourceview.md) property.

For example, if your source view is a table view, you can set the `sourceRect` property to the frame of the row under the user’s touch. The row then remains visually sharp when a user presses it, while surrounding content blurs, thereby indicating to the user that it is the row being touched that has a preview available.

You can change the value of this property at runtime.

## See Also

### Related Documentation

- [sourceView](sourceview.md) — A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user. _(deprecated)_

### Configuring a source view for a 3D Touch previewing view controller

- [previewingGestureRecognizerForFailureRelationship](previewinggesturerecognizerforfailurerelationship.md) — A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures. _(deprecated)_
