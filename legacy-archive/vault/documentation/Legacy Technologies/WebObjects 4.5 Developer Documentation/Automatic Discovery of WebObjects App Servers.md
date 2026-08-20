---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-9.html
archived_at: '2026-07-15T08:05:08.275810Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](WebObjects%20HTTP%20Adaptors.md) [!](Configuration%20Files.md) [!](Web%20Server%20Adaptor.md)

---

# Automatic Discovery of WebObjects App Servers

This beta release includes support for the automatic discovery of systems running WebObjects by web server adaptors. This should remove the necessity to administer the web servers (beyond the initial adaptor installation).

When the web server adaptor starts up, and at intervals determined by the configuration refresh interval setting, the adaptor sends out a multicast request in an effort to discover which WebObjects app servers are available. Each app server's wotaskd process replies with its URL (http://me.myself.com:1085). The adaptor constructs a list of these URLs and then polls each in turn to get the full site configuration information.

If the configuration refresh interval is 10 seconds, the discovery broadcast happens every 100 seconds (the discovery broadcast occurs a factor of 10 less frequently).

To enable this automatic discovery mechanism, you need to make changes in both the web server adaptor `s configuration file and on each machine running wotaskd.

#### [Web Server Adaptor](Web%20Server%20Adaptor.md#apple-obtwmslefuytanjvgi)

#### [wotaskd](wotaskd.md#apple-obtwmslefuytanrzgm)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](WebObjects%20HTTP%20Adaptors.md) [!](Configuration%20Files.md) [!](Web%20Server%20Adaptor.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
