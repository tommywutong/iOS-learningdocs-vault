---
title: FileManager.SearchPathDirectory.itemReplacementDirectory
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdirectory/itemreplacementdirectory
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/itemreplacementdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdirectory/itemreplacementdirectory.json'
content_hash: 'sha256:83403a10359b0817'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [SearchPathDirectory](../searchpathdirectory.md)

# FileManager.SearchPathDirectory.itemReplacementDirectory

<sub>Case</sub>

The constant used to create a temporary directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case itemReplacementDirectory
```

## Discussion

Pass this constant to the [FileManager](../../filemanager.md) method [- URLForDirectory:inDomain:appropriateForURL:create:error:](<../url(for_in_appropriatefor_create_).md>) in order to create a temporary directory.

## See Also

### Directory Locations

- [NSApplicationDirectory](applicationdirectory.md) — Supported applications (`/Applications`).
- [NSDemoApplicationDirectory](demoapplicationdirectory.md) — Unsupported applications and demonstration versions.
- [NSDeveloperApplicationDirectory](developerapplicationdirectory.md) — Developer applications (`/Developer/Applications`).
- [NSAdminApplicationDirectory](adminapplicationdirectory.md) — System and network administration applications.
- [NSLibraryDirectory](librarydirectory.md) — Various user-visible documentation, support, and configuration files (`/Library`).
- [NSDeveloperDirectory](developerdirectory.md) — Developer resources (`/Developer`).
- [NSUserDirectory](userdirectory.md) — User home directories (`/Users`).
- [NSDocumentationDirectory](documentationdirectory.md) — Documentation.
- [NSDocumentDirectory](documentdirectory.md) — Document directory.
- [NSCoreServiceDirectory](coreservicedirectory.md) — Core services (`System/Library/CoreServices`).
- [NSAutosavedInformationDirectory](autosavedinformationdirectory.md) — The user’s autosaved documents (`Library/Autosave Information`).
- [NSDesktopDirectory](desktopdirectory.md) — The user’s desktop directory.
- [NSCachesDirectory](cachesdirectory.md) — Discardable cache files (`Library/Caches`).
- [NSApplicationSupportDirectory](applicationsupportdirectory.md) — Application support files (`Library/Application Support`).
- [NSDownloadsDirectory](downloadsdirectory.md) — The user’s downloads directory.
