---
title: 'init(presentedViewController:presenting:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipresentationcontroller/init(presentedviewcontroller:presenting:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/init(presentedviewcontroller:presenting:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/init%28presentedviewcontroller%3Apresenting%3A%29.json'
content_hash: 'sha256:b15e40da8e11b746'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# init(presentedViewController:presenting:)

<sub>Initializer</sub>

Initializes and returns a presentation controller for transitioning between the specified view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(presentedViewController: UIViewController, presenting presentingViewController: UIViewController?)
```

## Parameters

- `presentedViewController` — The view controller being presented modally.

- `presentingViewController` — The view controller whose content represents the starting point of the transition.

## Return Value

An initialized presentation controller object or `nil` if the presentation controller could not be initialized.

## Discussion

This method is the designated initializer for the presentation controller. You must call it from any custom initialization methods you define for your presentation controller subclasses.
