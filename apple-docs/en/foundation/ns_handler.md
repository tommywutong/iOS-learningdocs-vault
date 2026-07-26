---
title: NS_HANDLER
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/ns_handler
source_url: 'https://developer.apple.com/documentation/foundation/ns_handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/ns_handler.json'
content_hash: 'sha256:0ffcd658eeab2b95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NS_HANDLER

<sub>Macro</sub>

Marks the end of the exception-handling domain and the start of the local exception handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NS_HANDLER
```

## Discussion

The NS_HANDLER macro marks end of a section of code that is an exception-handling domain while at the same time marking the beginning of a section of code that is a local exception handler for that domain. (The [NS_DURING](ns_during.md) macro marks the beginning of the exception-handling domain; the [NS_ENDHANDLER](ns_endhandler.md) marks the end of the local exception handler.) If an exception is raised in the exception-handling domain, the local exception handler is first given the chance to handle the exception before lower-level handlers are given a chance.

## See Also

### Legacy Macros

- [NS_DURING](ns_during.md) — Marks the start of the exception-handling domain.
- [NS_ENDHANDLER](ns_endhandler.md) — Marks the end of the local event handler.
- [NS_VALUERETURN](ns_valuereturn.md) — Permits program control to exit from an exception-handling domain with a value of a specified type.
- [NS_VOIDRETURN](ns_voidreturn.md) — Permits program control to exit from an exception-handling domain.
