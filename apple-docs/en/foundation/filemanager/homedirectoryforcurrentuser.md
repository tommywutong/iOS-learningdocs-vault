---
title: homeDirectoryForCurrentUser
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.12+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/homedirectoryforcurrentuser
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/homedirectoryforcurrentuser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/homedirectoryforcurrentuser.json'
content_hash: 'sha256:07effb5891725ab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# homeDirectoryForCurrentUser

<sub>Instance Property</sub>

The home directory for the current user.

<sub>macOS</sub>

```swift
var homeDirectoryForCurrentUser: URL { get }
```

## See Also

### Accessing user directories

- [NSHomeDirectory](<../nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSUserName](<../nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<../nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [NSHomeDirectoryForUser](<../nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [temporaryDirectory](temporarydirectory.md) — The temporary directory for the current user.
- [NSTemporaryDirectory](<../nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.
