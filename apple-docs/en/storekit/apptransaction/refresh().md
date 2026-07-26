---
title: refresh()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/refresh()
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/refresh()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/refresh%28%29.json'
content_hash: 'sha256:b44ea9e28d72741d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# refresh()

<sub>Type Method</sub>

Gets the App Store-signed app transaction information from the App Store server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func refresh() async throws -> VerificationResult<AppTransaction>
```

## Return Value

Returns a [VerificationResult](../verificationresult.md) with a single [AppTransaction](../apptransaction.md).

## Discussion

This method queries the App Store server to refresh the app transaction information. This method returns a [VerificationResult](../verificationresult.md) that contains the App Store-signed app transaction information for your app.

> [!important] Important
> Calling [refresh()](<refresh().md>) displays a system prompt that asks users to authenticate with their App Store credentials. Call this function only in response to an explicit user action, like tapping or clicking a button.

Use this method to get an [AppTransaction](../apptransaction.md) in the following cases:

- The [shared](shared.md) property throws an error.
- The [shared](shared.md) property returns an unverified ([VerificationResult.unverified(_:_:)](<../verificationresult/unverified(____).md>) ) result.

This method throws an error if the user cancels the authentication prompt, if there’s no network connectivity, or if the call fails to update the app transaction.
