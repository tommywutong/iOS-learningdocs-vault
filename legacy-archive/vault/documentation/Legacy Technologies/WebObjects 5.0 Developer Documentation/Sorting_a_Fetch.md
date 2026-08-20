---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/Sorting_a_Fetch.html
archived_at: '2026-07-15T08:13:07.310571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Deleting_Authors.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/Glossary/index.html)

## Sorting a Fetch

Fetch specifications can be created either programmatically
or created with EOModeler and stored in the model file. Up to this
point you have use a simple fetch specification, returning an unsorted
list of enterprise objects. Now, you'll create a more elaborate
fetch specification with EOModeler and save it in the model file.
You'll see how EOModeler's graphical user interface makes it
easy to develop fetch specifications.

First, you'll define the new fetch specification on the
Author entity. Then, you'll amend the code in `Session.java` to
use the new fetch specification. Finally, you'll use in-memory sorting
to keep the list sorted even after you add new authors.

In ["Further Exploration"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOMBasics/iFurther_Exploration.html), you were
given the opportunity to sort the list of authors during the fetch.
If you did so, you probably noticed that once you added new authors
to the list, the list didn't stay sorted. You can use Enterprise
Objects's sorting mechanism on a previously fetched array of enterprise
objects, as well as during a fetch.

In this section you'll add a new method to `Session.java`, `sortAuthorList`,
which sorts the `authorList` array.
You'll also modify the `addAuthor` method
in `Main.java` to call
the `sortAuthorList` method
to re-sort the `authorList` array
each time an author is added.

1. Add the `sortAuthorList` method,
   shown in [Listing 12-17](#apple-ijbegq2cindei), to `Session.java`.

   __Listing
   12-17 The sortAuthorList method in Session.java__

   ```
   public void sortAuthorList() {
       // create array to store sort orderings
       NSMutableArray sortOrderings = new NSMutableArray();

       // create sort ordering
       EOSortOrdering sortOrdering1 = new EOSortOrdering("lastName",  EOSortOrdering.CompareAscending);

       // add sort ordering to orderings array
       sortOrderings.addObject(sortOrdering1);

       // sort authorList using orderings
       EOSortOrdering.sortArrayUsingKeyOrderArray(authorList, sortOrderings);
   }
   ```
2. Edit the `addAuthor` method
   in `Session.java` to sort
   the list after adding a new author to it.

   Add the following
   code after the line that adds a new author to the list:

   ```
   // sort list
   sortAuthorList();
   ```

Sorting is performed in this section of the code because if
the list remains unchanged, there is no need to sort it.

Build and run the application. You'll find that the author
list is sorted after you add a new author.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Deleting_Authors.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/Glossary/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
