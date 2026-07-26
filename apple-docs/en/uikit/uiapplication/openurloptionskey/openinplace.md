---
title: openInPlace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+（26.0 起废弃）, iPadOS 9.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/openurloptionskey/openinplace
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/openinplace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openurloptionskey/openinplace.json'
content_hash: 'sha256:314e5ac5b01f016d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [OpenURLOptionsKey](../openurloptionskey.md)

# openInPlace

<sub>Type Property</sub>

A key containing a flag that indicates whether a document must be copied before you use it.

> [!warning] Deprecated
> Use UIScene lifecycle and UISceneOpenURLOptions.openInPlace from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let openInPlace: UIApplication.OpenURLOptionsKey
```

## Discussion

When the value of this property is [false](../../../swift/false.md), you must copy the document to maintain access to it. If the flag is not set, you also must copy the document before you can use it.

If the document does not need to be copied, you can open it in place in your implementation of the [- application:openURL:options:](<../../uiapplicationdelegate/application(__open_options_).md>) method. For information about declaring whether your app wants the ability to open iCloud Drive documents in place, see the description of the [LSSupportsOpeningDocumentsInPlace](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW13) information property list key. For an example of an app that opens iCloud Drive documents in place, see [ShapeEdit: Building a Simple iCloud Document App](https://developer.apple.com/library/archive/samplecode/ShapeEdit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016100).

## See Also

### Accessing open-URL options

- [UIApplicationOpenURLOptionsSourceApplicationKey](sourceapplication.md) — A key containing the bundle ID of the app that sent the open-URL request to your app. _(deprecated)_
- [UIApplicationOpenURLOptionsAnnotationKey](annotation.md) — A key containing the information passed to a document interaction controller object’s annotation property. _(deprecated)_
- [UIApplicationOpenURLOptionsEventAttributionKey](eventattribution.md) — An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open. _(deprecated)_
