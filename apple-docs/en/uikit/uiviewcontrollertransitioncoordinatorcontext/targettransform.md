---
title: targetTransform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/targettransform
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/targettransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/targettransform.json'
content_hash: 'sha256:4bd89e40ffd490a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# targetTransform

<sub>Instance Property</sub>

Returns a transform indicating the amount of rotation being applied during the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var targetTransform: CGAffineTransform { get }
```

## Return Value

An affine transform indicating the amount of rotation being applied to the interface. This transform is the identity transform when no rotation is applied; otherwise, it is a transform that applies a 90 degree, -90 degree, or 180 degree rotation.
