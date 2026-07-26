---
title: NS_VOIDRETURN
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/ns_voidreturn
source_url: 'https://developer.apple.com/documentation/foundation/ns_voidreturn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/ns_voidreturn.json'
content_hash: 'sha256:90e1a8d2ef76bec2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NS_VOIDRETURN

<sub>Macro</sub>

Permits program control to exit from an exception-handling domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NS_VOIDRETURN
```

## Discussion

The `NS_VOIDRETURN` macro returns program control to the caller out of the exception-handling domain—that is, a section of code between the [NS_DURING](ns_during.md) and [NS_HANDLER](ns_handler.md) macros that might raise an exception. The standard `return` statement does not work as expected in the exception-handling domain.

## See Also

### Legacy Macros

- [NS_DURING](ns_during.md) — Marks the start of the exception-handling domain.
- [NS_ENDHANDLER](ns_endhandler.md) — Marks the end of the local event handler.
- [NS_HANDLER](ns_handler.md) — Marks the end of the exception-handling domain and the start of the local exception handler.
- [NS_VALUERETURN](ns_valuereturn.md) — Permits program control to exit from an exception-handling domain with a value of a specified type.
