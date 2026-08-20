---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects31.html
archived_at: '2026-07-18T01:23:50.277556Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects30.md)

## Load Balancing

You can improve the performance of a WebObjects application by distributing the processing load among multiple instances of the application. These application processes can be running on the same machine as the server or on remote machines. The task that accomplishes this distribution is called _load balancing_.
As an example of how load balancing works, suppose you have an application called MyApp and you have configured WebObjects to run two instances of MyApp on the host toga and two instances on the host tutu. When a user types this URL:

```
http://toga.acme.com/cgi-bin/WebObjects/MyApp
```


the WebObjects adaptor looks for an instance of MyApp on the host toga. If it finds an instance and the instance is ready to receive requests, the adaptor sends the request to that instance. If both of the instances of MyApp on toga are busy, it accesses an instance on the host tutu.
Use the Monitor application to create multiple new instances of an application for load balancing. See "[Creating Application Instances](ServingWebObjects13.md#apple-gyytsni)" on for details.

When you create multiple application instances, you are creating the public configuration file _NEXT_ROOT___/Library/WebObjects/Configuration/WebObjects.conf__. When the adaptor receives an HTTP request for an application, it first (in its initial mode) checks __WebObjects.conf__ for an application instance that is accepting connections and forwards the request to it. The section "[WebObjects HTTP Adaptors](WebObjects%20HTTP%20Adaptors.md#apple-gq2tqni)" describes in some detail both the public configuration file and the adaptor modes involved in load balancing.

Monitor always assigns a unique number to each application instance, even if it is running on a different host. It does this so that it can recover a crashed instance for you. If an instance dies, Monitor can try to recover it by launching it on another host. Because of this, instance numbers must be unique across hosts.
The __WebObjects.conf__ file, however, only requires an instance number to be unique on a given host. Consider the example given previously, where two instances of MyApp run on host toga and two instances run on host tutu. If you were to set up a __WebObjects.conf__ file by hand, you could assign instance numbers 1 and 2 to the two instances on toga and instance numbers 1 and 2 to the instances on tutu. This is legal, but it's not supported by the Monitor, and if you do this, you won't be able to use Monitor for the instances you've created.
!
To determine how many instances of an application you should run, do the following:

- Test the application using the recording and playback performance tools as described in the section "[Performance Testing](ServingWebObjects28.md#apple-guydgmq)."
- Check the application's response times using the Instance Detail View page in the Monitor application.
- If the response time is slow, use Monitor to add another instance of the application.
- Continue to add instances and check their response times. When all instances have reasonable response times, you have the number of instances you need.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects32.md)
