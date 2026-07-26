---
title: 'zoom(options:sourceViewProvider:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/transition/zoom(options:sourceviewprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoom(options:sourceviewprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoom%28options%3Asourceviewprovider%3A%29.json'
content_hash: 'sha256:02392b579cdc6e80'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIViewController](../../uiviewcontroller.md) · [Transition](../transition.md)

# zoom(options:sourceViewProvider:)

<sub>Type Method</sub>

Creates a zoom transition from the view that the source provider specifies.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func zoom(options: UIViewController.Transition.ZoomOptions? = nil, sourceViewProvider: @escaping (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self
```

## Parameters

- `options` — Additional options for the zoom transition.

- `sourceViewProvider` — A closure that returns the view, for example a thumbnail image, that the animation zooms out from and zooms back in to.

## Discussion

The system calls the source view provider when it presents and when it dismisses the view controller. In the closure, return the [UIView](../../uiview.md) that the animation should zoom in from or zoom back out to, respectively. For more information, see [Enhancing your app with fluid transitions](../../enhancing-your-app-with-fluid-transitions.md).

## See Also

### Creating zoom transitions

- [ZoomOptions](zoomoptions.md) — Options for a zoom transition.
- [ZoomSourceViewProviderContext](zoomsourceviewprovidercontext.md) — A context object that contains references to the view controllers from a zoom transition.
