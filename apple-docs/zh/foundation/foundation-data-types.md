---
title: Foundation 数据类型
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/foundation-data-types
source_url: 'https://developer.apple.com/documentation/foundation/foundation-data-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/foundation-data-types.json'
content_hash: 'sha256:8fbbbc7fc83b98d9'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md)

# Foundation 数据类型

<sub>API 集合</sub>

本文档描述 Foundation 框架中的数据类型和常量。

## 主题

### 类

- [NSKeyValueObservation](nskeyvalueobservation.md)
- [NSKeyValueSharedObservers](nskeyvaluesharedobservers.md) — 可向多个可观察对象注册的键值观察集合
- [NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobserverssnapshot.md) — 可向多个可观察对象注册的键值观察集合。使用 `-[NSKeyValueSharedObservers snapshot]` 创建

### 协议

- [DiscreteFormatStyle](discreteformatstyle.md) — 将连续输入转换为离散输出，并提供有关其离散化边界信息的格式样式。
- [NSKeyValueObservingCustomization](nskeyvalueobservingcustomization.md) — 使用键值观察不要求符合 NSKeyValueObservingCustomization。如果需要停用某个键的自动通知或添加依赖键，请提供这些函数的实现

### 结构体

- [AsyncCharacterSequence](asynccharactersequence.md) — 字符的异步序列。
- [AsyncLineSequence](asynclinesequence.md) — 文本行的异步序列。
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — Unicode 标量值的异步序列。
- [Expression](expression.md)
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — 表示格式化上下文字典中某个键的类型。
- [NSKeyValueChangeKey](nskeyvaluechangekey.md) — 可以出现在更改字典中的键。
- [NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [NSKeyValueOperator](nskeyvalueoperator.md) — 这些常量定义可用的数组运算符。有关更多信息，请参阅[使用集合运算符](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html)。
- [PresentationIntent](presentationintent.md) — 定义段落、列表、块引用和表格等字符 block 的呈现意图的类型。

### 变量

- [NSOperationNotSupportedForKeyException](nsoperationnotsupportedforkeyexception.md)
- [NSURLSessionUploadTaskResumeData](nsurlsessionuploadtaskresumedata.md) — 上传失败期间收到的 NSError 的 userInfo 字典中的键。
- [kCFStringEncodingASCII](kcfstringencodingascii.md)

### 宏

- [Expression(_:)](<expression(__).md>)
- [Predicate(_:)](<predicate(__).md>)

### 类型别名

- [uuid_string_t](uuid_string_t.md)
- [uuid_t](uuid_t.md)

## 另请参阅

### 参考

- [Foundation 枚举](foundation-enumerations.md)
