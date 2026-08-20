---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-16.html
archived_at: '2026-07-15T08:04:40.695615Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Attributes-2.md) [!](Configuration%20File%20DTD.md)

---

# Sample Configuration File

`<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE adaptor SYSTEM "woadaptor.dtd">`
`<adaptor>
  <application name="HelloWorld"
   retries="5"
   loadbalance="roundrobin"
   dormant="300"
   protocol="http"
   transport="fsocket"
   redir="http://www.apple.com">
   <instance id="1" host="localhost" port="2001"
    refuseNewSessions="NO"
    sendTimeout="3"
    recvTimeout="10">
   </instance>
   <instance id="2" host="localhost" port="2002"
    refuseNewSessions="YES">
   </instance
  </application>

  <application name="Movies"
    urlVersion="3.5"
    retries="1"
    loadbalance="random"
    protocol="http"
    transport="socket">
   <instance id="3" host="localhost" port="1001"
    refuseNewSessions="NO">
   </instance>
   <instance id="4" host="localhost" port="1003"
    refuseNewSessions="NO">
   </instance>
  </application>

</adaptor>`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md) [!](Attributes-2.md) [!](Configuration%20File%20DTD.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
