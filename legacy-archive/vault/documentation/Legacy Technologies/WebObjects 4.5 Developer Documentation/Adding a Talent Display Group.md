---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.50.html
archived_at: '2026-07-15T08:08:22.051698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md) [!](Adding%20a%20Form.md) [!](Configuring%20the%20Browser.md)

---

#  Adding a Talent Display Group

The browser you just created is going to display a list of Talent objects. Like a repetition element, a browser has __list__ and __item__ attributes. As the browser moves through its __list__, the browser sets __item__ to the object at the current index. The Movies application uses a display group to provide the browser with a list of Talent objects, so now you need to create the new display group and a variable to bind to the browser's __item__ attribute.

1. 

   Use the Add Key command to create two new instance variables:
2. 

   __talentDisplayGroup__, whose type is WODisplayGroup
3. 

   __talent__, whose type is Talent

   You don't need to add set and get methods for the variables.
4. 

   Using the Display Group Options panel, assign the __talentDisplayGroup__ object'sentity to Talent.

   Remember that to open the Display Group Options panel, simply
   double-click the __talentDisplayGroup__ variable in the object browser. The ! icon initially displayed next to the variable indicates that initialization parameters have not yet been set.
5. 

   Configure __talentDisplayGroup__ to sort its objects alphabetically (ascending) by __lastName__.
6. 

   Configure it to fetch on load and click OK.

   After you configure __talentDisplayGroup__, the object browser shows a ! icon next to the variable.

The Movies application uses a display group to provide Talent objects, but you could fetch the Talent objects from the database without one. Display groups provide a simple way to fetch, insert, update, and delete enterprise objects without writing much, if any, code. To get finer-grained control over these operations, you can work directly with an EOEditingContext object. An editing context can do everything a display group does and much more, but you have to write more code to use one. For more information, see the EOEditingContext class specification in the _Enterprise Objects Framework Reference_.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md) [!](Adding%20a%20Form.md) [!](Configuring%20the%20Browser.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
