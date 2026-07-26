---
title: NS_VALID_UNTIL_END_OF_SCOPE
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/ns_valid_until_end_of_scope
source_url: 'https://developer.apple.com/documentation/foundation/ns_valid_until_end_of_scope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/ns_valid_until_end_of_scope.json'
content_hash: 'sha256:8accf41fff4ba403'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NS_VALID_UNTIL_END_OF_SCOPE

<sub>Macro</sub>

Marks local variables of type `id` or pointer-to-ObjC-object-type so that values stored into those local variable are not aggressively released by the compiler during optimization. Instead, the values are held until either the variable is assigned to again, or the end of the scope of the local variable (such as in a compound statement or a method definition).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NS_VALID_UNTIL_END_OF_SCOPE
```

## See Also

### Macros

- [ABS](abs.md)
- [FOUNDATION_EXPORT](foundation_export.md)
- [FOUNDATION_EXTERN](foundation_extern.md)
- [FOUNDATION_EXTERN_INLINE](foundation_extern_inline.md)
- [FOUNDATION_IMPORT](foundation_import.md)
- [FOUNDATION_STATIC_INLINE](foundation_static_inline.md)
- [FOUNDATION_SWIFT_SDK_EPOCH_AT_LEAST](foundation_swift_sdk_epoch_at_least.md)
- [MAX](max.md)
- [MIN](min.md)
- [NS_ASSUME_NONNULL_BEGIN](ns_assume_nonnull_begin.md)
- [NS_ASSUME_NONNULL_END](ns_assume_nonnull_end.md)
- [NS_AUTOMATED_REFCOUNT_UNAVAILABLE](ns_automated_refcount_unavailable.md)
- [NS_AUTOMATED_REFCOUNT_WEAK_UNAVAILABLE](ns_automated_refcount_weak_unavailable.md)
- [NS_AVAILABLE](ns_available.md)
- [NS_AVAILABLE_IOS](ns_available_ios.md)
