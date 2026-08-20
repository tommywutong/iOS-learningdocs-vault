---
title: 'PIVToken: Using CryptoTokenKit to add support for new types of tokens'
apple_id: TP40017285
resource_type: Sample Code
platform: macOS
topic: null
technology: CryptoTokenKit
published: '2016-09-22'
source_url: https://developer.apple.com/library/archive/samplecode/PIVToken/Listings/PIVToken_TokenDriver_m.html
archived_at: '2026-07-18T03:18:35.227569Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PIVToken: Using CryptoTokenKit to add support for new types of tokens](PIVToken-%20Using%20CryptoTokenKit%20to%20add%20support%20for%20new%20types%20of%20tokens.md)


[Next](PIVToken-Token.h.md)[Previous](PIVToken-Token.m.md)

# PIVToken/TokenDriver.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 TokenDriver Instantiates the Token
 */

#import <Foundation/Foundation.h>
#import <CryptoTokenKit/CryptoTokenKit.h>

#import "Token.h"

@implementation PIVTokenDriver

- (TKSmartCardToken *)tokenDriver:(TKSmartCardTokenDriver *)driver createTokenForSmartCard:(TKSmartCard *)smartCard AID:(NSData *)AID error:(NSError * _Nullable __autoreleasing *)error {
    return [[PIVToken alloc] initWithSmartCard:smartCard AID:AID PIVDriver:self error:error];
}

@end
```

[Next](PIVToken-Token.h.md)[Previous](PIVToken-Token.m.md)

