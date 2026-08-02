---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/RRLoopInfo.html
archived_at: '2026-07-15T07:46:55.704988Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](SessionMgt.md)

# __Request-Response Loop Information__

A request-response cycle (sometimes called a _transaction_) has three phases, the first for transferring user-entered data to the objects associated with the request page, the second for invoking an action method, and the third for generating and returning the response. The application initiates each phase by sending a messages: __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__ It passes in WORequest, WOResponse, and WOContext objects as arguments to one or more of these methods. From these objects, the components, dynamic elements, and other objects involved in the transaction get essential information. (See "[The Phases of the Request-Response Loop](PhasesRRLoop.md#apple-kjcumnzuge4ds)" for more on the mechanics of request handling).

!

**- WORequest**
: Stores essential data about an HTTP request, such as header information, form values, HTTP version, host and page name, and session, context, and sender IDs.

**- WOResponse**
: Stores and allows the modification of HTTP response data, such as header information, status, and HTTP version. It also provides convenience methods for appending HTML and simple textual data to the content of the response (that is, the response page).

**- WOContext**
: Provides access to the objects involved in the current transaction, including the current request, response, session, and application objects. It also stores the component (which is either the current page or one of its subcomponents) to which the elements of the page make reference when they "push and pull" values via association (see "[Component and Element](ComponentElement.md)" for an explanation of this). The WOContext object acts as a "cursor" for traversing the object graph during a phase of the request-response loop. The WOContext for a transaction is identified by a unique context ID, which appears in the URL.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](PageComp.md)
