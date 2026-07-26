---
title: BOOL
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/bool
source_url: 'https://developer.apple.com/documentation/objectivec/bool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/bool.json'
content_hash: 'sha256:85287370ea4ec1a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# BOOL

<sub>Type Alias</sub>

Type to represent a Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef bool BOOL;
```

## Discussion

`BOOL` is explicitly signed so `@encode(BOOL)` is `c` rather than `C` even if `-funsigned-char` is used.

For values, see [Boolean Values](boolean-values.md).

### Special Considerations

Since the type of `BOOL` is actually `char`, it does not behave in the same way as a C `_Bool` value or a C++ _bool_ value. For example, the conditional in the following code will be false on i386 (and true on PPC):

```objc
- (BOOL)value {
    return 256;
}
// then
if ([self value]) doStuff();
```

By contrast, the conditional in the following code will be true on all platforms (even where `sizeof(bool) == 1`):

```objc
- (bool)value {
    return 256;
}
// then
if ([self value]) doStuff();
```
