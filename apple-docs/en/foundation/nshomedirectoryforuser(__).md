---
title: 'NSHomeDirectoryForUser(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshomedirectoryforuser(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshomedirectoryforuser(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshomedirectoryforuser%28_%3A%29.json'
content_hash: 'sha256:b1242c38a034abc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHomeDirectoryForUser(_:)

<sub>Function</sub>

Returns the path to a given user’s home directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSHomeDirectoryForUser(_ userName: String?) -> String?
```

## Parameters

- `userName` — The name of a user.

## Return Value

The path to the home directory for the user specified by `userName`.

## Discussion

For more information on file system utilities, see Low-Level File Management Programming Topics.

## See Also

### Accessing user directories

- [homeDirectoryForCurrentUser](filemanager/homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSHomeDirectory](<nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSUserName](<nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<filemanager/homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [temporaryDirectory](filemanager/temporarydirectory.md) — The temporary directory for the current user.
- [NSTemporaryDirectory](<nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.
