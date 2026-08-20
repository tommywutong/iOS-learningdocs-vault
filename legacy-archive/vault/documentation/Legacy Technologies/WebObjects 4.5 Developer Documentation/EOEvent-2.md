---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOEvent.html
archived_at: '2026-07-15T08:11:39.708447Z'
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

> __Declared in:__ : EOControl/EOEvent.h

---

## Class Description

---

EOEvent is an abstract class that provides
concrete subclasses with a structure for storing information (such
as duration) about a logged event.

Subclasses of EOEvent don't need to override any inherited
methods or implement any methods at all. You can customize the behavior
if you want, but the EOEvent implementations are sufficient for
most cases. Generally, to create a subclass of EOEvent, you merely
declare it and create a description file that defines the events
your subclass logs. The class itself usually declares no instance
variables and implements no methods. The abstract implementation
gets all the information it needs from the description file. For
more information on the description file, see the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y) method description.

Most of the work involved in logging custom events is instrumenting
your code. For more information on that and on the event logging
system itself, see the [EOEventCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOEventCenter.html#CAHBICFD) class specification.

## Constants

---

In EOEvent.h, EOControl defines the `int` type `EOEventSignatureType` which
is the argument type for the methods [signatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bponuwo3tbor2xezkpmzkhs4dfhi), [aggregateEvents:bySignatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6ylhm5zgkz3borsuk5tfnz2hgotcpfjwsz3omf2hk4tfj5tfi6lqmu5a),
and [groupEvents:bySignatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6z3sn52xarlwmvxhi4z2mj4vg2lhnzqxi5lsmvhwmvdzobstu). EOEvent.h also
defines the following enumeration constant as a possible signature type
to be used as the argument to these methods.

- EOBasicEventSignature

Additionally, EOEvent.h defines
the following NSString constant to be used as a key into the dictionary returned
by [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y).
The `EOEventGroupName` entry
provides the description of the family of events represented by
the event class.

- EOEventGroupName

## Method Types

---

> **Defining an event type**
> : [+ eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y)
> : [+ description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zdfonrxe2lqoruw63q)
>
> **Accessing information
> about the event**
> : [- description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmrsxgy3snfyhi2lpny)
> : [- title](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bporuxi3df)
> : [- startDate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpon2gc4tuirqxizi)
> : [- duration](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmr2xeylunfxw4)
> : [- durationWithoutSubevents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmr2xeylunfxw4v3jorug65lukn2wezlwmvxhi4y)
> : [- setType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bponsxivdzobstu)
> : [- type](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpor4xazi)
> : [- setInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bponsxislomzxtu)
> : [- info](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnfxgm3y)
> : [- comment](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmnxw23lfnz2a)
>
> **Grouping and Aggregating
> Events**
> : [+ aggregateEvents:bySignatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6ylhm5zgkz3borsuk5tfnz2hgotcpfjwsz3omf2hk4tfj5tfi6lqmu5a)
> : [+ groupEvents:bySignatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6z3sn52xarlwmvxhi4z2mj4vg2lhnzqxi5lsmvhwmvdzobstu)
> : [- signatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bponuwo3tbor2xezkpmzkhs4dfhi)
>
> **Displaying event information**
> : [- displayComponentName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmruxg4dmmf4ug33nobxw4zloorhgc3lf)
>
> **Traversing the event
> hierarchy**
> : [- parentEvent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpobqxezloorcxmzlooq)
> : [- subevents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpon2wezlwmvxhi4y)
>
> **Logging events**
> : [- markAtomicWithInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnvqxe22borxw22ldk5uxi2cjnztg6oq)
> : [- markEnd](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnvqxe22fnzsa)
> : [- markStartWithInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnvqxe22torqxe5cxnf2gqslomzxtu)

## Class Methods

---

### aggregateEvents:bySignatureOfType:

`+ (NSArray *)aggregateEvents:(NSArray
*)events
bySignatureOfType:(EOEventSignatureType)tag`

Returns an array of aggregated
events. Gets the signature of type _tag_ from
each event in _events_ and aggregates
events with the same signature into a special, single event. The
resulting array has an event for each different signature. The events
in this array have a duration equal to the sum of the durations of
its aggregated events. The [subevents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpon2wezlwmvxhi4y) of
these special events are the union of the subevents of its aggregated
events.

This method is for use by the WOEventDisplay page.
For more information, see ["WOEventDisplay page"](EOEventCenter-3.md#apple-inauqr2eivduo).

---

### description

`+ (NSString *)description`

Returns a description of the
family of events represented by the class. EOEvent's
implementation returns the event description for the [EOEventGroupName](#apple-ineucrseiveem) key.
For more information, see the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y) method description.

---

### eventTypeDescriptions

`+ (NSDictionary *)eventTypeDescriptions`

Returns a dictionary of event
types and descriptions for the family of events represented by the
event class. The keys of this dictionary are event
types and the corresponding values are descriptions of events of
the types. Subclasses don't need to override this method; EOEvent's
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
of EOEvent. It uses EOEvent's implementation of __eventTypeDescriptions__.
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

### groupEvents:bySignatureOfType:

`+ (NSArray *)groupEvents:(NSArray
*)events
bySignatureOfType:(EOEventSignatureType)tag`

Returns an array of grouped
events. Gets the signature of type _tag_ from
each event in _events_ and groups events
with the same signature into a special, single event. The resulting
array has an event for each different signature. The [subevents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpon2wezlwmvxhi4y) of these
special events are the grouped events.

This method is for use
by the WOEventDisplay page. For more information, see ["WOEventDisplay page"](EOEventCenter-3.md#apple-inauqr2eivduo).

---

## Instance Methods

---

### comment

`- (NSString *)comment`

Returns type specific information
about the event. EOEvent's implementation returns
a string representation of the receiver's [info](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnfxgm3y).

---

### description

`- (NSString *)description`

Returns a
description of the receiver. EOEvent's implementation returns
a string that includes the receiver's [title](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bporuxi3df), [comment](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmnxw23lfnz2a), and [duration](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmr2xeylunfxw4) or [startDate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpon2gc4tuirqxizi).

---

### displayComponentName

`- (NSString *)displayComponentName`

Returns the name of a WebObjects
component to use to display the receiver's logging information. EOEvent's
implementation uses the WOEventRow component, which is generally
sufficient for subclasses.

---

### duration

`- (int)duration`

Returns the duration of the
receiver, in milliseconds; returns 0 if the event is atomic (not
a branch event) or if the branch is not yet closed.

---

### durationWithoutSubevents

`- (int)durationWithoutSubevents`

Returns the duration of receiver,
in milliseconds, not including the time spent in its subevents (if
any).

---

### info

`- (id)info`

Returns the
custom info for the receiver.

---

### markAtomicWithInfo:

`- (void)markAtomicWithInfo:(id)info`

Initializes
the receiver, a newly allocated event, as an atomic event that has
an absolute [startDate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpon2gc4tuirqxizi) (and not
a [duration](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmr2xeylunfxw4)), and assigns
the event's [info](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnfxgm3y).
The newly allocated event is usually created with the EOEventCenter
method [newEventOfClass:eventType:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOEventCenter.html#//apple_ref/occ/clm/EOEventCenter/newEventOfClass:eventType:).

|  |
| --- |
| __Note:__ Don't invoke this method directly. Use the corresponding function defined in EOEventCenter.h instead. |

---

### markEnd

`- (void)markEnd`

Marks the end of a branch event,
which has the side-effect of setting the [duration](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpmr2xeylunfxw4).

|  |
| --- |
| __Note:__ Don't invoke this method directly. Use the corresponding function defined in EOEventCenter.h instead. |

---

### markStartWithInfo:

`- (void)markStartWithInfo:(id)info`

Initializes the receiver, a
newly allocated event, to be a branch event (that possibly has nested subevents),
and assigns it's [info](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpnfxgm3y) to _info_. The
newly allocated event is usually created with the EOEventCenter
method [newEventOfClass:eventType:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOEventCenter.html#//apple_ref/occ/clm/EOEventCenter/newEventOfClass:eventType:).

|  |
| --- |
| __Note:__ Don't invoke this method directly. Use the corresponding function defined in EOEventCenter.h instead. |

---

### parentEvent

`- (EOEvent *)parentEvent`

Returns the
parent event, if any, or nil otherwise. Events logged at the root
level do not have a parent. Other events return the event that was
open at the time that they were started.

---

### setInfo:

`- (void)setInfo:(id)info`

Sets the custom event information
for the receiver. This information is used to
display event logging information in the WOEventDisplay page. The _info_ argument
can be any kind of object that responds to __isEqual:__, __description__, __retain__,
and __release__.

---

### setType:

`- (void)setType:(NSString
*)type`

Sets the receiver's type
to _type_. EOEvent's implementation
gets the set of available types from a description file. For more
information, see the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y) method
description.

---

### signatureOfType:

`- (id)signatureOfType:(EOEventSignatureType)tag`

Returns the requested receiver's
signature, which can be used to group and aggregate the receiver
with other events that have the same signature. EOEvent
defines one signature type, [EOBasicEventSignature](#apple-ineucsceifcee), which
has the corresponding signature of the form "title - comment".
If the specified type is unknown, EOEvent's implementation returns nil otherwise.

__See
Also:__  [+ aggregateEvents:bySignatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6ylhm5zgkz3borsuk5tfnz2hgotcpfjwsz3omf2hk4tfj5tfi6lqmu5a), [+ groupEvents:bySignatureOfType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6z3sn52xarlwmvxhi4z2mj4vg2lhnzqxi5lsmvhwmvdzobstu)

---

### startDate

`- (NSCalendarDate *)startDate`

Returns the
date at which the receiver was logged. For a non-atomic event, the
return value is the time at which the event logging began, not when
it ended.

---

### subevents

`- (NSArray *)subevents`

Returns the
receiver's immediate subevents; that is, the events that were
logged with this event as their parent.

---

### title

`- (NSString *)title`

Returns the event type description
corresponding with the receiver's [type](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fozsw45bpor4xazi). The title
is used by the WOEventDisplay. EOEvent's implementation returns
the value from the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y) dictionary
for the receiver's type. If there isn't an entry in the __eventTypeDescriptions__ dictionary
for the receiver's type, EOEvent's implementation returns the
name of the receiver's class.

---

### type

`- (NSString *)type`

Returns the receiver's type. Using
the event type definition scheme implemented by EOEvent, the types are
defined in a description file as described in the [eventTypeDescriptions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuk5tfnz2c6zlwmvxhivdzobsuizltmnzgs4dunfxw44y) method
description.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
