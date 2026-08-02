---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSDelayedCBCenter.html
archived_at: '2026-07-15T08:13:55.910488Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSDelayedCallbackCenter

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSDelayedCallbackCenter object (also called a delayed callback center) provides a way to guarantee that particular methods are invoked after an event has ended. You can register selectors with the delayed callback center. The center, in turn, invokes them when the event ends. In WebObjects, this happens at then end of the current WebObjects request-response cycle.

When you register a selector, you also specify a priority, which determines the order in which it is invoked relative to the other selectors. The selectors are invoked in order of ascending priority. To register a selector with the delayed callback center, use [performSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirswyylzmvsegylmnrrgcy3linsw45dfoixxazlsmzxxe3ktmvwgky3un5za). To cancel it before the event ends, use [cancelPerformSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirswyylzmvsegylmnrrgcy3linsw45dfoixwgylomnswyudfojtg64tnknswyzldorxxe).

The event loop invokes [eventEnded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirswyylzmvsegylmnrrgcy3linsw45dfoixwk5tfnz2ek3temvsa) to indicate that the current event has ended. The __eventEnded__ method invokes the queued selectors.

Each task has a default delayed callback center that you access with the [defaultCenter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgrdfnrqxszleinqwy3dcmfrwwq3fnz2gk4rpmrswmylvnr2egzloorsxe) static method.

## Method Types

---

> **Accessing the default center**
>
> : [defaultCenter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgrdfnrqxszleinqwy3dcmfrwwq3fnz2gk4rpmrswmylvnr2egzloorsxe)
>
> **Managing selectors**
>
> : [cancelPerformSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirswyylzmvsegylmnrrgcy3linsw45dfoixwgylomnswyudfojtg64tnknswyzldorxxe): [performSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirswyylzmvsegylmnrrgcy3linsw45dfoixxazlsmzxxe3ktmvwgky3un5za)
>
> **Indicating the end of an event**
>
> : [eventEnded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirswyylzmvsegylmnrrgcy3linsw45dfoixwk5tfnz2ek3temvsa)

## Static Methods

---

### defaultCenter

`public static NSDelayedCallbackCenter defaultCenter()`

Returns the current task's delayed callback center.

---

## Instance Methods

---

### cancelPerformSelector

`public void cancelPerformSelector( NSSelector selector, Object target, Object argument)`

Removes the specified selector with the specified target object and argument from the list of registered selectors.

---

### eventEnded

`public void eventEnded()`

Invokes the registered selectors in order of ascending priority. The event loop should invoke this method when the current event ends.

---

### performSelector

`public void performSelector( NSSelector selector, Object target, Object argument, int priority)`

Registers _selector_ to be invoked on _target_ with the specified argument and priority. When the current event ends, the registered selectors are invoked in order of ascending priority.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
