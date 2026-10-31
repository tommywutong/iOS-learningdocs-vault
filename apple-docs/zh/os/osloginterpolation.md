---
title: OSLogInterpolation
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osloginterpolation
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation.json'
content_hash: 'sha256:8b30eedf7fdf0f94'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogInterpolation

<sub>结构体</sub>

日志消息各元素的容器。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogInterpolation
```

## 概述

[OSLogInterpolation](osloginterpolation.md) 结构体包含格式化字符串及其插值参数。不要直接创建 [OSLogInterpolation](osloginterpolation.md) 结构体。当你使用 [Logger](logger.md) 对象记录消息时，系统会自动创建它们。

编写日志消息时，你可以把代码中变量的内容直接纳入消息字符串。这样做时，日志系统会创建 [OSLogInterpolation](osloginterpolation.md) 结构体来存储这些值。该结构体按原样存储所提供的值，日志系统仅在最终日志消息中才把这些值格式化为字符串。要更改值的最终外观，请连同该值一起包含额外参数。请看下面的示例，它记录了几种不同类型的值：

```swift
logger.log("\(taskID) \(giftCardID) \(serverID) \(seconds)")
```

对于长度可变的值，对它们进行格式化可以让日志消息更易读。在上例中，`giftCardID` 和 `seconds` 包含长度可变的值。下面的示例通过使所有礼品卡 ID 具有相同宽度并将它们对齐到可用空间的左边缘，修复了格式化问题。该示例还将每个秒数值格式化为小数点右侧仅有两位数字的定点数字。

```swift
logger.log("\(taskID) \(giftCardID, align: .left(columns: GiftCard.maxIDLength)) \(serverID) \(seconds, format: .fixed(precision: 2))")
```

因为字符串和自定义对象可能包含对用户敏感的信息，日志系统默认会隐去这些值，但不会隐去数值。最终日志消息会显示类似 `<private>` 的字符串，而不是实际值。如果你知道该值不包含敏感数据，请使用 `privacy` 参数更改隐私设置，如下例所示：

```swift
logger.log("Paid with bank account \(accountNumberString)")   // 默认隐去
logger.log("Ordered smoothie \(smoothieName, privacy: .public)")  // 可见！
```

## 关系

- **遵循**： [StringInterpolationProtocol](../swift/stringinterpolationprotocol.md)

## 主题

### 追加字符串

- [appendInterpolation(_:align:privacy:)](<osloginterpolation/appendinterpolation(__align_privacy_)-6tazr.md>) — 追加一个插值字符串。
- [appendInterpolation(_:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__align_privacy_attributes_)-7g68v.md>) — 使用指定属性追加一个插值字符串。

### 追加有符号整数

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-8kli1.md>) — 追加一个插值整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-5ihzf.md>) — 追加一个插值 8 位整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-190d0.md>) — 追加一个插值 16 位整数。
- [appendInterpolation(_:format:privacy:)](<osloginterpolation/appendinterpolation(__format_privacy_)-3ji02.md>) — 追加一个插值 32 位整数。
- [appendInterpolation(_:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_privacy_attributes_)-4i2ir.md>) — 使用指定属性追加一个插值 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-2sb1i.md>) — 使用指定对齐方式追加一个插值 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-802m9.md>) — 追加一个插值 64 位整数。

### 追加无符号整数

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-20jin.md>) — 追加一个插值无符号整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-4qvu9.md>) — 追加一个插值无符号 8 位整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-7k91g.md>) — 追加一个插值无符号 16 位整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-2i3qh.md>) — 追加一个插值无符号 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-81jbm.md>) — 追加一个插值无符号 64 位整数。

### 追加 Double

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-6mu00.md>) — 追加一个插值 double。
- [appendInterpolation(_:format:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_align_privacy_attributes_)-8bi90.md>) — 使用指定属性追加一个插值 double。

### 追加 Float

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-7z1jd.md>) — 追加一个插值 float。
- [appendInterpolation(_:format:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_align_privacy_attributes_)-78sek.md>) — 使用指定属性追加一个插值 float。

### 追加布尔值

- [appendInterpolation(_:format:privacy:)](<osloginterpolation/appendinterpolation(__format_privacy_)-686xc.md>) — 向消息添加一个布尔参数。

### 追加泛型类型

- [appendInterpolation(_:align:privacy:)](<osloginterpolation/appendinterpolation(__align_privacy_)-84m60.md>) — 追加某个类型的插值文本表示。
- [appendInterpolation(_:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__align_privacy_attributes_)-xyum.md>) — 使用指定属性追加某个类型的插值文本表示。
- [appendInterpolation(_:format:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_align_privacy_attributes_)-8107a.md>) — 使用指定属性追加一个插值数值类型。
- [appendInterpolation(_:align:privacy:)](<osloginterpolation/appendinterpolation(__align_privacy_)-8hwmt.md>) — 追加一个插值类型描述。
- [appendInterpolation(_:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__align_privacy_attributes_)-9hehv.md>) — 使用指定属性追加一个插值类型描述。

### 追加指针数据

- [appendInterpolation(_:bytes:format:privacy:)](<osloginterpolation/appendinterpolation(__bytes_format_privacy_).md>) — 追加插值指针数据。
- [appendInterpolation(_:bytes:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__bytes_format_privacy_attributes_).md>) — 使用指定属性追加插值指针数据。
- [appendInterpolation(_:format:privacy:)](<osloginterpolation/appendinterpolation(__format_privacy_)-5qaau.md>) — 追加一个插值原始字节集合。
- [appendInterpolation(_:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_privacy_attributes_)-93lbs.md>) — 使用指定属性追加一个插值原始字节集合。

### 追加对象

- [appendInterpolation(_:privacy:)](<osloginterpolation/appendinterpolation(__privacy_).md>) — 追加一个插值对象描述。
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-3czd2.md>) — 使用指定属性追加一个插值对象描述。

### 实例方法

- [appendInterpolation(_:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_privacy_attributes_)-6le5w.md>)
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-4o74h.md>)
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-6vtcc.md>)
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-9eafm.md>)

## 另请参阅

### 值插值

- [OSLogIntExtendedFormat](oslogintextendedformat.md) — 在日志记录期间展开以 int 存储的比特率信息的选项。
