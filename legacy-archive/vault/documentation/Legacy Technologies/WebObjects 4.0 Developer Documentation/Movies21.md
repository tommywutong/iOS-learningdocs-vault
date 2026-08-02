---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies21.html
archived_at: '2026-07-18T01:22:12.039359Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies20.md)

## Specifying Default Values for New Enterprise Objects

When new enterprise objects are created in your application, it's common to assign default values to some of their properties. For example, in your Movies application it makes sense to assign a default value for the __title__ attribute so a new movie won't be displayed in the list of movies as a blank line.
You could write an action method for the Insert/New button instead of binding it directly to the display group __insert__ action method. In the custom action, you would create a new Movie object, assign default values to it, and then insert the new object into the display group. However, there are two additional ways to specify default values for new enterprise objects, without making explicit assignments:

- Assign default values in the enterprise object class.
- Specify default values using a display group.

For a particular situation, one of the approaches is usually better than the other. If the default values are intrinsic to the enterprise object, assign them in the enterprise object class. For example, consider a Member class with a __memberSince__ property. It's likely that you would automatically assign the current date to __memberSince__ instead of forcing a user to supply a value. You'll see how to use this technique in [Adding Behavior to Your Enterprise Objects](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md#apple-ge4tcmjq).

On the other hand, if the default values are specific to an application or to a particular user interface, explicitly initialize the object in code or specify the default values using a display group. In the Movies application, the need for default values is motivated by Main's user interface: you need to provide a default value so users can tell when a newly inserted record is selected. In another situation, you might not want a new movie to have a default title; you might instead want a new movie's title to be blank.
The Movies application specifies default values for newly created Movie objects using the display group, __movieDisplayGroup__.

- Open __Main.java__ in Project Builder.
- Add the following constructor:

```
public Main() {
    super();
    NSMutableDictionary defaultValues = new NSMutableDictionary();
    defaultValues.setObjectForKey("New Movie Title", "title");
    movieDisplayGroup.setInsertedObjectDefaultValues(defaultValues);
}
```


This method assigns the value "New Movie Title" as the default value for a new movie's __title__ attribute. When __movieDisplayGroup__ inserts a new movie (as it does when a user clicks the Insert/New button), it creates a new movie and assigns this default value to that movie.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies22.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
