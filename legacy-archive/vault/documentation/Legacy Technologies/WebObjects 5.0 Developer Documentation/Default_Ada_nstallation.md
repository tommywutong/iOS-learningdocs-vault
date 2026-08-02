---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/Default_Ada_nstallation.html
archived_at: '2026-07-15T08:12:11.461742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Confirming__d_Is_Active.md)[!](Building_Ad_From_Source.md)

## Default Adaptor Installation

Depending on your deployment platform, several HTTP adaptors
are installed by default. [Table 3-2](#apple-ijbussciircue) lists the adaptors that are installed on each platform.

__Table
3-2 The adaptors installed in each platform__

__|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Apache | CGI | ISAPI | NSAPI |__| Mac OS X Server | x | x |  |  |
| Solaris | x | x |  | x |
| Windows 2000 |  | x | x | x |

In Mac OS X Server and Solaris, the Apache adaptor is active
by default. Requests in the form `http://.../cgi-bin/WebObjects/` are
handled by the Apache adaptor. If you disable the Apache module,
then such requests are handled by the CGI adaptor.

To install the ISAPI adaptor, copy the `WebObjects.dll` file
to your Web server's scripts directory. The ISAPI adaptor is loaded
into the Web server the first time a request of the form `http://.../scripts/WebObjects.dll/` is
received. It then remains active until the server is stopped.

[!](Confirming__d_Is_Active.md)[!](Building_Ad_From_Source.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
