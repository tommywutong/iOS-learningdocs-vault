---
title: NSUserName()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsusername()
source_url: 'https://developer.apple.com/documentation/foundation/nsusername()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusername%28%29.json'
content_hash: 'sha256:367003749fb52696'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserName()

<sub>Function</sub>

Returns the logon name of the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSUserName() -> String
```

## Return Value

The logon name of the current user.

## See Also

### Accessing user directories

- [homeDirectoryForCurrentUser](filemanager/homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSHomeDirectory](<nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSFullUserName](<nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<filemanager/homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [NSHomeDirectoryForUser](<nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [temporaryDirectory](filemanager/temporarydirectory.md) — The temporary directory for the current user.
- [NSTemporaryDirectory](<nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.
