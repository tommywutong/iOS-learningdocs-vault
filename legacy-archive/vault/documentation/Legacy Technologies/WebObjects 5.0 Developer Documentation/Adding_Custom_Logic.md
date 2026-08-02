---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOCustomObjects/Adding_Custom_Logic.html
archived_at: '2026-07-15T08:12:59.222961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Modifying_t_ors_Project.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Using_Custom_Logic.md)

## Adding Custom Logic

Now that the Author entity is represented by the Author class,
you can add custom methods to it.

Frequently, you'll want to display data in a form different
from that used to is record it in the database. For example, it
would be convenient to have a single method in the Author class
that returns an author's full name, last name first with a comma
separating the last and first names. A similar technique is used
in the Authors application (two WOStrings separated by a comma),
but putting the logic into a single method allows you to easily suppress
the comma if the first name is not present.

Add the `fullName` method
shown in [Listing 11-3](#apple-ijauuq2eivduk) to the Author class, and save `Author.java`.

__Listing
11-3 The fullName method in Author.java__

```
public String fullName() {
    String first = firstName();
    String last = lastName();
    String full;
    if ((first != null) && (! (first.equals("")))) {
        full = last + ", " + first;
    }
    else {
        full = last;
    }
    return full;
}
```

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Modifying_t_ors_Project.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Using_Custom_Logic.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
