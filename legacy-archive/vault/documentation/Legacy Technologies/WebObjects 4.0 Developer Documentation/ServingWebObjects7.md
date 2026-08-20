---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects7.html
archived_at: '2026-07-18T01:23:53.547002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects6.md)

## Setting Up Monitor

Your first probable task as administrator is to verify and change the configuration settings that Monitor chooses by default, particularly the URL used to locate the adaptor. To do this, complete the following steps:

- Click the Configure button. This brings up the Global Configuration page:

!

- Click the small triangle next to the "HTTP Server and WebObjects Adaptor" item. Doing so causes the display of the following page:

!

- In the URL To Adaptor field enter the adaptor's URL

This URL should include the web server from which clients will access applications plus the remaining portion of the URL up to the WebObjects adaptor.

- Click Update Adaptor URL.

Setting the adaptor URL is the minimal setup task required for administering applications on the local machine. You might want to fine-tune your site's configuration and take advantage of other features such as e-mail notifications.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects8.md)
