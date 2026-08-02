---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-47.html
archived_at: '2026-07-15T08:05:04.269167Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Administrative%20Tasks.md) [!](Load%20Balancing.md) [!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md)

---

# Increasing the Listen Queue Depth

The listen queue depth indicates the number of transactions that can be in the socket buffer (the listen queue) awaiting processing. If the number of transactions in the buffer reach the limit set by the listen queue depth, the socket refuses new requests. The default depth is five.

When an application's request load varies by period (that is, it experiences "spikes"), you can increase the listen queue depth to improve performance. For example, suppose an application can process one transaction per second and it typically receives transactions at the rate of one transaction every two seconds. The application's listen queue remains empty because it can handle the load. Suppose that at certain times of the day this same application receives a much heavier load of two requests per second. At these times, the listen queue fills up because the application cannot process as many requests as it receives. If you know that the request rate will eventually return to the normal load of one request every two seconds, increasing the listen queue depth will help improve performance during the heavy load time.

On the other hand, suppose that two requests per second becomes the normal request load for this application. In this case, no matter how big the listen queue, the application can never catch up because it only processes one request per second. In this situation, when the average load is higher than the application can handle, load balancing is the proper solution.

To set the listen queue depth for all instances of an application, do the following in Monitor:

1. Click Applications in the Monitor banner to go to the Applications page.
2. Click the Config button in any row containing a configured application.
3. In the Application Configuration page, click the New Instance Defaults option. This displays the following form:

!4. Type the new listen queue depth in the Listen Queue Size field and check the box to the left of this field.
5. Click the Update for New and Existing Instances button.
6. Restart any existing instance to have it assume the new listen queue depth.

If you want to change the listen queue depth for specific instances, enter the new depth in the List Queue Size field of the Application Start-Up/Command-line Arguments form in the Instance Configuration page for an instance.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Administrative%20Tasks.md) [!](Load%20Balancing.md) [!](Making%20Monitor%20and%20wotaskd%20Fail-safe.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
