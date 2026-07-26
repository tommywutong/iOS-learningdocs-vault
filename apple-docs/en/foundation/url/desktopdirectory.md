---
title: desktopDirectory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/desktopdirectory
source_url: 'https://developer.apple.com/documentation/foundation/url/desktopdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/desktopdirectory.json'
content_hash: 'sha256:1798ac7c5163dc57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# desktopDirectory

<sub>Type Property</sub>

The standard directory for files on the desktop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var desktopDirectory: URL { get }
```

## Discussion

In iOS, this directory is within the app’s sandbox directory. In macOS, it’s within the app’s sandbox directory for sandboxed apps, or in the current user’s home directory `(~/Desktop)` if the app isn’t sandboxed.

This computed property is equivalent to calling [NSSearchPathForDirectoriesInDomains](<../nssearchpathfordirectoriesindomains(______).md>) with the [NSDesktopDirectory](../filemanager/searchpathdirectory/desktopdirectory.md) parameter.

## See Also

### Accessing common directories

- [applicationDirectory](applicationdirectory.md) — The standard directory for apps.
- [applicationSupportDirectory](applicationsupportdirectory.md) — The standard directory for application support files.
- [cachesDirectory](cachesdirectory.md) — The standard directory for discardable cache files.
- [documentsDirectory](documentsdirectory.md) — The standard directory for document files.
- [downloadsDirectory](downloadsdirectory.md) — The standard directory for download files.
- [libraryDirectory](librarydirectory.md) — The standard directory for documentation, support, and configuration files.
- [moviesDirectory](moviesdirectory.md) — The standard directory for movie files.
- [musicDirectory](musicdirectory.md) — The standard directory for music files.
- [picturesDirectory](picturesdirectory.md) — The standard directory for image files.
- [sharedPublicDirectory](sharedpublicdirectory.md) — The standard directory for publicly shared files.
- [temporaryDirectory](temporarydirectory.md) — The standard directory for temporary files.
- [trashDirectory](trashdirectory.md) — The standard trash directory.
- [userDirectory](userdirectory.md) — The container directory of user home directories.
