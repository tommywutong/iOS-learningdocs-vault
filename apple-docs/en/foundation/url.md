---
title: URL
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url
source_url: 'https://developer.apple.com/documentation/foundation/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url.json'
content_hash: 'sha256:2f0406f629dfa1cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URL

<sub>Structure</sub>

A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URL
```

## Overview

You can construct URLs and access their parts. For URLs that represent local files, you can also manipulate properties of those files directly, such as changing the file’s last modification date. Finally, you can pass URLs to other APIs to retrieve the contents of those URLs. For example, you can use [URLSession](urlsession.md) and its related classes to access the contents of remote resources.

URLs are the preferred way to refer to local files. Most objects that read data from or write data to a file have methods that accept a URL instead of a pathname as the file reference. For example, you can get the contents of a local file URL as [String](../swift/string.md) by calling [init(contentsOf:encoding:)](<../swift/string/init(contentsof_encoding_).md>), or as a [Data](data.md) by calling [init(contentsOf:options:)](<data/init(contentsof_options_).md>).

As a convenience, you can use Swift’s `async`-`await` syntax to asynchronously access the contents of a [URL](url.md) through the [resourceBytes](url/resourcebytes.md) and [lines](url/lines.md) properties. These properties use the shared [URLSession](urlsession.md) instance to load the resource.

`URL` defines a set of properties for common directories like [documentsDirectory](url/documentsdirectory.md) and [cachesDirectory](url/cachesdirectory.md), some of which have distinct behaviors for backup or automatic purging. To make the best use of these directories, see [Using the file system effectively](using-the-file-system-effectively.md).

## Relationships

- **Conforms To**: [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [CustomURLRepresentationParameterConvertible](../appintents/customurlrepresentationparameterconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Transferable](../coretransferable/transferable.md)

## Topics

### Creating a URL from a string

- [init(string:)](<url/init(string_).md>) — Creates a URL instance from the provided string.
- [init(string:encodingInvalidCharacters:)](<url/init(string_encodinginvalidcharacters_).md>) — Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init(string:relativeTo:)](<url/init(string_relativeto_).md>) — Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<url/init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-3ic6f.md>) — Creates a URL that refers to a location specified by resolving bookmark data.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<url/init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-97e6x.md>) — Initializes a URL that refers to a location specified by resolving bookmark data.

### Creating a file URL from a string path

- [init(filePath:directoryHint:relativeTo:)](<url/init(filepath_directoryhint_relativeto_).md>) — Creates a file URL that references a path you specify as a string.
- [DirectoryHint](url/directoryhint.md) — A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath:)](<url/init(fileurlwithpath_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:isDirectory:)](<url/init(fileurlwithpath_isdirectory_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:relativeTo:)](<url/init(fileurlwithpath_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithPath:isDirectory:relativeTo:)](<url/init(fileurlwithpath_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithFileSystemRepresentation:isDirectory:relativeTo:)](<url/init(fileurlwithfilesystemrepresentation_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName:)](<url/init(filereferenceliteralresourcename_).md>) — Creates a URL from a playground file literal.
- [init(filePath:directoryHint:)](<url/init(filepath_directoryhint_).md>) — Creates a file URL that references a file path.

### Creating a file URL from a file path

- [init(_:)](<url/init(__).md>) — Creates a file URL that references the local file or directory at the file path you specify. _(deprecated)_
- [init(_:isDirectory:)](<url/init(__isdirectory_).md>) — Creates a file URL that references the local file or directory at the file path you specify. _(deprecated)_
- [FilePath](../system/filepath.md) — Represents a location in the file system.

### Creating a file URL for a common directory

- [init(for:in:appropriateFor:create:)](<url/init(for_in_appropriatefor_create_).md>) — Creates a file URL for a common directory in a domain.
- [SearchPathDirectory](filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.

### Creating a URL by resolving a bookmark

- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<url/init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-3ic6f.md>) — Creates a URL that refers to a location specified by resolving bookmark data.
- [init(resolvingAliasFileAt:options:)](<url/init(resolvingaliasfileat_options_).md>) — Creates a URL that refers to the location specified by resolving an alias file.
- [BookmarkResolutionOptions](url/bookmarkresolutionoptions.md) — An alias for the bookmark resolution options type.
- [BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md) — Options used when resolving bookmark data.

### Creating a URL from a resource

- [init(resource:)](<url/init(resource_).md>) — Creates a URL from a resource.

### Creating a URL by parsing

- [init(_:strategy:)](<url/init(__strategy_).md>) — Creates a URL instance by parsing the provided input in accordance with a parse strategy.
- [ParseStrategy](url/parsestrategy.md) — A parse strategy for creating URLs from formatted strings.

### Accessing the parts of a URL

- [fragment(percentEncoded:)](<url/fragment(percentencoded_).md>) — Returns the fragment component of the URL, optionally removing any percent-encoding.
- [fragment](url/fragment.md) — The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [host(percentEncoded:)](<url/host(percentencoded_).md>) — Returns the host component of the URL, optionally removing any percent-encoding.
- [host](url/host.md) — The host component of a URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [lastPathComponent](url/lastpathcomponent.md) — The last path component of the URL, or an empty string if the path is an empty string.
- [path(percentEncoded:)](<url/path(percentencoded_).md>) — Returns the path component of the URL, optionally removing any percent-encoding.
- [path](url/path.md) — The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string. _(deprecated)_
- [password(percentEncoded:)](<url/password(percentencoded_).md>) — Returns the password component of the URL, optionally removing any percent-encoding.
- [password](url/password.md) — The password component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [pathComponents](url/pathcomponents.md) — The path components of the URL, or an empty array if the path is an empty string.
- [pathExtension](url/pathextension.md) — The path extension of the URL, or an empty string if the path is an empty string.
- [port](url/port.md) — The port component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [query(percentEncoded:)](<url/query(percentencoded_).md>) — Returns the query component of the URL, optionally removing any percent-encoding.
- [query](url/query.md) — The query of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [scheme](url/scheme.md) — The scheme of the URL.
- [user(percentEncoded:)](<url/user(percentencoded_).md>) — Returns the user component of the URL, optionally removing any percent-encoding.
- [user](url/user.md) — The user component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_

### Accessing URL representations

- [baseURL](url/baseurl.md) — The base URL.
- [absoluteString](url/absolutestring.md) — The absolute string for the URL.
- [absoluteURL](url/absoluteurl.md) — The absolute URL.
- [relativePath](url/relativepath.md) — The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [relativeString](url/relativestring.md) — The relative portion of a URL.
- [standardized](url/standardized.md) — A version of the URL with any instances of “..” or “.” resolved in its path.
- [standardizedFileURL](url/standardizedfileurl.md) — A standardized version of the path of a file URL.

### Accessing resource values

- [resourceValues(forKeys:)](<url/resourcevalues(forkeys_).md>) — Returns a collection of resource values identified by the given resource keys.
- [setResourceValues(_:)](<url/setresourcevalues(__).md>) — Sets the resource value identified by a given resource key.
- [removeCachedResourceValue(forKey:)](<url/removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given resource value key from the URL object.
- [removeAllCachedResourceValues()](<url/removeallcachedresourcevalues().md>) — Removes all cached resource values and all temporary resource values from the URL object.
- [setTemporaryResourceValue(_:forKey:)](<url/settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](urlresourcekey.md) — Keys that apply to file system URLs.
- [URLResourceValues](urlresourcevalues.md) — The properties that the file system resources support.

### Working with the data representation of a URL

- [init(dataRepresentation:relativeTo:isAbsolute:)](<url/init(datarepresentation_relativeto_isabsolute_).md>) — Initializes a newly created URL using the contents of the given data, relative to a base URL.
- [dataRepresentation](url/datarepresentation.md) — The data representation of the URL’s relativeString.

### Working with file URLs

- [isFileURL](url/isfileurl.md) — A Boolean that is true if the scheme is `file:`.
- [hasDirectoryPath](url/hasdirectorypath.md) — A Boolean that is true if the URL path represents a directory.
- [withUnsafeFileSystemRepresentation(_:)](<url/withunsafefilesystemrepresentation(__).md>) — Passes the URL’s path in the file system representation to a closure.
- [resolveSymlinksInPath()](<url/resolvesymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [resolvingSymlinksInPath()](<url/resolvingsymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [standardize()](<url/standardize().md>) — Standardizes the path of a file URL.

### Accessing common directories

- [applicationDirectory](url/applicationdirectory.md) — The standard directory for apps.
- [applicationSupportDirectory](url/applicationsupportdirectory.md) — The standard directory for application support files.
- [cachesDirectory](url/cachesdirectory.md) — The standard directory for discardable cache files.
- [desktopDirectory](url/desktopdirectory.md) — The standard directory for files on the desktop.
- [documentsDirectory](url/documentsdirectory.md) — The standard directory for document files.
- [downloadsDirectory](url/downloadsdirectory.md) — The standard directory for download files.
- [libraryDirectory](url/librarydirectory.md) — The standard directory for documentation, support, and configuration files.
- [moviesDirectory](url/moviesdirectory.md) — The standard directory for movie files.
- [musicDirectory](url/musicdirectory.md) — The standard directory for music files.
- [picturesDirectory](url/picturesdirectory.md) — The standard directory for image files.
- [sharedPublicDirectory](url/sharedpublicdirectory.md) — The standard directory for publicly shared files.
- [temporaryDirectory](url/temporarydirectory.md) — The standard directory for temporary files.
- [trashDirectory](url/trashdirectory.md) — The standard trash directory.
- [userDirectory](url/userdirectory.md) — The container directory of user home directories.

### Accessing home and user directories

- [currentDirectory()](<url/currentdirectory().md>) — Returns the working directory of the current process.
- [homeDirectory](url/homedirectory.md) — The home directory for the current user.
- [homeDirectory(forUser:)](<url/homedirectory(foruser_).md>) — Returns the home directory for the specified user.

### Adding path components

- [append(path:directoryHint:)](<url/append(path_directoryhint_).md>) — Appends a path to the URL, with a hint for handling directory awareness.
- [append(component:directoryHint:)](<url/append(component_directoryhint_).md>) — Appends a path component to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:)](<url/appendpathcomponent(__).md>) — Appends a path component to the URL. _(deprecated)_
- [appendPathComponent(_:isDirectory:)](<url/appendpathcomponent(__isdirectory_).md>) — Appends a path component to the URL, specifying whether the resulting path is a directory. _(deprecated)_
- [appending(path:directoryHint:)](<url/appending(path_directoryhint_).md>) — Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [appending(component:directoryHint:)](<url/appending(component_directoryhint_).md>) — Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [appendingPathComponent(_:)](<url/appendingpathcomponent(__).md>) — Returns a URL by appending the specified path component to self. _(deprecated)_
- [appendingPathComponent(_:isDirectory:)](<url/appendingpathcomponent(__isdirectory_).md>) — Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory. _(deprecated)_
- [append(components:directoryHint:)](<url/append(components_directoryhint_).md>) — Appends multiple path components to the URL, with a hint for handling directory awareness.
- [appending(components:directoryHint:)](<url/appending(components_directoryhint_).md>) — Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:conformingTo:)](<url/appendpathcomponent(__conformingto_).md>) — Appends a path component to the URL that conforms to a uniform type identifier.
- [appendingPathComponent(_:conformingTo:)](<url/appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component that conforms to a uniform type identifier.

### Adding a path extension

- [appendPathExtension(_:)](<url/appendpathextension(__).md>) — Appends the specified path extension to self.
- [appendingPathExtension(_:)](<url/appendingpathextension(__).md>) — Returns a URL by appending the specified path extension to self.
- [appendPathExtension(for:)](<url/appendpathextension(for_).md>) — Appends the preferred path extension for the type you specify.
- [appendingPathExtension(for:)](<url/appendingpathextension(for_).md>) — Returns a URL by appending the preferred path extension for the type you specify to the URL’s last path component.

### Adding query items

- [append(queryItems:)](<url/append(queryitems_).md>) — Appends a list of query items to the URL.
- [appending(queryItems:)](<url/appending(queryitems_).md>) — Returns a new URL formed by appending a list of query items to the URL.
- [URLQueryItem](urlqueryitem.md) — A single name-value pair from the query portion of a URL.

### Removing path components

- [deleteLastPathComponent()](<url/deletelastpathcomponent().md>) — Returns a URL constructed by removing the last path component of self.
- [deletingLastPathComponent()](<url/deletinglastpathcomponent().md>) — Returns a URL constructed by removing the last path component of self.

### Removing a path extension

- [deletePathExtension()](<url/deletepathextension().md>) — Returns a URL constructed by removing any path extension.
- [deletingPathExtension()](<url/deletingpathextension().md>) — Returns a URL constructed by removing any path extension.

### Creating bookmarks

- [bookmarkData(options:includingResourceValuesForKeys:relativeTo:)](<url/bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns bookmark data for the URL, created with specified options and resource values.
- [bookmarkData(withContentsOf:)](<url/bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [writeBookmarkData(_:to:)](<url/writebookmarkdata(__to_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [resourceValues(forKeys:fromBookmarkData:)](<url/resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [BookmarkCreationOptions](url/bookmarkcreationoptions.md) — An alias for bookmark creation options.
- [BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md) — Options used when creating bookmark data.

### Checking reachability

- [checkResourceIsReachable()](<url/checkresourceisreachable().md>) — Returns whether the URL’s resource exists and is reachable.

### Loading URL contents asynchronously

- [resourceBytes](url/resourcebytes.md) — The URL’s resource data, as an asynchronous sequence of bytes.
- [lines](url/lines.md) — The URL’s resource data, as an asynchronous sequence of lines of text.
- [AsyncBytes](url/asyncbytes.md) — An asynchronous sequence of bytes loaded from the URL.

### Working with promised items

- [checkPromisedItemIsReachable()](<url/checkpromiseditemisreachable().md>) — Returns whether the promised item URL’s resource exists and is reachable.
- [promisedItemResourceValues(forKeys:)](<url/promiseditemresourcevalues(forkeys_).md>) — Gets resource values from URLs of ‘promised’ items.

### Working with security scoped resources

- [startAccessingSecurityScopedResource()](<url/startaccessingsecurityscopedresource().md>) — Given a url created by resolving a bookmark data created with security scope, make the resource referenced by the url accessible to the process.
- [stopAccessingSecurityScopedResource()](<url/stopaccessingsecurityscopedresource().md>) — Revokes the access granted to the url by a prior successful call to the complementary start function.

### Describing a URL

- [customPlaygroundQuickLook](url/customplaygroundquicklook.md) — A playground quicklook for the URL. _(deprecated)_

### Formatting a URL

- [formatted()](<url/formatted().md>) — Formats the URL using a default format style.
- [formatted(_:)](<url/formatted(__).md>) — Formats the URL, using the provided format style.
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.

### Using reference types

- [NSURL](nsurl.md) — An object that represents the location of a resource, such as an item on a remote server or the path to a local file.

### App Intents support

- [defaultResolverSpecification](url/defaultresolverspecification.md) — The default resolver specification that the App Intents framework uses.
- [Specification](url/specification.md) — The specification type for conforming with App Intents.
- [UnwrappedType](url/unwrappedtype.md) — The core type for conforming with App Intents.
- [ValueType](url/valuetype.md) — The value type for conforming with App Intents.

### Structures

- [Template](url/template.md) — A template for constructing a URL from variable expansions.

### Initializers

- [init(template:variables:)](<url/init(template_variables_).md>) — Creates a new `URL` by expanding the RFC 6570 template and variables.

## See Also

### URLs

- [URLComponents](urlcomponents.md) — A structure that parses URLs into and constructs URLs from their constituent parts.
- [URLQueryItem](urlqueryitem.md) — A single name-value pair from the query portion of a URL.
