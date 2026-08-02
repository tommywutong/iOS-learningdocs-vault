---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOAdaptor.html
archived_at: '2026-07-18T01:28:50.789658Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20WebObjects%20Framework.md)
[!](WOApplication.md)

---

# WOAdaptor

__Inherits From:__
 NSObject

__Inherits From:__
 com.apple.yellow.webobjects

---

## Class Description

WOAdaptor is an abstract class that represents objects that can receive
events from a WebObjects adaptor. A WebObjects adaptor is a process that
handles communication between the server and a WebObjects application. The
WebObjects application (a WOApplication instance) communicates with the adaptor
using messages defined in the WOAdaptor class.

The purpose of the WOAdaptor
class is to perform these tasks:

- Register with the application's
  run loop to begin receiving events.
- Receive incoming events from the run
  loop and package them as WORequest objects.
- Forward the WORequest to the
  WOApplication by sending it the message [`dispatchRequest`](WOApplication.md#apple-g43tini).
- Receive
  the WOResponse object from the WOApplication and send it to the client using an
  RPC mechanism.

---

## Method Types

**Constructors**

**[WOAdaptor](#apple-g4ydkny)**

**Obtaining attributes**

**[doesBusyRunOnce](#apple-gqzdmna)

**[dispatchesRequestsConcurrently](#apple-gizdcni)****

**Event
registering**

**[registerForEvents](#apple-gu2daoa)

**[unregisterForEvents](#apple-gyyq)****

**Running**

**[runOnce](#apple-giytsoi)**

---

## Constructors

---

### WOAdaptor

public
`WOAdaptor`(java.lang.String _aName_, NSDictionary
_someArguments_)

Initializes a WOAdaptor with the name _aName_
and arguments _someArguments_. _aName_ is the name of the
WOAdaptor subclass. _someArguments_ are the default options specified
for this adaptor (such as port number and listen queue depth).

The
WOApplication method `adaptorWithName:arguments:` invokes this
message when it encounters an `WOAdaptor` option on the command
line. The WOApplication retains each of its WOAdaptors.

__See also:__
[`adaptorWithName`](WOApplication.md#apple-g43doma)
(WOApplication)

---

## Instance Methods

---

### doesBusyRunOnce

public boolean `doesBusyRunOnce`()

Returns whether repeatedly
invoking [`runOnce`](#apple-giytsoi) would result in
busy waiting.

---

### dispatchesRequestsConcurrently

public boolean `dispatchesRequestsConcurrently`()

Returns
true if the adaptor is multi-threaded, false otherwise. If the adaptor is
multi-threaded, the adaptor may dispatch requests to the application
concurrently in separate threads.

__See also:__  [`adaptorsDispatchRequestsConcurrently`](WOApplication.md#apple-g43dqni)
(WOApplication)

---

### registerForEvents

public void `registerForEvents`()

Performs any actions
necessary to have the WOAdaptor start receiving events.

__See also:__  [`runLoop`](WOApplication.md#apple-ge3tcobw) in WOApplication

---

### runOnce

public void `runOnce`()

Invoked by the application's main
loop

__See also:__  [`doesBusyRunOnce`](#apple-gqzdmna)

---

### unregisterForEvents

public void `unregisterForEvents`()

Undoes the actions
performed in [`registerForEvents`](#apple-gu2daoa)
so that the WOAdaptor stops receiving events.

****

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html) [[Prev]](../IntroWebObjects.frame.md) [[Next]](WOApplication.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
