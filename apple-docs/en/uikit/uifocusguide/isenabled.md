---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusguide/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uifocusguide/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusguide/isenabled.json'
content_hash: 'sha256:d09345d3fffb1943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusGuide](../uifocusguide.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the guide is focusable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md) (the default), then the guide may be focusable. Some conditions, defined by the system, may prevent the guide from being focusable even if it’s enabled, such as when the guide’s frame overlaps with the currently focused view. However, if this property is set to [false](../../swift/false.md), then the guide isn’t focusable.

## See Also

### Enabling focus

- [preferredFocusEnvironments](preferredfocusenvironments.md) — An array of focus environments to which the guide directs focus, ordered by priority.
- [preferredFocusedView](preferredfocusedview.md) — The view that the focus will be redirected to if this guide is focused. _(deprecated)_
