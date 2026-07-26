---
title: 'directoryContents(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/directorycontents(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directorycontents(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directorycontents%28atpath%3A%29.json'
content_hash: 'sha256:11264edef1a825a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# directoryContents(atPath:)

<sub>Instance Method</sub>

Returns the directories and files (including symbolic links) contained in a given directory.

> [!warning] Deprecated
> Use [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func directoryContents(atPath path: String) -> [Any]?
```

## Parameters

- `path` — A path to a directory.

## Return Value

An array of [NSString](../nsstring.md) objects identifying the directories and files (including symbolic links) contained in `path`. Returns an empty array if the directory exists but has no contents. Returns `nil` if the directory specified at `path` does not exist or there is some other error accessing it.

## Discussion

The search is shallow, and therefore does not return the contents of any subdirectories and does not traverse symbolic links in the specified directory. This returned array does not contain strings for the current directory (”`.`”), parent directory (”`..`”), or resource forks (begin with “._”).

### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) instead.

## See Also

### Related Documentation

- [currentDirectoryPath](currentdirectorypath.md) — The path to the program’s current directory.
- [- fileExistsAtPath:isDirectory:](<fileexists(atpath_isdirectory_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
