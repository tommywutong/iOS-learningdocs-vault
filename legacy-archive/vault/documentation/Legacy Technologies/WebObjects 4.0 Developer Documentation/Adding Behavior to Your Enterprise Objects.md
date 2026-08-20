---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies45.html
archived_at: '2026-07-18T01:23:02.881076Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies44.md)

# Adding Behavior to Your Enterprise Objects

Right now, the Movies application maps all its entities to the EOGenericRecord class. As the preceding sections illustrate, you can go quite far in an application using just this default enterprise object class, but now you need to add some custom classes to the Movies application.
In this section, you'll learn how to:

- Generate source code for a custom enterprise object class.
- Provide default values in a custom enterprise object class.

You'll create custom classes for the Talent and MovieRole entities. In the Talent class, you'll write a __fullName__ method that concatenates a Talent's first and last names. You'll use the method to populate MovieDetail's browser element. In the MovieRole class, you'll provide default values for newly inserted MovieRoles so they don't show up in the list of movie roles as a blank line.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies46.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
