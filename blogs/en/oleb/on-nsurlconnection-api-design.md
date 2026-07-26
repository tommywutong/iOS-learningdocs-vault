---
title: On NSURLConnection API Design
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/07/nsurlconnection-api-design/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4d0f6a7ccf18a9ce'
translated: false
---

> 原文：[On NSURLConnection API Design](https://oleb.net/blog/2013/07/nsurlconnection-api-design/)　·　Ole Begemann

# On NSURLConnection API Design

Today I learned that Apple’s [`NSURLConnection`](https://developer.apple.com/library/ios/#documentation/cocoa/Reference/Foundation/Classes/NSURLConnection_Class/Reference/Reference.html) class was originally written for the [first release of Safari](https://donmelton.com/2013/01/10/safari-is-released-to-the-world/) in 2003.^[1](#fn:1) I had always wondered why the `NSURLConnection` API was designed as it is. Now that I know it was specifically designed for a web browser, it suddenly makes much more sense.

# Web Browsers vs. Talking to Web Services

Over the last ten years, very few users of `NSURLConnection` have probably used it to actually implement a web browser. The large majority of developers use the API to talk to a web service of some kind. These are two very different use cases with vastly different requirements:

- A web browser does not need to distinguish between HTTP status codes.^[2](#fn:2) Regardless whether the response’s status code is 200, 404 or 500, the browser can always get away with displaying the response body. Consequently, `NSURLConnection` reports a 404 response as success. In contrast, a web service client needs to handle a 4xx or 5xx response as an error.
- A web browser can profit from a URL loading system that is [extensible and customizable with new URL schemes](https://developer.apple.com/library/ios/#documentation/cocoa/Reference/Foundation/Classes/NSURLProtocol_Class/Reference/Reference.html). This functionality is useless to a web service client.
- A web browser needs to [handle cookies](http://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSHTTPCookieStorage_Class/Reference/Reference.html), again something that web service clients generally do not care about.

The original goals for `NSURLConnection` still show in its API design today. Contrast this with a modern networking library like [AFNetworking](https://github.com/AFNetworking/AFNetworking), which has been designed from the start with web services in mind. Consequently, it handles HTTP 4xx and 5xx status codes as errors and comes with an extensible system for dealing with different response types like XML, JSON or images.

It’s no wonder there are so many third-party networking libraries for Cocoa because the built-in API is arguably not the perfect fit for the most common use cases.

# Design Your API for the Most Important Use Case

API design is very much influenced by the goal the API is intended to accomplish. This is, of course, hardly a surprise and definitely not a bad thing. When designing your own API, it helps to define this goal explicitly. Make sure your design makes implementing the most common use cases you expect especially easy. When you find yourself having a hard time grasping an API others have written, learning about their original design goal may help you better understand why the API has been designed in a particular way.

1. Source: WWDC 2013 session 705. [↩︎](#fnref:1)
2. Redirects are an exception. It’s no surprise then that `NSURLConnection` can handle HTTP redirects automatically. [↩︎](#fnref:2)
