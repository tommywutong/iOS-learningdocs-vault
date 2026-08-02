---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/Components_and_Classes.html
archived_at: '2026-07-15T08:12:53.174927Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Developing__mic_Content.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](The_Main_Component.md)

## Components and Classes

Each Web page displayed on a user's Web browser is a WebObjects
component. A component is made up of several parts:

- __HTML
  file__ This portion of the component is mostly standard
  HTML code. A component is either a complete HTML page, with `<HTML>` and `</HTML>` tags,
  or a shorter segment of HTML code that can be inserted inline into
  another component.

  In addition to regular HTML tags and text,
  a component can contain special tags used by WebObjects, the `<WEBOBJECT>
  and </WEBOBJECT>` tags. Web browsers
  never see these tags because WebObjects replaces them with regular
  HTML code before sending them to the browser.
- __WOD file__ This is the glue between your
  HTML file and your Java code. Every WebObjects element used in a
  component has an entry in this file specifying its parameters, such
  as Java methods to call for data. WOD stands for WebObjects data.
- __Java file__ Every component has a Java
  class file associated with it. These classes inherit from the WOComponent
  class, which provides all the basic functionality a component needs.
  To customize behavior, you can add your own variables and logic
  to intercede in the built-in system
- __API file__ If you design your own components
  for reuse, they may rely on certain information being present in
  their Java code definitions. The API file lists the parameters for
  your custom components.
- __WOO file__ Contains information about __display
  groups__, special components used to display database information.
  WOO stands for WebObjects object.

The Web Components group—in the Groups & Files list
in Project Builder's main window—lists all the components of
a project. Each item is itself a subgroup named after the component.
Such groups contain the Java and API files for the component. The
HTML, WOD, and WOO files are contained in a subgroup of the component
subgroup, named using the component's name with the `.wo` extension
(`Main.wo`, for example).
The contents of the `.wo` group
are maintained by WebObjects Builder.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Developing__mic_Content.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](The_Main_Component.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
