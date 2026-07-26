---
title: FileManager.SearchPathDirectory.developerDirectory
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdirectory/developerdirectory
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/developerdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdirectory/developerdirectory.json'
content_hash: 'sha256:55b6d1e091ed35b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [SearchPathDirectory](../searchpathdirectory.md)

# FileManager.SearchPathDirectory.developerDirectory

<sub>Case</sub>

Developer resources (`/Developer`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case developerDirectory
```

## Discussion

Deprecated: As of Xcode 4.3, there is no longer a Developer directory; instead, Xcode.app is a self-contained application that gets installed in the user’s Applications directory, by default, although it can be put anywhere.

## See Also

### Directory Locations

- [NSApplicationDirectory](applicationdirectory.md) — Supported applications (`/Applications`).
- [NSDemoApplicationDirectory](demoapplicationdirectory.md) — Unsupported applications and demonstration versions.
- [NSDeveloperApplicationDirectory](developerapplicationdirectory.md) — Developer applications (`/Developer/Applications`).
- [NSAdminApplicationDirectory](adminapplicationdirectory.md) — System and network administration applications.
- [NSLibraryDirectory](librarydirectory.md) — Various user-visible documentation, support, and configuration files (`/Library`).
- [NSUserDirectory](userdirectory.md) — User home directories (`/Users`).
- [NSDocumentationDirectory](documentationdirectory.md) — Documentation.
- [NSDocumentDirectory](documentdirectory.md) — Document directory.
- [NSCoreServiceDirectory](coreservicedirectory.md) — Core services (`System/Library/CoreServices`).
- [NSAutosavedInformationDirectory](autosavedinformationdirectory.md) — The user’s autosaved documents (`Library/Autosave Information`).
- [NSDesktopDirectory](desktopdirectory.md) — The user’s desktop directory.
- [NSCachesDirectory](cachesdirectory.md) — Discardable cache files (`Library/Caches`).
- [NSApplicationSupportDirectory](applicationsupportdirectory.md) — Application support files (`Library/Application Support`).
- [NSDownloadsDirectory](downloadsdirectory.md) — The user’s downloads directory.
- [NSInputMethodsDirectory](inputmethodsdirectory.md) — Input Methods `(Library/Input Methods)`.
