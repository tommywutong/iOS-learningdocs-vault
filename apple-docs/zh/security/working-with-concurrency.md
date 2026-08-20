---
title: 处理并发
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/working-with-concurrency
source_url: 'https://developer.apple.com/documentation/security/working-with-concurrency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/working-with-concurrency.json'
content_hash: 'sha256:187f9e3bbb2b0f87'
translated: true
---

> 导航：[技术](../technologies.md) · [安全](../security.md) · [证书、密钥与信任服务](certificate-key-and-trust-services.md)

# 处理并发

<sub>文章</sub>

了解与证书、密钥和信任服务 API 相关的线程安全（thread safety）问题。

## 概述

在 macOS 中，此 API 的某些函数在等待用户输入时会 block（阻塞）（例如，当要求用户解锁钥匙串或授予更改信任设置的权限时）。通常，在主线程以外的线程中使用此 API 是安全的，但应避免从多个操作、工作队列或线程同时调用这些函数。相反，应将函数调用序列化，或将其限制在单个线程中。

在 iOS 中，此 API 中的所有函数都是线程安全且可重入的。
