---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/Running_the_Application.html
archived_at: '2026-07-15T08:13:07.284210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Using_Relat_n_Your_Code.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Deleting_Authors.md)

## Running the Application

Build and run your application. When the user clicks on an
author's Book link, Main's `editBook` method
creates an AuthorBookEdit object and tells it which author it is
to process with the `setAuthor` message.

The AuthorBookEdit component displays the books associated
with the author by iterating through the `books` relationship
of `author` (an NSMutableArray)
in the WORepetition. When the user clicks Add, the `addBook` method
creates a new Book object and adds it to the `books` relationship
of `author` and the editing
context. Similarly, when the user clicks Delete on a book in the
list, the book is removed from the `books` relationship
and deleted from the editing context. When the user is done editing
the books of the author, she clicks Done to return to the Main page.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Using_Relat_n_Your_Code.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Deleting_Authors.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
