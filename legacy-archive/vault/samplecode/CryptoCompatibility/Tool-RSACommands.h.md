---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Tool_RSACommands_h.html
archived_at: '2026-07-18T03:05:22.120887Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Tool-DigestCommands.m.md)[Previous](Tool-CryptorCommands.h.md)

# Tool/RSACommands.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Commands for RSA-based encryption, decryption, signing, and verification.
 */

#import "QToolCommand.h"

NS_ASSUME_NONNULL_BEGIN

/*! Implements the `rsa-verify` command.
 */

@interface RSASHAVerifyCommand : QToolCommand

@end

/*! Implements the `rsa-sign` command.
 */

@interface RSASHASignCommand : QToolCommand

@end

/*! A base class for the `RSASmallEncryptCommand` and `RSASmallDecryptCommand` classes.
 */

@interface RSACryptorCommand : QToolCommand

@end

/*! Implements the `rsa-small-encrypt` command.
 */

@interface RSASmallEncryptCommand : RSACryptorCommand

@end

/*! Implements the `rsa-small-decrypt` command.
 */

@interface RSASmallDecryptCommand : RSACryptorCommand

@end

NS_ASSUME_NONNULL_END
```

[Next](Tool-DigestCommands.m.md)[Previous](Tool-CryptorCommands.h.md)

