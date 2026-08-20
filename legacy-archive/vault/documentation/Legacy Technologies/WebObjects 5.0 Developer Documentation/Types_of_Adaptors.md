---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/Types_of_Adaptors.html
archived_at: '2026-07-15T08:12:19.041053Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Adaptors_Ap_s_and_Hosts.md)[!](State_Discovery.md)

## Types of Adaptors

There are two general types of HTTP adaptors, __CGI
adaptors__ and __API-based adaptors__. CGI
adaptors are portable across many platforms. API-based adaptors
are generally more efficient than CGI adaptors.

### CGI Adaptors

WebObjects Deployment includes a CGI adaptor, which is an
executable file named `WebObjects`;
in Windows 2000, it's named `WebObjects.exe`.
The CGI adaptor resides in the Web server's cgi-bin or scripts directory.
This adaptor works with any Web server that conforms to the CGI
standard.

The major drawback of CGI adaptors is their performance. When
the Web server receives a request from a browser, it creates a new
process for the adaptor. When the adaptor is done processing the
request, the process is terminated.

The CGI adaptor is installed by default on all platforms,
but it may not be the active one on your platform. See ["Default Adaptor Installation"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/iDefault_Ada_nstallation.html) for
more information.

### API-Based Adaptors

API-based adaptors are based on APIs specific to a particular
Web server. They allow CGI-like tasks to run as part of the main
server process, avoiding the creation and termination of a process
for each request. [Table 4-1](#apple-ijbegrkji5fem) lists the API-based adaptors included with WebObjects
and the platforms on which they are supported.

__Table
4-1 API-based adaptors and supported platforms__

__|  |  |  |
| --- | --- | --- |
| Adaptor | API | Supported platforms |__| Apache | Apache's module API | Mac OS X Server Solaris |
| ISAPI | Microsoft's Internet Information Server API | Windows 2000 |
| NSAPI | Netscape Server 3.5 API | Solaris Windows 2000 |

[!](Adaptors_Ap_s_and_Hosts.md)[!](State_Discovery.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
