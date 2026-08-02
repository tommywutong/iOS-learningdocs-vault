---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-11.html
archived_at: '2026-07-15T08:04:38.244434Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects

---

[!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md) [!](Web%20Server%20Adaptor.md) [!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md)

---

# wotaskd

By default `wotaskd` listens for multicast discovery requests on IP address `239.128.14.2`. If you've configured the web server adaptor to send such requests to a different IP address, you must also set the `WOConfigMulticastAddress` user default on machines running `wotaskd`. You must to do this as root/administrator on the given machine (the user running `wotaskd`), or modify the startup script to provide it as a command-line option:

`defaults write wotaskd WOConfigMulticastAddress 239.128.14.2`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Automatic%20Discovery%20of%20WebObjects%20App%20Servers.md) [!](Web%20Server%20Adaptor.md) [!](Web%20Server%20Adaptor%20Configuration%20File%20Format.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
