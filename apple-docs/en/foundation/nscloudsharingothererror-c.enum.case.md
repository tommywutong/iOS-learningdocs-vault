---
title: NSCloudSharingOtherError
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscloudsharingothererror-c.enum.case
source_url: 'https://developer.apple.com/documentation/foundation/nscloudsharingothererror-c.enum.case'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscloudsharingothererror-c.enum.case.json'
content_hash: 'sha256:2df05ea7a4fcfaca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCloudSharingOtherError

<sub>Enumeration Case</sub>

An otherwise unspecified cloud-sharing error occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSCloudSharingOtherError
```

## Discussion

For CloudKit sharing, use the [NSUnderlyingErrorKey](nsunderlyingerrorkey.md), whose value is a [CKErrorDomain](../cloudkit/ckerrordomain.md) error, to discover the specific error. Refer to the [CloudKit](../cloudkit.md) documentation for the proper response to these errors.

## See Also

### iCloud Sharing Errors

- [NSCloudSharingConflictError](nscloudsharingconflicterror-c.enum.case.md) — A conflict occurred during an attempt to save changes.
- [NSCloudSharingErrorMaximum](nscloudsharingerrormaximum-c.enum.case.md) — The end of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingErrorMinimum](nscloudsharingerrorminimum-c.enum.case.md) — The start of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingNetworkFailureError](nscloudsharingnetworkfailureerror-c.enum.case.md) — Sharing failed due to a network failure.
- [NSCloudSharingNoPermissionError](nscloudsharingnopermissionerror-c.enum.case.md) — The current user doesn’t have permission to perform the requested actions.
- [NSCloudSharingQuotaExceededError](nscloudsharingquotaexceedederror-c.enum.case.md) — The user doesn’t have enough storage space available to share the requested items.
- [NSCloudSharingTooManyParticipantsError](nscloudsharingtoomanyparticipantserror-c.enum.case.md) — Additional participants couldn’t be added to the share, because the limit was reached.
