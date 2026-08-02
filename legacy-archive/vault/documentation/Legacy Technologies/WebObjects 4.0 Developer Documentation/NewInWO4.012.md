---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.012.html
archived_at: '2026-07-15T07:58:26.737131Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.011.md)

## Changes to Adaptor Configuration Files

The format of the private and public configuration files (__WebObjects.conf__) has changed slightly. Along with this format change come two conceptual changes:

- Entering the path to the WebObjects adaptor in the browser (usually __http://localhost/cgi-bin/WebObjects__) used to provide a list of applications you had installed under the document root. Selecting one of these applications took you to it, autostarting the application if necessary.

Because the adaptor can no longer autostart applications, entering the path to the adaptor now takes you to a list of already running applications.

- You no longer specify the application instance number on the command line. The instance number and the host name are now private to the __WebObjects.conf__ file.

If a client browser tries to access an application instance that isn't running, the adaptor attempts to perform load-balancing with all existing instances. For example, suppose a user bookmarked a URL that contained 4 as the instance number and tried to use that bookmark two weeks later when instance 4 is no longer running. Instead of failing, WebObjects simply uses one of the instances that is running.

### The Application Instance Number

For security reasons, an application instance's host name and port number cannot be visible either in a page or in a URL. There is a one-to-one mapping between these values and an application's instance number in the __WebObjects.conf__ file; this mapping is resolved by the adaptor. Because it is a one-to-one mapping, the instance number must be unique across a deployment environment for a given application name.
When the adaptor load-balances a request to an application at a given port and host, it assigns an application instance number and places it into the request . (Because of this, you now obtain the application instance number from the WORequest rather than from the WOApplication object.) Application instances take the instance number from the request and send that number back in the response URLs. As far as the application instance is concerned, the instance number could change with every request-the application instance wouldn't notice.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.013.md)
