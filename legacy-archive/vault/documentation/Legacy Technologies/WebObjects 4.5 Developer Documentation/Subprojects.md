---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.d.html
archived_at: '2026-07-15T08:11:27.827156Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Headers.md) [!](Supporting%20Files.md)

---

#   Subprojects

A subproject has the same structure as a WebObjects Application project. You can use subprojects to divide large projects into manageable chunks.

When you create a new project, ProjectBuilder creates two subprojects (ClientSideJava and CommonJava) in your project folder. By default, they are not added to the Subprojects suitcase. If you need to use them, you must add them to the project. Then you can add your Java classes to the appropriate project as follows:

- 

  Add server-side Java classes to your top-level project.
- 

  Add client-side Java classes to the ClientSideJava subproject.
- 

  Add Java classes that are common to both client and server to the CommonJava subproject.

__Note:__
These subprojects have the makefile variables
JAVA_IS_CLIENT_SIDE
and
JAVA_IS_SERVER_SIDE
set in __Makefile.preamble__
so that the appropriate Java code is generated when you build your project.

To create a subproject:

1. 

   Choose Project !
   New Subproject.
2. 

   Specify the name of your subproject in the New Subproject panel, the type of project from the Type pull-down menu, and click OK.

   A subproject is created inside the project, with a similar structure to the top-level project. You can add items to the subproject in the same way that you add items to the top-level project.

To add an existing subproject (such as ClientSideJava or CommonJava) to your project:

1. 

   Double-click Subprojects in the first column of the browser.
   
   !
2. 

   In the Add Subprojects panel, navigate to the directory of the subproject you want to add and click Open.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Headers.md) [!](Supporting%20Files.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
