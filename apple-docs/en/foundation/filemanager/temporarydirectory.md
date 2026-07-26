---
title: temporaryDirectory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/temporarydirectory
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/temporarydirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/temporarydirectory.json'
content_hash: 'sha256:5f8990a4ffdd5dbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# temporaryDirectory

<sub>Instance Property</sub>

The temporary directory for the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var temporaryDirectory: URL { get }
```

## See Also

### Accessing user directories

- [homeDirectoryForCurrentUser](homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSHomeDirectory](<../nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSUserName](<../nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<../nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [NSHomeDirectoryForUser](<../nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [NSTemporaryDirectory](<../nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.
