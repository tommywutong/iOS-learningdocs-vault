---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.7.html
archived_at: '2026-07-15T08:11:24.718048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Adding%20or%20Deleting%20Items%20From%20a%20Project.md) [!](Classes.md)

---

#  Web Components

A _component_
represents a page, or part of a page, in your application. An application can have one or more components.

Every application starts with a component called Main, which is shown in the Web Components suitcase in the second column of the browser as __Main.wo__
. All components have the __.wo__
extension.

If you double-click a component, WebObjects Builder opens the component for editing. [Editing With WebObjects Builder](Editing%20With%20WebObjects%20Builder.md#apple-obtwmslehu3dembv)
shows how to edit your component using WebObjects Builder.

On disk, a component is represented as a folder with the __.wo__
extension. Every component has several files that specify the component's look and behavior. The name of each one is the component's name followed by a specific file extension. These are the files in the Main component:

- 

  __Main.html__
  is the HTML template for the component. This file contains HTML tags, just like any web page; in addition, it typically contains tags for dynamic WebObjects elements.
- 

  __Main.wod__
  is the _declarations file_
  that specifies bindings between the dynamic elements and variables or methods in your code.
- 

  __Main.woo__
  is used to store information about display groups (if your project accesses a database) and encodings for HTML templates. You should never edit this file (it does not appear in Project Builder's browser).

To create a new component:

1. 

   With Web Components selected in the first column of the browser, choose File !
   New in Project.
2. 

   In the New File panel, type the name of your project and click OK.

   The WebObjects Component Wizard appears.
   
   !
3. 

   If you want the Wizard to assist you in creating a component with database access, choose Component Wizard from Available Assistance; otherwise choose None. See "Creating a WebObjects Database Application" in _Getting Started With WebObjects_ for more information on using the Wizard with databases.
4. 

   Specify the language for your component and click Finish.

__Note:__

You can also create components in WebObjects Builder and save them into your project.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Adding%20or%20Deleting%20Items%20From%20a%20Project.md) [!](Classes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
