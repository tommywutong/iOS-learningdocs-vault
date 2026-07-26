---
title: UIViewController.Transition
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition.json'
content_hash: 'sha256:1a12aa0741a634c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# UIViewController.Transition

<sub>Class</sub>

An object that defines the transition animation when switching to a new view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class Transition
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating zoom transitions

- [zoom(options:sourceViewProvider:)](<transition/zoom(options_sourceviewprovider_).md>) — Creates a zoom transition from the view that the source provider specifies.
- [ZoomOptions](transition/zoomoptions.md) — Options for a zoom transition.
- [ZoomSourceViewProviderContext](transition/zoomsourceviewprovidercontext.md) — A context object that contains references to the view controllers from a zoom transition.

### Accessing transitions

- [coverVertical](transition/coververtical.md) — A transition where the new view slides up from the bottom of the screen.
- [crossDissolve](transition/crossdissolve.md) — A transition where the current view fades out while the new view fades in at the same time.
- [flipHorizontal](transition/fliphorizontal.md) — A transition where the current view flips horizontally to reveal the new view.
- [partialCurl](transition/partialcurl.md) — A transition where one corner of the current view curls up, revealing the new view underneath.

### Type Methods

- [zoom(options:sourceBarButtonItemProvider:)](<transition/zoom(options_sourcebarbuttonitemprovider_).md>)

## See Also

### Working with transitions

- [preferredTransition](preferredtransition.md) — An object that defines the transition animation when switching to the view controller.
