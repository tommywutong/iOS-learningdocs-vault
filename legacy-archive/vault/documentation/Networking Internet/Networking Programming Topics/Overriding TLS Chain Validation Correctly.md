---
title: Networking Programming Topics
apple_id: TP40012488
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Articles/OverridingSSLChainValidationCorrectly.html
archived_at: '2026-07-15T08:18:51.130443Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Programming Topics](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Resolving%20DNS%20Hostnames.md)

# Overriding TLS Chain Validation Correctly

This article describes how to override the chain validation behavior of network connections secured with Transport Layer Security (TLS).

When a TLS certificate is verified, the operating system verifies its chain of trust. If that chain of trust contains only valid certificates and ends at a known (trusted) anchor certificate, then the certificate is considered valid. If it does not, it is considered invalid. If you are using a commercially signed certificate from a major vendor, the certificate should “just work”.

However, if you are doing something that falls outside the norm—creating client certificates for your users, providing service for multiple domains with a single certificate that is not trusted for those domains, using a self-signed certificate, connecting to a host by IP address (where the networking stack cannot determine the server’s hostname), and so on—you must take additional steps to convince the operating system to accept the certificate.

At a high level, TLS chain validation is performed by a trust object (`SecTrustRef`). This object contains a number of flags that control what types of validation are performed. As a rule, you should not touch these flags, but you should be aware of their existence. In addition, the trust object contains a policy (`SecPolicyRef`) that allows you to provide the hostname that should be used when evaluating a TLS certificate. Finally, the trust object contains a list of trusted anchor certificates that your application can modify.

This article is split into multiple parts. The first part, [Manipulating Trust Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknbufvjvomq), describes common ways to manipulate the trust object to change validation behavior. The remaining sections, [Trust Objects and NSURLConnection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknbufvjvonq) and [Trust Objects and NSStream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknbufvjvooa), show how to integrate those changes with various networking technologies.

The details of manipulating the trust object depend in large part on what you’re trying to override. The two most common things to override are the hostname (which must match either the leaf certificate’s common name or one of the names in its Subject Alternate Name extension) and the set of anchors (which determine a set of trusted certificate authorities).

To add a certificate to the list of trusted anchor certificates, you must copy the existing anchor certificates into an array, create a mutable version of that array, add the new anchor certificate to the mutable array, and tell the trust object to use that newly updated array for future evaluation of trust. A simple function to do this is listed in Listing 1.

__Listing 1__  Adding an anchor to a `SecTrustRef` object

```
SecTrustRef addAnchorToTrust(SecTrustRef trust, SecCertificateRef trustedCert)
{
#ifdef PRE_10_6_COMPAT
        CFArrayRef oldAnchorArray = NULL;

        /* In OS X prior to 10.6, copy the built-in
           anchors into a new array. */
        if (SecTrustCopyAnchorCertificates(&oldAnchorArray) != errSecSuccess) {
                /* Something went wrong. */
                return NULL;
        }

        CFMutableArrayRef newAnchorArray = CFArrayCreateMutableCopy(
                kCFAllocatorDefault, 0, oldAnchorArray);
        CFRelease(oldAnchorArray);
#else
        /* In iOS and OS X v10.6 and later, just create an empty
           array. */
        CFMutableArrayRef newAnchorArray = CFArrayCreateMutable (
                kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);
#endif

        CFArrayAppendValue(newAnchorArray, trustedCert);

        SecTrustSetAnchorCertificates(trust, newAnchorArray);

#ifndef PRE_10_6_COMPAT
        /* In iOS or OS X v10.6 and later, reenable the
           built-in anchors after adding your own.
         */
        SecTrustSetAnchorCertificatesOnly(trust, false);
#endif

        return trust;
```

To override the hostname (to allow a certificate for one specific site to work for another specific site, or to allow a certificate to work when you connected to a host by its IP address), you must replace the policy object that the trust policy uses to determine how to interpret the certificate. To do this, first create a new TLS policy object for the desired hostname. Then create an array containing that policy. Finally, tell the trust object to use that array for future evaluation of trust. Listing 2 shows a function that does this.

__Listing 2__  Changing the remote hostname for a `SecTrustRef` object

```
SecTrustRef changeHostForTrust(SecTrustRef trust)
{
        CFMutableArrayRef newTrustPolicies = CFArrayCreateMutable(
                kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);

        SecPolicyRef sslPolicy = SecPolicyCreateSSL(true, CFSTR("www.example.com"));

        CFArrayAppendValue(newTrustPolicies, sslPolicy);

#ifdef MAC_BACKWARDS_COMPATIBILITY
        /* This technique works in OS X (v10.5 and later) */

        SecTrustSetPolicies(trust, newTrustPolicies);
        CFRelease(oldTrustPolicies);

        return trust;
#else
        /* This technique works in iOS 2 and later, or
           OS X v10.7 and later */

        CFMutableArrayRef certificates = CFArrayCreateMutable(
                kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);

        /* Copy the certificates from the original trust object */
        CFIndex count = SecTrustGetCertificateCount(trust);
        CFIndex i=0;
        for (i = 0; i < count; i++) {
                SecCertificateRef item = SecTrustGetCertificateAtIndex(trust, i);
                CFArrayAppendValue(certificates, item);
        }

        /* Create a new trust object */
        SecTrustRef newtrust = NULL;
        if (SecTrustCreateWithCertificates(certificates, newTrustPolicies, &newtrust) != errSecSuccess) {
                /* Probably a good spot to log something. */

                return NULL;
        }

        return newtrust;
#endif
}
```


To override the chain validation behavior of [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection), you must override two methods:

- `connection:canAuthenticateAgainstProtectionSpace:`

  This method tells `NSURLConnection` that it knows how to handle authentication of a particular type. When your application decides whether to trust a server certificate, it is considered a form of authentication—your application authenticating the server.
- `connection:didReceiveAuthenticationChallenge:`

  In this method, your code needs to modify the trust policies, keys, or hostnames provided by the server or the client so that the trust policy evaluates successfully.

Listing 3 shows an example of these two methods.

__Listing 3__  Overriding the trust object used by an `NSURLConnection` object

```objc
// If you are building for OS X 10.7 and later or iOS 5 and later,
// leave out the first method and use the second method as the
// connection:willSendRequestForAuthenticationChallenge: method.
// For earlier operating systems, include the first method, and
// use the second method as the connection:didReceiveAuthenticationChallenge:
// method.

#ifndef NEW_STYLE
- (BOOL)connection:(NSURLConnection *)connection canAuthenticateAgainstProtectionSpace:(NSURLProtectionSpace *)protectionSpace {
    #pragma unused(connection)

    NSString *method = [protectionSpace authenticationMethod];
    if (method == NSURLAuthenticationMethodServerTrust) {
           return YES;
    }
    return NO;
}

-(void)connection:(NSURLConnection *)connection
        didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
#else
-(void)connection:(NSURLConnection *)connection
        willSendRequestForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
#endif
{
    NSURLProtectionSpace *protectionSpace = [challenge protectionSpace];
    if ([protectionSpace authenticationMethod] == NSURLAuthenticationMethodServerTrust) {
    SecTrustRef trust = [protectionSpace serverTrust];

    /***** Make specific changes to the trust policy here. *****/

    /* Re-evaluate the trust policy. */
    SecTrustResultType secresult = kSecTrustResultInvalid;
    if (SecTrustEvaluate(trust, &secresult) != errSecSuccess) {
        /* Trust evaluation failed. */

        [connection cancel];

        // Perform other cleanup here, as needed.
        return;
    }

    switch (secresult) {
        case kSecTrustResultUnspecified: // The OS trusts this certificate implicitly.
        case kSecTrustResultProceed: // The user explicitly told the OS to trust it.
            {
            NSURLCredential *credential =
                [NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust];
            [challenge.sender useCredential:credential forAuthenticationChallenge:challenge];
            return;
            }
        default:
            /* It's somebody else's key. Fall through. */
    }
    /* The server sent a key other than the trusted key. */
    [connection cancel];

    // Perform other cleanup here, as needed.
    }
}
```


The way you override trust for an `NSStream` depends on what you are trying to do.

If all you need to do is specify a different TLS hostname, you can do this trivially by executing three lines of code before you open the streams:

__Listing 4__  Overriding the TLS hostname with `NSStream`

```
        NSDictionary *sslSettings =
                [NSDictionary dictionaryWithObjectsAndKeys:
                        @"www.gatwood.net",
                        (__bridge id)kCFStreamSSLPeerName, nil];
        if (![myInputStream setProperty: sslSettings
            forKey: (__bridge NSString *)kCFStreamPropertySSLSettings]) {
                // Handle the error here.
        }
```

This changes the stream’s notion of its hostname so that when the stream object later creates a trust object, it provides the new name.

If you need to actually alter the list of trusted anchors, the process is somewhat more complex. As soon as the stream object creates a trust object, it evaluates it. If that trust evaluation fails, the stream is closed before your code has the opportunity to modify the trust object. Thus, to override trust evaluation, you must:

- Disable TLS chain validation. Because the stream never evaluates the TLS chain, the evaluation does not fail, and the stream does not close.
- Perform the chain validation yourself in the stream’s delegate (after modifying the trust object appropriately).

By the time your stream delegate’s event handler gets called to indicate that there is space available on the socket, the operating system has already constructed a TLS channel, obtained a certificate chain from the other end of the connection, and created a trust object to evaluate it. At this point, you have an open TLS stream, but you have no idea whether you can trust the host at the other end. By disabling chain validation, it becomes _your_ responsibility to verify that the host at the other end can be trusted. Among other things, this means:

- Do not disable hostname checking by creating a non-TLS policy or passing in a `NULL` pointer for the hostname. If you are intentionally connecting to a host using a hostname other than one of the names listed on its certificate, you should allow the operation only if the certificate you receive from that host is valid for some other domain that _you control_.
- Do not implicitly trust self-signed certificates as anchors (`kSecTrustOptionImplicitAnchors`). Instead, add your own (self-signed) CA certificate to the list of trusted anchors.
- Do not arbitrarily disable other security options, such as checking for expired certificates or roots. There are certain situations where doing so might make sense (such as verifying that a document signed back in 2001 was signed by a certificate that was valid back in 2001), but for networking purposes, the default options should generally be left alone.

With those rules in mind, Listing 5 shows how to use custom TLS anchors with `NSStream`. This listing also uses the function `addAnchorToTrust` from [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknbufvjvomy).

__Listing 5__  Using custom TLS anchors with `NSStream`

```objc
/* Code executed after creating the socket: */

        [inStream setProperty:NSStreamSocketSecurityLevelNegotiatedSSL
            forKey:NSStreamSocketSecurityLevelKey];

    NSDictionary *sslSettings =
        [NSDictionary dictionaryWithObjectsAndKeys:
        (id)kCFBooleanFalse, (id)kCFStreamSSLValidatesCertificateChain,
        nil];

    [inStream setProperty: sslSettings forKey: (__bridge NSString *)kCFStreamPropertySSLSettings];


...


/* Methods in your stream delegate class */

NSString *kAnchorAlreadyAdded = @"AnchorAlreadyAdded";

- (void)stream:(NSStream *)theStream handleEvent:(NSStreamEvent)streamEvent {
    if (streamEvent == NSStreamEventHasBytesAvailable || streamEvent == NSStreamEventHasSpaceAvailable) {
        /* Check it. */

        SecTrustRef trust = (SecTrustRef)[theStream propertyForKey: (__bridge NSString *)kCFStreamPropertySSLPeerTrust];

        /* Because you don't want the array of certificates to keep
           growing, you should add the anchor to the trust list only
           upon the initial receipt of data (rather than every time).
         */
        NSNumber *alreadyAdded = [theStream propertyForKey: kAnchorAlreadyAdded];
        if (!alreadyAdded || ![alreadyAdded boolValue]) {
            trust = addAnchorToTrust(trust, self.trustedCert); // defined earlier.
            [theStream setProperty: [NSNumber numberWithBool: YES] forKey: kAnchorAlreadyAdded];
        }

        SecTrustResultType res = kSecTrustResultInvalid;
        if (SecTrustEvaluate(trust, &res)) {
            /* The trust evaluation failed for some reason.
               This probably means your certificate was broken
               in some way or your code is otherwise wrong. */

            /* Tear down the input stream. */
            [theStream removeFromRunLoop: ... forMode: ...];
            [theStream setDelegate: nil];
            [theStream close];

            /* Tear down the output stream. */
            ...

            return;

        }

        if (res != kSecTrustResultProceed && res != kSecTrustResultUnspecified) {
            /* The host is not trusted. */
            /* Tear down the input stream. */
            [theStream removeFromRunLoop: ... forMode: ...];
            [theStream setDelegate: nil];
            [theStream close];

            /* Tear down the output stream. */
            ...

        } else {
            // Host is trusted.  Handle the data callback normally.

        }
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Resolving%20DNS%20Hostnames.md)

