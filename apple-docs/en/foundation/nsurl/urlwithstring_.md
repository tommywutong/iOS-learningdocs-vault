---
title: 'URLWithString:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/urlwithstring:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/urlwithstring:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/urlwithstring%3A.json'
content_hash: 'sha256:55a67149c5c43d4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# URLWithString:

<sub>Type Method</sub>

Creates and returns an NSURL object initialized with a provided URL string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) URLWithString:(NSString *) URLString;
```

## Parameters

- `URLString` — The URL string with which to initialize the NSURL object. Linked on or after iOS 17, this method parses `URLString` according to RFC 3986. Linked before iOS 17, this method parses `URLString` according to RFCs 1738 and 1808.

## Return Value

An NSURL object initialized with `URLString`. If the URL string was malformed or `nil`, returns `nil`.

## Discussion

> [!important] Important
> For apps linked on or after iOS 17 and aligned OS versions, [NSURL](../nsurl.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) parsing as [NSURLComponents](../nsurlcomponents.md). This unifies the parsing behaviors of the `NSURL` and `NSURLComponents` APIs. Now, `NSURL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

To check if `URLString` is strictly valid according to the RFC, use the new `[NSURL URLWithString:URLString encodingInvalidCharacters:NO]` method. This method leaves all characters as they are and returns `nil` if `URLString` is explicitly invalid.

For apps linked before iOS 17, this method expects `URLString` to contain only characters that are allowed in a properly formed URL. All other characters must be properly percent encoded. Any percent-encoded characters are interpreted using UTF-8 encoding.

> [!important] Important
> To create NSURL objects for file system paths, use [+ fileURLWithPath:isDirectory:](<fileurl(withpath_isdirectory_).md>) instead.

## See Also

### Creating a URL object

- [- initWithString:](<init(string_).md>) — Initializes an NSURL object with a provided URL string.
- [URLWithString:encodingInvalidCharacters:](urlwithstring_encodinginvalidcharacters_.md) — Creates and returns an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [URLWithString:relativeToURL:](urlwithstring_relativetourl_.md) — Creates and returns an NSURL object initialized with a base URL and a relative string.
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
