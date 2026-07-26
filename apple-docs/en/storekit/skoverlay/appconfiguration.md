---
title: SKOverlay.AppConfiguration
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/appconfiguration
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/appconfiguration.json'
content_hash: 'sha256:6768b0594398af8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# SKOverlay.AppConfiguration

<sub>Class</sub>

An object that represents the attributes of an overlay you use to recommend another app on the App Store.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class AppConfiguration
```

## Relationships

- **Inherits From**: [Configuration](configuration-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an App Configuration

- [- initWithAppIdentifier:position:](<appconfiguration/init(appidentifier_position_).md>) — Creates an object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [appIdentifier](appconfiguration/appidentifier.md) — The iTunes identifier of the recommended app.
- [position](appconfiguration/position.md) — The position of the overlay on the screen.
- [Position](position.md) — Constants that identify the position of an overlay on the screen.

### Dismissing the Overlay

- [userDismissible](appconfiguration/userdismissible.md) — A Boolean value that indicates whether the user can dismiss the overlay.

### Verifying Advertising Campaigns

- [campaignToken](appconfiguration/campaigntoken.md) — A token you use to represent an ad campaign and measure its effectiveness.
- [providerToken](appconfiguration/providertoken.md) — A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [- setAdditionalValue:forKey:](<appconfiguration/setadditionalvalue(__forkey_).md>) — Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.
- [- additionalValueForKey:](<appconfiguration/additionalvalue(forkey_).md>) — Returns the object associated with the key.

### Promoting the Latest App Version

- [latestReleaseID](appconfiguration/latestreleaseid.md) — The release ID of the latest version of your app as displayed in App Store Connect.

### Advertising Another App

- [customProductPageIdentifier](appconfiguration/customproductpageidentifier.md) — An optional identifier for an app’s custom product page.

### Setting an Ad Impression

- [- setAdImpression:](<appconfiguration/setadimpression(__).md>)

### Instance Properties

- [adAttributionReengagementURL](appconfiguration/adattributionreengagementurl.md)
- [appImpression](appconfiguration/appimpression.md)

## See Also

### Creating an overlay

- [- initWithConfiguration:](<init(configuration_).md>) — Creates an overlay you use to recommend another app on the App Store.
- [configuration](configuration-swift.property.md) — An overlay’s attributes; for example, its position on the screen.
- [AppClipConfiguration](appclipconfiguration.md) — An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [Configuration](configuration-swift.class.md) — The abstract superclass for all classes that represent an overlay’s attributes.
