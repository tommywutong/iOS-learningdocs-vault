---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/AppendToResponse.html
archived_at: '2026-07-15T07:46:48.707670Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](InvokeAction.md)

# __Generating the Response__

In the final phase of request-response loop, the response page generates an HTTP response. Generally, the response contains a dynamically generated HTML page. Each element (static and dynamic) that makes up the response page appends its HTML to the total stream of HTML code that will be interpreted by the client browser.

This is the basic sequence of events in generating a response:

1. The WOApplication object stores the object returned from an invoked action method as the current page for the transaction.
2. Then it sends __appendToResponse:inContext:__ to itself; its implementation simply invokes the WOSession object's __appendToResponse:inContext:__.
3. The session, in its implementation of __appendToResponse:inContext:__, pushes the response component onto the WOContext stack, gets the template for the component, and sends __appendToResponse:inContext:__ to the template.
4. All static and dynamic HTML elements in the response-page template, and in subcomponent templates, receivethe __appendToResponse:inContext:__ message. In it, they append to the content of the response the HTML code that represents them. For dynamic elements, this code includes the values assigned to variables.

After the response has been generated, but before returning the response to the adaptor, the application object concludes request handling by doing the following:

1. It causes the __sleep__ method---the counterpart of __awake__---to be invoked in all components involved the transaction (request, response, and subcomponents). In __sleep__ objects can release resources that don't have to be saved between transactions.
2. Then the application requests the session object to save (cache) the response page.
3. It invokes the session object's __sleep__ method and saves the session object.
4. It invokes its own __sleep__ method.

When an object is about to be destroyed, its __dealloc__ method is invoked. This happens some at some indefinite point after a transaction (indicated by vertical ellipses in the diagram below). In the __dealloc__ method, the object should release any retained instance variable. (In scripted applications this is unnecessary since "garbage collection" occurs automatically in this case.)

!

Figure 5: Generating the Response


```

```

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](ComponentElement.md)
