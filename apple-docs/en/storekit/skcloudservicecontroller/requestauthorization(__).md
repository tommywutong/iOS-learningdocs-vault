---
title: 'requestAuthorization(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicecontroller/requestauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller/requestauthorization%28_%3A%29.json'
content_hash: 'sha256:33c2797c3ac5bde9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceController](../skcloudservicecontroller.md)

# requestAuthorization(_:)

<sub>Type Method</sub>

Asks the customer for permission to access the Music library on the device.

> [!warning] Deprecated
> Use MusicAuthorization.request() from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class func requestAuthorization(_ completionHandler: @escaping @Sendable (SKCloudServiceAuthorizationStatus) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class func requestAuthorization() async -> SKCloudServiceAuthorizationStatus
```

## Parameters

- `completionHandler` — A block that is called when authorization is granted or denied by the user.

## Discussion

You can use this method to ask the user for permission to play Apple Music tracks or to add tracks to the music library.

## See Also

### Getting authorization to access the Music library

- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md) — Prompt the customer to authorize access to Apple Music library.
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the type of authorization the customer has for accessing the Music library on the device. _(deprecated)_
- [SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md) — Constants that indicate the type of authorization the customer has for accessing the Music library. _(deprecated)_
