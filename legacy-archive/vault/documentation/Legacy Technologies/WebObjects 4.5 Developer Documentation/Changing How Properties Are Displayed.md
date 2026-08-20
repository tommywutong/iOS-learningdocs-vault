---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.6a.html
archived_at: '2026-07-15T08:11:21.034013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Setting%20Which%20Properties%20are%20Displayed.md) [!](Textual%20Attributes%20and%20Formatting.md)

---

#   Changing How Properties Are Displayed

You can use the Customize Properties display of the Web Assistant to specify various display characteristics of properties, such as formatting, color, alignment, and the representation of relationships. The fields and controls for setting these characteristics are on the right half of the display. Here is an example:

!

Let's go over the various elements of this part of the user interface:

- 

  At the top is the Display field, which holds the title of the property for the current page and entity. As discussed in [Setting Which Properties are Displayed](Setting%20Which%20Properties%20are%20Displayed.md#apple-gi4dambv)
  , you can edit this string.
- 

  Next to the Display field, in parentheses, is its data type. The data type determines the set of display components available for use. You cannot edit this information directly (however, you can edit the model file, which specifies the data type, using EOModeler).
- 

  The WOComponent group (or "box") contains a pop-up list showing the name of the component that is used to display the selected property in the current page. From this menu you can choose a different component to display the property. When you choose a display component, the set of controls and fields in the WOComponent group can change.

The items in the WOComponent pop-up list identify reusable components in the Direct to Web framework which are used to generate the pages you see in your application. Each property in a page of any type is initially shown in a default way for that type and is based on a certain component.

#### [Textual Attributes and Formatting](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.6b.html#pgfId=11138)

#### [Representation of Relationships](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.6c.html#pgfId=11141)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Setting%20Which%20Properties%20are%20Displayed.md) [!](Textual%20Attributes%20and%20Formatting.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
