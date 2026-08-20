---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Tool_CryptorCommands_h.html
archived_at: '2026-07-18T03:05:21.456157Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Tool-RSACommands.h.md)[Previous](Tool-QHex.h.md)

# Tool/CryptorCommands.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Commands for symmetric encryption and decryption.
 */

#import "QToolCommand.h"

NS_ASSUME_NONNULL_BEGIN

/*! A base class for all the AES commands.
 */

@interface AESCryptorCommand : QToolCommand

@end

/*! Implements the `aes-encrypt` command.
 */

@interface AESEncryptCommand : AESCryptorCommand

@end

/*! Implements the `aes-decrypt` command.
 */

@interface AESDecryptCommand : AESCryptorCommand

@end

/*! Implements the `aes-pad-encrypt` command.
 */

@interface AESPadEncryptCommand : AESCryptorCommand

@end

/*! Implements the `aes-pad-decrypt` command.
 */

@interface AESPadDecryptCommand : AESCryptorCommand

@end

/*! A base class for the AES 'big' cryptor commands.
 */

@interface AESBigCryptorCommand : AESCryptorCommand

@end

/*! Implements the `aes-pad-big-encrypt` command.
 */

@interface AESPadBigEncryptCommand : AESBigCryptorCommand

@end

/*! Implements the `aes-pad-big-decrypt` command.
 */

@interface AESPadBigDecryptCommand : AESBigCryptorCommand

@end

NS_ASSUME_NONNULL_END
```

[Next](Tool-RSACommands.h.md)[Previous](Tool-QHex.h.md)

