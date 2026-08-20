---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSFwdExc.html
archived_at: '2026-07-15T08:13:55.969881Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSForwardException

> **__Inherits from:__**
> : RuntimeException : Exception : Throwable : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSForwardException objects (or forward exceptions) are wrappers for Throwable objects that are not RuntimeExceptions. Since NSForwardException is a subclass of RuntimeException, forward exceptions can be omitted from the `throws` clause of a method even if the original exception had to be declared.

NSForwardException is used internally within WebObjects to keep the API congruent with the WebObjects 4.5 API (which uses the Java Bridge). Apple doesn't anticipate the need for you to create NSForwardException objects. You may need to catch them, however. To access the original exception, use the [originalException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxw64tjm5uw4ylmiv4ggzlqoruw63q) method.

## Method Types

---

> **Constructors**
>
> : [NSForwardException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxu4u2gn5zhoylsmrcxqy3fob2gs33o)
>
> **Accessing the wrapped exception**
>
> : [originalException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxw64tjm5uw4ylmiv4ggzlqoruw63q)
>
> **Methods inherited from Throwable**
>
> : [printStackTrace](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxxa4tjnz2fg5dbmnvvi4tbmnsq): [stackTrace](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxxg5dbmnvvi4tbmnsq): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxxi32torzgs3th)

## Constructors

---

### NSForwardException

`public NSForwardException(Throwable exception)`

`public NSForwardException( Throwable exception, String extraMessage)`

Creates an NSForwardException from _exception_. If _exception_ is already an NSForwardException, the constructor wraps the exception's [originalException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstizxxe53bojsek6ddmvyhi2lpnyxw64tjm5uw4ylmiv4ggzlqoruw63q).

The two-argument constructor allows you to specify an extra message; in this case, the new NSForwardException's message is _exception_'s message with _extraMessage_ appended. See the Throwable class specification in Sun's documentation for more information about an exception's messages.

---

## Instance Methods

---

### originalException

`public Throwable originalException()`

Returns the exception wrapped by the receiver.

---

### printStackTrace

`public void printStackTrace()`

Prints the wrapped exception and its stack trace to the standard error stream. See the class specification for java.lang.Throwable in Sun's Java documentation for more information about the stack trace format.

`public void printStackTrace(java.io.PrintStream printStream)`

Prints the wrapped exception and its stack trace to the specified print stream.

`public void printStackTrace(java.io.PrintWriter printWriter)`

Prints the wrapped exception and its stack trace to the specified print writer.

---

### stackTrace

`public String stackTrace()`

Returns a string containing the wrapped exception and its stack trace.

---

### toString

`public String toString()`

Returns a string representation of the receiver indicating the receiver's class, its wrapped exception's class, and the wrapped exception's error message string.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
