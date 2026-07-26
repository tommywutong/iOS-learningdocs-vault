---
title: 'exceptionWithName:reason:userInfo:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexception/exceptionwithname:reason:userinfo:'
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/exceptionwithname:reason:userinfo:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/exceptionwithname%3Areason%3Auserinfo%3A.json'
content_hash: 'sha256:fe170e85d394d3ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# exceptionWithName:reason:userInfo:

<sub>Type Method</sub>

Creates and returns an exception object .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSException *) exceptionWithName:(NSExceptionName) name reason:(NSString *) reason userInfo:(NSDictionary *) userInfo;
```

## Parameters

- `name` — The name of the exception.

- `reason` — A human-readable message string summarizing the reason for the exception.

- `userInfo` — A dictionary containing user-defined information relating to the exception

## Return Value

The created `NSException` object or `nil` if the object couldn’t be created.

## See Also

### Related Documentation

- [userInfo](userinfo-swift.property.md) — A dictionary containing application-specific data pertaining to the receiver.
- [reason](reason-swift.property.md) — A string containing a “human-readable” reason for the receiver.
- [Exception Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Exceptions.html#//apple_ref/doc/uid/10000012i)
- [name](name-swift.property.md) — A string used to uniquely identify the receiver.

### Creating and Raising an NSException Object

- [raise:format:](raise_format_.md) — A convenience method that creates and raises an exception.
- [+ raise:format:arguments:](<raise(__format_arguments_).md>) — Creates and raises an exception with the specified name, reason, and arguments.
- [- initWithName:reason:userInfo:](<init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.
- [- raise](<raise().md>) — Raises the receiver, causing program flow to jump to the local exception handler.
