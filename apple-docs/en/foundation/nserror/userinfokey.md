---
title: NSError.UserInfoKey
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/userinfokey
source_url: 'https://developer.apple.com/documentation/foundation/nserror/userinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/userinfokey.json'
content_hash: 'sha256:29998250baae5a72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# NSError.UserInfoKey

<sub>Type Alias</sub>

These keys may exist in the user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias UserInfoKey = NSString
```

## Topics

### Constants

- [NSURLErrorKey](../nsurlerrorkey.md) — The corresponding value is an `NSURL` object.
- [NSFilePathErrorKey](../nsfilepatherrorkey.md) — Contains the file path of the error.
- [NSHelpAnchorErrorKey](../nshelpanchorerrorkey.md) — The corresponding value is an `NSString` containing the localized help corresponding to the help button. See [helpAnchor](helpanchor.md) for more information.
- [NSLocalizedDescriptionKey](../nslocalizeddescriptionkey.md) — The corresponding value is a localized string representation of the error that, if present, will be returned by [localizedDescription](localizeddescription.md).
- [NSLocalizedFailureErrorKey](../nslocalizedfailureerrorkey.md)
- [NSLocalizedFailureReasonErrorKey](../nslocalizedfailurereasonerrorkey.md) — The corresponding value is a localized string representation containing the reason for the failure that, if present, will be returned by [localizedFailureReason](localizedfailurereason.md).
- [NSLocalizedRecoveryOptionsErrorKey](../nslocalizedrecoveryoptionserrorkey.md) — The corresponding value is an array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [NSLocalizedRecoverySuggestionErrorKey](../nslocalizedrecoverysuggestionerrorkey.md) — The corresponding value is a string containing the localized recovery suggestion for the error.
- [NSRecoveryAttempterErrorKey](../nsrecoveryattemptererrorkey.md) — The corresponding value is an object that conforms to the NSErrorRecoveryAttempting informal protocol.
- [NSStringEncodingErrorKey](../nsstringencodingerrorkey.md) — The corresponding value is an `NSNumber` object containing the `NSStringEncoding` value.
- [NSUnderlyingErrorKey](../nsunderlyingerrorkey.md) — The corresponding value is an error that was encountered in an underlying implementation and caused the error that the receiver represents to occur.
- [NSDebugDescriptionErrorKey](../nsdebugdescriptionerrorkey.md)
- [NSMultipleUnderlyingErrorsKey](../nsmultipleunderlyingerrorskey.md)

## See Also

### Providing Error User Info

- [+ setUserInfoValueProviderForDomain:provider:](<setuserinfovalueprovider(fordomain_provider_).md>) — Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [+ userInfoValueProviderForDomain:](<userinfovalueprovider(fordomain_).md>) — Returns any user info provider specified for a given error domain.
- [ErrorUserInfoKey](../erroruserinfokey.md) — These keys may exist in the user info dictionary.
