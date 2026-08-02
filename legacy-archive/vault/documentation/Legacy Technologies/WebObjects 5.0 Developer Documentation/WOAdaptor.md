---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOAdaptor.html
archived_at: '2026-07-15T08:15:14.700011Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOAdaptor

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOAdaptor is an abstract class that represents objects that can receive events from a WebObjects adaptor. A WebObjects adaptor is a process that handles communication between the server and a WebObjects application. The WebObjects application (a WOApplication instance) communicates with the adaptor using messages defined in the WOAdaptor class.

The purpose of the WOAdaptor class is to perform these tasks:

- Register with the application's run loop to begin receiving events.
- Receive incoming events from the run loop and package them as WORequest objects.
- Forward the WORequest to the WOApplication by sending it the message dispatchRequest.
- Receive the WOResponse object from the WOApplication and send it to the client using an RPC mechanism.

## Constants

---

WOAdaptor constants:

|  |  |
| --- | --- |
| __Class Variable__ | __Description__ |
| `DefaultListenQueueSize` | This class constant is an integer that specifies the maximum queue length for the listener thread. WOAdaptor's implementation sets this value to 128. Override this value by changing the WOListenQueueSize property. |

## Method Types

---

> **Constructors**
> : [WOAdaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6v2pifsgc4dun5za)
>
> **Obtaining attributes**
> : [doesBusyRunOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6zdpmvzue5ltpfjhk3spnzrwk): [dispatchesRequestsConcurrently](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6zdjonygc5ddnbsxgutfof2wk43uonbw63tdovzhezloorwhs): [port](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64dpoj2a)
>
> **Event registering**
> : [registerForEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tfm5uxg5dfojdg64sfozsw45dt): [unregisterForEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc65loojswo2ltorsxertpojcxmzloorzq)
>
> **Running**
> : [runOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tvnzhw4y3f)

## Constructors

---

### WOAdaptor

`public WOAdaptor( String aName, NSDictionary someArguments)`

Initializes a WOAdaptor with the name _aName_ and arguments _someArguments_. _aName_ is the name of the WOAdaptor subclass. _someArguments_ are the default options specified for this adaptor (such as port number and listen queue depth).

The WOApplication method __adaptorWithName__ invokes this message when it encounters an __WOAdaptor__ option on the command line. The WOApplication retains each of its WOAdaptors.

__See Also:__ adaptorWithName (WOApplication class)

---

## Instance Methods

---

### dispatchesRequestsConcurrently

`public boolean dispatchesRequestsConcurrently()`

Returns true if the adaptor is multi-threaded, false otherwise. If the adaptor is multi-threaded, the adaptor may dispatch requests to the application concurrently in separate threads.

__See Also:__ adaptorsDispatchRequestsConcurrently (WOApplication class)

---

### doesBusyRunOnce

`public boolean doesBusyRunOnce()`

Returns whether repeatedly invoking [runOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tvnzhw4y3f) would result in busy waiting.

---

### port

`public int port()`

After the application's constructor has been called, __port__ returns the port number on which this adaptor will listen. During execution of the application's constructor, this method returns the value of the WOPort user default (or the value of the -WOPort command-line option, of one was specified when the application was started).

__See Also:__ [port](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64dpoj2a) (WOApplication class)

---

### registerForEvents

`public abstract void registerForEvents()`

Performs any actions necessary to have the WOAdaptor start receiving events. WOAdaptor's implementation does nothing.

---

### runOnce

`public abstract void runOnce()`

Invoked by the application's main loop. WOAdaptor's implementation does nothing.

__See Also:__ [doesBusyRunOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6zdpmvzue5ltpfjhk3spnzrwk)

---

### toString

`public String toString()`

Description forthcoming.

---

### unregisterForEvents

`public abstract void unregisterForEvents()`

Undoes the actions performed in [registerForEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tfm5uxg5dfojdg64sfozsw45dt) so that the WOAdaptor stops receiving events. WOAdaptor's implementation does nothing.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
