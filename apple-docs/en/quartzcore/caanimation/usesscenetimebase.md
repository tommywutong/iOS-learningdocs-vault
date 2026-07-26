---
title: usesSceneTimeBase
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimation/usesscenetimebase
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/usesscenetimebase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/usesscenetimebase.json'
content_hash: 'sha256:48107dd23c172d10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# usesSceneTimeBase

<sub>Instance Property</sub>

For animations attached to SceneKit objects, a Boolean value that determines whether the animation is evaluated using the scene time or the system time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var usesSceneTimeBase: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), animation timing is governed by the currentTime property of the view, layer, or custom renderer responsible for drawing the scene. The default value is [false](../../swift/false.md).

To attach animations to SceneKit objects, see [SCNAnimatable](../../scenekit/scnanimatable.md).
