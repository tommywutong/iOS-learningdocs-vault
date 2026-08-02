---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.063.html
archived_at: '2026-07-15T07:59:03.122526Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Debugging.md)

# Other Changes

- The WebObjects Framework now allows you to save pages in a separate, permanent page cache. This allows you to have pages that remain in the cache; they won't drop out as the page stack is filled by other pages; you no longer have to write custom code to keep toolbars and other "static" pages around. Use WOSession's __savePageInPermanentCache:__ method to save pages in this new cache. Use WOApplication's __setPermanentPageCacheSize:__ and __permanentPageCacheSize__ methods to set and get the size of the permanent page cache (the default size is 30 pages).
- WebScript now supports Objective-C style exception handling. See the WebObjects Developer's Guide for a complete discussion.
- WOStats is now a direct action; it no longer creates a session when you access it, causing the statistics to be thrown off. Access it now with:

```
..../App.woa/wa/WOStats
```

- WebObjects now includes a native adaptor for the Apache web server, as well as a WAI adaptor.
- WOContext's __session__ method will create a new session of one doesn't already exist.
- WOAdaptor's __init__ method now takes an NSDictionary instead of an NSArray. WOApplication's __adaptorWithName:arguments:__ method also takes a dictionary instead of an array.
- WebObjects documentation and examples are now accessible through the WebObjects Info Center, instead of the "WOHomePage." The Info Center is a full-fledged WebObjects application that, in addition to acting as a single point-of-entry to developer documentation and examples, allows you to search the documentation and examples that are on your disk.
- You can now use the debug and profile targets in Project Builder when building your WebObjects applications. Parts of WebObjects-including the WebObjects Framework, the WOExtensions Framework, and MultiScript-are provided in profiled form.
