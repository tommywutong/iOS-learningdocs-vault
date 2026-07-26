---
title: NS_DURING
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/ns_during
source_url: 'https://developer.apple.com/documentation/foundation/ns_during'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/ns_during.json'
content_hash: 'sha256:99cff7d924e5ee19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NS_DURING

<sub>Macro</sub>

Marks the start of the exception-handling domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NS_DURING
```

## Discussion

The `NS_DURING` macro marks the start of the exception-handling domain for a section of code. (The [NS_HANDLER](ns_handler.md)macro marks the end of the domain.) Within the exception-handling domain you can raise an exception, giving the local exception handler (or lower exception handlers) a chance to handle it.

## See Also

### Legacy Macros

- [NS_ENDHANDLER](ns_endhandler.md) — Marks the end of the local event handler.
- [NS_HANDLER](ns_handler.md) — Marks the end of the exception-handling domain and the start of the local exception handler.
- [NS_VALUERETURN](ns_valuereturn.md) — Permits program control to exit from an exception-handling domain with a value of a specified type.
- [NS_VOIDRETURN](ns_voidreturn.md) — Permits program control to exit from an exception-handling domain.
