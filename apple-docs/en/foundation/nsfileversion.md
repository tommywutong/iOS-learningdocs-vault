---
title: NSFileVersion
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion.json'
content_hash: 'sha256:5feea95a36b6cc1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileVersion

<sub>Class</sub>

A snapshot of a file at a specific point in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSFileVersion
```

## Overview

Use the methods of this class to access, create, and manage file revisions in your app.

Each file version instance contains metadata about a single revision, including the location of the associated file, the modification date of the revision, and whether the revision is discardable.

In Mac apps, you can use file version objects to track changes to a local file over time and to prevent the loss of data during editing. When managing local versions, the document architecture creates versions at specific points in the lifetime of your application. Your application can also create versions explicitly at times that your application designates as appropriate.

In addition to managing local files, the system also uses this class to manage cloud-based files. For files in the cloud, there is usually only one version of the file at any given time. However, additional file versions may be created in cases where two different computers attempt to save the file to the cloud at the same time. In that case, one file is chosen as the current version and any other versions are tagged as being in conflict with the original. Conflict versions are reported to the appropriate file presenter objects and should be resolved as soon as possible so that the corresponding files can be removed from the cloud.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the Version of a File

- [+ currentVersionOfItemAtURL:](<nsfileversion/currentversionofitem(at_).md>) — Returns the most recent version object for the file at the specified URL.
- [+ otherVersionsOfItemAtURL:](<nsfileversion/otherversionsofitem(at_).md>) — Returns all versions of the specified file except the current version.
- [+ versionOfItemAtURL:forPersistentIdentifier:](<nsfileversion/version(itemat_forpersistentidentifier_).md>) — Returns the version of the file that has the specified persistent ID.
- [+ temporaryDirectoryURLForNewVersionOfItemAtURL:](<nsfileversion/temporarydirectoryurlfornewversionofitem(at_).md>) — Creates and returns a temporary directory to use for saving the contents of the file.

### Creating a New Version

- [+ addVersionOfItemAtURL:withContentsOfURL:options:error:](<nsfileversion/addofitem(at_withcontentsof_options_).md>) — Creates a version of the file at the specified location.

### Accessing the Version Information

- [URL](nsfileversion/url.md) — The URL identifying the location of the file associated with the file version object.
- [localizedName](nsfileversion/localizedname.md) — The string containing the user-presentable name of the file version.
- [localizedNameOfSavingComputer](nsfileversion/localizednameofsavingcomputer.md) — The user-presentable name of the computer on which the revision was saved.
- [modificationDate](nsfileversion/modificationdate.md) — The modification date of the version.
- [persistentIdentifier](nsfileversion/persistentidentifier.md) — The identifier for this version of the file.
- [discardable](nsfileversion/isdiscardable.md) — A Boolean value that specifies whether the system can delete the associated file at some future time.

### Handling Version Conflicts

- [conflict](nsfileversion/isconflict.md) — A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [resolved](nsfileversion/isresolved.md) — A Boolean value that indicates if the version object is in conflict or not.
- [+ unresolvedConflictVersionsOfItemAtURL:](<nsfileversion/unresolvedconflictversionsofitem(at_).md>) — Returns an array of version objects that are currently in conflict for the specified URL.

### Replacing and Deleting Versions

- [- replaceItemAtURL:options:error:](<nsfileversion/replaceitem(at_options_).md>) — Replace the contents of the specified file with the contents of the current version’s file.
- [- removeAndReturnError:](<nsfileversion/remove().md>) — Remove this version object and its associated file from the version store.
- [+ removeOtherVersionsOfItemAtURL:error:](<nsfileversion/removeotherversionsofitem(at_).md>) — Removes all versions of a file, except the current one, from the version store.

### Constants

- [AddingOptions](nsfileversion/addingoptions.md) — Options for adding a new file version.
- [ReplacingOptions](nsfileversion/replacingoptions.md) — Options for replacing a file version.

### Initializers

- [init(ofItemAtURL:forPersistentIdentifier:)](<nsfileversion/init(ofitematurl_forpersistentidentifier_).md>)

### Instance Properties

- [hasLocalContents](nsfileversion/haslocalcontents.md) — Whether the version has local contents. Versions that are returned by +getNonlocalVersionsOfItemAtURL:completionHandler: do not initially have local contents. You can only access their contents, either directly via the URL or by invoking -replaceItemAtURL:options:error:, from within a coordinated read on the NSFileVersion’s URL.
- [hasThumbnail](nsfileversion/hasthumbnail.md) — Whether the version has a thumbnail image available. Thumbnails for versions from +getNonlocalVersionsOfItemAtURL:completionHandler: may not immediately be available. As soon as it becomes available, this property will change from NO to YES. You can use KVO to be notified of this change. If a thumbnail is available, you can access it using NSURLThumbnailKey or NSURLThumbnailDictionaryKey.
- [originatorNameComponents](nsfileversion/originatornamecomponents.md) — The name components of the user who created this version of the file. Is nil if the file is not shared or if the current user is the originator.

### Type Methods

- [+ getNonlocalVersionsOfItemAtURL:completionHandler:](<nsfileversion/getnonlocalversionsofitem(at_completionhandler_).md>) — Asynchronously returns an array of NSFileVersions associated with the file located by the given URL, or nil if there is no such file or another error occurs.

## See Also

### Managed file access

- [FileHandle](filehandle.md) — An object-oriented wrapper for a file descriptor.
- [NSFileSecurity](nsfilesecurity.md) — A stub class that encapsulates security information about a file.
- [FileWrapper](filewrapper.md) — A representation of a node (a file, directory, or symbolic link) in the file system.
