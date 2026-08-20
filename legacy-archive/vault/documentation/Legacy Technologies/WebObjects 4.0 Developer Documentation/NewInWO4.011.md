---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.011.html
archived_at: '2026-07-15T07:58:26.332173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.010.md)

## "Serverless" Applications

WebObjects 4.0 applications can receive HTTP requests directly. Previously, a web server had to be running to receive HTTP requests and to forward them through the WebObjects adaptor.
To run a WebObjects application when no HTTP server is present, you simply specify the number of the port where the application should receive requests using the __WOPort__ option. By default, __WOPort__ is -1, which assigns an arbitrary high port number to the application. Thus, if you specify no port number at all, you can still run your application without a web server.
This new feature has several advantages:

- You can debug applications on a machine that doesn't have a web server present.
- You don't have to install project directories under the document root to test them.
- Running without an HTTP server uses less memory on your development machine.
- The WebObjects example applications no longer need to be installed under the web server's document root. Instead they are installed under __Developer/Examples/WebObjects__.

Note that if you do want to use a web server to test WebObjects examples, you can still do so. Before you do, do a "make install" to install the example's web server resources (such as image files and Java client-side classes) in the document root, just as you do when installing a WebObjects application. If you put your application in a directory other than "WebObjects" under your document root, set the __WOApplicationBaseURL__ option to the __.woa__ directory's path relative to the document root (__WOApplicationBaseURL__ is set to __/WebObjects__ by default). If you don't perform these steps, the web server won't be able to find web server resources; when you run the application, you'll see broken images, and client-side classes won't be loaded. (See [Rapid Turnaround Mode](Rapid%20Turnaround%20Mode.md#apple-gm3dcnbq) for more on developing with and without a web server.)

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.012.md)
