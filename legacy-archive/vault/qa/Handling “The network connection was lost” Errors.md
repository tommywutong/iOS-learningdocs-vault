---
title: Handling “The network connection was lost” Errors
apple_id: DTS40017602
resource_type: QA
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2017-01-25'
source_url: https://developer.apple.com/library/archive/qa/qa1941/_index.html
archived_at: '2026-07-18T02:37:25.096544Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1941

# Handling “The network connection was lost” Errors

## Q:  My app is seeing `NSURLErrorNetworkConnectionLost` errors returned by NSURLSession. How should I handle these errors?

A: `NSURLErrorNetworkConnectionLost` is error -1005 in the `NSURLErrorDomain` error domain, and is displayed to users as “The network connection was lost”. This error means that the underlying TCP connection that’s carrying the HTTP request disconnected while the HTTP request was in progress (see below for more information about this). In some circumstances NSURLSession may retry such requests automatically (specifically, if the request is idempotent) but in other circumstances that’s not allowed by the HTTP standards.

It’s easy to understand why this restriction is important. Consider a `POST` request that triggers a bank transfer. If NSURLSession has started transmitting the request and then the connection fails, it can’t distinguish between the following cases:

- The request never made it to the server, and thus it’s safe to retry
- The request made it to the server but the response never made it back to the client, and thus a retry would be bad

Given the above, the correct way to handle `NSURLErrorNetworkConnectionLost` depends on the type of request:

- Requests that are idempotent can simply be retried. You might attempt an immediate retry, just in case there was a transient failure, and then back off to using whatever general retry logic is appropriate for your app (time based, triggered by the user, triggered by a reachability query, and so on).
- For non-idempotent requests, you’ll need request-specific retry logic.

  To continue the example above, one approach would be for the app to associate a unique ID with each bank transfer. Then, if the request fails, the app can query the server to see if a transfer with that unique ID exists. If not, it can safely retry the request.

For this to work you must make sure that you use the right HTTP method for each request. There are two ways this can go wrong:

- If you use a non-idempotent HTTP method for an idempotent request, NSURLSession will not retry the request even though it could safely do so. This isn’t a serious problem; you can just retry the request yourself.
- If you use an idempotent HTTP method for a non-idempotent request, that’s very bad. NSURLSession might retry the request even though doing so is unsafe. The only valid solution here is to change your request to use a different HTTP method, which may require server-side changes.

Finally, as an app developer it’s reasonable to expect a small number of `NSURLErrorNetworkConnectionLost` errors caused by problems with the underlying network. However, if you’re seeing a large number of these errors, and especially if they are raised in environments with good network connectivity, there might be a problem with NSURLSession talking to your server. You can investigate that by looking at the on-the-wire traffic to see whether there’s an obvious underlying cause for these errors, for example, your server actually closing connections unexpectedly.

For information about how to look at the on-the-wire traffic, see _[Getting a Packet Trace](https://developer.apple.com/library/archive/qa/qa1176/_index.html#//apple_ref/doc/uid/DTS10001707)_. You can also use the techniques described in _[CFNetwork Diagnostic Logging](https://developer.apple.com/library/archive/qa/qa1887/_index.html#//apple_ref/doc/uid/DTS40015177)_ to look at NSURLSession’s internal state.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-01-25 | New document that describes how to handle the NSURLErrorNetworkConnectionLost error. |

