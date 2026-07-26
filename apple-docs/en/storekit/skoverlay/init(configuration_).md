---
title: 'init(configuration:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlay/init(configuration:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/init(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/init%28configuration%3A%29.json'
content_hash: 'sha256:32d76be1745880f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# init(configuration:)

<sub>Initializer</sub>

Creates an overlay you use to recommend another app on the App Store.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(configuration: SKOverlay.Configuration)
```

## Parameters

- `configuration` — The object that represents the overlay’s attributes; for example, its position on the screen.

## Discussion

Pass an [AppConfiguration](appconfiguration.md) as the `configuration` parameter if you want to display the overlay in an app. To recommend an App Clip’s corresponding app, pass an [AppClipConfiguration](appclipconfiguration.md) object to the initializer. For more information, see [Recommending your app to App Clip users](../../appclip/recommending-your-app-to-app-clip-users.md).

## See Also

### Creating an overlay

- [configuration](configuration-swift.property.md) — An overlay’s attributes; for example, its position on the screen.
- [AppConfiguration](appconfiguration.md) — An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [AppClipConfiguration](appclipconfiguration.md) — An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [Configuration](configuration-swift.class.md) — The abstract superclass for all classes that represent an overlay’s attributes.
