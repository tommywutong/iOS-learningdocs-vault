---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.19.html
archived_at: '2026-07-15T08:08:53.763669Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Server%20Files.md) [!](Server%20Files.md) [!](Other%20Server%20Files.md)

---

#  The WOJavaClientApplet Component

The "Applet" WEBOBJECT tag in the HTML above represents a WOJavaClientApplet component. Java Client applications use this component to create an applet (of class com.apple.client.interface.EOApplet) and to pass this applet several parameters, some standard, such as size and codebase, and others specific to Java Client applications, such as channel class and interface-controller class.

The __Main.wod__ file created by Project Builder contains the following default bindings for WOJavaClientApplet:

Applet: WOJavaClientApplet {

  height = 512;

  width = 512;

  interfaceControllerClassName =
 "studiomanager.client.StudioManager";

  useJavaPlugin = NO;

}

Note that Project Builder automatically provides the binding for __interfaceControllerClassName__ (see "[The Interface Controller](The%20Interface%20Controller.md#apple-gi3dgmbz)
," above for details).

The WOJavaClientApplet bindings specific to the EODistribution layer are:

__ Property__ |   Value ||   useJavaPlugin |   If YES, generates HTML that causes Internet Explorer and Netscape browsers to use SunSoft's Java Plug-in. |
|   distributionContext |   The EODistributionContext that the applet uses to handle requests from the client. If no binding is specified, WOJavaClientApplet instantiates one with the session's default editing context and sets the session as the delegate of the distribution context and itself as the invocation target. |
|   interfaceControllerClassName |   The name of the initial EOInterfaceController subclass. |
|   applicationClassName |   The name of the EOApplication subclass used for the shared application object. |
|   language |   The preferred language for the application. This corresponds to a localized _language___.lproj__ directory in the application's resources. When searching for localized resources, Java Client first looks in the __.lproj__ directory of the preferred language, next __English.lproj__   (if English is not the preferred language), and finally   for non-localized resources. |
|   channelClassName |   The class name of the distribution channel to be used by the client, EOHTTPChannel by default. |

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Server%20Files.md) [!](Server%20Files.md) [!](Other%20Server%20Files.md)
