---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies21.html
archived_at: '2026-07-15T07:54:22.766981Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies20.md)

## Specifying Default Values for New Enterprise Objects

When new enterprise objects are created in your application, it's common to assign default values to some of their properties. For example, in your Movies application it makes sense to assign a default value for the __title__ attribute so a new movie won't be displayed in the list of movies as a blank line.
You could write an action method for the Insert/New button instead of binding it directly to the display group __insert__ action method. In the custom action, you would create a new Movie object, assign default values to it, and then insert the new object into the display group. However, there are two additional ways to specify default values for new enterprise objects, without making explicit assignments:

- Assign default values in the enterprise object class.
- Specify default values using a display group.

For a particular situation, one of the approaches is usually better than the other. If the default values are intrinsic to the enterprise object, assign them in the enterprise object class. For example, consider a Member class with a __memberSince__ property. It's likely that you would automatically assign the current date to __memberSince__ instead of forcing a user to supply a value. You'll see how to use this technique in ["Adding Behavior to Your Enterprise Objects"](Movies45.md#apple-ge4tcmjq).

On the other hand, if the default values are specific to an application or to a particular user interface, explicitly initialize the object in code or specify the default values using a display group. In the Movies application, the need for default values is motivated by Main's user interface: you need to provide a default value so users can tell when a newly inserted record is selected. In another situation, you might not want a new movie to have a default title; you might instead want a new movie's title to be blank.
The Movies application specifies default values for newly created Movie objects using the display group, __movieDisplayGroup__.

- Open __Main.java__ in Project Builder.
- Add the following constructor:

```
public Main() {
    super();
    MutableHashtable defaultValues = new MutableHashtable();
    defaultValues.put("title", "New Movie Title");
    movieDisplayGroup.setInsertedObjectDefaultValues(defaultValues);
}
```


This method assigns the value "New Movie Title" as the default value for a new movie's __title__ attribute. When __movieDisplayGroup__ inserts a new movie (as it does when a user clicks the Insert button), it creates a new movie and assigns this default value to that movie.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies22.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
