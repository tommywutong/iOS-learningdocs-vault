---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/HowWOWorks.html
archived_at: '2026-07-15T07:51:48.369036Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../DevGuideTOC.md)

# WebObjects Viewed Through Its Classes

---

As you learned at the end of the first chapter, WebObjects applications respond to HTTP requests from the server and return responses in the form of dynamically generated HTML pages. The main loop of a WebObjects application, in which the application performs this work, is called the request-response loop. You have a very broad understanding of how this works: the web browser sends a request to the HTTP server, which forwards it to the WebObjects adaptor, which translates it into a form that a WebObjects application can understand. For the response, the process is reversed.
This chapter describes in much greater detail what happens during the request-response loop. It does so by describing the request-response loop as WebObjects views it: as a communication between objects. In this chapter, you learn about the objects that are involved at each level of the loop, each object's duty during each part of the request-response loop, and the way these objects generate an appropriate HTML page in response to the user request.
In the chapter ["Common Methods"](../CommonMethods/CommonMethods.md#apple-gyytknq), you learned some of the methods that are invoked during the request-response loop, and you learned about cases where you might want to override these methods. As you write more complex WebObjects applications, it becomes necessary to know exactly what happens at each point in the processing of an HTTP request and the generation of an HTTP response. You should read this chapter to learn that level of detail. You can also refer to the class specifications in the online book [_WebObjects Class Reference_](../../Reference/Reference.md).

[****
: __The Classes in the Request-Response Loop__](WideAngleView.md#apple-gu4dcmi)

[****
: Server and Application Level](ServerAppMgmt.md#apple-ha2a)[****
: Session Level](SessionMgmt.md#apple-gy3dcma)[****
: Request Level](RRLoopInfo.md#apple-gy2tcmi)[****
: Page Level](PageComp.md#apple-g4zdoma)[****
: Database Integration Level](DBIntegration.md#apple-g42a)

[****
: __How WebObjects Works-A Class Perspective__](PhasesRRLoop.md#apple-gezti)

[****
: Starting the Request-Response Loop](StartingRRLoop.md#apple-gu3tsnq)[****
: Taking Values From the Request](TakeValues.md#apple-gmztona)

[****
: Accessing the Session](AccessSession.md#apple-guydima)[****
: Creating or Restoring the Request Page](RequestPage.md#apple-gyztcny)[****
: Assigning Input Values](AssignInputValues.md#apple-ge4tq)

[****
: Invoking an Action](InvokeAction.md#apple-he3q)[****
: Generating the Response](AppendToResponse.md#apple-geyte)

[****
: __How HTML Pages Are Generated__](ComponentElement.md#apple-gy2dsmq)

[****
: Component Templates](Templates.md#apple-gezdk)[****
: Associations and the Current Component](Associations.md#apple-gezde)[****
: Associations and Client-Side Java Components](ClientSideAssociations.md#apple-gy2tgmi)[****
: Subcomponents and Component References](Subcomponents.md#apple-gy4timi)

[!First Section](WideAngleView.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
