---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOAdaptor.html
archived_at: '2026-07-15T08:11:46.646970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOAdaptor

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

WOAdaptor is an abstract class that represents objects that
can receive events from a WebObjects adaptor. A WebObjects adaptor
is a process that handles communication between the server and a WebObjects
application. The WebObjects application (a WOApplication instance)
communicates with the adaptor using messages defined in the WOAdaptor
class.

The purpose of the WOAdaptor class is to perform these tasks:

- Register with the application's run loop to
  begin receiving events.
- Receive incoming events from the run loop and package them
  as WORequest objects.
- Forward the WORequest to the WOApplication by sending it the
  message [dispatchRequest](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwi2ltobqxiy3ikjsxc5lfon2a).
- Receive the WOResponse object from the WOApplication and send
  it to the client using an RPC mechanism.

## Method Types

---

> **Constructors**
> : [WOAdaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6v2pifsgc4dun5za)
>
> **Obtaining attributes**
> : [doesBusyRunOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6zdpmvzue5ltpfjhk3spnzrwk)
> : [dispatchesRequestsConcurrently](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6zdjonygc5ddnbsxgutfof2wk43uonbw63tdovzhezloorwhs)
> : [port](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64dpoj2a)
>
> **Event registering**
> : [registerForEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tfm5uxg5dfojdg64sfozsw45dt)
> : [unregisterForEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc65loojswo2ltorsxertpojcxmzloorzq)
>
> **Running**
> : [runOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tvnzhw4y3f)

## Constructors

---

### WOAdaptor

`public WOAdaptor(
String aName,
NSDictionary someArguments)`

Initializes a WOAdaptor with the name _aName_ and
arguments _someArguments_. _aName_ is
the name of the WOAdaptor subclass. _someArguments_ are
the default options specified for this adaptor (such as port number
and listen queue depth).

The WOApplication method __adaptorWithName__ invokes
this message when it encounters an __WOAdaptor__ option
on the command line. The WOApplication retains each of its WOAdaptors.

__See
Also:__  [adaptorWithName](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64sxnf2gqttbnvsq) ( [WOApplication class](WOApplication.md#apple-k5huc4dqnruwgylunfxw4))

---

## Instance Methods

---

### dispatchesRequestsConcurrently

`public boolean dispatchesRequestsConcurrently()`

Returns true if the adaptor is multi-threaded, false otherwise.
If the adaptor is multi-threaded, the adaptor may dispatch requests
to the application concurrently in separate threads.

__See
Also:__  [adaptorsDispatchRequestsConcurrently](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64ttiruxg4dborrwqutfof2wk43uonbw63tdovzhezloorwhs) ( [WOApplication class](WOApplication.md#apple-k5huc4dqnruwgylunfxw4))

---

### doesBusyRunOnce

`public boolean doesBusyRunOnce()`

Returns whether repeatedly invoking [runOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tvnzhw4y3f) would result
in busy waiting.

---

### port

`public int port()`

After the application's constructor
has been called, __port__ returns the port
number on which this adaptor will listen. During execution of the
application's constructor, this method returns the value of the WOPort
user default (or the value of the -WOPort command-line option, of
one was specified when the application was started).

__See
Also:__  [port](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qlqobwgsy3boruw63rpobxxe5a) ( [WOApplication class](WOApplication.md#apple-k5huc4dqnruwgylunfxw4))

---

### registerForEvents

`public void registerForEvents()`

Performs any actions necessary to have the WOAdaptor
start receiving events.

__See Also:__  [runLoop](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxe5lojrxw64a) ( [WOApplication class](WOApplication.md#apple-k5huc4dqnruwgylunfxw4))

---

### runOnce

`public void runOnce()`

Invoked by the application's main loop

__See
Also:__  [doesBusyRunOnce](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc6zdpmvzue5ltpfjhk3spnzrwk)

---

### unregisterForEvents

`public void unregisterForEvents()`

Undoes the actions performed in [registerForEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifsgc4dun5zc64tfm5uxg5dfojdg64sfozsw45dt) so
that the WOAdaptor stops receiving events.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
