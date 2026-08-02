---
title: 'PIVToken: Using CryptoTokenKit to add support for new types of tokens'
apple_id: TP40017285
resource_type: Sample Code
platform: macOS
topic: null
technology: CryptoTokenKit
published: '2016-09-22'
source_url: https://developer.apple.com/library/archive/samplecode/PIVToken/Listings/PIVToken_Token_h.html
archived_at: '2026-07-18T03:18:35.366256Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PIVToken: Using CryptoTokenKit to add support for new types of tokens](PIVToken-%20Using%20CryptoTokenKit%20to%20add%20support%20for%20new%20types%20of%20tokens.md)


[Next](PIVToken-TokenSession.h.md)[Previous](PIVToken-TokenDriver.m.md)

# PIVToken/Token.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements PIV token core
 */


#import <Foundation/Foundation.h>
#import <CryptoTokenKit/CryptoTokenKit.h>
#import <CryptoTokenKit/TKSmartCardToken.h>

NS_ASSUME_NONNULL_BEGIN

#pragma mark TKSmartCard utility extension for sending/receiving TKBERTLVRecord-formatted APDUs

@interface TKSmartCard(PIVDataFormat)

- (nullable TKTLVRecord *)sendIns:(UInt8)ins p1:(UInt8)p1 p2:(UInt8)p2 request:(nullable TKTLVRecord *)request expectedTag:(TKTLVTag)expectedTag sw:(UInt16 *)sw error:(NSError **)error;
- (nullable NSArray<TKTLVRecord *> *)recordsOfObject:(TKTokenObjectID)objectID error:(NSError **)error;

@end

#pragma mark PIV implementation of TKToken classes

@interface PIVTokenKeychainKey : TKTokenKeychainKey

- (instancetype)initWithCertificate:(SecCertificateRef)certificateRef objectID:(TKTokenObjectID)objectID certificateID:(TKTokenObjectID)certificateID alwaysAuthenticate:(BOOL)alwaysAuthenticate NS_DESIGNATED_INITIALIZER;
- (instancetype)initWithCertificate:(nullable SecCertificateRef)certificateRef objectID:(TKTokenObjectID)objectID NS_UNAVAILABLE;

@property (readonly) TKTokenObjectID certificateID;
@property (readonly) BOOL alwaysAuthenticate;
@property (readonly) UInt8 keyID;
@property (readonly) UInt8 algID;

@end

@class PIVTokenDriver;
@class PIVToken;
@class PIVTokenSession;

static const TKTokenOperationConstraint PIVConstraintPIN = @"PIN";
static const TKTokenOperationConstraint PIVConstraintPINAlways = @"PINAlways";

@interface PIVTokenSession : TKSmartCardTokenSession<TKTokenSessionDelegate>
- (instancetype)initWithToken:(TKToken *)token delegate:(id<TKTokenSessionDelegate>)delegate NS_UNAVAILABLE;

- (instancetype)initWithToken:(PIVToken *)token;
@property (readonly) PIVToken *PIVToken;

@end

@interface PIVToken : TKSmartCardToken<TKTokenDelegate>
- (instancetype)initWithSmartCard:(TKSmartCard *)smartCard AID:(nullable NSData *)AID tokenDriver:(TKSmartCardTokenDriver *)tokenDriver delegate:(id<TKTokenDelegate>)delegate NS_UNAVAILABLE;

- (nullable instancetype)initWithSmartCard:(TKSmartCard *)smartCard AID:(nullable NSData *)AID PIVDriver:(PIVTokenDriver *)tokenDriver error:(NSError **)error;
@property (readonly) PIVTokenDriver *driver;

@end

@interface PIVTokenDriver : TKSmartCardTokenDriver<TKSmartCardTokenDriverDelegate>
@end

NS_ASSUME_NONNULL_END
```

[Next](PIVToken-TokenSession.h.md)[Previous](PIVToken-TokenDriver.m.md)

