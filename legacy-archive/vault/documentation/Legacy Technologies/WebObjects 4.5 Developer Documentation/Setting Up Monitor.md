---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-22.html
archived_at: '2026-07-15T08:04:43.264016Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20With%20Monitor.md) [!](Starting%20Up%20Monitor.md) [!](Deploying%20on%20Multiple%20Hosts.md)

---

# Setting Up Monitor

Your first probable task as administrator is to verify and change the configuration settings that Monitor chooses by default, particularly the URL used to locate the adaptor. To do this, complete the following steps:

1. Click the Configure button. This brings up the Global Configuration page:

!2. Click the "HTTP Server and WebObjects Adaptor" item. Doing so causes the display of the following page:

!3. Enter the adaptor's URL in the URL To Adaptor field.
> This URL should identify the WebObjects adaptor running on the web server from which clients will access applications.

4. Click Update Adaptor URL.

Setting the adaptor URL is the minimal setup task required for administering applications on the local machine. You might want to fine-tune your site's configuration and take advantage of other features such as e-mail notifications.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20With%20Monitor.md) [!](Starting%20Up%20Monitor.md) [!](Deploying%20on%20Multiple%20Hosts.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
