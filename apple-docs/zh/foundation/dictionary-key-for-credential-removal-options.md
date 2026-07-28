---
title: 凭证移除选项的字典键
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dictionary-key-for-credential-removal-options
source_url: 'https://developer.apple.com/documentation/foundation/dictionary-key-for-credential-removal-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dictionary-key-for-credential-removal-options.json'
content_hash: 'sha256:2977e488c1ff6c7c'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [URL 加载系统](url-loading-system.md) · [URLCredentialStorage](urlcredentialstorage.md)

# 凭证移除选项的字典键

<sub>API 集合</sub>

传递给 [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>) 的选项字典所使用的键。

## 主题

### 选项

- [NSURLCredentialStorageRemoveSynchronizableCredentials](nsurlcredentialstorageremovesynchronizablecredentials.md) — 对应值是表示布尔值的 `NSNumber` 对象，用于指示是否应移除包含 [NSURLCredentialPersistenceSynchronizable](urlcredential/persistence-swift.enum/synchronizable.md) 特性（attribute）的凭证。

## 另请参阅

### 添加和移除凭证

- [- removeCredential:forProtectionSpace:](<urlcredentialstorage/remove(__for_).md>) — 从指定保护空间的凭证存储中移除指定凭证。
- [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>) — 使用给定选项，从指定保护空间的凭证存储中移除指定凭证。
- [- removeCredential:forProtectionSpace:options:task:](<urlcredentialstorage/remove(__for_options_task_).md>) — 代表给定任务并使用给定选项，从指定保护空间的凭证存储中移除指定凭证。
- [- setCredential:forProtectionSpace:](<urlcredentialstorage/set(__for_).md>) — 向指定保护空间的凭证存储添加凭证。
- [- setCredential:forProtectionSpace:task:](<urlcredentialstorage/set(__for_task_).md>) — 代表指定任务，向指定保护空间的凭证存储添加凭证。
