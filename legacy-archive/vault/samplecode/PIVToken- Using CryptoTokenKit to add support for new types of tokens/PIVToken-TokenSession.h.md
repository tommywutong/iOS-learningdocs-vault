---
title: 'PIVToken: Using CryptoTokenKit to add support for new types of tokens'
apple_id: TP40017285
resource_type: Sample Code
platform: macOS
topic: null
technology: CryptoTokenKit
published: '2016-09-22'
source_url: https://developer.apple.com/library/archive/samplecode/PIVToken/Listings/PIVToken_TokenSession_h.html
archived_at: '2026-07-18T03:18:35.252317Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PIVToken: Using CryptoTokenKit to add support for new types of tokens](PIVToken-%20Using%20CryptoTokenKit%20to%20add%20support%20for%20new%20types%20of%20tokens.md)


[Next](PIVToken-TokenSession.m.md)[Previous](PIVToken-Token.h.md)

# PIVToken/TokenSession.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements PIV token session
 */

NS_ASSUME_NONNULL_BEGIN

@interface PIVTokenSession()

typedef NS_ENUM(NSInteger, PIVAuthState) {
    PIVAuthStateUnauthorized = 0,
    PIVAuthStateFreshlyAuthorized = 1,
    PIVAuthStateAuthorizedButAlreadyUsed = 2,
};

@property PIVAuthState authState;

@end

@interface PIVAuthOperation : TKTokenSmartCardPINAuthOperation

- (instancetype)initWithSession:(PIVTokenSession *)session;
@property (readonly) PIVTokenSession *session;

@end


NS_ASSUME_NONNULL_END
```

[Next](PIVToken-TokenSession.m.md)[Previous](PIVToken-Token.h.md)

