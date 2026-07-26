---
title: NSTemporaryDirectory()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstemporarydirectory()
source_url: 'https://developer.apple.com/documentation/foundation/nstemporarydirectory()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstemporarydirectory%28%29.json'
content_hash: 'sha256:6f7f91c53f2c06c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSTemporaryDirectory()

<sub>Function</sub>

Returns the path of the temporary directory for the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSTemporaryDirectory() -> String
```

## Return Value

A string containing the path of the temporary directory for the current user.

## Discussion

See the [FileManager](filemanager.md) method [- URLForDirectory:inDomain:appropriateForURL:create:error:](<filemanager/url(for_in_appropriatefor_create_).md>) for the preferred means of finding the correct temporary directory.

For more information about temporary files, see [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

## See Also

### Related Documentation

- [NSSearchPathForDirectoriesInDomains](<nssearchpathfordirectoriesindomains(______).md>) — Creates a list of directory search paths.

### Accessing user directories

- [homeDirectoryForCurrentUser](filemanager/homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSHomeDirectory](<nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSUserName](<nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<filemanager/homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [NSHomeDirectoryForUser](<nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [temporaryDirectory](filemanager/temporarydirectory.md) — The temporary directory for the current user.
