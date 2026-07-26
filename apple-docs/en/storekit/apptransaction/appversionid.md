---
title: appVersionID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/appversionid
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/appversionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/appversionid.json'
content_hash: 'sha256:919de4914fb5aafe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# appVersionID

<sub>Instance Property</sub>

The number that the App Store uses to uniquely identify the version of the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let appVersionID: UInt64?
```

## Discussion

The App Store assigns this value. In the [sandbox](../appstore/environment/sandbox.md) and [xcode](../appstore/environment/xcode.md) environments, this value is `nil`.

## See Also

### Getting app and version information

- [bundleID](bundleid.md) — The bundle identifier that the app transaction applies to.
- [appVersion](appversion.md) — The app version that the app transaction applies to.
- [originalAppVersion](originalappversion.md) — The app version that the customer originally purchased from the App Store.
- [appID](appid.md) — The unique identifier the App Store uses to identify the app.
