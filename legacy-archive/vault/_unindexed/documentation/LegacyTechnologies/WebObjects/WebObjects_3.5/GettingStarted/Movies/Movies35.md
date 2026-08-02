---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies35.html
archived_at: '2026-07-15T07:54:44.717904Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies34.md)

# Setting Up a Master-Detail Configuration

So far your Movies application fetches, inserts, updates, and deletes only Movie objects. Considered alone, a Movie object isn't as interesting as it is when it's related to actors and roles. In this section, you'll add MovieRole and Talent objects to the Movies application.
The relationships defined in your model now come into play. Using Movie's __movieRoles__ relationship, you can display the MovieRoles for the selected Movie. In this type of configuration, called _master-detail_, a master display group holds enterprise objects for the source of a relationship, while a detail display group holds records for the destination. As individual records are selected in the master display group, the detail display group gets a new set of enterprise objects to correspond to the selection in the master.
In the Movies application, the master-detail configuration is built around Movie's __movieRoles__ relationship. The configuration is split across two pages in the application. The master, __movieDisplayGroup__, is in the Main component, while the detail is in MovieDetails.
In this section, you'll:

- Create and configure the detail display group.
- Extend the MovieDetails user interface to hold MovieRole and Talent information.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies36.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
