---
title: SKCloudServiceAuthorizationStatus.authorized
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudserviceauthorizationstatus/authorized
source_url: 'https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/authorized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudserviceauthorizationstatus/authorized.json'
content_hash: 'sha256:58a59740bc09b326'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md)

# SKCloudServiceAuthorizationStatus.authorized

<sub>Case</sub>

The user authorizes playback of Apple Music tracks and the addition of tracks to their music library.

> [!warning] Deprecated
> Use MusicAuthorization.Status from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
case authorized
```

## See Also

### Constants

- [SKCloudServiceAuthorizationStatusNotDetermined](notdetermined.md) — The authorization type cannot be determined. _(deprecated)_
- [SKCloudServiceAuthorizationStatusDenied](denied.md) — The user does not authorize any access to their music library. _(deprecated)_
- [SKCloudServiceAuthorizationStatusRestricted](restricted.md) — Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode. _(deprecated)_
