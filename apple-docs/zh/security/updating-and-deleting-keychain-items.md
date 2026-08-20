---
title: 更新和删除钥匙串项目
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/updating-and-deleting-keychain-items
source_url: 'https://developer.apple.com/documentation/security/updating-and-deleting-keychain-items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/updating-and-deleting-keychain-items.json'
content_hash: 'sha256:eec74b57a72e1d3a'
translated: true
---

> 导航：[技术](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [钥匙串项目](keychain-items.md)

# 更新和删除钥匙串项目

<sub>文章</sub>

在用户数据发生变化时修改钥匙串中的项目。

## 概述

当用户在你的 App 流程之外更改了 App 存储在钥匙串中的密码时，你可能只有在使用该密码进行认证失败时才会发现这一更改。作为响应，你的 App 会提示用户提供新的凭证，并更新钥匙串以反映这一更改。

在此过程中，如果你尝试调用 [SecItemAdd](<secitemadd(____).md>) 函数来存储新的一组凭证，可能会发现操作失败。当主要特性与现有项目相同时，新项目无法与旧项目在钥匙串中共存。即使某个主要特性（如用户名）确实发生了更改，且添加操作成功，最终也会使钥匙串中充满陈旧、被遗弃的项目。这些项目可能很难与你实际需要的项目区分开来。为了避免这些问题，请改为更新现有项目。

### 准备搜索查询和新特性

要更新钥匙串项目，首先需要找到它们。因此，更新操作从一次隐式搜索开始，就像 [SecItemCopyMatching](<secitemcopymatching(____).md>) 函数显式执行的那样。与显式搜索一样，你通过创建一个查询字典来控制这次隐式搜索：

```swift
let query: [String: Any] = [kSecClass as String: kSecClassInternetPassword,
                            kSecAttrServer as String: server]
```

这个特定查询表示搜索与你的 `server` 关联的互联网密码。请注意，这会匹配（并更新）你已存储的所有此类密码。如果你将钥匙串用于其他存储，可能需要进一步限定此搜索，以确保只影响你关心的项目。由于你并非在检索数据，因此无需指定返回类型。

除了提供搜索查询，你还需要提供第二个字典来描述所需的更改。你可以使用 [kSecValueData](ksecvaluedata.md) 键提供新的项目数据，例如用于更改存储的密码。并且你可以更改项目的特性——例如，通过使用 [kSecAttrAccount](ksecattraccount.md) 键来更新账户：

```swift
let account = credentials.username
let password = credentials.password.data(using: String.Encoding.utf8)!
let attributes: [String: Any] = [kSecAttrAccount as String: account,
                                 kSecValueData as String: password]
```

你提供用户给出的用户名和密码，通过一个 `C``redentials` 实例传递。即使用户名恰好与现有值相同，只有密码数据发生了更改，这也是没问题的。

### 执行更新

使用搜索查询和新特性，调用 [SecItemUpdate](<secitemupdate(____).md>) 函数：

```swift
let status = SecItemUpdate(query as CFDictionary, attributes as CFDictionary)
guard status != errSecItemNotFound else { throw KeychainError.noPassword }
guard status == errSecSuccess else { throw KeychainError.unhandledError(status: status) }
```

请务必检查调用返回的状态，并处理所有失败情形。如果调用成功，它会根据你提供的特性修改所有匹配的项目。

### 删除不再需要的项目

如果用户决定在你的 App 内从你的服务器登出，你可能需要作为该过程的一部分从钥匙串中删除密码项目。删除项目与更新它非常相似，不同之处在于它只需要查询字典。你可以使用前面定义的相同查询，这次调用 [SecItemDelete](<secitemdelete(__).md>) 函数：

```swift
let status = SecItemDelete(query as CFDictionary)
guard status == errSecSuccess || status == errSecItemNotFound else { throw KeychainError.unhandledError(status: status) }
```

默认情况下，钥匙串服务（Keychain services）会删除所有与搜索参数匹配的钥匙串项目。如果你想要删除一个你已经拥有其引用或持久引用的特定项目，请将其以 [kSecMatchItemList](ksecmatchitemlist.md) 键的值形式添加到搜索字典中。通过这种方式，你将删除操作限制为仅指定的项目。
