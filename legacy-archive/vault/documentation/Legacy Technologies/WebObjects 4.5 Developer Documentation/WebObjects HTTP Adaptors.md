---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-4.html
archived_at: '2026-07-15T08:04:57.782513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20WebObjects%20Applications.md) [!](Related%20Documentation.md) [!](CGI%20Adaptors.md)

---

# WebObjects HTTP Adaptors

A key part of WebObjects administration involves dealing with adaptors. This section provides a little background material on what a WebObjects HTTP adaptor is, how it works, and how you can configure it to suit your needs.

A WebObjects HTTP adaptor (called _WebObjects adaptor_
or sometimes _HTTP adaptor_
) routes client requests processed by an HTTP server to WebObjects applications and returns the response to the server, which sends them back to the client. WebObjects makes available several adaptors, of which only one can be active with a particular server at a time. Every transaction with a WebObjects application uses the currently active adaptor.

The relationships between adaptor and application are, potentially, many-to-many. Multiple instances of the same WebObjects application can run on the same machine or on a variety of machines and communicate with the same adaptor. In addition, multiple HTTP servers can be running on the same machine or on different machines; each server can have its own adaptor, each with its own constellation of application instances. Although there can be only one active HTTP adaptor per HTTP server, an application can concurrently communicate with other types of adaptors, such as an adaptor that uses Distributed Objects or a secure-socket adaptor.

There are two general types of HTTP adaptors, CGI adaptors and API-based adaptors. When WebObjects is installed, the CGI adaptor is made active by default. To use an API-based adaptor, you must specifically activate it. Activating the API-based adaptor deactivates the CGI adaptor for a particular server. To activate an API-based adaptor, build and install it using the instructions found in __BuildingInstructions.html__
and __InstallationInstructions.html__
(both are located in  ___NEXT_ROOT___
__/Developer/Examples/WebObjects/Source/Adaptors/__
).

#### [CGI Adaptors](CGI%20Adaptors.md#apple-obtwmslefu4tmnbr)

#### [API-based Adaptors](API-based%20Adaptors.md#apple-obtwmslefu4tmnbs)

#### [Installable HTTP Adaptors](Installable%20HTTP%20Adaptors.md#apple-obtwmslefu4tonbs)

#### [Configuration Files](Configuration%20Files.md#apple-obtwmslefu2dmmbq)

#### [Automatic Discovery of WebObjects App Servers](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md#apple-obtwmslefuytanjrgi)

#### [Web Server Adaptor Configuration File Format](Web%20Server%20Adaptor%20Configuration%20File%20Format.md#apple-obtwmslefu4tqmrz)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20WebObjects%20Applications.md) [!](Related%20Documentation.md) [!](CGI%20Adaptors.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
