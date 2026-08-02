---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.57.html
archived_at: '2026-07-15T08:08:27.751111Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md) [!](Adding%20Custom%20Behavior%20to%20Talent.md) [!](Running%20Movies-4.md)

---

#  Providing Default Values in MovieRole

As discussed in [Specifying Default Values for New Enterprise Objects](Specifying%20Default%20Values%20for%20New%20Enterprise%20Objects.md#apple-gm3dqnbt)
, there are two main ways to specify default values for new enterprise objects without making explicit assignments:

- 

  Assign default values in the enterprise object class.
- 

  Specify default values using a display group.

For the Movie class, you specified default values using a display group. This approach is also the more appropriate choice for the MovieRole class, but you'll use the other approach for MovieRole just to see how its done.

1. 

   Open __MovieRole.java__ in Project Builder.
2. 

   Add the method, __awakeFromInsertion__, as follows

   public void awakeFromInsertion(EOEditingContext context){

      super.awakeFromInsertion(context);

      setRoleName("New Role");

   }

   This method is automatically invoked right after your enterprise object class creates a new MovieRole and inserts it into an editing context, which happens when you use a display group to insert.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md) [!](Adding%20Custom%20Behavior%20to%20Talent.md) [!](Running%20Movies-4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
