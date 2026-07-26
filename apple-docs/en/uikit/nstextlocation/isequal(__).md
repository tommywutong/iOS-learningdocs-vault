---
title: 'isEqual(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlocation/isequal(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlocation/isequal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlocation/isequal%28_%3A%29.json'
content_hash: 'sha256:7726c7d55616912c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLocation](../nstextlocation.md)

# isEqual(_:)

<sub>Instance Method</sub>

Returns `true` for locations representing the same document position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(_ location: Any?) -> Bool
```

## Discussion

Must not depend on auxiliary state such as affinity or visual-edge preference. Locations from different data source methods are compared using `isEqual:` and must agree when they refer to the same position.
