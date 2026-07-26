---
title: NSFileManagerUploadLocalVersionConflictPolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy.json'
content_hash: 'sha256:2bcfee8fa75ed3dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileManagerUploadLocalVersionConflictPolicy

<sub>Enumeration</sub>

The policies the file manager can apply to resolve conflicts when uploading a local version of a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum NSFileManagerUploadLocalVersionConflictPolicy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with conflict policies

- [NSFileManagerUploadConflictPolicyDefault](nsfilemanageruploadlocalversionconflictpolicy/conflictpolicydefault.md) — Resolves the conflict using the policy defined by the file provider.
- [NSFileManagerUploadConflictPolicyFailOnConflict](nsfilemanageruploadlocalversionconflictpolicy/conflictpolicyfailonconflict.md) — Resolves the conflict by causing the upload to fail.

### Working with raw values

- [init(rawValue:)](<nsfilemanageruploadlocalversionconflictpolicy/init(rawvalue_).md>)

## See Also

### Controlling file provider synchronization

- [NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md) — An option set of the sync controls available for an item.
- [- pauseSyncForUbiquitousItemAtURL:completionHandler:](<filemanager/pausesyncforubiquitousitem(at_completionhandler_).md>) — Asynchronously pauses sync of an item at the given URL.
- [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<filemanager/resumesyncforubiquitousitem(at_with_completionhandler_).md>) — Asynchronously resumes the sync on a paused item using the given resume behavior.
- [NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md) — The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<filemanager/fetchlatestremoteversionofitem(at_completionhandler_).md>) — Asynchronously fetches the latest remote version of a given item from the server.
- [NSFileVersion](nsfileversion.md) — A snapshot of a file at a specific point in time.
- [- uploadLocalVersionOfUbiquitousItemAtURL:withConflictResolutionPolicy:completionHandler:](<filemanager/uploadlocalversionofubiquitousitem(at_withconflictresolutionpolicy_completionhandler_).md>) — Asynchronously uploads the local version of the item using the provided conflict resolution policy.
