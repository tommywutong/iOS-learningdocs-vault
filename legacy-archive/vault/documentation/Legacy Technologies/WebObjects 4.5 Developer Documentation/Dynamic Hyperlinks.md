---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.4f.html
archived_at: '2026-07-15T08:10:50.218135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Creating%20Other%20WebObjects.md) [!](Dynamic%20Strings.md) [!](Repetitions.md)

---

#   Dynamic Hyperlinks

Dynamic hyperlinks (WOHyperlink) allow you to specify the link's destination at run time rather than at compile time. There are several ways to do this:

- 

  You can specify the name of a page in your application as the destination of the link. To do this, bind the name to the WOHyperlink's __pageName__

  attribute. This is useful since pages in a WebObjects application don't have predictable URLs that you can specify in an HTML hyperlink.
- 

  You can specify an action to be performed when the hyperlink is clicked by binding WOHyperlink's __action__
  attribute to an action method in your code. This method can perform any sort of action, as well as returning a page as the destination.
- 

  You can also specify a URL as the destination by binding to the __href__
  _attribute._

To create a dynamic hyperlink:

1. 

   Click !
   in the toolbar.
2. 

   Replace the word _Hyperlink_
   with the text of the link.
3. 

   Create the element's bindings.

To learn how to create a static hyperlink, see [Setting Page Attributes](Setting%20Page%20Attributes.md#apple-geydcmry)
.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Creating%20Other%20WebObjects.md) [!](Dynamic%20Strings.md) [!](Repetitions.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
