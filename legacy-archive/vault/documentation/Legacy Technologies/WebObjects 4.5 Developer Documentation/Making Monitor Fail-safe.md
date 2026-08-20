---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.5.html
archived_at: '2026-07-15T08:09:45.995925Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Windows%20NT%20Post-Installation%20Steps.md) [!](Windows%20NT%20Post-Installation%20Steps.md) [!](Obtain%20and%20Install%20Database%20Client%20Libraries.md)

---

#   Making Monitor Fail-safe

Because Monitor is a critical piece of any deployment, measures should be taken to make sure that it does not fail. Monitor is installed as a service (listed as "Apple WebObjects Monitor" in the Services control panel) and you can configure it to start automatically upon boot by changing its Startup mode to Automatic. Note that although this will cause Monitor to be started automatically, you'll have to manually start your web browser and connect to Monitor manually (or by putting a shortcut to your web browser in your Startup program group). The URL for Monitor can be verified by checking the Windows NT Event Viewer (Start > Programs > Administrative Tools > Event Viewer) and is similar to:

http://localhost:1027/cgi-bin/WebObjects.exe/Monitor

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Windows%20NT%20Post-Installation%20Steps.md) [!](Windows%20NT%20Post-Installation%20Steps.md) [!](Obtain%20and%20Install%20Database%20Client%20Libraries.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
