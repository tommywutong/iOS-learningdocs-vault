---
title: overrideTraitCollection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（17.0 起废弃）, iPadOS 8.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipresentationcontroller/overridetraitcollection
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/overridetraitcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/overridetraitcollection.json'
content_hash: 'sha256:ea75741b05b21bbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# overrideTraitCollection

<sub>Instance Property</sub>

Interface traits for the presented view controller, to use in place of traits from the iOS environment.

> [!warning] Deprecated
> Use [traitOverrides](traitoverrides-629ka.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var overrideTraitCollection: UITraitCollection? { get set }
```

## Discussion

Use this property to provide an interface trait collection for the presented view controller, overriding one or more values in the iOS trait environment.

Each value you place in the [overrideTraitCollection](overridetraitcollection.md) property overrides the corresponding value in the iOS trait environment. For example, the following code snippet shows how to override the display scale for the presented view controller, leaving other traits as they are provided by the system. Place such code, typically, in the implementation file for the presenting view controller:

```objc
presentedVC.presentationController.overrideTraitCollection = [UITraitCollection traitCollectionWithDisplayScale: 1.5];
[self presentViewController: presentedVC animated: NO completion: nil];
```

The _presenting_ view controller is not affected by use of this property.

The default value of the [overrideTraitCollection](overridetraitcollection.md) property is `nil`, which results in the full iOS trait environment being used by the presented view controller.
