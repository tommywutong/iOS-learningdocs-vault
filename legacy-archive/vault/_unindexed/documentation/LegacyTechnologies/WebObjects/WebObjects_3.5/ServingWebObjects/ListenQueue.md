---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/ListenQueue.html
archived_at: '2026-07-15T07:55:59.931927Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](LoadBalancing.md)

## Increasing the Listen Queue Depth

When an application's request load is sometimes heavier than other times, you can increase the listen queue depth to improve performance.
For example, suppose an application can process one transaction per second and it typically receives transactions at the rate of one transaction every two seconds. The application's listen queue remains empty because it can handle the load. Suppose that at certain times of the day, this same application receives a much heavier load of two requests per second. At these times, the listen queue fills up because the application cannot process as many requests as it receives. If you know that the request rate will eventually return to the normal load of one request every two seconds, increasing the listen queue depth will help improve performance during the heavy load time.
On the other hand, suppose that two requests per second becomes the normal request load for this application. In this case, no matter how big the listen queue, the application can never catch up because it only processes one request per second. In this situation, when the average load is higher than the application can handle, load balancing is the proper solution.
To increase the listen queue depth, do the following in Monitor:

- In the Application Inspector, click the More button to show the Application Instance Inspector in the bottom frame.
- Scroll down until you see the check box labeled Listen queue depth. Click this check box.
- Enter the size of the listen queue depth in the field next to the check box.
- Click the Save Settings button at the bottom of the frame.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](NSAPIConfig.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
