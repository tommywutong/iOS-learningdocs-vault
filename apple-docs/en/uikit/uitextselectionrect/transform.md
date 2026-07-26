---
title: transform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionrect/transform
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionrect/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionrect/transform.json'
content_hash: 'sha256:bfb12a021e473d38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionRect](../uitextselectionrect.md)

# transform

<sub>Instance Property</sub>

Custom transform for highlight rects. This transform is assumed to be in the `textInputView` coordinate space. Default is CGAffineTransformIdentity (no transform applied).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transform: CGAffineTransform { get }
```
