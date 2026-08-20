---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.17.html
archived_at: '2026-07-15T08:14:50.655348Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.16.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.18.md)

#   Batching the Output of a WODisplayGroup

##  Synopsis

Describes how you display the WODisplayGroup output in batches.

##  Description

One of the most useful features of a WODisplayGroup is its capacity to display its output in fixed-sized batches. Users can navigate to the previous batch or the next batch using hyperlinks or buttons. Batching reduces the amount of data transmitted to the user's browser and makes the output more managable.

If you create the WODisplayGroup using Project Builder's Wizard, the default batch size is 10. Thus if there are one hundred objects to display,
displayedObjects
returns only the first ten of those objects when the page is generated. If
displayNextBatch
is invoked,
displayedObjects
is updated to contain the next ten objects, and the page is regenerated.

You use
displayNextBatch
and
displayPreviousBatch
to move back and forth through the displayed objects. These methods can be bound directly to the action attributes of hyperlinks or buttons.

The
setNumberOfObjectsPerBatch
method changes the batch size. You can also change batch size using WebObjects Builder's display group configuration panel, which is accessed by double-clicking the display group in the object browser.

##  See Also

- 

  [Creating a WODisplayGroup](Creating%20a%20WODisplayGroup.md#apple-gi3tanbu)
- 

  [Setting a WODisplayGroup's Fetch Specification Programmatically](Setting%20a%20WODisplayGroup%27s%20Fetch%20Specification%20Programmatically.md#apple-gi3tanbu)
- 

  [Manipulating Selections in a WODisplayGroup](Manipulating%20Selections%20in%20a%20WODisplayGroup.md#apple-gi3tanbu)
- 

  WODisplayGroup class specification in the _WebObjects Framework Reference_
  .

##  Questions

- 

  How do I display the output from my WODisplayGroup in batches?

##  Keywords

- 

  WODisplayGroup
- 

  Batching

##  Revision History

19 February 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.16.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.18.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
