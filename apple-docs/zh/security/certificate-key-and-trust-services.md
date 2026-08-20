---
title: 证书、密钥与信任服务
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/certificate-key-and-trust-services
source_url: 'https://developer.apple.com/documentation/security/certificate-key-and-trust-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/certificate-key-and-trust-services.json'
content_hash: 'sha256:a1ba3849a5401d2a'
translated: true
---

> 导航：[技术](../technologies.md) · [Security](../security.md)

# 证书、密钥与信任服务

使用证书和加密密钥建立信任。

## 概述

证书、密钥与信任服务 API 是一组函数和数据结构，你可以用来进行安全且经过认证的数据传输。具体来说，你可以使用此 API 来管理和使用以下内容：

- **证书和身份标识**。证书是一组数据，以防篡改的方式标识其所有者。当你使用证书分发公钥时，接收方可以确信其来源。你还可以将证书及其对应的私钥打包到需要保密的身份标识对象中。
- **策略与信任服务**。收到证书后，在使用其中嵌入的公钥之前，你需要回答一个问题：“我可以信任这个证书吗？”你要根据一组标准（即信任策略）对信任进行评估。
- **加密密钥**。拥有了来源可信的密钥后，你就可以开始执行加密操作，例如加密或数据签名与验证。这些操作通常在更广泛的用途中发挥作用，例如对用户进行身份验证、安全地传输数据，或验证数据块自签名密封后未被更改。

> [!note] 注意
> 依赖 [Security Interface](../securityinterface.md) 框架的类，以确保在向用户显示证书和信任设置、以及用户选择身份标识或修改钥匙串（Keychain）设置时，提供一致的体验。

## 主题

### API 组件

- [证书](certificates.md) — 管理数字证书。
- [密钥](keys.md) — 生成、存储和使用加密密钥。
- [身份标识](identities.md) — 将证书和加密密钥组合为身份标识。
- [策略](policies.md) — 获取用于建立信任的策略。
- [信任](trust.md) — 根据给定的策略评估信任。

### 线程安全

- [处理并发](working-with-concurrency.md) — 了解与证书、密钥与信任服务 API 相关的线程安全问题。

## 另请参阅

### 相关文档

- [Cryptographic Services Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172)
- [Security Interface](../securityinterface.md) — 为授权、数字证书访问和钥匙串条目访问等安全功能提供用户界面元素。
