---
title: 'adaptivePresentationStyle(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle%28for%3A%29.json'
content_hash: 'sha256:fba9348d7efb46ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# adaptivePresentationStyle(for:)

<sub>Instance Method</sub>

Asks the delegate for the new presentation style to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func adaptivePresentationStyle(for controller: UIPresentationController) -> UIModalPresentationStyle
```

## Parameters

- `controller` — The presentation controller that is managing the size change. Use this object to retrieve the view controllers involved in the presentation.

## Return Value

The new presentation style, which must be [UIModalPresentationFullScreen](../uimodalpresentationstyle/fullscreen.md), [UIModalPresentationOverFullScreen](../uimodalpresentationstyle/overfullscreen.md), or [UIModalPresentationNone](../uimodalpresentationstyle/none.md).

## Discussion

In iOS 8.3 and later, use the [- adaptivePresentationStyleForPresentationController:traitCollection:](<adaptivepresentationstyle(for_traitcollection_).md>) method to handle all trait changes instead of this method. If you do not implement that method, you can use this method to change the presentation style when transitioning to a horizontally compact environment.

If you do not implement this method or if you return an invalid style, the current presentation controller returns its preferred default style.

## See Also

### Adapting the presentation style

- [- adaptivePresentationStyleForPresentationController:traitCollection:](<adaptivepresentationstyle(for_traitcollection_).md>) — Asks the delegate for the presentation style to use when the specified set of traits are active.
