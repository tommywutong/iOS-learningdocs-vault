---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Advanced/Customizing__Assistants.html
archived_at: '2026-07-15T08:13:58.219328Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Debugging_J_pplications.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/index.html)

## Customizing Your Project With Assistants

Project Builder includes several features, including assistants,
that you can-and should-use to add Web components, interface-controller
subclasses, and client-side interface files to Java Client applications.
This is especially true with interface (nib) files; never create
a client-side nib file using Interface Builder (as, for instance,
by choosing the New Database Interface command from the Document
menu).

### Adding Interface Controller Subclasses and Nib Files

To add an EOInterfaceController subclass with a new interface
file to your client-side subproject

1. Select the
   Interfaces group in your project file.
2. Chose File > New File.
3. Select WebObjects > Java Client Interface and click Next.
4. Enter the filename for the new EOInterfaceController subclass
   and select its location.
5. Select the Client target and click Next.
6. Enter class and package names for the new interface class
   and click Next.
7. Select the options that you want for the new interface file.

   Choose
   the template and available options that you want your interface
   to use.
8. Follow the subsequent instructions until completion.

After finishing the assistant, Project Builder will add two
files to your project: a source (`.java`)
file for the EOInterfaceController subclass and the nib file that
is owned by the interface controller.

|  |
| --- |
| __Note:__ When you create a Java Client project, the EOInterfaceController subclass and its interface file by default have the same name as your application. If you rename these files, you must make adjustments elsewhere in your project, as described in ["Manual Adjustments to Java Client Projects"](#apple-ijbusqsbjfceo). |

### Adding Web Components (with Interface Controllers)

You can use Project Builder to add a web component containing
a WOJavaClientApplet component with a binding to an EOInterfaceController
subclass in your project. To create such a Web Component

1. Select the
   Web Components group in your root (main) project.
2. Choose File > New File.
3. Select WebObjects/Component.
4. Click Next.
5. Enter a the name and location of the new component.
6. Select the Server target.
7. Click Finish.

When you complete these steps Project Builder adds the following
to your project:

- a subgroup
  named after your component in the Web Components group
- a Web Component (`.wo`)
  containing a `.html` and
  a `.wod` file
- an `.api` file for
  the component
- a `.java` file

### Manual Adjustments to Java Client Projects

You should always use the Java Client wizards if you can because
the files that they generate have characteristics that are important
for Java Client applications. These files have various dependencies
and assumptions, which you must know about if you decide to create
them manually.

- The file's
  owner class of an Java Client interface (nib) file must be the EOInterfaceController
  subclass that uses it. It is also very important that the package name
  of the file's owner class is identical to the package name of the
  interface controller. So if you change the package of the interface
  controller, you have to open the interface file in Interface Builder
  and change the name of the EOInterfaceController subclass used for
  the file's owner.
- The `interfaceControllerClassName` binding
  of WOJavaClientApplet used in web components has to be the complete
  class name of an interface controller, including the full package
  prefix. If you change the package of the interface controller, you
  have to change the value of the `interfaceControllerClassName` binding.
- If you change the size of a window in a nib file which is
  later placed in a WOJavaClientApplet (because the WOJavaClientApplet
  uses the corresponding EOInterfaceController subclass), you have
  to modify the size bindings of the WOJavaClientApplet so that the
  window contents still fit into it.
- You might want to add additional bindings to a WOJavaClientApplet.
  This component takes standard java.applet bindings
  plus some special Java Client ones. See ["The Ingredients of a Java Client Project"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/iThe_Ingredi_ent_Project.html) for more information or refer to the WOJavaClientApplet
  directory in the WebObjects Java Client examples for a complete list
  of bindings.

[![Previous](attachments/JavaClient/Images/previous.gif)](Debugging_J_pplications.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
