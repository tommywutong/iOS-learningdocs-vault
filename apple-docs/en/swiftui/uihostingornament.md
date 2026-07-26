---
title: UIHostingOrnament
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingornament
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingornament'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingornament.json'
content_hash: 'sha256:e0d261ee6986c2e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIHostingOrnament

<sub>Class</sub>

A model that represents an ornament suitable for being hosted in UIKit.

<sub>visionOS</sub>

```swift
class UIHostingOrnament<Content> where Content : View
```

## Overview

Use a `UIHostingOrnament` when you want to add ornaments to a UIKit view controller. For example, the following adds a single bottom ornament to the current view controller:

```swift
self.ornaments = [
    UIHostingOrnament(sceneAnchor: .bottom) {
        OrnamentContent()
    }
]
```

## Relationships

- **Inherits From**: [UIOrnament](uiornament.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a hosting ornament

- [init(sceneAnchor:contentAlignment:content:)](<uihostingornament/init(sceneanchor_contentalignment_content_).md>) — Creates an ornament with the specified alignment and content.
- [rootView](uihostingornament/rootview.md) — The root view of the SwiftUI view hierarchy managed by this ornament.

### Setting the alignment

- [contentAlignment](uihostingornament/contentalignment.md) — The alignment in the ornament used to position it.
- [sceneAnchor](uihostingornament/sceneanchor.md) — The anchor point for aligning the ornament’s content (based on the `contentAlignment`) with the scene.

### Instance Properties

- [contentAlignment3D](uihostingornament/contentalignment3d.md)

## See Also

### Hosting an ornament in UIKit

- [UIOrnament](uiornament.md) — The abstract base class that represents an ornament.
