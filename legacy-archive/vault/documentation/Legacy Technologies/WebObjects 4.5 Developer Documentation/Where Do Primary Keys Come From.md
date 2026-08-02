---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.48.html
archived_at: '2026-07-15T08:08:12.475709Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Refining%20Your%20Model.md) [!](Using%20the%20Advanced%20Relationship%20Inspector.md) [!](Setting%20Up%20a%20Master-Detail%20Configuration.md)

---

#   Where Do Primary Keys Come From?

Enterprise Objects Framework uses primary keys to identify enterprise objects in memory, and it works best if you never change an enterprise object's primary key from its initial value. Consequently, applications usually generate and assign primary key values automatically instead of having users provide them. For example, the Movies application assigns a __movieId__ value to a new movie when it's created, and the value never changes afterward. The Movies interface doesn't even display __movieId__ values because they aren't meaningful to users of the application.

Enterprise Objects Framework provides several mechanisms for generating and assigning unique values to primary key attributes. By default, Enterprise Objects Framework uses a native database mechanism to assign primary key values. See the chapter "Answers to Common Design Questions" in the _Enterprise Objects Framework Developer's Guide_ for more information.

The Movies application generates primary key values for Movie and Talent objects using the default mechanism, but MovieRole is a special case because:

- 

  MovieRole's primary key is compound. The default behavior of generating a primary key value using a native database mechanism works only on simple (not compound) primary keys.
- 

  A MovieRole's primary key attributes, __movieId__ and __talentId__, must match the corresponding attributes in the MovieRole's Movie and Talent objects. The default mechanism generates new, unique values.

Instead of the default mechanism, Enterprise Objects Framework uses primary key propagation to assign primary keys to MovieRole objects. By configuring the Movie's __toMovieRole__ relationship to propagate primary key, the Framework knows to assign a new MovieRole's __movieId__ to the same value as the __movieId__ of the MovieRole's Movie. Similarly, a new MovieRole's __talentId__ is set to the same value as the __talentId__ of the MovieRole's Talent.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Refining%20Your%20Model.md) [!](Using%20the%20Advanced%20Relationship%20Inspector.md) [!](Setting%20Up%20a%20Master-Detail%20Configuration.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
