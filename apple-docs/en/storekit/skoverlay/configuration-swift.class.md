---
title: SKOverlay.Configuration
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/configuration-swift.class
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/configuration-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/configuration-swift.class.json'
content_hash: 'sha256:a17f12b3c9662d2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# SKOverlay.Configuration

<sub>Class</sub>

The abstract superclass for all classes that represent an overlay’s attributes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class Configuration
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AppClipConfiguration](appclipconfiguration.md), [AppConfiguration](appconfiguration.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## See Also

### Creating an overlay

- [- initWithConfiguration:](<init(configuration_).md>) — Creates an overlay you use to recommend another app on the App Store.
- [configuration](configuration-swift.property.md) — An overlay’s attributes; for example, its position on the screen.
- [AppConfiguration](appconfiguration.md) — An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [AppClipConfiguration](appclipconfiguration.md) — An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
