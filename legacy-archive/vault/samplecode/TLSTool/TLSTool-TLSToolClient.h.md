---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_TLSToolClient_h.html
archived_at: '2026-07-26T19:54:14.787379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-QNetworkAdditions.h.md)[Previous](TLSTool-TLSToolCommon.m.md)

# TLSTool/TLSToolClient.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Core of the s_client implementation.
 */

#import "TLSToolCommon.h"

NS_ASSUME_NONNULL_BEGIN

/*! An object that implements the tool's s_client command.
 *  \details To use this class, simply initialise it with a host and port to
 *  to connect to and then call -run.  Before calling -run you can optionally
 *  configure various parameters that modify its behaviour.
 */

@interface TLSToolClient : TLSToolCommon

/*! Initialises the object to connect to the specified host and port.
 *  \param hostName The host name (or IPv{4,6} address to connect to; must not be NULL.
 *  \param port The port to connect to; must be in the range 1..65535, inclusive.
 *  \returns An initialised object.
 */

- (instancetype)initWithHostName:(NSString *)hostName port:(NSInteger)port NS_DESIGNATED_INITIALIZER;

- (instancetype)init NS_UNAVAILABLE;

@property (atomic, copy,   readonly ) NSString *        hostName;   ///< The host to connect to; set by the init method.
@property (atomic, assign, readonly ) NSInteger         port;       ///< The port to connect to; set by the init method.

/*! Runs the command, never returning.
 */

- (void)run __attribute__ ((noreturn));

@property (atomic, assign, readwrite, nullable) SecIdentityRef clientIdentity __attribute((NSObject));  ///< Set to supply an identity to the server (which may or may not check it).
@property (atomic, assign, readwrite) BOOL              disableServerTrustEvaluation;   ///< Set to YES to disable the client's trust evaluation of the server.
@property (atomic, assign, readwrite) BOOL              showDistinguishedNames;         ///< Set to YES to have the client dump the distinguished names it got from the server.
@property (atomic, copy,   readwrite) NSArray *         serverTrustedRoots;             ///< Trust only certificates issued by these certificate authorities.
// showCertificates and translateCRToCRLF properties inherited from TLSToolCommon

@end

NS_ASSUME_NONNULL_END
```

[Next](TLSTool-QNetworkAdditions.h.md)[Previous](TLSTool-TLSToolCommon.m.md)

