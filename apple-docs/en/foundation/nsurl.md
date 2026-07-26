---
title: NSURL
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl
source_url: 'https://developer.apple.com/documentation/foundation/nsurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl.json'
content_hash: 'sha256:596c97f66d90690e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURL

<sub>Class</sub>

An object that represents the location of a resource, such as an item on a remote server or the path to a local file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSURL
```

## Overview

In Swift, this object bridges to [URL](url.md); use [NSURL](nsurl.md) when you need reference semantics or other Foundation-specific behavior.

You can use URL objects to construct URLs and access their parts. For URLs that represent local files, you can also manipulate properties of those files directly, such as changing the file’s last modification date. Finally, you can pass URL objects to other APIs to retrieve the contents of those URLs. For example, you can use the [URLSession](urlsession.md), [NSURLConnection](nsurlconnection.md), and [NSURLDownload](nsurldownload.md) classes to access the contents of remote resources, as described in [URL Loading System](url-loading-system.md).

URL objects are the preferred way to refer to local files. Most objects that read data from or write data to a file have methods that accept an [NSURL](nsurl.md) object instead of a pathname as the file reference. For example, you can get the contents of a local file URL as an `NSString` object using the `NSString/init(contentsOfURL:encoding:)-715fw` initializer, or as an `NSData` object using the `NSData/init(contentsOfURL:options:)-5abi3` initializer.

You can also use URLs for interapplication communication. In macOS, the [NSWorkspace](../appkit/nsworkspace.md) class provides the [open(_:)](<../appkit/nsworkspace/open(__).md>) method to open a location specified by a URL. Similarly, in iOS, the [UIApplication](../uikit/uiapplication.md) class provides the [open(_:options:completionHandler:)](<../uikit/uiapplication/open(__options_completionhandler_).md>) method.

Additionally, you can use URLs when working with pasteboards, as described in NSURL Additions Reference (part of the AppKit framework).

The [NSURL](nsurl.md) class is “toll-free bridged” with its Core Foundation counterpart, [CFURL](../corefoundation/cfurl.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [URL](url.md) structure, which bridges to the [NSURL](nsurl.md) class. For more information about value types, see [Classes and Structures](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/ClassesAndStructures.html#//apple_ref/doc/uid/TP40014097-CH13) in [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097) and [Working with Cocoa Frameworks](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [Using Swift with Cocoa and Objective-C (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

### Structure of a URL

An [NSURL](nsurl.md) object is composed of two parts—a potentially `nil` base URL and a string that is resolved relative to the base URL. An [NSURL](nsurl.md) object is considered absolute if its string part is fully resolved without a base; all other URLs are considered relative.

For example, when constructing an `NSURL` object, you might specify `file:///path/to/user/` as the base URL and `folder/file.html` as the string part, as follows:

```objc
NSURL *baseURL = [NSURL fileURLWithPath:@"file:///path/to/user/"];
NSURL *URL = [NSURL URLWithString:@"folder/file.html" relativeToURL:baseURL];
NSLog(@"absoluteURL = %@", [URL absoluteURL]);
```

When fully resolved, the absolute URL is `file:///path/to/user/folder/file.html`.

A URL can be also be divided into pieces based on its structure. For example, the URL `https://johnny:p4ssw0rd@www.example.com:443/script.ext;param=value?query=value#ref` contains the following URL components:

| Component | Value |
|---|---|
| [scheme](nsurl/scheme.md) | `https` |
| [user](nsurl/user.md) | `johnny` |
| [password](nsurl/password.md) | `p4ssw0rd` |
| [host](nsurl/host.md) | `www.example.com` |
| [port](nsurl/port.md) | `443` |
| [path](nsurl/path.md) | `/script.ext` |
| [pathExtension](nsurl/pathextension.md) | `ext` |
| [pathComponents](nsurl/pathcomponents.md) | `["/", "script.ext"]` |
| [parameterString](nsurl/parameterstring.md) | `param=value` |
| [query](nsurl/query.md) | `query=value` |
| [fragment](nsurl/fragment.md) | `ref` |

The [NSURL](nsurl.md) class provides properties that let you examine each of these components.

> [!important] Important
> For apps linked on or after iOS 17 and aligned OS versions, [NSURL](nsurl.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) parsing as [NSURLComponents](nsurlcomponents.md). This unifies the parsing behaviors of the `NSURL` and `NSURLComponents` APIs. Now, `NSURL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.
>
> To check if a `URLString` is strictly valid according to the RFC, use the new `[NSURL URLWithString:URLString encodingInvalidCharacters:NO]` method. This method leaves all characters as they are and returns `nil` if `URLString` is explicitly invalid.

For apps linked before iOS 17, the [NSURL](nsurl.md) class parses URLs according to [RFC 1808](https://tools.ietf.org/html/rfc1808), [RFC 1738](https://tools.ietf.org/html/rfc1738), and [RFC 2732](https://tools.ietf.org/html/rfc2732).

### Bookmarks and Security Scope

Starting with OS X v10.6 and iOS 4.0, the [NSURL](nsurl.md) class provides a facility for creating and using bookmark objects. A **bookmark** provides a persistent reference to a file-system resource. When you resolve a bookmark, you obtain a URL to the resource’s current location. A bookmark’s association with a file-system resource (typically a file or folder) usually continues to work if the user moves or renames the resource, or if the user relaunches your app or restarts the system.

For a general introduction to using bookmarks, read [Locating Files Using Bookmarks](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html#//apple_ref/doc/uid/TP40010672-CH3-SW10) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

In a macOS app that adopts App Sandbox, you can use **security-scoped bookmarks** to gain access to file-system resources outside your app’s sandbox. These bookmarks preserve the user’s intent to give your app access to a resource across app launches. For details on how this works, including information on the entitlements you need in your Xcode project, read [Security-Scoped Bookmarks and Persistent Resource Access](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183). The methods for using security-scoped bookmarks are described in this document in Working with Bookmark Data.

When you resolve a security-scoped bookmark, you get a security-scoped URL.

### Security-Scoped URLs

Security-scoped URLs provide access to resources outside an app’s sandbox. In macOS, you get access to security-scoped URLs when you resolve a security-scoped bookmark. In iOS, apps that _open_ or _move_ documents using a [UIDocumentPickerViewController](../uikit/uidocumentpickerviewcontroller.md) also receive security-scoped URLs.

To gain access to a security-scoped URL, you must call the [- startAccessingSecurityScopedResource](<nsurl/startaccessingsecurityscopedresource().md>) method (or its Core Foundation equivalent, the [CFURLStartAccessingSecurityScopedResource(_:)](<../corefoundation/cfurlstartaccessingsecurityscopedresource(__).md>) function). For iOS apps, if you use a [UIDocument](../uikit/uidocument.md) to access the URL, it automatically manages the security-scoped URL for you.

If `startAccessingSecurityScopedResource` (or `CFUrLStartAccessingSecurityScopedResource`) returns [true](../swift/true.md), you must relinquish your access by calling the [- stopAccessingSecurityScopedResource](<nsurl/stopaccessingsecurityscopedresource().md>) method (or its Core Foundation equivalent, the [CFURLStopAccessingSecurityScopedResource(_:)](<../corefoundation/cfurlstopaccessingsecurityscopedresource(__).md>) function). You should relinquish your access as soon as you have finished using the file. After you call these methods, you immediately lose access to the resource in question.

> [!warning] Warning
> If you fail to relinquish your access when you no longer need a file-system resource, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, using Powerbox, security-scoped bookmarks, or similar APIs, until relaunched.

#### Security-Scoped URLs and String Paths

In a macOS app, when you copy a security-scoped URL, the copy has the security scope of the original. You gain access to the file-system resource (that the URL points to) just as you would with the original URL: by calling the [- startAccessingSecurityScopedResource](<nsurl/startaccessingsecurityscopedresource().md>) method (or its Core Foundation equivalent).

If you need a security-scoped URL’s path as a string value (as provided by the [path](nsurl/path.md) method), such as to provide to an API that requires a string value, obtain the path from the URL as needed. Note, however, that a string-based path obtained from a security-scoped URL _does not_ have security scope and you cannot use that string to obtain access to a security-scoped resource.

### iCloud Document Thumbnails

With OS X v10.10 and iOS 8.0, the NSURL class includes the ability to get and set document thumbnails as a resource property for iCloud documents. You can get a dictionary of [NSImage](../appkit/nsimage.md) objects in macOS or [UIImage](../uikit/uiimage.md) objects in iOS using the [- getResourceValue:forKey:error:](<nsurl/getresourcevalue(__forkey_).md>) or [- getPromisedItemResourceValue:forKey:error:](<nsurl/getpromiseditemresourcevalue(__forkey_).md>) methods.

**Swift**

```swift
let URL = self.URLForDocument()
var thumbnails: AnyObject?
 
do {
    try URL.getResourceValue(&thumbnails, forKey: NSURLThumbnailDictionaryKey)
    if let thumbnails = thumbnails as? [NSString: NSImage] {
        let image = thumbnails[NSThumbnail1024x1024SizeKey]
    }
} catch {
    // handle the error
}
```

**Objective-C**

```objc
NSURL *URL = [self URLForDocument];
NSDictionary *thumbnails = nil;
NSError *error = nil;
 
BOOL success = [URL getPromisedItemResourceValue:&thumbnails
                                          forKey:NSURLThumbnailDictionaryKey
                                           error:&error];
if (success) {
  NSImage *image = thumbnails[NSThumbnail1024x1024SizeKey];
} else {
  // handle the error
}
```

In macOS, you can set a dictionary of thumbnails using the [- setResourceValue:forKey:error:](<nsurl/setresourcevalue(__forkey_).md>) method. You can also get or set all the thumbnails as an `NSImage` object with multiple representations by using the [NSURLThumbnailKey](urlresourcekey/thumbnailkey.md).

**Swift**

```swift
let URL = self.URLForDocument()
let thumbnail = self.createDocumentThumbnail()
 
do {
    try URL.setResourceValue([NSThumbnail1024x1024SizeKey: thumbnail], forKey: NSURLThumbnailDictionaryKey)
} catch {
    // handle the error
}
```

**Objective-C**

```objc
NSURL *URL = [self URLForDocument];
NSImage *thumbnail = [self createDocumentThumbnail];
NSError *error = nil;
 
BOOL success = [URL setResourceValue:@{NSThumbnail1024x1024SizeKey : thumbnail}
                              forKey:NSURLThumbnailDictionaryKey
                               error:&error];
 
if (!success) {
  // handle the error
}
```

> [!note] Note
> Do not set the [NSURLThumbnailDictionaryKey](urlresourcekey/thumbnaildictionarykey.md) key directly. Modifying this key interferes with document tracking and can create duplicates of your document, as well as other possible problems.
>
> In iOS, use a [UIDocument](../uikit/uidocument.md) subclass to manage your file. Set the thumbnail by overriding the document’s [fileAttributesToWrite(to:for:)](<../uikit/uidocument/fileattributestowrite(to_for_).md>) method and returning a dictionary that contains the proper thumbnail keys (along with any other file attributes).
>
> In macOS, follow the instructions for creating thumbnails given in [Quick Look Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005020).

> [!note] Note
> Although the thumbnail API is designed to support multiple image resolutions, currently it only supports 1024 x 1024 pixel thumbnails.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSItemProviderReading](nsitemproviderreading.md), [NSItemProviderWriting](nsitemproviderwriting.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSPasteboardReading](../appkit/nspasteboardreading.md), [NSPasteboardWriting](../appkit/nspasteboardwriting.md), [NSSecureCoding](nssecurecoding.md), [QLPreviewItem](../quicklookui/qlpreviewitem.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a URL object

- [- initWithString:](<nsurl/init(string_).md>) — Initializes an NSURL object with a provided URL string.
- [- initWithString:encodingInvalidCharacters:](<nsurl/init(string_encodinginvalidcharacters_).md>) — Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithString:relativeToURL:](<nsurl/init(string_relativeto_).md>) — Initializes an NSURL object with a base URL and a relative string.
- [+ fileURLWithPath:isDirectory:](<nsurl/fileurl(withpath_isdirectory_).md>) — Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [- initFileURLWithPath:isDirectory:](<nsurl/init(fileurlwithpath_isdirectory_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPath:relativeToURL:](<nsurl/fileurl(withpath_relativeto_).md>) — Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [- initFileURLWithPath:relativeToURL:](<nsurl/init(fileurlwithpath_relativeto_).md>) — Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [+ fileURLWithPath:isDirectory:relativeToURL:](<nsurl/fileurl(withpath_isdirectory_relativeto_).md>) — Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [- initFileURLWithPath:isDirectory:relativeToURL:](<nsurl/init(fileurlwithpath_isdirectory_relativeto_).md>) — Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [+ fileURLWithPath:](<nsurl/fileurl(withpath_).md>) — Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [- initFileURLWithPath:](<nsurl/init(fileurlwithpath_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPathComponents:](<nsurl/fileurl(withpathcomponents_).md>) — Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [+ URLByResolvingAliasFileAtURL:options:error:](<nsurl/init(resolvingaliasfileat_options_).md>) — Returns a new URL made by resolving the alias file at `url`.
- [- initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](<nsurl/init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_).md>) — Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [+ fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:](<nsurl/fileurl(withfilesystemrepresentation_isdirectory_relativeto_).md>) — Returns a new URL object initialized with a C string representing a local file system path.
- [- getFileSystemRepresentation:maxLength:](<nsurl/getfilesystemrepresentation(__maxlength_).md>) — Fills the provided buffer with a C string representing a local file system path.
- [- initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:](<nsurl/init(fileurlwithfilesystemrepresentation_isdirectory_relativeto_).md>) — Initializes a URL object with a C string representing a local file system path.
- [+ absoluteURLWithDataRepresentation:relativeToURL:](<nsurl/absoluteurl(withdatarepresentation_relativeto_).md>) — Initializes and returns a newly created absolute NSURL using the contents of the given data, relative to a base URL.
- [- initAbsoluteURLWithDataRepresentation:relativeToURL:](<nsurl/init(absoluteurlwithdatarepresentation_relativeto_).md>) — Initializes a newly created absolute NSURL using the contents of the given data, relative to a base URL.
- [- initWithDataRepresentation:relativeToURL:](<nsurl/init(datarepresentation_relativeto_).md>) — Initializes a newly created NSURL using the contents of the given data, relative to a base URL.
- [dataRepresentation](nsurl/datarepresentation.md) — The data representation of the URL’s relativeString.

### Querying an NSURL

- [- checkResourceIsReachableAndReturnError:](<nsurl/checkresourceisreachableandreturnerror(__).md>) — Returns whether the resource pointed to by a file URL can be reached.
- [- isFileReferenceURL](<nsurl/isfilereferenceurl().md>) — Returns whether the URL is a file reference URL.
- [fileURL](nsurl/isfileurl.md) — A boolean value that determines whether the receiver is a file URL.

### Accessing the Parts of the URL

- [absoluteString](nsurl/absolutestring.md) — The URL string for the receiver as an absolute URL. (read-only)
- [absoluteURL](nsurl/absoluteurl.md) — An absolute URL that refers to the same resource as the receiver. (read-only)
- [baseURL](nsurl/baseurl.md) — The base URL. (read-only)
- [fileSystemRepresentation](nsurl/filesystemrepresentation.md) — A C string containing the URL’s file system path. (read-only)
- [fragment](nsurl/fragment.md) — The fragment identifier, conforming to RFC 1808. (read-only)
- [host](nsurl/host.md) — The host, conforming to RFC 1808. (read-only)
- [lastPathComponent](nsurl/lastpathcomponent.md) — The last path component. (read-only)
- [parameterString](nsurl/parameterstring.md) — The parameter string conforming to RFC 1808. (read-only) _(deprecated)_
- [password](nsurl/password.md) — The password conforming to RFC 1808. (read-only)
- [path](nsurl/path.md) — The path, conforming to RFC 1808. (read-only)
- [pathComponents](nsurl/pathcomponents.md) — An array containing the  path components. (read-only)
- [pathExtension](nsurl/pathextension.md) — The path extension. (read-only)
- [port](nsurl/port.md) — The port, conforming to RFC 1808.
- [query](nsurl/query.md) — The query string, conforming to RFC 1808.
- [relativePath](nsurl/relativepath.md) — The relative path, conforming to RFC 1808. (read-only)
- [relativeString](nsurl/relativestring.md) — A string representation of the relative portion of the URL. (read-only)
- [resourceSpecifier](nsurl/resourcespecifier.md) — The resource specifier. (read-only)
- [scheme](nsurl/scheme.md) — The scheme. (read-only)
- [standardizedURL](nsurl/standardized.md) — A copy of the URL with any instances of `".."` or `"."` removed from its path. (read-only)
- [user](nsurl/user.md) — The user name, conforming to RFC 1808.

### Accessing Resource Values

- [- resourceValuesForKeys:error:](<nsurl/resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.
- [- getResourceValue:forKey:error:](<nsurl/getresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- setResourceValue:forKey:error:](<nsurl/setresourcevalue(__forkey_).md>) — Sets the URL’s resource property for a given key to a given value.
- [- setResourceValues:error:](<nsurl/setresourcevalues(__).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [- removeAllCachedResourceValues](<nsurl/removeallcachedresourcevalues().md>) — Removes all cached resource values and temporary resource values from the URL object.
- [- removeCachedResourceValueForKey:](<nsurl/removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given key from the URL object.
- [- setTemporaryResourceValue:forKey:](<nsurl/settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](urlresourcekey.md) — Keys that apply to file system URLs.

### Modifying and Converting a File URL

- [filePathURL](nsurl/filepathurl.md) — A file path URL that points to the same resource as the URL object. (read-only)
- [- fileReferenceURL](<nsurl/filereferenceurl().md>) — Returns a new file reference URL that points to the same resource as the receiver.
- [- URLByAppendingPathComponent:](<nsurl/appendingpathcomponent(__).md>) — Returns a new URL by appending a path component to the original URL.
- [- URLByAppendingPathComponent:isDirectory:](<nsurl/appendingpathcomponent(__isdirectory_).md>) — Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [- URLByAppendingPathComponent:conformingToType:](<nsurl/appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [- URLByAppendingPathExtension:](<nsurl/appendingpathextension(__).md>) — Returns a new URL by appending a path extension to the original URL.
- [- URLByAppendingPathExtensionForType:](<nsurl/appendingpathextension(for_).md>) — Returns a URL by appending the path extension for a uniform type identifier.
- [URLByDeletingLastPathComponent](nsurl/deletinglastpathcomponent.md) — A URL you create by removing the last path component from the receiver. (read-only)
- [URLByDeletingPathExtension](nsurl/deletingpathextension.md) — A URL you create by removing the path extension from the receiver, if any. (read-only)
- [URLByResolvingSymlinksInPath](nsurl/resolvingsymlinksinpath.md) — A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [URLByStandardizingPath](nsurl/standardizingpath.md) — A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [hasDirectoryPath](nsurl/hasdirectorypath.md) — A Boolean value that indicates whether the URL string’s path represents a directory.

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<nsurl/bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<nsurl/bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<nsurl/resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<nsurl/writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<nsurl/startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<nsurl/stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkFileCreationOptions](nsurl/bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md) — Options used when creating bookmark data.
- [BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md) — Options used when resolving bookmark data.

### Working with Promised Items

- [- checkPromisedItemIsReachableAndReturnError:](<nsurl/checkpromiseditemisreachableandreturnerror(__).md>) — Returns whether the promised item can be reached.
- [- getPromisedItemResourceValue:forKey:error:](<nsurl/getpromiseditemresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- promisedItemResourceValuesForKeys:error:](<nsurl/promiseditemresourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.

### Working with Pasteboards

- [+ URLFromPasteboard:](<nsurl/init(frompasteboard_).md>) — Reads an NSURL object off of the specified pasteboard.
- [- writeToPasteboard:](<nsurl/write(to_).md>) — Writes the URL to the specified pasteboard.

### Using Quick Looks

- [customPlaygroundQuickLook](nsurl/customplaygroundquicklook.md) — A custom playground Quick Look for this instance. _(deprecated)_

### Constants

- [NSURL Schemes](nsurl-schemes.md) — The schemes that the `NSURL` class is able to parse.
- [NSError userInfo Dictionary Keys](nserror-userinfo-dictionary-keys.md) — Keys in the userInfo dictionary of an `NSError` object when certain NSURL methods return an error.

### Deprecated

- [- initWithScheme:host:path:](<nsurl/init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_

### Initializers

- [init(absoluteURLWithDataRepresentation:relativeToURL:)](<nsurl/init(absoluteurlwithdatarepresentation_relativetourl_).md>)
- [init(byResolvingAliasFileAtURL:options:)](<nsurl/init(byresolvingaliasfileaturl_options_).md>)
- [init(byResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:)](<nsurl/init(byresolvingbookmarkdata_options_relativetourl_bookmarkdataisstale_).md>)
- [init(coder:)](<nsurl/init(coder_).md>)
- [init(dataRepresentation:relativeToURL:)](<nsurl/init(datarepresentation_relativetourl_)-8fa9z.md>)
- [init(dataRepresentation:relativeToURL:)](<nsurl/init(datarepresentation_relativetourl_)-8jv1p.md>)
- [init(fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:)](<nsurl/init(fileurlwithfilesystemrepresentation_isdirectory_relativetourl_).md>)
- [init(fileURLWithPath:isDirectory:relativeToURL:)](<nsurl/init(fileurlwithpath_isdirectory_relativetourl_).md>)
- [init(fileURLWithPath:relativeToURL:)](<nsurl/init(fileurlwithpath_relativetourl_).md>)
- [init(pasteboardPropertyList:ofType:)](<nsurl/init(pasteboardpropertylist_oftype_).md>)
- [init(string:relativeToURL:)](<nsurl/init(string_relativetourl_)-48a3i.md>)
- [init(string:relativeToURL:)](<nsurl/init(string_relativetourl_)-6beup.md>)
