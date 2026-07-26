---
title: 'pathContentOfSymbolicLink(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/pathcontentofsymboliclink(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/pathcontentofsymboliclink(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/pathcontentofsymboliclink%28atpath%3A%29.json'
content_hash: 'sha256:a5a7b4f8c98012d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# pathContentOfSymbolicLink(atPath:)

<sub>Instance Method</sub>

Returns the path of the directory or file that a symbolic link at a given path refers to.

> [!warning] Deprecated
> Use [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func pathContentOfSymbolicLink(atPath path: String) -> String?
```

## Parameters

- `path` — The path of a symbolic link.

## Return Value

The path of the directory or file to which the symbolic link `path` refers, or `nil` upon failure. If the symbolic link is specified as a relative path, that relative path is returned.

## Discussion

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) instead.

## See Also

### Related Documentation

- [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.
- [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
