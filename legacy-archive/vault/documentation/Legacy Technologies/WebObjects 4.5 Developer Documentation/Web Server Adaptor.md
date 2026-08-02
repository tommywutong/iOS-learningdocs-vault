---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-10.html
archived_at: '2026-07-15T08:04:37.710794Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md) [!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md) [!](wotaskd.md)

---

# Web Server Adaptor

The adaptor sends discovery requests out on a particular multicast "channel" (IP address + port). The defaults are:

Default IP Address: 239.128.14.2

Default port: 1085

The default multicast address is within the "Adminstratively Scoped Domain." That is, it's within the range of addresses intended for internal use inside organizations.

For Apache, place the following in your apache.conf (the final value--10 in this instance--indicates the configuration refresh interval):

`WebObjectsConfig webobjects://239.128.14.2:1085 10`

For CGI, either recompile, or set the WO_CONFIG_URL environment variable as above.

__Note:__ With Apache, you'll need the SetEnv command, which comes with the "env" module. Note that Mac OS X Server doesn't switch this module on by default.

For NSAPI, place something like the following in your obj.conf:

__Standard:__

`Init fn="WebObjects_init" root="/opt/ns-home/docs"
 config="http://localhost:1085"`

__Multicast:__

`Init fn="WebObjects_init" root="/opt/ns-home/docs"
 config="webobjects://239.128.14.2:1085"`

For ISAPI, add the following to the registry:

`\\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_URL
 webobjects://239.128.14.2:1085`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md) [!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md) [!](wotaskd.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
