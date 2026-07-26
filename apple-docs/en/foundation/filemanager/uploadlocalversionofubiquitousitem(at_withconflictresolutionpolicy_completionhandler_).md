---
title: 'uploadLocalVersionOfUbiquitousItem(at:withConflictResolutionPolicy:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/uploadlocalversionofubiquitousitem%28at%3Awithconflictresolutionpolicy%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:fed684a98c92ce8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# uploadLocalVersionOfUbiquitousItem(at:withConflictResolutionPolicy:completionHandler:)

<sub>Instance Method</sub>

Asynchronously uploads the local version of the item using the provided conflict resolution policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func uploadLocalVersionOfUbiquitousItem(at url: URL, withConflictResolutionPolicy conflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: @escaping @Sendable (NSFileVersion?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func uploadLocalVersionOfUbiquitousItem(at url: URL, withConflictResolutionPolicy conflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy) async throws -> NSFileVersion
```

## Parameters

- `url` — The URL of the item for which to check the version.

- `conflictResolutionPolicy` — The policy the file manager applies if the local and server versions conflict.

- `completionHandler` — A closure or block that the framework calls when the upload completes. It receives parameters of types [NSFileVersion](../nsfileversion.md) and [NSError](../nserror.md). The error is `nil` if fetching the remote version succeeded; otherwise it indicates the error that caused the call to fail. In Swift, you can omit the completion handler, catching any error in a `do`-`catch` block and receiving the version as the return value.

## Discussion

Once your app pauses a sync for an item, call this method every time your document is in a stable state. This action keeps the server version as up-to-date as possible.

If the server has a newer version than the one to which the app made changes, uploading fails with [NSFileWriteUnknownError](../nsfilewriteunknownerror-c.enum.case.md), with an underlying error of [localVersionConflictingWithServer](../../fileprovider/nsfileprovidererror/localversionconflictingwithserver.md). In this case, call [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<fetchlatestremoteversionofitem(at_completionhandler_).md>), rebase local changes on top of that version, and retry the upload.

If the device isn’t connected to the network, the call may fail with [NSFileWriteUnknownError](../nsfilewriteunknownerror-c.enum.case.md), with the underlying error of [serverUnreachable](../../fileprovider/nsfileprovidererror/serverunreachable.md).

## See Also

### Controlling file provider synchronization

- [NSFileManagerSupportedSyncControls](../nsfilemanagersupportedsynccontrols.md) — An option set of the sync controls available for an item.
- [- pauseSyncForUbiquitousItemAtURL:completionHandler:](<pausesyncforubiquitousitem(at_completionhandler_).md>) — Asynchronously pauses sync of an item at the given URL.
- [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<resumesyncforubiquitousitem(at_with_completionhandler_).md>) — Asynchronously resumes the sync on a paused item using the given resume behavior.
- [NSFileManagerResumeSyncBehavior](../nsfilemanagerresumesyncbehavior.md) — The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<fetchlatestremoteversionofitem(at_completionhandler_).md>) — Asynchronously fetches the latest remote version of a given item from the server.
- [NSFileVersion](../nsfileversion.md) — A snapshot of a file at a specific point in time.
- [NSFileManagerUploadLocalVersionConflictPolicy](../nsfilemanageruploadlocalversionconflictpolicy.md) — The policies the file manager can apply to resolve conflicts when uploading a local version of a file.
