---
title: contentUnavailableConfigurationState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-7sczw
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-7sczw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-7sczw.json'
content_hash: 'sha256:61de7be6632ff253'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# contentUnavailableConfigurationState

<sub>Instance Property</sub>

The current configuration state of the content-unavailable view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @objc(_bridgedContentUnavailableConfigurationState) @preconcurrency dynamic var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState { get }
```

## Discussion

You can customize the configuration state by overriding this property in your subclass. Obtain the system instance from the superclass, and customize the state as appropriate.

## See Also

### Indicating missing content

- [contentUnavailableConfiguration](contentunavailableconfiguration-4b95e.md) — The current content-unavailable configuration of the view controller.
- [- setNeedsUpdateContentUnavailableConfiguration](<setneedsupdatecontentunavailableconfiguration().md>) — Requests that the system update the content-unavailable configuration for the latest state.
- [updateContentUnavailableConfiguration(using:)](<updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md) — A content configuration for a content-unavailable view.
