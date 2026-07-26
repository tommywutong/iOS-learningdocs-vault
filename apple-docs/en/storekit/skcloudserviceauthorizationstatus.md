---
title: SKCloudServiceAuthorizationStatus
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudserviceauthorizationstatus
source_url: 'https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudserviceauthorizationstatus.json'
content_hash: 'sha256:8ad711d43545cbde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceAuthorizationStatus

<sub>Enumeration</sub>

Constants that indicate the type of authorization the customer has for accessing the Music library.

> [!warning] Deprecated
> Use MusicAuthorization.Status from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
enum SKCloudServiceAuthorizationStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [SKCloudServiceAuthorizationStatusNotDetermined](skcloudserviceauthorizationstatus/notdetermined.md) — The authorization type cannot be determined. _(deprecated)_
- [SKCloudServiceAuthorizationStatusDenied](skcloudserviceauthorizationstatus/denied.md) — The user does not authorize any access to their music library. _(deprecated)_
- [SKCloudServiceAuthorizationStatusRestricted](skcloudserviceauthorizationstatus/restricted.md) — Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode. _(deprecated)_
- [SKCloudServiceAuthorizationStatusAuthorized](skcloudserviceauthorizationstatus/authorized.md) — The user authorizes playback of Apple Music tracks and the addition of tracks to their music library. _(deprecated)_

### Initializers

- [init(rawValue:)](<skcloudserviceauthorizationstatus/init(rawvalue_).md>) _(deprecated)_

## See Also

### Getting authorization to access the Music library

- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md) — Prompt the customer to authorize access to Apple Music library.
- [+ authorizationStatus](<skcloudservicecontroller/authorizationstatus().md>) — Returns the type of authorization the customer has for accessing the Music library on the device. _(deprecated)_
- [+ requestAuthorization:](<skcloudservicecontroller/requestauthorization(__).md>) — Asks the customer for permission to access the Music library on the device. _(deprecated)_
