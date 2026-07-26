---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdatelink/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/isenabled.json'
content_hash: 'sha256:7abf28a5fbce0cf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the UI update link is monitoring UI updates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

By default, the value of this property is [true](../../swift/true.md), which means the system invokes the actions of the UI update link for each UI update.

When the value is [false](../../swift/false.md), the UI update link has no effect. Set the value to [false](../../swift/false.md) if you want to temporarily turn off the UI update link.
