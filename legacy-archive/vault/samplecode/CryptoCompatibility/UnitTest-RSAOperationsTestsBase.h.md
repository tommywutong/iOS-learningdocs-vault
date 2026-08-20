---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/UnitTest_RSAOperationsTestsBase_h.html
archived_at: '2026-07-18T03:05:23.802060Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](UnitTest-RSAOperationsTestsCompat.m.md)[Previous](UnitTest-RSAOperationsTestsBase.m.md)

# UnitTest/RSAOperationsTestsBase.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Base class for our RSA operation tests.
 */

@import XCTest;

NS_ASSUME_NONNULL_BEGIN

@interface RSAOperationsTestsBase : XCTestCase

@property (nonatomic, strong, readonly, nullable) SecKeyRef     publicKey __attribute__ (( NSObject ));
@property (nonatomic, strong, readonly, nullable) SecKeyRef     privateKey __attribute__ (( NSObject ));
@property (nonatomic, assign, readonly)           BOOL          hasUnifiedCrypto;

@end

NS_ASSUME_NONNULL_END
```

[Next](UnitTest-RSAOperationsTestsCompat.m.md)[Previous](UnitTest-RSAOperationsTestsBase.m.md)

