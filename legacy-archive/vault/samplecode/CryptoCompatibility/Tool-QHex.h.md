---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Tool_QHex_h.html
archived_at: '2026-07-18T03:05:21.859936Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Tool-CryptorCommands.h.md)[Previous](Tool-Base64Commands.h.md)

# Tool/QHex.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Hex dump utilities.
 */

@import Foundation;

NS_ASSUME_NONNULL_BEGIN

/*! Hex dump utilities.
 */

@interface QHex : NSObject

/*! Converts a buffer of bytes to a hex string.
 *  \param bytes The start of the buffer.
 *  \param length The length of the buffer.
 *  \returns A hex string, all lower case, with no spaces.
 */

+ (NSString *)hexStringWithBytes:(const void *)bytes length:(NSUInteger)length;

/*! Converts a data object to a hex string.
 *  \param data The data object.
 *  \returns A hex string, all lower case, with no spaces.
 */

+ (NSString *)hexStringWithData:(NSData *)data;

/*! Converts a hex string to a data object.
 *  \param hexString A hex string, using upper or lower case, with no spaces.
 *  \returns A data object holding the bytes described by the hex string, or 
 *      nil if there was a problem parsing the string.
 */

+ (nullable NSData *)optionalDataWithHexString:(NSString *)hexString;

/*! Converts a known good hex string to a data object.
 *  \details This is used extensively by the unit tests, where the hex strings are 
 *      hard wired and thus known to be good.
 *  \param hexString A hex string, using upper or lower case, with no spaces.
 *  \returns A data object holding the bytes described by the hex string.  This 
 *      will trap if the hex string can't be parsed.
 */

+ (NSData *)dataWithHexString:(NSString *)hexString;

@end

NS_ASSUME_NONNULL_END
```

[Next](Tool-CryptorCommands.h.md)[Previous](Tool-Base64Commands.h.md)

