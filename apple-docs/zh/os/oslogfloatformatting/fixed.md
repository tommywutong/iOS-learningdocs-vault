---
title: fixed
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting/fixed
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/fixed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/fixed.json'
content_hash: 'sha256:2769246ef9e215a2'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# fixed

<sub>类型属性</sub>

标准定点格式选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var fixed: OSLogFloatFormatting { get }
```

## 讨论

此选项等效于 `fprintf` 的 `%f` 选项，会打印小数点前的全部位数，以及小数点后由系统决定数量的位数。

## 另请参阅

### 获取标准格式

- [hex](hex.md) — 浮点值的标准十六进制格式。
- [exponential](exponential.md) — 标准指数格式选项。
- [hybrid](hybrid.md) — 根据数值大小切换格式的混合选项。
