---
title: 'setUserInfoValueProvider(forDomain:provider:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nserror/setuserinfovalueprovider(fordomain:provider:)'
source_url: 'https://developer.apple.com/documentation/foundation/nserror/setuserinfovalueprovider(fordomain:provider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/setuserinfovalueprovider%28fordomain%3Aprovider%3A%29.json'
content_hash: 'sha256:58afe9c57e0d5a04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# setUserInfoValueProvider(forDomain:provider:)

<sub>Type Method</sub>

Specifies a block to call when the corresponding property is not present in the user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setUserInfoValueProvider(forDomain errorDomain: String, provider: (@Sendable (any Error, String) -> Any?)? = nil)
```

## Parameters

- `errorDomain` — The error domain of the provider.

- `provider` — A block to be executed synchronously at the time a corresponding property is accessed. - **err** — The error object that is being accessed. - **userInfoKey** — The user info key corresponding to the accessed property.

## Discussion

This method specifies a block that is called from the implementations of [localizedDescription](localizeddescription.md), [localizedFailureReason](localizedfailurereason.md), [localizedRecoverySuggestion](localizedrecoverysuggestion.md), [localizedRecoveryOptions](localizedrecoveryoptions.md), [recoveryAttempter](recoveryattempter.md), and [helpAnchor](helpanchor.md) when the underlying value for any of those properties is not present in the [userInfo](userinfo.md) dictionary of NSError instances with the specified domain.

A user info provider is optional, and allows localization and formatting of error messages to be done lazily, rather than populating the [userInfo](userinfo.md) at the time of creation. It is expected that only the “owner” of an [NSError](../nserror.md) domain specifies the provider for the domain, and that this is done at most once. This method is not meant for consumers of errors to customize the [userInfo](userinfo.md) entries, and should not be used to customize the behaviors of error domains provided by the system.

The keys of a provider’s [userInfo](userinfo.md) dictionary correspond to the queried property, such as [NSLocalizedDescriptionKey](../nslocalizeddescriptionkey.md) for the [localizedDescription](localizeddescription.md) property. The provider should return `nil` for any keys that it is unable to provide, as well as any keys it does not recognize (since the list of error keys may be extended in future releases). If an appropriate result for the requested key cannot be provided, return `nil` rather than choosing to manufacture a generic fallback response.

The provider block is executed synchronously at the time when a corresponding property is accessed. The results are not cached.

## See Also

### Providing Error User Info

- [+ userInfoValueProviderForDomain:](<userinfovalueprovider(fordomain_).md>) — Returns any user info provider specified for a given error domain.
- [ErrorUserInfoKey](../erroruserinfokey.md) — These keys may exist in the user info dictionary.
- [UserInfoKey](userinfokey.md) — These keys may exist in the user info dictionary.
