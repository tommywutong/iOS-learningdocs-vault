---
title: 'URLWithDataRepresentation:relativeToURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/urlwithdatarepresentation:relativetourl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/urlwithdatarepresentation:relativetourl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/urlwithdatarepresentation%3Arelativetourl%3A.json'
content_hash: 'sha256:98069312f1e047f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# URLWithDataRepresentation:relativeToURL:

<sub>Type Method</sub>

Initializes and returns a newly created NSURL using the contents of the given data, relative to a base URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSURL *) URLWithDataRepresentation:(NSData *) data relativeToURL:(NSURL *) baseURL;
```

## Discussion

If the data representation is not a legal URL string as ASCII bytes, the URL object may not behave as expected.

## See Also

### Creating a URL object

- [URLWithString:](urlwithstring_.md) — Creates and returns an NSURL object initialized with a provided URL string.
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
