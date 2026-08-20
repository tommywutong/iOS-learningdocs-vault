---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_TLSToolServer_m.html
archived_at: '2026-07-26T19:54:14.695950Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-TLSToolCommon.h.md)[Previous](README.md.md)

# TLSTool/TLSToolServer.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Core of the s_server implementation.
 */

#import "TLSToolServer.h"

@interface TLSToolServer () <NSNetServiceDelegate>

@property (atomic, strong, readwrite) NSNetService *    server;                         ///< The net service that manages our listening socket.

@property (atomic, assign, readwrite) BOOL              hasPrintedServerDidStartMessage;///< See the discussion in -netServiceDidPublish:.

@property (atomic, copy,   readwrite) NSArray *         autorespondContent;             ///< An array of data with which to autorespond.
@property (atomic, copy,   readwrite) NSArray *         autorespondURLs;                ///< An array of URLs indicating where the autoresponse data was read from.
@property (atomic, assign, readwrite) NSUInteger        nextAutorespondContentIndex;    ///< The next item in the autorespondContent array to use.

@end

@implementation TLSToolServer

- (instancetype)initWithServerIdentify:(SecIdentityRef)serverIdentity port:(NSInteger)port {
    NSParameterAssert(serverIdentity != NULL);
    NSParameterAssert( (port > 0) && (port <= 65536) );
    self = [super init];
    if (self != nil) {
        self->_serverIdentity = serverIdentity;
        CFRetain(self->_serverIdentity);
        self->_port = port;
        self->_clientCertificateRoots = @[];
    }
    return self;
}

- (void)dealloc {
    // This object is not set up to be deallocated.
    assert(NO);
}

/*! Reads a single autorespond file, adding the content to the content array and the URL to the URLs array.
 *  \param url The location of the autorespond file.
 *  \param content The array to which to add the file's content.
 *  \param URLs The arary to which to add the file's URL.
 */

- (void)addAutorespondFileAtURL:(NSURL *)url toContent:(NSMutableArray *)content URLs:(NSMutableArray *)URLs {
    NSData *    d;
    NSError *   error;

    d = [NSData dataWithContentsOfURL:url options:0 error:&error];
    if (d == nil) {
        [self logWithFormat:@"server failed to read autorespond content: %@", url.path];
    } else {
        [content addObject:d];
        [URLs addObject:url];
    }
}

/*! Reads autorespond content from the location on disk into an in-memory array.
 */

- (void)readAutorespondContent {
    BOOL                success;
    NSNumber *          isDir;
    NSMutableArray *    content;
    NSMutableArray *    URLs;

    content = [[NSMutableArray alloc] init];
    URLs = [[NSMutableArray alloc] init];
    success = [self.autorespondContentURL getResourceValue:&isDir forKey:NSURLIsDirectoryKey error:NULL];
    if (success && isDir.boolValue) {
        for (NSURL * childURL in [[NSFileManager defaultManager] enumeratorAtURL:self.autorespondContentURL includingPropertiesForKeys:@[ NSURLIsDirectoryKey ] options:NSDirectoryEnumerationSkipsSubdirectoryDescendants | NSDirectoryEnumerationSkipsHiddenFiles errorHandler:nil]) {
            success = [childURL getResourceValue:&isDir forKey:NSURLIsDirectoryKey error:NULL];
            if (success && ! isDir.boolValue ) {
                [self addAutorespondFileAtURL:childURL toContent:content URLs:URLs];
            }
        }
    } else {
        [self addAutorespondFileAtURL:self.autorespondContentURL toContent:content URLs:URLs];
    }
    self.autorespondContent = content;
    self.autorespondURLs = URLs;
    assert([self.autorespondContent count] == [self.autorespondURLs count]);
}

- (void)run {
    [self logWithFormat:@"server identity: %@", [TLSUtilities subjectSummaryForIdentity:self.serverIdentity]];

    // Read in our autoresponse content.

    if (self.autorespondContentURL != nil) {
        [self readAutorespondContent];
        if (self.autorespondContent.count == 0) {
            [self logWithFormat:@"server could not read any autorespond content"];
            exit(EXIT_FAILURE);
        }
    }

    // Create the NSNetService object that handles incoming connections.  We don't care
    // about the domain or name (they both have reasonable defaults) but we have to supply
    // a type.

    self.server = [[NSNetService alloc] initWithDomain:@"" type:@"_x-TLSTool._tcp." name:@"" port:(int) self.port];
    self.server.delegate = self;
    [self.server publishWithOptions:NSNetServiceListenForConnections];

    // Run the server.  We can't use dispatch_main because NSNetService really wants a
    // run loop <rdar://problem/17960834>.  We have to have an exit() after the
    // -[NSRunLoop run] because it can return under oddball circumstances.

    [[NSRunLoop currentRunLoop] run];
    exit(EXIT_FAILURE);
}

- (void)startConnectionWithInputStream:(NSInputStream *)inputStream outputStream:(NSOutputStream *)outputStream responseData:(NSData *)responseData {
    BOOL                    success;
    SSLContextRef           context;

    assert(inputStream  != nil);
    assert(outputStream != nil);

    // Apply TLS settings.  Not that we always disable client trust evaluation because
    // the built-in support exhibits some very odd behaviour.  Rather, we do it all
    // manually in -evaluateClientTrustManually.

    success = [inputStream  setProperty:@{
        (__bridge NSString *) kCFStreamSSLIsServer:                  @YES,
        (__bridge NSString *) kCFStreamSSLCertificates:              @[ (__bridge id) self.serverIdentity ],
        (__bridge NSString *) kCFStreamSSLValidatesCertificateChain: @NO
    } forKey:(__bridge NSString *) kCFStreamPropertySSLSettings];
    assert(success);

    // Requesting a client certificate can't be done directly using socket stream properties;
    // instead we get the Secure Transport context and set it up there.

    context = (__bridge SSLContextRef) [inputStream propertyForKey:(__bridge NSString *) kCFStreamPropertySSLContext];
    assert(context != NULL);

    success = SSLSetClientSideAuthenticate(context, self.clientCertificateMode) == errSecSuccess;
    assert(success);

    // Previous versions of the code used to call SSLSetCertificateAuthorities here.  Now we
    // completely disable client trust evaluation and do it all ourselves in -evaluateClientTrustManually.

    [super startConnectionWithInputStream:inputStream outputStream:outputStream responseData:responseData];
}

/*! Called when a connection is established to do client trust evaluation.
 */

- (void)evaluateClientTrustManually{
    OSStatus            err;
    NSString *          errorMessage;
    SecTrustRef         trust;
    SecTrustResultType  trustResult;

    errorMessage = nil;

    trust = (__bridge SecTrustRef) [self.inputStream propertyForKey:(__bridge NSString *) kCFStreamPropertySSLPeerTrust];

    if (trust == NULL) {

        // On some OS X versions prior to 10.11, if you set the client-side authentication mode
        // to kAlwaysAuthenticate the systems acts like you set it to mode kTryAuthenticate
        // <rdar://problem/18816667>.  So, if we're in the mode kAlwaysAuthenticate and we didn't
        // get a trust object, we fail.

        if (self.clientCertificateMode == kAlwaysAuthenticate) {
            errorMessage = @"client certificate required but not presented";
        }
    } else if ( ! self.disableClientTrustEvaluation ) {

        // In -startConnectionWithInputStream:outputStream:responseData: we always disable the
        // default client trust evaluation so here we have to do the trust evaluation manually.
        // If anything fails, the connection fails.

        errorMessage = @"manual client trust evaluation failed";
        if (self.clientCertificateRoots.count == 0) {
            err = errSecSuccess;
        } else {
            err = SecTrustSetAnchorCertificates(trust, (__bridge CFArrayRef) self.clientCertificateRoots);
        }
        if (err == errSecSuccess) {
            err = SecTrustEvaluate(trust, &trustResult);
            if (err == errSecSuccess) {
                if ( (trustResult == kSecTrustResultProceed) || (trustResult == kSecTrustResultUnspecified) ) {
                    errorMessage = nil;
                }
            }
        }
    }

    if (errorMessage != nil) {
        [self logWithFormat:@"%@", errorMessage];
        [self stopConnectionWithError:[NSError errorWithDomain:NSOSStatusErrorDomain code:errSSLXCertChainInvalid userInfo:nil]];
    }
}

- (void)connectionDidOpen {
    [self evaluateClientTrustManually];
}

- (void)netServiceDidPublish:(NSNetService *)sender {
    assert(sender == self.server);

    // If you have multiple Bonjour registration domains (you most commonly see this
    // when Back to My Mac is enabled), -netServiceDidPublish: is called multiple
    // times, once for each domain.  We don't want to confused our users by printing
    // multiple "server did start" messages, so we only print that message on the
    // first call.
    //
    // Note that hasPrintedServerDidStartMessage is never cleared because the server
    // runs until someone terminates the entire process.

    if ( ! self.hasPrintedServerDidStartMessage ) {
        [self logWithFormat:@"server did start"];
        self.hasPrintedServerDidStartMessage = YES;
    }
}

- (void)netService:(NSNetService *)sender didNotPublish:(NSDictionary *)errorDict {
    assert(sender == self.server);

    [self logWithFormat:@"server startup failed %@ / %@", errorDict[NSNetServicesErrorDomain], errorDict[NSNetServicesErrorCode]];
    exit(EXIT_FAILURE);
}

- (void)netService:(NSNetService *)sender didAcceptConnectionWithInputStream:(NSInputStream *)inputStream outputStream:(NSOutputStream *)outputStream {
    dispatch_async(self.queue, ^{
        assert(sender == self.server);

        if (self.isStarted) {
            // We already have a connection in place; reject this connection.
            [inputStream  open];
            [outputStream open];
            [inputStream  close];
            [outputStream close];
        } else {
            NSData *        responseData;

            // If we have autoresponse content, work out which content to send next.

            responseData = nil;
            if (self.autorespondContent != nil) {
                NSString *      responseFileNamePath;

                responseData = self.autorespondContent[self.nextAutorespondContentIndex];
                responseFileNamePath = [self.autorespondURLs[self.nextAutorespondContentIndex] path].lastPathComponent;
                self.nextAutorespondContentIndex += 1;
                if (self.nextAutorespondContentIndex == self.autorespondContent.count) {
                    self.nextAutorespondContentIndex = 0;
                }

                [self logWithFormat:@"server will respond with contents of '%@'", responseFileNamePath];
            }

            // Start a connection based on these streams.

            [self startConnectionWithInputStream:inputStream outputStream:outputStream responseData:responseData];
        }
    });
}

@end
```

[Next](TLSTool-TLSToolCommon.h.md)[Previous](README.md.md)

