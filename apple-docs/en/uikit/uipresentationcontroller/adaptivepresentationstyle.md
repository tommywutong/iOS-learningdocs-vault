---
title: adaptivePresentationStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/adaptivepresentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/adaptivepresentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/adaptivepresentationstyle.json'
content_hash: 'sha256:30f442e6c48342bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# adaptivePresentationStyle

<sub>Instance Property</sub>

Returns the presentation style to use when the presented view controller becomes horizontally compact.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adaptivePresentationStyle: UIModalPresentationStyle { get }
```

## Return Value

The value provided by the presentation controller’s delegate or [UIModalPresentationNone](../uimodalpresentationstyle/none.md) if a delegate was not provided or does not return a valid value.

## Discussion

After the content managed by the presentation controller is onscreen, this method returns the presentation style to use when transitioning to a horizontally compact environment. This method is not meant to be overridden. The implementation consults its delegate object and returns the value provided by that object’s [- adaptivePresentationStyleForPresentationController:](<../uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for_).md>) method. Some system-supplied presentation controllers may also provide a new style that is more suited for a compact environment. For example, presentation controllers that manage popovers and form sheets return the [UIModalPresentationFullScreen](../uimodalpresentationstyle/fullscreen.md) value.

This method only returns the presentation style to use in a horizontally compact environment. It does not initiate a transition to the new style. The system initiates the transition to the new style when the size class actually changes. When transitioning to a new style, the actual presentation controller object may change. As a result, do not cache the presentation controller object in your code. Always retrieve it from your view controller’s [presentationController](../uiviewcontroller/presentationcontroller.md) property.

In iOS 8.3 and later, UIKit calls the [- adaptivePresentationStyleForTraitCollection:](<adaptivepresentationstyle(for_).md>) method to retrieve presentation styles instead of this one.

## See Also

### Getting the presentation attributes

- [presentationStyle](presentationstyle.md) — The presentation style of the presented view controller.
- [- adaptivePresentationStyleForTraitCollection:](<adaptivepresentationstyle(for_).md>) — Returns the presentation style to use for the specified set of traits.
- [shouldPresentInFullscreen](shouldpresentinfullscreen.md) — A Boolean value indicating whether the presentation covers the entire screen.
- [shouldRemovePresentersView](shouldremovepresentersview.md) — A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.
