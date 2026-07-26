---
title: 'homeDirectory(forUser:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.12+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/homedirectory(foruser:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/homedirectory(foruser:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/homedirectory%28foruser%3A%29.json'
content_hash: 'sha256:200d32c33be6ba62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# homeDirectory(forUser:)

<sub>Instance Method</sub>

Returns the home directory for the specified user.

<sub>macOS</sub>

```swift
func homeDirectory(forUser userName: String) -> URL?
```

## Parameters

- `userName` — The username of the owner of the desired home directory.

## Return Value

A URL object containing the location of the specified user’s home directory, or `nil` if no such user exists or the user’s home directory is not available.

## See Also

### Accessing user directories

- [homeDirectoryForCurrentUser](homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSHomeDirectory](<../nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSUserName](<../nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<../nsfullusername().md>) — Returns a string containing the full name of the current user.
- [NSHomeDirectoryForUser](<../nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [temporaryDirectory](temporarydirectory.md) — The temporary directory for the current user.
- [NSTemporaryDirectory](<../nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.
