---
title: 'NSSearchPathForDirectoriesInDomains(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssearchpathfordirectoriesindomains(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssearchpathfordirectoriesindomains(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssearchpathfordirectoriesindomains%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:de88e49b4a7a83df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSearchPathForDirectoriesInDomains(_:_:_:)

<sub>Function</sub>

Creates a list of directory search paths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSSearchPathForDirectoriesInDomains(_ directory: FileManager.SearchPathDirectory, _ domainMask: FileManager.SearchPathDomainMask, _ expandTilde: Bool) -> [String]
```

## Discussion

Creates a list of path strings for the specified directories in the specified domains. The list is in the order in which you should search the directories. If `expandTilde` is [true](../swift/true.md), tildes are expanded as described in [stringByExpandingTildeInPath](nsstring/expandingtildeinpath.md).

You should consider using the [FileManager](filemanager.md) methods [- URLsForDirectory:inDomains:](<filemanager/urls(for_in_).md>) and [- URLForDirectory:inDomain:appropriateForURL:create:error:](<filemanager/url(for_in_appropriatefor_create_).md>). which return URLs, which are the preferred format.

For more information on file system utilities, see [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

> [!note] Note
> The directory returned by this method may not exist. This method simply gives you the appropriate location for the requested directory. Depending on the application’s needs, it may be up to the developer to create the appropriate directory and any in between.

## See Also

### Locating system directories

- [- URLForDirectory:inDomain:appropriateForURL:create:error:](<filemanager/url(for_in_appropriatefor_create_).md>) — Locates and optionally creates the specified common directory in a domain.
- [- URLsForDirectory:inDomains:](<filemanager/urls(for_in_).md>) — Returns an array of URLs for the specified common directory in the requested domains.
- [NSOpenStepRootDirectory](<nsopensteprootdirectory().md>) — Returns the root directory of the user’s system.
