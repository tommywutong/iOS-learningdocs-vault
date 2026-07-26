---
title: NSCloudSharingConflictError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscloudsharingconflicterror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nscloudsharingconflicterror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscloudsharingconflicterror-swift.var.json'
content_hash: 'sha256:ca47262f6efbc9ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCloudSharingConflictError

<sub>Global Variable</sub>

A conflict occurred during an attempt to save changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var NSCloudSharingConflictError: Int { get }
```

## Discussion

This error occurs when a conflict is detected while trying to save changes to the [CKShare](../cloudkit/ckshare.md) or root [CKRecord](../cloudkit/ckrecord.md). Respond to this error by first fetching the server’s changes to the records, then either handle the conflict manually or present it, which will instruct the user to try the operation again.

## See Also

### iCloud Sharing Errors

- [NSCloudSharingErrorMaximum](nscloudsharingerrormaximum-swift.var.md) — The end of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingErrorMinimum](nscloudsharingerrorminimum-swift.var.md) — The start of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingNetworkFailureError](nscloudsharingnetworkfailureerror-swift.var.md) — Sharing failed due to a network failure.
- [NSCloudSharingNoPermissionError](nscloudsharingnopermissionerror-swift.var.md) — The current user doesn’t have permission to perform the requested actions.
- [NSCloudSharingOtherError](nscloudsharingothererror-swift.var.md) — An otherwise unspecified cloud-sharing error occurred.
- [NSCloudSharingQuotaExceededError](nscloudsharingquotaexceedederror-swift.var.md) — The user doesn’t have enough storage space available to share the requested items.
- [NSCloudSharingTooManyParticipantsError](nscloudsharingtoomanyparticipantserror-swift.var.md) — Additional participants couldn’t be added to the share, because the limit was reached.
