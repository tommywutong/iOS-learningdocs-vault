---
title: 'requestUserToken(forDeveloperToken:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller/requestusertoken%28fordevelopertoken%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:40de4a3d3039a784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceController](../skcloudservicecontroller.md)

# requestUserToken(forDeveloperToken:completionHandler:)

<sub>Instance Method</sub>

Returns a user token that you use to access personalized Apple Music content.

> [!warning] Deprecated
> Use MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func requestUserToken(forDeveloperToken developerToken: String, completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func requestUserToken(forDeveloperToken developerToken: String) async throws -> String
```

## Parameters

- `developerToken` — A signed and encrypted JWT token used to authenticate the developer in Apple Music API requests.

- `completionHandler` — A completion block that includes the following parameters: - **userToken** — A token that identifies the user. - **error** — The error that occurred, if any.

## Discussion

Use this method with your developer token to get a token that authenticates the user in personalized Apple Music API requests. Note that personalized requests return user-specific data. Errors 401 and 403 only occur when requesting a music user token. They do not occur for any of the other Apple Music API requests.

## See Also

### Determining capabilities

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md) — Determine which Apple Music capabilities are available on a customer’s device.
- [- requestStorefrontCountryCodeWithCompletionHandler:](<requeststorefrontcountrycode(completionhandler_).md>) — Gets the country code for the storefront associated with a customer’s iTunes account. _(deprecated)_
- [- requestCapabilitiesWithCompletionHandler:](<requestcapabilities(completionhandler_).md>) — Gets the current capabilities associated with the Music library on the device. _(deprecated)_
- [SKCloudServiceCapability](../skcloudservicecapability.md) — Constants that specify the current capabilities of the customer’s Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
- [- requestPersonalizationTokenForClientToken:withCompletionHandler:](<requestpersonalizationtoken(forclienttoken_withcompletionhandler_).md>) _(deprecated)_
