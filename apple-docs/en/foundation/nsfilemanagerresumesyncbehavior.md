---
title: NSFileManagerResumeSyncBehavior
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanagerresumesyncbehavior
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanagerresumesyncbehavior.json'
content_hash: 'sha256:20976a528a3e6d1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileManagerResumeSyncBehavior

<sub>Enumeration</sub>

The behaviors the file manager can apply to resolve conflicts when resuming a sync.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum NSFileManagerResumeSyncBehavior
```

## Overview

You use this type when calling [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<filemanager/resumesyncforubiquitousitem(at_with_completionhandler_).md>) to resume synchronizing. In most situations, the [NSFileManagerResumeSyncBehaviorPreserveLocalChanges](nsfilemanagerresumesyncbehavior/preservelocalchanges.md) behavior is the best choice to avoid risk of data loss.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying sync behaviors

- [NSFileManagerResumeSyncBehaviorPreserveLocalChanges](nsfilemanagerresumesyncbehavior/preservelocalchanges.md) — Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehaviorAfterUploadWithFailOnConflict](nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict.md) — Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.
- [NSFileManagerResumeSyncBehaviorDropLocalChanges](nsfilemanagerresumesyncbehavior/droplocalchanges.md) — Resumes synchronizing by overwriting any local changes with the remote version of the file.

### Working with raw values

- [init(rawValue:)](<nsfilemanagerresumesyncbehavior/init(rawvalue_).md>)

## See Also

### Controlling file provider synchronization

- [NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md) — An option set of the sync controls available for an item.
- [- pauseSyncForUbiquitousItemAtURL:completionHandler:](<filemanager/pausesyncforubiquitousitem(at_completionhandler_).md>) — Asynchronously pauses sync of an item at the given URL.
- [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<filemanager/resumesyncforubiquitousitem(at_with_completionhandler_).md>) — Asynchronously resumes the sync on a paused item using the given resume behavior.
- [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<filemanager/fetchlatestremoteversionofitem(at_completionhandler_).md>) — Asynchronously fetches the latest remote version of a given item from the server.
- [NSFileVersion](nsfileversion.md) — A snapshot of a file at a specific point in time.
- [- uploadLocalVersionOfUbiquitousItemAtURL:withConflictResolutionPolicy:completionHandler:](<filemanager/uploadlocalversionofubiquitousitem(at_withconflictresolutionpolicy_completionhandler_).md>) — Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md) — The policies the file manager can apply to resolve conflicts when uploading a local version of a file.
