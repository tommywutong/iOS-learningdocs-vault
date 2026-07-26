---
title: 'adaptivePresentationStyle(for:traitCollection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle%28for%3Atraitcollection%3A%29.json'
content_hash: 'sha256:22f025a105939ea7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# adaptivePresentationStyle(for:traitCollection:)

<sub>Instance Method</sub>

Asks the delegate for the presentation style to use when the specified set of traits are active.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func adaptivePresentationStyle(for controller: UIPresentationController, traitCollection: UITraitCollection) -> UIModalPresentationStyle
```

## Parameters

- `controller` — The presentation controller that is managing the size change. Use this object to retrieve the view controllers involved in the presentation.

- `traitCollection` — The traits representing the target environment.

## Return Value

The new presentation style, which must be [UIModalPresentationFullScreen](../uimodalpresentationstyle/fullscreen.md), [UIModalPresentationOverFullScreen](../uimodalpresentationstyle/overfullscreen.md), [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md), or [UIModalPresentationNone](../uimodalpresentationstyle/none.md).

## Discussion

The presentation controller calls this method when the traits of the current environment are about to change. Your implementation of this method can return the preferred presentation style to use for the specified traits. If you do not return one of the allowed styles, the presentation controller uses its preferred default style.

If you do not implement this method in your delegate, UIKit calls the [- adaptivePresentationStyleForPresentationController:](<adaptivepresentationstyle(for_).md>) method instead.

## See Also

### Adapting the presentation style

- [- adaptivePresentationStyleForPresentationController:](<adaptivepresentationstyle(for_).md>) — Asks the delegate for the new presentation style to use.
