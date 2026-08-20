---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Tool_ToolCommon_m.html
archived_at: '2026-07-18T03:05:22.407019Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Tool-QHex.m.md)[Previous](Tool-CryptorCommands.m.md)

# Tool/ToolCommon.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Utilities used by various tool commands.
 */

#import "ToolCommon.h"

NS_ASSUME_NONNULL_BEGIN

@interface ToolCommon ()

@property (atomic, strong, readonly ) NSOperationQueue *    queue;

@end

NS_ASSUME_NONNULL_END

@implementation ToolCommon

+ (ToolCommon *)sharedInstance {
    static ToolCommon *     sSharedInstance;
    static dispatch_once_t  sOnceToken;
    dispatch_once(&sOnceToken, ^{
        sSharedInstance = [[ToolCommon alloc] init];
    });
    return sSharedInstance;
}

- (instancetype)init {
    self = [super init];
    if (self != nil) {
        self->_queue = [[NSOperationQueue alloc] init];
    }
    return self;
}

- (void)dealloc {
    assert(NO);
}

- (void)synchronouslyRunOperation:(NSOperation *)op {
    NSParameterAssert(op != nil);
    if (self.debugRunOpOnMainThread) {
        // This is the hacky way we do it to simplify debugging.
        [op main];
    } else {
        // This is how it /should/ be done.
        [self.queue addOperation:op];
        [self.queue waitUntilAllOperationsAreFinished];
    }
}

@end
```

[Next](Tool-QHex.m.md)[Previous](Tool-CryptorCommands.m.md)

