---
title: FileManager.SearchPathDirectory.downloadsDirectory
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdirectory/downloadsdirectory
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/downloadsdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdirectory/downloadsdirectory.json'
content_hash: 'sha256:611c2c3415173cbc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [SearchPathDirectory](../searchpathdirectory.md)

# FileManager.SearchPathDirectory.downloadsDirectory

<sub>Case</sub>

The user’s downloads directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case downloadsDirectory
```

## Discussion

The [NSDownloadsDirectory](downloadsdirectory.md) flag only produces a path when you provide a [NSUserDomainMask](../searchpathdomainmask/userdomainmask.md).

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
- [NSInputMethodsDirectory](inputmethodsdirectory.md) — Input Methods `(Library/Input Methods)`.
