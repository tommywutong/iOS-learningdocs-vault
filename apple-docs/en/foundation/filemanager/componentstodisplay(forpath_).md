---
title: 'componentsToDisplay(forPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/componentstodisplay(forpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/componentstodisplay(forpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/componentstodisplay%28forpath%3A%29.json'
content_hash: 'sha256:b44a0cf2ad9e1339'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# componentsToDisplay(forPath:)

<sub>Instance Method</sub>

Returns an array of strings representing the user-visible components of a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func componentsToDisplay(forPath path: String) -> [String]?
```

## Parameters

- `path` — A pathname.

## Return Value

An array of [NSString](../nsstring.md) objects representing the user-visible (for the Finder, Open and Save panels, and so on) components of `path`. Returns `nil` if path does not exist.

## Discussion

These components cannot be used for path operations and are only suitable for display to the user.

## See Also

### Getting and setting attributes

- [- displayNameAtPath:](<displayname(atpath_).md>) — Returns the display name of the file or directory at a specified path.
- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.
