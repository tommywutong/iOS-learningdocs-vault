---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-40.html
archived_at: '2026-07-15T08:04:58.268928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Monitoring%20Application%20Activity.md) [!](Logging%20and%20Analyzing%20Adaptor%20Activity.md) [!](Performance%20Testing.md)

---

# Accessing the Application Statistics Page

Most WebObjects applications automatically include a WOStats page and record statistics about themselves in that page while they run. To look at these statistics, access the WOStats page while the application is running. You can do this through Monitor or through any browser that can access your application.

- In Monitor, go to the Detail View page for an application and click the WOStats button next to an instance.
- From a browser, access the WOStats page with a URL like the following:

`
http://myhost/cgi-bin/WebObjects/MyWebApp.woa/wa/WOStats`

If there are multiple instances, specify the instance number as well:

`
http://myhost/cgi-bin/WebObjects/MyWebApp.woa/1/wa/WOStats`

The "1" just before "/wa" is the instance number.

The WOStats page looks similar to the following:

!

See the description of WOStats in the _WOExtensions Reference_
for more information about what the page displays.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Monitoring%20Application%20Activity.md) [!](Logging%20and%20Analyzing%20Adaptor%20Activity.md) [!](Performance%20Testing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
