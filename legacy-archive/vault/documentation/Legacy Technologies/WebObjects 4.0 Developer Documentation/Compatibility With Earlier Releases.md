---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.01.html
archived_at: '2026-07-15T07:58:19.772144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](What%27s%20New%20in%20WebObjects%204.0.md)

# Compatibility With Earlier Releases

WebObjects 4.0 is backward compatible to WebObjects 3.5. However, you must keep in mind the following:

- WebObjects 4.0 is the first release of WebObjects that runs on Mac OS X Server and Yellow Box for Windows NT. It does not run on OpenStep 4.2. Because of this change, the locations of WebObjects files have changed. See [File Location Changes](File%20Location%20Changes.md#apple-giytcmrv).
- Because Mac OS X Server and Yellow Box are not upgrades to OpenStep for Mach and OpenStep Enterprise, respectively, their underlying frameworks are not necessarily upwardly-compatible. In particular, the Foundation framework supplied with Mac OS X Server and Yellow Box isn't upwardly-compatible. As one example, NSArray's makeObjectsPerform: method doesn't exist in the versions of Foundation that ship with Mac OS X Server and Yellow Box.
- The file location changes require some changes to your Project Builder projects. See [Converting an Existing WebObjects Application](Converting%20an%20Existing%20WebObjects%20Application.md#apple-giydsnzt).
- Yellow Box uses a different version of the Java-wrapped APIs. The package names, class names, and some method names have changed. There are scripts to help you convert your Java code. See [Converting an Existing WebObjects Application](Converting%20an%20Existing%20WebObjects%20Application.md#apple-giydsnzt).
- WebObjects applications are launched differently in WebObjects 4.0, as described in [Running an Application on WebObjects 4.0](Running%20an%20Application%20on%20WebObjects%204.0.md#apple-giytemzq).
- The WebObjects Framework contains many new optimizations that should greatly improve your application's performance. However, you may find your code relied on some part of the request-response loop or template parsing code that is no longer always performed. If so, there are compatibility flags to disable these optimizations. These flags are described in [Converting an Existing WebObjects Application](Converting%20an%20Existing%20WebObjects%20Application.md#apple-giydsnzt).
- The default adaptor now supports multithreaded request handling. This change should have no effect on your running application other than to make resource loading faster.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Converting%20an%20Existing%20WebObjects%20Application.md)
