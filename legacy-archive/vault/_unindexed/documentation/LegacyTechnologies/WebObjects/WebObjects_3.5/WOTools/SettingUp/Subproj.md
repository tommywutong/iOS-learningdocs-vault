---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Subproj.htm
archived_at: '2026-07-15T07:57:49.081893Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](Classes.md)

## Subprojects

A subproject has the same structure as a WebObjects Application project. You can use subprojects to divide large projects into manageable chunks.
When you create a new project, ProjectBuilder creates two subprojects (ClientSideJava and CommonJava) in your project folder. By default, they are not added to the Subprojects suitcase. If you need to use them, you must add them to the project. Then you can add your Java classes to the appropriate project as follows:

- Add server-side Java classes to your top-level project.
- Add client-side Java classes to the ClientSideJava subproject.
- Add Java classes that are common to both client and server to the CommonJava subproject.

__Note:__ These subprojects have the makefile variables JAVA_IS_CLIENT_SIDE and JAVA_IS_SERVER_SIDE set in __Makefile.preamble__ so that the appropriate Java code is generated when you build your project.
To create a subproject:

- Choose Project !New Subproject.
- Specify the name of your subproject in the New Subproject panel and click OK.

A subproject is created inside the project, with a similar structure to the top-level project. You can add items to the subproject in the same way that you add items to the top-level project.

To add an existing subproject (such as ClientSideJava or CommonJava) to your project:

- Double-click Subprojects in the first column of the browser.
!- In the Add Subprojects panel, navigate to the directory of the subproject you want to add and click Open.
- Double-click __PB.project__ to add the subproject to your project.

## Supporting Files

The Supporting Files suitcase contains your project's _makefile_ (which you should not edit), as well as __Makefile.preamble__ and __Makefile.postamble__, which you can modify in order to customize the makefile. You can add other files your project may need (such as Read Me documents) to this suitcase so that they can be edited in Project Builder.

[!Table of Contents](SetUpTOC.md) [!Next Section](Framewrk.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
