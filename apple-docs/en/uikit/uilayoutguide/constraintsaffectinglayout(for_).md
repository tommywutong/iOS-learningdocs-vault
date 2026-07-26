---
title: 'constraintsAffectingLayout(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilayoutguide/constraintsaffectinglayout(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguide/constraintsaffectinglayout(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguide/constraintsaffectinglayout%28for%3A%29.json'
content_hash: 'sha256:f1684b0ff2d02001'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutGuide](../uilayoutguide.md)

# constraintsAffectingLayout(for:)

<sub>Instance Method</sub>

The constraints that impact the layout of the guide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraintsAffectingLayout(for axis: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]
```

## See Also

### Debugging the layout guide

- [hasAmbiguousLayout](hasambiguouslayout.md) — A Boolean value indicating whether the constraints impacting the layout guide specify its location ambiguously.
