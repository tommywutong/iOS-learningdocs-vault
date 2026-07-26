---
title: NSCloudSharingOtherError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscloudsharingothererror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nscloudsharingothererror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscloudsharingothererror-swift.var.json'
content_hash: 'sha256:ee2faa31bf60c370'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCloudSharingOtherError

<sub>Global Variable</sub>

An otherwise unspecified cloud-sharing error occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var NSCloudSharingOtherError: Int { get }
```

## Discussion

For CloudKit sharing, use the [NSUnderlyingErrorKey](nsunderlyingerrorkey.md), whose value is a [CKErrorDomain](../cloudkit/ckerrordomain.md) error, to discover the specific error. Refer to the [CloudKit](../cloudkit.md) documentation for the proper response to these errors.

## See Also

### iCloud Sharing Errors

- [NSCloudSharingConflictError](nscloudsharingconflicterror-swift.var.md) — A conflict occurred during an attempt to save changes.
- [NSCloudSharingErrorMaximum](nscloudsharingerrormaximum-swift.var.md) — The end of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingErrorMinimum](nscloudsharingerrorminimum-swift.var.md) — The start of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingNetworkFailureError](nscloudsharingnetworkfailureerror-swift.var.md) — Sharing failed due to a network failure.
- [NSCloudSharingNoPermissionError](nscloudsharingnopermissionerror-swift.var.md) — The current user doesn’t have permission to perform the requested actions.
- [NSCloudSharingQuotaExceededError](nscloudsharingquotaexceedederror-swift.var.md) — The user doesn’t have enough storage space available to share the requested items.
- [NSCloudSharingTooManyParticipantsError](nscloudsharingtoomanyparticipantserror-swift.var.md) — Additional participants couldn’t be added to the share, because the limit was reached.
