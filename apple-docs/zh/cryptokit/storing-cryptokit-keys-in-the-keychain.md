---
title: 在钥匙串中储存 CryptoKit 密钥
framework: Apple CryptoKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, Xcode 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/storing-cryptokit-keys-in-the-keychain
source_url: 'https://developer.apple.com/documentation/cryptokit/storing-cryptokit-keys-in-the-keychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/storing-cryptokit-keys-in-the-keychain.json'
content_hash: 'sha256:e9a383aaede9fb34'
translated: true
---

> 导航：[技术](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# 在钥匙串中储存 CryptoKit 密钥

<sub>示例代码</sub>

在强类型的加密密钥和原生钥匙串类型之间进行转换。

## 概述

CryptoKit 定义了高度具体的密钥类型，这些类型体现了特定的加密算法和用途。其中一些密钥类型，例如 [`P256.Signing.PrivateKey`](p256/signing/privatekey.md)，对应于 [Keychain Services](../security/keychain-services.md) API 原生以 [`SecKey`](../security/seckey.md) 实例储存的条目。其他密钥类型，例如 [`Curve25519.Signing.PrivateKey`](curve25519/signing/privatekey.md)，在钥匙串（Keychain）中没有直接的对应项。要储存这些类型的密钥，你可以将它们打包为通用密码。

这个示例代码项目演示了将所有 CryptoKit 密钥类型储存到钥匙串所需的转换。

### 配置示例代码项目

该示例提供了 iOS 和 macOS 的目标。对于这两个平台，在构建之前，请在 Xcode 的“签名与功能（Signing & Capabilities）”标签页中指定你的开发团队。macOS 目标还设置了 [Keychain Access Groups Entitlement](../bundleresources/entitlements/keychain-access-groups.md)，以允许在该平台上访问钥匙串。

### 声明 NIST 密钥的可转换性

[Keychain Services](../security/keychain-services.md) 允许你在 [`SecKey`](../security/seckey.md) 实例与 X9.63 数据格式的数据之间进行转换。对于支持该表示的 NIST 密钥，例如 [`P256`](p256.md)、[`P382`](p384.md) 和 [`P521`](p521.md)，CryptoKit 定义了一个属性（property），你可以使用它来获取 X9.63 数据。该框架还提供了一个补充的初始化方法，用于从该格式的数据创建新密钥。

定义一个名为 `SecKeyConvertible` 的协议（protocol）来表示这个接口：

```swift
protocol SecKeyConvertible: CustomStringConvertible {
    /// 从 X9.63 表示创建密钥。
    init<Bytes>(x963Representation: Bytes) throws where Bytes: ContiguousBytes
    
    /// 密钥的 X9.63 表示。
    var x963Representation: Data { get }
}
```

然后断言所有 NIST 私钥都采用了此协议：

```swift
extension P256.Signing.PrivateKey: SecKeyConvertible {}
extension P256.KeyAgreement.PrivateKey: SecKeyConvertible {}
extension P384.Signing.PrivateKey: SecKeyConvertible {}
extension P384.KeyAgreement.PrivateKey: SecKeyConvertible {}
extension P521.Signing.PrivateKey: SecKeyConvertible {}
extension P521.KeyAgreement.PrivateKey: SecKeyConvertible {}
```

### 声明其他密钥类型的可转换性

[Keychain Services](../security/keychain-services.md) 还允许你将小块数据安全地储存为通用密码钥匙串条目。对于任何没有 X9.63 表示的 CryptoKit 密钥，CryptoKit 提供了一种获取该密钥数据表示的方法，从而实现通用密码储存。定义 `GenericPasswordConvertible` 协议来为这些条目建立一个接口：

```swift
protocol GenericPasswordConvertible: CustomStringConvertible {
    /// 从通用密钥表示创建密钥。
    init<D>(genericKeyRepresentation data: D) throws where D: ContiguousBytes
    
    /// 密钥的通用表示。
    var genericKeyRepresentation: SymmetricKey { get }
}
```

某些密钥，例如 [`Curve25519`](curve25519.md)，直接采用了此接口，你只需断言它们采用了即可：

```swift
extension Curve25519.KeyAgreement.PrivateKey: GenericPasswordConvertible {
    init<D>(genericKeyRepresentation data: D) throws where D: ContiguousBytes {
        try self.init(rawRepresentation: data)
    }

    var genericKeyRepresentation: SymmetricKey {
        self.rawRepresentation.withUnsafeBytes {
            SymmetricKey(data: $0)
        }
    }
}
extension Curve25519.Signing.PrivateKey: GenericPasswordConvertible {
    init<D>(genericKeyRepresentation data: D) throws where D: ContiguousBytes {
        try self.init(rawRepresentation: data)
    }

    var genericKeyRepresentation: SymmetricKey {
        self.rawRepresentation.withUnsafeBytes {
            SymmetricKey(data: $0)
        }
    }
}
```

其他密钥提供了类似的功能，但需要对其接口进行适度的调整。例如，你为 [`SymmetricKey`](symmetrickey.md) 的实例提供了一个安全的转换：

```swift
extension SymmetricKey: GenericPasswordConvertible {
    init<D>(genericKeyRepresentation data: D) throws where D: ContiguousBytes {
        self.init(data: data)
    }
    
    var genericKeyRepresentation: SymmetricKey {
        self
    }
}
```

你储存在安全隔区（Secure Enclave）中的密钥也会暴露原始表示，但在这种情况下，数据并非原始密钥本身。相反，安全隔区会导出一个加密块，只有同一个安全隔区以后才能用它来恢复该密钥。你可以采用相同的可转换性协议，将安全隔区的加密数据作为通用密码储存在钥匙串中，随后允许安全隔区在同一设备上重建该密钥：

```swift
extension SecureEnclave.P256.Signing.PrivateKey: GenericPasswordConvertible {
    init<D>(genericKeyRepresentation data: D) throws where D: ContiguousBytes {
        try self.init(dataRepresentation: data.withUnsafeBytes { Data($0) })
    }

    var genericKeyRepresentation: SymmetricKey {
        return SymmetricKey(data: dataRepresentation)
    }
}
```

### 储存 NIST 密钥

要将 NIST 密钥储存在钥匙串中，请创建一个约束输入密钥类型为 `SecKeyConvertible` 的储存方法：

```swift
func storeKey<T: SecKeyConvertible>(_ key: T, label: String) throws {
```

然后使用密钥的 X9.63 表示调用 [`SecKeyCreateWithData(_:_:_:)`](<../security/seckeycreatewithdata(______).md>) 函数来创建一个 [`SecKey`](../security/seckey.md) 实例。同时包含描述该密钥为私有的椭圆曲线密钥的属性。

```swift
// 描述密钥。
let attributes = [kSecAttrKeyType: kSecAttrKeyTypeECSECPrimeRandom,
                  kSecAttrKeyClass: kSecAttrKeyClassPrivate] as [String: Any]

// 获取 SecKey 表示。
guard let secKey = SecKeyCreateWithData(key.x963Representation as CFData,
                                        attributes as CFDictionary,
                                        nil)
    else {
        throw KeyStoreError("Unable to create SecKey representation.")
}
```

将 [`SecKey`](../security/seckey.md) 表示放入添加查询中，并调用 [`SecItemAdd(_:_:)`](<../security/secitemadd(____).md>) 函数，从而将其储存在钥匙串中。为密钥提供一个标签，以便将来更容易找到它。

```swift
// 描述添加操作。
let query = [kSecClass: kSecClassKey,
             kSecAttrApplicationLabel: label,
             kSecAttrAccessible: kSecAttrAccessibleWhenUnlocked,
             kSecUseDataProtectionKeychain: true,
             kSecValueRef: secKey] as [String: Any]

// 将密钥添加到钥匙串。
let status = SecItemAdd(query as CFDictionary, nil)
guard status == errSecSuccess else {
    throw KeyStoreError("Unable to store item: \(status.message)")
}
```

### 在钥匙串中储存其他密钥类型

要储存其他类型的密钥，请创建一个不同的储存方法，该方法约束输入密钥的类型为 `GenericPasswordConvertible`：

```swift
func storeKey<T: GenericPasswordConvertible>(_ key: T, account: String) throws {
```

在这种情况下，你将原始表示作为密码条目的数据提供，并通过调用 [`SecItemAdd(_:_:)`](<../security/secitemadd(____).md>) 函数进行储存：

```swift
// 将密钥数据视为通用密码。
try key.genericKeyRepresentation.withUnsafeBytes { keyBytes in
    let cfd = Data(bytesNoCopy: UnsafeMutableRawPointer(mutating: keyBytes.baseAddress!), count: keyBytes.count, deallocator: .none)
    let query = [kSecClass: kSecClassGenericPassword,
                 kSecAttrAccount: account,
                 kSecAttrAccessible: kSecAttrAccessibleWhenUnlocked,
                 kSecUseDataProtectionKeychain: true,
                 kSecValueData: cfd] as [String: Any]

    // 添加密钥数据。
    let status = SecItemAdd(query as CFDictionary, nil)
    guard status == errSecSuccess else {
        throw KeyStoreError("Unable to store item: \(status.message)")
    }
}

```

### 以原生钥匙串密钥的形式检索 NIST 密钥

你可以通过调用 [`SecItemCopyMatching(_:_:)`](<../security/secitemcopymatching(____).md>) 函数从钥匙串中检索密钥。构建一个查询字典来精确定位你想要查找的特定密钥。当搜索返回目标密钥后——它以 [`SecKeychainItem`](../security/seckeychainitem.md) 实例的形式储存——你将其转换为 [`SecKey`](../security/seckey.md) 实例。

```swift
// 查找具有给定标签的椭圆曲线密钥。
let query = [kSecClass: kSecClassKey,
             kSecAttrApplicationLabel: label,
             kSecAttrKeyType: kSecAttrKeyTypeECSECPrimeRandom,
             kSecUseDataProtectionKeychain: true,
             kSecReturnRef: true] as [String: Any]

// 查找并将结果转换为 SecKey 实例。
var item: CFTypeRef?
var secKey: SecKey
switch SecItemCopyMatching(query as CFDictionary, &item) {
case errSecSuccess: secKey = item as! SecKey
case errSecItemNotFound: return nil
case let status: throw KeyStoreError("Keychain read failed: \(status.message)")
}
```

> [!note] 注意
> 上述查询返回在用户钥匙串中找到的第一个具有给定标签的椭圆曲线密钥。如果可能有多个密钥匹配，你可能需要执行更复杂的搜索，具体如[在钥匙串中储存密钥](../security/storing-keys-in-the-keychain.md)所述。

获取 [`SecKey`](../security/seckey.md) 引用后，使用由 [`SecKeyCopyExternalRepresentation(_:_:)`](<../security/seckeycopyexternalrepresentation(____).md>) 函数返回的 X9.63 表示来初始化一个 CryptoKit 密钥。

```swift
// 将 SecKey 转换为 CryptoKit 密钥。
var error: Unmanaged<CFError>?
guard let data = SecKeyCopyExternalRepresentation(secKey, &error) as Data? else {
    throw KeyStoreError(error.debugDescription)
}
let key = try T(x963Representation: data)
```

确保你使用数据初始化的密钥类型与原始密钥的类型匹配。例如，从对应使用 [`P256`](p256.md) 密钥创建的钥匙串条目的数据来初始化 [`P384`](p384.md) 密钥会产生未定义的结果。

### 检索储存为通用密码的密钥

你也可以使用 [`SecItemCopyMatching(_:_:)`](<../security/secitemcopymatching(____).md>) 函数检索通用密码，在这种情况下，要使用 [`kSecClassGenericPassword`](../security/ksecclassgenericpassword.md) 作为条目的类别。将返回的条目转换为数据，并直接用它来实例化相应类型的密钥：

```swift
// 查找具有给定帐户的通用密码。
let query = [kSecClass: kSecClassGenericPassword,
             kSecAttrAccount: account,
             kSecUseDataProtectionKeychain: true,
             kSecReturnData: true] as [String: Any]

// 查找并将结果转换为数据。
var item: CFTypeRef?
switch SecItemCopyMatching(query as CFDictionary, &item) {
case errSecSuccess:
    guard let data = item as? Data else { return nil }
    return try T(genericKeyRepresentation: data)  // Convert back to a key.
case errSecItemNotFound: return nil
case let status: throw KeyStoreError("Keychain read failed: \(status.message)")
}
```

只要初始化的类型与你之前用于在钥匙串中储存条目的类型匹配，初始化就会正确地重建密钥。

## 另请参阅

### 基础

- [遵守加密出口法规](../security/complying-with-encryption-export-regulations.md) — 在你的 App 中声明加密的使用，以简化 App 提交流程。
- [执行常见密码学操作](performing-common-cryptographic-operations.md) — 使用 CryptoKit 执行哈希、密钥生成和加密等操作。
- [使用量子安全工作流程提升 App 的隐私与安全](enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows.md) — 使用量子安全密码学保护你的 App 免受量子攻击。

## 下载

- [StoringCryptoKitKeysInTheKeychain.zip](https://docs-assets.developer.apple.com/published/e58b2aada138/StoringCryptoKitKeysInTheKeychain.zip)
