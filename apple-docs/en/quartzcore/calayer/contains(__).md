---
title: 'contains(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/contains(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/contains%28_%3A%29.json'
content_hash: 'sha256:cad1e389fcb0f0ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# contains(_:)

<sub>Instance Method</sub>

Returns whether the receiver contains a specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func contains(_ p: CGPoint) -> Bool
```

## Parameters

- `p` — A point in the receiver’s coordinate system.

## Return Value

[true](../../swift/true.md) if the bounds of the layer contains the point.

## See Also

### Hit testing

- [- hitTest:](<hittest(__).md>) — Returns the farthest descendant of the receiver in the layer hierarchy (including itself) that contains the specified point.
