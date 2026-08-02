---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp9.html
archived_at: '2026-07-18T01:27:56.034382Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp8.md)

## Subprojects

A subproject has the same structure as a WebObjects Application project. You can use subprojects to divide large projects into manageable chunks.
When you create a new project, ProjectBuilder creates two subprojects (ClientSideJava and CommonJava) in your project folder. By default, they are not added to the Subprojects suitcase. If you need to use them, you must add them to the project. Then you can add your Java classes to the appropriate project as follows:

- Add server-side Java classes to your top-level project.
- Add client-side Java classes to the ClientSideJava subproject.
- Add Java classes that are common to both client and server to the CommonJava subproject.

__Note:__ These subprojects have the makefile variables JAVA_IS_CLIENT_SIDE and JAVA_IS_SERVER_SIDE set in __Makefile.preamble__ so that the appropriate Java code is generated when you build your project.
To create a subproject:

- Choose Project !New Subproject.
- Specify the name of your subproject in the New Subproject panel, the type of project from the Type pull-down menu, and click OK.

A subproject is created inside the project, with a similar structure to the top-level project. You can add items to the subproject in the same way that you add items to the top-level project.

To add an existing subproject (such as ClientSideJava or CommonJava) to your project:

- Double-click Subprojects in the first column of the browser.
!- In the Add Subprojects panel, navigate to the directory of the subproject you want to add and click Open.

## Supporting Files

The Supporting Files suitcase contains your project's __Makefile__ (which you should not edit since this file is maintained by Project Builder), as well as __Makefile.preamble__ and __Makefile.postamble__, which you can modify in order to customize the build. You can add other files your project may need (such as Read Me documents) to this suitcase so that they can be edited in Project Builder.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](SettingUp10.md)
