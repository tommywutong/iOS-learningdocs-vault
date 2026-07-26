---
title: updateTraitsIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/updatetraitsifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/updatetraitsifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/updatetraitsifneeded%28%29.json'
content_hash: 'sha256:01539605b33c6922'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# updateTraitsIfNeeded()

<sub>Instance Method</sub>

Updates traits immediately for this view controller and its view, including any view controllers and views in this subtree.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateTraitsIfNeeded()
```

## Discussion

The system sends trait change callbacks synchronously.

## See Also

### Overriding trait values

- [traitOverrides](traitoverrides-1z1cc.md) — A mutable container of traits you use to set trait changes for this view controller and its views.
- [UITraitOverrides](../uitraitoverrides-swift.struct.md) — A mutable container of traits you use to set trait changes for an object and its descendants.
