---
title: 使用钥匙串来管理用户机密
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/using-the-keychain-to-manage-user-secrets
source_url: 'https://developer.apple.com/documentation/security/using-the-keychain-to-manage-user-secrets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/using-the-keychain-to-manage-user-secrets.json'
content_hash: 'sha256:dee2ae5cd31d8b51'
translated: true
---

> 导航：[技术](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [钥匙串条目](keychain-items.md)

# 使用钥匙串来管理用户机密

通过将机密信息存储在钥匙串中，让用户免于记住那些小段机密。

## 概述

App 通常需要访问敏感的用户数据，例如密码，但保证数据安全可能会带来代价：如果你存储数据时不进行加密，就会造成安全风险。如果你改为反复提示用户，则会产生糟糕的用户体验——这通常会导致用户创建简单的密码，或者把密码写下来。

Keychain services 通过提供对加密存储的简便访问，帮助解决了这个问题。你的 App 使用钥匙串，并结合最少的用户交互，来提供良好的用户体验。例如，考虑图 1 中描述的那种用于存储互联网密码的流程。

![](../../../attachments/6e130349e0acca782d2d0c7dbcb81660/media-2928527@2x.png)

<sub>一个流程图，描绘了在可能的情况下使用钥匙串条目来认证服务器，并在找不到钥匙串条目或条目过期时提示用户的流程。</sub>

### 在需要时让用户参与

App 首次需要凭证时，钥匙串中没有存储密码。此时，如图中右侧分支所示，App 会提示用户。

当用户提供了成功通过认证的凭证后，App 会调用 [SecItemAdd](<secitemadd(____).md>) 函数将其存储起来。App 现在继续进行常规的网络访问。稍后，当服务器要求重新认证时，App 可以从钥匙串中检索凭证，而无需打扰用户。

有关如何向钥匙串添加条目的更多信息，请参阅[向钥匙串添加密码](adding-a-password-to-the-keychain.md)。

### 在常见情况下避免打扰用户

流程图中最常见的路径是中间那条，它不需要用户交互。在此路径中，一个安全的网络资源需要定期重新认证，例如，因为用户离开一段时间后重新启动了 App。

作为回应，App 使用 [SecItemCopyMatching](<secitemcopymatching(____).md>) 函数在钥匙串中搜索密码。如果找到密码，并且 App 成功使用它进行认证，则 App 可以继续操作，无需用户参与。

有关如何进行搜索的详细信息，请参阅[搜索钥匙串条目](searching-for-keychain-items.md)。

### 优雅地处理变更

有时，用户会在 App 的范畴之外更改凭证。例如，你可能为同一服务提供了一个 Web 界面，允许用户更改或重置其密码。在这种情况下，随后在 App 中搜索钥匙串条目会得到一个过期的密码，从而导致认证失败。流程图左侧的分支处理了这种情况。与右侧分支类似，App 会提示用户输入新凭证。但在这种情况下，App 在验证新凭证后，会调用 [SecItemUpdate](<secitemupdate(____).md>) 函数来修改现有的存储值。

用户也可能决定完全断开与该网络服务的连接。作为回应，你的 App 应该“忘掉”相应的凭证，同时执行登出所需的任何其他操作。使用 [SecItemDelete](<secitemdelete(__).md>) 函数从钥匙串中完全移除密码。

有关更改和移除现有条目的讨论，请参阅[更新和删除钥匙串条目](updating-and-deleting-keychain-items.md)。

## 主题

### 条目创建与修改

- [向钥匙串添加密码](adding-a-password-to-the-keychain.md) — 代表用户向钥匙串添加网络凭证。
- [搜索钥匙串条目](searching-for-keychain-items.md) — 根据你指定的搜索条件查找钥匙串条目。
- [更新和删除钥匙串条目](updating-and-deleting-keychain-items.md) — 当用户数据发生变化时，修改钥匙串中的条目。

### 条目访问

- [在一组 App 间共享钥匙串条目的访问权限](sharing-access-to-keychain-items-among-a-collection-of-apps.md) — 通过将 App 添加到一个访问组（access group），使其能够彼此共享钥匙串条目。
- [限制钥匙串条目的可访问性](restricting-keychain-item-accessibility.md) — 设置 App 可以访问钥匙串条目（例如密码）的条件。
