---
title: options
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationconfiguration/options
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationconfiguration/options.json'
content_hash: 'sha256:a325c08b43c0910a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationConfiguration](../activationconfiguration.md)

# options

<sub>Instance Property</sub>

Options for customizing the scene request.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var options: UIWindowScene.ActivationRequestOptions? { get set }
```

## Discussion

This property is optional. If you don’t specify options, the system requests a scene using the default options.

## See Also

### Getting information about the activation configuration

- [userActivity](useractivity.md) — The user activity used to request a scene.
- [ActivationRequestOptions](../activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [preview](preview.md) — An optional targeted preview that the system uses to animate the transition to the new scene.
