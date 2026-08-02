---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Operations_QCCBase64Decode_m.html
archived_at: '2026-07-18T03:05:19.672858Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Operations-QCCHMACSHAAuthentication.h.md)[Previous](Operations-QCCHMACSHAAuthentication.m.md)

# Operations/QCCBase64Decode.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements Base64 decoding.
 */

#import "QCCBase64Decode.h"

NS_ASSUME_NONNULL_BEGIN

@interface QCCBase64Decode ()

// read/write versions of public properties

@property (atomic, copy,   readwrite, nullable) NSData *        outputData;

@end

NS_ASSUME_NONNULL_END

@implementation QCCBase64Decode

- (instancetype)init {
    abort();
}

- (instancetype)initWithInputString:(NSString *)inputString {
    NSParameterAssert(inputString != nil);
    self = [super init];
    if (self != nil) {
        self->_inputString = [inputString copy];
    }
    return self;
}

- (void)main {
    self.outputData = [[NSData alloc] initWithBase64EncodedString:self.inputString options:NSDataBase64DecodingIgnoreUnknownCharacters];
}

@end
```

[Next](Operations-QCCHMACSHAAuthentication.h.md)[Previous](Operations-QCCHMACSHAAuthentication.m.md)

