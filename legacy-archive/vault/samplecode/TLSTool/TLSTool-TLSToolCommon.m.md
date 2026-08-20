---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_TLSToolCommon_m.html
archived_at: '2026-07-26T19:54:14.781400Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-TLSToolClient.h.md)[Previous](TLSTool-TLSToolServer.h.md)

# TLSTool/TLSToolCommon.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Code shared between the client and server.
 */

#import "TLSToolCommon.h"

#import "TLSUtilities.h"
#import "QHex.h"

@interface TLSToolCommon () <NSStreamDelegate>

@property (atomic, strong, readwrite) dispatch_source_t stdinSource;

@property (atomic, strong, readwrite) NSInputStream *   inputStream;
@property (atomic, strong, readwrite) NSOutputStream *  outputStream;
@property (atomic, copy,   readwrite) NSData *          responseData;
@property (atomic, assign, readwrite) BOOL              haveSentResponseData;
@property (atomic, assign, readwrite) BOOL              haveSentConnectionDidOpen;
@property (atomic, assign, readwrite) BOOL              hasSpaceAvailable;
@property (atomic, strong, readonly ) NSMutableData *   outputBuffer;
@property (atomic, assign, readwrite) BOOL              haveLoggedConnectionDetails;
@property (atomic, assign, readwrite) uint64_t          bytesSent;
@property (atomic, assign, readwrite) uint64_t          bytesReceived;

@end

@implementation TLSToolCommon

static int sTLSToolKey = 42;    // The value here isn't significant; it's the address of sTLSToolKey that matters.

- (instancetype)init {
    self = [super init];
    if (self != nil) {
        NSString *      queueName;

        // Create our serial queue, setting some queue-specific data so we can identify it.

        queueName = [NSString stringWithFormat:@"%@.queue", NSStringFromClass([self class])];
        self->_queue = dispatch_queue_create(queueName.UTF8String, DISPATCH_QUEUE_SERIAL);
        dispatch_queue_set_specific(self->_queue, &sTLSToolKey, (__bridge void *) self, NULL);

        self->_outputBuffer = [[NSMutableData alloc] init];
    }
    return self;
}

- (void)dealloc {
    // This object is not set up to be deallocated.
    assert(NO);
}

/*! Determines if the current thread is running on the queue associated with self.
 *  \returns YES if is it; NO otherwise.
 */

- (BOOL)runningOnOwnQueue {
    return dispatch_get_specific(&sTLSToolKey) == (__bridge void *) self;
}

- (void)startConnectionWithInputStream:(NSInputStream *)inputStream outputStream:(NSOutputStream *)outputStream responseData:(NSData *)responseData {
    BOOL                    success;
    SSLContextRef           context;

    assert([self runningOnOwnQueue]);

    context = (__bridge SSLContextRef) [inputStream propertyForKey:(__bridge NSString *) kCFStreamPropertySSLContext];
    assert(context != NULL);

    if (self.minProtocol != kSSLProtocolUnknown) {
        success = SSLSetProtocolVersionMin(context, self.minProtocol) == errSecSuccess;
        assert(success);
    }
    if (self.maxProtocol != kSSLProtocolUnknown) {
        success = SSLSetProtocolVersionMax(context, self.maxProtocol) == errSecSuccess;
        assert(success);
    }

    self.inputStream  = inputStream;
    self.outputStream = outputStream;
    self.responseData = responseData;

    // If there's no response data, set up to read lines from stdin.

    if (self.responseData == nil) {
        if (self.stdinSource == nil) {
            [self startStdinReader];
        }
    }

    self.inputStream.delegate = self;
    self.outputStream.delegate = self;

    CFReadStreamSetDispatchQueue( (__bridge CFReadStreamRef ) self.inputStream,  self.queue);
    CFWriteStreamSetDispatchQueue((__bridge CFWriteStreamRef) self.outputStream, self.queue);

    [self.inputStream  open];
    [self.outputStream open];
}

- (BOOL)isStarted {
    assert([self runningOnOwnQueue]);
    return self.inputStream != nil;
}

- (void)connectionDidOpen {
    // do nothing
}

- (void)connectionDidCloseWithError:(NSError *)error {
    #pragma unused(error)
    // do nothing
}

- (void)stopConnectionWithError:(NSError *)error {
    if (error == nil) {
        [self logWithFormat:@"close"];
    } else {
        [self logWithFormat:@"error %@ / %d", error.domain, (int) error.code];
    }
    [self logWithFormat:@"bytes sent %llu, bytes received %llu", (unsigned long long) self.bytesSent, (unsigned long long) self.bytesReceived];
    [self.inputStream  setDelegate:nil];
    [self.outputStream setDelegate:nil];
    if (self.inputStream != NULL) {
        CFReadStreamSetDispatchQueue(  (CFReadStreamRef ) self.inputStream,  NULL);
    }
    if (self.outputStream != NULL) {
        CFWriteStreamSetDispatchQueue( (CFWriteStreamRef) self.outputStream, NULL);
    }
    [self.inputStream  close];
    [self.outputStream close];
    self.inputStream  = nil;
    self.outputStream = nil;

    self.haveSentConnectionDidOpen = NO;
    self.hasSpaceAvailable = NO;
    self.outputBuffer.length = 0;
    self.responseData = nil;
    self.haveSentResponseData = NO;
    self.haveLoggedConnectionDetails = NO;
    self.bytesSent = 0;
    self.bytesReceived = 0;

    [self connectionDidCloseWithError:error];
}

- (void)logWithFormat:(NSString *)format, ... {
    va_list             ap;
    NSString *          str;
    NSMutableArray *    lines;

    // assert([self runningOnOwnQueue]);        -- We specifically allow this off the standard queue.

    va_start(ap, format);
    str = [[NSString alloc] initWithFormat:format arguments:ap];
    va_end(ap);

    lines = [[NSMutableArray alloc] init];
    [str enumerateLinesUsingBlock:^(NSString *line, BOOL *stop) {
        #pragma unused(stop)
        [lines addObject:[[NSString alloc] initWithFormat:@"* %@\n", line]];
    }];
    (void) fprintf(stdout, "%s", [lines componentsJoinedByString:@""].UTF8String);
    (void) fflush(stdout);
}

/*! Called by -logConnectionDetails to log information about the TLS protocol negotiation.
 */

- (void)logTLSProtocolDetails {
    OSStatus            err;
    SSLContextRef       context;
    SSLProtocol         protocol;
    SSLCipherSuite      cipher;

    context = (__bridge SSLContextRef) [self.inputStream propertyForKey:(__bridge NSString *) kCFStreamPropertySSLContext];
    if (context == NULL) {
        [self logWithFormat:@"no context"];
    } else {
        err = SSLGetNegotiatedProtocolVersion(context, &protocol);
        if (err != errSecSuccess) {
            [self logWithFormat:@"could not get protocol version: %d", (int) err];
        } else {
            [self logWithFormat:@"protocol: %@", [TLSUtilities stringForProtocolVersion:protocol]];
        }

        err = SSLGetNegotiatedCipher(context, &cipher);
        if (err != errSecSuccess) {
            [self logWithFormat:@"could not get cypher: %d", (int) err];
        } else {
            [self logWithFormat:@"cipher: %@", [TLSUtilities stringForCipherSuite:cipher]];
        }
    }
}

/*! Returns the set of certificates from the TLS handshake.

    When you get a trust object via `kCFStreamPropertySSLPeerTrust`, someone has already
    evaluated that trust for you (that's not API, btw, but a compatibility measure).  That
    makes it hard to distinguish between the certificates given to you by the server and
    the certificates found via trust evaluation.  That's distinction is important because
    trust evaluation can work differently on different platforms.  For example, iOS doesn't
    automatically find intermediate certificates via the Authority Information Access
    (1.3.6.1.5.5.7.1.1) extension but OS X, where this code is running, does.  There's no
    way to ask the trust object for the set of certificates it was created with, so instead
    we get that set from the SSLContext.  That requires us to use a deprecated, and not
    available on iOS, API, SSLCopyPeerCertificates.  That's not a big deal here because
    we're just a debugging tool.
 */

- (NSSet *)certificatesFromHandshake {
    OSStatus        err;
    NSSet *         result;
    SSLContextRef   context;
    CFArrayRef      contextCertificates;

    result = nil;

    context = (__bridge SSLContextRef) [self.inputStream propertyForKey:(__bridge NSString *) kCFStreamPropertySSLContext];

    #pragma clang diagnostic push
    #pragma clang diagnostic ignored "-Wdeprecated-declarations"

    err = SSLCopyPeerCertificates(context, &contextCertificates);

    #pragma clang diagnostic pop

    if (err == errSecSuccess) {
        result = [NSSet setWithArray:(__bridge NSArray *) contextCertificates];

        CFRelease(contextCertificates);
    }

    if (result == nil) {
        result = [NSSet set];
    }

    return result;
}

/*! Logs information about each certificate in the certificate chain of the supplied trust object.
 */

- (void)logCertificateInfoForTrust:(SecTrustRef)trust {
    NSSet *             handshakeCertificates;
    CFIndex             certificateCount;
    CFIndex             certificateIndex;

    [self logWithFormat:@"certificate info:"];
    handshakeCertificates = [self certificatesFromHandshake];
    certificateCount = SecTrustGetCertificateCount(trust);
    for (certificateIndex = 0; certificateIndex < certificateCount; certificateIndex++) {
        SecCertificateRef   certificate;
        BOOL                cameFromHandshake;

        certificate = SecTrustGetCertificateAtIndex(trust, certificateIndex);

        cameFromHandshake = [handshakeCertificates containsObject:(__bridge id) certificate];

        [self logWithFormat:@"  %zu %@ %@ %@ %@ '%@'",
            (size_t) certificateIndex,
            cameFromHandshake ? @"+" : @" ",
            [TLSUtilities keyAlgorithmStringForCertificate:certificate],
            [TLSUtilities keyBitSizeStringForCertificate:certificate],
            [TLSUtilities signatureAlgorithmStringForCertificate:certificate],
            CFBridgingRelease( SecCertificateCopySubjectSummary( certificate ) )
        ];
    }
}

/*! Logs a hex dump of each certificate in the certificate chain of the supplied trust object.
 */

- (void)logCertificateDataForTrust:(SecTrustRef)trust {
    CFIndex             certificateCount;
    CFIndex             certificateIndex;

    [self logWithFormat:@"certificate data:"];
    certificateCount = SecTrustGetCertificateCount(trust);
    for (certificateIndex = 0; certificateIndex < certificateCount; certificateIndex++) {
        [self logWithFormat:@"  %zu %@",
            (size_t) certificateIndex,
            [QHex hexStringWithData:CFBridgingRelease( SecCertificateCopyData( SecTrustGetCertificateAtIndex(trust, certificateIndex) ) )]
        ];
    }
}

/*! Called by -logConnectionDetails to log information about the trust evaulation.
 */

- (void)logTrustDetails {
    OSStatus            err;
    SecTrustRef         trust;
    SecTrustResultType  trustResult;

    trust = (__bridge SecTrustRef) [self.inputStream propertyForKey:(__bridge NSString *) kCFStreamPropertySSLPeerTrust];
    if (trust == nil) {
        [self logWithFormat:@"no trust"];
    } else {
        err = SecTrustEvaluate(trust, &trustResult);
        if (err != errSecSuccess) {
            [self logWithFormat:@"trust evaluation failed: %d", (int) err];
        } else {
            [self logWithFormat:@"trust result: %@", [TLSUtilities stringForTrustResult:trustResult]];
            [self logCertificateInfoForTrust:trust];
            if (self.showCertificates) {
                [self logCertificateDataForTrust:trust];
            }
        }
    }
}

/*! Logs information about the connection.
 *  \details This routine is called on each has-{space,data}-available event.  On the first
 *  such event, it logs details about the connection, including information about trust
 *  evaluation and the TLS protocol parameters.
 *
 *  Note that we do this on the has-{space,data}-available event, not the open event,
 *  because the TLS state isn't set up at the point that the open event is delivered.
 */

- (void)logConnectionDetails {
    if ( ! self.haveLoggedConnectionDetails ) {
        [self logTLSProtocolDetails];
        [self logTrustDetails];
        self.haveLoggedConnectionDetails = YES;
    }
}

/*! Create an input source that reads stdin and routes it to the output stream.
 */

- (void)startStdinReader {
    self.stdinSource = dispatch_source_create(DISPATCH_SOURCE_TYPE_READ, STDIN_FILENO, 0, self.queue);
    dispatch_source_set_event_handler(self->_stdinSource, ^{
        assert([self runningOnOwnQueue]);
        [self readAndSendStdin];
    });
    dispatch_resume(self->_stdinSource);
}

/*! Reads data from stdin and sends it to the output stream.
 *  \details This is called by a dispatch event source handler when
 *  stdin has data available.  It makes a single read call to get
 *  what data is currently there and sends it to the output stream.
 */

- (void)readAndSendStdin {
    ssize_t         bytesRead;
    uint8_t         buf[2048];

    assert([self runningOnOwnQueue]);

    bytesRead = read(STDIN_FILENO, buf, sizeof(buf));
    if (bytesRead < 0) {
        [self stopConnectionWithError:[NSError errorWithDomain:NSPOSIXErrorDomain code:errno userInfo:nil]];
    } else if (bytesRead == 0) {
        [self stopConnectionWithError:nil];
    } else if (self.outputStream == nil) {
        [self logWithFormat:@"could not send data; no connection"];
    } else {
        NSMutableData *     newData;

        newData = [NSMutableData dataWithBytes:buf length:(NSUInteger) bytesRead];

        if (self.translateCRToCRLF) {
            NSUInteger      index;

            // Convert CR to CRLF in newData.

            index = 0;
            while (index != newData.length) {
                if ( ((uint8_t *) newData.mutableBytes)[index] == '\n') {
                    [newData replaceBytesInRange:NSMakeRange(index, 1) withBytes:"\r\n" length:2];
                    index += 2;
                } else {
                    index += 1;
                }
            }
        }

        if ((newData.length + self.outputBuffer.length) > 4096) {
            [self stopConnectionWithError:[NSError errorWithDomain:NSPOSIXErrorDomain code:ENOBUFS userInfo:nil]];
        } else {
            [self.outputBuffer appendData:newData];
            if (self.hasSpaceAvailable) {
                [self sendData];
            }
        }
    }
}

/*! Attemps to send data from the output buffer.
 *  \details Called in two situations:
 *
 *  - when new data is placed in the output buffer and we've previously
 *    ignored a has-space-available event because of the lack of data
 *
 *  - when space has become available
 *
 *  It checks to see if there is data in the output buffer.  If there is,
 *  it sends what it can to the output stream and then removes the sent
 *  data from the buffer.  Also, in the case where we're sending autorespond
 *  data, it takes care of closing the stream after we've completely sent
 *  that data.
 */

- (void)sendData {
    NSInteger       bytesWritten;

    assert(self.hasSpaceAvailable);
    if (self.outputBuffer.length != 0) {
        self.hasSpaceAvailable = NO;

        bytesWritten = [self.outputStream write:self.outputBuffer.bytes maxLength:self.outputBuffer.length];
        if (bytesWritten > 0) {
            self.bytesSent += (NSUInteger) bytesWritten;
            [self.outputBuffer replaceBytesInRange:NSMakeRange(0, (NSUInteger) bytesWritten) withBytes:NULL length:0];
        }
    }

    // If the we're sending pre-programmed data and we've put that data into the output buffer
    // already and yet we didn't send any data (that is, hasSpaceAvailable is still true), we have
    // no more data to send and thus close the streams.  We do this on the next has-space-available
    // event, rather than after the write that emptied the output buffer, because CFSocketStream
    // can truncate data if you're using TLS and close the stream immediately after a write
    // <rdar://problem/19498032>.

    if ( (self.responseData != nil) && self.haveSentResponseData && self.hasSpaceAvailable ) {
        [self stopConnectionWithError:nil];
    }
}

- (void)stream:(NSStream *)aStream handleEvent:(NSStreamEvent)eventCode {
    NSString *  streamName;

    assert([self runningOnOwnQueue]);

    streamName = aStream == self.inputStream ? @" input" : @"output";
    switch (eventCode) {
        case NSStreamEventOpenCompleted: {
            [self logWithFormat:@"%@ stream did open", streamName];
        } break;
        case NSStreamEventHasBytesAvailable: {
            NSInteger   bytesRead;
            uint8_t     buffer[2048];

            [self logWithFormat:@"%@ stream has bytes", streamName];
            [self logConnectionDetails];
            bytesRead = [self.inputStream read:buffer maxLength:sizeof(buffer)];
            if (bytesRead > 0) {
                self.bytesReceived += (NSUInteger) bytesRead;

                (void) fwrite(buffer, 1, (size_t) bytesRead, stdout);
                (void) fflush(stdout);

                if ( (self.responseData != nil) && ! self.haveSentResponseData ) {
                    [self.outputBuffer appendData:self.responseData];
                    self.haveSentResponseData = YES;

                    if (self.hasSpaceAvailable) {
                        [self sendData];
                    }
                }
            }
        } break;
        case NSStreamEventHasSpaceAvailable: {

            // Tell the subclass about the open connection.  There are two gotchas here:
            //
            // * The subclass may close the connection, so we have to check self.outputStream
            //   after the call before trying to process the has-space-available event.
            //
            // * We have to set haveSentConnectionDidOpen to YES /before/ calling the subclass,
            //   because otherwise, if the client closes the connection, we end up setting it
            //   to YES while the connection is closed and bad things ensue.

            if ( ! self.haveSentConnectionDidOpen ) {
                self.haveSentConnectionDidOpen = YES;
                [self connectionDidOpen];
            }

            // If the connection isn't closed, deal with the has-space-available event.

            if (self.outputStream != nil) {
                [self logWithFormat:@"%@ stream has space", streamName];
                [self logConnectionDetails];
                self.hasSpaceAvailable = YES;
                [self sendData];
            }
        } break;
        default:
            assert(NO);
            // fall through
        case NSStreamEventEndEncountered: {
            [self logWithFormat:@"%@ stream end", streamName];
            [self stopConnectionWithError:nil];
        } break;
        case NSStreamEventErrorOccurred: {
            NSError *   error;

            error = aStream.streamError;
            [self stopConnectionWithError:error];
        } break;
    }
}

@end
```

[Next](TLSTool-TLSToolClient.h.md)[Previous](TLSTool-TLSToolServer.h.md)

