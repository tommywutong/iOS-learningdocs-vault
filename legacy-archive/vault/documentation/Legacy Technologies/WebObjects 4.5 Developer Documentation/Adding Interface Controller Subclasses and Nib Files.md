---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.3b.html
archived_at: '2026-07-15T08:09:16.487870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Adding%20Client-side%20Subprojects.md) [!](Adding%20Web%20Components%20%28with%20Interface%20Controllers%29.md)

---

#  Adding Interface Controller Subclasses and Nib Files

To add an EOInterfaceController subclass with a new interface file to your client-side subproject

1. 

   Select the Interfaces bucket in your EOJavaClientSubproject subproject
2. 

   Chose New In Project from the File menu.
3. 

   In the New File panel, enter the name for the new EOInterfaceController subclass and its interface file.
4. 

   Click OK.

   The WebObjects Java Client Interface Wizard then appears, asking you to choose templates and other options for the interface.
5. 

   Select the options that you want for the new interface file.
6. 

   Follow the subsequent instructions until completion.

After finishing the wizard, ProjectBuilder will add two files to your client-side subproject: a source (__.java__) file for the EOInterfaceController subclass and the nib file that is owned by the interface controller.
__Note:__

When you create a Java Client project, the EOInterfaceController subclass and its interface file by default have the same name as your application. If you rename these files, you must make adjustments elsewhere in your project, as described in "[Manual Adjustments to Java Client Projects](Manual%20Adjustments%20to%20Java%20Client%20Projects.md#apple-gmztgnby)
."

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Adding%20Client-side%20Subprojects.md) [!](Adding%20Web%20Components%20%28with%20Interface%20Controllers%29.md)
