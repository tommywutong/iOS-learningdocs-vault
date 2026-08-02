---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-8.html
archived_at: '2026-07-15T08:05:07.773993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](WebObjects%20HTTP%20Adaptors.md) [!](Installable%20HTTP%20Adaptors.md) [!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md)

---

# Configuration Files

Web server adaptors obtain configuration information from __wotaskd__
via HTTP requests. Web server adaptors default to __wotaskd__
on __localhost__
, or, when __wotaskd__
cannot be found, the adaptor gets its configuration information from  ___NEXT_ROOT___
__/Local/Library/WebObjects/Configuration/WebObjects.xml__
(___NEXT_ROOT___
is defined at system installation time on Windows NT systems; on Mac OS X Server and similar systems, it is always __/System__
.) This file tells the adaptor what applications are (or should be) running and allows the adaptor to balance transactions among different instances of the same application. This configuration file isn't present on your system by default; if you need it, you'll need to create this file by hand following the format outlined in [Web Server Adaptor Configuration File Format](Web%20Server%20Adaptor%20Configuration%20File%20Format.md#apple-gu3danzr).

In general, you want one configuration file per site. That means if you have multiple machines running WebObjects, you should access all WebObjects applications through a single machine that is running the HTTP server and that contains the configuration file.

If you have multiple HTTP servers running on a single machine, they all share the configuration file. If you want each server to have its own configuration file, you can install one __WebObjects.xml__
file in each server's configuration directory if you a using an API adaptor, or in each server's __cgi-bin__
or __scripts__
directory if you are using the CGI adaptor.

The Monitor application also maintains a configuration file for the purposes of crash recovery; in the event that Monitor fails for any reason, when restarted it reads the file  ___NEXT_ROOT___
__/Local/Library/WebObjects/Configuration/SiteConfig.conf__
in order to restore its state.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](WebObjects%20HTTP%20Adaptors.md) [!](Installable%20HTTP%20Adaptors.md) [!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
