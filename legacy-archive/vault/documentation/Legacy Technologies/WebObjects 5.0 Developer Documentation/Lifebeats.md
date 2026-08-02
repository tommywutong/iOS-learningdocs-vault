---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/Lifebeats.html
archived_at: '2026-07-15T08:12:10.448895Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Configuration_Files.md)[!](wotaskd_Processes.md)

## Lifebeats

After adding an application to your site, you need to add
instances of it as well. This allows the application's users connect
to it. One of the main goals of WebObjects Deployment is to provide
you with tools that help you deploy a resilient site. To accomplish
that, wotaskd restarts application instances that become unresponsive.

A __lifebeat__ is a status message that an
application instance sends to a wotaskd process to keep it informed
of the instance's status. There are four kinds of lifebeats:

- has started
- is alive
- will stop
- will crash

An application instance is configured by default to send lifebeats
to a wotaskd process through TCP (Transmission Control Protocol)
sockets. (A __socket__ is a mechanism through which
two processes communicate.) Instances can also send lifebeats using
UDP (User Datagram Protocol) sockets. UDP sockets use fewer resources
than TCP sockets.

The lifebeat mechanism is how the state of your site is constantly
updated. Lifebeats are sent from a separate execution thread in
a WebObjects application and do not interfere with, nor are they
affected by, normal request processing.

By default, application instances try to send a lifebeat every
30 seconds. If a failure occurs (there is no wotaskd process listening
on the `WOLifebeatDesinationPort`),
the instance does the following:

1. Sends up
   to 10 TCP lifebeats until a response is received.

   After the
   tenth unanswered lifebeat, the instance goes to stage 2.
2. Sends UDP lifebeats (low-resource lifebeat mode) until a response
   is received.

   If the instance cannot create a UDP socket, it
   goes back to stage 1.

   When the instance receives an
   acknowledgement, it resumes sending TCP lifebeats.

The two-stage mechanism allows application instances to go
into low-resource lifebeat mode if wotaskd isn't running when
the instance starts.

[!](Configuration_Files.md)[!](wotaskd_Processes.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
