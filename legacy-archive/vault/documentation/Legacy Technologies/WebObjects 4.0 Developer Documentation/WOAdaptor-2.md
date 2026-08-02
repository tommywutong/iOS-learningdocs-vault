---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOAdaptor.html
archived_at: '2026-07-18T01:28:53.119894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20WebObjects%20Framework-2.md)
[!](WOApplication-2.md)

---

# WOAdaptor

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOAdaptor.h

---

## Class Description

WOAdaptor is an abstract class that represents objects that can receive events from a WebObjects adaptor. A WebObjects adaptor is a process that handles communication between the server and a WebObjects application. The WebObjects application (a WOApplication instance) communicates with the adaptor using messages defined in the WOAdaptor class.

The purpose of the WOAdaptor class is to perform these tasks:

- Register with the application's run loop to begin receiving events.
- Receive incoming events from the run loop and package them as WORequest objects.
- Forward the WORequest to the WOApplication by sending it the message [__dispatchRequest:__](WOApplication-2.md#apple-g43tini).
- Receive the WOResponse object from the WOApplication and send it to the client using an RPC mechanism.

---

## Method Types

**Creation**

**[- initWithName:arguments:](#apple-gy4tmoa)**

**Obtaining attributes**

**[- doesBusyRunOnce](#apple-gqzdmna)

**[- dispatchesRequestsConcurrently](#apple-gizdcni)****

**Event registering**

**[- registerForEvents](#apple-gu2daoa)

**[- unregisterForEvents](#apple-gyyq)****

**Running**

**[- runOnce](#apple-giytsoi)**

---

## Instance Methods

---

### doesBusyRunOnce

- (BOOL)__doesBusyRunOnce__

Returns whether repeatedly invoking [__runOnce__](#apple-giytsoi) would result in busy waiting.

---

### dispatchesRequestsConcurrently

- (BOOL)`dispatchesRequestsConcurrently`

Returns YES if the adaptor is multi-threaded, NO otherwise. If the adaptor is multi-threaded, the adaptor may dispatch requests to the application concurrently in separate threads.

__See also:__
[- __adaptorsDispatchRequestsConcurrently__](WOApplication-2.md#apple-g43dqni) (WOApplication)

---

### initWithName:arguments:

- (id)`initWithName:`(NSString \*)_aName_ `arguments:`(NSDictionary \*)_someArguments_

Initializes a WOAdaptor with the name _aName_ and arguments _someArguments_. _aName_ is the name of the WOAdaptor subclass. _someArguments_ are the default options specified for this adaptor (such as port number and listen queue depth).

The WOApplication method __adaptorWithName:arguments:__  invokes this message when it encounters an __WOAdaptor__ option on the command line. The WOApplication retains each of its WOAdaptors.

__See also:__
[- __adaptorWithName:arguments:__](WOApplication-2.md#apple-g43doma) (WOApplication)

---

### registerForEvents

- (void)`registerForEvents`

Performs any actions necessary to have the WOAdaptor start receiving events.

__See also:__
[- __runLoop__](WOApplication-2.md#apple-ge3tcobw) in WOApplication

---

### runOnce

- (void)__runOnce__

Invoked by the application's main loop

__See also:__
[- __doesBusyRunOnce__](#apple-gqzdmna)

---

### unregisterForEvents

- (void)`unregisterForEvents`

Undoes the actions performed in [__registerForEvents__](#apple-gu2daoa) so that the WOAdaptor stops receiving events.

****

---

[!](The%20WebObjects%20Framework-2.md)
[!](WOApplication-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
