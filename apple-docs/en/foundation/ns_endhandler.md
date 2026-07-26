---
title: NS_ENDHANDLER
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/ns_endhandler
source_url: 'https://developer.apple.com/documentation/foundation/ns_endhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/ns_endhandler.json'
content_hash: 'sha256:799d14587353ee1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NS_ENDHANDLER

<sub>Macro</sub>

Marks the end of the local event handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NS_ENDHANDLER
```

## Discussion

The `NS_ENDHANDLER` marks the end of a section of code that is a local exception handler. (The [NS_HANDLER](ns_handler.md)macros marks the beginning of this section.) If an exception is raised in the exception handling domain marked off by the [NS_DURING](ns_during.md) and [NS_HANDLER](ns_handler.md), the local exception handler (if specified) is given a chance to handle the exception.

## See Also

### Legacy Macros

- [NS_DURING](ns_during.md) — Marks the start of the exception-handling domain.
- [NS_HANDLER](ns_handler.md) — Marks the end of the exception-handling domain and the start of the local exception handler.
- [NS_VALUERETURN](ns_valuereturn.md) — Permits program control to exit from an exception-handling domain with a value of a specified type.
- [NS_VOIDRETURN](ns_voidreturn.md) — Permits program control to exit from an exception-handling domain.
