---
title: UIViewController.Transition.ZoomSourceViewProviderContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition/zoomsourceviewprovidercontext
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomsourceviewprovidercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoomsourceviewprovidercontext.json'
content_hash: 'sha256:53a407fd14c606bd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIViewController](../../uiviewcontroller.md) · [Transition](../transition.md)

# UIViewController.Transition.ZoomSourceViewProviderContext

<sub>Class</sub>

A context object that contains references to the view controllers from a zoom transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class ZoomSourceViewProviderContext
```

## Relationships

- **Inherits From**: [NSObject](../../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the view controllers

- [sourceViewController](zoomsourceviewprovidercontext/sourceviewcontroller.md) — The view controller that presents the zoomed view.
- [zoomedViewController](zoomsourceviewprovidercontext/zoomedviewcontroller.md) — The view controller for the presented view.

## See Also

### Creating zoom transitions

- [zoom(options:sourceViewProvider:)](<zoom(options_sourceviewprovider_).md>) — Creates a zoom transition from the view that the source provider specifies.
- [ZoomOptions](zoomoptions.md) — Options for a zoom transition.
