---
title: FileManager
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager
source_url: 'https://developer.apple.com/documentation/foundation/filemanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager.json'
content_hash: 'sha256:8ee4f516f4458314'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileManager

<sub>Class</sub>

A convenient interface to the contents of the file system, and the primary means of interacting with it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class FileManager
```

## Overview

A file manager object lets you examine the contents of the file system and make changes to it. The [FileManager](filemanager.md) class provides convenient access to a shared file manager object that is suitable for most types of file-related manipulations. A file manager object is typically your primary mode of interaction with the file system. You use it to locate, create, copy, and move files and directories. You also use it to get information about a file or directory or change some of its attributes.

When specifying the location of files, you can use either [NSURL](nsurl.md) or [NSString](nsstring.md) objects. The use of the [NSURL](nsurl.md) class is generally preferred for specifying file-system items because URLs can convert path information to a more efficient representation internally. You can also obtain a bookmark from an [NSURL](nsurl.md) object, which is similar to an alias and offers a more sure way of locating the file or directory later.

If you are moving, copying, linking, or removing files or directories, you can use a delegate in conjunction with a file manager object to manage those operations. The delegate’s role is to affirm the operation and to decide whether to proceed when errors occur. In macOS 10.7 and later, the delegate must conform to the [FileManagerDelegate](filemanagerdelegate.md) protocol.

In iOS 5.0 and later and in macOS 10.7 and later, [FileManager](filemanager.md) includes methods for managing items stored in iCloud. Files and directories tagged for cloud storage are synced to iCloud so that they can be made available to the user’s iOS devices and Macintosh computers. Changes to an item in one location are propagated to all other locations to ensure the items stay in sync.

### Sync control

A [package](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/DocumentPackages/DocumentPackages.html#//apple_ref/doc/uid/10000123i-CH106-SW1) is a directory that the system presents as a single file to the person using the device. Apps with documents that contain multiple files can use packages to manage contents like media assets. In iOS 26 and macOS 26 and later, [FileManager](filemanager.md) introduces methods for controlling how a file provider syncs these items. By pausing sync when your app opens a package and resuming when it closes, your app can prevent the file provider from changing the contents of the package in unexpected ways, which potentially leaves the document in an inconsistent state. You can also use this pause and resume API on regular “flat” files.

### Threading considerations

The methods of the shared [FileManager](filemanager.md) object can be called from multiple threads safely. However, if you use a delegate to receive notifications about the status of move, copy, remove, and link operations, you should create a unique instance of the file manager object, assign your delegate to that object, and use that file manager to initiate your operations.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a file manager

- [+ fileManagerWithAuthorization:](<filemanager/init(authorization_).md>) — Initializes a file manager object that is authorized to perform privileged file system operations.
- [defaultManager](filemanager/default.md) — The shared file manager object for the process.

### Accessing user directories

- [homeDirectoryForCurrentUser](filemanager/homedirectoryforcurrentuser.md) — The home directory for the current user.
- [NSHomeDirectory](<nshomedirectory().md>) — Returns the path to either the user’s or application’s home directory, depending on the platform.
- [NSUserName](<nsusername().md>) — Returns the logon name of the current user.
- [NSFullUserName](<nsfullusername().md>) — Returns a string containing the full name of the current user.
- [- homeDirectoryForUser:](<filemanager/homedirectory(foruser_).md>) — Returns the home directory for the specified user.
- [NSHomeDirectoryForUser](<nshomedirectoryforuser(__).md>) — Returns the path to a given user’s home directory.
- [temporaryDirectory](filemanager/temporarydirectory.md) — The temporary directory for the current user.
- [NSTemporaryDirectory](<nstemporarydirectory().md>) — Returns the path of the temporary directory for the current user.

### Locating system directories

- [- URLForDirectory:inDomain:appropriateForURL:create:error:](<filemanager/url(for_in_appropriatefor_create_).md>) — Locates and optionally creates the specified common directory in a domain.
- [- URLsForDirectory:inDomains:](<filemanager/urls(for_in_).md>) — Returns an array of URLs for the specified common directory in the requested domains.
- [NSSearchPathForDirectoriesInDomains](<nssearchpathfordirectoriesindomains(______).md>) — Creates a list of directory search paths.
- [NSOpenStepRootDirectory](<nsopensteprootdirectory().md>) — Returns the root directory of the user’s system.

### Locating application group container directories

- [- containerURLForSecurityApplicationGroupIdentifier:](<filemanager/containerurl(forsecurityapplicationgroupidentifier_).md>) — Returns the container directory associated with the specified security application group identifier.
- [App Groups Entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md) — A list of identifiers specifying the groups your app belongs to.

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<filemanager/contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<filemanager/contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<filemanager/enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<filemanager/enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [DirectoryEnumerator](filemanager/directoryenumerator.md) — An object that enumerates the contents of a directory.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<filemanager/mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [VolumeEnumerationOptions](filemanager/volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<filemanager/mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsOfDirectoryAtPath:error:](<filemanager/subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- subpathsAtPath:](<filemanager/subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.

### Creating and deleting items

- [- createDirectoryAtURL:withIntermediateDirectories:attributes:error:](<filemanager/createdirectory(at_withintermediatedirectories_attributes_).md>) — Creates a directory with the given attributes at the specified URL.
- [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<filemanager/createdirectory(atpath_withintermediatedirectories_attributes_).md>) — Creates a directory with given attributes at the specified path.
- [- createFileAtPath:contents:attributes:](<filemanager/createfile(atpath_contents_attributes_).md>) — Creates a file with the specified content and attributes at the given location.
- [- removeItemAtURL:error:](<filemanager/removeitem(at_).md>) — Removes the file or directory at the specified URL.
- [- removeItemAtPath:error:](<filemanager/removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- trashItemAtURL:resultingItemURL:error:](<filemanager/trashitem(at_resultingitemurl_).md>) — Moves an item to the trash.

### Replacing items

- [replaceItemAt(_:withItemAt:backupItemName:options:)](<filemanager/replaceitemat(__withitemat_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [- replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:](<filemanager/replaceitem(at_withitemat_backupitemname_options_resultingitemurl_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [ItemReplacementOptions](filemanager/itemreplacementoptions.md) — Options for specifying the behavior of file replacement operations.

### Moving and copying items

- [- copyItemAtURL:toURL:error:](<filemanager/copyitem(at_to_).md>) — Copies the file at the specified URL to a new location synchronously.
- [- copyItemAtPath:toPath:error:](<filemanager/copyitem(atpath_topath_).md>) — Copies the item at the specified path to a new location synchronously.
- [- moveItemAtURL:toURL:error:](<filemanager/moveitem(at_to_).md>) — Moves the file or directory at the specified URL to a new location synchronously.
- [- moveItemAtPath:toPath:error:](<filemanager/moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.

### Managing iCloud-based items

- [ubiquityIdentityToken](filemanager/ubiquityidentitytoken.md) — An opaque token that represents the current user’s iCloud Drive Documents identity.
- [- URLForUbiquityContainerIdentifier:](<filemanager/url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- isUbiquitousItemAtURL:](<filemanager/isubiquitousitem(at_).md>) — Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [- setUbiquitous:itemAtURL:destinationURL:error:](<filemanager/setubiquitous(__itemat_destinationurl_).md>) — Indicates whether the item at the specified URL should be stored in iCloud.
- [- startDownloadingUbiquitousItemAtURL:error:](<filemanager/startdownloadingubiquitousitem(at_).md>) — Starts downloading (if necessary) the specified item to the local system.
- [- evictUbiquitousItemAtURL:error:](<filemanager/evictubiquitousitem(at_).md>) — Removes the local copy of the specified item that’s stored in iCloud.
- [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<filemanager/url(forpublishingubiquitousitemat_expiration_).md>) — Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.

### Accessing file provider services

- [- getFileProviderServicesForItemAtURL:completionHandler:](<filemanager/getfileproviderservicesforitem(at_completionhandler_).md>) — Returns the services provided by the File Provider extension that manages the item at the given URL.
- [NSFileProviderService](nsfileproviderservice.md) — A service that provides a custom communication channel between your app and a File Provider extension.
- [NSFileProviderServiceName](nsfileproviderservicename.md) — The name used to identify a File Provider service.

### Controlling file provider synchronization

- [NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md) — An option set of the sync controls available for an item.
- [- pauseSyncForUbiquitousItemAtURL:completionHandler:](<filemanager/pausesyncforubiquitousitem(at_completionhandler_).md>) — Asynchronously pauses sync of an item at the given URL.
- [- resumeSyncForUbiquitousItemAtURL:withBehavior:completionHandler:](<filemanager/resumesyncforubiquitousitem(at_with_completionhandler_).md>) — Asynchronously resumes the sync on a paused item using the given resume behavior.
- [NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md) — The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [- fetchLatestRemoteVersionOfItemAtURL:completionHandler:](<filemanager/fetchlatestremoteversionofitem(at_completionhandler_).md>) — Asynchronously fetches the latest remote version of a given item from the server.
- [NSFileVersion](nsfileversion.md) — A snapshot of a file at a specific point in time.
- [- uploadLocalVersionOfUbiquitousItemAtURL:withConflictResolutionPolicy:completionHandler:](<filemanager/uploadlocalversionofubiquitousitem(at_withconflictresolutionpolicy_completionhandler_).md>) — Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md) — The policies the file manager can apply to resolve conflicts when uploading a local version of a file.

### Creating symbolic and hard links

- [- createSymbolicLinkAtURL:withDestinationURL:error:](<filemanager/createsymboliclink(at_withdestinationurl_).md>) — Creates a symbolic link at the specified URL that points to an item at the given URL.
- [- createSymbolicLinkAtPath:withDestinationPath:error:](<filemanager/createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.
- [- linkItemAtURL:toURL:error:](<filemanager/linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<filemanager/linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.
- [- destinationOfSymbolicLinkAtPath:error:](<filemanager/destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.

### Determining access to files

- [- fileExistsAtPath:](<filemanager/fileexists(atpath_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- fileExistsAtPath:isDirectory:](<filemanager/fileexists(atpath_isdirectory_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- isReadableFileAtPath:](<filemanager/isreadablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [- isWritableFileAtPath:](<filemanager/iswritablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.
- [- isExecutableFileAtPath:](<filemanager/isexecutablefile(atpath_).md>) — Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
- [- isDeletableFileAtPath:](<filemanager/isdeletablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.

### Getting and setting attributes

- [- componentsToDisplayForPath:](<filemanager/componentstodisplay(forpath_).md>) — Returns an array of strings representing the user-visible components of a given path.
- [- displayNameAtPath:](<filemanager/displayname(atpath_).md>) — Returns the display name of the file or directory at a specified path.
- [- attributesOfItemAtPath:error:](<filemanager/attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- attributesOfFileSystemForPath:error:](<filemanager/attributesoffilesystem(forpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [- setAttributes:ofItemAtPath:error:](<filemanager/setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.

### Getting and comparing file contents

- [- contentsAtPath:](<filemanager/contents(atpath_).md>) — Returns the contents of the file at the specified path.
- [- contentsEqualAtPath:andPath:](<filemanager/contentsequal(atpath_andpath_).md>) — Returns a Boolean value that indicates whether the files or directories in specified paths have the same contents.

### Getting the relationship between items

- [- getRelationship:ofDirectoryAtURL:toItemAtURL:error:](<filemanager/getrelationship(__ofdirectoryat_toitemat_).md>) — Determines the type of relationship that exists between a directory and an item.
- [- getRelationship:ofDirectory:inDomain:toItemAtURL:error:](<filemanager/getrelationship(__of_in_toitemat_).md>) — Determines the type of relationship that exists between a system directory and the specified item.
- [URLRelationship](filemanager/urlrelationship.md) — Constants indicating the relationship between a directory and an item.

### Converting file paths to strings

- [- fileSystemRepresentationWithPath:](<filemanager/filesystemrepresentation(withpath_).md>) — Returns a C-string representation of a given path that properly encodes Unicode strings for use by the file system.
- [- stringWithFileSystemRepresentation:length:](<filemanager/string(withfilesystemrepresentation_length_).md>) — Returns an [NSString](nsstring.md) object whose contents are derived from the specified C-string path.

### Managing the delegate

- [delegate](filemanager/delegate.md) — The delegate of the file manager object.

### Managing the current directory

- [- changeCurrentDirectoryPath:](<filemanager/changecurrentdirectorypath(__).md>) — Changes the path of the current working directory to the specified path.
- [currentDirectoryPath](filemanager/currentdirectorypath.md) — The path to the program’s current directory.

### Unmounting volumes

- [- unmountVolumeAtURL:options:completionHandler:](<filemanager/unmountvolume(at_options_completionhandler_).md>) — Starts the process of unmounting the specified volume.
- [UnmountOptions](filemanager/unmountoptions.md) — Options that specify the behavior of an unmount operation.
- [NSFileManagerUnmountDissentingProcessIdentifierErrorKey](nsfilemanagerunmountdissentingprocessidentifiererrorkey.md) — The process identifier of the process that prevented a volume from unmounting.

### Working with HFS file types

- [NSFileTypeForHFSTypeCode](<nsfiletypeforhfstypecode(__).md>) — Returns a string encoding a file type code.
- [NSHFSTypeCodeFromFileType](<nshfstypecodefromfiletype(__).md>) — Returns a file type code.
- [NSHFSTypeOfFile](<nshfstypeoffile(__).md>) — Returns a string encoding a file type.

### Determining resource fork support

- [NSFoundationVersionWithFileManagerResourceForkSupport](nsfoundationversionwithfilemanagerresourceforksupport.md) — The version of the Foundation framework in which `NSFileManager` first supported resource forks.

### Working with notifications

- [NSUbiquityIdentityDidChangeNotification](nsnotification/name-swift.struct/nsubiquityidentitydidchange.md) — Sent after the iCloud (“ubiquity”) identity has changed.

### Working with notification messages

- [UbiquityIdentityDidChangeMessage](filemanager/ubiquityidentitydidchangemessage.md) — A message a file manager sends after the iCloud (“ubiquity”) identity changes.

### Supporting Types

- [DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDirectory](filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeKey](fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileAttributeType](fileattributetype.md) — Values representing a file’s type attribute.
- [FileProtectionType](fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
- [URLFileProtection](urlfileprotection.md) — Protection-level values for a URL resource key.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<filemanager/changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<filemanager/fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filemanager/filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<filemanager/directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<filemanager/createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<filemanager/createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<filemanager/pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<filemanager/replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_

## See Also

### File system operations

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md) — Prevent data loss and app crashes by interacting with the file system in a coordinated, asynchronous manner and by avoiding unnecessary disk I/O.
- [Using the file system effectively](using-the-file-system-effectively.md) — Gain access to benefits like automatic backup or purging by using purpose-built directories provided by the system.
- [FileManagerDelegate](filemanagerdelegate.md) — The interface a file manager’s delegate uses to intervene during operations or if an error occurs.
- [About Apple File System](about-apple-file-system.md) — Use high-level APIs to get the most out of Apple File System.
