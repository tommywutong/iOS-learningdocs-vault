---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-46.html
archived_at: '2026-07-15T08:05:03.280715Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Administrative%20Tasks.md) [!](Automatic%20Scheduling.md) [!](Increasing%20the%20Listen%20Queue%20Depth.md)

---

# Load Balancing

You can improve the performance of a WebObjects application by distributing the processing load among multiple instances of the application. These application processes can be running on the same machine as the server or on remote machines. The task that accomplishes this distribution is called _load balancing_
.

As an example of how load balancing works, suppose you have an application called MyApp and you have configured WebObjects to run two instances of MyApp on the host __toga__
and two instances on the host __tutu__
. When a user types this URL:

`http://toga.acme.com/cgi-bin/WebObjects/MyApp`

the WebObjects adaptor looks for an instance of MyApp on the host __toga__
. If it finds an instance and the instance is ready to receive requests, the adaptor sends the request to that instance. If both of the instances of MyApp on __toga__
are busy, it accesses an instance on the host __tutu__
.

Use the Monitor application to create multiple new instances of an application for load balancing. See [Creating Application Instances](Creating%20Application%20Instances.md#apple-gm3dambz) for details.

When you create multiple application instances, you are creating the configuration file  ___NEXT_ROOT___
__/Library/WebObjects/Configuration/WebObjects.conf__
. When the adaptor receives an HTTP request for an application, it first (in its initial mode) checks __WebObjects.conf__
for an application instance that is accepting connections and forwards the request to it.

Monitor always assigns a unique number to each application instance, even if it is running on a different host. It does this so that it can recover a crashed instance for you. If an instance dies, Monitor can try to recover it by launching it on another host. Because of this, instance numbers must be unique across hosts.

Even though instance numbers are unique across hosts, the web server adaptor's configuration file only requires an instance number to be unique on a given host. Consider the example given previously, where two instances of MyApp run on host __toga__
and two instances run on host __tutu__
. If you were to set up a web server adaptor's configuration file by hand, you could assign instance numbers 1 and 2 to the two instances on __toga__
and instance numbers 1 and 2 to the instances on __tutu__
(see [Web Server Adaptor Configuration File Format](Web%20Server%20Adaptor%20Configuration%20File%20Format.md#apple-gu3danzr)). This is legal, but it's not supported by Monitor, and if you do this you won't be able to use Monitor for the instances you've created.

!

To determine how many instances of an application you should run, do the following:

1. Test the application using the recording and playback performance tools as described in the section "[Performance Testing](Performance%20Testing.md#apple-gi3demju)."
2. Check the application's response times using the Instance Detail View page in the Monitor application.
3. If the response time is slow, use Monitor to add another instance of the application.
4. Continue to add instances and check their response times. When all instances have reasonable response times, you have the number of instances you need.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Administrative%20Tasks.md) [!](Automatic%20Scheduling.md) [!](Increasing%20the%20Listen%20Queue%20Depth.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
