---
title: 为局域网 TLS 创建身份
framework: Network
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/creating-an-identity-for-local-network-tls
source_url: 'https://developer.apple.com/documentation/network/creating-an-identity-for-local-network-tls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/creating-an-identity-for-local-network-tls.json'
content_hash: 'sha256:4d64117b44852c66'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md)

# 为局域网 TLS 创建身份

<sub>文章</sub>

了解如何在你的 App 中创建和使用数字身份（digital identity）用于局域网 TLS。

## 概述

在传输层安全（Transport Layer Security, TLS）的上下文中，**数字身份**是一种加密资产，它包含一个证书（certificate）和一个关联的私钥（private key），用于加密客户端和服务器之间发送的网络流量。为 iOS 或 macOS 创建数字身份后，客户端就能通过互联网或局域网使用 TLS 进行通信。

在此场景中，服务器接受局域网上的客户端连接。虽然本文主要关注局域网 TLS，但你可以将其中许多概念应用于其他用例。例如，使用从第三方证书颁发机构（Certificate Authority）获得的证书来设置 TLS，或配置任何需要建立到根证书（root certificate）信任链的系统。

### 准备环境

假设你在构建一个用于处理餐厅订单的 App。此 App 运行在前台服务器设备上——比如一台 iPad 或 Mac。在餐厅各处，顾客使用 iOS 客户端设备创建订单并发送到服务器进行处理。在这种情况下，服务器使用来自本地证书颁发机构的数字身份，为客户端提供 TLS。下文将说明如何在服务器和客户端设备上设置局域网 TLS。

要为局域网 TLS 创建身份，首先需要创建和管理一个本地证书颁发机构（Certificate Authority, CA）。CA 是受信任的实体（entity），负责颁发用于加密操作的证书。在本例中，CA 作为受信任的权威来源，颁发用于 TLS 数字身份的证书。如果没有这个受信任的权威，客户端将无法验证其所用证书的颁发者。

创建 CA 后，你需要为安装在服务器上的数字身份颁发一个叶子证书（leaf certificate）。接着，你需要将身份分发给服务器。在餐厅示例中，这可以是充当服务器的 macOS 或 iOS 设备。最后，你还需要将根证书分发给餐厅网络中的所有 iOS 客户端设备，以便它们在握手（handshake）过程中建立信任链，且无需覆盖信任评估（trust evaluation）。

整个流程概述如下：

1. 使用 macOS 上的“钥匙串访问”（Keychain）App 创建和管理你自己的证书颁发机构。
2. 将身份分发给服务器。在 macOS 上，可以在运行服务器的同一台机器上创建并使用身份，或者将 PKCS#12 文件安全地分发到设备钥匙串。在 iOS 上，将 PKCS#12 文件导入到服务器设备。例如，你可以将 PKCS#12 文件放在 U 盘上，导入到 iOS 服务器 App 中，并保存到钥匙串。
3. 在 iOS 客户端设备上，安装根证书以形成信任链。

### 将身份分发给服务器

在 iOS 上，证书颁发机构所有者面临将身份分发给服务器的挑战。将身份传输到服务器后——无论是通过 U 盘还是安全的网络传输——将其保存到钥匙串。要保存身份到 iOS 钥匙串，请使用以下代码：

```swift
let password = <# A password from the Keychain #>
let options = [kSecImportExportPassphrase: password ] as NSDictionary
var rawItems: CFArray?
let status = SecPKCS12Import(data as CFData, // Data from imported Identity.
                             options as CFDictionary,
                             &rawItems)

guard status == errSecSuccess,
      let items = rawItems,
      let dictionaryItems = items as? Array<Dictionary<String, Any>> else {
    // 处理错误 …
}

let secIdentity: SecIdentity = dictionaryItems[0][kSecImportItemIdentity as String] as! SecIdentity

// 请注意，这里没有使用 kSecClass as String: kSecClassIdentity，因为会根据 kSecValueRef 推断。
let identityAddition = [
    kSecValueRef: secIdentity,
    kSecAttrLabel: "ListenerIdentityLabel"
] as NSDictionary

let identityStatus = SecItemAdd(identityAddition as CFDictionary, nil)

guard identityStatus == errSecSuccess else {
    // 处理错误 …
}
// 身份添加成功。
```

要从 iOS 钥匙串中检索身份，请使用以下代码：

```swift
func getSecIdentity() -> SecIdentity? {

    // 在查询时，使用 kSecClassIdentity 以确保提取的是 SecIdentity。
    let identityQuery = [
        kSecClass: kSecClassIdentity,
        kSecReturnRef: true,
        kSecAttrLabel: "ListenerIdentityLabel"
    ] as NSDictionary
    var identityItem: CFTypeRef?
    let getIdentityStatus = SecItemCopyMatching(identityQuery as CFDictionary, &identityItem)

    guard getIdentityStatus == errSecSuccess else {
        // 处理错误 …
    }
    let secIdentity = identityItem as! SecIdentity
    return secIdentity
}
```

当本地身份可从钥匙串访问后，将其设置到 [NWListener](nwlistener.md) 以使用 TLS 1.2+ 提供连接服务，方法如下：

```swift
let tlsOptions = NWProtocolTLS.Options()
let tlsParams = NWParameters(tls: tlsOptions, tcp: .init())

if let secIdentity = getSecIdentity(),
   let identity = sec_identity_create(secIdentity) {
    sec_protocol_options_set_min_tls_protocol_version(
        tlsOptions.securityProtocolOptions, .TLSv12)
    sec_protocol_options_set_local_identity(
        tlsOptions.securityProtocolOptions, identity)
} 
let listener = try NWListener(using: tlsParams, on: 4433)
```

在 macOS 上，代码基本相同，但如果 `NWListener` 运行在设置了本地证书颁发机构的同一台机器上，则 App 的代码可以通过从钥匙串中的 [SecCertificate](../security/seccertificate.md) 加载引用来引用该身份。要从 macOS 上的钥匙串中检索身份，请使用以下代码：

```swift
func getSecIdentity() -> SecIdentity? {

    var identity: SecIdentity?
    let getquery = [kSecClass: kSecClassCertificate,
        kSecAttrLabel: "certificate_name_in_keychain",
        kSecReturnRef: true] as NSDictionary

    var item: CFTypeRef?
    let status = SecItemCopyMatching(getquery as CFDictionary, &item)
    guard status == errSecSuccess else {
        // 处理错误 …
    }
    let certificate = item as! SecCertificate

    let identityStatus = SecIdentityCreateWithCertificate(nil, certificate, &identity)
    guard identityStatus == errSecSuccess else {
        // 处理错误 …
    }
    return identity
}
```

在 macOS 上加载身份后，你可以使用与 iOS 完全相同的 `NWListener` 代码。

### 配置客户端设备

对于连接到服务器的客户端，请在客户端设备上安装根证书，以避免覆盖信任评估。在客户端设备上安装根证书后，客户端使用局域网名称连接到服务器。从客户端侧进行连接时，请使用以下代码：

```swift
let tlsOptions = NWProtocolTLS.Options()
sec_protocol_options_set_min_tls_protocol_version(
    tlsOptions.securityProtocolOptions, 
    .TLSv12)

let tlsParams = NWParameters(tls: tlsOptions, tcp: .init())

let endpoint = NWEndpoint.hostPort(host: "listener-name.local", port: 4433)
let connection = NWConnection(to: endpoint, using: tlsParams)
```

> [!note] 注意
> 如果来自 CA 的根证书已安装在设备上，你可以直接使用上述代码，无需实现 [sec_protocol_options_set_verify_block(_:_:_:)](<../security/sec_protocol_options_set_verify_block(______).md>) 来覆盖信任评估。

如果你的客户端需要通过 IP 连接，而不是使用局域网名称，则服务器需要使用一个叶子证书，该证书在主题备用名称（Subject Alternative Name）的“IP Address”字段中列出该 IP。这也避免了在客户端覆盖信任评估，并允许客户端连接使用以下代码：

```swift
let tlsOptions = NWProtocolTLS.Options()
sec_protocol_options_set_min_tls_protocol_version(
    tlsOptions.securityProtocolOptions, 
    .TLSv12)

let tlsParams = NWParameters(tls: tlsOptions, tcp: .init())

let endpoint = NWEndpoint.hostPort(host: "x.x.x.x", port: 4433)
let connection = NWConnection(to: endpoint, using: tlsParams)
```

尝试从客户端连接到未在客户端 iOS 设备上安装根证书的服务器，会导致类似于以下的应用程序错误：

```
// [BoringSSL] boringssl_context_error_print(1863) boringssl ctx 0x2813acbe0: 4348594328:error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED
// [BoringSSL] boringssl_session_handshake_incomplete(164) [C1:1][0x1032186d0] SSL library error
```

> [!note] 注意
> 如果叶子证书的主题备用名称字段中缺少 IP 地址或 DNS 名称，同样会出现此问题。

要在客户端解决此问题，可以使用 `sec_protocol_options_set_verify_block` 来执行你自己的对等方叶子证书验证检查。这不是推荐的做法，但在极端情况下可以采用。在以下示例中，[SecPolicyCreateBasicX509()](<../security/secpolicycreatebasicx509().md>) 根据证书的基本 x509 策略进行检查：

```swift
sec_protocol_options_set_verify_block(tlsOptions.securityProtocolOptions, { (_, trust, completionHandler) in
    let secTrustRef = sec_trust_copy_ref(trust).takeRetainedValue() as SecTrust

    // 由于是 IP，无法在这里进行主机名验证。
    let x509Policy = SecPolicyCreateBasicX509()
    SecTrustSetPolicies(secTrustRef, x509Policy)

    var error: CFError?
    if !SecTrustEvaluateWithError(secTrustRef, &error) {
        completionHandler(false)
    }
    // 执行其他基于证书的检查。  

    completionHandler(true)
}, .main)
```

至此，客户端就可以在局域网上使用 TLS 建立握手连接了。

## 另请参阅

### 网络安全与隐私

- [安全选项](security-options.md) — 配置 TLS 握手的安全选项。
- [隐私管理](privacy-management.md) — 配置与用户隐私相关的参数。
