---
title: ErrorUserInfoKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/erroruserinfokey
source_url: 'https://developer.apple.com/documentation/foundation/erroruserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/erroruserinfokey.json'
content_hash: 'sha256:e76bfe82bdb61091'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ErrorUserInfoKey

<sub>Structure</sub>

These keys may exist in the user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ErrorUserInfoKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSURLErrorKey](erroruserinfokey/nsurlerrorkey.md) _(deprecated)_
- [filePathErrorKey](erroruserinfokey/filepatherrorkey.md) _(deprecated)_
- [helpAnchorErrorKey](erroruserinfokey/helpanchorerrorkey.md) _(deprecated)_
- [localizedDescriptionKey](erroruserinfokey/localizeddescriptionkey.md) _(deprecated)_
- [localizedFailureReasonErrorKey](erroruserinfokey/localizedfailurereasonerrorkey.md) _(deprecated)_
- [localizedRecoveryOptionsErrorKey](erroruserinfokey/localizedrecoveryoptionserrorkey.md) _(deprecated)_
- [localizedRecoverySuggestionErrorKey](erroruserinfokey/localizedrecoverysuggestionerrorkey.md) _(deprecated)_
- [recoveryAttempterErrorKey](erroruserinfokey/recoveryattemptererrorkey.md) _(deprecated)_
- [stringEncodingErrorKey](erroruserinfokey/stringencodingerrorkey.md) _(deprecated)_
- [underlyingErrorKey](erroruserinfokey/underlyingerrorkey.md) _(deprecated)_

## See Also

### Providing Error User Info

- [+ setUserInfoValueProviderForDomain:provider:](<nserror/setuserinfovalueprovider(fordomain_provider_).md>) — Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [+ userInfoValueProviderForDomain:](<nserror/userinfovalueprovider(fordomain_).md>) — Returns any user info provider specified for a given error domain.
- [UserInfoKey](nserror/userinfokey.md) — These keys may exist in the user info dictionary.
