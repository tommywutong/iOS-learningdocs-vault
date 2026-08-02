---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Operations_QCCBase64Encode_m.html
archived_at: '2026-07-18T03:05:19.777114Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Operations-QCCAESPadBigCryptor.h.md)[Previous](Operations-QCCRSASmallCryptorCompat.h.md)

# Operations/QCCBase64Encode.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements Base64 encoding.
 */

#import "QCCBase64Encode.h"

NS_ASSUME_NONNULL_BEGIN

@interface QCCBase64Encode ()

// read/write versions of public properties

@property (atomic, copy,   readwrite, nullable) NSString *      outputString;

@end

NS_ASSUME_NONNULL_END

@implementation QCCBase64Encode

- (instancetype)init {
    abort();
}

- (instancetype)initWithInputData:(NSData *)inputData {
    NSParameterAssert(inputData != nil);
    self = [super init];
    if (self != nil) {
        self->_inputData = [inputData copy];
    }
    return self;
}

- (void)main {
    NSDataBase64EncodingOptions options;
    NSString * output;

    options = NSDataBase64EncodingEndLineWithLineFeed;
    if (self.addLineBreaks) {
        options |= NSDataBase64Encoding64CharacterLineLength; 
    }
    output = [self.inputData base64EncodedStringWithOptions:options];

    // Our old code use to always add a trailing LF unless the input was empty, 
    // and our unit test relies on that, so we replicate it here.  

    if ( (output.length > 0) && ! [output hasSuffix:@"\n"] ) {
        output = [output stringByAppendingString:@"\n"];
    }
    self.outputString = output;
}

@end
```

[Next](Operations-QCCAESPadBigCryptor.h.md)[Previous](Operations-QCCRSASmallCryptorCompat.h.md)

