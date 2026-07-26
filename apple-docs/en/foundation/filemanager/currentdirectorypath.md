---
title: currentDirectoryPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/currentdirectorypath
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/currentdirectorypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/currentdirectorypath.json'
content_hash: 'sha256:da9d1539c6109192'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# currentDirectoryPath

<sub>Instance Property</sub>

The path to the program’s current directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentDirectoryPath: String { get }
```

## Discussion

The current directory path is the starting point for any relative paths you specify. For example, if the current directory is `/tmp` and you specify a relative pathname of `reports/info.txt`, the resulting full path for the item is `/tmp/reports/info.txt`.

When an app is launched, this property is initially set to the app’s current working directory. If the current working directory is not accessible for any reason, the value of this property is `nil`. You can change the value of this property by calling the [- changeCurrentDirectoryPath:](<changecurrentdirectorypath(__).md>) method.

> [!warning] Warning
> This property reports the current working directory for the current process, not just the receiver.

## See Also

### Related Documentation

- [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<createdirectory(atpath_withintermediatedirectories_attributes_).md>) — Creates a directory with given attributes at the specified path.

### Managing the current directory

- [- changeCurrentDirectoryPath:](<changecurrentdirectorypath(__).md>) — Changes the path of the current working directory to the specified path.
