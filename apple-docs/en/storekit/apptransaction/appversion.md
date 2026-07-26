---
title: appVersion
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/appversion
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/appversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/appversion.json'
content_hash: 'sha256:40c87175783f0f4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# appVersion

<sub>Instance Property</sub>

The app version that the app transaction applies to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let appVersion: String
```

## Discussion

This value is the version string you entered in Xcode. This value is a machine-readable string composed of one to three period-separated integers, such as `10.4.1`.

## See Also

### Getting app and version information

- [bundleID](bundleid.md) — The bundle identifier that the app transaction applies to.
- [originalAppVersion](originalappversion.md) — The app version that the customer originally purchased from the App Store.
- [appID](appid.md) — The unique identifier the App Store uses to identify the app.
- [appVersionID](appversionid.md) — The number that the App Store uses to uniquely identify the version of the app.
