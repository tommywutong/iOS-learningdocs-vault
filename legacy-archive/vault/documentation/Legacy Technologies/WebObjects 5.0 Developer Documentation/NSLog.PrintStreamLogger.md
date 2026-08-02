---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSLog.PrintStreamLogger.html
archived_at: '2026-07-15T08:13:56.151855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSLog.PrintStreamLogger

> **__Inherits from:__**
> : [NSLog.Logger](NSLog.Logger.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjzjuy33hfzgg6z3hmvza)

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSLog.PrintStreamLogger is a concrete subclass of NSLog.Logger. It logs output to a java.io.PrintStream which is contained by the logger. This PrintStream can be changed, which causes the receiver to output log messages somewhere else, such as a local file. Methods are provided to enable and disable logging, and to enable and disable verbose logging.

NSLog.out and NSLog.debug are PrintStreamLoggers that point at System.out. NSLog.err is a PrintStreamLogger that points to System.err.

NSLog.PrintStreamLogger looks at the value of the internal variables set by NSLog.Logger.setIsVerbose() and NSLog.Logger.setIsEnabled() to determine whether to produce verbose output and to determine whether to log messages to the logger. See the method descriptions for these methods in the documentation for ["NSLog.Logger" (page 139)](NSLog.Logger.md#apple-ijbesqsei5eec).

## Method Types

---

> **All methods**
>
> : [NSLog.PrintStreamLogger](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsqojuw45ctorzgkylnjrxwoz3foixu4u2mn5ts4udsnfxhiu3uojswc3kmn5twozls): [appendln](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsqojuw45ctorzgkylnjrxwoz3foixwc4dqmvxgi3do): [appendln](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsqojuw45ctorzgkylnjrxwoz3foixwc4dqmvxgi3do): [flush](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsqojuw45ctorzgkylnjrxwoz3foixwm3dvonua): [printStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsqojuw45ctorzgkylnjrxwoz3foixxa4tjnz2fg5dsmvqw2): [setPrintStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsqojuw45ctorzgkylnjrxwoz3foixxgzlukbzgs3tukn2hezlbnu)

## Constructors

---

### NSLog.PrintStreamLogger

`public NSLog.PrintStreamLogger(java.io.PrintStream aPrintStream)`

Creates a new NSLog.PrintStreamLogger which directs output to _aPrintStream_. Throws an IllegalArgumentException if _aPrintStream_ is null.

`public NSLog.PrintStreamLogger()`

Creates a new NSLog.PrintStreamLogger which directs output to System.out.

---

## Instance Methods

---

### appendln

`public void appendln()`

Writes a new line to the receiver's PrintStream.

---

### appendln

`public void appendln(Throwable aThrowable)`

Writes the stack trace of _aThrowable_ to the receiver's PrintStream.

---

### appendln

`public void appendln(Object anObject)`

Writes _anObject_ to the receiver's PrintStream.

---

### flush

`public void flush()`

Flush's the receiver's PrintStream by invoking the PrintStream's __flush__ method.

---

### printStream

`public java.io.PrintStream printStream()`

Returns the receiver's PrintStream.

---

### setPrintStream

`public void setPrintStream(java.io.PrintStream aPrintStream)`

Sets the receiver's print stream to _aPrintStream_. This redirects the receiver's output. For example, to redirect all log messages to the local file /Local/Users/log.txt, use the following code:
> ```
> NSLog.PrintStreamLogger aLogger =
>     new NSLog.PrintStreamLogger(); // Output defaults to System.out
> PrintStream aStream =
>     NSLog.printStreamForPath ("/Local/Users/log.txt"); // New print stream based on path.
> aLogger.setPrintStream (aStream); // Direct output to the custom PrintStream.
> NSLog.setOut(aLogger); // Assign the custom PrintStreamLogger to the declared instances of NSLogger in NSLog
> NSLog.setErr(aLogger);
> NSLog.setDebug(aLogger);
> aLogger.appendln(anObject);
> ```

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
