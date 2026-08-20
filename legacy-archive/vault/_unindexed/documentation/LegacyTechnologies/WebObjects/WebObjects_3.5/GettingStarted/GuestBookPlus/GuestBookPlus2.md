---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBookPlus/GuestBookPlus2.html
archived_at: '2026-07-15T07:53:53.669047Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookPlusTOC.md) [!Previous Section](GuestBookPlus1.md)

# Creating a Custom Guest Class

In the first chapter, you created individual variables to store a guest's name, e-mail address, and comments. When keeping track of multiple guests, it's more useful to encapsulate all the data for a guest as a single entity. You'll do this by creating a Java class that contains the data for a single guest.

- In Project Builder's browser, select Classes in the first column.
- Choose File ! New in Project.
  !
- Type Guest.java as the name of the file.
- Click OK.

The newly created file contains a skeleton for a class called Guest.

- Enter the following code to complete the definition of the Guest class.
  !

A class stores information in its _instance variables_ (also referred to as _data members_). Here you're declaring three instance variables for Guest: __name__, __email__, and __comments__. Note that these declarations are the same as those that appeared in the code for __Main.java__ when you added the three variables using WebObjects Builder. In WebObjects, a component is also a class, specifically a subclass of the class next.wo.Component (called WOComponent in WebScript or Objective-C).

Java classes require a _constructor_ to initialize an instance (or _object_) of a particular class whenever one is created. A constructor has the same name as the class and returns no value.

Whenever your application creates a new Guest class, its instance variables are initialized with empty strings, which is the default value if the user enters no data. (If you prefer, you can use different strings for these initial values.)

- Save __Guest.java__.

Saving the file lets WebObjects Builder know about your newly created Guest class.

[!Table of Contents](GuestBookPlusTOC.md) [!Next Section](GuestBookPlus3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
