---
title: SKOverlay.AppClipConfiguration
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/appclipconfiguration
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/appclipconfiguration.json'
content_hash: 'sha256:5897f54bf6f905bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# SKOverlay.AppClipConfiguration

<sub>Class</sub>

An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class AppClipConfiguration
```

## Relationships

- **Inherits From**: [Configuration](configuration-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an App Clip Configuration

- [- initWithPosition:](<appclipconfiguration/init(position_).md>) — Creates an object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding app.
- [position](appclipconfiguration/position.md) — The position of the overlay on the screen.
- [Position](position.md) — Constants that identify the position of an overlay on the screen.

### Verifying Advertising Campaigns

- [campaignToken](appclipconfiguration/campaigntoken.md) — A token you use to represent an ad campaign and measure its effectiveness.
- [providerToken](appclipconfiguration/providertoken.md) — A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [- setAdditionalValue:forKey:](<appclipconfiguration/setadditionalvalue(__forkey_).md>) — Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.
- [- additionalValueForKey:](<appclipconfiguration/additionalvalue(forkey_).md>) — Returns the object associated with the key.

### Promoting the Latest App Version

- [latestReleaseID](appclipconfiguration/latestreleaseid.md) — The release ID of the latest version of your parent app as displayed in App Store Connect.

### Advertising Another App

- [customProductPageIdentifier](appclipconfiguration/customproductpageidentifier.md) — An identifier for a parent app’s custom product page.

## See Also

### Creating an overlay

- [- initWithConfiguration:](<init(configuration_).md>) — Creates an overlay you use to recommend another app on the App Store.
- [configuration](configuration-swift.property.md) — An overlay’s attributes; for example, its position on the screen.
- [AppConfiguration](appconfiguration.md) — An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [Configuration](configuration-swift.class.md) — The abstract superclass for all classes that represent an overlay’s attributes.
