---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.5a.html
archived_at: '2026-07-15T08:11:07.813861Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](The%20Different%20Looks%20for%20WebObjects%20Applications.md) [!](Using%20Your%20Direct%20to%20Web%20Application.md)

---

#  The Structure of a Direct to Web Project

A Direct to Web project has a structure similar to other WebObjects application projects. A newly created project contains three components:

!

- 

  __MenuHeader.wo__
  is a reusable component that contains the header with the control buttons on the left side of each page (or the top of the page in the Basic look.) You can add text or other elements to this component if you choose.
- 

  __Main.wo__
  is the main component, representing the login page of the application.
- 

  __PageWrapper.wo__
  is a reusable component that wraps the content of the pages of the application (except for __Main.wo__
  ). It contains a header, the menu header component (__MenuHeader.wo__
  ), and footer text and elements common to these pages. If you want to customize the headers and footers for all pages of your application, you can add text or other elements to this component.

As you run your application, Direct to Web creates additional pages, using information in your model file and the settings specified in the Web Assistant. These pages do not show up as components in your project. Rather, Direct to Web creates them dynamically using a set of reusable components in the Direct to Web framework. However, you can save any page as a component or generate a user template. When you do that, you are then able to modify the component just as you would with any other WebObjects component. See [Generating Components](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.70.html#14372)
and [User Templates](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.71.html#23681)
for more information.

In your project's Classes suitcase, you'll see a Java file for each of the components, as well as the Session and Application objects. You can add code to any of these files to extend their functionality.

!

The Resources suitcase contains the model file you specified when you created the project (in this example, __Movies.eomodeld__
). It also contains __user.d2wmodel__
, which stores the preferences you have specified using the Web Assistant. Advanced users can edit this file; see _Developing WebObjects Applications With Direct to Web_
for more information about the rule file. The Resources suitcase also holds files specifying the exported keys, both optional and required, for each type of component used in the application; these files have an extension of __.api__
.

!

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](The%20Different%20Looks%20for%20WebObjects%20Applications.md) [!](Using%20Your%20Direct%20to%20Web%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
