---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Operations_QCCBase64Encode_h.html
archived_at: '2026-07-18T03:05:19.726548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Operations-QCCAESPadCryptor.m.md)[Previous](Operations-QCCHMACSHAAuthentication.h.md)

# Operations/QCCBase64Encode.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements Base64 encoding.
 */

@import Foundation;

NS_ASSUME_NONNULL_BEGIN

/*! Encodes data as a Base64 string.
 *  \details This is a vanilla encoding; it does not do anything especially clever, like 
 *      deal PEM headers and footers.
 */

@interface QCCBase64Encode : NSOperation

/*! Initialise the object to encode the supplied data.
 *  \param inputData The data to encode; this may be empty.
 *  \returns The initialised object.
 */

- (instancetype)initWithInputData:(NSData *)inputData NS_DESIGNATED_INITIALIZER;

- (instancetype)init NS_UNAVAILABLE;

/*! The data to encode.
 *  \details This is set by the init method.
 */

@property (atomic, copy,   readonly ) NSData *              inputData;

/*! Determines whether line breaks are added.
 *  \details If true, UNIX style line breaks (LF) are added at column 64 as is traditional 
 *      for PEM.
 */

@property (atomic, assign, readwrite) BOOL                  addLineBreaks;

/*! The output Base64 string. 
 *  \details This is set when the operation is finished.
 */

@property (atomic, copy,   readonly, nullable) NSString *   outputString;

@end

NS_ASSUME_NONNULL_END
```

[Next](Operations-QCCAESPadCryptor.m.md)[Previous](Operations-QCCHMACSHAAuthentication.h.md)

