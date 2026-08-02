---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-17.html
archived_at: '2026-07-15T08:04:41.197904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Sample%20Configuration%20File.md) [!](Installing%20Applications-2.md)

---

# Configuration File DTD

`<!-- Can actually incorporate status info in here -->

<!ELEMENT adaptor (application)*>
<!ATTLIST adaptor
   xyzzy CDATA #IMPLIED
   confinterval CDATA #IMPLIED
   retries CDATA #IMPLIED
   loadbalance ("random"|"roundrobin"|"loadaverage") #IMPLIED
   dormant CDATA #IMPLIED
   protocol CDATA "http" #IMPLIED
   transport ("socket"|"fsocket"|"winsock"|"nssocket") #IMPLIED
   redir CDATA #IMPLIED`
` timeout CDATA #IMPLIED
   sendTimeout CDATA #IMPLIED
   recvTimeout CDATA #IMPLIED
   cnctTimeout CDATA #IMPLIED
  sendBufSize CDATA #IMPLIED
  recvBufSize CDATA #IMPLIED
   poolsize CDATA #IMPLIED
   urlVersion ("3"| "3.5" | "4") #IMPLIED>

<!ELEMENT application (instance)*>
<!ATTLIST application name STRING #REQUIRED
   retries CDATA #IMPLIED
   loadbalance ("random"|"roundrobin"|"loadaverage") #IMPLIED
   dormant CDATA #IMPLIED
   protocol CDATA "http" #IMPLIED
   transport ("socket"|"fsocket"|"winsock"|"nssocket") #IMPLIED
   redir CDATA #IMPLIED
   timeout CDATA #IMPLIED
   sendTimeout CDATA #IMPLIED
   recvTimeout CDATA #IMPLIED
  cnctTimeout CDATA #IMPLIED
  sendBufSize CDATA #IMPLIED
  recvBufSize CDATA #IMPLIED
   poolsize CDATA #IMPLIED
   urlVersion ("3"| "3.5" | "4") #IMPLIED>

<!ELEMENT instance>
<!ATTLIST instance id CDATA #REQUIRED port CDATA #REQUIRED host CDATA #REQUIRED
   refuseNewSessions ("YES"|"NO") #IMPLIED
   count CDATA "-1" #IMPLIED
   dormant CDATA #IMPLIED
   protocol CDATA "http" #IMPLIED
   transport ("socket"|"fsocket"|"winsock"|"nssocket") #IMPLIED
   redir CDATA #IMPLIED
   timeout CDATA #IMPLIED
   sendTimeout CDATA #IMPLIED
   recvTimeout CDATA #IMPLIED
   cnctTimeout CDATA #IMPLIED
  sendBufSize CDATA #IMPLIED
  recvBufSize CDATA #IMPLIED
   poolsize CDATA #IMPLIED
   urlVersion ("3"| "3.5" | "4") #IMPLIED>`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Sample%20Configuration%20File.md) [!](Installing%20Applications-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
