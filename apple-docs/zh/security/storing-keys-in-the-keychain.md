---
title: 在钥匙串中储存密钥
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/storing-keys-in-the-keychain
source_url: 'https://developer.apple.com/documentation/security/storing-keys-in-the-keychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/storing-keys-in-the-keychain.json'
content_hash: 'sha256:ece27bf0aeae824d'
translated: true
---

> 导航：[技术](../technologies.md) · [安全性](../security.md) · [证书、密钥与信任服务](certificate-key-and-trust-services.md) · [密钥](keys.md)

# 在钥匙串中储存密钥

<sub>文章</sub>

在钥匙串中储存和访问加密密钥。

## 概述

钥匙串（Keychain）是储存小型机密（如密码和加密密钥）的最佳位置。你可以使用钥匙串服务 API 的函数来添加、检索、删除或修改钥匙串条目。

关于如何储存使用 [Apple CryptoKit](../cryptokit.md) 框架创建的加密密钥，请参阅[在钥匙串中储存 CryptoKit 密钥](../cryptokit/storing-cryptokit-keys-in-the-keychain.md)。

### 创建查询字典

当你按照[生成新的加密密钥](generating-new-cryptographic-keys.md)所述自行生成密钥时，可以将密钥作为该过程的一部分隐式存储在钥匙串中。如果你通过其他方式获得了密钥，仍然可以将其存入钥匙串。为此，请先创建一个包含并描述该条目的查询字典：

**Swift**

```swift
let key = <# a key #>
let tag = "com.example.keys.mykey".data(using: .utf8)!
let addquery: [String: Any] = [kSecClass as String: kSecClassKey,
                               kSecAttrApplicationTag as String: tag,
                               kSecValueRef as String: key]
```

**Objective-C**

```objc
SecKeyRef key = <# a key #>;
NSData* tag = [@"com.example.keys.mykey" dataUsingEncoding:NSUTF8StringEncoding];
NSDictionary* addquery = @{ (id)kSecValueRef: (__bridge id)key,
                            (id)kSecClass: (id)kSecClassKey,
                            (id)kSecAttrApplicationTag: tag,
                           };
```

这个查询字典使用 [kSecClassKey](ksecclasskey.md) 作为 [kSecClass](ksecclass.md) 条目的值，以指明这是一个密钥条目（而非证书、身份或密码）。你还应用了一个 App 标签（application tag），以便在后续搜索时将该密钥与其他密钥区分开来。

### 储存条目

使用 [SecItemAdd](<secitemadd(____).md>) 函数来实际储存条目：

**Swift**

```swift
let status = SecItemAdd(addquery as CFDictionary, nil)
guard status == errSecSuccess else { throw <# an error #> }
```

**Objective-C**

```objc
OSStatus status = SecItemAdd((__bridge CFDictionaryRef)addquery, NULL);
if (status != errSecSuccess) { <# Handle the error #> }
else                         { <# Use the key #> }
```

### 检索条目

当你想检索密钥时，使用相同的 App 标签构建另一个查询字典：

**Swift**

```swift
let getquery: [String: Any] = [kSecClass as String: kSecClassKey,
                               kSecAttrApplicationTag as String: tag,
                               kSecAttrKeyType as String: kSecAttrKeyTypeRSA,
                               kSecReturnRef as String: true]
```

**Objective-C**

```objc
NSDictionary *getquery = @{ (id)kSecClass: (id)kSecClassKey,
                            (id)kSecAttrApplicationTag: tag,
                            (id)kSecAttrKeyType: (id)kSecAttrKeyTypeRSA,
                            (id)kSecReturnRef: @YES,
                         };
```

上述字典指明密钥类型应为 [kSecAttrKeyTypeRSA](ksecattrkeytypersa.md)（如[创建非对称密钥对](generating-new-cryptographic-keys.md#Creating-an-Asymmetric-Key-Pair)中所述），并且应使用该示例及上文所用的标签。最后一行指明检索应返回一个密钥引用（而不是密钥的实际数据）。

> [!note] 注意
> 这是一个简单的查询，其搜索细化程度可能不如你所愿。有关其他细化方式，请参见下方的[细化搜索](storing-keys-in-the-keychain.md#Refine-the-Search)。

你可以将此查询与 [SecItemCopyMatching](<secitemcopymatching(____).md>) 函数配合使用，以执行搜索并填充你提供的空引用：

**Swift**

```swift
var item: CFTypeRef?
let status = SecItemCopyMatching(query as CFDictionary, &item)
guard status == errSecSuccess else { throw <# an error #> }
let key = item as! SecKey
```

**Objective-C**

```objc
SecKeyRef key = NULL;
OSStatus status = SecItemCopyMatching((__bridge CFDictionaryRef)getquery,
                                      (CFTypeRef *)&key);
if (status!=errSecSuccess) { <# Handle the error #> }
else                       { <# Use the key #> }
	 
if (key) { CFRelease(key); }  // After you are done with it
```

如果调用成功（由状态结果指示），你就可以使用返回的密钥引用执行加密操作。在 Objective-C 中，你负责释放通过这种方式检索到的任何密钥的内存。在 Swift 中，系统会管理对象的内存。

### 细化搜索

上面示例中的查询并未将搜索限制为特定的密钥类别（公钥、私钥或对称密钥）或任何其他密钥特性。它仅匹配标签和类型，并返回第一个成功匹配的结果。除非你对给定类型的所有密钥都使用唯一的标签，否则在运行搜索时可能无法获得你正在寻找的密钥。这是因为只返回第一个匹配的密钥，它可能是也可能不是你想要的。

有几种方法可以处理这种情况。例如，你可以：

- **扩大搜索范围。** 如果你向查询字典中添加 [kSecMatchLimit](ksecmatchlimit.md) 条目，并将其值设为 [kSecMatchLimitAll](ksecmatchlimitall.md)，那么 [SecItemCopyMatching](<secitemcopymatching(____).md>) 将生成一个密钥引用数组（而不是单个密钥引用），你可以通过检查该数组来找到所需的密钥。
- **缩小搜索范围。** 如果你有其他属性（例如密钥大小或密钥类别）来区分你的密钥，请在搜索前向查询字典中添加相应的条目。
- **从一开始就避免重复使用标签。** 在添加具有特定标签和类型（或任何其他区分特征）的密钥之前，先从钥匙串中读取具有相同特征的现有密钥。如果发现潜在的重复项，要么重用原始密钥并跳过创建新密钥，要么使用不同的标签创建新密钥，要么在添加新密钥之前使用 [SecItemDelete](<secitemdelete(__).md>) 函数删除旧密钥。
