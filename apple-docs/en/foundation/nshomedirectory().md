---
title: NSHomeDirectory()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshomedirectory()
source_url: 'https://developer.apple.com/documentation/foundation/nshomedirectory()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshomedirectory%28%29.json'
content_hash: 'sha256:274dfd0ce668a181'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHomeDirectory()

<sub>Function</sub>

Returns the path to either the user’s or application’s home directory, depending on the platform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSHomeDirectory() -> String
```

## Return Value

The path to the current home directory.

## Discussion

In iOS, the home directory is the application’s sandbox directory. In macOS, it’s the application’s sandbox directory, or the current user’s home directory if the application isn’t in a sandbox.

## See Also

### Accessing user directories

- [homeDirectoryForCurrentUser](filemanager/homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSUserName](<nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<filemanager/homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [NSHomeDirectoryForUser](<nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [temporaryDirectory](filemanager/temporarydirectory.md) — The temporary directory for the current user.
- [NSTemporaryDirectory](<nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.
