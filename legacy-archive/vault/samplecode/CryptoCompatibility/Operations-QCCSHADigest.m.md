---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Operations_QCCSHADigest_m.html
archived_at: '2026-07-18T03:05:21.202194Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Operations-QCCBase64Decode.h.md)[Previous](Operations-QCCAESCryptor.m.md)

# Operations/QCCSHADigest.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Calculates the SHA digest of some data.
 */

#import "QCCSHADigest.h"

#include <CommonCrypto/CommonCrypto.h>

NS_ASSUME_NONNULL_BEGIN

@interface QCCSHADigest ()

// read/write versions of public properties

@property (atomic, copy,   readwrite, nullable) NSData *        outputDigest;

@end

NS_ASSUME_NONNULL_END

@implementation QCCSHADigest

- (instancetype)init {
    abort();
}

- (instancetype)initWithAlgorithm:(QCCSHADigestAlgorithm)algorithm inputData:(NSData *)inputData {
    NSParameterAssert(inputData != nil);
    self = [super init];
    if (self != nil) {
        self->_algorithm = algorithm;
        self->_inputData = [inputData copy];
    }
    return self;
}

- (void)main {
    NSMutableData *     digest;

    // You can ignore the result CC_SHAxxx because it never fails.

    switch (self.algorithm) {
        case QCCSHADigestAlgorithmSHA1: {
            digest = [[NSMutableData alloc] initWithLength:CC_SHA1_DIGEST_LENGTH];
            (void) CC_SHA1(self.inputData.bytes, (CC_LONG) self.inputData.length, digest.mutableBytes);
        } break;
        case QCCSHADigestAlgorithmSHA2_224: {
            digest = [[NSMutableData alloc] initWithLength:CC_SHA224_DIGEST_LENGTH];
            (void) CC_SHA224(self.inputData.bytes, (CC_LONG) self.inputData.length, digest.mutableBytes);
        } break;
        case QCCSHADigestAlgorithmSHA2_256: {
            digest = [[NSMutableData alloc] initWithLength:CC_SHA256_DIGEST_LENGTH];
            (void) CC_SHA256(self.inputData.bytes, (CC_LONG) self.inputData.length, digest.mutableBytes);
        } break;
        case QCCSHADigestAlgorithmSHA2_384: {
            digest = [[NSMutableData alloc] initWithLength:CC_SHA384_DIGEST_LENGTH];
            (void) CC_SHA384(self.inputData.bytes, (CC_LONG) self.inputData.length, digest.mutableBytes);
        } break;
        case QCCSHADigestAlgorithmSHA2_512: {
            digest = [[NSMutableData alloc] initWithLength:CC_SHA512_DIGEST_LENGTH];
            (void) CC_SHA512(self.inputData.bytes, (CC_LONG) self.inputData.length, digest.mutableBytes);
        } break;
        default: {
            abort();
        } break;
    }

    self.outputDigest = digest;
}

@end
```

[Next](Operations-QCCBase64Decode.h.md)[Previous](Operations-QCCAESCryptor.m.md)

