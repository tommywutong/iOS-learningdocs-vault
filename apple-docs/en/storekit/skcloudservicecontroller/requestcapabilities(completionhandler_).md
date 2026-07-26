---
title: 'requestCapabilities(completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicecontroller/requestcapabilities(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestcapabilities(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller/requestcapabilities%28completionhandler%3A%29.json'
content_hash: 'sha256:3c8cd1ea131e450a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceController](../skcloudservicecontroller.md)

# requestCapabilities(completionHandler:)

<sub>Instance Method</sub>

Gets the current capabilities associated with the Music library on the device.

> [!warning] Deprecated
> Use MusicSubscription.current from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func requestCapabilities(completionHandler: @escaping @Sendable (SKCloudServiceCapability, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func requestCapabilities() async throws -> SKCloudServiceCapability
```

## Parameters

- `completionHandler` — A block that is called when the device’s current capabilities are determined. The block takes the following parameters: - **capabilities** — Flags that indicate the device’s capabilities. For possible values, see [SKCloudServiceCapability](../skcloudservicecapability.md). - **error** — An error value that indicates the reason for failure. Possible values are [SKErrorUnknown](../skerror/code/unknown.md), [SKErrorCloudServicePermissionDenied](../skerror/code/cloudservicepermissiondenied.md), and [SKErrorCloudServiceNetworkConnectionFailed](../skerror/code/cloudservicenetworkconnectionfailed.md).

## Discussion

## See Also

### Determining capabilities

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md) — Determine which Apple Music capabilities are available on a customer’s device.
- [- requestUserTokenForDeveloperToken:completionHandler:](<requestusertoken(fordevelopertoken_completionhandler_).md>) — Returns a user token that you use to access personalized Apple Music content. _(deprecated)_
- [- requestStorefrontCountryCodeWithCompletionHandler:](<requeststorefrontcountrycode(completionhandler_).md>) — Gets the country code for the storefront associated with a customer’s iTunes account. _(deprecated)_
- [SKCloudServiceCapability](../skcloudservicecapability.md) — Constants that specify the current capabilities of the customer’s Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
- [- requestPersonalizationTokenForClientToken:withCompletionHandler:](<requestpersonalizationtoken(forclienttoken_withcompletionhandler_).md>) _(deprecated)_
