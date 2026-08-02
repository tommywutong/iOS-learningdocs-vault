---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOCustomObjects/Setting_Default_Values.html
archived_at: '2026-07-15T08:13:00.768266Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Using_Custom_Logic.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/index.html)

## Setting Default Values

When an Author object is instantiated, its first and last
name attributes have no values. Sometimes default values should
be provided for properties of your enterprise objects. There are
several ways to do accomplish this.

You could assign initial values in the same method that creates
the new instance. You could do so by simply invoking the `setLastName` and `setFirstName` methods
on the new instance with the appropriate arguments. One advantage
of this approach is that it allows you to create new instances with
different defaults depending on certain circumstances.

Alternatively, you can provide initial values in the Author
class itself, so that no values need to be set when the instance
is created. This is the strategy you will use for the Author entity.

You can also combine these methods—setting a default in
the class and overriding it in the specific cases you wish to.

Modify the constructor in `Author.java` so
that it looks like [Listing 11-4](#apple-ijauuqsgjjfek).

__Listing
11-4 The constructor in Author.java—setting
default value for lastName__

```
public Author() {
    super();
    setLastName("*required*");
}
```

When you build and run the application, "\*required\*" appears
in the Last Name text field whenever a new author object is created.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Using_Custom_Logic.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
