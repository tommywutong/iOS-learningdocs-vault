---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-13.html
archived_at: '2026-07-15T08:04:39.196882Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Sections.md)

---

# XML Format in Full

The following is a complete definition of the XML-format configuration file, showing all possible attributes and values.

`<!DOCTYPE WebObjectsAdaptorConfiguration SYSTEM "woadaptor.dtd">`
``

`<adaptor
 retries=NUMBER
 scheduler=["random"|"roundrobin"|"loadaverage"]
 dormant=NUMBER
 protocol="http"
 transport=["socket"|"fsocket"|"winsock"|"nssocket"]
 redir=URL
 xyzzy=STRING
 confinterval=NUMBER
 timeout=NUMBER
 sendTimeout=NUMBER
 recvTimeout=NUMBER
 cnctTimeout=NUMBER
 poolSize=NUMBER
 sendBufSize=NUMBER
 recvBufSize=NUMBER
 urlVersion=["3"|"3.5"|"4"]
>
</adaptor>
<application
 name=STRING
 retries=NUMBER
 scheduler=["random"|"roundrobin"|"loadaverage"]
 dormant=NUMBER
 protocol="http"
 transport=["socket"|"fsocket"|"winsock"|"nssocket"]
 redir=URL
 timeout=NUMBER
 sendTimeout=NUMBER
 recvTimeout=NUMBER
 cnctTimeout=NUMBER
 poolSize=NUMBER
 urlVersion=["3"|"3.5"|"4"]
>
<instance
 id=NUMBER
 port=NUMBER
 host=STRING
 dormant=NUMBER
 protocol="http"
 transport=["socket"|"fsocket"|"winsock"|"nssocket"]
 redir=URL
 timeout=NUMBER
 sendTimeout=NUMBER
 recvTimeout=NUMBER
 cnctTimeout=NUMBER
 poolSize=NUMBER
 urlVersion=["3"|"3.5"|"4"]
 refuseNewSessions=["YES"|"NO"]
>
</instance>
</application>`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Sections.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
