---
title: hybrid
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting/hybrid
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/hybrid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/hybrid.json'
content_hash: 'sha256:ea7c6a267b9ee0d7'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# hybrid

<sub>类型属性</sub>

根据数值大小切换格式的混合选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hybrid: OSLogFloatFormatting { get }
```

## 讨论

此选项等效于 `fprintf` 中的 `%g` 选项。当数值接近 `1.0` 时，其行为类似 [fixed](fixed.md) 选项；当数值指数较大时，其行为类似 [exponential](exponential.md) 选项。

## 另请参阅

### 获取标准格式

- [fixed](fixed.md) — 标准定点格式选项。
- [hex](hex.md) — 浮点值的标准十六进制格式。
- [exponential](exponential.md) — 标准指数格式选项。
