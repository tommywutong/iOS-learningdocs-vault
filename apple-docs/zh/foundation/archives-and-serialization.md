---
title: 归档与序列化
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/archives-and-serialization
source_url: 'https://developer.apple.com/documentation/foundation/archives-and-serialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/archives-and-serialization.json'
content_hash: 'sha256:196cb39489eabfb8'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 归档与序列化

<sub>API 集合</sub>

在对象和值与属性列表、JSON 及其他平面二进制表示之间进行转换。

## 概述

使用这些 API 将 App 的内存中类型转换为适合通过 I/O 和网络接口进行序列化（serialization），或适合长期存储的表示。

在 Swift 中，标准库定义了 [Encodable](../swift/encodable.md)、[Decodable](../swift/decodable.md) 和 [Codable](../swift/codable.md) 类型，以及用于执行编码和解码的 [Encoder](../swift/encoder.md) 和 [Decoder](../swift/decoder.md) API，详见[编码、解码与序列化](../swift/encoding-decoding-and-serialization.md)。Foundation 通过 [EncodableWithConfiguration](encodablewithconfiguration.md) 和 [DecodableWithConfiguration](decodablewithconfiguration.md) 协议扩展了这些功能；这些协议适用于编码和解码时需要额外静态信息的类型，例如 [AttributedString](attributedstring.md)。

在 Objective-C 中，[NSCoding](nscoding.md) 定义了用于编码和解码对象的协议。为你自己的类型添加序列化支持时，还应采纳 [NSSecureCoding](nssecurecoding.md)。此协议可防范解码过程中实例化任意对象所引入的安全漏洞。

许多系统框架都会使用这些类型。与 URL 端点等外部系统交互时，请使用 JSON 和 XML API 将 App 的类型序列化为标准格式。

## 主题

### 采纳可编码性

- [编码和解码自定义类型](encoding-and-decoding-custom-types.md) — 使你的数据类型可编码和解码，以便兼容 JSON 等外部表示。
- [Codable](../swift/codable.md) — 一种可以在自身与外部表示之间转换的类型。
- [NSCoding](nscoding.md) — 一种协议，使对象可以进行编码和解码，以供归档（archiving）和分发。
- [NSSecureCoding](nssecurecoding.md) — 一种协议，以能抵御对象替换攻击的方式进行编码和解码。

### 序列化任意有效负载

- [CodableWithConfiguration](codablewithconfiguration.md) — 一种借助配置在自身与外部表示之间转换的类型，该配置负责处理所含类型的编码。
- [CodableConfiguration](codableconfiguration.md) — 一种属性包装器（property wrapper），通过提供用于补充序列化信息的配置，使类型具备可编码性。
- [DecodableWithConfiguration](decodablewithconfiguration.md) — 一种协议，适用于在提供额外配置类型时支持解码的类型。
- [DecodingConfigurationProviding](decodingconfigurationproviding.md) — 一种协议，其符合者提供配置实例，帮助解码自身不支持编码的类型。
- [EncodableWithConfiguration](encodablewithconfiguration.md) — 一种协议，适用于在提供额外配置类型时支持编码的类型。
- [EncodingConfigurationProviding](encodingconfigurationproviding.md) — 一种协议，其符合者提供配置实例，帮助编码自身不支持编码的类型。

### JSON

- [将 JSON 与自定义类型配合使用](using-json-with-custom-types.md) — 使用 Swift 的 JSON 支持来编码和解码 JSON 数据，而不受其结构限制。
- [JSONEncoder](jsonencoder.md) — 将数据类型实例编码为 JSON 对象的对象。
- [JSONDecoder](jsondecoder.md) — 从 JSON 对象解码数据类型实例的对象。
- [JSONSerialization](jsonserialization.md) — 在 JSON 与等效 Foundation 对象之间转换的对象。

### 属性列表

- [PropertyListEncoder](propertylistencoder.md) — 将数据类型实例编码为属性列表的对象。
- [PropertyListDecoder](propertylistdecoder.md) — 从属性列表解码数据类型实例的对象。
- [PropertyListSerialization](propertylistserialization.md) — 在属性列表与若干序列化表示之一之间转换的对象。

### XML

- [XML 处理与建模](xml-processing-and-modeling.md) — 解析 XML 文稿。

### 键控归档器

- [NSKeyedArchiver](nskeyedarchiver.md) — 将对象数据存储到由键引用的归档中的编码器。
- [NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md) — 键控归档器的委托（delegate）所实现的可选方法。
- [NSKeyedUnarchiver](nskeyedunarchiver.md) — 从由键引用的归档中恢复数据的解码器。
- [NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md) — 键控解档器的委托所实现的可选方法。
- [NSCoder](nscoder.md) — 作为对象基础的抽象类，这些对象使其他对象能够归档和分发。
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) — 在数据与支持安全编码的类之间转换的值转换器。

### 已废弃

- [NSArchiver](nsarchiver.md) — 将对象数据存储到归档中的编码器。 _(已废弃)_
- [NSUnarchiver](nsunarchiver.md) — 从归档中恢复数据的解码器。 _(已废弃)_

## 另请参阅

### 文件与数据持久化

- [文件系统](file-system.md) — 在文件系统中创建、读取、写入和检查文件及文件夹。
- [设置](settings.md) — 使用持久存储在本地磁盘或 iCloud 中的数据配置你的 App。
- [聚焦](spotlight.md) — 搜索本地设备上的文件和其他项目，并为你的 App 内容建立索引以供搜索。
- [iCloud](icloud.md) — 管理会在用户的 iCloud 设备之间自动同步的文件和键值数据。
- [优化 App 数据以进行 iCloud 备份](optimizing-your-app-s-data-for-icloud-backup.md) — 通过从备份中排除可清除和不可清除的数据，尽量减少创建备份所需的空间和时间。
