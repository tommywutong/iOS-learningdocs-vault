---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.53.html
archived_at: '2026-07-15T08:10:56.610810Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Creating%20Other%20WebObjects.md) [!](Dynamic%20Images.md) [!](WOComponentContent.md)

---

#   Generic WebObjects

You can use the generic WebObject element to create a dynamic version of any HTML element.

To create a dynamic version of a standard HTML element:

1. 

   Create the element (say, a heading) and select it.
2. 

   In the Inspector, click Make Dynamic.
   
   !

   If the element has no specific dynamic counterpart, it becomes a generic WebObject element.
   
   !

To create a generic WebObject corresponding to any HTML element (even ones not supported directly by WebObjects Builder):

1. 

   Click !
   in the toolbar.
2. 

   Bring up the inspector.
   
   !

   A generic WebObject element has one required attribute, __elementName__
   , which specifies what type of element should be generated at run time.

   For example, imagine that a future version of HTML adds a new container element, which you would like to generate dynamically in your component. You would:
3. 

   Double click in the binding column next to __elementName__
   . Type the name of the container in quotes.

   If the name isn't in quotes, WebObjects assumes it is a binding that should be resolved at run time. You might use that technique if you wanted to choose the type of element programmatically rather than specifying it in advance.
4. 

   Check "Element is container".
5. 

   Use the Add binding item in the inspector's binding pull-down list to specify any additional properties of the element that don't appear in the inspector.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Creating%20Other%20WebObjects.md) [!](Dynamic%20Images.md) [!](WOComponentContent.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
