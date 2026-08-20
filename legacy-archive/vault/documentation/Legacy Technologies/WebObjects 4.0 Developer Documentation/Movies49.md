---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies49.html
archived_at: '2026-07-18T01:23:04.097498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies48.md)

## Providing Default Values in MovieRole

As discussed in [Specifying Default Values for New Enterprise Objects](Movies21.md#apple-gi2dimrr), there are two main ways to specify default values for new enterprise objects without making explicit assignments:

- Assign default values in the enterprise object class.
- Specify default values using a display group.

For the Movie class, you specified default values using a display group. This approach is also the more appropriate choice for the MovieRole class, but you'll use the other approach for MovieRole just to see how its done.

- Open __MovieRole.java__ in Project Builder.
- Add the method, __awakeFromInsertionInEditingContext__, as follows

```
public void awakeFromInsertion(EOEditingContext context){
        super.awakeFromInsertion(context);
        roleName = "New Role";
}
```


This method is automatically invoked right after your enterprise object class creates a new MovieRole and inserts it into an editing context, which happens when you use a display group to insert.

## Running Movies

Be sure that all your project's files are saved (including your model file), and build and run your application. Now when a user clicks the Insert/New button on the MovieDetails page, a new MovieRole is inserted, with "New Role" already displayed as the role name.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
