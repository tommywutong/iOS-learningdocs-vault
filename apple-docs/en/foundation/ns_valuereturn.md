---
title: NS_VALUERETURN
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/ns_valuereturn
source_url: 'https://developer.apple.com/documentation/foundation/ns_valuereturn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/ns_valuereturn.json'
content_hash: 'sha256:ad1c081f260b0e62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NS_VALUERETURN

<sub>Macro</sub>

Permits program control to exit from an exception-handling domain with a value of a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NS_VALUERETURN(v, t)
```

## Parameters

- `v` — A value to preserve beyond the exception-handling domain.

- `t` — The type of the value specified in `val`.

## Discussion

The `NS_VALUERETURN` macro returns program control to the caller out of the exception-handling domain—that is, a section of code between the [NS_DURING](ns_during.md) and [NS_HANDLER](ns_handler.md) macros that might raise an exception. The specified value (of the specified type) is returned to the caller. The standard `return` statement does not work as expected in the exception-handling domain.

## See Also

### Legacy Macros

- [NS_DURING](ns_during.md) — Marks the start of the exception-handling domain.
- [NS_ENDHANDLER](ns_endhandler.md) — Marks the end of the local event handler.
- [NS_HANDLER](ns_handler.md) — Marks the end of the exception-handling domain and the start of the local exception handler.
- [NS_VOIDRETURN](ns_voidreturn.md) — Permits program control to exit from an exception-handling domain.
