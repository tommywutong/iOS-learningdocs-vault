---
title: NSFileManagerUploadLocalVersionConflictPolicy.conflictPolicyFailOnConflict
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy/conflictpolicyfailonconflict
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy/conflictpolicyfailonconflict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy/conflictpolicyfailonconflict.json'
content_hash: 'sha256:14172c09cf9fb2fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileManagerUploadLocalVersionConflictPolicy](../nsfilemanageruploadlocalversionconflictpolicy.md)

# NSFileManagerUploadLocalVersionConflictPolicy.conflictPolicyFailOnConflict

<sub>Case</sub>

Resolves the conflict by causing the upload to fail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case conflictPolicyFailOnConflict
```

## Discussion

This policy causes an upload to fail if the local version of a file, with any local changes applied, doesn’t match the server version. In this scenario, call [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<../filemanager/fetchlatestremoteversionofitem(at_completionhandler_).md>), rebase local changes on top of the newly fetched version, and retry the upload.

This policy is only available on paused items for which the file provider supports the fail-on-conflict behavior. To check that the file provider supports the behavior, get the [NSURLUbiquitousItemSupportedSyncControlsKey](../urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md) URL resource and verify that [NSFileManagerSupportedSyncControlsFailUploadOnConflict](../nsfilemanagersupportedsynccontrols/failuploadonconflict.md) is `true`.

## See Also

### Working with conflict policies

- [NSFileManagerUploadConflictPolicyDefault](conflictpolicydefault.md) — Resolves the conflict using the policy defined by the file provider.
