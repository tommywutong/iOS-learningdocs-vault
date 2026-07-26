---
title: CFURL
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurl
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurl.json'
content_hash: 'sha256:810a869b57dc54e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURL

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFURL
```

## Overview

The `CFURL` opaque type provides facilities for creating, parsing, and dereferencing URL strings. `CFURL` is useful to applications that need to use URLs to access resources, including local files.

A `CFURL` object is composed of two parts—a base URL, which can be `NULL`, and a string that is resolved relative to the base URL. A `CFURL` object whose string is fully resolved without a base URL is considered absolute; all others are considered relative.

`CFURL` is “toll-free bridged” with its Cocoa Foundation counterpart, [NSURL](../foundation/nsurl.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSURL *` parameter, you can pass in a `CFURLRef`, and in a function where you see a `CFURLRef` parameter, you can pass in an `NSURL` instance. This also applies to concrete subclasses of `NSURL`. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

Starting in OS X v10.6, the `CFURL` opaque type provides a facility for creating and using bookmarks. A _bookmark_ provides a persistent reference to a file-system resource. When you resolve a bookmark, you obtain a URL to the resource’s current location. A bookmark’s association with a file-system resource (typically a file or folder) usually continues to work if the user moves or renames the resource, or if the user relaunches your app or restarts the system.

In a macOS app that adopts App Sandbox, to gain persistent access to a file-system resource you must use a _security-scoped bookmark_. Such a bookmark preserves, across app launches, a user’s intent to give your app access to a resource. For details on how this works, including information on the entitlements you need in your Xcode project, read [Security-Scoped Bookmarks and Persistent Resource Access](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

When you resolve a security-scoped bookmark, you get a security-scoped URL. The file system resource that the URL points to is not available for use inside your app’s sandbox until you call the [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) function (or its Cocoa equivalent, the [startAccessingSecurityScopedResource()](<../foundation/nsurl/startaccessingsecurityscopedresource().md>) method) on the URL.

When you no longer need access to a resource that you obtained using security scope (typically, after you close the resource) you must call the [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) method (or its Cocoa equivalent, the [stopAccessingSecurityScopedResource()](<../foundation/nsurl/stopaccessingsecurityscopedresource().md>) method) on the resource’s URL.

> [!warning] Warning
> You must balance every call to the [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) method with a corresponding call to the [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) method. If you fail to relinquish your access when you no longer need a file-system resource, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, such as via Powerbox or security-scoped bookmarks, until relaunched.

The functions for using security-scoped bookmarks are described in this document in Working with Bookmark Data. For a general introduction to using bookmarks in macOS, read [Locating Files Using Bookmarks](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html#//apple_ref/doc/uid/TP40010672-CH3-SW10) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

When you copy a security-scoped URL (as obtained from a security-scoped bookmark), the copy has the security scope of the original. You gain access to the file-system resource (that the URL points to) just as you would with the original URL: by calling the [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) function (or its Cocoa equivalent).

If you need a security-scoped URL’s path as a string value (as provided by the [CFURLGetString](<cfurlgetstring(__).md>) function), such as to provide to an API that requires a string value, obtain the path from the URL as needed. Note, however, that a string-based path obtained from a security-scoped URL _does not_ have security scope and you cannot use that string to obtain access a security-scoped resource.

`CFURL` fails to create an object if the string passed is not well-formed (that is, if it does not comply with RFC 2396). Examples of cases that will not succeed are strings containing space characters and high-bit characters. If a function fails to create a `CFURL` object, it returns `NULL`, which you must be prepared to handle. If you create `CFURL` objects using file system paths, you should use the [CFURLCreateFromFileSystemRepresentation](<cfurlcreatefromfilesystemrepresentation(________).md>) and [CFURLCreateFromFileSystemRepresentationRelativeToBase](<cfurlcreatefromfilesystemrepresentationrelativetobase(__________).md>) functions, which handle the subtle differences between URL paths and file system paths.

For functions that read and write data from a URL, see [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFURL

- [CFURLCopyAbsoluteURL](<cfurlcopyabsoluteurl(__).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [CFURLCreateAbsoluteURLWithBytes](<cfurlcreateabsoluteurlwithbytes(____________).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [CFURLCreateByResolvingBookmarkData](<cfurlcreatebyresolvingbookmarkdata(______________).md>) — Returns a new URL made by resolving bookmark data.
- [CFURLCreateCopyAppendingPathComponent](<cfurlcreatecopyappendingpathcomponent(________).md>) — Creates a copy of a given URL and appends a path component.
- [CFURLCreateCopyAppendingPathExtension](<cfurlcreatecopyappendingpathextension(______).md>) — Creates a copy of a given URL and appends a path extension.
- [CFURLCreateCopyDeletingLastPathComponent](<cfurlcreatecopydeletinglastpathcomponent(____).md>) — Creates a copy of a given URL with the last path component deleted.
- [CFURLCreateCopyDeletingPathExtension](<cfurlcreatecopydeletingpathextension(____).md>) — Creates a copy of a given URL with its last path extension removed.
- [CFURLCreateFilePathURL](<cfurlcreatefilepathurl(______).md>) — Returns a new file path URL that refers to the same resource as a specified URL.
- [CFURLCreateFileReferenceURL](<cfurlcreatefilereferenceurl(______).md>) — Returns a new file reference URL that points to the same resource as a specified URL.
- [CFURLCreateFromFileSystemRepresentation](<cfurlcreatefromfilesystemrepresentation(________).md>) — Creates a new `CFURL` object for a file system entity using the native representation.
- [CFURLCreateFromFileSystemRepresentationRelativeToBase](<cfurlcreatefromfilesystemrepresentationrelativetobase(__________).md>) — Creates a `CFURL` object from a native character string path relative to a base URL.
- [CFURLCreateFromFSRef](<cfurlcreatefromfsref(____).md>) — Creates a URL from a given directory or file. _(deprecated)_
- [CFURLCreateWithBytes](<cfurlcreatewithbytes(__________).md>) — Creates a `CFURL` object using a given character bytes.
- [CFURLCreateWithFileSystemPath](<cfurlcreatewithfilesystempath(________).md>) — Creates a `CFURL` object using a local file system path string.
- [CFURLCreateWithFileSystemPathRelativeToBase](<cfurlcreatewithfilesystempathrelativetobase(__________).md>) — Creates a `CFURL` object using a local file system path string relative to a base URL.
- [CFURLCreateWithString](<cfurlcreatewithstring(______).md>) — Creates a `CFURL` object using a given `CFString` object.

### Accessing the Parts of a URL

- [CFURLCanBeDecomposed](<cfurlcanbedecomposed(__).md>) — Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.
- [CFURLCopyFileSystemPath](<cfurlcopyfilesystempath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyFragment](<cfurlcopyfragment(____).md>) — Returns the fragment from a given URL.
- [CFURLCopyHostName](<cfurlcopyhostname(__).md>) — Returns the host name of a given URL.
- [CFURLCopyLastPathComponent](<cfurlcopylastpathcomponent(__).md>) — Returns the last path component of a given URL.
- [CFURLCopyNetLocation](<cfurlcopynetlocation(__).md>) — Returns the net location portion of a given URL.
- [CFURLCopyParameterString](<cfurlcopyparameterstring(____).md>) — Returns the parameter string from a given URL. _(deprecated)_
- [CFURLCopyPassword](<cfurlcopypassword(__).md>) — Returns the password of a given URL.
- [CFURLCopyPath](<cfurlcopypath(__).md>) — Returns the path portion of a given URL.
- [CFURLCopyPathExtension](<cfurlcopypathextension(__).md>) — Returns the path extension of a given URL.
- [CFURLCopyQueryString](<cfurlcopyquerystring(____).md>) — Returns the query string of a given URL.
- [CFURLCopyResourceSpecifier](<cfurlcopyresourcespecifier(__).md>) — Returns any additional resource specifiers after the path.
- [CFURLCopyScheme](<cfurlcopyscheme(__).md>) — Returns the scheme portion of a given URL.
- [CFURLCopyStrictPath](<cfurlcopystrictpath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyUserName](<cfurlcopyusername(__).md>) — Returns the user name from a given URL.
- [CFURLGetPortNumber](<cfurlgetportnumber(__).md>) — Returns the port number from a given URL.
- [CFURLHasDirectoryPath](<cfurlhasdirectorypath(__).md>) — Determines if a given URL’s path represents a directory.

### Converting URLs to Other Representations

- [CFURLCreateData](<cfurlcreatedata(________).md>) — Creates a `CFData` object containing the content of a given URL.
- [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>) — Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding. _(deprecated)_
- [CFURLCreateStringByReplacingPercentEscapes](<cfurlcreatestringbyreplacingpercentescapes(______).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent.
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>) — Fills a buffer with the file system’s native string representation of a given URL’s path.
- [CFURLGetFSRef](<cfurlgetfsref(____).md>) — Converts a given URL to a file or directory object. _(deprecated)_
- [CFURLGetString](<cfurlgetstring(__).md>) — Returns the URL as a `CFString` object.

### Getting URL Properties

- [CFURLGetBaseURL](<cfurlgetbaseurl(__).md>) — Returns the base URL of a given URL if it exists.
- [CFURLGetBytes](<cfurlgetbytes(______).md>) — Returns by reference the byte representation of a URL object.
- [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) — Returns the range of the specified component in the bytes of a URL.
- [CFURLGetTypeID](<cfurlgettypeid().md>) — Returns the type identifier for the `CFURL` opaque type.
- [CFURLResourceIsReachable](<cfurlresourceisreachable(____).md>) — Returns whether the resource pointed to by a file URL can be reached.

### Getting and Setting File System Resource Properties

- [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) — Removes all cached resource values and temporary resource values from the URL object.
- [CFURLClearResourcePropertyCacheForKey](<cfurlclearresourcepropertycacheforkey(____).md>) — Removes the cached resource value identified by a given key from the URL object.
- [CFURLCopyResourcePropertiesForKeys](<cfurlcopyresourcepropertiesforkeys(______).md>) — Returns the resource values for the properties identified by specified array of keys.
- [CFURLCopyResourcePropertyForKey](<cfurlcopyresourcepropertyforkey(________).md>) — Returns the value of a given resource property of a given URL.
- [CFURLCreateResourcePropertiesForKeysFromBookmarkData](<cfurlcreateresourcepropertiesforkeysfrombookmarkdata(______).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [CFURLCreateResourcePropertyForKeyFromBookmarkData](<cfurlcreateresourcepropertyforkeyfrombookmarkdata(______).md>) — Returns the value of a resource property from specified bookmark data.
- [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) — Sets the URL’s resource property for a given key to a given value.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.

### Working with Bookmark Data

- [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) — Returns bookmark data for a URL, created with specified options and resource values.
- [CFURLCreateBookmarkDataFromAliasRecord](<cfurlcreatebookmarkdatafromaliasrecord(____).md>) — Initializes and returns bookmark data derived from an alias record. _(deprecated)_
- [CFURLCreateBookmarkDataFromFile](<cfurlcreatebookmarkdatafromfile(______).md>) — Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [CFURLWriteBookmarkDataToFile](<cfurlwritebookmarkdatatofile(________).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.

### Bookmark Data Types

- [CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions.md) — Type for bookmark data creation options.
- [CFURLBookmarkFileCreationOptions](cfurlbookmarkfilecreationoptions.md) — Type for bookmark file creation options.
- [CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions.md) — Type for bookmark data resolution options.

### Bookmark Data Constants

- [Bookmark Data Creation Options](bookmark-data-creation-options.md) — Options used when creating bookmark data.
- [Bookmark Data Resolution Options](bookmark-data-resolution-options.md) — Options used when resolving bookmark data.

### File System Constants

- [Common File System Resource Keys](common-file-system-resource-keys.md) — Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md) — Possible values for the [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md) — Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md) — These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md) — Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md) — Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.

### Miscellaneous

- [CFURLComponentType](cfurlcomponenttype.md) — The types of components in a URL.
- [CFURLPathStyle](cfurlpathstyle.md) — Options you can use to determine how CFURL functions parse a file system path name.

## See Also

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
