---
title: force
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/force
source_url: 'https://developer.apple.com/documentation/uikit/uipress/force'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/force.json'
content_hash: 'sha256:785a40205444cc2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# force

<sub>Instance Property</sub>

The force of the button press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var force: CGFloat { get }
```

## Discussion

While all buttons can be “down” or “up”, some physical buttons also have a notion of a “force” with which they’re pressed. For analog buttons, force returns a value between 0 and 1, and for digital buttons it returns 0 or 1.

## See Also

### Getting a press object’s gesture recognizers

- [gestureRecognizers](gesturerecognizers.md) — The gesture recognizers that are receiving the press.
