---
title: 'requestStorefrontCountryCode(completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller/requeststorefrontcountrycode%28completionhandler%3A%29.json'
content_hash: 'sha256:c9e1afae34ebe847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceController](../skcloudservicecontroller.md)

# requestStorefrontCountryCode(completionHandler:)

<sub>Instance Method</sub>

Gets the country code for the storefront associated with a customer’s iTunes account.

> [!warning] Deprecated
> Use MusicDataRequest.currentCountryCode from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func requestStorefrontCountryCode(completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func requestStorefrontCountryCode() async throws -> String
```

## Parameters

- `completionHandler` — A block that is called when the storefront country code is returned. The block takes the following parameters: - **storefrontCountryCode** — The country code of a specific storefront. - **error** — An error value that indicates the reason for failure. See [Code](../skerror/code.md) for possible error values.

## Discussion

You need to get the appropriate storefront country code before you specify a product as each country or region contains different products.

## See Also

### Determining capabilities

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md) — Determine which Apple Music capabilities are available on a customer’s device.
- [- requestUserTokenForDeveloperToken:completionHandler:](<requestusertoken(fordevelopertoken_completionhandler_).md>) — Returns a user token that you use to access personalized Apple Music content. _(deprecated)_
- [- requestCapabilitiesWithCompletionHandler:](<requestcapabilities(completionhandler_).md>) — Gets the current capabilities associated with the Music library on the device. _(deprecated)_
- [SKCloudServiceCapability](../skcloudservicecapability.md) — Constants that specify the current capabilities of the customer’s Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
- [- requestPersonalizationTokenForClientToken:withCompletionHandler:](<requestpersonalizationtoken(forclienttoken_withcompletionhandler_).md>) _(deprecated)_
