---
title: 'updateContentUnavailableConfigurationUsingState:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/updatecontentunavailableconfigurationusingstate:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/updatecontentunavailableconfigurationusingstate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/updatecontentunavailableconfigurationusingstate%3A.json'
content_hash: 'sha256:9ecf9571b68739e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# updateContentUnavailableConfigurationUsingState:

<sub>Instance Method</sub>

Updates the content-unavailable configuration for the provided state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) updateContentUnavailableConfigurationUsingState:(UIContentUnavailableConfigurationState *) state;
```

## Parameters

- `state` — The current configuration state for a content-unavailable view.

## Discussion

Override this method to update the value of [contentUnavailableConfiguration](contentunavailableconfiguration-6kqfk.md) as appropriate for the given state.

Don’t call this method directly. Instead, call [- setNeedsUpdateContentUnavailableConfiguration](<setneedsupdatecontentunavailableconfiguration().md>) to tell the system to request an update.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [view](view.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Indicating missing content

- [contentUnavailableConfiguration](contentunavailableconfiguration-6kqfk.md) — Setting a content unavailable configuration replaces the existing content unavailable view of the view controller with a new content unavailable view instance from the configuration, or directly applies the configuration to the existing content unavailable view if the configuration is compatible with the existing content unavailable view type. The default value is nil.
- [contentUnavailableConfigurationState](contentunavailableconfigurationstate-9bvga.md) — Returns the current content unavailable configuration state for the view. To add your own custom state(s), override the getter and call super to obtain an instance with the system properties set, then set your own custom states as desired.
- [- setNeedsUpdateContentUnavailableConfiguration](<setneedsupdatecontentunavailableconfiguration().md>) — Requests that the system update the content-unavailable configuration for the latest state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-c.class.md) — A content configuration for a content-unavailable view.
