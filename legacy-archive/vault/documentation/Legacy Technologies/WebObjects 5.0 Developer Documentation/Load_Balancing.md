---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Load_Balancing.html
archived_at: '2026-07-15T08:12:00.413792Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Setting_Mon_Preferences.md)[!](Deploying_Multiple_Sites.md)

## Load Balancing

|  |
| --- |
| __Note:__ Load balancing occurs only with the hosts that the HTTP adaptor knows about. Adding a host in Monitor is not enough. For more information on how to configure hosts in the HTTP adaptor, see ["State Discovery"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/iState_Discovery.html). |

Load balancing is a mechanism by which user-load is spread
out among the instances of an application; these instances can be
running on different hosts. Load balancing ensures that your site's
hardware resources are used efficiently and with the highest level
of performance. The default load-balancing algorithm used is Random.
The following list describes how user load is distributed under
each of the provided algorithms:

- __Random__ assigns
  a user to an arbitrarily-chosen instance.
- __Round-Robin__ assigns users among instances
  sequentially.
- __Load Average__ balances load by distributing
  users evenly among instances.

You can choose a load-balancing algorithm at two levels:

- __Site
  level__ You set a site-wide load-balancing algorithm in
  the HTTP Adaptor Settings section of the Site page. From then on,
  the applications in your site will use that load-balancing algorithm.
- __Application level__ You can override
  the site-wide load-balancing algorithm in the Load Balancing and
  Adaptor Settings section of the application configuration page.

[!](Setting_Mon_Preferences.md)[!](Deploying_Multiple_Sites.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
