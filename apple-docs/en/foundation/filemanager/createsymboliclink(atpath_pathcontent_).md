---
title: 'createSymbolicLink(atPath:pathContent:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/createsymboliclink(atpath:pathcontent:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/createsymboliclink(atpath:pathcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/createsymboliclink%28atpath%3Apathcontent%3A%29.json'
content_hash: 'sha256:f821d93aa23d2fa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# createSymbolicLink(atPath:pathContent:)

<sub>Instance Method</sub>

Creates a symbolic link identified by a given path that refers to a given location.

> [!warning] Deprecated
> Use [- createSymbolicLinkAtURL:withDestinationURL:error:](<createsymboliclink(at_withdestinationurl_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func createSymbolicLink(atPath path: String, pathContent otherpath: String) -> Bool
```

## Parameters

- `path` — The path for a symbolic link.

- `otherpath` — The path to which `path` should refer.

## Return Value

[true](../../swift/true.md) if the operation is successful, otherwise [false](../../swift/false.md). Returns [false](../../swift/false.md) if a file, directory, or symbolic link identical to `path` already exists.

## Discussion

Creates a symbolic link identified by `path` that refers to the location `otherPath` in the file system.

### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) instead.

## See Also

### Related Documentation

- [- removeItemAtPath:error:](<removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.
- [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
