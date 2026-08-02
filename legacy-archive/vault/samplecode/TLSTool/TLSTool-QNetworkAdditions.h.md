---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_QNetworkAdditions_h.html
archived_at: '2026-07-26T19:54:14.792974Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-QNetworkAdditions.m.md)[Previous](TLSTool-TLSToolClient.h.md)

# TLSTool/QNetworkAdditions.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Compatibility shim for OS X 10.10 / iOS 8 networking methods.
 */

@import Foundation;

NS_ASSUME_NONNULL_BEGIN

/*! Compatibility shim for OS X 10.10 / iOS 8 networking methods
 *
 *  \details OS X 10.10 / iOS 8 added some extremely useful class methods to NSStream.
 *  This class contains a methods that are compatible with the new methods but which you
 *  can call on earlier systems.
 */

@interface QNetworkAdditions : NSObject

/*! Creates a pair of streams that connect over TCP to a DNS name and port number.
 *
 *  \details This is a simple wrapper around CFStreamCreatePairWithSocketToHost, as
 *  described in QA1652 "Using NSStreams For A TCP Connection Without NSHost".
 *
 *  <https://developer.apple.com/library/ios/#qa/qa1652/_index.html>
 *
 *  \param hostname The DNS name of the host to connect to; must not be nil.
 *  \param port The port number on that host to connect to; must be in the range 1...65535.
 *  \param inputStream A pointer to an input stream variable; must not be NULL; on entry
 *  the value is ignored; on return the value will be a valid input stream.
 *  \param outputStream A pointer to an output stream variable; must not be NULL; on entry
 *  the value is ignored; on return the value will be a valid output stream.
 */

+ (void)getStreamsToHostWithName:(NSString *)hostname
    port:(NSInteger)port
    inputStream:( NSInputStream  * __autoreleasing __nonnull * __nullable)inputStream
    outputStream:(NSOutputStream * __autoreleasing __nonnull * __nullable)outputStream;

@end

NS_ASSUME_NONNULL_END
```

[Next](TLSTool-QNetworkAdditions.m.md)[Previous](TLSTool-TLSToolClient.h.md)

