---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements8.html
archived_at: '2026-07-18T01:20:10.848306Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements7.md)

## Creating Client-Side Components

You can create your own client-side component if the components supplied with WebObjects don't suit your needs or if you already have a Java applet that you would like to use as a client-side component. You can create a client-side component out of any Java applet, provided you know some details about it. You must know the applet's accessor methods for setting and getting state, and you must know how to detect when the applet has triggered an action (for applets that trigger actions). How you create a client-side component depends on whether you have source code for the applet.
If you don't have the applet's source code, you must create your own subclass of __com.apple.client.webobjects.Association__. As explained in ["How Client-Side Components Work"](DynamicElements7.md#apple-gi4teny), client-side components use an Association to communicate with the component on the server. Associations can extract values from the client-side component, set values in the client-side component, and trigger action methods on the server.

If you do have the source code, you may still want to provide your own subclass of Association. However, you're more likely to want to use the provided subclass SimpleAssociation (which is what all of the client-side components packaged with WebObjects use). All associations are linked on one side to one of your applets, and on the other to an AppletGroupController. AppletGroupController is a hidden Java applet (on the client) that controls the visible applets and handles communication back to the server (see [Figure 14](#apple-guztmni)). The AppletGroupController accesses each of the applets on the page using an Association. It is through these Associations that the data or state each applet manages is passed to the AppletGroupController and, through it, to the server. When an applet fires an action on its association, the AppletGroupController does what is necessary to ensure that the bound method in the server is invoked. An AppletGroupController, once downloaded, knows what class of Association to use and what the destination applets are. To determine these, it inspects the visible applets on the page and looks for some special parameters.

!

Figure 14. The Principal Objects Involved in Client-Side Components

SimpleAssociation objects don't get or set values themselves; instead, they rely on the actual client-side components and on the AppletGroupController to do so. This means that if you want to use the SimpleAssociation class, you must modify the applet so that it implements the SimpleAssociationDestination interface. This interface defines the methods that are used to get and set values.

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
