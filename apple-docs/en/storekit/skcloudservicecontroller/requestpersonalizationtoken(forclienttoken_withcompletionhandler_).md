---
title: 'requestPersonalizationToken(forClientToken:withCompletionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+（11.0 起废弃）, iPadOS 10.3+（11.0 起废弃）, tvOS 10.3+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller/requestpersonalizationtoken%28forclienttoken%3Awithcompletionhandler%3A%29.json'
content_hash: 'sha256:778c659849c3462d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceController](../skcloudservicecontroller.md)

# requestPersonalizationToken(forClientToken:withCompletionHandler:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func requestPersonalizationToken(forClientToken clientToken: String, withCompletionHandler completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

## See Also

### Determining capabilities

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md) — Determine which Apple Music capabilities are available on a customer’s device.
- [- requestUserTokenForDeveloperToken:completionHandler:](<requestusertoken(fordevelopertoken_completionhandler_).md>) — Returns a user token that you use to access personalized Apple Music content. _(deprecated)_
- [- requestStorefrontCountryCodeWithCompletionHandler:](<requeststorefrontcountrycode(completionhandler_).md>) — Gets the country code for the storefront associated with a customer’s iTunes account. _(deprecated)_
- [- requestCapabilitiesWithCompletionHandler:](<requestcapabilities(completionhandler_).md>) — Gets the current capabilities associated with the Music library on the device. _(deprecated)_
- [SKCloudServiceCapability](../skcloudservicecapability.md) — Constants that specify the current capabilities of the customer’s Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
