---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies49.html
archived_at: '2026-07-15T07:55:01.355012Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies48.md)

## Providing Default Values in MovieRole

As discussed in ["Specifying Default Values for New Enterprise Objects"](Movies21.md#apple-ge3tknbx), there are two main ways to specify default values for new enterprise objects without making explicit assignments:

- Assign default values in the enterprise object class.
- Specify default values using a display group.

For the Movie class, you specified default values using a display group. This approach is also the more appropriate choice for the MovieRole class, but you'll use the other approach for MovieRole just to see how its done.

- Open __MovieRole.java__ in Project Builder.
- Add the method, __awakeFromInsertionInEditingContext__, as follows.

```
public void awakeFromInsertionInEditingContext(EditingContext
context) {
    super.awakeFromInsertionInEditingContext(context);
    roleName = "New Role";
}
```


This method is automatically invoked right after your enterprise object class creates a new MovieRole and inserts it into an editing context, which happens when you use a display group to insert.

## Running Movies

Be sure that all your project's files are saved (including your model file), and build and run your application. Now when a user clicks the Insert/New button on the MovieDetails page, a new MovieRole is inserted, with "New Role" already displayed as the role name.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
