---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_QHex_h.html
archived_at: '2026-07-26T19:54:14.743125Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-TLSToolServer.h.md)[Previous](TLSTool-TLSUtilities.m.md)

# TLSTool/QHex.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Hex dump utilities.
 */

@import Foundation;

NS_ASSUME_NONNULL_BEGIN

/*! Hex utilities, primarily for testing.
 *  \details This class exports routines for converting data to a hex string
 *      and a hex string to data.  In all cases the hex string is very strict.
 */

@interface QHex : NSObject

/*! Returns a hex dump of the supplied binary data.
 *  \details The hex dump uses lowercase letters with no spaces.
 *  \param bytes A pointer to the data.
 *  \param length The length of that data; this may be 0.
 *  \returns A hex dump string.
 */

+ (NSString *)hexStringWithBytes:(const void *)bytes length:(NSUInteger)length;

/*! Returns a hex dump of the supplied data.
 *  \details The hex dump uses lowercase letters with no spaces.
 *  \param data The data to use; this may be empty.
 *  \returns A hex dump string.
 */

+ (NSString *)hexStringWithData:(NSData *)data;

/*! Returns binary data for the supplied hex string.
 *  \details The input data must be strictly formatted.  Specifically,
 *      no whitespace is allowed, all digits must be valid hex characters,
 *      and the length must be even.  Both upper and lower case letters are
 *      allowed.
 *  \param hexString The hex string to parse; this may be empty.
 *  \returns The parsed data; will not return nil; if the data is
 *      malformed, this routine will throw an exception.
 */

+ (NSData *)dataWithValidHexString:(NSString *)hexString;

/*! Returns binary data for the supplied hex string.
 *  \details The input data should be strictly formatted as defined by
 *      +hexStringWithData:.
 *  \param hexString The hex string to parse; this may be empty.
 *  \returns The parsed data, or nil if the data is malformed.
 */

+ (nullable NSData *)dataWithHexString:(NSString *)hexString;

@end

NS_ASSUME_NONNULL_END
```

[Next](TLSTool-TLSToolServer.h.md)[Previous](TLSTool-TLSUtilities.m.md)

