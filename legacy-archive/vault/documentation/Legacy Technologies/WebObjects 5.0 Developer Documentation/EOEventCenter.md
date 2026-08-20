---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOEventCenter.html
archived_at: '2026-07-15T08:13:46.834368Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOEventCenter

> __Inherits from:__ Object

> __Package:__ com.webobjects.eocontrol

---

## Class Description

---

EOEventCenter collects and manages EOEvents to allow you to measure the duration of operations in your applications. Measurements allow you to profile an application and optimize its execution time. For this, Enterprise Objects Framework and WebObjects instrument key portions of their code to measure the elapsed time of functions and methods.

For more information on the event logging feature and on instrumenting your own code for event logging, see the following sections:

- ["Event Logging Overview" (page 89)](EOEventCenter.Concepts.md#apple-inbeoq2gi5cuk)
- ["WOEventSetup page" (page 89)](EOEventCenter.Concepts.md#apple-inbeoq2bifbuq)
- ["WOEventDisplay page" (page 90)](EOEventCenter.Concepts.md#apple-inauqr2eivduo)
- ["Custom Event Logging" (page 91)](EOEventCenter.Concepts.md#apple-inauqsskizdem)

## Method Types

---

> Registering event classes for logging
> [registerEventClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojswo2ltorsxerlwmvxhiq3mmfzxg)
> [registeredEventClasses](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojswo2ltorsxezleiv3gk3tuinwgc43tmvzq)
> [setRecordsEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rponsxiutfmnxxezdtiv3gk3tuom)
> [recordsEventsForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojswg33smrzuk5tfnz2hgrtpojbwyyltom)
>
> Logging events
> [newEventOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnzsxorlwmvxhit3ginwgc43t)
> [markAtomicEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnvqxe22borxw22ldiv3gk3tu)
> [markStartOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnvqxe22torqxe5cpmzcxmzlooq)
> [markEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnvqxe22fnzse6zsfozsw45a)
> [cancelEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpmnqw4y3fnrcxmzlooq)
>
> Accessing event centers
> [currentCenter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpmn2xe4tfnz2egzloorsxe)
> [allCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpmfwgyq3fnz2gk4tt)
>
> Accessing events
> [allEventsForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpmfwgyrlwmvxhi42gn5zec3dminsw45dfojzq)
> [allEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixwc3dmiv3gk3tuom)
> [eventsOfClassForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpmv3gk3tuonhwmq3mmfzxgrtpojawy3cdmvxhizlsom)
> [eventsOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixwk5tfnz2hgt3ginwgc43t)
> [rootEventsForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojxw65cfozsw45dtizxxeqlmnrbwk3tumvzhg)
> [rootEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixxe33porcxmzloorzq)
> [rootEventsByDuration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojxw65cfozsw45dtij4ui5lsmf2gs33o)
>
> Resetting and suspending event logging
> [resetLoggingForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojsxgzlujrxwoz3jnztum33sifwgyq3fnz2gk4tt)
> [resetLogging](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixxezltmv2ey33hm5uw4zy)
> [suspendLogging](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpon2xg4dfnzsey33hm5uw4zy)
> [resumeLogging](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojsxg5lnmvgg6z3hnfxgo)

## Constructors

---

### EOEventCenter

`public EOEventCenter()`

Description forthcoming.

---

## Static Methods

---

### allCenters

`public static NSArray allCenters()`

Returns all event centers. Typically used only for post-processing of events and statistics gathering. Note that there is one event center per thread.

---

### allEventsForAllCenters

`public static NSArray allEventsForAllCenters()`

Returns an array of all the events logged in all the event centers. The events in the returned array are in no particular order.

__See Also:__ [allEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixwc3dmiv3gk3tuom)

---

### cancelEvent

`public static void cancelEvent(EOEvent event)`

Cancels the recording of an in-progress event. This method doesn't work with atomic events or with events that have already been ended with [markEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnvqxe22fnzse6zsfozsw45a).

Generally you cancel an event when the operation being logged is aborted. For example, the ODBCAdaptorChannel cancels an "Open Channel" event if the __openChannel__ method doesn't successfully open a connection to the database.

---

### currentCenter

`public static EOEventCenter currentCenter()`

Returns the event center for the calling thread.

---

### eventsOfClassForAllCenters

`public static NSArray eventsOfClassForAllCenters( Class aClass, String type)`

Returns an array of all events (from all the event centers) that are instances of _aClass_ and whose type is _type_. Specifying `null` for the class returns events of any class. Similarly, specifying `null` for the type returns events of any type.

__See Also:__ [eventsOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixwk5tfnz2hgt3ginwgc43t)

---

### markAtomicEvent

`public static void markAtomicEvent( EOEvent event, Object info)`

Initializes _event_, a newly allocated event, as an atomic event, and assigns it's info to _info_. The newly allocated event is usually created with the EOEventCenter method [newEventOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnzsxorlwmvxhit3ginwgc43t).

---

### markEndOfEvent

`public static void markEndOfEvent(EOEvent event)`

Marks the time _event_ ended.

---

### markStartOfEvent

`public static void markStartOfEvent( EOEvent event, Object info)`

Marks _event_, a newly allocated event, to be a branch event (that possibly has nested subevents), and assigns it's info to _info_. The newly allocated event is usually created with [newEventOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnzsxorlwmvxhit3ginwgc43t).

There is a limit on the number of events the event logging system logs-200,000 by default. You can change the limit using the user default __EOEventLoggingLimit__. When the logging limit is reached, the logging system attempts to purge old events before logging new ones. If the system is unable to purge old events, event logging is aborted.

The system's attempt to purge events can fail if the event logging limit is too small. This happens because the event system can't purge the first event logged, and it can't purge unclosed branch events.

---

### newEventOfClass

`public static EOEvent newEventOfClass( Class aClass, String aType)`

Creates an event of the desired class and type.

---

### password

`public static String password()`

Description forthcoming.

---

### recordsEventsForClass

`public static boolean recordsEventsForClass(Class eventClass)`

Returns `true` if the application logs events of the _eventClass_ class.

---

### registerEventClass

`public static void registerEventClass( Class aClass, EOEventCenter.EventRecordingHandler handler)`

Registers _aClass_ as an event class. The _handler_ argument is an object that the event logging system notifies when event logging is enabled or disabled for _aClass_.

If the `EOEventLoggingEnabled` user default is set to `true`, this method enables logging for _aClass_. Programmatically, you can selectively enable or disable logging for a specific class with [setRecordsEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rponsxiutfmnxxezdtiv3gk3tuom). It is more common, however, for users to enable and disable logging of a particular class through the WOEventSetup page-for more information, see ["WOEventSetup page" (page 89)](EOEventCenter.Concepts.md#apple-inbeoq2bifbuq).

When the event logging system enables logging for the ODBCAdaptorEvent class, it sends _handler_ a setLoggingEnabled message with `true` as the flag and ODBCAdaptorEvent as the event class. _handler_ is responsible for enabling logging in the instrumented code.

---

### registeredEventClasses

`public static NSArray registeredEventClasses()`

Returns all the event classes registered in the application.

---

### resetLoggingForAllCenters

`public static void resetLoggingForAllCenters()`

Discards all events in all event centers, restarting event collection for the entire application.

__See Also:__ [resetLogging](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixxezltmv2ey33hm5uw4zy)

---

### resumeLogging

`public static void resumeLogging()`

Resumes event logging in all centers. However, logging doesn't actually resume until each invocation of [suspendLogging](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpon2xg4dfnzsey33hm5uw4zy) is paired with an invocation of __resumeLogging__. Invoking __resumeLogging__ without a corresponding __suspendLogging__ isn't harmful.

---

### rootEventsByDuration

`public static NSArray rootEventsByDuration()`

Returns all root events from all event centers, sorted by decreasing duration.

__See Also:__ [rootEventsForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojxw65cfozsw45dtizxxeqlmnrbwk3tumvzhg), [rootEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixxe33porcxmzloorzq)

---

### rootEventsForAllCenters

`public static NSArray rootEventsForAllCenters()`

Returns all events from all event centers that are recorded at the root level; that is, it returns the events that don't have parent events.

__See Also:__ [rootEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuinsw45dfoixxe33porcxmzloorzq)

---

### setPassword

`public static void setPassword(String aString)`

Description forthcoming.

---

### setRecordsEvents

`public static void setRecordsEvents( boolean flag, Class eventClass)`

Sets according to _flag_ whether event centers record events of the _eventClass_ class (and its subclasses). By default, event centers don't record events of any class. You can selectively enable logging for a particular event class with this method. To enable event logging for all event classes, set the user default EOEventLoggingEnabled. Then, you can selectively disable logging for a particular event with this method.

---

### suspendLogging

`public static void suspendLogging()`

Suspends event logging in all event centers. Each invocation of __suspendLogging__ must be paired with an invocation of [resumeLogging](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojsxg5lnmvgg6z3hnfxgo) to resume event logging.

---

## Instance Methods

---

### allEvents

`public NSArray allEvents()`

Returns the receiver's events (in no particular order).

---

### eventsOfClass

`public NSArray eventsOfClass( Class aClass, String type)`

Returns the subset of the receiver's events that are instances of _aClass_ and that have the type _type_. Specifying `null` for the class returns events of any class. Similarly, specifying `null` for the type returns events of any type.

---

### resetLogging

`public void resetLogging()`

Discards all events in the event center for the calling thread.

__See Also:__ [resetLoggingForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojsxgzlujrxwoz3jnztum33sifwgyq3fnz2gk4tt)

---

### rootEvents

`public NSArray rootEvents()`

Returns the receiver's events that were recorded at root level; that is, returns the events that don't have a parent event.

__See Also:__ [rootEventsForAllCenters](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojxw65cfozsw45dtizxxeqlmnrbwk3tumvzhg), [rootEventsByDuration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojxw65cfozsw45dtij4ui5lsmf2gs33o)

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
