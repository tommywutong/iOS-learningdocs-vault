---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.3a.html
archived_at: '2026-07-15T08:09:16.458745Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Adding%20Interface%20Controller%20Subclasses%20and%20Nib%20Files.md)

---

#  Adding Client-side Subprojects

You can add more than one client-side subproject to your project, especially if you want to use a framework. The subprojects containing EOInterfaceController subclasses and their nib files have to have a special project type: EOJavaClientSubproject.

To add a subproject of this type

1. 

   Open your project in Project Builder.
2. 

   Choose New Subproject from the Project menu.
3. 

   In the New Subproject panel, type a name for your subproject
4. 

   Make sure that the pop-up list displays the project type EOJavaClientSubproject.
5. 

   Click OK.

This procedure adds only the subproject; it does not add an interface-controller subclass, a nib file, or any other files (except makefiles). It also does not add __EOJavaClient.framework__ to the root project's list of frameworks.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Adding%20Interface%20Controller%20Subclasses%20and%20Nib%20Files.md)
