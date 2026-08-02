---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.2a.html
archived_at: '2026-07-15T07:59:54.748377Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.29.md) | [Back Up One Level](CSJ_Tutorial.26.md) | [Next](CSJ_Tutorial.2b.md)

###   Manual Adjustments to Java Client Projects

You should always use the Java Client wizards if you can because the files that they generate have characteristics that are important for Java Client applications. These files have various dependencies and assumptions, which you must know about if you decide to create them manually.

- If you create a subproject of type EOJavaClientSubproject by hand, make sure that __EOJavaClient.framework__
  is added to the frameworks of the main project. Otherwise the compiler might not find all the Java Client classes required by the interface controllers.

- The file's owner class of an Java Client interface (nib) file must be the EOInterfaceController subclass that uses it. It is also very important that the package name of the file's owner class is identical to the package name of the interface controller. So if you change the package of the interface controller, you have to open the interface file in Interface Builder and change the name of the EOInterfaceController subclass used for the file's owner.

- The "interfaceControllerClassName" binding of WOJavaClientApplet used in web components has to be the complete class name of an interface controller in a EOJavaClientSubproject, including the full package prefix. If you change the package of the interface controller, you have to change the value of the "interfaceControllerClassName" binding.

- If you change the size of a window in a nib file which is later placed in a WOJavaClientApplet (because the WOJavaClientApplet uses the corresponding EOInterfaceController subclass), you have to modify the size bindings of the WOJavaClientApplet so that the window contents still fit into it.

- You might want to add additional bindings to a WOJavaClientApplet. This component takes standard java.applet bindings plus some special Java Client ones. See "[The Ingredients of a Java Client Project](CSJ_Tutorial.d.md#apple-gmytamzu)
  " in the tutorial for more information or refer to the WOJavaClientApplet directory in the WebObjects Java Client examples for a complete list of bindings.
  
- If you use Sun's Java Plug-in, you must set the value of the "useJavaPlugin" binding of all WOJavaClientApplets to YES.

A typical __.wod__
file for a web component using a WOJavaClientApplet looks like this:

`

Applet: WOJavaClientApplet {

    height = 567;

    width = 695;

    interfaceControllerClassName = "movie.client.Movie";

    useJavaPlugin = NO;

}`

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.29.md) | [Back Up One Level](CSJ_Tutorial.26.md) | [Next](CSJ_Tutorial.2b.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
