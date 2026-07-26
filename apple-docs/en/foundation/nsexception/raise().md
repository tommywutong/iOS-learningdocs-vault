---
title: raise()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexception/raise()
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/raise()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/raise%28%29.json'
content_hash: 'sha256:d3c1801937f9f517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# raise()

<sub>Instance Method</sub>

Raises the receiver, causing program flow to jump to the local exception handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func raise()
```

## Discussion

When there are no exception handlers in the exception handler stack, unless the exception is raised during the posting of a notification, this method calls the uncaught exception handler, in which last-minute logging can be performed. The program then terminates, regardless of the actions taken by the uncaught exception handler.

## See Also

### Creating and Raising an NSException Object

- [+ raise:format:arguments:](<raise(__format_arguments_).md>) — Creates and raises an exception with the specified name, reason, and arguments.
- [- initWithName:reason:userInfo:](<init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.
