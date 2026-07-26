---
title: SKCloudServiceAuthorizationStatus.denied
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudserviceauthorizationstatus/denied
source_url: 'https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/denied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudserviceauthorizationstatus/denied.json'
content_hash: 'sha256:9e9695bf4fa11031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md)

# SKCloudServiceAuthorizationStatus.denied

<sub>Case</sub>

The user does not authorize any access to their music library.

> [!warning] Deprecated
> Use MusicAuthorization.Status from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
case denied
```

## See Also

### Constants

- [SKCloudServiceAuthorizationStatusNotDetermined](notdetermined.md) — The authorization type cannot be determined. _(deprecated)_
- [SKCloudServiceAuthorizationStatusRestricted](restricted.md) — Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode. _(deprecated)_
- [SKCloudServiceAuthorizationStatusAuthorized](authorized.md) — The user authorizes playback of Apple Music tracks and the addition of tracks to their music library. _(deprecated)_
