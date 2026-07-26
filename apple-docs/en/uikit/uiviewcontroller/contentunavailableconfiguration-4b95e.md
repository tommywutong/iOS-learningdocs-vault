---
title: contentUnavailableConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/contentunavailableconfiguration-4b95e
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/contentunavailableconfiguration-4b95e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/contentunavailableconfiguration-4b95e.json'
content_hash: 'sha256:063855b8e07b9403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# contentUnavailableConfiguration

<sub>Instance Property</sub>

The current content-unavailable configuration of the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var contentUnavailableConfiguration: (any UIContentConfiguration)? { get set }
```

## Discussion

Use this property to configure a content-unavailable view that the view controller manages. The value of this property is commonly an instance of [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md), but you can use other types of content configuration, including a [UIHostingConfiguration](../../swiftui/uihostingconfiguration.md), to display a SwiftUI view.

## See Also

### Indicating missing content

- [contentUnavailableConfigurationState](contentunavailableconfigurationstate-7sczw.md) — The current configuration state of the content-unavailable view.
- [- setNeedsUpdateContentUnavailableConfiguration](<setneedsupdatecontentunavailableconfiguration().md>) — Requests that the system update the content-unavailable configuration for the latest state.
- [updateContentUnavailableConfiguration(using:)](<updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md) — A content configuration for a content-unavailable view.
