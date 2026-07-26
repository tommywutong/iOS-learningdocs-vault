---
title: userDirectory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/userdirectory
source_url: 'https://developer.apple.com/documentation/foundation/url/userdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/userdirectory.json'
content_hash: 'sha256:e8e0fd97763bdd5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# userDirectory

<sub>Type Property</sub>

The container directory of user home directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var userDirectory: URL { get }
```

## Discussion

In iOS, this directory is within the app’s sandbox directory. In macOS, it’s within the app’s sandbox directory for sandboxed apps, or the `/Users` directory if the app isn’t sandboxed.

This computed property is equivalent to calling [NSSearchPathForDirectoriesInDomains](<../nssearchpathfordirectoriesindomains(______).md>) with the [NSUserDirectory](../filemanager/searchpathdirectory/userdirectory.md) parameter.

## See Also

### Accessing common directories

- [applicationDirectory](applicationdirectory.md) — The standard directory for apps.
- [applicationSupportDirectory](applicationsupportdirectory.md) — The standard directory for application support files.
- [cachesDirectory](cachesdirectory.md) — The standard directory for discardable cache files.
- [desktopDirectory](desktopdirectory.md) — The standard directory for files on the desktop.
- [documentsDirectory](documentsdirectory.md) — The standard directory for document files.
- [downloadsDirectory](downloadsdirectory.md) — The standard directory for download files.
- [libraryDirectory](librarydirectory.md) — The standard directory for documentation, support, and configuration files.
- [moviesDirectory](moviesdirectory.md) — The standard directory for movie files.
- [musicDirectory](musicdirectory.md) — The standard directory for music files.
- [picturesDirectory](picturesdirectory.md) — The standard directory for image files.
- [sharedPublicDirectory](sharedpublicdirectory.md) — The standard directory for publicly shared files.
- [temporaryDirectory](temporarydirectory.md) — The standard directory for temporary files.
- [trashDirectory](trashdirectory.md) — The standard trash directory.
