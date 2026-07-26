---
title: activityItemsConfigurationSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activityitemsconfigurationsource
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activityitemsconfigurationsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activityitemsconfigurationsource.json'
content_hash: 'sha256:786022063de41d23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# activityItemsConfigurationSource

<sub>Instance Property</sub>

An object that can provide shareable items for a scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var activityItemsConfigurationSource: (any UIActivityItemsConfigurationProviding)? { get set }
```

## Discussion

When a user asks Siri to “share this” on iOS, or clicks an [NSSharingServicePickerToolbarItem](../../appkit/nssharingservicepickertoolbaritem.md) in the toolbar of an app built with Mac Catalyst, the system asks the current scene or view controller what to share. You can supply multiple representations of the current content, such as a file, image, and URL.

You can implement this property or provide configurations from view controllers with [activityItemsConfiguration](../uiactivityitemsconfigurationproviding/activityitemsconfiguration.md).

If you don’t provide a [UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md) in either of these ways, the system may fall back to sharing either the [webpageURL](../../foundation/nsuseractivity/webpageurl.md) of your app’s current user activity or a screenshot of the scene.

## See Also

### Sharing content

- [UIActivityItemsConfigurationProviding](../uiactivityitemsconfigurationproviding.md) — An interface that provides a source for shareable content to fulfill user requests to share current content.
