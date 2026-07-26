---
title: 'presentationController(forPresented:presenting:source:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioningdelegate/presentationcontroller(forpresented:presenting:source:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/presentationcontroller(forpresented:presenting:source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioningdelegate/presentationcontroller%28forpresented%3Apresenting%3Asource%3A%29.json'
content_hash: 'sha256:ac09f729a53ce8a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md)

# presentationController(forPresented:presenting:source:)

<sub>Instance Method</sub>

Asks your delegate for the custom presentation controller to use for managing the view hierarchy when presenting a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationController(forPresented presented: UIViewController, presenting: UIViewController?, source: UIViewController) -> UIPresentationController?
```

## Parameters

- `presented` — The view controller being presented.

- `presenting` — The view controller that is presenting the view controller in the `presented` parameter. The object in this parameter could be the root view controller of the window, a parent view controller that is marked as defining the current context, or the last view controller that was presented. This view controller may or may not be the same as the one in the `source` parameter. This parameter may also be `nil` to indicate that the presenting view controller will be determined later.

- `source` — The view controller whose [- presentViewController:animated:completion:](<../uiviewcontroller/present(__animated_completion_).md>) method was called to initiate the presentation process.

## Return Value

The custom presentation controller for managing the modal presentation.

## Discussion

When you present a view controller using the [UIModalPresentationCustom](../uimodalpresentationstyle/custom.md) presentation style, the system calls this method and asks for the presentation controller that manages your custom style. If you implement this method, use it to create and return the custom presentation controller object that you want to use to manage the presentation process.

If you don’t implement this method, or if your implementation of this method returns `nil`, the system uses a default presentation controller object. The default presentation controller doesn’t add any views or content to the view hierarchy.
