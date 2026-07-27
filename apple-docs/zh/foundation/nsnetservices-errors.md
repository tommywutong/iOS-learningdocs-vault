---
title: NSNetServices 错误
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnetservices-errors
source_url: 'https://developer.apple.com/documentation/foundation/nsnetservices-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnetservices-errors.json'
content_hash: 'sha256:f7567601210669ad'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [Bonjour](bonjour.md) · [NetService](netservice.md)

# NSNetServices 错误

<sub>API 集合</sub>

如果发生错误，委托（delegate）的错误处理方法会返回一个包含以下键的字典。

## 主题

### 常量

- [NSNetServicesErrorCode](netservice/errorcode-swift.type.property.md) — 此键标识最近一次操作期间发生的错误。
- [NSNetServicesErrorDomain](netservice/errordomain.md) — 此键标识错误的来源，即 `NSNetService` 对象或 Mach 网络层。对于大多数错误，你无需使用此键提供的值。

## 另请参阅

### 常量

- [ErrorCode](netservice/errorcode-swift.enum.md) — 这些常量标识访问网络服务时可能发生的错误。
- [Options](netservice/options.md) — 这些常量指定网络服务的选项。
