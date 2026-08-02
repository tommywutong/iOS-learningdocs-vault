---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.53.html
archived_at: '2026-07-15T08:08:25.412158Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20WebObjects%20Database%20Application.md) [!](Adding%20Insert%2C%20Save%2C%20and%20Delete%20Buttons.md) [!](Specifying%20Custom%20Enterprise%20Object%20Classes.md)

---

#   Adding Behavior to Your Enterprise Objects

Right now, the Movies application maps all its entities to the EOGenericRecord class. As the preceding sections illustrate, you can go quite far in an application using just this default enterprise object class, but now you need to add some custom classes to the Movies application.

In this section, you'll learn how to:

- 

  Generate source code for a custom enterprise object class.
- 

  Provide default values in a custom enterprise object class.

  You'll create custom classes for the Talent and MovieRole entities. In the Talent class, you'll write a __fullName__ method that concatenates a Talent's first and last names. You'll use the method to populate MovieDetail's browser element. In the MovieRole class, you'll provide default values for newly inserted MovieRoles so they don't show up in the list of movie roles as a blank line.

  #### [Specifying Custom Enterprise Object Classes](Specifying%20Custom%20Enterprise%20Object%20Classes.md#apple-obtwmslehuytsnbtge)

  #### [Generating Custom Enterprise Object Classes](Generating%20Custom%20Enterprise%20Object%20Classes.md#apple-obtwmslehuytsnbsgq)

  #### [Adding Custom Behavior to Talent](Adding%20Custom%20Behavior%20to%20Talent.md#apple-obtwmslehuytsmrwg4)

  #### [Providing Default Values in MovieRole](Providing%20Default%20Values%20in%20MovieRole.md#apple-obtwmslehuytsmzrhe)

  #### [Running Movies](Running%20Movies-4.md#apple-obtwmslehuzdanrqge)

  ---

  © 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

  [!](Creating%20a%20WebObjects%20Database%20Application.md) [!](Adding%20Insert%2C%20Save%2C%20and%20Delete%20Buttons.md) [!](Specifying%20Custom%20Enterprise%20Object%20Classes.md)

  Copyright © 2016 Apple Inc. All rights reserved.

  - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
  - [Privacy Policy](http://www.apple.com/privacy/)
