---
title: gestureRecognizers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/gesturerecognizers
source_url: 'https://developer.apple.com/documentation/uikit/uipress/gesturerecognizers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/gesturerecognizers.json'
content_hash: 'sha256:96aabd5e72bc6e63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# gestureRecognizers

<sub>Instance Property</sub>

The gesture recognizers that are receiving the press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var gestureRecognizers: [UIGestureRecognizer]? { get }
```

## Discussion

The objects held in this array are instances of a subclass of the abstract base class, [UIGestureRecognizer](../uigesturerecognizer.md). If there are no gesture recognizers currently receiving the touch objects, this property holds an empty array.

## See Also

### Getting a press object’s gesture recognizers

- [force](force.md) — The force of the button press.
