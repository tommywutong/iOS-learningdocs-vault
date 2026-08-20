---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-31.html
archived_at: '2026-07-15T08:04:53.252546Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Monitor%20Option%20Summary.md) [!](Monitor%20Option%20Summary.md) [!](Host%20Configuration.md)

---

# Global Configuration

The Global Configuration page allows you to configure aspects of Monitor and your site that are not specific to an application. It lists the options described below. Click the Configure button in the Monitor banner to display the Global Configuration page.

#### Monitor Password

In this section specify a password that is required to access Monitor. Monitor does not have a password set by default. After you set a password Monitor prompts users for it each time they access the application.

#### HTTP Server and WebObjects Adaptor

You use this section primarily to specify the URL that points to the adaptor on your deployment's web server. Monitor uses this URL to construct more URLs that direct the administrator to running instances, the WOStats page, and other destinations.

#### Adaptor Settings

This section is where you specify global default values for applications and instances (many of these settions can be overridden for individual applications or instances). Attribute values defined here apply to global adaptor behavior and apply to all applications.

__Load balancing scheme__
: Specifies which load balancing algorithm to use to select an application instance.

__Transport__
: The socket API used to contact an instance. "socket" indicates simple, cross platform, unbuffered sockets. "fsocket" specifies sockets buffered using fopen(), fread(), fwrite() & such (valid on Unix only). "winsock" specifies Win32 socket API (valid on NT only). "nssocket" indicates Netscape's NSAPI socket API (NSAPI only).

__Adaptor stats string__
: Return a page reporting some adaptor details when a request for this application arrives.

__Configuration read interval__
: How often, in seconds, the adaptor should check to see if the configuration has changed.

__Retries__
: Specifies the number of times to try a request against an application (trying several instances) before returning an error.

__Redirection URL__
: If an error occurs during request processing, return a redirect (302) HTTP response with the specified URL as the location.

__Timeout__
: Default for Send Timeout, Receive Timeout, and Connect Timeout.

__Send timeout__
: Timeout, in seconds, before reporting a failed send() to an instance.

__Receive timeout__
: Timeout, in seconds, before reporting a failed recv() from an instance.

__Connect timeout__
: Timeout, in seconds, before reporting a failed connect() to an instance.

__Connection pool size__
: Number of persistent connections to maintain with an instance.

Click Change Adaptor Settings to cause changes in the above settings to take effect.

#### Auto-Recover Settings

This configuration option allows you to have an additional level of recovery outside the per-instance Auto-Recover feature. This feature restarts application instances after they fail. When __wotaskd__
decides that an instance has crashed, it checks the instance's auto-recover setting to see if it should start a new instance. With the global auto-recover option enabled, when __wotaskd__
is started (perhaps when a machine is booted) it will locate all instances configured to be auto-recovered and start them if they are not running. This allows you to have a machine that has failed to boot up, start __wotaskd__
, and then have __wotaskd__
start all the appropriate applications.

When this setting is on, __wotaskd__
perform this check on regular intervals. If __wotaskd__
fails or you change an instance's Auto-Recover setting, __wotaskd__
launches the appropriate instances within 45 seconds.

#### E-Mail Notification

In this section you specify an SMTP server that Monitor uses to send e-mail to a set of addresses when application instances fail unexpectedly. In order for Monitor to send e-mail it requires the name or IP Address of an SMTP server.

#### Detail View

In this section you can set the interval at which the Detail View page is automatically refreshed.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Monitor%20Option%20Summary.md) [!](Monitor%20Option%20Summary.md) [!](Host%20Configuration.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
