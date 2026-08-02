---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/Concepts/EOEventCenterConcepts.html
archived_at: '2026-07-15T08:13:45.123765Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md) 

# EOEventCenter.Concepts

## Event Logging Overview

The event logging system defined by EOEventCenter and EOEvent allow the measurement of the length of certain _instrumented_ operations. An EOEvent keeps information (such as duration and type) about a logged event, and an EOEventCenter manages those events. EOEvent is an abstract class whose subclasses are responsible for defining the events they track. For example, there are (private) subclasses for Sybase adaptor events, editing context events, WOApplication events, and so on. To enable event logging in an application, simply open the WOEventSetup page as described in ["WOEventSetup page" (page 89)](#apple-inbeoq2bifbuq) and enable logging for the event classes you want to see.

In addition to the framework support, the WOExtensions framework provides components for using the feature. WOEventSetup is a page you use to configure event logging, and WOEventDisplay is a page the displays event information. Both pages can be accessed in any WebObjects 4.5 application with a direct action.

## WOEventSetup page

The page used to set up the logging properties is accessed through a direct action named "WOEventSetup". So for example, you can access the WOEventSetup page for an application named "MyApp" with a URL such as the following:

```
http://myhost:aPort/cgi-bin/WebObjects/MyApp.woa/wa/WOEventSetup
```

On the WOEventSetup page, you can see all families of events that are registered for the application. Since the event classes are registered dynamically as the program executes, it is a good idea to "warm up" an application before accessing WOEventSetup.

The page lists the registered event classes, their subcategories, and a description of the kinds of events that can be logged. For instance, the EOEditingContext event class logs events for the __saveChanges__ and __objectsWithFetchSpecification__ methods. Logging for each class can be enabled and disabled with the corresponding check box; it isn't possible to disable individual subcategories of an event class.

The logging mechanism is extremely fast and memory efficient. A standard 300MHz G3 can log more than 300,000 events per second, so event logging overhead is negligible compared to the time required to generate dynamic web pages.

## User Defaults

In addition to the configuration you can do on the WOEventSetup page, the event logging system uses user defaults to additionally configure event logging behavior. The user defaults are:

- __EOEventLoggingEnabled__, a boolean value that specifies whether or not to log registered event classes by default.
- __EOEventLoggingLimit__, an integer value that specifies the number of events to log before suspending logging.

## WOEventDisplay page

The page that displays collected events, WOEventDisplay, is also accessed through a direct action. For example, you can access the WOEventSetup page for an application named "MyApp" with a URL such as the following:

```
http://myhost:aPort/cgi-bin/WebObjects/MyApp.woa/wa/WOEventDisplay
```

On this page, you can view events in four different ways:

- _Raw root events_. In this view, all events at the root level (events without an encompassing event) are displayed. WOEventDisplay shows each event individually, which means that it's possible for an event to appear multiple times if the thread of execution crossed its point more than once.
- _Aggregated root events_. This view is similar to the raw root event view, except that multiple identical events are aggregated, and their combined time is displayed. In addition, the "Calls" column shows how many times an event was executed (in other words, how many events contributed to the displayed aggregate event).
- _Events grouped by page and component_. In this view, the first level of display shows only page names. By expanding a page, you get a list of components in that page. Expanding a component shows all the events within that component. This means that even events which were collected "deep" within a component are shown immediately below the component name. All identical events are aggregated as in the aggregated root event view for easier reading. It's possible to traverse the component event hierarchy by expanding the hyperlinks within a component. Note that since a page is also a component, a page with no dynamic subcomponents seems as if it's nested one level too deep. This is the correct behavior.
- _Events grouped by page only_. This display is similar to the grouped by page and component view, except the events do not have a by-component subgrouping.

In any of these displays, if an event or event group has subevents, it can be expanded by clicking the hyperlink or triangle image.

Each view orders events by duration (in milliseconds) from the longest to the shortest. Aggregation induces rounding errors, which are a maximum of 1ms per event. In other words, an aggregate event consisting of ten events has at most 1ms deviation from the actual run time; however, manually adding ten individual events as displayed in the table might have up to a 10ms deviation. Therefore, any displayed sum is always more accurate than adding up the durations of individual events. Also note that the sub-events of an event branch doesn't necessarily add up to the duration of the branch event-the branch event's duration might be larger. This because the parent event generally consists of more than just calling the methods causing the sub-events.

## Custom Event Logging

To define and log custom events, you create an event class, you define the event's categories and subcategories, you register the event class with the WOEvent center, and you instrument the portions of code you want to log. This section describes these steps.

To create a custom event:

1. Create a subclass of EOEvent or an appropriate subclass. For example, to log events for a custom adaptor you've written, say MyAdaptor, create an EOEvent subclass named MyAdaptorEvent. Your subclass doesn't usually have to override any of the inherited methods, but you can customize the default behavior. For more information, see the EOEvent class specification.
2. Create a description file for your event and add it to your project's Resources folder. An event's description file defines the event categories and subcategories used in the WOEventDisplay page. The file's contents is a dictionary in plist format. For the MyAdaptorEvent class, the file's name is MyAdaptorEvent.description, and it might look like the following:

   ```
   {
       EOEventGroupName = "MyAdaptor Event";
       connect = "Connect";
       openChannel = "Open Channel";
       evaluateExpression = "Evaluate Expression";
       fetchRow = "Fetch Row";
       commitTransaction = "Commit Transaction";
   }
   ```

   For more information, see the eventTypeDescriptions method description in the EOEvent class specification.
3. Register the event class with the EOEventCenter. Typically you register an event class in the __initialize__ method of the class whose code you're instrumenting-MyAdaptor in this example.

   ```
   static Class MyAdaptorEventLoggingClass = Nil;
   static NSString *connectEvent = @"connect";
   static NSString *openChannelEvent = @"openChannel";
   static NSString *evaluateExpressionEvent = @"evaluateExpression";
   static NSString *fetchRowEvent = @"fetchRow";
   static NSString *commitTransactionEvent = @"commitTransaction";

   + (void)initialize {
       [EOEventCenter registerEventClass:[MyAdaptorEvent class]
               classPointer:&MyAdaptorEventLoggingClass;];
   }
   ```

   As in this example, you might want to define string constants for the keys in your event's description dictionary.
4. Instrument the methods. In any method you want to instrument, add the following code, substituting the appropriate event key. This code instruments the "connect" event of MyAdaptorEvent.

   ```
   MyAdaptorEvent *event = nil;
   // Setup and start logging
   if (MyAdaptorEventLoggingClass) {
       event = EONewEventOfClass(MyAdaptorEventLoggingClass, connectEvent);
       EOMarkStartOfEvent(event, nil);
   }

   // Code to be timed goes here.

   // Finish logging.
   if(event) {
       EOMarkEndOfEvent(event);
   ```

   The second argument to __EONewEventOfClass__ is an event key corresponding with an entry in the .description file. The corresponding value is used in the Title column of the WOEventDisplay page. If the argument isn't a key in the description dictionary, __EONewEventOfClass__ uses the argument instead. For more information on the methods used in this example, see the appropriate method descriptions in the EOEventCenter class specification.

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
