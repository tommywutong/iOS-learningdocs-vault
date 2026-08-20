---
title: How to securely serve Key files for HTTP Live Streaming with HTTPS
apple_id: DTS40009204
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: null
published: '2009-08-27'
source_url: https://developer.apple.com/library/archive/qa/qa1661/_index.html
archived_at: '2026-07-18T02:33:22.418796Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1661

# How to securely serve Key files for HTTP Live Streaming with HTTPS

## Q:  I'm streaming live media over HTTP to iPhone 3.0 from my web server. I've also turned on the media encryption, but I am concerned because the key file is being delivered unprotected over HTTP. I tried serving the key file using HTTPS, but the iPhone will no longer play the stream. Can I serve the key file using HTTPS? If so, what do I need to do in order for this to work?

A: Yes, you can serve key files using either HTTP or HTTPS. Here's a brief overview.

Before moving from HTTP to HTTPS you should first test by serving the key from an internal HTTP server. If this fails, you should debug your encryption setup before moving on.

When setting up your HTTPS server, the SSL Server Certificate must be trusted.

If your HTTPS server does not have an SSL certificate signed by a trusted authority you should create a self-signed SSL Certificate Authority for testing and a leaf certificate for your server. Attach the certificate for the certificate authority to an email, send it to yourself on the device and tap on the attachment in Mail to make the device trust the server.

If serving the key via HTTP succeeds, but serving via HTTPS fails, there may be a problem with your SSL certificate.

Next, introduce your authentication scheme. There is a hitch: the authentication domain of the very first playlist file must match that of the keys. One option is to serve the variant playlist over HTTPS from the same domain, since it is only read once - and serve individual variants over HTTP.

Note that since live streaming over HTTP does not bring up interactive dialogs, you will need to store credentials, whether cookie-based authentication or HTTP Digest authentication. Refer to [Using NSURLConnection](https://developer.apple.com/documentation/Cocoa/Conceptual/URLLoadingSystem/Tasks/UsingNSURLConnection.html), particularly the section [Handling Authentication Challenges](https://developer.apple.com/documentation/Cocoa/Conceptual/URLLoadingSystem/Tasks/UsingNSURLConnection.html#//apple_ref/doc/uid/20001836-160393). The credentials you supply in the `didReceiveAuthenticationChallenge` callback will be cached and reused by the media player.

Finally, before deployment, you will need to install an SSL certificate signed by a trusted authority on your server (so your clients will not have to manually install the server's certificate).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-08-27 | New document that discusses how to serve key files for HTTP Live Streaming with HTTPS |

