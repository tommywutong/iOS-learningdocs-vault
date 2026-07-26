---
title: contentUnavailableConfigurationState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-9bvga
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-9bvga'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-9bvga.json'
content_hash: 'sha256:b29b3a2196d8987d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# contentUnavailableConfigurationState

<sub>Instance Property</sub>

Returns the current content unavailable configuration state for the view. To add your own custom state(s), override the getter and call super to obtain an instance with the system properties set, then set your own custom states as desired.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) UIContentUnavailableConfigurationState * contentUnavailableConfigurationState;
```

## See Also

### Indicating missing content

- [contentUnavailableConfiguration](contentunavailableconfiguration-6kqfk.md) — Setting a content unavailable configuration replaces the existing content unavailable view of the view controller with a new content unavailable view instance from the configuration, or directly applies the configuration to the existing content unavailable view if the configuration is compatible with the existing content unavailable view type. The default value is nil.
- [- setNeedsUpdateContentUnavailableConfiguration](<setneedsupdatecontentunavailableconfiguration().md>) — Requests that the system update the content-unavailable configuration for the latest state.
- [updateContentUnavailableConfigurationUsingState:](updatecontentunavailableconfigurationusingstate_.md) — Updates the content-unavailable configuration for the provided state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-c.class.md) — A content configuration for a content-unavailable view.
