---
title: UIAccelerometerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: []
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiaccelerometerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiaccelerometerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccelerometerdelegate.json'
content_hash: 'sha256:b56f6888abce9f01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccelerometerDelegate

<sub>Protocol</sub>

The interface for receiving acceleration-related data from the system.

> [!warning] Deprecated
> Use the [Core Motion](../coremotion.md) framework instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UIAccelerometerDelegate <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to acceleration events

- [accelerometer:didAccelerate:](uiaccelerometerdelegate/accelerometer_didaccelerate_.md) — Delivers the latest acceleration data to the delegate. _(deprecated)_

## See Also

### Deprecated protocols

- [UIActionSheetDelegate](uiactionsheetdelegate.md) — The interface for the delegate of an action sheet object. _(deprecated)_
- [UIAlertViewDelegate](uialertviewdelegate.md) — The interface for the delegate of an alert view object. _(deprecated)_
- [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md) — The interface for the delegate of a popover controller object. _(deprecated)_
- [UISearchDisplayDelegate](uisearchdisplaydelegate.md) — The interface for the delegate of a search display controller. _(deprecated)_
- [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) — A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch. _(deprecated)_
- [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) — A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch. _(deprecated)_
