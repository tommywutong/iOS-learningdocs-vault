---
title: UIViewController.Transition.ZoomOptions.AlignmentRectContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectcontext
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectcontext.json'
content_hash: 'sha256:db29c0f6a5ea3acf'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIViewController](../../../uiviewcontroller.md) · [Transition](../../transition.md) · [ZoomOptions](../zoomoptions.md)

# UIViewController.Transition.ZoomOptions.AlignmentRectContext

<sub>Class</sub>

An object that contains a zoom transition’s starting and ending views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class AlignmentRectContext
```

## Relationships

- **Inherits From**: [NSObject](../../../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../../swift/customstringconvertible.md), [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [NSObjectProtocol](../../../../objectivec/nsobjectprotocol.md)

## Topics

### Accessing views

- [sourceView](alignmentrectcontext/sourceview.md) — The zoomed-out view, for example a thumbnail image.
- [zoomedViewController](alignmentrectcontext/zoomedviewcontroller.md) — The zoomed in view.

## See Also

### Setting options

- [alignmentRectProvider](alignmentrectprovider.md) — A closure that returns the alignment rectangle for the starting and ending views.
- [dimmingColor](dimmingcolor.md) — The dimming color.
- [dimmingVisualEffect](dimmingvisualeffect.md) — The dimming visual effect.
