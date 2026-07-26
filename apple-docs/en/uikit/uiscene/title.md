---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/title
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/title.json'
content_hash: 'sha256:15218c53ee6cd5f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# title

<sub>Instance Property</sub>

A user-visible string you supply to help users differentiate among your app’s scenes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String! { get set }
```

## Discussion

The system displays this string in the app switcher to make it easier for the user to differentiate among your app’s scenes. Set this property to an empty string if you don’t want the app switcher to display anything for the scene.

iPad and iPhone apps running on a Mac with Apple silicon and apps built with Mac Catalyst display the title in the title bar of the scene’s window.

## See Also

### Getting the scene attributes

- [activationState](activationstate-swift.property.md) — The current execution state of the scene.
- [ActivationState](activationstate-swift.enum.md) — Constants that indicate the foreground or background execution state of your app.
- [subtitle](subtitle.md) — A string that the app displays in the title bar of a window when running in macOS.
