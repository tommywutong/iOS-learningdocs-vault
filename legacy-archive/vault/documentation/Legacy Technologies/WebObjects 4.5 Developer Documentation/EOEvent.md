---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOEvent.html
archived_at: '2026-07-15T08:11:37.546856Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEvent

> **__Inherits
> from:__**
> : NSObject

> **__Package:__**
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOEvent is an abstract class that provides
concrete subclasses with a structure for storing information (such
as duration) about a logged event.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eocontrol package. The event logging system is not available for Java Client. In a Java Client application, you can view event logging information for the server side of the application, but not on the client side. |

Subclasses of EOEvent don't need to override any inherited
methods or implement any methods at all. You can customize the behavior
if you want, but the EOEvent implementations are sufficient for
most cases. Generally, to create a subclass of EOEvent, you merely
declare it and create a description file that defines the events
your subclass logs. The class itself usually declares no instance
variables and implements no methods. The abstract implementation
gets all the information it needs from the description file. For
more information on the description file, see the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt) method description.

Most of the work involved in logging custom events is instrumenting
your code. For more information on that and on the event logging
system itself, see the [EOEventCenter](EOEventCenter.md#apple-inauqqsjindei) class specification.

## Constants

---

EOAttribute defines the following `int` constant
as a possible signature type for use with the methods [signatureOfType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zwsz3omf2hk4tfj5tfi6lqmu), [aggregateEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3bm5txezlhmf2gkrlwmvxhi4y),
and [groupEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3hojxxk4cfozsw45dt).

- EOBasicEventSignature

Additionally, EOEvent defines the following String
constant to be used as a key into the dictionary returned by [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt).
The `EOEventGroupName` entry
provides the description of the family of events represented by
the event class.

- EOEventGroupName

## Method Types

---

> **Defining an event type**
> : [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt)
> : [description](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3emvzwg4tjob2gs33o)
>
> **Accessing information
> about the event**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf52g6u3uojuw4zy)
> : [title](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf52gs5dmmu)
> : [startDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zxiylsorcgc5df)
> : [duration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5shk4tboruw63q)
> : [durationWithoutSubevents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5shk4tboruw63sxnf2gq33vorjxkytfozsw45dt)
> : [setType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zwk5cupfygk)
> : [type](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf52hs4df)
> : [setInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zwk5cjnztg6)
> : [info](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5uw4ztp)
> : [comment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5rw63lnmvxhi)
>
> **Grouping and Aggregating
> Events**
> : [aggregateEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3bm5txezlhmf2gkrlwmvxhi4y)
> : [groupEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3hojxxk4cfozsw45dt)
> : [signatureOfType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zwsz3omf2hk4tfj5tfi6lqmu)
>
> **Displaying event information**
> : [displayComponentName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5sgs43qnrqxsq3pnvyg63tfnz2e4ylnmu)
>
> **Traversing the event
> hierarchy**
> : [parentEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5ygc4tfnz2ek5tfnz2a)
> : [subevents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zxkytfozsw45dt)
>
> **Logging events**
> : [markAtomicWithInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5wwc4tlif2g63ljmnlws5dijfxgm3y)
> : [markEnd](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5wwc4tlivxgi)
> : [markStartWithInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5wwc4tlkn2gc4tuk5uxi2cjnztg6)

## Static Methods

---

### aggregateEvents

`public static NSArray aggregateEvents(
NSArray events,
int tag)`

Returns an array of aggregated
events. Gets the signature of type _tag_ from
each event in _events_ and aggregates
events with the same signature into a special, single event. The
resulting array has an event for each different signature. The events
in this array have a duration equal to the sum of the durations of
its aggregated events. The [subevents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zxkytfozsw45dt) of
these special events are the union of the subevents of its aggregated
events.

This method is for use by the WOEventDisplay page.
For more information, see ["WOEventDisplay page"](EOEventCenter-2.md#apple-inauqr2eivduo).

---

### description

`public static String description()`

Returns a description of the
family of events represented by the class. EOEvent's
implementation returns the event description for the [EOEventGroupName](#apple-ineucrseiveem) key.
For more information, see the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt) method description.

---

### eventTypeDescriptions

`public static NSDictionary eventTypeDescriptions()`

Returns a dictionary of event
types and descriptions for the family of events represented by the
event class. The keys of this dictionary are event
types and the corresponding values are descriptions of events of
the types. Subclasses don't need to implement this method; EOEvent's
implementation is generally sufficient for subclasses.

EOEvent's
implementation reads the event types and their descriptions from
a file. To define the types your event class represents, create
a description file for your event and add it to your project's Resources
folder. An event's description file defines the event __categories__ and __subcategories__ used
in the WOEventDisplay page. The file's contents is a dictionary
in plist format.

For example, consider the ODBCAdaptorEvent
that logs events for the ODBC adaptor. ODBCAdaptorEvent is a subclass
of EOEvent. It uses EOEvent's implementation of `eventTypeDescriptions`.
The name of its description file is ODBCAdaptorEvent.description,
and it looks like this:

> ```
> {
>     EOEventGroupName = "ODBC Adaptor Event";
>     connect = "Connect";
>     openChannel = "Open Channel";
>     evaluateExpression = "Evaluate Expression";
>     fetchRow = "Fetch Row";
>     commitTransaction = "Commit Transaction";
> }
> ```

Using the EOEvent
implementation, the [EOEventGroupName](#apple-ineucrseiveem) entry
is mandatory; it describes the family of events logged by the event
class. Any other keys are defined by the event class itself. In
the ODBCAdaptorEvent class, the other keys (`connect`, `openChannel`,
and so on) are the __types__ of the events ODBCAdaptorEvent
logs.

If the file doesn't exist or if there's an
error reading the file, EOEvent creates a dictionary with a single entry;
the entry's key is `EOEventGroupName` and
the value is the name of the event class (such as ODBCAdaptorEvent).

---

### groupEvents

`public static NSArray groupEvents(
NSArray events,
int tag)`

Returns an array of grouped
events. Gets the signature of type _tag_ from
each event in _events_ and groups events
with the same signature into a special, single event. The resulting
array has an event for each different signature. The [subevents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zxkytfozsw45dt) of these
special events are the grouped events.

This method is for use
by the WOEventDisplay page. For more information, see ["WOEventDisplay page"](EOEventCenter-2.md#apple-inauqr2eivduo).

---

## Instance Methods

---

### comment

`public String comment()`

Returns type specific information
about the event. EOEvent's implementation returns
a string representation of the receiver's [info](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5uw4ztp).

---

### displayComponentName

`public String displayComponentName()`

Returns the name of a WebObjects
component to use to display the receiver's logging information. EOEvent's
implementation uses the WOEventRow component, which is generally
sufficient for subclasses.

---

### duration

`public int duration()`

Returns the duration of the
receiver, in milliseconds; returns 0 if the event is atomic (not
a branch event) or if the branch is not yet closed.

---

### durationWithoutSubevents

`public int durationWithoutSubevents()`

Returns the duration of receiver,
in milliseconds, not including the time spent in its subevents (if
any).

---

### info

`public Object info()`

Returns the
custom info for the receiver.

---

### markAtomicWithInfo

`public void markAtomicWithInfo(Object info)`

Initializes
the receiver, a newly allocated event, as an atomic event that has
an absolute [startDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zxiylsorcgc5df) (and not
a [duration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5shk4tboruw63q)), and assigns
the event's [info](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5uw4ztp).
The newly allocated event is usually created with the EOEventCenter
method [newEventOfClass](EOEventCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnzsxorlwmvxhit3ginwgc43t).

|  |
| --- |
| __Note:__ Don't invoke this method directly. Use the corresponding method defined in EOEventCenter instead. |

---

### markEnd

`public void markEnd()`

Marks the end of a branch event,
which has the side-effect of setting the [duration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5shk4tboruw63q).

|  |
| --- |
| __Note:__ Don't invoke this method directly. Use the corresponding method defined in EOEventCenter instead. |

---

### markStartWithInfo

`public void markStartWithInfo(Object info)`

Initializes the receiver, a
newly allocated event, to be a branch event (that possibly has nested subevents),
and assigns it's [info](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5uw4ztp) to _info._ The
newly allocated event is usually created with the EOEventCenter
method [newEventOfClass](EOEventCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpnzsxorlwmvxhit3ginwgc43t).

|  |
| --- |
| __Note:__ Don't invoke this method directly. Use the corresponding method defined in EOEventCenter instead. |

---

### parentEvent

`public EOEvent parentEvent()`

Returns the
parent event, if any, or null otherwise. Events logged at the root
level do not have a parent. Other events return the event that was
open at the time that they were started.

---

### setInfo

`public void setInfo(Object info)`

Sets the custom event information
for the receiver. This information is used to
display event logging information in the WOEventDisplay page. The _info_ argument
can be any kind of object that responds to `equals` and `toString`.

---

### setType

`public void setType(String type)`

Sets the receiver's type
to _type._ EOEvent's implementation
gets the set of available types from a description file. For more
information, see the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt) method
description.

---

### signatureOfType

`public Object signatureOfType(int tag)`

Returns the requested receiver's
signature, which can be used to group and aggregate the receiver
with other events that have the same signature. EOEvent
defines one signature type, [EOBasicEventSignature](#apple-ineucsceifcee), which
has the corresponding signature of the form "title - comment".
If the specified type is unknown, EOEvent's implementation returns null otherwise.

__See
Also:__  [aggregateEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3bm5txezlhmf2gkrlwmvxhi4y), [groupEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3hojxxk4cfozsw45dt)

---

### startDate

`public NSGregorianDate startDate()`

Returns the
date at which the receiver was logged. For a non-atomic event, the
return value is the time at which the event logging began, not when
it ended.

---

### subevents

`public NSArray subevents()`

Returns the
receiver's immediate subevents; that is, the events that were
logged with this event as their parent.

---

### title

`public String title()`

Returns the event type description
corresponding with the receiver's [type](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf52hs4df). The title
is used by the WOEventDisplay. EOEvent's implementation returns
the value from the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt) dictionary
for the receiver's type. If there isn't an entry in the `eventTypeDescriptions` dictionary
for the receiver's type, EOEvent's implementation returns the
name of the receiver's class.

---

### `toString`

`public String toString()`

Returns a
description of the receiver. EOEvent's implementation returns
a string that includes the receiver's [title](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf52gs5dmmu), [comment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5rw63lnmvxhi), and [duration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5shk4tboruw63q) or [startDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiv3gk3tuf5zxiylsorcgc5df).

---

### type

`public String type()`

Returns the receiver's type. Using
the event type definition scheme implemented by EOEvent, the types are
defined in a description file as described in the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhil3fozsw45cupfygkrdfonrxe2lqoruw63tt) method
description.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
