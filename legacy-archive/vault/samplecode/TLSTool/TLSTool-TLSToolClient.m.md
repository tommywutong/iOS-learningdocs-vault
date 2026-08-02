---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_TLSToolClient_m.html
archived_at: '2026-07-26T19:54:14.821897Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](LICENSE.txt.md)[Previous](TLSTool-QHex.m.md)

# TLSTool/TLSToolClient.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Core of the s_client implementation.
 */

#import "TLSToolClient.h"

@import Security;

#import "QNetworkAdditions.h"
#import "QHex.h"

@interface TLSToolClient ()

@end

@implementation TLSToolClient

- (instancetype)initWithHostName:(NSString *)hostName port:(NSInteger)port {
    NSParameterAssert(hostName != nil);
    NSParameterAssert( (port > 0) && (port < 65536) );
    self = [super init];
    if (self != nil) {
        self->_hostName = [hostName copy];
        self->_port = port;
        self->_serverTrustedRoots = @[];
    }
    return self;
}

- (void)run {
    dispatch_async(self.queue, ^{
        BOOL                success;
        NSInputStream *     inStream;
        NSOutputStream *    outStream;

        // Create our streams.

        [QNetworkAdditions getStreamsToHostWithName:self.hostName port:self.port inputStream:&inStream outputStream:&outStream];

        if ( (NO) ) {
            // In many cases you can enable TLS with this code, which assumes a whole bunch
            // of standard defaults.  In our case, however, we need to configure some non-standard
            // properties so we have to use kCFStreamPropertySSLSettings.

            success = [inStream setProperty:NSStreamSocketSecurityLevelNegotiatedSSL forKey:NSStreamSocketSecurityLevelKey];
            assert(success);
        } else {
            NSMutableDictionary *   settings;

            settings = [NSMutableDictionary dictionary];

            // We disable the default server trust evaluation if:
            //
            // * we've been explicitly told to
            //
            // * we've been given some root certificates, in which case we need to do the trust
            //   evaluation manually (see -evaluateServerTrustManually, below)

            if (self.disableServerTrustEvaluation || (self.serverTrustedRoots.count != 0)) {
                settings[ (__bridge id) kCFStreamSSLValidatesCertificateChain ] = @NO;
            }

            // If we have a client identity, pass it along.  It's unfortunate that the CFSocketStream
            // API does not support client identity challenges (like NSURL{Session,Connection}, or indeed
            // like Secure Transprot via the kSSLSessionOptionBreakOnCertRequested option) but that's
            // the way things are.

            if (self.clientIdentity != NULL) {
                [self logWithFormat:@"client identity: %@", [TLSUtilities subjectSummaryForIdentity:self.clientIdentity]];
                settings[ (__bridge id) kCFStreamSSLCertificates ] = @[ (__bridge id) self.clientIdentity ];
            }

            // Configure the stream to use the new settings.

            success = [inStream setProperty:settings forKey:(__bridge NSString *) kCFStreamPropertySSLSettings];
            assert(success);
        }

        [self startConnectionWithInputStream:inStream outputStream:outStream responseData:nil];
    });

    dispatch_main();
}

/*! Called when the connection it opened to show any distinguished names received from the server.
 */

- (void)logDistinguishedNames {
    OSStatus        err;
    SSLContextRef   context;
    CFArrayRef      copyResult;

    context = (__bridge SSLContextRef) [self.inputStream propertyForKey: (__bridge NSString *) kCFStreamPropertySSLContext ];
    assert(context != NULL);

    err = SSLCopyDistinguishedNames(context, &copyResult);
    if (err == errSecSuccess) {
        NSArray *   distinguishedNames;

        distinguishedNames = CFBridgingRelease( copyResult );
        if (distinguishedNames != nil) {       // You get errSecSuccess and distinguishedNames == nil if the server didn't send us any DNs.
            if (distinguishedNames.count != 0) {
                [distinguishedNames enumerateObjectsUsingBlock:^(NSData * dnData, NSUInteger dnIndex, BOOL * stop) {
                    #pragma unused(stop)
                    [self logWithFormat:@"  %zu %@", (size_t) dnIndex, [QHex hexStringWithData:dnData]];
                }];
            }
        }
    } else {
        assert(NO);
    }
}

/*! Called when the caller has overridden the set of root certificates to trust (via the
 *  serverTrustedRoots property).  In that case standard trust evaluation is disabled
 *  and we have to do our own, using those trusted root certificates supplied by the caller.
 */

- (void)evaluateServerTrustManually {
    BOOL                allowConnection;
    OSStatus            err;
    SecTrustRef         trust;
    SecTrustResultType  trustResult;

    allowConnection = NO;

    trust = (__bridge SecTrustRef) [self.inputStream propertyForKey: (__bridge NSString *) kCFStreamPropertySSLPeerTrust];
    if (trust != NULL) {
        err = SecTrustSetAnchorCertificates(trust, (__bridge CFArrayRef) self.serverTrustedRoots);
        if (err == errSecSuccess) {
            err = SecTrustEvaluate(trust, &trustResult);
            if (err == errSecSuccess) {
                allowConnection = (trustResult == kSecTrustResultProceed) || (trustResult == kSecTrustResultUnspecified);
            }
        }
    }

    if ( ! allowConnection ) {
        [self logWithFormat:@"manual server trust evaluation failed"];
        [self stopConnectionWithError:[NSError errorWithDomain:NSOSStatusErrorDomain code:errSSLXCertChainInvalid userInfo:nil]];
    }
}

- (void)connectionDidOpen {
    if (self.showDistinguishedNames) {
        [self logDistinguishedNames];
    }
    if (self.serverTrustedRoots.count != 0) {
        [self evaluateServerTrustManually];
    }
}

- (void)connectionDidCloseWithError:(NSError *)error {
    exit(error == nil ? EXIT_SUCCESS : EXIT_FAILURE);
}

@end
```

[Next](LICENSE.txt.md)[Previous](TLSTool-QHex.m.md)

