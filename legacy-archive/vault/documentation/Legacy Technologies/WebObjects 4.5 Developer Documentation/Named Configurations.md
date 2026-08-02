---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.6f.html
archived_at: '2026-07-15T08:11:24.684465Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Web%20Assistant%20Expert%20Mode.md) [!](Choosing%20a%20Page%20to%20Customize.md) [!](Generating%20Components.md)

---

#  Named Configurations

Once you have customized a page, you can capture the settings in a _named configuration_
. Named configurations are used when you need more than one page for a particular task and entity. Consider a page that lists movies for a video rental store. A customer would want to see the names of the movies and plot summaries. A store clerk would want to see how many copies are available for rental and how long they can be rented. In addition, the customer should not be able to edit any information, while the store clerk might be able to edit some properties. To set up such a system, you create two named configurations for listing movies: one for the customer and the other for the store clerk.

Named configurations can only be displayed programmatically; the Web Assistant can edit named configurations but can't display the changes in your browser.

To save the settings of the current task and entity in a named configuration:

1. 

   Click Add.

   A panel appears with a text field containing a default name for the configuration (the page name followed by the entity name).
2. 

   Enter a new name for the configuration if you choose.
3. 

   Click Ok.

To edit a named configuration, select it from the Named Configurations pop-up list. You can now change settings on the Properties and Page displays.
__Note:__

When you edit a named configuration, the changes are not reflected in your browser. Named configurations can only be displayed programmatically.

To delete a named configuration, select it from the Named Configurations pop-up list and click Delete.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Web%20Assistant%20Expert%20Mode.md) [!](Choosing%20a%20Page%20to%20Customize.md) [!](Generating%20Components.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
