---
title: 'adaptivePresentationStyle(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipresentationcontroller/adaptivepresentationstyle(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/adaptivepresentationstyle(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/adaptivepresentationstyle%28for%3A%29.json'
content_hash: 'sha256:2be3ba12f559b403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# adaptivePresentationStyle(for:)

<sub>Instance Method</sub>

Returns the presentation style to use for the specified set of traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func adaptivePresentationStyle(for traitCollection: UITraitCollection) -> UIModalPresentationStyle
```

## Parameters

- `traitCollection` — The traits for the target environment.

## Return Value

The value provided by the presentation controller’s delegate or [UIModalPresentationNone](../uimodalpresentationstyle/none.md) if a delegate was not provided or does not return a valid value.

## Discussion

After the content managed by the presentation controller is onscreen, this method returns the presentation style to use for the specified set of traits. The default implementation of this method consults its delegate object and returns the value returned by that object’s `adaptivePresentationStyleForPresentationController:traitCollection:` method. Some system-supplied presentation controllers may also provide a new style that is more suited to the new set of traits.

This method returns the presentation style for the new traits, but does not initiate a transition to the new style. The system initiates the transition to the new style when the traits actually change. When transitioning to new traits, the actual presentation controller object may change. As a result, do not cache the presentation controller object in your code. Always retrieve it from your view controller’s [presentationController](../uiviewcontroller/presentationcontroller.md) property.

## See Also

### Getting the presentation attributes

- [presentationStyle](presentationstyle.md) — The presentation style of the presented view controller.
- [adaptivePresentationStyle](adaptivepresentationstyle.md) — Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [shouldPresentInFullscreen](shouldpresentinfullscreen.md) — A Boolean value indicating whether the presentation covers the entire screen.
- [shouldRemovePresentersView](shouldremovepresentersview.md) — A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.
