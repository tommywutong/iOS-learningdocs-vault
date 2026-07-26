---
title: 'presentationController(_:prepare:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:prepare:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:prepare:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller%28_%3Aprepare%3A%29.json'
content_hash: 'sha256:5a5f77108ef788ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# presentationController(_:prepare:)

<sub>Instance Method</sub>

Provides an opportunity to configure the adaptive presentation controller after an adaptivity change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationController(_ presentationController: UIPresentationController, prepare adaptivePresentationController: UIPresentationController)
```

## Parameters

- `presentationController` — The presentation controller that is managing the adaptivity change.

- `adaptivePresentationController` — The adaptive presentation controller to prepare. Configure this presentation controller’s properties as necessary before it presents.

## Discussion

The system calls this method during adaptation so the delegate can configure properties of the adaptive presentation controller before it presents.

For example, the system automatically adapts a view controller that presents as a popover in standard size classes to a sheet in compact size classes. You can implement this method to customize the sheet’s properties before it presents.
