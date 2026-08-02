---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-49.html
archived_at: '2026-07-15T08:05:05.279839Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md) [!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md) [!](Using%20woservice%20on%20Mac%20OS%20X%20Server-2.md)

---

# Starting Monitor and wotaskd on Windows NT

During installation on Windows NT, __wotaskd__
is configured to start automatically at boot time (in the Services control panel, it's listed as "Apple WebObjects Task Daemon"). If it doesn't appear to be starting correctly, check the Services control panel and ensure that __wotaskd__
's Startup mode is set to Automatic. As was previously noted, __wotaskd__
is started under the control of __woservice__
.

Monitor is also installed as a service (listed as "Apple WebObjects Monitor" in the Services control panel) and you can configure it to start automatically upon boot by changing its Startup mode to Automatic. Note that although this will cause Monitor to be started automatically, you'll have to manually start your web browser and connect to Monitor manually (or by putting a shortcut to your web browser in your Startup program group). The URL for Monitor is can be verified by checking the Windows NT Event Viewer (Start > Programs > Administrative Tools > Event Viewer) and is similar to:

`http://localhost:1027/cgi-bin/WebObjects.exe/Monitor`

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md) [!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md) [!](Using%20woservice%20on%20Mac%20OS%20X%20Server-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
