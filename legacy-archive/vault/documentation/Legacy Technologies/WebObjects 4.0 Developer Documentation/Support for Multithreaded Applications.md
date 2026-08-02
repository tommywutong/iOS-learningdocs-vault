---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.014.html
archived_at: '2026-07-15T07:58:27.711909Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.013.md)

# Support for Multithreaded Applications

In release 4.0, WebObjects and Enterprise Objects Framework provide thread-safe APIs. This means that you can write a multithreaded WebObjects application where you couldn't before.
To support multithreaded applications, there are two major changes:

- The default adaptor has been rewritten to support multithreaded request handling. By default, this adaptor does multithreaded adaptor I/O and resource handling, but only single-threaded request handling. If you rewrite your application so that it is thread safe, locking any access to shared resources as necessary, you can enable concurrent request handling. To rewrite your application to be thread safe, you'll also need to remove all invocations of some deprecated API; see "[Deprecated API](NewInWO4.015.md#apple-giytknzz)," below, for more information. To enable concurrent request handling, override the __allowsConcurrentRequestHandling__ method in your application class to return __YES__ or __true__.

The default adaptor can be made to operate in single-threaded mode by setting the __WOWorkerThreadCount__ command-line option to 0.

- Certain method names have changed. You can still use the old methods, but their use is deprecated.

For information on multithreading Enterprise Objects Framework operations, see "[What's New in Enterprise Objects Framework 3.0](What%27s%20New%20in%20Enterprise%20Objects%20Framework%203.0.md)".

The rest of this section lists the methods that have changed and describes new methods that you can use to ensure that your application is thread-safe.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.015.md)
