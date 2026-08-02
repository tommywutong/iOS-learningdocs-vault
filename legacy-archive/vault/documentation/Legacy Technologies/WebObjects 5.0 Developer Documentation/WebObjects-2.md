---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Introduction.html
archived_at: '2026-07-15T08:15:15.973978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](WebObjectsTOC.md)

# WebObjects

> **__Package:__**
> : com.webobjects.appserver

---

## Introduction

The WebObjects class hierarchy is rooted in the java.lang.Object class. The bulk of the WebObjects framework consists of several related groups of classes as well as a few individual classes.

The more commonly-used classes within the WebObjects framework can be grouped as follows:

- Server and Application Level Classes. WOAdaptor defines the interface for objects mediating the exchange of data between an HTTP server and a WebObjects application. WOApplication receives requests from the adaptor and initiates and coordinates the request-handling process, after which it returns a response to the adaptor.
- Session Level Classes. WOSession encapsulates the state of a session; WOSession objects persiste between the cycles of the request-response loop. WOSessionStore provides the strategy or mechanism through which WOSession objects are made persistent.
- Request Level Classes. WORequest and WOResponse, along with their parent class WOMessage, store essential data about HTTP requests and responses, such as header information, form values, HTTP version, host and page name, and session, context, and sender IDs. WOContext provides access to the objects involved in the current cycle, such as the current request, response, session, and application objects.
- Page Level Classes. WOComponent represents an integral, reusable page (or portion of a page) for display in a web browser. WOElement declares the three request-handling methods: takeValuesFromRequest, invokeActionForRequest, and appendToResponse. WODynamicElement is an abstract class for subclasses that generate particular dynamic elements. WOAssociation knows how to find and set a value by reference to a key.
- Database Integration Level Classes. WODisplayGroup performs fetches, queries, creations, and deletions of records from one table in the database.

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
