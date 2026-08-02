---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.49.html
archived_at: '2026-07-15T08:08:12.976857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20WebObjects%20Database%20Application.md) [!](Where%20Do%20Primary%20Keys%20Come%20From.md) [!](Creating%20a%20Detail%20Display%20Group.md)

---

#  Setting Up a Master-Detail Configuration

So far your Movies application fetches, inserts, updates, and deletes only Movie objects. Considered alone, a Movie object isn't as interesting as it is when it's related to actors and roles. In this section, you'll add MovieRole and Talent objects to the Movies application.

The relationships defined in your model now come into play. Using Movie's __toMovieRole__ relationship, you can display the MovieRoles for the selected Movie. In this type of configuration, called _master-detail,_ a master display group holds enterprise objects for the source of a relationship, while a detail display group holds records for the destination. As individual records are selected in the master display group, the detail display group gets a new set of enterprise objects to correspond to the selection in the master.

In the Movies application, the master-detail configuration is built around Movie's __toMovieRole__ relationship. The configuration is split across two pages in the application. The master, __movieDisplayGroup__, is in the Main component, while the detail is in MovieDetails.

In this section, you'll:

- 

  Create and configure the detail display group.
- 

  Extend the MovieDetails user interface to hold MovieRole and Talent information.

#### [Creating a Detail Display Group](Creating%20a%20Detail%20Display%20Group.md#apple-obtwmslehuytinbvgi)

#### [Adding a Repetition](Adding%20a%20Repetition.md#apple-obtwmslehuytmmbzgi)

#### [Configuring a Repetition](Configuring%20a%20Repetition.md#apple-obtwmslehuytgnjzga)

#### [Running Movies](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.4ca.html#pgfld=26127)

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20WebObjects%20Database%20Application.md) [!](Where%20Do%20Primary%20Keys%20Come%20From.md) [!](Creating%20a%20Detail%20Display%20Group.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
