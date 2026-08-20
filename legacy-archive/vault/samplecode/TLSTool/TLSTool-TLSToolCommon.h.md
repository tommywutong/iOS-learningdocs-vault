---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_TLSToolCommon_h.html
archived_at: '2026-07-26T19:54:14.704375Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-TLSUtilities.h.md)[Previous](TLSTool-TLSToolServer.m.md)

# TLSTool/TLSToolCommon.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Code shared between the client and server.
 */

@import Foundation;

#import "TLSUtilities.h"

NS_ASSUME_NONNULL_BEGIN

/*! A base class shared by the s_client and s_server command code.
 *  \details This is where the bulk of the networking code exists. The subclasses
 *  just set up the streams correctly and then call down here to do the real work.
 *
 *  This code's main function is to manage the input and output streams:
 *
 *  - For the input stream, it reads any data that arrives on the stream and
 *    writes it to stdout.
 *
 *  - For the output stream, it reads any data that arrives on stdin and writes
 *    it to the stream.
 */

@interface TLSToolCommon : NSObject

// The following are API that clients can reasonable access.

@property (atomic, assign, readwrite) SSLProtocol       minProtocol;        ///< Defaults to kSSLProtocolUnknown, that is, the system-defined default value.
@property (atomic, assign, readwrite) SSLProtocol       maxProtocol;        ///< Defaults to kSSLProtocolUnknown, that is, the system-defined default value.
@property (atomic, assign, readwrite) BOOL              showCertificates;   ///< Set to YES to have the code display a hex dump of each certificate received.
@property (atomic, assign, readwrite) BOOL              translateCRToCRLF;  ///< Set to YES to have the stdin reading code convert LF to CR LF.

// The following declarations are for subclassers only.

- (instancetype)init NS_DESIGNATED_INITIALIZER;

/*! Starts a connection running over the specified stream pair.
 *  \details The streams are scheduled to run asynchronously.  The work
 *  is done on a serial queue that you can access via the queue property.
 *  Must be called on that queue.
 *  \param inputStream The input stream of the pair; must not be nil.
 *  \param outputStream The input stream of the pair; must not be nil.
 *  \param responseData The data to send on the output stream; if this is nil, lines are read from stdin.
 */

- (void)startConnectionWithInputStream:(NSInputStream *)inputStream outputStream:(NSOutputStream *)outputStream responseData:(NSData * __nullable)responseData;

/*! Stops the current connection, cleaning up all its state.
 *  \param error If not nil, this is the error that caused the connection to
 *  stop; nil if the connection stopped due to EOF.
 */

- (void)stopConnectionWithError:(NSError * __nullable)error;

@property (atomic, strong, readonly, nullable) NSInputStream *   inputStream;   ///< The current input stream.
@property (atomic, strong, readonly, nullable) NSOutputStream *  outputStream;  ///< The current output stream.
@property (atomic, copy,   readonly, nullable) NSData *          responseData;  ///< Data to send on output stream; may be nil.

/*! Called when the connection opens.
 *  \details A subclass can override this to print information about the newly
 *  opened connection.  Called on the object's queue.
 */

- (void)connectionDidOpen;

/*! Called when the connection closes.
 *  \details The client subclass overrides this so that it can quit when
 *  the connection closes.  Called on the object's queue.
 *  \param error An error value indicating why the connection closed, or
 *  nil if the connection closed due to EOF.
 */

- (void)connectionDidCloseWithError:(NSError * __nullable)error;

@property (atomic, assign, readonly ) BOOL              isStarted;          ///< Returns YES if there's are input streams in place; can only be accessed on the object's queue.

@property (atomic, strong, readonly ) dispatch_queue_t  queue;              ///< The dispatch queue used for all processing.

/*! Logs the specified message.
 *  \details This can be called from any context.
 *  \param format A standard NSString format string.
 */

- (void)logWithFormat:(NSString *)format, ... NS_FORMAT_FUNCTION(1,2);

@end

NS_ASSUME_NONNULL_END
```

[Next](TLSTool-TLSUtilities.h.md)[Previous](TLSTool-TLSToolServer.m.md)

