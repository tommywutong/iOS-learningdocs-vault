---
title: 'allocWithZone:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsport-allocwithzone
source_url: 'https://developer.apple.com/documentation/foundation/nsport-allocwithzone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsport-allocwithzone.json'
content_hash: 'sha256:3037c411b187bdb2'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [流、套接字与端口](streams-sockets-and-ports.md) · [Port](port.md)

# allocWithZone:

<sub>文章</sub>

返回 `NSMachPort` 类的一个实例。

## 概述

为了在 Mach 上保持向后兼容，向 `NSPort` 类发送 [allocWithZone:](nsport-allocwithzone.md) 时，该方法会返回 `NSMachPort` 类的一个实例。否则，它会返回某个具体子类的实例，该实例可用于本地计算机上线程之间或进程之间的消息传递；如果是 `NSSocketPort`，则可用于不同计算机上的进程之间进行消息传递。

## 另请参阅

### 相关文档

- [线程编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [分布式对象编程主题](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
