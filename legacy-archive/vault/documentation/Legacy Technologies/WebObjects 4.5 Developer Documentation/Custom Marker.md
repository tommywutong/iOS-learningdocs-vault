---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.31.html
archived_at: '2026-07-15T08:10:24.499089Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Structure%20Elements.md) [!](Tables.md) [!](Working%20With%20Tables.md)

---

#  Custom Marker

Not all legal HTML elements can be created directly using WebObjects Builder's buttons or menu commands. However, you can create any type of element using the custom tag.

To create an HTML element using a custom marker:

1. 

   Place the cursor where you want the element.
2. 

   Click !
   .
3. 

   In the panel that appears, enter the tag's name in the "Tag to use:" field.
4. 

   If the element doesn't require an end tag, uncheck "New marker is a container (allow children)."
5. 

   Click OK.

   !
   appears in the component window. You can replace the text "Custom Marker" with the content of the element (if any).
6. 

   If the element has attributes you want to specify, Control-click the tag in the path view on Rhapsody (right-click on Windows NT) and choose Inspect.
   
   !

   In the Generic Inspector that appears, select Add Attribute from the attribute pull-down list (alternatively, you can press Enter.) Type the attribute's name, press Tab, and enter the attribute's value.
   
   !

You can also enter the source view and type the marker and its text directly.

__Tip:__

To save a custom element so you can use it again, save it on a palette. See [Palettes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.3a.html#26538)
.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Structure%20Elements.md) [!](Tables.md) [!](Working%20With%20Tables.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
