---
title: NSFileManagerSupportedSyncControls
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanagersupportedsynccontrols
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanagersupportedsynccontrols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanagersupportedsynccontrols.json'
content_hash: 'sha256:af06aaf3fcd874b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileManagerSupportedSyncControls

<sub>Structure</sub>

An option set of the sync controls available for an item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSFileManagerSupportedSyncControls
```

## Overview

Get an instance of this type by calling [resourceValues(forKeys:)](<url/resourcevalues(forkeys_).md>) on a [URL](url.md) instance (Swift) or [- getResourceValue:forKey:error:](<nsurl/getresourcevalue(__forkey_).md>) on an [NSURL](nsurl.md) (Swift or Objective-C) and passing in the key [NSURLUbiquitousItemSupportedSyncControlsKey](urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Inspecting supported sync controls

- [NSFileManagerSupportedSyncControlsPauseSync](nsfilemanagersupportedsynccontrols/pausesync.md) — The file provider supports pausing the sync on the item.
- [NSFileManagerSupportedSyncControlsFailUploadOnConflict](nsfilemanagersupportedsynccontrols/failuploadonconflict.md) — The file provider supports failing an upload if the local and server versions conflict.

### Working with raw values

- [init(rawValue:)](<nsfilemanagersupportedsynccontrols/init(rawvalue_).md>)

## See Also

### Controlling file provider synchronization

- [- pauseSyncForUbiquitousItemAtURL:completionHandler:](<filemanager/pausesyncforubiquitousitem(at_completionhandler_).md>) — Asynchronously pauses sync of an item at the given URL.
- [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<filemanager/resumesyncforubiquitousitem(at_with_completionhandler_).md>) — Asynchronously resumes the sync on a paused item using the given resume behavior.
- [NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md) — The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<filemanager/fetchlatestremoteversionofitem(at_completionhandler_).md>) — Asynchronously fetches the latest remote version of a given item from the server.
- [NSFileVersion](nsfileversion.md) — A snapshot of a file at a specific point in time.
- [- uploadLocalVersionOfUbiquitousItemAtURL:withConflictResolutionPolicy:completionHandler:](<filemanager/uploadlocalversionofubiquitousitem(at_withconflictresolutionpolicy_completionhandler_).md>) — Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md) — The policies the file manager can apply to resolve conflicts when uploading a local version of a file.
