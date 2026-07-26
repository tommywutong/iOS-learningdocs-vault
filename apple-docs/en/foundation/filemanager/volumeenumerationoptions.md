---
title: FileManager.VolumeEnumerationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/volumeenumerationoptions
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/volumeenumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/volumeenumerationoptions.json'
content_hash: 'sha256:f385f6c7f5ede415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.VolumeEnumerationOptions

<sub>Structure</sub>

Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct VolumeEnumerationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a Volume Enumeration Options Value

- [init(rawValue:)](<volumeenumerationoptions/init(rawvalue_).md>) — Create a volume enumeration options value.

### Volume Enumeration Options

- [NSVolumeEnumerationSkipHiddenVolumes](volumeenumerationoptions/skiphiddenvolumes.md) — The enumeration skips hidden volumes.
- [NSVolumeEnumerationProduceFileReferenceURLs](volumeenumerationoptions/producefilereferenceurls.md) — The enumeration produces file reference URLs rather than path-based URLs.

## See Also

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [DirectoryEnumerator](directoryenumerator.md) — An object that enumerates the contents of a directory.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
