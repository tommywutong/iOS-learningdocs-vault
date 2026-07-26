---
title: previewingGestureRecognizerForFailureRelationship
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship.json'
content_hash: 'sha256:3f6d9b05f3bd459d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md)

# previewingGestureRecognizerForFailureRelationship

<sub>Instance Property</sub>

A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.

> [!warning] Deprecated
> For more information, see [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer { get }
```

## Discussion

Use this gesture recognizer by implementing a delegate object for it that conforms to the [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md) protocol. The protocol methods let you prevent a preview (peek) press from interfering with an app’s other supported gestures. For example, you could delay a preview’s presentation until after other gestures fail, or you could allow simultaneous recognition of a press and other gestures during a preview’s presentation.

For more information, see the [- gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldberequiredtofailby_).md>) and [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldrequirefailureof_).md>) methods in [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md).

## See Also

### Configuring a source view for a 3D Touch previewing view controller

- [sourceRect](sourcerect.md) — The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs. _(deprecated)_
