---
title: 'containerConcentric(minimum:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicornerradius-swift.struct/containerconcentric(minimum:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicornerradius-swift.struct/containerconcentric(minimum:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerradius-swift.struct/containerconcentric%28minimum%3A%29.json'
content_hash: 'sha256:45a83cfc35bfcaf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICornerRadius](../uicornerradius-swift.struct.md)

# containerConcentric(minimum:)

<sub>Type Method</sub>

A dynamic corner radius calculated using the geometry of the view and its container limited to a minimum radius.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func containerConcentric(minimum: CGFloat? = nil) -> UICornerRadius
```

## Parameters

- `minimum` — An optional float value that represents a minimum radius, expressed in points.

## See Also

### Defining a radius

- [fixed(_:)](<fixed(__).md>) — Creates a radius that represents a fixed corner radius in points.
