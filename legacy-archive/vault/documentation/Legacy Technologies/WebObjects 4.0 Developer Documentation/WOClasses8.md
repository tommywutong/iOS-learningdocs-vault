---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WOClasses8.html
archived_at: '2026-07-18T01:20:34.112212Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](How%20WebObjects%20Works-A%20Class%20Perspective.md)

## Starting the Request-Response Loop

A WebObjects application's entry point is the same as that of any C program: the __main__ function. In a WebObjects application, __main__ is usually very short. Its job is to create and run the application.
The __main__ function typically consists of a single line of code that calls the __WOApplicationMain__ function, passing the name of your application's principal class and any arguments you may have passed to your application. __WOApplicationMain__ processes any arguments, then creates an instance of your principal class (which should be a subclass of WOApplication, and is named __Application__ by default). In your application class' __init__ method (or constructor) the application creates and stores one or more adaptors in an instance variable. These adaptors-all instances of a WOAdaptor subclass-handle communication between an HTTP server and the WOApplication object. The application first parses user defaults dictionary for the specified adaptors (with necessary arguments); if none are specified, it creates a suitable default adaptor.
Also during application initialization, the application object creates its pool of WORequestHandlers. By default, applications have three request handlers: one for component actions (WOComponentRequestHandler), one for direct actions (WODirectActionRequestHandler), and one for resource requests (WOResourceRequestHandler). All three of these are private subclasses of WORequestHandler. If your application has additional request handlers, they should be registered with the application at application initialization time.
After your application class has been initialized, __WOApplicationMain__ sends it a __run__ message, initiating the request-response loop. When __run__ is invoked, the application sends __registerForEvents__ to each of its adaptors to tell them to begin receiving events. Then the application begins running in its run loop.
The autorelease pool is released and recreated immediately before the __run__ message is sent. Releasing the autorelease pool at this point releases any temporary variables created during initialization of the application class. Creating a new autorelease pool before sending __run__ ensures that all variables created while running the application will be released eventually. The last message releases the autorelease pool, which in turn releases any object that has been added to the pool since the application started running.
In the rest of this section, we look at what happens during one complete cycle of the request-response loop.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
