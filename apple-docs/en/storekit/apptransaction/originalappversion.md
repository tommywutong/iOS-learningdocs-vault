---
title: originalAppVersion
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/originalappversion
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/originalappversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/originalappversion.json'
content_hash: 'sha256:447f0cceb5a2b7f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# originalAppVersion

<sub>Instance Property</sub>

The app version that the customer originally purchased from the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let originalAppVersion: String
```

## Discussion

Use this value to determine which app version the customer first purchased or downloaded. This value is comparable to the [appVersion](appversion.md) value.

The [originalAppVersion](originalappversion.md) remains constant and doesn’t change when the customer upgrades the app. The string value contains the original value of the [CFBundleShortVersionString](../../bundleresources/information-property-list/cfbundleshortversionstring.md) for apps running in macOS, and the original value of the [CFBundleVersion](../../bundleresources/information-property-list/cfbundleversion.md) for apps running on all other platforms.

In the sandbox testing environment, the [originalAppVersion](originalappversion.md) value is always `1.0`.

For more information about using the [originalAppVersion](originalappversion.md), see [Supporting business model changes by using the app transaction](../supporting-business-model-changes-by-using-the-app-transaction.md).

## See Also

### Getting app and version information

- [bundleID](bundleid.md) — The bundle identifier that the app transaction applies to.
- [appVersion](appversion.md) — The app version that the app transaction applies to.
- [appID](appid.md) — The unique identifier the App Store uses to identify the app.
- [appVersionID](appversionid.md) — The number that the App Store uses to uniquely identify the version of the app.
