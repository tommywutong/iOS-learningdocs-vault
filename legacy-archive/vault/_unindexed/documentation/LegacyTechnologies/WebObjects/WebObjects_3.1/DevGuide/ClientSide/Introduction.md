---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/Introduction.html
archived_at: '2026-07-15T07:46:38.720767Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)

# Introduction

Programs written for the World Wide Web implicitly acknowledge a well-defined and somewhat limiting separation between the client (browser) and the server. Data can pass from server to the browser and back again, but only under rigidly controlled conditions. This is considered true of object-oriented programs as well as procedural programs. For example, you can have objects on the server side of a connection and objects on the browser side that have been downloaded from the server. The server can pass initial values to the downloaded objects, but once they're on the page, these objects tend to be pretty much on their own.

A feature named _Java client-side components_ bridges this "gulf." It enables Java applets on the client side to synchronize their states continuously with objects on the server side. Java client-side components also allow applets to trigger action methods on the server.

There are several advantages to using client-side components in a WebObjects application. The most obvious benefit is that Java applets have almost none of the limitations of forms. HTML forms are fixed and limited as to what they can do or how they look. You have fields and buttons, and not much else. Applets, on the other hand, are true programs with a graphical user interface, set in the context of an HTML browser. Applets can be just about any imaginable control on a page: a dynamic calendar, a spreadsheet, a graphing tool. If a control that you need doesn't exist, you can create it, with a little work. And with a little extra work, you can get the applet to work with the objects on the server side of a WebObjects application.

Another advantage of Java client-side components results from the way these components---that is, the applet controls---communicate with the server. Previously, the initial state of applets could be downloaded from the server, but that ended the communication. There was no way the applets could pass data back to the server or receive any subsequent updated state from the server.

Client-side components enable applet controls to synchronize any change in their state with the server and to receive back any further change in that state made by the server-side component. This state synchronization occurs in a request-response cycle in which the response-generation phase is used primarily to return state. As a result, state is synchronized without the page being reloaded.

Furthermore, client-side components allow users to activate applet controls to trigger action methods in the server component, and elicit responses that can result in the re-synchronization of state _`or`_ the return of a new page.

It's easy to think of potential uses of client-side components. For example, you could have a tax-preparation application in which an assortment of applets represent a tax form. The aggregate applet itself performs calculations on the entered data, but it downloads timely information like tax tables from the server. When a form is complete, the user could trigger an action method to store the current tax record in a database.

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](IfDoesntWork.md)
