---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/LoadBalancing.html
archived_at: '2026-07-15T07:56:00.533074Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](AppShutdown.md)[Previous
Section](AppShutdown.md) 

## Load Balancing

You can improve the performance of a WebObjects application
by distributing the processing load among multiple instances of the application.
These application processes can be running on the same machine as the server
or on remote machines. The task that accomplishes this distribution is
called _load balancing_.

As an example of how load balancing works, suppose
you have an application called MyApp and you have configured WebObjects
to run two instances of MyApp on the host toga and two instances on the
host tutu. When a user types this URL:

```
        http://toga.acme.com/cgi-bin/WebObjects/MyApp
```

the WebObjects adaptor looks for an instance of MyApp
on the host toga. If it finds an instance and the instance is ready to
receive requests, the adaptor sends the request to that instance. If both
of the instances of MyApp on toga are busy, it accesses an instance on
the host tutu.

Use the Monitor application to create new instances
of an application for load balancing. To create new instances of an application,
do the following:

1. Locate the application in the left frame and click the inspector button
   to its left. 

The Application Inspector opens in the right frame.

!

2. Click the Add Instance button to add a new instance of the application.
   
3. If you want the instance to run on a different host, click the More
   button for that instance, scroll down in the bottom frame until you see
   the host name field, enter the name of the host you want that instance
   to run on, and click the Save Settings button at the bottom of the frame.
   
4. To start the application instance, click the On/Off switch in the Instance
   Status field.

When you create multiple application instances in
this manner, you are creating the public configuration file _NeXT_ROOT___/NextLibrary/WOAdaptors/Configuration/WebObjects.conf__.
When the adaptor receives an HTTP request for an application, it first
(in its initial mode) checks __WebObjects.conf__ for an application
instance that is accepting connections and forwards the request to it.
The section "[WebObjects HTTP Adaptors](HTTPAdaptors.md#apple-gq2tqni)"
describes in some detail both the public configuration file and the adaptor
modes involved in load balancing.

Note that Monitor always assigns a unique number
to each application instance, even if it is running on a different host.
It does this so that it can recover a crashed instance for you. If an instance
dies, Monitor can try to recover it by launching it on another host. Because
of this, instance numbers must be unique across hosts.

The __WebObjects.conf__ file, however, only requires
an instance number to be unique on a given host. Consider the example given
previously, where two instances of MyApp run on host toga and two instances
run on host tutu. If you were to set up a __WebObjects.conf__ file by
hand, you could assign instance numbers 1 and 2 to the two instances on
toga and instance numbers 1 and 2 to the instances on tutu. This is legal,
but it's not supported by the Monitor, and if you do this, you won't be
able to use Monitor for the instances you've created.

!

To determine how many instances of an application
you should run, do the following:

1. Test the application using the recording and playback performance tools
   as described in the section "[Performance
   Testing](PerformanceTesting.md#apple-guydgmq)." 
2. Check the application's response times using the Application Inspector
   in the Monitor application. 
3. If the response time is slow, use Monitor to add another instance of
   the application. 
4. Continue to add instances and check their response times. When all
   instances have reasonable response times, you have the number of instances
   you need.

Your application's state-storage strategy affects
load balancing. By default, applications store state in memory in the server.
If the application uses this default state-storage strategy, the instance
that processed a session's first request must be used to process all subsequent
requests. That is, the load-balancing granularity is per session. If you
store state using some other strategy (for example, if you store state
in the file system), true load-balancing can be achieved; each request
from a session can be processed by any application instance (that is, the
load-balancing granularity is per request).

[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](ListenQueue.md)[Next
Section](ListenQueue.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
