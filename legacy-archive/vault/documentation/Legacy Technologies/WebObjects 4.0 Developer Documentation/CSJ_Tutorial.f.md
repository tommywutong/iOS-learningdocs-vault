---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.f.html
archived_at: '2026-07-15T08:00:18.382233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.e.md) | [Back Up One Level](CSJ_Tutorial.d.md) | [Next](CSJ_Tutorial.10.md)

###  Server Files

The server-side project files are, as usual, accessible from the first column of the project browser (the main project). Most notable of these is the Main component (__Main.wo__
) in the WebComponents suitcase. The __Main.html__
file contains this generated HTML code:

<HTML>

<HEAD>

   

<TITLE>Main</TITLE>

</HEAD>

<BODY>

   

<CENTER><WEBOBJECT NAME=Applet></WEBOBJECT></CENTER>

</BODY>

</HTML>

###  The WOJavaClientApplet Component

The "Applet" WEBOBJECT tag in the HTML above represents a WOJavaClientApplet component. Java Client applications use this component to create an applet (of class com.apple.client.interface.EOApplet) and to pass this applet several parameters, some standard, such as size and codebase, and others specific to Java Client applications, such as channel class and interface-controller class.

The __Main.wod__
file created by Project Builder contains the following default bindings for WOJavaClientApplet:

Applet: WOJavaClientApplet {

height = 512;

   

width = 512;

   

interfaceControllerClassName =
"studiomanager.client.StudioManager";

   

useJavaPlugin = NO;

}

Note that Project Builder automatically provides the binding for __interfaceControllerClassName__
(see "[The Interface Controller](CSJ_Tutorial.e.md#apple-gi3dgmbz)
," above for details).

The WOJavaClientApplet bindings specific to the EODistribution layer are:

|   Property |   Value |
| --- | --- |
|   useJavaPlugin |   If YES, generates HTML that causes Internet Explorer and Netscape browsers to use SunSoft's Java Plug-in. |
|   distributionContext |   The EODistributionContext that the applet uses to handle requests from the client. If no binding is specified, WOJavaClientApplet instantiates one with the session's default editing context and sets the session as the delegate of the distribution context and itself as the invocation target. |
|   interfaceControllerClassName |   The name of the initial EOInterfaceController subclass. |
|   applicationClassName |   The name of the EOApplication subclass used for the shared application object. |
|   language |   The preferred language for the application. This corresponds to a localized _language_ __.lproj__ directory in the application's resources. When searching for localized resources, Java Client first looks in the __.lproj__ directory of the preferred language, next __English.lproj__   (if English is not the preferred language), and finally   for non-localized resources. |
|   channelClassName |   The class name of the distribution channel to be used by the client, EOHTTPChannel by default. |

###  Other Server Files

A Java Client project includes these other server-side files:

- 

  The application, session, and direct action class (__.java__
  ) files; if you selected Objective-C as the primary language, these would be Objective-C implementation (__.m__
  ) and header files.

- In the Resources suitcase, the model file (__StudioManager.eomodeld__
  )

- Also in the Resources suitcase, the exported bindings file for the Main component (__Main.api__
  )

- In the Supporting Files suitcase, the makefiles __Makefile__
  , __Makefile.preamble__
  , and __Makefile.postamble__
  .

__Related Concepts:__

[Customizing Your Project With Wizards](CSJ_Tutorial.26.md#apple-gi3tinzs)

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.e.md) | [Back Up One Level](CSJ_Tutorial.d.md) | [Next](CSJ_Tutorial.10.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
