---
title: annotation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+（26.0 起废弃）, iPadOS 9.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/openurloptionskey/annotation
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/annotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openurloptionskey/annotation.json'
content_hash: 'sha256:eac141cd7c391997'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [OpenURLOptionsKey](../openurloptionskey.md)

# annotation

<sub>Type Property</sub>

A key containing the information passed to a document interaction controller object’s annotation property.

> [!warning] Deprecated
> Use UIScene lifecycle and UISceneOpenURLOptions.annotation from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let annotation: UIApplication.OpenURLOptionsKey
```

## Discussion

The value of this key is a property list-typed object.

## See Also

### Accessing open-URL options

- [UIApplicationOpenURLOptionsSourceApplicationKey](sourceapplication.md) — A key containing the bundle ID of the app that sent the open-URL request to your app. _(deprecated)_
- [UIApplicationOpenURLOptionsOpenInPlaceKey](openinplace.md) — A key containing a flag that indicates whether a document must be copied before you use it. _(deprecated)_
- [UIApplicationOpenURLOptionsEventAttributionKey](eventattribution.md) — An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open. _(deprecated)_
