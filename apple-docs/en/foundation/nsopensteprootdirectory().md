---
title: NSOpenStepRootDirectory()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsopensteprootdirectory()
source_url: 'https://developer.apple.com/documentation/foundation/nsopensteprootdirectory()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsopensteprootdirectory%28%29.json'
content_hash: 'sha256:822c3bd03bb714b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOpenStepRootDirectory()

<sub>Function</sub>

Returns the root directory of the user’s system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSOpenStepRootDirectory() -> String
```

## Return Value

A string identifying the root directory of the user’s system.

## Discussion

For more information on file system utilities, see Low-Level File Management Programming Topics.

## See Also

### Related Documentation

- [NSHomeDirectory](<nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSHomeDirectoryForUser](<nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.

### Locating system directories

- [- URLForDirectory:inDomain:appropriateForURL:create:error:](<filemanager/url(for_in_appropriatefor_create_).md>) — Locates and optionally creates the specified common directory in a domain.
- [- URLsForDirectory:inDomains:](<filemanager/urls(for_in_).md>) — Returns an array of URLs for the specified common directory in the requested domains.
- [NSSearchPathForDirectoriesInDomains](<nssearchpathfordirectoriesindomains(______).md>) — Creates a list of directory search paths.
