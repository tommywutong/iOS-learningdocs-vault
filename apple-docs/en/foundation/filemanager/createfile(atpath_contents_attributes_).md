---
title: 'createFile(atPath:contents:attributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/createfile(atpath:contents:attributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/createfile(atpath:contents:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/createfile%28atpath%3Acontents%3Aattributes%3A%29.json'
content_hash: 'sha256:cb2916d0df29c7e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# createFile(atPath:contents:attributes:)

<sub>Instance Method</sub>

Creates a file with the specified content and attributes at the given location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createFile(atPath path: String, contents data: Data?, attributes attr: [FileAttributeKey : Any]? = nil) -> Bool
```

## Parameters

- `path` — The path for the new file.

- `data` — A data object containing the contents of the new file.

- `attr` — A dictionary containing the attributes to associate with the new file. You can use these attributes to set the owner and group numbers, file permissions, and modification date. For a list of keys, see [FileAttributeKey](../fileattributekey.md). If you specify `nil` for `attributes`, the file is created with a set of default attributes.

## Return Value

[true](../../swift/true.md) if the operation was successful or if the item already exists, otherwise [false](../../swift/false.md).

## Discussion

If you specify `nil` for the `attributes` parameter, this method uses a default set of values for the owner, group, and permissions of any newly created directories in the path. Similarly, if you omit a specific attribute, the default value is used. The default values for newly created files are as follows:

- Permissions are set according to the umask of the current process. For more information, see umask.
- The owner ID is set to the effective user ID of the process.
- The group ID is set to that of the parent directory.

If a file already exists at `path`, this method overwrites the contents of that file if the current process has the appropriate privileges to do so.

## See Also

### Related Documentation

- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- contentsAtPath:](<contents(atpath_).md>) — Returns the contents of the file at the specified path.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.
- [FileAttributeKey](../fileattributekey.md) — Keys in dictionaries used to get and set file attributes.

### Creating and deleting items

- [- createDirectoryAtURL:withIntermediateDirectories:attributes:error:](<createdirectory(at_withintermediatedirectories_attributes_).md>) — Creates a directory with the given attributes at the specified URL.
- [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<createdirectory(atpath_withintermediatedirectories_attributes_).md>) — Creates a directory with given attributes at the specified path.
- [- removeItemAtURL:error:](<removeitem(at_).md>) — Removes the file or directory at the specified URL.
- [- removeItemAtPath:error:](<removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- trashItemAtURL:resultingItemURL:error:](<trashitem(at_resultingitemurl_).md>) — Moves an item to the trash.
