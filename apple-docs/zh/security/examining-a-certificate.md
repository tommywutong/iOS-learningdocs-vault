---
title: 检查证书
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/examining-a-certificate
source_url: 'https://developer.apple.com/documentation/security/examining-a-certificate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/examining-a-certificate.json'
content_hash: 'sha256:a69b5f24ff04a4e2'
translated: true
---

> 导航：[技术](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Certificates](certificates.md)

# 检查证书

<sub>文章</sub>

了解如何从证书中获取属性。

## 概述

为了验证其所有者的身份，证书包含如下信息：

- 证书颁发者
- 证书持有者
- 有效期（证书在此期限前后均无效）
- 证书所有者的公钥
- _证书扩展（Certificate Extensions）_，包含附加信息，例如证书持有者的备用名称以及证书相关私钥的允许用途
- 来自证书颁发机构的数字签名，以确保证书未被篡改，并指明颁发者的身份

证书、密钥与信任服务（Certificate, Key, and Trust Services）API 提供了检查证书属性的函数。例如，[SecCertificateCopySubjectSummary](<seccertificatecopysubjectsummary(__).md>) 函数返回证书的人类可读摘要：

**Swift**

```swift
let certificate = <# a certificate #>
let summary = SecCertificateCopySubjectSummary(certificate) as String
print("Cert summary: \(summary)")
```

**Objective-C**

```objc
SecCertificateRef certificate = <# a certificate #>;
NSString* summary = (NSString*)CFBridgingRelease(  // ARC takes ownership
                       SecCertificateCopySubjectSummary(certificate)
                    );
NSLog(@"Cert summary: %@", summary);
```

在 macOS 中，有几个额外的函数用于返回有关证书的数据。例如，要从证书中提取公钥，你可以使用 [SecCertificateCopyPublicKey](<seccertificatecopypublickey(__).md>) 函数：

**Swift**

```swift
var publicKey: SecKey?
let status = SecCertificateCopyPublicKey(certificate, &publicKey)
guard status == errSecSuccess else { throw <# an error #> }
```

**Objective-C**

```objc
SecKeyRef publicKey = NULL;
OSStatus status = SecCertificateCopyPublicKey(certificate, &publicKey);
if (status != errSecSuccess) { <# Handle error #> }
else                         { <# Use key #> }
 
if (publicKey) { CFRelease(publicKey); }  // After you are done with it
```
