---
title: traitOverrides
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/traitoverrides-1z1cc
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/traitoverrides-1z1cc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/traitoverrides-1z1cc.json'
content_hash: 'sha256:fcf35cabc1544c0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# traitOverrides

<sub>Instance Property</sub>

A mutable container of traits you use to set trait changes for this view controller and its views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var traitOverrides: UITraitOverrides { get set }
```

## See Also

### Overriding trait values

- [UITraitOverrides](../uitraitoverrides-swift.struct.md) — A mutable container of traits you use to set trait changes for an object and its descendants.
- [- updateTraitsIfNeeded](<updatetraitsifneeded().md>) — Updates traits immediately for this view controller and its view, including any view controllers and views in this subtree.
