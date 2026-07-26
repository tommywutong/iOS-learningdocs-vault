---
title: 'displayName(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/displayname(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/displayname(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/displayname%28atpath%3A%29.json'
content_hash: 'sha256:1f25e5eb1ee96e3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# displayName(atPath:)

<sub>Instance Method</sub>

Returns the display name of the file or directory at a specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func displayName(atPath path: String) -> String
```

## Parameters

- `path` — The path of a file or directory.

## Return Value

The name of the file or directory at `path` in a localized form appropriate for presentation to the user. If there is no file or directory at `path`, or if an error occurs, returns `path` as is.

## Discussion

Display names are user-friendly names for files. They are typically used to localize standard file and directory names according to the user’s language settings. They may also reflect other modifications, such as the removal of filename extensions. Such modifications are used only when displaying the file or directory to the user and do not reflect the actual path to the item in the file system. For example, if the current user’s preferred language is French, the following code fragment logs the name `Bibliothèque` and not the name `Library`, which is the actual name of the directory.

```objc
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSLibraryDirectory, NSUserDomainMask, YES);
if ([paths count] > 0)
{
    NSString *documentsDirectory = [paths objectAtIndex:0];
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSString *displayNameAtPath = [fileManager displayNameAtPath:documentsDirectory];
    NSLog(@"%@", displayNameAtPath);
}
```

## See Also

### Getting and setting attributes

- [- componentsToDisplayForPath:](<componentstodisplay(forpath_).md>) — Returns an array of strings representing the user-visible components of a given path.
- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.
