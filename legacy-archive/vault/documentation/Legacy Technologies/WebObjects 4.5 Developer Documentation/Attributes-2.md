---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-15.html
archived_at: '2026-07-15T08:04:40.195722Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Sections.md) [!](Sample%20Configuration%20File.md)

---

# Attributes

The various attributes used throughout the configuration file are defined as follows:

retries=_NUMBER_

> Specifies the _NUMBER_ of times to try a request against an application (trying several instances) before returning an error.

scheduler=["random"|"roundrobin"|"loadaverage"]

> Specifies which load balancing algorithm to use to select an application instance

dormant=_NUMBER_

> If an instance doesn't respond, do not try to contact it for this many subsequent requests

protocol="http"

> The RPC protocol to use to the application. Currently only HTTP is supported.

transport=["socket"|"fsocket"|"winsock"|"nssocket"]

> The socket API used to contact an instance. "socket" indicates simple, cross platform, unbuffered sockets. "fsocket" specifies sockets buffered using fopen(), fread(), fwrite() & such (valid on Unix only). "winsock" specifies Win32 socket API (valid on NT only). "nssocket" indicates Netscape's NSAPI socket API (NSAPI only).

redir=URL

> If an error occurs during request processing, return a redirect (302) HTTP response with URL as the location

xyzzy=_STRING_

> Return a page reporting some adaptor details when a request for this application arrives

confinterval=_NUMBER_

> How often, in seconds, the adaptor should check to see if the configuration has changed

timeout=_NUMBER_

> Default for sendTimeout, recvTimeout and cnctTimeout

sendTimeout=_NUMBER_

> Timeout, in seconds, before reporting a failed send() to an instance

recvTimeout=_NUMBER_

> Timeout, in seconds, before reporting a failed recv() from an instance

cnctTimeout=_NUMBER_

> Timeout, in seconds, before reporting a failed connect() to an instance

poolSize=_NUMBER_

> _NUMBER_ of persistent connections to maintain with an instance

sendBufSize=_NUMBER_

> Size of the TCP/IP socket send buffer (in bytes) that's used for adaptor-to-web-app communication

recvBufSize=_NUMBER_

> Size of the TCP/IP socket receive buffer (in bytes) that's used for adaptor-to-web-app communication

urlVersion=["3"|"3.5"|"4"]

> The WebObjects version to use for URL parsing and formatting

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Sections.md) [!](Sample%20Configuration%20File.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
