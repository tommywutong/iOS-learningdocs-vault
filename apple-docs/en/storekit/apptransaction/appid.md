---
title: appID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/appid
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/appid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/appid.json'
content_hash: 'sha256:849fea597b063e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# appID

<sub>Instance Property</sub>

The unique identifier the App Store uses to identify the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let appID: UInt64?
```

## Discussion

The App Store assigns this value. This value is the app’s Apple ID in App Store Connect. In the [sandbox](../appstore/environment/sandbox.md) and [xcode](../appstore/environment/xcode.md) environments, this value is `nil`.

## See Also

### Getting app and version information

- [bundleID](bundleid.md) — The bundle identifier that the app transaction applies to.
- [appVersion](appversion.md) — The app version that the app transaction applies to.
- [originalAppVersion](originalappversion.md) — The app version that the customer originally purchased from the App Store.
- [appVersionID](appversionid.md) — The number that the App Store uses to uniquely identify the version of the app.
