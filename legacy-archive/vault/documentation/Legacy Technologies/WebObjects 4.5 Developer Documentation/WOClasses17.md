---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses17.html
archived_at: '2026-07-15T08:06:14.157860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses16.md)

## Handling Direct Action Requests

As you saw in the previous section, component action requests are handled in three basic phases: taking input values from the request, invoking the action, and generating the response. The WOApplication, WOSession, and WOComponent objects are involved in each phase. Direct actions have a simpler request-response loop cycle.
When the direct action request handler receives the __handleRequest:__ message from the application, its first step is to determine what action should be performed and by what object. It does so by looking at the request URL. The URL for a direct action request looks like the one shown in [Figure 27](#apple-haydgmi).

!

Figure 27. Direct Action Request URL

The WODirectAction class field is optional. If the WODirectAction class isn't specified in the URL, a subclass named DirectAction is assumed.
If the request is the first one for a given user session, the request URL looks like the URL shown in [Figure 20](WOClasses9.md#apple-g43dcnq). This URL contains neither a WODirectAction class name nor an action name. In this case, the direct action request handler assumes that the action to be performed is the __defaultAction__ method in the class DirectAction. Remember that the direct action request handler does not process the first request in a session unless you send the __setDefaultRequestHandler:__ to the WOApplication and specify the WODirectActionRequestHandler.

Since URLs can contain class names, the WODirectActionRequestHandler always checks to make sure that the class specified is a subclass of WODirectAction.

### Invoking the Action

Once the direct action request handler has determined the action to be performed and which object should perform the action, the handler does the following:

- It creates an instance of the appropriate WODirectAction subclass, which in turn creates a WOContext object.
- It sends that instance a __performActionNamed:__ message.
- In its implementation of __performActionNamed:__, the WODirectAction object looks for a method named _action___Action__. For example, if the action specified in the URL is "display", WODirectAction looks for a method named __displayAction__. It then invokes that method.
- If necessary, the action method takes input values from the request and assigns them either to its own local variables or to the object's instance variables.

With direct actions, all input values are in the WORequest object as form values. If the form method was a "GET" then the URL contains the form values.

- When it is finished processing, the action method invoked in the previous step returns either a WOResponse or WOComponent object. The WODirectAction object returns that object to the direct action request handler.

### Generating the Response

Upon receiving a return value from __performActionNamed:__, the direct action request handler sends the returned object a __generateResponse__ message. Typically, the returned object is a WOComponent. When a WOComponent receives __generateResponse__ message, the following sequence of events take place:

- The component gets the template for itself and sends __appendToResponse:inContext:__ to the template's root object.
- All static and dynamic HTML elements in the component's template, and in subcomponent templates, receive the __appendToResponse:inContext:__ message. In it, they append to the content of the response the HTML code that represents them. For dynamic elements, this code includes the values assigned to variables.

The object returned by __performActionNamed:__ can actually be any object that conforms to the WOActionResults procotol (or Java interface). WOActionResults defines the __generateResponse__ method. In the WebObjects framework, two classes conform to WOActionResults: WOResponse and WOComponent. (When a WOResponse object receives __generateResponse__, it simply returns itself.)

### Request Post-Processing

After the response has been generated, but before returning the response to the application, the direct action request handler concludes request handling by releasing the WODirectAction instance it created, or in Java, marking it for garbage collection. If the WODirectAction created a component and returned that as the response, that component is released along with the WODirectAction. Thus, in the default implementation, WODirectActions do not maintain any session state between cycles of the request-response loop.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses18.md)
