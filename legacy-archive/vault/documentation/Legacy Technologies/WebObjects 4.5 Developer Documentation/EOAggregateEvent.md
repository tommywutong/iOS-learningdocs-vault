---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOAggregateEvent.html
archived_at: '2026-07-15T08:11:37.029822Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOAggregateEvent

> **__Inherits
> from:__**
> : [EOEvent](EOEvent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuk5tfnz2a) : NSObject

> **__Package:__**
> : com.apple.yellow.eocontrol

---

## Class Description

---

An instance of the EOAggregateEvent class
is used to aggregate into one event multiple EOEvent objects that
have the same aggregate signature. This one aggregate event is typically
used in a WOEventDisplay page in a WebObjects application to display
the sum of all of the aggregated events' durations.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eocontrol package. The event logging system is not available for Java Client. In a Java Client application, you can view event logging information for the server side of the application, but not on the client side. |

## Instance Methods

---

### addEvent

`public void addEvent(EOEvent event)`

Adds _event_ to
the set of events that the receiver aggregates.

---

### events

`public NSArray events()`

Returns the set of events that
the receiver aggregates. In the typical scenario, an EOAggregateEvent always
has at least one event-the event for which the
event logging system created the aggregate event.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
