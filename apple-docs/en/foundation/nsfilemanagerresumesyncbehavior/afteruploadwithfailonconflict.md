---
title: NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict.json'
content_hash: 'sha256:b1bf8cb33e1c039f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileManagerResumeSyncBehavior](../nsfilemanagerresumesyncbehavior.md)

# NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict

<sub>Case</sub>

Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case afterUploadWithFailOnConflict
```

## Discussion

If the upload succeeds, the sync resumes with the [NSFileManagerResumeSyncBehaviorPreserveLocalChanges](preservelocalchanges.md) behavior.

If the provider detects a conflict, the upload fails with an  [NSFileWriteUnknownError](../nsfilewriteunknownerror-c.enum.case.md), with the underlying error of [localVersionConflictingWithServer](../../fileprovider/nsfileprovidererror/localversionconflictingwithserver.md). In this case, the app needs to call [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<../filemanager/fetchlatestremoteversionofitem(at_completionhandler_).md>), rebase local changes on top of the newly fetched version to resolve the conflict, and try again to resume sync. This scenario is only available on paused items for which the file provider supports the fail-on-conflict behavior. To check that the file provider supports the behavior, get the [NSURLUbiquitousItemSupportedSyncControlsKey](../urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md) URL resource and verify that [NSFileManagerSupportedSyncControlsFailUploadOnConflict](../nsfilemanagersupportedsynccontrols/failuploadonconflict.md) is `true`.

## See Also

### Identifying sync behaviors

- [NSFileManagerResumeSyncBehaviorPreserveLocalChanges](preservelocalchanges.md) — Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehaviorDropLocalChanges](droplocalchanges.md) — Resumes synchronizing by overwriting any local changes with the remote version of the file.
