---
title: 'init(userActivity:options:preview:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscene/activationconfiguration/init(useractivity:options:preview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/init(useractivity:options:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationconfiguration/init%28useractivity%3Aoptions%3Apreview%3A%29.json'
content_hash: 'sha256:bd01a6006a622864'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationConfiguration](../activationconfiguration.md)

# init(userActivity:options:preview:)

<sub>Initializer</sub>

Creates an activation configuration.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(userActivity: NSUserActivity, options: UIWindowScene.ActivationRequestOptions? = nil, preview: UITargetedPreview? = nil)
```

## Parameters

- `userActivity` — The user activity used to request a scene.

- `options` — Options for customizing the scene request. If you don’t provide options, the system uses the default options.

- `preview` — An optional targeted preview that the system uses to animate the transition to the new scene.
