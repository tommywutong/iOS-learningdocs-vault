---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-33.html
archived_at: '2026-07-15T08:04:54.277552Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Monitor%20Option%20Summary.md) [!](Host%20Configuration.md) [!](Instance%20Configuration%20Options.md)

---

# Application Configuration Options

The Application Configuration page allows you to configure general aspects of an application. It lists the options described below. To access the Application Configuration page, click the Applications button on the Monitor banner, then click the Config button next to any application.

#### New Instance Defaults

In this section you can specify a set of default arguments that Monitor uses when it creates new instances of the application. Most of these arguments are the normal command-line options used to configure an instance of a WebObjects application (see [Starting Up Applications From the Command Line](Deploying-29.md#apple-ge3tkmjv) for descriptions of these options). Two options, Auto Recover and Minimum Active Sessions, are not command-line options but are deployment settings that Monitor uses for determining starting and stopping policy.

[Setting Command-Line Arguments in Monitor](Setting%20Command-Line%20Arguments%20in%20Monitor.md#apple-gqydsmrz) discusses how to set launch options using Monitor.

#### Scheduling

This section enables the administrator to configure an application's pool of instances (you must have more than one instance running) to conform to a staggered schedule of starting, running for a period of time, begin refusing new sessions, and shutting down when the minimum active session threshold is reached.

See [Automatic Scheduling](Automatic%20Scheduling.md#apple-geytgnzt) for instructions on setting the shutdown and startup schedules for all instances of an application as well as specific instances.

#### E-Mail Notifications

If the SMTP server has been set in Monitor's Global Configuration page (see "[Global Configuration](Global%20Configuration.md#apple-gi4tambz)" on [Global Configuration](Global%20Configuration.md#apple-gi4tambz)) then an application can specify a list of electronic-mail addresses to send an mail to when an instance fails unexpectedly. This list should be comma delimited (for example, "jdoe@somewhere.com, mpublic@else.com, foo@bar.com").

The mail message contains the application name, host, port, and date and time of the failure.

To turn off the email feature, delete all addresses from the text field and click Update.

#### Load Balancing and Adaptor Settings

This section is where you specify default values for individual applications (many of these settions can be overridden for individual instances). These settings override the corresponding settings made for a given host.

__Load balancing scheme__
: Specifies which load balancing algorithm to use to select an application instance.

__Failover mode__
: Allows you to specify what should happen when an error occurs: report the error to the client, retry the same instance, or try another instance (which one is determined by the load balancing scheme).

__Transport__
: The socket API used to contact an instance. "socket" indicates simple, cross platform, unbuffered sockets. "fsocket" specifies sockets buffered using fopen(), fread(), fwrite() & such (valid on Unix only). "winsock" specifies Win32 socket API (valid on NT only). "nssocket" indicates Netscape's NSAPI socket API (NSAPI only).

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

Click Change Adaptor Settings to cause changes in any of these settings to take affect.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Monitor%20Option%20Summary.md) [!](Host%20Configuration.md) [!](Instance%20Configuration%20Options.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
