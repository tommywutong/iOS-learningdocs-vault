---
title: 字节序实用工具
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/byte-order-utilities
source_url: 'https://developer.apple.com/documentation/corefoundation/byte-order-utilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/byte-order-utilities.json'
content_hash: 'sha256:fe03a9f43532d4df'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md)

# 字节序实用工具

<sub>API 集合</sub>

## 概述

在处理跨平台传输或共享的二进制数据时，你需要关注每个平台如何存储数值。平台以大端序（big-endian）或小端序（little-endian）格式存储值。在大端序机器（例如 PowerPC 机器）上，值在内存中以最高有效字节在前的方式存储；在小端序机器（例如 Pentium 机器）上，值以最低有效字节在前的方式存储。如果其中一台计算机未正确转换，以不同格式发送到另一平台的多字节值将被错误解读。

你使用 [CFByteOrderGetCurrent](<cfbyteordergetcurrent().md>) 函数识别当前平台的原生格式。使用诸如 [CFSwapInt32BigToHost](<cfswapint32bigtohost(__).md>) 和 [CFConvertFloat32HostToSwapped](<cfconvertfloat32hosttoswapped(__).md>) 之类的函数在不同字节序格式之间转换值。

## 主题

### Core Foundation 字节序实用工具杂项函数

- [CFByteOrderGetCurrent](<cfbyteordergetcurrent().md>) — 返回当前计算机的字节序。
- [CFConvertDoubleHostToSwapped](<cfconvertdoublehosttoswapped(__).md>) — 将 64 位 double 从主机的原生字节序转换为平台无关格式。
- [CFConvertDoubleSwappedToHost](<cfconvertdoubleswappedtohost(__).md>) — 将 64 位 double 从平台无关格式转换为主机的原生字节序。
- [CFConvertFloat32HostToSwapped](<cfconvertfloat32hosttoswapped(__).md>) — 将 32 位 float 从主机的原生字节序转换为平台无关格式。
- [CFConvertFloat32SwappedToHost](<cfconvertfloat32swappedtohost(__).md>) — 将 32 位 float 从平台无关格式转换为主机的原生字节序。
- [CFConvertFloat64HostToSwapped](<cfconvertfloat64hosttoswapped(__).md>) — 将 64 位 float 从主机的原生字节序转换为平台无关格式。
- [CFConvertFloat64SwappedToHost](<cfconvertfloat64swappedtohost(__).md>) — 将 64 位 float 从平台无关格式转换为主机的原生字节序。
- [CFConvertFloatHostToSwapped](<cfconvertfloathosttoswapped(__).md>) — 将 32 位 float 从主机的原生字节序转换为平台无关格式。
- [CFConvertFloatSwappedToHost](<cfconvertfloatswappedtohost(__).md>) — 将 32 位 float 从平台无关格式转换为主机的原生字节序。
- [CFSwapInt16](<cfswapint16(__).md>) — 交换 16 位整数的字节。
- [CFSwapInt16BigToHost](<cfswapint16bigtohost(__).md>) — 将 16 位整数从大端序格式转换为主机的原生字节序。
- [CFSwapInt16HostToBig](<cfswapint16hosttobig(__).md>) — 将 16 位整数从主机的原生字节序转换为大端序格式。
- [CFSwapInt16HostToLittle](<cfswapint16hosttolittle(__).md>) — 将 16 位整数从主机的原生字节序转换为小端序格式。
- [CFSwapInt16LittleToHost](<cfswapint16littletohost(__).md>) — 将 16 位整数从小端序格式转换为主机的原生字节序。
- [CFSwapInt32](<cfswapint32(__).md>) — 交换 32 位整数的字节。
- [CFSwapInt32BigToHost](<cfswapint32bigtohost(__).md>) — 将 32 位整数从大端序格式转换为主机的原生字节序。
- [CFSwapInt32HostToBig](<cfswapint32hosttobig(__).md>) — 将 32 位整数从主机的原生字节序转换为大端序格式。
- [CFSwapInt32HostToLittle](<cfswapint32hosttolittle(__).md>) — 将 32 位整数从主机的原生字节序转换为小端序格式。
- [CFSwapInt32LittleToHost](<cfswapint32littletohost(__).md>) — 将 32 位整数从小端序格式转换为主机的原生字节序。
- [CFSwapInt64](<cfswapint64(__).md>) — 交换 64 位整数的字节。
- [CFSwapInt64BigToHost](<cfswapint64bigtohost(__).md>) — 将 64 位整数从大端序格式转换为主机的原生字节序。
- [CFSwapInt64HostToBig](<cfswapint64hosttobig(__).md>) — 将 64 位整数从主机的原生字节序转换为大端序格式。
- [CFSwapInt64HostToLittle](<cfswapint64hosttolittle(__).md>) — 将 64 位整数从主机的原生字节序转换为小端序格式。
- [CFSwapInt64LittleToHost](<cfswapint64littletohost(__).md>) — 将 64 位整数从小端序格式转换为主机的原生字节序。

### 数据类型

- [CFSwappedFloat32](cfswappedfloat32.md) — 以平台无关字节序保存 32 位 float 值的结构体。
- [CFSwappedFloat64](cfswappedfloat64.md) — 以平台无关字节序保存 64 位 float 值的结构体。

### 常量

- [CFByteOrder](cfbyteorder.md) — 标识字节序的标志。

## 另请参阅

### 相关文档

- [Core Foundation 内存管理编程指南](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)

### 实用工具

- [基础实用工具](base-utilities.md)
- [Core Foundation URL 访问实用工具](core-foundation-url-access-utilities.md)
- [偏好设置实用工具](preferences-utilities.md)
- [套接字名称服务器实用工具](socket-name-server-utilities.md)
- [时间实用工具](time-utilities.md)
