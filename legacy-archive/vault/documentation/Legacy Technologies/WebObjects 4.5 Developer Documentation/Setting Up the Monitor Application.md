---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-20.html
archived_at: '2026-07-15T08:04:41.696085Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20With%20Monitor.md) [!](Deploying%20With%20Monitor.md) [!](Starting%20Up%20Monitor.md)

---

# Setting Up the Monitor Application

When WebObjects is installed, the Monitor application (__Monitor.woa__
) is put in  ___NEXT_ROOT___
__/Library/WebObjects/Applications/__
. Monitor's images are also installed in your web server's document root under  ___DOC_ROOT___
__/WebObjects/Monitor.woa__
. Verify that both these paths exist if you have problems starting Monitor.

Depending on your platform and on other factors related to your deployment, you might want to configure your server to launch Monitor automatically when the server starts up. To do this on Windows NT, open the Control Panel and click the Services icon. Look for a service named "Apple WebObjects Monitor." You can configure this service to start up automatically.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20With%20Monitor.md) [!](Deploying%20With%20Monitor.md) [!](Starting%20Up%20Monitor.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
