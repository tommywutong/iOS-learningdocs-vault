---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WOClassesTOC.html
archived_at: '2026-07-15T07:59:10.124415Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Top](The%20WebObjects%20Developer%27s%20Guide.md)

# WebObjects Viewed Through Its Classes

---

As you learned at the end of the first chapter, WebObjects applications respond to HTTP requests and return responses in the form of dynamically generated HTML pages. The main loop of a WebObjects application, in which the application performs this work, is called the request-response loop. You have a very broad understanding of how this works: the web browser sends a request to the HTTP server, which forwards it to the WebObjects adaptor, which translates it into a form that a WebObjects application can understand. For the response, the process is reversed.
This chapter describes in much greater detail what happens during the request-response loop. It does so by describing the request-response loop as WebObjects views it: as a communication between objects. In this chapter, you learn about the objects that are involved at each level of the loop, each object's duty during each part of the request-response loop, and the way these objects generate an appropriate HTML page in response to the user request. You also learn about the two varieties of request handling (component action and direct action) and exactly how these two differ.
In the chapter ["Common Methods"](Common%20Methods.md#apple-heydqmi), you learned some of the methods that are invoked during the request-response loop, and you learned about cases where you might want to override these methods. As you write more complex WebObjects applications, it becomes necessary to know exactly what happens at each point in the processing of an HTTP request and the generation of an HTTP response. You should read this chapter to learn that level of detail. You can also refer to the class specifications in the online book [_WebObjects Class Reference_](WebObjectsTOC.md).

[****
: __The Classes in the Request-Response Loop__](WOClasses1.md)

[****
: Server and Application Level](WOClasses2.md)[****
: Session Level](WOClasses3.md)[****
: Request Level](WOClasses4.md)[****
: Page Level](WOClasses5.md)[****
: Database Integration Level](WOClasses6.md)

[****
: __How WebObjects Works-A Class Perspective__](WOClasses7.md)

[****
: Starting the Request-Response Loop](WOClasses8.md)[****
: Determining the Request Type](WOClasses9.md)[****
: Handling Component Action Requests](WOClasses10.md)

[****
: Accessing the Session](WOClasses11.md)[****
: Creating or Restoring the Request Page](WOClasses12.md)[****
: Taking Input Values From a Request](WOClasses13.md)[****
: Invoking an Action](WOClasses14.md)[****
: Generating the Response](WOClasses15.md)[****
: Request Post-Processing](WOClasses16.md)

[****
: Handling Direct Action Requests](WOClasses17.md)

[****
: Invoking the Action](WOClasses17.md#apple-haydmmq)[****
: Generating the Response](WOClasses17.md#apple-haydsni)[****
: Request Post-Processing](WOClasses17.md#apple-g44teni)

[****
: Component Actions vs. Direct Actions](WOClasses18.md)

[****
: __How HTML Pages Are Generated__](WOClasses19.md)

[****
: Component Templates](WOClasses20.md)[****
: Associations and the Current Component](WOClasses21.md)[****
: Subcomponents and Component References](WOClasses22.md)

[!First Section](The%20Classes%20in%20the%20Request-Response%20Loop.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
