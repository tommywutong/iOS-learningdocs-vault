---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/PhasesRRLoop.html
archived_at: '2026-07-15T07:46:55.296718Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](ScriptedClasses.md)

# __The Phases of the Request-Response Loop__

When the adaptor receives a request for a page from the HTTP server, it sends the message __handleRequest:__ to the WebObjects application that "owns" the page. This message sets in motion a cycle of the request-response loop. This cycle consists of three phases:

- Taking values from the request
- Invoking an action
- Generating a response

Each phase is associated with a message originated by the application object. Each message passes from application to session, from session to component, and from component to (potentially) each HTML element the component contains.

__A note on terminology__: In WebObjects, a _page_ in a browser is represented by a WOComponent object, or simply, a _component_. Conceptually, this relationship is so strong, that "page" and "component" are synonymous in many of the discussions that follow. In other words, "request page" usually refers to the same thing as "request component." However, components are not always identified with an entire page; you can have nested components, called _subcomponents_ or _reusable_ _components_, that occupy only a portion of a page. See "[Subcomponents and Component References](Subcomponents.md)" for more on subcomponents.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](TakeValues.md)
