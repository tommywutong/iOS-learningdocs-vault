---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects27.html
archived_at: '2026-07-18T01:23:44.376741Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects26.md)

### Accessing the Application Statistics Page

Most WebObjects applications automatically include a WOStats page and record statistics about themselves in that page while they run. To look at these statistics, access the WOStats page while the application is running. You can do this through Monitor or through any browser.

- In Monitor, go to the Detail View page for an application and click the WOStats button next to an instance.
- From a browser, access the WOStats page with a URL like the following:

```
http://myhost/cgi-bin/WebObjects/MyWebApp.woa/wa/WOStats
```


If there are multiple instances, specify the instance number as well:

```
http://myhost/cgi-bin/WebObjects/MyWebApp.woa/1/wa/WOStats
```


The "1" just before "/wa" is the instance number.

The WOStats page looks similar to the following example:

!

See the description of WOStats in the _WOExtensions Reference_ for more information about what the page displays.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects28.md)
