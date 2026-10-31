---
title: exponential
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting/exponential
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/exponential'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/exponential.json'
content_hash: 'sha256:51306e9c78da3215'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# exponential

<sub>类型属性</sub>

标准指数格式选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var exponential: OSLogFloatFormatting { get }
```

## 讨论

此选项等效于 `fprintf` 中的 `%e` 选项。它以 `[-]d.ddde±dd` 的形式打印数字，其中 `d` 表示数字的各位。小数点后的位数由系统决定。

## 另请参阅

### 获取标准格式

- [fixed](fixed.md) — 标准定点格式选项。
- [hex](hex.md) — 浮点值的标准十六进制格式。
- [hybrid](hybrid.md) — 根据数值大小切换格式的混合选项。
