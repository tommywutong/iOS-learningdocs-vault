---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOAdaptor.html
archived_at: '2026-07-15T08:11:47.310530Z'
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

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOAdaptor.h

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
  message [dispatchRequest:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgs43qmf2gg2csmvyxkzltoq5a).
- Receive the WOResponse object from the WOApplication and send
  it to the client using an RPC mechanism.

## Method Types

---

> **Creation**
> : [- initWithName:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixws3tjorlws5dijzqw2zj2mfzgo5lnmvxhi4z2)
>
> **Obtaining attributes**
> : [- doesBusyRunOnce](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixwi33fonbhk43zkj2w4t3omnsq)
> : [- dispatchesRequestsConcurrently](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixwi2ltobqxiy3imvzvezlrovsxg5dtinxw4y3vojzgk3tunr4q)
> : [- port](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxa33soq)
>
> **Event registering**
> : [- registerForEvents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxezlhnfzxizlsizxxerlwmvxhi4y)
> : [- unregisterForEvents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxk3tsmvtws43umvzem33siv3gk3tuom)
>
> **Running**
> : [- runOnce](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxe5loj5xggzi)

## Instance Methods

---

### dispatchesRequestsConcurrently

`- (BOOL)dispatchesRequestsConcurrently`

Returns YES if the adaptor is multi-threaded, NO otherwise.
If the adaptor is multi-threaded, the adaptor may dispatch requests
to the application concurrently in separate threads.

__See
Also:__  [- adaptorsDispatchRequestsConcurrently](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwiylqorxxe42enfzxaylumnufezlrovsxg5dtinxw4y3vojzgk3tunr4q) ( [WOApplication class](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4))

---

### doesBusyRunOnce

`- (BOOL)doesBusyRunOnce`

Returns whether repeatedly invoking [runOnce](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxe5loj5xggzi) would result
in busy waiting.

---

### initWithName:arguments:

`- (id)initWithName:(NSString
*)aName
arguments:(NSDictionary *)someArguments`

Initializes a WOAdaptor with the name _aName_ and
arguments _someArguments_. _aName_ is
the name of the WOAdaptor subclass. _someArguments_ are
the default options specified for this adaptor (such as port number
and listen queue depth).

The WOApplication method __adaptorWithName:arguments:__ invokes
this message when it encounters an __WOAdaptor__ option
on the command line. The WOApplication retains each of its WOAdaptors.

__See
Also:__  [- adaptorWithName:arguments:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwiylqorxxev3jorue4ylnmu5gc4thovwwk3tuom5a) ( [WOApplication class](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4))

---

### port

`- (int)port`

After the application's constructor
has been called, __port__ returns the port
number on which this adaptor will listen. During execution of the
application's constructor, this method returns the value of the WOPort
user default (or the value of the -WOPort command-line option, of
one was specified when the application was started).

__See
Also:__  [+ port](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3qn5zhi) ( [WOApplication class](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4))

---

### registerForEvents

`- (void)registerForEvents`

Performs any actions necessary to have the WOAdaptor
start receiving events.

__See Also:__  [- runLoop](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zhk3smn5xxa) ( [WOApplication class](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4))

---

### runOnce

`- (void)runOnce`

Invoked by the application's main loop

__See
Also:__  [- doesBusyRunOnce](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixwi33fonbhk43zkj2w4t3omnsq)

---

### unregisterForEvents

`- (void)unregisterForEvents`

Undoes the actions performed in [registerForEvents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxezlhnfzxizlsizxxerlwmvxhi4y) so
that the WOAdaptor stops receiving events.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
