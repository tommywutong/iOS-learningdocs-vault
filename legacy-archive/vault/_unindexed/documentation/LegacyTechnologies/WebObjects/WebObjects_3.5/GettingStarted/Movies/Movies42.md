---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies42.html
archived_at: '2026-07-15T07:54:55.868456Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies41.md)

## Adding a Talent Display Group

The browser you just created is going to display a list of Talent objects. Like a repetition element, a browser has __list__ and __item__ attributes. As the browser moves through its __list__, the browser sets __item__ to the object at the current index. The Movies application uses a display group to provide the browser with a list of Talent objects, so now you need to create the new display group and a variable to bind to the browser's __item__ attribute.

- Use the Add Variable/Method command to create two new instance variables:

- __talentDisplayGroup__, whose type is DisplayGroup
- __talent__, whose type is Talent

You don't need to add set and get methods for the variables.

- Using the Display Group Options panel, assign __talentDisplayGroup__'s entity to Talent.

Remember that to open the Display Group Options panel, simply
double-click the __talentDisplayGroup__ variable in the object browser. The ! icon initially displayed next to the variable indicates that initialization parameters have not yet been set.

- Configure __talentDisplayGroup__ to sort its objects alphabetically (ascending) by __lastName__.
- Configure it to fetch on load.

After you configure __talentDisplayGroup__, the object browser shows a ! icon next to the variable.

The Movies application uses a display group to provide Talent objects, but you could fetch the Talent objects from the database without one. Display groups provide a simple way to fetch, insert, update, and delete enterprise objects without writing much, if any, code. To get finer-grained control over these operations, you can work directly with an EditingContext object. An editing context can do everything a display group does and much more, but you have to write more code to use one. For more information, see the EditingContext class specification in the _Enterprise Objects Framework Reference_.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies43.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
