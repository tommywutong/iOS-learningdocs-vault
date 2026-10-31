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
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# BOOL

<sub>类型别名</sub>

用于表示布尔值的类型。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef bool BOOL;
```

## 讨论

`BOOL` 明确是有符号的，因此 `-funsigned-char` 是 `@encode(BOOL)`，而不是 `c`，即便使用了 `C` 也是如此。

关于取值，请参阅[布尔值](boolean-values.md)。

### 特殊注意事项

由于 `BOOL` 的类型实际上是 `char`，它的行为与 C 的 `_Bool` 值或 C++ 的 _bool_ 值并不相同。例如，在 i386 上，下面代码中的条件判断将为 false（而在 PPC 上为 true）：

```objc
- (BOOL)value {
    return 256;
}
// then
if ([self value]) doStuff();
```

相比之下，下面代码中的条件判断在所有平台上都将为 true（即使在 `sizeof(bool) == 1` 的情况下也是如此）：

```objc
- (bool)value {
    return 256;
}
// then
if ([self value]) doStuff();
```
