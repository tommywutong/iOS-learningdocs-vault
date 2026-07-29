---
title: 'Friday Q&A 2012-08-10：CommonCrypto 概览'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b5c3c8f7e51b0450'
translated: true
---

> 原文：[Friday Q&A 2012-08-10：CommonCrypto 概览](https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html)　·　mikeash.com Friday Q&A

发布于 2012-08-10 13:21| [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2012-08-24：你不一定想知道的关于 C 的那些事](https://www.mikeash.com/pyblog/friday-qa-2012-08-24-things-you-never-wanted-to-know-about-c.html)  
上一篇文章：[Friday Q&A 2012-07-27：让我们来构建 Tagged Pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)  
标签：[cryptography](https://www.mikeash.com/pyblog/?tag=cryptography) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa)

Friday Q&A 2012-08-10：CommonCrypto 概览

作者：[Mike Ash](https://www.mikeash.com/)

**哈希**  
用于计算加密哈希（也称为摘要）的功能位于 `CommonDigest.h` 中。其中提供了多种不同的哈希算法，每种都有自己的函数，从常见的 SHA-1 到不常见的 MD2.

快速回顾一下，加密哈希函数是一种将任意大小的数据映射为较小数据的函数，使得 `x = y` 总是意味着 `f(x) = f(y)`，并且 `f(x) = f(y)` 以极高的概率意味着 `x = y`。换句话说，如果两段数据具有相同的加密哈希值，你可以高度确信它们内容相同。它们也是_抗原像攻击的_，这意味着如果你只有 `f(x)`，要恢复出`x`.

中的每种哈希都有一个状态结构体和三个用于操作它的函数。`CommonDigest.h` 中的每种哈希都有一个状态结构体和三个用于操作它的函数。`Init` 函数初始化状态结构体。`Update` 函数将数据送入哈希计算。`Final` 函数随后计算已提供数据的哈希值。所有这些哈希都是流式哈希，因此你可以逐段输入数据，然后计算整个数据的哈希值，而无需一次性将所有数据都保存在内存中。

让我们看一个例子，说明如何计算几段不同数据的 SHA-1 哈希，这里假设是用户名和机器标识符。我们假定它们已经被转换成了 `NSData` 实例。对于字符串，你可能希望将它们转换为 `NSData`，使用像 UTF-8 这样的编码，可能还需要先用类似 `NSString` 的 `decomposedStringWithCanonicalMapping` 方法进行 Unicode 标准化。以下是假设的 `NSData` 变量：

```
    NSData *username = ...;
    NSData *machineIdentifier = ...;
```

接下来，我们为 `SHA-1`:

```
    CC_SHA1_CTX context;
    CC_SHA1_Init(&context);
```

创建并初始化状态结构体。然后我们使用 `Update` 函数将数据送入上下文：

```
    CC_SHA1_Update(&context, [username bytes], [username length]);
    CC_SHA1_Update(&context, [machineIdentifier bytes], [machineIdentifier length]);
```

最后，我们使用 `Final` 函数计算哈希值。我们需要自己为哈希值分配存储空间，但有一个便捷的宏可以告诉我们它有多长。`NSMutableData` 是存储哈希数据的理想目标：

```
    NSMutableData *hash = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CC_SHA1_Final([hash mutableBytes], &context);
```

现在哈希值就在 `hash` 变量中。请注意，这是原始哈希值，而不是 human-readable 版本。如果你需要像十六进制这样的格式，你之后必须自己进行转换。

为方便起见，还提供了一个函数，将 `Init`, `Update`, `Final` 序列封装成单个调用，适用于需要计算单个数据块的哈希值时。使用方法如下：

```
    NSData *toHash = ...;
    NSMutableData *hash = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CC_SHA1([toHash bytes], [toHash length], [hash mutableBytes]);
```

所有其他哈希算法都具有相同的上下文结构体和四个函数，只需将函数名中的 `SHA1` 替换为相应哈希算法的名称即可。有关完整列表，请参见 `CommonDigest.h` 头文件。

请注意，由于历史遗留原因，所有这些函数都返回一个指示成功或失败的代码。然而，这些函数不可能失败，因此该返回值可以安全地忽略。

**HMACs**  
HMAC 请注意，由于历史遗留原因，所有这些函数都返回一个指示成功或失败的代码。然而，这些函数不可能失败，因此该返回值可以安全地忽略。Hash-based 消息认证码。一个 HMAC 将加密哈希与密钥结合起来，以提供_认证 _。使用 HMAC CommonCrypto 在 HMAC 中提供了 HMAC 函数。`CommonHMAC.h`.

 函数。HMAC 函数与哈希函数类似，不同之处在于，它不是为每种哈希提供一组独立的函数，而是只提供一组函数，通过一个参数来指定要使用的哈希函数。可用的哈希函数列表在头文件顶部的枚举中列出。

 以下是一个使用 HMAC 计算一段数据的 `Init`, `Update`, `Final` 序列，使用 SHA-1 作为哈希函数：

```
    NSData *key = ...;
    NSData *data = ...;

    CCHmacContext context;
    CCHmacInit(&context, kCCHmacAlgSHA1, [key bytes], [key length]);
    CCHmacUpdate(&context, [data bytes], [data length]);

    NSMutableData *hash = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CCHmacFinal(&context, [hash mutableBytes]);
```

与哈希函数一样，有一个单独的 `CCHmac` 函数可以一次性完成整个序列，适用于单个数据块。

**密钥派生函数**  
密钥派生函数是加密哈希的另一种衍生形式。密钥派生函数接受一个密码和盐值，并从中计算出一个密钥，这基本上是 random-looking 数据，由密码和盐值派生而来。CommonCrypto 在 `CommonKeyDerivation.h`.

这可以用来从密码生成加密密钥，例如安全地 password-protect 保护文件。它还可以用于安全地认证用户，而不会让攻击者在认证数据库被攻破后从中提取密码。

一个好的密钥派生函数支持_密钥拉伸_，即人为地增加函数计算难度，使其需要更长时间。已认证的用户只需计算一次该函数，因此花费较多时间是可以接受的。而攻击者需要猜测大量密码，因此每次猜测花费大量时间会使整个过程极其缓慢。例如，一个需要一秒钟计算的密钥派生函数对于认证来说是可以接受的，但每次猜测都需要一秒钟，就使攻击者几乎不可能猜出密码。

CommonCrypto 提供了一个 key-derivation 函数，PBKDF2，它通过允许调用者指定迭代次数来支持密钥拉伸。密钥派生函数通过 `CCKeyDerivationPBKDF` 函数。为了帮助决定使用多少次迭代，`CCCalibratePBKDF` 可用于计算需要多少次迭代才能使函数花费特定的时间。

以下是一个从密码派生密钥的示例，使用 PBKDF2 基于 SHA-1:

```
    NSData *password = ...;
    NSData *salt = ...;

    // Figure out how many rounds needed for 1000ms computation time
    uint rounds = CCCalibratePBKDF(kCCPBKDF2,
                                   [password length],
                                   [salt length],
                                   kCCPRFHmacAlgSHA1,
                                   CC_SHA1_DIGEST_LENGTH),
                                   1000);

    // Derive the key
    NSMutableData *derivedKey = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CCKeyDerivationPBKDF(kCCPBKDF2,
                         [password bytes],
                         [password length],
                         [salt bytes],
                         [salt length],
                         kCCPRFHmacAlgSHA1,
                         rounds,
                         [derivedKey mutableBytes],
                         [derivedKey length]);
```

初始计算可以使用像这样校准的迭代次数，但对于验证，迭代次数必须与初始计算中使用的次数相同。因此，如果你使用动态迭代次数，则需要存储最初使用的迭代次数以及盐值和派生密钥。

**对称加密**  
CommonCrypto 提供了令人眼花缭乱的加密算法和模式，我不打算全部介绍。如果你需要与现有的加密系统兼容，该加密系统应明确指定其使用的算法和模式。如果你可以自由选择算法，你可能希望使用[AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) 以 [CBC](http://en.wikipedia.org/wiki/CBC_mode_of_operation#Cipher-block_chaining_.28CBC.29) 模式并配合 [PKCS7](http://en.wikipedia.org/wiki/Padding_(cryptography)#Padding_填充。请注意，由于填充的原因，输出数据可能比输入数据略大。

加密功能位于 `CommonCryptor.h` 中。它遵循与其他功能相同的 init/update/final 模式，只不过初始化函数由于某种原因被命名为 `Create`。

与其他功能不同，加密是通过类似于实际对象（称为 cryptor）的方式提供的，而不是上下文结构体。这意味着，与其他 CommonCrypto 函数中使用的上下文结构体不同，你在使用完 cryptor 后必须显式释放它。

使用 `CCCryptorCreate` 函数创建 cryptor。它需要一组参数：

- 要执行的操作，加密或解密。
- 要使用的加密算法。
- 选项，例如填充。
- 加密密钥及其长度。
- 初始化向量。

其中大部分内容应该很清楚，但初始化向量对你来说可能比较陌生。对多段数据使用相同的加密密钥是不安全的。初始化向量是一段随机的、non-private 数据块，其基本作用是随机化加密算法，以便你可以安全地重用同一密钥。加密时，你生成初始化向量，然后将其与加密数据一起传输。解密时，你使用密钥、初始化向量和加密数据来恢复原始数据。

唯一另一个棘手的地方是获取数据。我们之前看到的 CommonCrypto 的所有其他功能都提供 fixed-sized 的输出，而输入是 variable-length 输入。而 `Update` 函数只负责接收数据，然后 `Final` 函数产生结果。对称加密在你馈入数据时就会生成数据，因此 `Update` 函数也会产生数据。由于数据量不一定固定，`Update` 函数会告诉调用者它实际写入了多少数据，而一个 `CCCryptorGetOutputLength` 函数可用于确定需要提供多大的缓冲区。

以下是一个使用 AES 加密某些数据的简单示例。请注意，这些函数可能返回错误，实际代码必须检查错误，而不是盲目地继续执行。为了简洁起见，此代码省略了错误检查：

```
    NSData *data;
    NSData *key;
    NSData *initializationVector;

    CCCryptorRef cryptor;
    CCCryptorCreate(kCCEncrypt,
                    kCCAlgorithmAES128,
                    kCCOptionPKCS7Padding,
                    [key bytes],
                    [key length],
                    [initializationVector bytes],
                    &cryptor);

    size_t length = CCCryptorGetOutputLength(cryptor, [data length], true);
    NSMutableData *encryptedData = [NSMutableData dataWithLength: length];
    size_t updateLength;
    CCCryptorUpdate(cryptor,
                    [data bytes],
                    [data length],
                    [encryptedData mutableBytes],
                    [encryptedData length],
                    &updateLength);

    // Final may emit data, put it on the end
    char *finalDataPointer = (char *)[encryptedData mutableBytes] + updateLength;
    size_t remainingLength = [encryptedData length] - updateLength;
    size_t finalLength;
    CCCryptorFinal(cryptor,
                   finalDataPointer,
                   remainingLength,
                   &finalLength);

    // The amount of data emitted may have been less than
    // GetOutputLength said, so truncate
    [encryptedData setLength: updateLength + finalLength];

    CCCryptorRelease(cryptor);
```

如果你要流式传输数据，或者有多段数据需要加密，你可以调用 `CCCryptorUpdate` 多次，最后调用 `CCCryptorFinal` 一次以完成输出。你可以将 `CCCryptorUpdate` 产生的数据流式传输到另一个目标，或者简单地将其全部累积到一个缓冲区中。

对于输入数据是单个连续块并且希望将输出数据累积在内存中的情况，`CCCrypt` 函数是一个快捷方式，它结合了上述使用的 `CCCryptorCreate`, `CCCryptorUpdate`, `CCCryptorFinal` 和 `CCCryptorRelease` 的功能。

**总结**  
CommonCrypto 是 Mac OS X 和 iOS 提供的一个便捷库，提供了一系列加密原语。它提供了加密哈希、message-authentication 消息认证码和 key-derivation 基于这些哈希的派生函数，以及对称加密。它不是 fully-featured 加密库，如[OpenSSL](http://www.openssl.org/)，因为它缺少更复杂的特性，例如公钥加密和通用协议，如[TLS](http://en.wikipedia.org/wiki/Transport_Layer_Security)。然而，如果你的需求在其能力范围内，CommonCrypto 易于使用且无需 third-party 代码。

密码学很难。本文不打算作为密码学的一般性介绍或如何使用它的指南。如果你计划在漏洞或故障可能导致损害的情况下实现加密，请务必在深入之前充分阅读相关主题。

今天就到这里。下次再来参加另一个神秘的 Friday Q&A。Friday Q&A 由读者建议驱动，所以请继续[发送你的想法](mailto:mike@mikeash.com)!

你喜欢这篇文章吗？我出售成书，里面全是这样的文章！第二卷和 III 现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle。[点击此处了解更多信息](https://www.mikeash.com/book.html).

---

评论：

---

[评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html)

添加你的想法，发表评论：

垃圾邮件和 off-topic 帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢[Pygments](http://pygments.org/).
