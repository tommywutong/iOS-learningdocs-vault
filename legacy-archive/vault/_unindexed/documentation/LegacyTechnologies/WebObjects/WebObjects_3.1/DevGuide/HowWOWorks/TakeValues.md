---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/TakeValues.html
archived_at: '2026-07-15T07:47:01.268906Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](PhasesRRLoop.md)

# __Taking Values From the Request__

The purpose of this first phase is to synchronize the state of the request component with the HTML page as submitted by the user. In this phase, the appropriate dynamic elements extract the values that users enter and the choices they make in the request page and assign them to declared variables. For example, if the user clicked a check box, the dynamic element that represents that check box must be set to the "checked" state. In other words, the __checked__ attribute of the appropriate WOCheckbox dynamic element must be set to YES.

__Note__: The discussion of each phase includes a diagram that---using a matrix of object, relationship, and sequence---lays out the messages invoked and the tasks accomplished in the phase. The diagram is thus mean to accompany the discussion of these specific messages and tasks. The three diagrams, taken together, constitute a diagram of the entire request-response loop. The following diagram shows what goes on in the first phase:

!

Figure 3: Taking Values from the Request

Upon receiving __handleRequest:__ from a WOAdaptor, the application first creates the WOResponse and WOContext objects that will be needed (the WORequest object is passed in). Then it does the following:

- It invokes its own __awake__ method.
- It restores the WOSession object for the transaction (thereby restoring all session variables) or, if this is the first request from a particular user, it creates a WOSession object. In the latter case, the WOSession's __init__ method is invoked.
- It invokes the session's __awake__ method.

## __Creating or Restoring the Request Page__

Each request received by a WebObjects application is associated with one of the application's pages---the _request page_. If the request doesn't explicitly specify a page, the WOApplication object associates the request with a page named "Main." By default, an application caches page instances once they're created, primarily to facilitate backtracking: when users backtrack, they're revisiting pages restored by the application. During the first phase of the request-response loop, the application restores the component instance that generated the response page earlier in the current session; if this instance doesn't exist, the application creates a component to represent the request page.

The component instance for the request page cannot be restored and must be created if:

- The page-caching feature is turned off.
- The request is the first for that page during the session.

This component---called the _request component_---is an instance of a WOComponent subclass (created automatically for scripted applications). The WOApplication object performs the following steps to create a WOComponent object:

1. It looks in the Objective-C run-time system for a WOComponent subclass with the same name as the request page. If it finds such a class with the same name, it creates an instance of that class. For example, if the request specifies a request page named "LoginPanel" and a class with the same name is present in the Objective-C runtime system, the WOComponent instantiates a LoginPanel object as the request component.
2. If the WOApplication object fails to find a class in the run-time system, it looks for a scripted component with the name of the request page. When it finds the ".wo" directory, it creates a component object using a unique WOComponent subclass for the scripted component and makes the scripted code the class implementation.

When a component is created its __init__ method is invoked. The __awake__ method of both restored and created components is also invoked. In other words, the __awake__ method of request components, as well as for the application and session objects, is invoked once per transaction. (There is one exception to this: When the response component is the same as the request component, __awake__ is not invoked.)

## __Assigning Input Values__

During the first phase of the request-response loop, the request component extracts user-entered values and assigns them to transaction variables. This is the basic sequence of events in preparing for a request:

1. The WOApplication object sends __takeValuesFromRequest:inContext:__ to itself; its implementation simply invokes the WOSession object's __takeValuesFromRequest:inContext:__.
2. The session, in its implementation of __takeValuesFromRequest:inContext:__, gets the _template_ of the component and forwards the message to it. A template consists of the static HTML elements, dynamic HTML elements, and subcomponents that together compose the page associated with a component instance. (See "[Templates](Templates.md#apple-kjcumnrzgm4do)" for more on this subject.)
3. All dynamic elements in the page template, and in the templates of subcomponents, receive the __takeValuesFromRequest:inContext:__ message. If one of these elements "owns" a user-entered value, it responds to the message by storing the value in the appropriate variable defined in the request component's declarations file.

For more on how components are associated with templates, and on how HTML elements participate in request-handling, see "[Component and Element](ComponentElement.md#apple-kjcumnbwgy4ds)."

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](InvokeAction.md)
