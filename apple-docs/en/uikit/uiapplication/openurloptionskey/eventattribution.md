---
title: eventAttribution
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.5+（26.0 起废弃）, iPadOS 14.5+（26.0 起废弃）, Mac Catalyst 14.5+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/openurloptionskey/eventattribution
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/eventattribution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openurloptionskey/eventattribution.json'
content_hash: 'sha256:aa7c70080ba5c478'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [OpenURLOptionsKey](../openurloptionskey.md)

# eventAttribution

<sub>Type Property</sub>

An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open.

> [!warning] Deprecated
> Use UIScene lifecycle and UISceneOpenURLOptions.eventAttribution from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let eventAttribution: UIApplication.OpenURLOptionsKey
```

## See Also

### Accessing open-URL options

- [UIApplicationOpenURLOptionsSourceApplicationKey](sourceapplication.md) — A key containing the bundle ID of the app that sent the open-URL request to your app. _(deprecated)_
- [UIApplicationOpenURLOptionsAnnotationKey](annotation.md) — A key containing the information passed to a document interaction controller object’s annotation property. _(deprecated)_
- [UIApplicationOpenURLOptionsOpenInPlaceKey](openinplace.md) — A key containing a flag that indicates whether a document must be copied before you use it. _(deprecated)_
