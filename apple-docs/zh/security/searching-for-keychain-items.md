---
title: 搜索钥匙串条目
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/searching-for-keychain-items
source_url: 'https://developer.apple.com/documentation/security/searching-for-keychain-items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/searching-for-keychain-items.json'
content_hash: 'sha256:f4edf04c851d172f'
translated: true
---

> 导航：[技术](../technologies.md) · [Security](../security.md) · [钥匙串服务](keychain-services.md) · [钥匙串条目](keychain-items.md)

# 搜索钥匙串条目

<sub>文章</sub>

根据你指定的搜索条件查找钥匙串条目（keychain items）。

## 概述

你可以使用查询字典来查找钥匙串条目，该字典告诉钥匙串服务 API 要查找哪些条目特性（attribute），以及在找到匹配项时返回什么。查询字典还允许你指定额外的参数来优化搜索。例如，你可以在匹配字符串特性时控制大小写敏感性，或限制匹配数量。

以执行搜索为例，考虑存储于[将密码添加到钥匙串](adding-a-password-to-the-keychain.md)中的密码条目。在为网络服务提供凭据（由你的 App 存储）后，用户使用你的 App 一段时间，然后转而处理其他事情。当用户返回时，你的 App 可能需要重新向服务器进行身份验证才能继续工作。这次，App 从钥匙串加载密码，而不是用登录视图打扰用户。

### 创建搜索查询

通过构建查询字典开始搜索：

```swift
let query: [String: Any] = [kSecClass as String: kSecClassInternetPassword,
                            kSecAttrServer as String: server,
                            kSecMatchLimit as String: kSecMatchLimitOne,
                            kSecReturnAttributes as String: true,
                            kSecReturnData as String: true]
```

此查询搜索具有 `server` 特性的互联网密码条目，该特性与你之前添加密码条目时使用的 `server` 特性相匹配。查询还使用 [kSecMatchLimit](ksecmatchlimit.md) 搜索参数将结果限制为单个值（这实际上是默认行为）。如果存在，你只会收到钥匙串中找到的第一个匹配项。

最后，查询从密码条目请求其特性和数据。两者都需要，因为 [kSecAttrAccount](ksecattraccount.md) 特性包含用户名，而条目的数据包含密码本身。

> [!note] 注意
> 默认情况下，你的 App 可以自由检索自己的钥匙串条目，但不能检索其他 App 的条目。然而，钥匙串服务确实提供了扩大或缩小这种可访问性的机制，例如使用 [kSecAttrAccessGroup](ksecattraccessgroup.md) 特性。

### 发起搜索

创建查询字典后，你通过调用 [SecItemCopyMatching](<secitemcopymatching(____).md>) 函数来发起搜索：

```swift
var item: CFTypeRef?
let status = SecItemCopyMatching(query as CFDictionary, &item)
guard status != errSecItemNotFound else { throw KeychainError.noPassword }
guard status == errSecSuccess else { throw KeychainError.unhandledError(status: status) }
```

与许多 Security 框架函数一样，你首先测试返回的状态值。除此之外，如果未找到匹配项，可能会发生错误——例如，因为你之前没有为给定的 `server` 存储密码。如果发生错误，你会收到 [errSecItemNotFound](errsecitemnotfound.md) 结果，你可能希望将该结果与一般错误区别对待。事实上，检测到此错误是在存储任何内容之前，识别你正在首次经历 App 登录流程的一种方法。

当搜索成功时，[SecItemCopyMatching](<secitemcopymatching(____).md>) 函数通过其 `item` 参数提供结果。返回项的类型取决于查询的性质，如[条目返回结果键](item-return-result-keys.md)中所述。

### 提取结果

因为在搜索中你请求了多种返回类型并只允许单个结果，所以你应当期望结果是一个字典。你从与 [kSecAttrAccount](ksecattraccount.md) 键关联的特性值中恢复用户名。同时，你使用 [kSecValueData](ksecvaluedata.md) 键提取密码数据，然后将其转换为字符串：

```swift
guard let existingItem = item as? [String : Any],
    let passwordData = existingItem[kSecValueData as String] as? Data,
    let password = String(data: passwordData, encoding: String.Encoding.utf8),
    let account = existingItem[kSecAttrAccount as String] as? String
else {
    throw KeychainError.unexpectedPasswordData
}
let credentials = Credentials(username: account, password: password)
```

如果在执行搜索时，你将与 [kSecMatchLimit](ksecmatchlimit.md) 键关联的值设置为大于 1 的整数，则返回的项是一个数组，其条目数限制为你设置的值。该数组中的每个条目的格式与你将匹配项限制为一个时获得的裸字典相同。如果你为 [kSecMatchLimit](ksecmatchlimit.md) 键指定 [kSecMatchLimitAll](ksecmatchlimitall.md)，则数组大小仅受钥匙串中找到的匹配项数量限制。

> [!note] 注意
> 复制密码条目时，不能同时使用 [kSecReturnData](ksecreturndata.md) 和 [kSecMatchLimitAll](ksecmatchlimitall.md) 选项，因为复制每个密码条目可能需要额外的身份验证。相反，请请求条目的引用或持久引用，然后仅请求你实际需要的特定密码的数据。

当你确实获得结果数组时，你可能需要遍历数组以查找单个感兴趣的条目。你可以通过检查其他条目特性（例如帐户、创建日期或标签（label））来做到这一点。另一方面，如果你事先知道一个区分特征，那么通常更有效的方法是在初始钥匙串搜索查询中使用相应的特性进行缩减。

是否需要处理多个匹配项完全取决于你的 App 如何使用钥匙串。如果你允许用户在运行时在多个身份之间进行选择，你可能希望为单个服务器存储多个密码，然后让用户使用存储的帐户作为选择键在搜索结果中进行选择。其他时候，你可能决定将搜索过滤到单个结果，而不涉及用户。如果你采用这种方法，请确保你不会在钥匙串中创建相似的条目——而是测试并删除或修改现有条目。有关更多详细信息，请参阅[更新和删除钥匙串条目](updating-and-deleting-keychain-items.md)。
