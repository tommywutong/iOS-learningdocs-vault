---
title: 'fileSystemAttributes(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/filesystemattributes(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/filesystemattributes(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/filesystemattributes%28atpath%3A%29.json'
content_hash: 'sha256:a601ef2cb4b577f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# fileSystemAttributes(atPath:)

<sub>Instance Method</sub>

Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.

> [!warning] Deprecated
> Use [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func fileSystemAttributes(atPath path: String) -> [AnyHashable : Any]?
```

## Parameters

- `path` — Any pathname within the mounted file system.

## Return Value

An `NSDictionary` object that describes the attributes of the mounted file system on which `path` resides. See `File-System Attribute Keys` for a description of the keys available in the dictionary.

## Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) instead.

## See Also

### Related Documentation

- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- directoryContentsAtPath:](<directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
