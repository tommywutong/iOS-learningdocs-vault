---
title: private
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/private
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/private'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/private.json'
content_hash: 'sha256:0817e66fdaf7bf32'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# private

<sub>类型属性</sub>

始终隐去插值的标准选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var `private`: OSLogPrivacy { get }
```

## 讨论

当系统隐去某个值时，会用通用字符串替换该值显示。如果你想关联包含相同值的日志消息，请使用 [private(mask:)](<private(mask_).md>) 函数，创建一个带有 [OSLogPrivacy.Mask.hash](mask/hash.md) 掩码的结构体。

## 另请参阅

### 获取隐私选项

- [auto](auto.md) — 让系统决定是隐去还是显示值的标准选项。
- [public](public.md) — 始终显示插值的标准选项。
- [sensitive](sensitive.md) — 始终隐去包含敏感信息的插值的选项。
