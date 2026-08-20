---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOAggregateEvent.html
archived_at: '2026-07-15T08:13:45.645504Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

# EOAggregateEvent

> **__Inherits from:__**
> : [EOEvent](EOEvent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuk5tfnz2a)

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

An instance of the EOAggregateEvent class is used to aggregate into one event multiple EOEvent objects that have the same aggregate signature. This one aggregate event is typically used in a WOEventDisplay page in a WebObjects application to display the sum of all of the aggregated events' durations.

## Instance Methods

---

### addEvent

`public void addEvent(EOEvent event)`

Adds _event_ to the set of events that the receiver aggregates.

---

### comment

`public String comment()`

Description forthcoming.

---

### description

`public String description()`

Description forthcoming.

---

### displayComponentName

`public String displayComponentName()`

Description forthcoming.

---

### duration

`public long duration()`

Description forthcoming.

---

### durationWithoutSubevents

`public long durationWithoutSubevents()`

Description forthcoming.

---

### events

`public NSArray events()`

Returns the set of events that the receiver aggregates. In the typical scenario, an EOAggregateEvent always has at least one event-the event for which the event logging system created the aggregate event.

---

## Instance Methods

---

### addEvent

`public void addEvent(EOEvent anEOEvent)`

Description forthcoming.

---

### comment

`public String comment()`

Description forthcoming.

---

### description

`public String description()`

Description forthcoming.

---

### displayComponentName

`public String displayComponentName()`

Description forthcoming.

---

### duration

`public long duration()`

Description forthcoming.

---

### durationWithoutSubevents

`public long durationWithoutSubevents()`

Description forthcoming.

---

### events

`public NSArray events()`

Description forthcoming.

---

### info

`public Object info()`

Description forthcoming.

---

### signatureOfType

`public String signatureOfType(int anInt)`

Description forthcoming.

---

### subevents

`public NSArray subevents()`

Description forthcoming.

---

### title

`public String title()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
