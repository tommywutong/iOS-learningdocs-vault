---
title: activityItemsConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationproviding/activityitemsconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationproviding/activityitemsconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationproviding/activityitemsconfiguration.json'
content_hash: 'sha256:e8024264af6f7f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfigurationProviding](../uiactivityitemsconfigurationproviding.md)

# activityItemsConfiguration

<sub>Instance Property</sub>

An object or value that specifies items to share.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)? { get }
```

## Discussion

To offer a configuration for sharing through Siri or the toolbar in an app built with Mac Catalyst, override this property on the root view controller or a modal view controller. To provide a configuration when your app is displaying a [UISplitViewController](../uisplitviewcontroller.md), implement this property on the detail view controller.

To offer a configuration for sharing through a context menu, override this property on your [UIView](../uiview.md) subclass, and attach a [UIContextMenuInteraction](../uicontextmenuinteraction.md) to that view.

> [!note] Note
> When the user asks Siri to “share this” on iOS, if both [activityItemsConfiguration](activityitemsconfiguration.md) and [activityItemsConfigurationSource](../uiwindowscene/activityitemsconfigurationsource.md) are `nil`, the system uses the [webpageURL](../../foundation/nsuseractivity/webpageurl.md) property on your app’s current [userActivity](../uiresponder/useractivity.md) to create shareable content. The system doesn’t offer this fallback behavior in an app built with Mac Catalyst.
