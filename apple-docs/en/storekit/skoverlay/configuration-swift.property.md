---
title: configuration
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/configuration-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/configuration-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/configuration-swift.property.json'
content_hash: 'sha256:cc6fdc3fbc0e9b16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# configuration

<sub>Instance Property</sub>

An overlay’s attributes; for example, its position on the screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var configuration: SKOverlay.Configuration { get }
```

## See Also

### Creating an overlay

- [- initWithConfiguration:](<init(configuration_).md>) — Creates an overlay you use to recommend another app on the App Store.
- [AppConfiguration](appconfiguration.md) — An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [AppClipConfiguration](appclipconfiguration.md) — An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [Configuration](configuration-swift.class.md) — The abstract superclass for all classes that represent an overlay’s attributes.
