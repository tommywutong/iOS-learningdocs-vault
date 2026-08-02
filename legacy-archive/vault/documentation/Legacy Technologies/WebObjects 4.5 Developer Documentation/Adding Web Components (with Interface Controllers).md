---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.3c.html
archived_at: '2026-07-15T08:09:16.507958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Adding%20Interface%20Controller%20Subclasses%20and%20Nib%20Files.md) [!](Manual%20Adjustments%20to%20Java%20Client%20Projects.md)

---

#  Adding Web Components (with Interface Controllers)

You can use Project Builder to add a web component containing a WOJavaClientApplet component with a binding to an EOInterfaceController subclass in your project. To create such a web component:

1. 

   Select the Web Components bucket in your root (main) project.
2. 

   Choose New In Project from the File menu.
3. 

   In the New File panel, enter the name of the new web component.

   This also become the name of the EOInterfaceController subclass and its interface file to be used in this web component.
4. 

   In the first screen of the WebObjects Component Wizard, select Java Client for assistance and select a language (usually Java). Click Next. (The Java Client option is disabled if your project does not contain a EOJavaClientSubproject subproject.
5. 

   If you have multiple EOJavaClientSubproject subprojects, the next wizard screen ask you to pick the one you want to associate with the component. Select a subproject and click Next.
6. 

   In the final wizard screen, select the template and associated options to use for the user interface. Follow the wizard's instructions, which vary depending on which options you choose.

When you complete these steps Project Builder adds the following files to your main project:

- 

  A web component (__.wo__) containing a __.html__ and a __.wod__ file
- 

  An __.api__ file for the component in Resources
- 

  A "skeletal" implementation file for the web component in Classes

In addition, Project Builder adds two files to the client-side subproject you chose in the wizard:

- 

  A implementation (__.java__) file for the new EOInterfaceController subclass
- 

  A nib file owned by the EOInterfaceController subclass

Project Builder presents the wizard with the Java Client assistance option _only_ if your project has at least one subproject of type EOJavaClientSubproject.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Customizing%20Your%20Project%20With%20Wizards.md) [!](Adding%20Interface%20Controller%20Subclasses%20and%20Nib%20Files.md) [!](Manual%20Adjustments%20to%20Java%20Client%20Projects.md)
