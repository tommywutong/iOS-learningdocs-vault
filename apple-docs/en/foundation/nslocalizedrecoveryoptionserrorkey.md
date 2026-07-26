---
title: NSLocalizedRecoveryOptionsErrorKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocalizedrecoveryoptionserrorkey
source_url: 'https://developer.apple.com/documentation/foundation/nslocalizedrecoveryoptionserrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocalizedrecoveryoptionserrorkey.json'
content_hash: 'sha256:09c52c4553ae5f0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLocalizedRecoveryOptionsErrorKey

<sub>Global Variable</sub>

The corresponding value is an array containing the localized titles of buttons appropriate for displaying in an alert panel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSLocalizedRecoveryOptionsErrorKey: String
```

## Discussion

The first string is the title of the right-most and default button, the second the one to the left, and so on. The recovery options should be appropriate for the recovery suggestion returned by [localizedRecoverySuggestion](nserror/localizedrecoverysuggestion.md).

## See Also

### Constants

- [NSURLErrorKey](nsurlerrorkey.md) — The corresponding value is an `NSURL` object.
- [NSFilePathErrorKey](nsfilepatherrorkey.md) — Contains the file path of the error.
- [NSHelpAnchorErrorKey](nshelpanchorerrorkey.md) — The corresponding value is an `NSString` containing the localized help corresponding to the help button. See [helpAnchor](nserror/helpanchor.md) for more information.
- [NSLocalizedDescriptionKey](nslocalizeddescriptionkey.md) — The corresponding value is a localized string representation of the error that, if present, will be returned by [localizedDescription](nserror/localizeddescription.md).
- [NSLocalizedFailureErrorKey](nslocalizedfailureerrorkey.md)
- [NSLocalizedFailureReasonErrorKey](nslocalizedfailurereasonerrorkey.md) — The corresponding value is a localized string representation containing the reason for the failure that, if present, will be returned by [localizedFailureReason](nserror/localizedfailurereason.md).
- [NSLocalizedRecoverySuggestionErrorKey](nslocalizedrecoverysuggestionerrorkey.md) — The corresponding value is a string containing the localized recovery suggestion for the error.
- [NSRecoveryAttempterErrorKey](nsrecoveryattemptererrorkey.md) — The corresponding value is an object that conforms to the NSErrorRecoveryAttempting informal protocol.
- [NSStringEncodingErrorKey](nsstringencodingerrorkey.md) — The corresponding value is an `NSNumber` object containing the `NSStringEncoding` value.
- [NSUnderlyingErrorKey](nsunderlyingerrorkey.md) — The corresponding value is an error that was encountered in an underlying implementation and caused the error that the receiver represents to occur.
- [NSDebugDescriptionErrorKey](nsdebugdescriptionerrorkey.md)
- [NSMultipleUnderlyingErrorsKey](nsmultipleunderlyingerrorskey.md)
