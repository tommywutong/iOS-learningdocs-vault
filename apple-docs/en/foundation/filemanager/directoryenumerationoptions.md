---
title: FileManager.DirectoryEnumerationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/directoryenumerationoptions
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directoryenumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directoryenumerationoptions.json'
content_hash: 'sha256:6b473da97edea0ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.DirectoryEnumerationOptions

<sub>Structure</sub>

Options for enumerating the contents of directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DirectoryEnumerationOptions
```

## Overview

These options are used with the [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a Directory Enumeration Options Value

- [init(rawValue:)](<directoryenumerationoptions/init(rawvalue_).md>) — Creates a directory enumeration options value.

### Directory Enumeration Options

- [NSDirectoryEnumerationSkipsSubdirectoryDescendants](directoryenumerationoptions/skipssubdirectorydescendants.md) — An option to perform a shallow enumeration that doesn’t descend into directories.
- [NSDirectoryEnumerationSkipsPackageDescendants](directoryenumerationoptions/skipspackagedescendants.md) — An option to treat packages like files and not descend into their contents.
- [NSDirectoryEnumerationSkipsHiddenFiles](directoryenumerationoptions/skipshiddenfiles.md) — An option to skip hidden files.

### Type Properties

- [NSDirectoryEnumerationIncludesDirectoriesPostOrder](directoryenumerationoptions/includesdirectoriespostorder.md) — An option to skip hidden files.
- [NSDirectoryEnumerationProducesRelativePathURLs](directoryenumerationoptions/producesrelativepathurls.md) — An option to skip hidden files.

## See Also

### Supporting Types

- [SearchPathDirectory](searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeKey](../fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileAttributeType](../fileattributetype.md) — Values representing a file’s type attribute.
- [FileProtectionType](../fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
- [URLFileProtection](../urlfileprotection.md) — Protection-level values for a URL resource key.
