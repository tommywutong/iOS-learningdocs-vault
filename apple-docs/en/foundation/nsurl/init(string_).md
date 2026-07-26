---
title: 'init(string:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/init(string:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/init(string:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/init%28string%3A%29.json'
content_hash: 'sha256:6d1236d11287bd3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# init(string:)

<sub>Initializer</sub>

Initializes an NSURL object with a provided URL string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(string URLString: String)
```

## Parameters

- `URLString` — The URL string with which to initialize the NSURL object. Linked on or after iOS 17, this method parses `URLString` according to RFC 3986. Linked before iOS 17, this method parses `URLString` according to RFCs 1738 and 1808.

## Return Value

An NSURL object initialized with `URLString`. If the URL string was malformed, returns `nil`.

## Discussion

> [!important] Important
> For apps linked on or after iOS 17 and aligned OS versions, [NSURL](../nsurl.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) parsing as [NSURLComponents](../nsurlcomponents.md). This unifies the parsing behaviors of the `NSURL` and `NSURLComponents` APIs. Now, `NSURL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

To check if `URLString` is strictly valid according to the RFC, use the new `[NSURL URLWithString:URLString encodingInvalidCharacters:NO]` method. This method leaves all characters as they are and returns `nil` if `URLString` is explicitly invalid.

For apps linked before iOS 17, this method expects `URLString` to contain only characters that are allowed in a properly formed URL. All other characters must be properly percent encoded. Any percent-encoded characters are interpreted using UTF-8 encoding.

## See Also

### Creating a URL object

- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithString:relativeToURL:](<init(string_relativeto_).md>) — Initializes an NSURL object with a base URL and a relative string.
- [+ fileURLWithPath:isDirectory:](<fileurl(withpath_isdirectory_).md>) — Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [- initFileURLWithPath:isDirectory:](<init(fileurlwithpath_isdirectory_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPath:relativeToURL:](<fileurl(withpath_relativeto_).md>) — Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [- initFileURLWithPath:relativeToURL:](<init(fileurlwithpath_relativeto_).md>) — Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [+ fileURLWithPath:isDirectory:relativeToURL:](<fileurl(withpath_isdirectory_relativeto_).md>) — Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [- initFileURLWithPath:isDirectory:relativeToURL:](<init(fileurlwithpath_isdirectory_relativeto_).md>) — Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [+ fileURLWithPath:](<fileurl(withpath_).md>) — Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [- initFileURLWithPath:](<init(fileurlwithpath_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPathComponents:](<fileurl(withpathcomponents_).md>) — Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [+ URLByResolvingAliasFileAtURL:options:error:](<init(resolvingaliasfileat_options_).md>) — Returns a new URL made by resolving the alias file at `url`.
- [- initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_).md>) — Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [+ fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:](<fileurl(withfilesystemrepresentation_isdirectory_relativeto_).md>) — Returns a new URL object initialized with a C string representing a local file system path.
- [- getFileSystemRepresentation:maxLength:](<getfilesystemrepresentation(__maxlength_).md>) — Fills the provided buffer with a C string representing a local file system path.
