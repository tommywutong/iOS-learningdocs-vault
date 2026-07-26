---
title: 'raise:format:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexception/raise:format:'
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/raise:format:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/raise%3Aformat%3A.json'
content_hash: 'sha256:5b6f4477657a7206'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# raise:format:

<sub>Type Method</sub>

A convenience method that creates and raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (void) raise:(NSExceptionName) name format:(NSString *) format;
```

## Parameters

- `name` — The name of the exception.

- `format` — A human-readable message string (that is, the exception reason) with conversion specifications for the variable arguments that follow.

## Discussion

The user-defined information is `nil` for the generated exception object.

Pass variable information to be inserted into the formatted exception reason (in the manner of `printf`) as variadic arguments.

## See Also

### Creating and Raising an NSException Object

- [exceptionWithName:reason:userInfo:](exceptionwithname_reason_userinfo_.md) — Creates and returns an exception object .
- [+ raise:format:arguments:](<raise(__format_arguments_).md>) — Creates and raises an exception with the specified name, reason, and arguments.
- [- initWithName:reason:userInfo:](<init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.
- [- raise](<raise().md>) — Raises the receiver, causing program flow to jump to the local exception handler.
