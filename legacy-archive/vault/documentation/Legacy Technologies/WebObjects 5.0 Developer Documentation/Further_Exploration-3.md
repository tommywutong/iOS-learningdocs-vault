---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOMBasics/Further_Exploration.html
archived_at: '2026-07-15T08:13:09.741107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](The_Authors_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOCustomObjects/index.html)

## Further Exploration

The third parameter of the constructor for an EOFetchSpecification
can be an NSArray of EOSortOrderings. You can examine the EOSortOrdering
class using the Java Browser.

To create an EOSortOrdering, you specify the attribute to
sort on and the selector to be used for sorting. Four selectors
are defined in the EOSortOrdering class:

- `CompareAscending`
- `CompareDescending`
- `CompareCaseInsensitiveAscending`
- `CompareCaseInsensitiveDescending`

The case insensitive versions of the ascending and descending
selectors are for use with strings and ignore the case of characters
when sorting.

A fetch specification created with a sort ordering in place
might look like [Listing 10-8](#apple-ijauuskgi5duu).

__Listing
10-8 Fetch specification that uses sort
orderings__

```
EOSortOrdering lastNameSort = new EOSortOrdering("lastName",  EOSortOrdering.CompareCaseInsensitiveAscending);
EOSortOrdering firstNameSort = new EOSortOrdering("firstName",  EOSortOrdering.CompareCaseInsensitiveAscending);
NSMutableArray sortOrderings = new NSMutableArray();
sortOrderings.addObject(lastNameSort);
sortOrderings.addObject(firstNameSort);

EOFetchSpecification authorFetch = new EOFetchSpecification("Author", null,  sortOrderings);
```

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](The_Authors_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOCustomObjects/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
