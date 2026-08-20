---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects10.html
archived_at: '2026-07-18T01:23:35.018533Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects9.md)

### Running MonitorProxy

The __MonitorProxy__ executable can be found inside the __Monitor.woa__ application directory in _NEXT_ROOT___/Library/WebObjects/Applications__.To start the __MonitorProxy__ service on a remote machine:

- Open a command shell (using, for instance __Terminal.app__ on Mac OS X Server or the Bourne Shell program on Window NT).
- Enter "MonitorProxy" with no arguments to start the service.

__MonitorProxy__ launches and searches for a Monitor application running on a nearby host. __MonitorProxy__ might not find a host running Monitor, but do not be alarmed. It's more important that Monitor finds the __MonitorProxy__ than vice versa. Go to the Hosts page in Monitor to see if Monitor detects that the host is available and running a __MonitorProxy__.
You might find that __MonitorProxy__ takes a long time to start up because it is searching for the Monitor's host. To resolve this problem, specify the host running the Monitor as a command-line argument when you run __MonitorProxy__. For example:

```
MonitorProxy -mhost server1
```


You might want to set up your system so that __MonitorProxy__ starts up at system boot time. See "[Setting up Monitor and MonitorProxy as Services on Windows NT](ServingWebObjects11.md#apple-gyydoni)," below, for instructions on doing this on Windows NT.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects11.md)
