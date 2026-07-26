---
title: gestureRecognizers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/gesturerecognizers
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/gesturerecognizers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/gesturerecognizers.json'
content_hash: 'sha256:a8dc01216efef723'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# gestureRecognizers

<sub>Instance Property</sub>

The gesture recognizers that are receiving the touch object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var gestureRecognizers: [UIGestureRecognizer]? { get }
```

## Discussion

The objects in the array are instances of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md). If there are no gesture recognizers currently receiving the touch, this property contains an empty array.
