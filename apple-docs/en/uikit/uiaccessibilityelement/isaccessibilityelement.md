---
title: isAccessibilityElement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityelement/isaccessibilityelement
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement/isaccessibilityelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement/isaccessibilityelement.json'
content_hash: 'sha256:ccc1772671cc62c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityElement](../uiaccessibilityelement.md)

# isAccessibilityElement

<sub>Instance Property</sub>

A Boolean value indicating whether the item is an accessibility element an assistive application can access.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isAccessibilityElement: Bool { get set }
```

## Discussion

The default value for this property is [false](../../swift/false.md). If the receiver is a UIKit control, the default value is [true](../../swift/true.md).
