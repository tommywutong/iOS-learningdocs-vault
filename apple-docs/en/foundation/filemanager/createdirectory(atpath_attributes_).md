---
title: 'createDirectory(atPath:attributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/createdirectory(atpath:attributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/createdirectory(atpath:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/createdirectory%28atpath%3Aattributes%3A%29.json'
content_hash: 'sha256:15b7d28edfa293b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# createDirectory(atPath:attributes:)

<sub>Instance Method</sub>

Creates a directory (without contents) at a given path with given attributes.

> [!warning] Deprecated
> Use [- createDirectoryAtURL:withIntermediateDirectories:attributes:error:](<createdirectory(at_withintermediatedirectories_attributes_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func createDirectory(atPath path: String, attributes: [AnyHashable : Any] = [:]) -> Bool
```

## Parameters

- `path` — The path at which to create the new directory. The directory to be created must not yet exist, but its parent directory must exist.

- `attributes` — The file attributes for the new directory. The attributes you can set are owner and group numbers, file permissions, and modification date. If you specify `nil` for `attributes`, default values for these attributes are set (particularly write access for the creator and read access for others). For a list of keys you can include in this dictionary, Supporting Types. Some of the keys, such as `NSFileHFSCreatorCode` and `NSFileHFSTypeCode`, do not apply to directories.

## Return Value

[true](../../swift/true.md) if the operation was successful, otherwise [false](../../swift/false.md).

## Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<createdirectory(atpath_withintermediatedirectories_attributes_).md>) instead.

## See Also

### Related Documentation

- [- changeCurrentDirectoryPath:](<changecurrentdirectorypath(__).md>) — Changes the path of the current working directory to the specified path.
- [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<createdirectory(atpath_withintermediatedirectories_attributes_).md>) — Creates a directory with given attributes at the specified path.
- [- createFileAtPath:contents:attributes:](<createfile(atpath_contents_attributes_).md>) — Creates a file with the specified content and attributes at the given location.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.
- [currentDirectoryPath](currentdirectorypath.md) — The path to the program’s current directory.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
