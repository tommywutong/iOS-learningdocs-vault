---
title: AppTransaction
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction.json'
content_hash: 'sha256:82055bff5dc6c16f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# AppTransaction

<sub>Structure</sub>

Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AppTransaction
```

## Overview

> [!note] Related sessions from WWDC22
> Session 10007:  [What’s new with in-app purchase](https://developer.apple.com/videos/play/wwdc2022/10007/)

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the signed app transaction

- [shared](apptransaction/shared.md) — Gets the App Store-signed app transaction information for the app.

### Getting the app transaction identifier

- [appTransactionID](apptransaction/apptransactionid.md) — The unique identifier of the app download transaction.

### Getting the environment

- [environment](apptransaction/environment.md) — The server environment that signs the app transaction.
- [Environment](appstore/environment.md) — Constants that represent the App Store server environment.

### Getting app and version information

- [bundleID](apptransaction/bundleid.md) — The bundle identifier that the app transaction applies to.
- [appVersion](apptransaction/appversion.md) — The app version that the app transaction applies to.
- [originalAppVersion](apptransaction/originalappversion.md) — The app version that the customer originally purchased from the App Store.
- [appID](apptransaction/appid.md) — The unique identifier the App Store uses to identify the app.
- [appVersionID](apptransaction/appversionid.md) — The number that the App Store uses to uniquely identify the version of the app.

### Getting the original platform

- [originalPlatform](apptransaction/originalplatform.md) — The platform on which the customer originally purchased the app.
- [Platform](appstore/platform.md) — Values that represent Apple platforms.

### Getting purchase dates

- [originalPurchaseDate](apptransaction/originalpurchasedate.md) — The date the customer originally purchased the app from the App Store.
- [preorderDate](apptransaction/preorderdate.md) — The date the customer placed an order for the app before it’s available in the App Store.

### Verifying the app transaction

- [deviceVerification](apptransaction/deviceverification.md) — The device verification value to use to verify whether the app transaction belongs to the device.
- [deviceVerificationNonce](apptransaction/deviceverificationnonce.md) — The UUID used to compute the device verification value.
- [signedDate](apptransaction/signeddate.md) — The date that the App Store signed the JWS app transaction.

### Getting app transaction information in JSON format

- [jsonRepresentation](apptransaction/jsonrepresentation.md) — The JSON representation of the app transaction information.

### Getting app transaction from the server

- [refresh()](<apptransaction/refresh().md>) — Gets the App Store-signed app transaction information from the App Store server.

### Deprecated

- [originalPlatformStringRepresentation](apptransaction/originalplatformstringrepresentation.md) — The string representation of the platform on which the customer originally purchased the app. _(deprecated)_

### Structures

- [AppTransactions](apptransaction/apptransactions.md) _(beta)_
- [StoreType](apptransaction/storetype-swift.struct.md) _(beta)_

### Instance Properties

- [revocationDate](apptransaction/revocationdate.md) — The revocation date of the app purchase.
- [storeType](apptransaction/storetype-swift.property.md) — The store where the original purchase of the app was made. _(beta)_
- [storeTypeStringRepresentation](apptransaction/storetypestringrepresentation.md) — The string representation of the store where the original purchase of the app was made. _(deprecated)_

### Type Properties

- [all](apptransaction/all.md) — Returns all the `AppTransaction`s for this version of the app. _(beta)_

## See Also

### App transaction

- [Supporting business model changes by using the app transaction](supporting-business-model-changes-by-using-the-app-transaction.md) — Access the app transaction to determine when a customer purchased an app and the features to which they’re entitled.
