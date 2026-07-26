---
title: UIApplication.OpenURLOptionsKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+（26.0 起废弃）, iPadOS 9.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/openurloptionskey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openurloptionskey.json'
content_hash: 'sha256:d8268792dbd3f9de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.OpenURLOptionsKey

<sub>Structure</sub>

Keys you use to access values in the options dictionary when opening a URL.

> [!warning] Deprecated
> Use UIScene lifecycle and equivalent properties on UISceneOpenURLOptions from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct OpenURLOptionsKey
```

## Overview

Use these keys to retrieve options in the [- application:openURL:options:](<../uiapplicationdelegate/application(__open_options_).md>) method of your app delegate.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessing open-URL options

- [UIApplicationOpenURLOptionsSourceApplicationKey](openurloptionskey/sourceapplication.md) — A key containing the bundle ID of the app that sent the open-URL request to your app. _(deprecated)_
- [UIApplicationOpenURLOptionsAnnotationKey](openurloptionskey/annotation.md) — A key containing the information passed to a document interaction controller object’s annotation property. _(deprecated)_
- [UIApplicationOpenURLOptionsOpenInPlaceKey](openurloptionskey/openinplace.md) — A key containing a flag that indicates whether a document must be copied before you use it. _(deprecated)_
- [UIApplicationOpenURLOptionsEventAttributionKey](openurloptionskey/eventattribution.md) — An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open. _(deprecated)_

### Creating an open-URL options key

- [init(rawValue:)](<openurloptionskey/init(rawvalue_).md>) — Creates a URL-opening options key with the specified raw value. _(deprecated)_

## See Also

### Opening a URL-specified resource

- [- application:openURL:options:](<../uiapplicationdelegate/application(__open_options_).md>) — Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options. _(deprecated)_
