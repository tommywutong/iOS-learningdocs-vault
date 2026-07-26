---
title: UIAdaptivePresentationControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiadaptivepresentationcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate.json'
content_hash: 'sha256:27e4112e113aee8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAdaptivePresentationControllerDelegate

<sub>Protocol</sub>

A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIAdaptivePresentationControllerDelegate : NSObjectProtocol
```

## Overview

After implementing an object that conforms to this protocol, assign that object to the [delegate](uipresentationcontroller/delegate.md) property of an appropriate [UIPresentationController](uipresentationcontroller.md) object. Your delegate can suggest a new presentation style or an entirely new view controller for displaying content. For more information about using the delegate to respond to size class changes, see [UIPresentationController](uipresentationcontroller.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIPopoverPresentationControllerDelegate](uipopoverpresentationcontrollerdelegate.md), [UISheetPresentationControllerDelegate](uisheetpresentationcontrollerdelegate.md)

## Topics

### Adapting the presentation style

- [- adaptivePresentationStyleForPresentationController:traitCollection:](<uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for_traitcollection_).md>) — Asks the delegate for the presentation style to use when the specified set of traits are active.
- [- adaptivePresentationStyleForPresentationController:](<uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for_).md>) — Asks the delegate for the new presentation style to use.

### Adapting the view controller

- [- presentationController:viewControllerForAdaptivePresentationStyle:](<uiadaptivepresentationcontrollerdelegate/presentationcontroller(__viewcontrollerforadaptivepresentationstyle_).md>) — Asks the delegate for the view controller to display when adapting to the specified presentation style.

### Responding to adaptive transitions

- [- presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:](<uiadaptivepresentationcontrollerdelegate/presentationcontroller(__willpresentwithadaptivestyle_transitioncoordinator_).md>) — Notifies the delegate that an adaptivity-related transition is about to occur.
- [- presentationControllerDidAttemptToDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(__).md>) — Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [- presentationControllerShouldDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(__).md>) — Asks the delegate for permission to dismiss the presentation.
- [- presentationControllerDidDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(__).md>) — Notifies the delegate after a presentation is dismissed.
- [- presentationControllerWillDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(__).md>) — Notifies the delegate before a presentation is dismissed.

### Preparing the adaptive presentation controller

- [- presentationController:prepareAdaptivePresentationController:](<uiadaptivepresentationcontrollerdelegate/presentationcontroller(__prepare_).md>) — Provides an opportunity to configure the adaptive presentation controller after an adaptivity change.

## See Also

### Adaptivity

- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
