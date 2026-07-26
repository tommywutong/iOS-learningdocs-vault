---
title: bundleID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/bundleid
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/bundleid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/bundleid.json'
content_hash: 'sha256:2dc2fecab72e4b90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# bundleID

<sub>Instance Property</sub>

The bundle identifier that the app transaction applies to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let bundleID: String
```

## Discussion

The [bundleID](bundleid.md) is the bundle identifier string that you entered in Xcode. For more information, see [What is a bundle ID?](https://help.apple.com/xcode/mac/current/#/deve70ea917b)

## See Also

### Getting app and version information

- [appVersion](appversion.md) — The app version that the app transaction applies to.
- [originalAppVersion](originalappversion.md) — The app version that the customer originally purchased from the App Store.
- [appID](appid.md) — The unique identifier the App Store uses to identify the app.
- [appVersionID](appversionid.md) — The number that the App Store uses to uniquely identify the version of the app.
