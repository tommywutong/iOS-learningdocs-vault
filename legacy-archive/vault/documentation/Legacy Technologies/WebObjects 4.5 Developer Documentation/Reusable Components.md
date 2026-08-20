---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.57.html
archived_at: '2026-07-15T08:11:01.209911Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Custom%20WebObjects.md) [!](Direct%20to%20Web.md)

---

#   Reusable Components

One of the strengths of the WebObjects architecture is its support of reusable components. Any component that you define, whether it represents an entire page or part of a page, can be reused by any WebObjects application. A component can be used in multiple pages or even multiple times in the same page. Reusable components can be used for such items as headers, footers, and navigation bars.

When a reusable component is used inside another component, it is referred to as a _child component_
; the containing component is called the _parent component_
.

To reuse a component, you can either:

- 

  Add the component to a framework and include the framework in any project that wants to use the component. The component is a _shared component_
  and doesn't need to be copied into each application that uses it.
- 

  Add the component directly to your project (in the Web Components suitcase).

See [Frameworks](Frameworks.md#apple-gi4dembv)
for information on creating frameworks and adding them to a project. To add a component directly to a project, you can:

- 

  Drag a component (a folder with the .__wo__
  extension) from the file system onto a component window.

  You are asked whether you want to add the component to your project. If you respond Yes, the component is copied to the project and placed in the Web Components suitcase, along with all the other components.

  The child component then appears in the window at the insertion point.
- 

  Use the toolbar to add a custom WebObject element (see [Custom WebObjects](Custom%20WebObjects.md#apple-ge4tsnjq)
  ) to your page, then use the Inspector to set its type to the name of the reusable component.
- 

  Drag a component that has been stored on a palette to the component window (see [Palettes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.3a.html#26538)

A component that is designed for reuse can _export_
keys and actions, which become attributes that the parent component can bind, just as it would set the attributes of any other dynamic element. When the component is added to a parent component, these attributes show up in the Custom WebObject Inspector. The attributes must be enumerated using the API Editor for the component.

The Inspector shows the child component's attributes. As with any other dynamic element, you can bind the child component's attributes to keys and actions in the parent component's code.

__Note:__
When you create a component that is specifically designed to be used within other pages, specify "Partial document" in the Page Attributes Inspector pop-up list (see [Setting Page Attributes](Setting%20Page%20Attributes.md#apple-gq3dinjs)
). This way WebObjects Builder does not wrap <HTML>, <HEAD>, and <BODY> tags around your component.

For more information, see "Reusable Components" in the _WebObjects Developer's Guide_
.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Custom%20WebObjects.md) [!](Direct%20to%20Web.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
