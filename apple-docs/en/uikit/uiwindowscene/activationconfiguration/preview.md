---
title: preview
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationconfiguration/preview
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/preview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationconfiguration/preview.json'
content_hash: 'sha256:ea0d890ea9a377f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationConfiguration](../activationconfiguration.md)

# preview

<sub>Instance Property</sub>

An optional targeted preview that the system uses to animate the transition to the new scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preview: UITargetedPreview? { get set }
```

## See Also

### Getting information about the activation configuration

- [userActivity](useractivity.md) — The user activity used to request a scene.
- [options](options.md) — Options for customizing the scene request.
- [ActivationRequestOptions](../activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
