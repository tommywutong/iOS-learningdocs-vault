---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/TLSTool_main_m.html
archived_at: '2026-07-26T19:54:14.661113Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](README.md.md)[Previous](TLSTool.md)

# TLSTool/main.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Command line tool main.
 */

@import Foundation;

#import "TLSToolClient.h"
#import "TLSToolServer.h"

/*! Parses a port string and returns its numeric value.
 *  \param portStr The string to parse.
 *  \param portPtr A pointer to a place to store the port number; must not be NULL;
 *  on call, the value is ignored; on success, this will be a port number; on failure,
 *  the value is unmodified.
 *  \returns EXIT_SUCCESS on success; EXIT_FAILURE otherwise.
 */

static int ParsePort(NSString * portStr, NSInteger * portPtr) {
    int             result;
    NSScanner *     s;
    NSInteger       port;

    assert(portStr != NULL);
    assert(portPtr != NULL);

    result = EXIT_FAILURE;
    s = [NSScanner scannerWithString:portStr];
    if ([s scanInteger:&port]) {
        if (s.atEnd) {
            if ( (port > 0) && (port < 65536) ) {
                *portPtr = port;
                result = EXIT_SUCCESS;
            }
        }
    }
    return result;
}

/*! Parses a client:port string and returns the two components.
 *  \param arg The string to parse; may be NULL, which guarantees failure.
 *  \param clientHostPtr A pointer to a place to store the host string; must not be NULL;
 *  on call, the value is ignored; on success, this will be an autoreleased string; on
 *  failure, the value is unmodified.
 *  \param portPtr A pointer to a place to store the port number; must not be NULL;
 *  on call, the value is ignored; on success, this will be a port number; on failure,
 *  the value is unmodified.
 *  \returns EXIT_SUCCESS on success; EXIT_FAILURE otherwise.
 */

static int ParseClientHostAndPort(const char * arg, __autoreleasing NSString ** clientHostPtr, NSInteger * portPtr) {
    int             result;
    NSString *      argStr;
    NSRange         lastColonRange;
    NSString *      hostStr;
    NSString *      portStr;

    // arg may be null
    assert(clientHostPtr != NULL);
    assert(portPtr != NULL);

    result = EXIT_FAILURE;

    if (arg != NULL) {
        argStr = @(arg);
        if (argStr != nil) {
            lastColonRange = [argStr rangeOfString:@":" options:NSBackwardsSearch];
            if (lastColonRange.location != NSNotFound) {
                hostStr = [argStr substringToIndex:lastColonRange.location];
                portStr = [argStr substringFromIndex:lastColonRange.location + lastColonRange.length];
                result = ParsePort(portStr, portPtr);
                if (result == EXIT_SUCCESS) {
                    *clientHostPtr = hostStr;
                }
            }
        }
    }

    return result;
}

/*! Parses a port string and returns its numeric value.
 *  \param arg The string to parse; may be NULL, which guarantees failure.
 *  \param portPtr A pointer to a place to store the port number; must not be NULL;
 *  on call, the value is ignored; on success, this will be a port number; on failure,
 *  the value is unmodified.
 *  \returns EXIT_SUCCESS on success; EXIT_FAILURE otherwise.
 */

static int ParseServerPort(const char * arg, NSInteger * portPtr) {
    int             result;
    NSString *      argStr;

    // arg may be null
    assert(portPtr != NULL);

    result = EXIT_FAILURE;

    if (arg != NULL) {
        argStr = @(arg);
        if (argStr != nil) {
            result = ParsePort(argStr, portPtr);
        }
    }

    return result;
}

/*! Searches the keychain and returns an identity for the specified name.
 *  \details It first looks for an exact match, then looks for a fuzzy
 *  match (a case and diacritical insensitive substring).
 *  \param arg The name to look for; may be NULL, which guarantees failure.
 *  \param identityPtr A pointer to a place to store the identity; must not be NULL;
 *  on call, the value is ignored; on success, this will be an identity that the
 *  caller must release; on failure, the value is unmodified.
 *  \returns EXIT_SUCCESS on success; EXIT_FAILURE otherwise.
 */

static int ParseIdentityNamed(const char * arg, SecIdentityRef * identityPtr) {
    NSString *      argStr;
    OSStatus        err;
    CFArrayRef      copyMatchingResult;
    SecIdentityRef  identity;

    identity = nil;

    if (arg != NULL) {
        argStr = @(arg);
        if (argStr != nil) {
            err = SecItemCopyMatching((__bridge CFDictionaryRef) @{
                    (__bridge id) kSecClass:            (__bridge id) kSecClassIdentity,
                    (__bridge id) kSecReturnRef:        @YES,
                    (__bridge id) kSecReturnAttributes: @YES,
                    (__bridge id) kSecMatchLimit:       (__bridge id) kSecMatchLimitAll
                },
                (CFTypeRef *) &copyMatchingResult
            );
            if (err == errSecSuccess) {
                NSArray *       matchResults;
                NSUInteger      matchIndex;

                matchResults = CFBridgingRelease( copyMatchingResult );

                // First look for an exact match.

                matchIndex = [matchResults indexOfObjectPassingTest:^BOOL(NSDictionary * matchDict, NSUInteger idx, BOOL *stop) {
                    #pragma unused(idx)
                    #pragma unused(stop)
                    return [matchDict[ (__bridge id) kSecAttrLabel ] isEqual:argStr];
                }];

                // If that fails, try a fuzzy match.

                if (matchIndex == NSNotFound) {
                    matchIndex = [matchResults indexOfObjectPassingTest:^BOOL(NSDictionary * matchDict, NSUInteger idx, BOOL *stop) {
                        #pragma unused(idx)
                        #pragma unused(stop)
                        return [matchDict[ (__bridge id) kSecAttrLabel ] rangeOfString:argStr options:NSCaseInsensitiveSearch | NSDiacriticInsensitiveSearch].location != NSNotFound;
                    }];
                }

                if (matchIndex != NSNotFound) {
                    identity = (__bridge SecIdentityRef) matchResults[matchIndex][ (__bridge id) kSecValueRef];
                    assert(CFGetTypeID(identity) == SecIdentityGetTypeID());
                    CFRetain(identity);
                }
            }
        }
    }

    if (identity != NULL) {
        *identityPtr = identity;
    }
    return identity != NULL ? EXIT_SUCCESS : EXIT_FAILURE;
}

/*! Parses a protocol string (as used by the -min and -max options) to return a
 *  SSLProtocol value.
 *  \param arg The protocol string; may be NULL, which guarantees failure.
 *  \param protocolPtr A pointer to a place to store the protocol number; must not be NULL;
 *  on call, the value is ignored; on success, this will be a protocol number; on failure,
 *  the value is unmodified.
 *  \returns EXIT_SUCCESS on success; EXIT_FAILURE otherwise.
 */

static int ParseProtocol(const char * arg, SSLProtocol * protocolPtr) {
    int         result;

    result = EXIT_FAILURE;
    if (arg != NULL) {
        result = EXIT_SUCCESS;
        if (strcmp(arg, "ssl3_0") == 0) {
            *protocolPtr = kSSLProtocol3;
        } else if (strcmp(arg, "tls1_0") == 0) {
            *protocolPtr = kTLSProtocol1;
        } else if (strcmp(arg, "tls1_1") == 0) {
            *protocolPtr = kTLSProtocol11;
        } else if (strcmp(arg, "tls1_2") == 0) {
            *protocolPtr = kTLSProtocol12;
        } else {
            result = EXIT_FAILURE;
        }
    }

    return result;
}

/*! Parse a certificate name, search the keychain for that certificate, and
 *  add it to the specified array.
 *  \param arg The protocol string; may be NULL, which guarantees failure.
 *  \param certificates An array to add the certificate too; must not be NULL.
 *  \returns EXIT_SUCCESS on success; EXIT_FAILURE otherwise.
 */

static int ParseAndAddCertificate(const char * arg, NSMutableArray * certificates) {
    SecCertificateRef   certificate;
    NSString *          argStr;
    OSStatus            err;

    certificate = NULL;
    if (arg != NULL) {
        argStr = @(arg);
        if (argStr != nil) {
            err = SecItemCopyMatching( (__bridge CFDictionaryRef) @{
                (__bridge id) kSecClass:            (__bridge id) kSecClassCertificate,
                (__bridge id) kSecReturnRef:        @YES,
                (__bridge id) kSecAttrLabel:        argStr
            }, (CFTypeRef *) &certificate);
            if (err == errSecSuccess) {
                [certificates addObject:(__bridge id) certificate];
                CFRelease(certificate);
            }
        }
    }
    return certificate != NULL ? EXIT_SUCCESS : EXIT_FAILURE;
}

int main(int argc, char **argv) {
    #pragma unused(argc)
    #pragma unused(argv)
    int                 retVal;

    @autoreleasepool {
        BOOL                client;
        NSString *          clientHost;
        NSInteger           port;
        BOOL                showCertificates;
        BOOL                translateCRToCRLF;
        BOOL                disableTrustEvaluation;
        BOOL                showDistinguishedNames;
        SSLAuthenticate     clientCertificateMode;
        NSURL *             autorespondContentURL;
        SecIdentityRef      identity;
        SSLProtocol         minProtocol;
        SSLProtocol         maxProtocol;
        NSMutableArray *    caCertificates;
        size_t              argIndex;

        // Parse the command line options.  We can't use <x-man-page://3/getopt> because
        // we're trying to be openssl-like.

        clientHost = @"localhost";
        port = 4433;
        showCertificates = NO;
        translateCRToCRLF = NO;
        disableTrustEvaluation = NO;
        showDistinguishedNames = NO;
        clientCertificateMode = kNeverAuthenticate;
        autorespondContentURL = nil;
        identity = NULL;
        minProtocol = kSSLProtocolUnknown;
        maxProtocol = kSSLProtocolUnknown;
        caCertificates = [[NSMutableArray alloc] init];
        retVal = EXIT_SUCCESS;
        if (argc < 2) {
            retVal = EXIT_FAILURE;
        } else {
            if (strcmp(argv[1], "s_client") == 0) {
                client = YES;

                argIndex = 2;
                while ( (retVal == EXIT_SUCCESS) && (argv[argIndex] != NULL) ) {
                    if (strcmp(argv[argIndex], "-connect") == 0) {
                        argIndex += 1;
                        retVal = ParseClientHostAndPort(argv[argIndex], &clientHost, &port);
                    } else if (strcmp(argv[argIndex], "-cert") == 0) {
                        argIndex += 1;
                        retVal = ParseIdentityNamed(argv[argIndex], &identity);
                    } else if (strcmp(argv[argIndex], "-noverify") == 0) {
                        disableTrustEvaluation = YES;
                    } else if (strcmp(argv[argIndex], "-show_DNs") == 0) {
                        showDistinguishedNames = YES;
                    } else if (strcmp(argv[argIndex], "-min") == 0) {
                        argIndex += 1;
                        retVal = ParseProtocol(argv[argIndex], &minProtocol);
                    } else if (strcmp(argv[argIndex], "-max") == 0) {
                        argIndex += 1;
                        retVal = ParseProtocol(argv[argIndex], &maxProtocol);
                    } else if (strcmp(argv[argIndex], "-cacert") == 0) {
                        argIndex += 1;
                        retVal = ParseAndAddCertificate(argv[argIndex], caCertificates);
                    } else if (strcmp(argv[argIndex], "-showcerts") == 0) {
                        showCertificates = YES;
                    } else if (strcmp(argv[argIndex], "-crlf") == 0) {
                        translateCRToCRLF = YES;
                    } else {
                        retVal = EXIT_FAILURE;
                    }
                    argIndex += 1;
                }
            } else if (strcmp(argv[1], "s_server") == 0) {
                client = NO;

                argIndex = 2;
                while ( (retVal == EXIT_SUCCESS) && (argv[argIndex] != NULL) ) {
                    if (strcmp(argv[argIndex], "-cert") == 0) {
                        argIndex += 1;
                        retVal = ParseIdentityNamed(argv[argIndex], &identity);
                    } else if (strcmp(argv[argIndex], "-accept") == 0) {
                        argIndex += 1;
                        retVal = ParseServerPort(argv[argIndex], &port);
                    } else if (strcmp(argv[argIndex], "-authenticate") == 0) {
                        argIndex += 1;
                        if (argv[argIndex] == NULL) {
                            retVal = EXIT_FAILURE;
                        } else if (strcmp(argv[argIndex], "none") == 0) {
                            clientCertificateMode = kNeverAuthenticate;
                        } else if (strcmp(argv[argIndex], "request") == 0) {
                            clientCertificateMode = kTryAuthenticate;
                        } else if (strcmp(argv[argIndex], "require") == 0) {
                            clientCertificateMode = kAlwaysAuthenticate;
                        } else {
                            retVal = EXIT_FAILURE;
                        }
                    } else if (strcmp(argv[argIndex], "-noverify") == 0) {
                        disableTrustEvaluation = YES;
                    } else if (strcmp(argv[argIndex], "-autorespond") == 0) {
                        argIndex += 1;
                        if (argv[argIndex] == NULL) {
                            retVal = EXIT_FAILURE;
                        } else {
                            autorespondContentURL = [NSURL fileURLWithFileSystemRepresentation:argv[argIndex] isDirectory:NO relativeToURL:nil];
                            if (autorespondContentURL == nil) {
                                retVal = EXIT_FAILURE;
                            }
                        }
                    } else if (strcmp(argv[argIndex], "-min") == 0) {
                        argIndex += 1;
                        retVal = ParseProtocol(argv[argIndex], &minProtocol);
                    } else if (strcmp(argv[argIndex], "-max") == 0) {
                        argIndex += 1;
                        retVal = ParseProtocol(argv[argIndex], &maxProtocol);
                    } else if (strcmp(argv[argIndex], "-cacert") == 0) {
                        argIndex += 1;
                        retVal = ParseAndAddCertificate(argv[argIndex], caCertificates);
                    } else if (strcmp(argv[argIndex], "-showcerts") == 0) {
                        showCertificates = YES;
                    } else if (strcmp(argv[argIndex], "-crlf") == 0) {
                        translateCRToCRLF = YES;
                    } else {
                        retVal = EXIT_FAILURE;
                    }
                    argIndex += 1;
                }

                if (identity == NULL) {
                    retVal = EXIT_FAILURE;
                }
            } else {
                retVal = EXIT_FAILURE;
            }
        }

        // On error, print the usage.

        if (retVal == EXIT_FAILURE) {
            fprintf(stderr, "usage: %s s_client options\n", getprogname());
            fprintf(stderr, "       %s s_server options\n", getprogname());
            fprintf(stderr, "  s_client options:\n");
            fprintf(stderr, "    -connect host:port\n");
            fprintf(stderr, "    -cert identityName (found in keychain)\n");
            fprintf(stderr, "    -noverify\n");
            fprintf(stderr, "    -show_DNs\n");
            fprintf(stderr, "    -min ssl3_0|tls1_0|tls1_1|tls1_2\n");
            fprintf(stderr, "    -max ssl3_0|tls1_0|tls1_1|tls1_2\n");
            fprintf(stderr, "    -cacert certificateName\n");
            fprintf(stderr, "    -showcerts\n");
            fprintf(stderr, "    -crlf\n");
            fprintf(stderr, "  s_server options:\n");
            fprintf(stderr, "    -cert identityName (found in keychain, required)\n");
            fprintf(stderr, "    -accept port (default is 4433)\n");
            fprintf(stderr, "    -authenticate none|request|require\n");
            fprintf(stderr, "    -noverify\n");
            fprintf(stderr, "    -autorespond fileOrDirPath\n");
            fprintf(stderr, "    -min ssl3_0|tls1_0|tls1_1|tls1_2\n");
            fprintf(stderr, "    -max ssl3_0|tls1_0|tls1_1|tls1_2\n");
            fprintf(stderr, "    -cacert certificateName\n");
            fprintf(stderr, "    -showcerts\n");
            fprintf(stderr, "    -crlf\n");
        } else {

            // On success, set up and run a client or server object.

            if (client) {
                TLSToolClient *     toolClient;

                toolClient = [[TLSToolClient alloc] initWithHostName:clientHost port:port];
                toolClient.clientIdentity = identity;
                toolClient.disableServerTrustEvaluation = disableTrustEvaluation;
                toolClient.showDistinguishedNames = showDistinguishedNames;
                toolClient.minProtocol = minProtocol;
                toolClient.maxProtocol = maxProtocol;
                if (caCertificates.count != 0) {
                    toolClient.serverTrustedRoots = caCertificates;
                }
                toolClient.showCertificates = showCertificates;
                toolClient.translateCRToCRLF = translateCRToCRLF;
                [toolClient run];
            } else {
                TLSToolServer *     toolServer;

                toolServer = [[TLSToolServer alloc] initWithServerIdentify:identity port:port];
                toolServer.clientCertificateMode = clientCertificateMode;
                toolServer.disableClientTrustEvaluation = disableTrustEvaluation;
                toolServer.autorespondContentURL = autorespondContentURL;
                toolServer.minProtocol = minProtocol;
                toolServer.maxProtocol = maxProtocol;
                if (caCertificates.count != 0) {
                    toolServer.clientCertificateRoots = caCertificates;
                }
                toolServer.showCertificates = showCertificates;
                toolServer.translateCRToCRLF = translateCRToCRLF;
                [toolServer run];
            }
            // no coming back to here
            assert(NO);
        }
    }

    return retVal;
}
```

[Next](README.md.md)[Previous](TLSTool.md)

