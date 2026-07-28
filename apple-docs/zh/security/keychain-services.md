---
title: 钥匙串服务
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/keychain-services
source_url: 'https://developer.apple.com/documentation/security/keychain-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/keychain-services.json'
content_hash: 'sha256:73c9a056ccaf7a3d'
translated: true
---

> 导航：[技术](../technologies.md) · [安全性](../security.md)

# 钥匙串服务

代表用户安全地存储小块数据。

## 概述

电脑用户常常有一些需要安全存储的小秘密。例如，大多数人都管理着大量的在线账户。记住每个账户复杂且独一无二的密码是不可能的，但把它们写下来既不安全又繁琐。用户通常的应对方式是跨多个账户重复使用简单的密码，这同样不安全。

钥匙串服务（keychain services）API 通过为你的 App 提供一种机制，将少量用户数据存储在一个称为钥匙串的加密数据库中，帮助你解决这个问题。当你为用户安全地记住密码时，你就解放了用户，让他们可以选择一个复杂的密码。

钥匙串不仅限于密码，如图 1 所示。你可以存储用户明确关心的其他秘密，例如信用卡信息，甚至简短笔记。你还可以存储用户需要但可能没有意识到的条目。例如，通过 [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) 管理的加密密钥和证书，可以让用户参与安全通信，并与其他用户和设备建立信任。你也可以使用钥匙串来存储这些条目。

![](../../../attachments/ad0bbbff6a49d15c0da8e31ef76adb08/media-2891902@2x.png)

<sub>图示展示密码、密钥、证书和身份标识均通过钥匙串服务 API 安全地存储到钥匙串中。</sub>

## 主题

### API 组件

- [钥匙串条目](keychain-items.md) — 将机密信息嵌入到你存储在钥匙串中的条目里。
- [钥匙串](keychains.md) — 在 macOS 中创建和管理整个钥匙串。
- [访问控制列表](access-control-lists.md) — 控制在 macOS 中哪些 App 可以访问钥匙串条目。
