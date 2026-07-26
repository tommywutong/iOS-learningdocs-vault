---
title: appStoreReceiptURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 2.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/bundle/appstorereceipturl
source_url: 'https://developer.apple.com/documentation/foundation/bundle/appstorereceipturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/appstorereceipturl.json'
content_hash: 'sha256:c44d4c6d83918e7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# appStoreReceiptURL

<sub>Instance Property</sub>

The file URL for the bundle’s App Store receipt.

> [!warning] Deprecated
> Use AppTransaction.shared and Transaction.all from StoreKit.framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var appStoreReceiptURL: URL? { get }
```

## Discussion

> [!note] Note
> The receipt isn’t necessary if you use [AppTransaction](../../storekit/apptransaction.md) to validate the app download, or [Transaction](../../storekit/transaction.md) to validate in-app purchases. Only use the receipt if your app uses the [Original API for In-App Purchase](../../storekit/original-api-for-in-app-purchase.md), or needs the receipt to validate the app download because it can’t use [AppTransaction](../../storekit/apptransaction.md).

Use this app bundle property to locate the app receipt if it’s present; this property is `nil` if the receipt isn’t present. In the rare case a receipt is invalid or missing in an app that a user downloads from the App Store, use [SKReceiptRefreshRequest](../../storekit/skreceiptrefreshrequest.md) to request a new receipt. For information about validating receipts, see [Choosing a receipt validation technique](../../storekit/choosing-a-receipt-validation-technique.md).

You can’t use the general best practice of weak linking using the [responds(to:)](<../../objectivec/nsobjectprotocol/responds(to_).md>) method here; the method’s implementation uses the [doesNotRecognizeSelector(_:)](<../../objectivec/nsobject-swift.class/doesnotrecognizeselector(__).md>) method.

### Get the receipt in testing environments

Receipts aren’t initially present in iOS and iPadOS apps in the sandbox environment and in Xcode. Apps get a receipt after the tester completes the first in-app purchase. When your app checks [appStoreReceiptURL](appstorereceipturl.md) and finds that it’s `nil`, assume the tester is a new customer and has no access to premium content. For Mac apps running in TestFlight, the receipt is always present.

## See Also

### Getting the standard bundle directories

- [resourceURL](resourceurl.md) — The file URL of the bundle’s subdirectory containing resource files.
- [executableURL](executableurl.md) — The file URL of the receiver’s executable file.
- [privateFrameworksURL](privateframeworksurl.md) — The file URL of the bundle’s subdirectory containing private frameworks.
- [sharedFrameworksURL](sharedframeworksurl.md) — The file URL of the receiver’s subdirectory containing shared frameworks.
- [builtInPlugInsURL](builtinpluginsurl.md) — The file URL of the receiver’s subdirectory containing plug-ins.
- [- URLForAuxiliaryExecutable:](<url(forauxiliaryexecutable_).md>) — Returns the file URL of the executable with the specified name in the receiver’s bundle.
- [sharedSupportURL](sharedsupporturl.md) — The file URL of the bundle’s subdirectory containing shared support files.
- [resourcePath](resourcepath.md) — The full pathname of the bundle’s subdirectory containing resources.
- [executablePath](executablepath.md) — The full pathname of the receiver’s executable file.
- [privateFrameworksPath](privateframeworkspath.md) — The full pathname of the bundle’s subdirectory containing private frameworks.
- [sharedFrameworksPath](sharedframeworkspath.md) — The full pathname of the bundle’s subdirectory containing shared frameworks.
- [builtInPlugInsPath](builtinpluginspath.md) — The full pathname of the receiver’s subdirectory containing plug-ins.
- [- pathForAuxiliaryExecutable:](<path(forauxiliaryexecutable_).md>) — Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [sharedSupportPath](sharedsupportpath.md) — The full pathname of the bundle’s subdirectory containing shared support files.
