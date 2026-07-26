---
title: 'init(appIdentifier:position:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlay/appconfiguration/init(appidentifier:position:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/init(appidentifier:position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/appconfiguration/init%28appidentifier%3Aposition%3A%29.json'
content_hash: 'sha256:50d920e4fad0df49'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKOverlay](../../skoverlay.md) · [AppConfiguration](../appconfiguration.md)

# init(appIdentifier:position:)

<sub>Initializer</sub>

Creates an object that represents the attributes of an overlay you use to recommend another app on the App Store.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(appIdentifier: String, position: SKOverlay.Position)
```

## Parameters

- `appIdentifier` — The iTunes identifier of the recommended app.

- `position` — The position of the overlay on the screen.

## See Also

### Creating an App Configuration

- [appIdentifier](appidentifier.md) — The iTunes identifier of the recommended app.
- [position](position.md) — The position of the overlay on the screen.
- [Position](../position.md) — Constants that identify the position of an overlay on the screen.
