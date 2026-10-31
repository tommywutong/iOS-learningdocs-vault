---
title: 'right(columns:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogstringalignment/right(columns:)'
source_url: 'https://developer.apple.com/documentation/os/oslogstringalignment/right(columns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogstringalignment/right%28columns%3A%29.json'
content_hash: 'sha256:4c83d3a23870607a'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogStringAlignment](../oslogstringalignment.md)

# right(columns:)

<sub>类型方法</sub>

将值在指定宽度的列中右对齐。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func right(columns: @autoclosure @escaping () -> Int) -> OSLogStringAlignment
```

## 参数

- `columns` — 该项的宽度（以字符计）。

## 返回值

具有指定值的字符串对齐结构体。

## 另请参阅

### 获取自定义字符串对齐

- [left(columns:)](<left(columns_).md>) — 将值在指定宽度的列中左对齐。
