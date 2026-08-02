---
title: iOS 5 and TLS 1.2 Interoperability Issues
apple_id: DTS40011309
resource_type: Technical Note
platform: iOS
topic: Security
technology: null
published: '2011-10-14'
source_url: https://developer.apple.com/library/archive/technotes/tn2287/_index.html
archived_at: '2026-07-26T19:54:10.121011Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2287

# iOS 5 and TLS 1.2 Interoperability Issues

iOS 5's TLS implementation has been upgraded to support TLS protocol version 1.2. Some non-compliant TLS server implementations do not handle TLS 1.2 and do not downgrade gracefully to a supported protocol version. This Technical Note explains the extent of this interoperability issue and how to work around it.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqhewugsbrfvke4vcbi4yq)[Workarounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqhewugsbrfvke4vcbi4za)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

iOS 5's TLS implementation has been upgraded to support TLS protocol version 1.2. Some non-compliant TLS server implementations do not implement TLS 1.2 and, more importantly, do not downgrade gracefully to a supported protocol version. As a result you may find that some TLS client applications built against the iOS 5 SDK may not connect to some TLS servers, when the same application built against a previous version of the iOS SDK would connect.

If your application implements a TLS client using the CFStream APIs or the SecureTransport APIs, it will now default to using a TLS 1.2 handshake when connecting to a TLS server. Compliant TLS server implementations that do not support the TLS 1.2 protocol version will signal the client to downgrade to a supported protocol version. By default, the iOS 5 TLS implementation will allow the server to downgrade as far as the SSL 3 protocol version. On the other hand, a non-compliant TLS server implementation may, upon receiving a TLS 1.2 handshake, simply terminate the TLS handshake or connection.

Affected servers include, but are not limited to, any servers implemented using the SecureTransport or CFStream APIs and running on any currently released Mac OS X system or iOS device prior to iOS 5.0.

[Back to Top](#)

## Workarounds

To workaround non-compliant server implementations, TLS clients should try to reconnect using a lower protocol version until the connection succeeds or all allowable protocol versions have failed.

This workaround is implemented at the NSURLConnection layer, so that TLS clients implemented on top of NSURLConnection—and things that use NSURLConnection, like UIWebView—should not be affected.

TLS client apps implemented using the CFStream APIs and linked against iOS SDK prior to iOS 5 SDK will keep using TLS 1.0 as the default protocol version, and should not be affected.

For TLS clients implemented directly using the SecureTransport APIs (only available starting with iOS 5.0 SDK), developers should use the `SSLSetProtocolVersionMax` and `SSLSetProtocolVersionMin` APIs to specify the allowed TLS protocol versions. The handshake will be attempted using the maximum version specified.

For TLS clients implemented using the CFStream APIs, developers can set the maximum protocol version using the `CFReadStreamSetProperty` API as shown in Listing 1

__Listing 1__  How to set the TLS protocol version on CFStream and CFHTTPStream.

```
// Use the following code to configure CFStream (e.g., CFStreamCreatePairWithSocketToHost)
// or CFHTTPStream (e.g., CFReadStreamCreateForHTTPRequest) based read streams to connect
//  with specific TLS protocol versions.
// Insert before calling CFReadStreamOpen().

const void* keys[] = { kCFStreamSSLLevel };
// New CFString values available only on iOS 5:
// (if these values are used on versions before iOS 5, then will
//    default to max TLS 1.0, min SSLv3)
// kCFStreamSocketSecurityLevelTLSv1_0SSLv3 configures max TLS 1.0, min SSLv3
// (same as default behavior on versions before iOS 5).
// kCFStreamSocketSecurityLevelTLSv1_0 configures to use only TLS 1.0.
// kCFStreamSocketSecurityLevelTLSv1_1 configures to use only TLS 1.1.
// kCFStreamSocketSecurityLevelTLSv1_2 configures to use only TLS 1.2.
const void* values[] = { CFSTR("kCFStreamSocketSecurityLevelTLSv1_0SSLv3") };
CFDictionaryRef sslSettingsDict = CFDictionaryCreate(kCFAllocatorDefault, keys, values, 1,
                                                     &kCFTypeDictionaryKeyCallBacks,
                                                     &kCFTypeDictionaryValueCallBacks);
CFReadStreamSetProperty(myStream, kCFStreamPropertySSLSettings, sslSettingsDict);
CFRelease(sslSettingsDict);
```

__Important:__ The socket security level constants shown in Listing 1 are not yet defined in `<CFNetwork/CFSocketStream.h>`
(r. [10229865](rdar://problem/10229865))
. For the moment you should use a literal string, as illustrated by the listing.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-10-14 | New document that describes a TLS interoperability issue between iOS 5 clients and some servers implementations, and suggests a workaround. |

