---
title: 'CATransform3DInvert(_:)'
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransform3dinvert(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3dinvert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3dinvert%28_%3A%29.json'
content_hash: 'sha256:b6df7bdadb47cb29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3DInvert(_:)

<sub>Function</sub>

Inverts `t` and returns the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CATransform3DInvert(_ t: CATransform3D) -> CATransform3D
```

## Discussion

Returns the original matrix if `t` has no inverse.
