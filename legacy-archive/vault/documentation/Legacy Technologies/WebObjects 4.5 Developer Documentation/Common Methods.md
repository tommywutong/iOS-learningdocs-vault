---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods.html
archived_at: '2026-07-15T08:05:49.141489Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Top](The%20WebObjects%20Developer%27s%20Guide.md)

#

# Common Methods

---

The methods that you write for your WebObjects application provide the behavior that makes your application unique. Because you are writing subclasses of WOApplication, WOSession, WOComponent, and WODirectAction you inherit the methods provided by those classes. These inherited methods take care of the details of receiving HTTP requests and generating responses. However, you'll sometimes find that you need to override some of the inherited methods to perform certain tasks.
This chapter describes the types of methods that you generally write in a WebObjects application. These types are:

- Action methods
- Initialization and deallocation methods
- Request-handling methods

In cases where you override existing methods, those methods are invoked at standard, predictable times during the application's request-response loop (the main loop for a WebObjects application). For background on the request-response loop, see the chapter ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy).

As you're writing methods, refer to the class specifications for WOApplication, WOSession, WOComponent, and WODirectAction to learn which messages you can send to these objects. The class specifications are in the online book [_WebObjects Class Reference_](WebObjects%20Java%20API%20Reference.md).

[****
: __Action Methods__](Methods1.md)

[****
: Component Actions](Methods2.md)[****
: Direct Actions](Methods3.md)[****
: Suppressing Session IDs in a Direct Action URL](Methods4.md)[****
: Setting the Default Request Handler](Methods5.md)

[****
: __Initialization and Deallocation Methods__](Methods6.md)

[****
: The Structure of init](Methods7.md)[****
: Application Initialization](Methods8.md)[****
: Session Initialization](Methods9.md)[****
: Component Initialization
[****
: WODirectAction Initialization](Methods11.md)](Methods10.md)

[****
: __Component-Action Request-Handling Methods__](Methods12.md)

[****
: Request Handling Initialization and Post-Processing](Methods13.md)[****
: Application Awake](Methods14.md)[****
: Session Awake](Methods15.md)[****
: Component Awake
[****
: Taking Input Values From a Request](Methods17.md)[****
: Invoking an Action](Methods18.md)[****
: Limitations on Direct Requests](Methods19.md)[****
: Generating a Response](Methods20.md)](Methods16.md)

[!First Section](Action%20Methods.md)
