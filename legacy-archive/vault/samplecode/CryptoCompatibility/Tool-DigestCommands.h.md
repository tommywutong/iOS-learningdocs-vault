---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Tool_DigestCommands_h.html
archived_at: '2026-07-18T03:05:21.579907Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Tool-KeyDerivationCommands.m.md)[Previous](Tool-ToolCommon.h.md)

# Tool/DigestCommands.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Commands for SHA and other digests.
 */

#import "QToolCommand.h"

NS_ASSUME_NONNULL_BEGIN

/*! Implements the `digest` command.
 */

@interface DigestCommand : QToolCommand

@end

/*! Implements the `hmac` command.
 */

@interface HMACCommand : QToolCommand

@end

NS_ASSUME_NONNULL_END
```

[Next](Tool-KeyDerivationCommands.m.md)[Previous](Tool-ToolCommon.h.md)

