---
title: 使用密钥进行加密
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/using-keys-for-encryption
source_url: 'https://developer.apple.com/documentation/security/using-keys-for-encryption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/using-keys-for-encryption.json'
content_hash: 'sha256:edb54c04b8a58021'
translated: true
---

> 导航：[技术](../technologies.md) · [安全](../security.md) · [证书、密钥和信任服务](certificate-key-and-trust-services.md) · [密钥](keys.md)

# 使用密钥进行加密

<sub>文章</sub>

使用加密密钥执行非对称和对称加密与解密。

## 概述

密码学（Cryptography）使得通过不受信任的通道实现安全的数据交换成为可能。这一活动的重要组成部分之一是加密。发射器在链路的一端对数据进行编码，使任何没有解密密钥的人看到的数据都变得毫无意义。然后数据通过通道传输——暴露在外部世界中，但对于除预期接收者之外的所有人来说都毫无意义。该接收者，即解密密钥的唯一持有者，逆转加密过程以揭示原始消息。

与加密密钥一样，加密也有两种主要类型：

- **非对称加密（Asymmetric）。** 非对称加密不需要共享秘密。但另一方面，它的计算成本高，并且仅适用于小的、离散的数据块。因此，它最适合在发送方和接收方之间没有建立关系时的小批量传输。
- **对称加密（Symmetric）。** 对称加密适用于批量数据传输，因为它计算效率高，并且可以对数据流进行操作。但它仅在发送方和接收方共享一个秘密密钥时才有效。因此，你通常需要依赖其他技术（例如非对称加密或 Diffie-Hellman 密钥交换）来共享密钥并建立会话。

### 使用非对称加密

要执行非对称加密，发射器使用公钥加密其数据。只有匹配私钥的持有者才能解密被隐藏的消息。你首先需要获取与你预期接收者的私钥相对应的公钥。根据情况，你可以从钥匙串或证书中读取它，或者使用[获取现有密钥](getting-an-existing-key.md)中描述的其他方法之一。无论你如何获取密钥，你能执行的加密类型取决于密钥本身。

例如，考虑一个 2048 位的 RSA 密钥对，就像在[创建非对称密钥对](generating-new-cryptographic-keys.md#Creating-an-Asymmetric-Key-Pair)中生成的那种。接收者通过使用签名证书或其他受信任（但不一定安全）的通道，将公钥传输给发射器。发射器和接收者然后协商一个适合密钥对能力的适当加密算法（或依赖预先商定的算法）。在此例中，假设你选择这个 [kSecKeyAlgorithmRSAEncryptionOAEPSHA512](seckeyalgorithm/rsaencryptionoaepsha512.md) 算法：

**Swift**

```swift
let publicKey: SecKey = <# a key #>
let algorithm: SecKeyAlgorithm = .rsaEncryptionOAEPSHA512
```

**Objective-C**

```objc
SecKeyRef publicKey = <# a key #>;  // E.g., from a signed cert
SecKeyAlgorithm algorithm = kSecKeyAlgorithmRSAEncryptionOAEPSHA512;
```

此设置指定了使用 SHA512 哈希的最优非对称加密填充（OAEP）方案的 RSA 加密。所选算法必须适合密钥的能力。但是，与其信任该密钥能与算法一起工作，不如使用 [SecKeyIsAlgorithmSupported](<seckeyisalgorithmsupported(______).md>) 函数显式测试与 [kSecKeyOperationTypeEncrypt](seckeyoperationtype/encrypt.md) 操作的兼容性：

**Swift**

```swift
guard SecKeyIsAlgorithmSupported(publicKey, .encrypt, algorithm) else {
    throw <# an error #>
}
```

**Objective-C**

```objc
BOOL canEncrypt = SecKeyIsAlgorithmSupported(publicKey,
                                             kSecKeyOperationTypeEncrypt,
                                             algorithm);
```

如果密钥实际上不是 RSA 类型，或者 `publicKey` 引用实际上指向了一个私钥（尽管其名称如此），此调用可能返回 false。私钥通常将其 [kSecAttrCanEncrypt](ksecattrcanencrypt.md) 特性（attribute）设置为 false，标记为不适合加密。

作为加密前的额外检查，由于非对称加密限制了可加密数据的长度，请验证数据是否足够短。对于此特定算法，明文数据的大小必须比密钥的 block size（通过 [SecKeyGetBlockSize](<seckeygetblocksize(__).md>) 获取）小 130 个字节。因此，你进一步通过长度测试来确保操作条件：

**Swift**

```swift
guard (plainText.count < (SecKeyGetBlockSize(publicKey)-130)) else {
    throw <# an error #>
}
```

**Objective-C**

```objc
NSData* plainText = <# Data to encrypt #>;
canEncrypt &= ([plainText length] < (SecKeyGetBlockSize(publicKey)-130));
```

最后，你通过调用 [SecKeyCreateEncryptedData](<seckeycreateencrypteddata(________).md>) 函数进行加密：

**Swift**

```swift
var error: Unmanaged<CFError>?
guard let cipherText = SecKeyCreateEncryptedData(publicKey,
                                                 algorithm,
                                                 plainText as CFData,
                                                 &error) as Data? else {
                                                    throw error!.takeRetainedValue() as Error
}
```

**Objective-C**

```objc
NSData* cipherText = nil;
if (canEncrypt) {
    CFErrorRef error = NULL;
    cipherText = (NSData*)CFBridgingRelease(      // ARC takes ownership
                     SecKeyCreateEncryptedData(publicKey,
                                               algorithm,
                                               (__bridge CFDataRef)plainText,
                                               &error));
    if (!cipherText) {
        NSError *err = CFBridgingRelease(error);  // ARC takes ownership
        // 处理错误. . .
    }
}
```

尽管有预先检查，加密调用仍可能出错。当出错时，该函数返回 `nil` 密文，并产生一个指示失败原因的错误对象。在 Objective-C 中，你通过调用 [CFBridgingRelease](../foundation/cfbridgingrelease.md) 将错误对象的所有权（ownership）转移给自动引用计数（Automatic Reference Counting，ARC），并处理错误。在 Swift 中，你将可选的、非托管的 [CFError](../corefoundation/cferror.md) 转换为托管的 [Error](../swift/error.md) 并抛出它。

假设加密成功，你将 `cipherText` 数据对象通过通道发送给接收者。然后接收者使用其私钥解密数据。如[获取现有密钥](getting-an-existing-key.md)中所述，你通常从钥匙串或身份（identity，它本身可能存储在钥匙串中）获取对你的私钥的引用。你可以再次测试密钥的适用性，使用与之前相同的算法，但针对 [kSecKeyOperationTypeDecrypt](seckeyoperationtype/decrypt.md) 操作：

**Swift**

```swift
guard SecKeyIsAlgorithmSupported(privateKey, .decrypt, algorithm) else {
    throw <# an error #>
}
```

**Objective-C**

```objc
SecKeyRef privateKey = <# a key #>;  // From keychain or identity
BOOL canDecrypt = SecKeyIsAlgorithmSupported(privateKey,
                                             kSecKeyOperationTypeDecrypt,
                                             algorithm);
```

你同样可以测试长度，尽管在这种情况下，密文应该与密钥的 block size 长度相同，因为加密操作应该已经产生这个结果：

**Swift**

```swift
guard cipherText.count == SecKeyGetBlockSize(privateKey) else {
    throw <# an error #>
}
```

**Objective-C**

```objc
canDecrypt &= ([cipherText length] == SecKeyGetBlockSize(privateKey));
```

完成这些测试后，解密过程与加密非常相似，只是现在调用的是 [SecKeyCreateDecryptedData](<seckeycreatedecrypteddata(________).md>)：

**Swift**

```swift
var error: Unmanaged<CFError>?
guard let clearText = SecKeyCreateDecryptedData(privateKey,
                                                algorithm,
                                                cipherText as CFData,
                                                &error) as Data? else {
                                                    throw error!.takeRetainedValue() as Error
}
```

**Objective-C**

```objc
NSData* clearText = nil;
if (canDecrypt) {
    CFErrorRef error = NULL;
    clearText = (NSData*)CFBridgingRelease(       // ARC takes ownership
                     SecKeyCreateDecryptedData(privateKey,
                                               algorithm,
                                               (__bridge CFDataRef)cipherText,
                                               &error));
    if (!clearText) {
        NSError *err = CFBridgingRelease(error);  // ARC takes ownership
        // 处理错误. . .
    }
}
```

像以前一样，你处理好失败及相应的错误对象（如果适用）。如果调用成功，`clearText` 对象将与发射器的 `plainText` 对象完全匹配。

### 使用对称加密

当发送方和接收方共享一个单一的机密密钥时，他们可以执行对称加密，其中相同的密钥既加密又解密消息。尽管此情况下的操作计算效率高，但最初共享密钥本身就是一个挑战。因此，你通常会在开始通信时使用另一种方法（例如非对称加密）来交换对称密钥。

实际上，证书、密钥和信任服务 API 提供了一种简单的方法来实现这一点。你按照[使用非对称加密](using-keys-for-encryption.md#Use-Asymmetric-Encryption)中概述的所有步骤进行，仅需进行以下调整：

- **更改算法。** 当你选择 [kSecKeyAlgorithmRSAEncryptionOAEPSHA512AESGCM](seckeyalgorithm/rsaencryptionoaepsha512aesgcm.md) 或其他对称加密算法之一时，加密和解密函数调用的行为会发生变化。
- **省略发送方和接收方的长度检查。** 因为输入数据由 AES 会话密钥加密，该数据不再受特定长度的限制。同样，加密数据块也不再预期是密钥的 block size。实际上，它是密钥的 block size 加上加密数据的（可变）长度再加 16 个字节。

在加密端，[SecKeyCreateEncryptedData](<seckeycreateencrypteddata(________).md>) 函数并不仅仅是使用密钥对给定的数据块进行填充和编码，而是首先生成一个随机的先进加密标准（Advanced Encryption Standard，AES）会话密钥。它使用此密钥加密输入数据，然后使用你提供的输入公钥对 AES 密钥进行 RSA 加密。最后，它将 RSA 加密的会话密钥、AES 加密的数据和一个 16 字节的 AES-GCM 标签组装成一个数据块并返回给你。

在解密端，过程相反。该函数使用你提供的私钥解密 AES 会话密钥，然后使用该密钥解密数据。

如果你使用椭圆曲线密钥，请使用椭圆曲线算法之一，例如 [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA256AESGCM](seckeyalgorithm/eciesencryptioncofactorx963sha256aesgcm.md)。与上述 RSA 交换相比，此密钥交换的具体细节有所不同。尽管如此，你作为 API 消费者所看到的实际行为是相同的。

通过这些微小的更改，你可以从非对称加密切换到由非对称加密支持的对称加密。你现在可以高效地传输任意大的加密数据块。
