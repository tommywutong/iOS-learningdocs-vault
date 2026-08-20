---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/StartingRRLoop.html
archived_at: '2026-07-15T07:46:59.213996Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](DBIntegration.md)

# __Starting the Request-Response Loop__

A WebObjects application can start up in one of two ways: automatically, when it receives a request (autostarting), or manually, when it's run from the command line. Either way, its entry point is the same as any C program: the __main()__ function. In a WebObjects application, __main()__ is usually very short. Its job is to create and run the application:

```
int main(int argc, const char *argv[]) {

    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    WOApplication *application = [[[WOApplication alloc] init] autorelease];
    [application run];
    [pool release];
    exit(0);       // ensure the process exit status is 0

    return 0;      // ...and make main fit the ANSI spec.
}
```

The WODefaultApp application uses a __main()__ function very much like this one. When Project Builder creates a WebObjects application project (for compiled applications) it also generates a similar __main()__ function. If you write a __main()__ function, it should look identical or much the same.

This version of the __main()__ function is deceptively simple. First, it creates an autorelease pool that's used for the automatic deallocation of objects that receive an __autorelease__ message. Then it creates a WOApplication object. This seems fairly straightforward, but in the __init__ method the application creates and stores, in an instance variable, one or more adaptors. These adaptors, all instances of a WOAdaptor subclass, handle communication between an HTTP server and the WOApplication object. The application first parses the command line for specified adaptors (with necessary arguments); if none are specified, as happens when the application is autostarted, it creates a suitable default adaptor.

The __run__ method initiates the request-response loop. When __run__ is invoked, the application sends __registerForEvents__ to each of its adaptors to tell the adaptor to begin receiving events. Then the application begins running in its run loop.

As shown in Figure 2, in each cycle of the loop a WOAdaptor object for the application receives an incoming HTTP request, packages the request in a WORequest object, forwards this object to the WOApplication object in a __handleRequest__ message, and returns the response from the WOApplication to the HTTP server in a form it can understand.

!

Figure 2: Adaptor and Application in the Request-Response Loop

The last message in this version of __main()__ releases the autorelease pool, which in turn releases any object that has been added to the pool since the application began. See the introduction to the Foundation Framework for a discussion of autorelease pools and object disposal.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](ScriptedClasses.md)
