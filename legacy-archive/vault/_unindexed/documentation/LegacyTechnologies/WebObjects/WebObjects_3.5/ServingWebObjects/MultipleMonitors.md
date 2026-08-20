---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/MultipleMonitors.html
archived_at: '2026-07-15T07:56:02.496606Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](ISAPIConfig.md)

## Starting Up Multiple Monitor Instances

As a fail-safe measure, you can start up multiple instances of the same Monitor application. When you start an instance of Monitor, the instance searches to see if another instance is running. If so, it puts itself to sleep. If the first Monitor instance crashes, the second instance will wake itself. Monitor stores its configuration information and its current state in the file system. Thus, in the event of a crash, the backup instance can take over, read the configuration file, restore the state from the file system, and continue as if nothing had happened.
You can have as many instances of Monitor running as you like. They will order themselves to take over in the event that the controlling instance fails.
The same holds true for __MonitorProxy__ daemon. You can have as many of these running as you like.
Remember that Monitor is a WebObjects application. To start multiple instances, you must provide unique instances numbers and port numbers to the adaptor on the command line, as well as the application path argument, like this:

```
> Monitor.exe -a WODefaultAdaptor -n 1 -p 1067 Monitor
> Monitor.exe -a WODefaultAdaptor -n 2 -p 1068 Monitor
```


In this example, the first instance becomes the controlling instance of Monitor. The second instance becomes active only if the first instance crashes.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
