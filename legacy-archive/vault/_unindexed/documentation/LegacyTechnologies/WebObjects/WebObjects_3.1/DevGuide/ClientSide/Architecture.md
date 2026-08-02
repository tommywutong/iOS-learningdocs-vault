---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/Architecture.html
archived_at: '2026-07-15T07:46:31.305874Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](IfDoesntWork.md)

# How Client-Side Components Work

Client-side components have a duality in that they are represented by objects both on the client browser and in the server component. On the client side they are specially modified or interfaced applets. On the server side, they are represented by WOApplet dynamic elements.

A WOApplet dynamic element is a kind of "proxy" on the server for the applet. A WOApplet permits the specification of applet-specific parameters, such as the dimensions of the applet and the location of the ".class" file to download to the browser. It also allows you to initialize parameters to be downloaded to the applet and to bind an applet's keys to variables and methods in the server-side component. These bindings associate state in the applet with state in the server and events in the applet with the invocation of methods in the server. What makes these bindings possible is another parameter specified in a WOApplet declaration: an association class. By providing an association class, you endow an applet with the capabilities of state synchronization and action invocation.

Before delving further into the subject of Associations, first consider the keys defined by an applet and how state synchronization happens. An application determines the keys of an applet through the class of the applet (specified in the __code__ attribute) and the applet's association class (specified in __associationClass__). Keys fall into two groups: state bindings and action bindings. State bindings form the basis for state synchronization by associating state in the applets with state in the server. Action bindings associate particular events in the client applet (such as button being clicked) with the invocation of methods in the server.

!

__Figure 1__: Bindings Between Client and Server Components

State is synchronized between client and server in three phases:

1. When a page is first generated the server sends all state for which there are bindings to the client.
2. Before an action is invoked in the server, the client sends any of its state that has changed back to the server.
3. After the action is completed, the server sends of its state that has changed back to the client.

This last synchronization occurs only if no new page is returned to the browser. When a method invoked remotely through an applet action binding returns __nil__, it signals that, instead of returning a new page, the server should re-synchronized its state with the applets on the page. WebObjects "snapshots" the changes in state in the server so that only the state that has changed is sent back to the client.

__Note__: The last two phases of synchronization cycle can only be initiated on the browser side. That is, except for the first "initialization" phase, the server component can only react to an action triggered in an applet. The component cannot unilaterally update the state of an applet when its own state changes.

An Association object---specifically an instance of an Association subclass---provides the "glue" that secures the bindings of state and action between client and server. Associations know how to get and set the state of their applets at run time. They are also responsible for knowing when to fire their applets' supported actions. To enable this, Associations for particular applets maintain a list of "keys" (state attributes) that the applet manages and a list of actions that the applet can trigger. The value for a "key" must be a property-list type of object (either singly or in combination, such as an array of string objects). The corresponding property-list type of objects for Objective-C and Java are:

__Table 1__: Valid Property List Objects

| Objective-C | Java |
| --- | --- |
| NSString | String |
| NSArray | Vector |
| NSDictionary | Hashtable |
| NSData | byte[] |

Associations, however, don't act alone. They mediate the exchange of state and action information between their applets and a hidden applet downloaded along with the applets that appear on the page. This hidden applet, AppletGroupController, controls the visible applets and handles communication back to the server. The AppletGroupController uses an Association to access each of the applets on the page. It is through these Associations that the data or state which each applet manages is passed to the AppletGroupController and, through it, to the server. When an Association fires its applet's action, the AppletGroupController does what is necessary to ensure that the bound method in the server is invoked. An AppletGroupController, once downloaded, knows what class of Association to use and what the destination applets are by inspecting the visible applets on the page and looking for some special parameters.

!

__Figure 2__: The Principal Objects Involved in Client-Side Components

Sometimes an Association subclass can be tied to a particular "family" of applets instead a particular applet. Such is the case with applets provided by NeXT. These applets use the SimpleAssociation class, but get and set the key values themselves. To do this, they assume most of the duties of the Association by implementing the SimpleAssociationDestination interface. You can adopt this strategy with applets that you create. See "[Making Your Own Java Client-Side Components](MakingOwn0.md)" for more information on this subject.

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](Integrating0.md)
