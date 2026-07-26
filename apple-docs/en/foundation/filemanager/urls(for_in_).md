---
title: 'urls(for:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/urls(for:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/urls(for:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/urls%28for%3Ain%3A%29.json'
content_hash: 'sha256:210a5a7511b464db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# urls(for:in:)

<sub>Instance Method</sub>

Returns an array of URLs for the specified common directory in the requested domains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urls(for directory: FileManager.SearchPathDirectory, in domainMask: FileManager.SearchPathDomainMask) -> [URL]
```

## Parameters

- `directory` — The search path directory. The supported values are described in [SearchPathDirectory](searchpathdirectory.md).

- `domainMask` — The file system domain to search. The value for this parameter is one or more of the constants described in [SearchPathDomainMask](searchpathdomainmask.md).

## Return Value

An array of [NSURL](../nsurl.md) objects identifying the requested directories. The directories are ordered according to the order of the domain mask constants, with items in the user domain first and items in the system domain last.

## Discussion

This method is intended to locate known and common directories in the system. For example, setting the directory to [NSApplicationDirectory](searchpathdirectory/applicationdirectory.md), will return the Applications directories in the requested domain. There are a number of common directories available in the [SearchPathDirectory](searchpathdirectory.md), including: [NSDesktopDirectory](searchpathdirectory/desktopdirectory.md), [NSApplicationSupportDirectory](searchpathdirectory/applicationsupportdirectory.md), and many more.

## See Also

### Locating system directories

- [- URLForDirectory:inDomain:appropriateForURL:create:error:](<url(for_in_appropriatefor_create_).md>) — Locates and optionally creates the specified common directory in a domain.
- [NSSearchPathForDirectoriesInDomains](<../nssearchpathfordirectoriesindomains(______).md>) — Creates a list of directory search paths.
- [NSOpenStepRootDirectory](<../nsopensteprootdirectory().md>) — Returns the root directory of the user’s system.
