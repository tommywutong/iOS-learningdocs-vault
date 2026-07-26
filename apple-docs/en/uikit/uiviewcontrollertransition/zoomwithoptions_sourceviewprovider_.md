---
title: 'zoomWithOptions:sourceViewProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransition/zoomwithoptions:sourceviewprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransition/zoomwithoptions:sourceviewprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransition/zoomwithoptions%3Asourceviewprovider%3A.json'
content_hash: 'sha256:342c97d12bb5089e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Transition](../uiviewcontroller/transition.md)

# zoomWithOptions:sourceViewProvider:

<sub>Type Method</sub>

Creates a zoom transition from the view specified by the source provider.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) zoomWithOptions:(UIZoomTransitionOptions *) options sourceViewProvider:(UIView * (^)(UIZoomTransitionSourceViewProviderContext *)) sourceViewProvider;
```

## Parameters

- `options` — Additional options for the zoom transition.

- `sourceViewProvider` — A closure that returns the view, for example a thumbnail image, that the animation zooms out from and zooms back in to.

## Discussion

The system calls the source view provider when it presents and when it dismisses the view controller. In the closure, return the [UIView](../uiview.md) that the animation should zoom in from or zoom back out to, respectively. For more information, see [Enhancing your app with fluid transitions](../enhancing-your-app-with-fluid-transitions.md).

## See Also

### Creating zoom transitions

- [ZoomOptions](../uiviewcontroller/transition/zoomoptions.md) — Options for a zoom transition.
- [ZoomSourceViewProviderContext](../uiviewcontroller/transition/zoomsourceviewprovidercontext.md) — A context object that contains references to the view controllers from a zoom transition.
