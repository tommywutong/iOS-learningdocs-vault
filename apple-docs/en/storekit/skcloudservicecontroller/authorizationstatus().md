---
title: authorizationStatus()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicecontroller/authorizationstatus()
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller/authorizationstatus()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller/authorizationstatus%28%29.json'
content_hash: 'sha256:bf2bce97272c812e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceController](../skcloudservicecontroller.md)

# authorizationStatus()

<sub>Type Method</sub>

Returns the type of authorization the customer has for accessing the Music library on the device.

> [!warning] Deprecated
> Use MusicAuthorization.currentStatus from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class func authorizationStatus() -> SKCloudServiceAuthorizationStatus
```

## Return Value

The type of authorization for music library access. See [SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md) for a list of possible values.

## Discussion

Use the authorization status to determine in what ways you can access the user’s music library.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Getting authorization to access the Music library

- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md) — Prompt the customer to authorize access to Apple Music library.
- [+ requestAuthorization:](<requestauthorization(__).md>) — Asks the customer for permission to access the Music library on the device. _(deprecated)_
- [SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md) — Constants that indicate the type of authorization the customer has for accessing the Music library. _(deprecated)_
