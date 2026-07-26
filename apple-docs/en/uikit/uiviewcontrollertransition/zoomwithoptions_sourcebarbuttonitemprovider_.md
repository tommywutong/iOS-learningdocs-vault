---
title: 'zoomWithOptions:sourceBarButtonItemProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransition/zoomwithoptions:sourcebarbuttonitemprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransition/zoomwithoptions:sourcebarbuttonitemprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransition/zoomwithoptions%3Asourcebarbuttonitemprovider%3A.json'
content_hash: 'sha256:c18f8db8fa25a249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Transition](../uiviewcontroller/transition.md)

# zoomWithOptions:sourceBarButtonItemProvider:

<sub>Type Method</sub>

Zoom from the `UIBarButtonItem` provided by the `sourceBarButtonItemProvider` to the presented or pushed view controller’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) zoomWithOptions:(UIZoomTransitionOptions *) options sourceBarButtonItemProvider:(UIBarButtonItem * (^)(UIZoomTransitionSourceViewProviderContext *)) sourceBarButtonItemProvider;
```
