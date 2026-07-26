---
title: subtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/subtitle
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/subtitle.json'
content_hash: 'sha256:86675b3fdd43c3dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# subtitle

<sub>Instance Property</sub>

A string that the app displays in the title bar of a window when running in macOS.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var subtitle: String { get set }
```

## Discussion

When this property is an empty string, the system removes the subtitle from the window layout. The default value is an empty string.

> [!note] Note
> Apps running in iOS ignore the [subtitle](subtitle.md) property.

## See Also

### Getting the scene attributes

- [activationState](activationstate-swift.property.md) — The current execution state of the scene.
- [ActivationState](activationstate-swift.enum.md) — Constants that indicate the foreground or background execution state of your app.
- [title](title.md) — A user-visible string you supply to help users differentiate among your app’s scenes.
