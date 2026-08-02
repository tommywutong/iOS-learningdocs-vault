---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/ClientSide/Strategy.html
archived_at: '2026-07-15T07:51:10.985236Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideTOC.md) [!Previous Section](ClientSideTOC.md)

# Choosing a Strategy

You can create a client-side component out of any Java applet, provided you know some details about it. You must know the applet's accessor methods for setting and getting state, and you must know how to detect when the applet has triggered an action (for applets that trigger actions). How you create a client-side component depends on whether you have source code for the applet.
If you don't have the applet's source code, you must create your own subclass of __next.wo.client.Association__. As explained in ["How Client-Side Components Work"](../DynEl/HowClientSideWork.md#apple-gi4teny), client-side components use an Association object to communicate with the component on the server. Associations can extract values from the client-side component, set values in the client-side component, and trigger action methods on the server.

If you do have the source code, you may still want to provide your own subclass of Association. However, you're more likely to want to use the provided subclass SimpleAssociation (which is what all of the client-side components packaged with WebObjects use). The benefit of using SimpleAssociation is that it uses an AppletGroupController object. AppletGroupController is a hidden Java applet (on the client) that controls the visible applets and handles communication back to the server (see [Figure 37](#apple-gizdsoa)). The AppletGroupController accesses each of the applets on the page using an Association. It is through these Associations that the data or state each applet manages is passed to the AppletGroupController and, through it, to the server. When an Association fires its applet's action, the AppletGroupController does what is necessary to ensure that the bound method in the server is invoked. An AppletGroupController, once downloaded, knows what class of Association to use and what the destination applets are. To determine these, it inspects the visible applets on the page and looks for some special parameters.

!Figure 37. The Principal Objects Involved in Client-Side Components
SimpleAssociation objects don't get or set values themselves; instead, they rely on the actual client-side components to do so. This means that if you want to use the SimpleAssociation class, you must modify the applet so that it implements the SimpleAssociationDestination interface. This interface defines the methods that are used to get and set values.

[!Table of Contents](ClientSideTOC.md) [!Next Section](ImplementingSAD.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
