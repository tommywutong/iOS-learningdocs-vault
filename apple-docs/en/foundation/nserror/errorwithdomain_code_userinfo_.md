---
title: 'errorWithDomain:code:userInfo:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nserror/errorwithdomain:code:userinfo:'
source_url: 'https://developer.apple.com/documentation/foundation/nserror/errorwithdomain:code:userinfo:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/errorwithdomain%3Acode%3Auserinfo%3A.json'
content_hash: 'sha256:e6372ce5dc4bdd6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# errorWithDomain:code:userInfo:

<sub>Type Method</sub>

Creates and initializes an `NSError` object for a given domain and code with a given `userInfo` dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) errorWithDomain:(NSErrorDomain) domain code:(NSInteger) code userInfo:(NSDictionary<NSString *,id> *) dict;
```

## Parameters

- `domain` — The error domain—this can be one of the predefined `NSError` domains, or an arbitrary string describing a custom domain. `domain` must not be `nil`. See `Error Domains` for a list of predefined domains.

- `code` — The error code for the error.

- `dict` — The `userInfo` dictionary for the error. `userInfo` may be `nil`.

## Return Value

An `NSError` object for `domain` with the specified error `code` and the dictionary of arbitrary data `userInfo`.

## See Also

### Related Documentation

- [Error Handling Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806)

### Creating Error Objects

- [- initWithDomain:code:userInfo:](<init(domain_code_userinfo_).md>) — Returns an `NSError` object initialized for a given domain and code with a given `userInfo` dictionary.
