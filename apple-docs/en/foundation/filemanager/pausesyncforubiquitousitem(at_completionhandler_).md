---
title: 'pauseSyncForUbiquitousItem(at:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/pausesyncforubiquitousitem(at:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/pausesyncforubiquitousitem(at:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/pausesyncforubiquitousitem%28at%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:8d4735cd4d103a01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# pauseSyncForUbiquitousItem(at:completionHandler:)

<sub>Instance Method</sub>

Asynchronously pauses sync of an item at the given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func pauseSyncForUbiquitousItem(at url: URL, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func pauseSyncForUbiquitousItem(at url: URL) async throws
```

## Parameters

- `url` — The URL of the item for which to pause sync.

- `completionHandler` — A closure or block that the framework calls when the pause action completes. It receives a single [NSError](../nserror.md) parameter to indicate an error that prevented pausing; this value is `nil` if the pause succeeded. In Swift, you can omit the completion handler and catch the thrown error instead.

## Discussion

Call this when opening an item to prevent sync from altering the contents of the URL. Once paused, the file provider will not upload local changes nor download remote changes.

While paused, call [- uploadLocalVersionOfUbiquitousItemAtURL:withConflictResolutionPolicy:completionHandler:](<uploadlocalversionofubiquitousitem(at_withconflictresolutionpolicy_completionhandler_).md>) when the document is in a stable state. This action keeps the server version as up-to-date as possible.

If the item is already paused, a second call to this method reports success. If the file provider is already applying changes to the item, the pause fails with an [NSFileWriteUnknownError](../nsfilewriteunknownerror-c.enum.case.md), with an underlying error that has domain [NSPOSIXErrorDomain](../nsposixerrordomain.md) and code [EBUSY](../posixerror/ebusy.md). If the pause fails, wait for the state to stabilize before retrying. Pausing also fails with [featureUnsupported](../cocoaerror/featureunsupported.md) if `url` refers to a regular (non-package) directory.

Pausing sync is independent of the calling app’s lifecycle; sync doesn’t automatically resume if the app closes or crashes and relaunches later. To resume syncing, explicitly call [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<resumesyncforubiquitousitem(at_with_completionhandler_).md>). Always be sure to resume syncing before you close the item.

## See Also

### Controlling file provider synchronization

- [NSFileManagerSupportedSyncControls](../nsfilemanagersupportedsynccontrols.md) — An option set of the sync controls available for an item.
- [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<resumesyncforubiquitousitem(at_with_completionhandler_).md>) — Asynchronously resumes the sync on a paused item using the given resume behavior.
- [NSFileManagerResumeSyncBehavior](../nsfilemanagerresumesyncbehavior.md) — The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<fetchlatestremoteversionofitem(at_completionhandler_).md>) — Asynchronously fetches the latest remote version of a given item from the server.
- [NSFileVersion](../nsfileversion.md) — A snapshot of a file at a specific point in time.
- [- uploadLocalVersionOfUbiquitousItemAtURL:withConflictResolutionPolicy:completionHandler:](<uploadlocalversionofubiquitousitem(at_withconflictresolutionpolicy_completionhandler_).md>) — Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [NSFileManagerUploadLocalVersionConflictPolicy](../nsfilemanageruploadlocalversionconflictpolicy.md) — The policies the file manager can apply to resolve conflicts when uploading a local version of a file.
