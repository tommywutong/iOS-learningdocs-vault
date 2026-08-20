---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSLog.Logger.html
archived_at: '2026-07-15T08:13:56.133503Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSLog.Logger

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSLog.Logger is an abstract class that specifies the core functionality for NSLog.

You can subclass NSLog.Logger to add custom logging implementations based on Email, java.io.PrintWriters, display to a Swing window, etc. To add custom logging implementations based on java.io.PrintStream, subclass NSLog.PrintStreamLogger. If you subclass NSLog.Logger, you need only implement two of the __appendln__ methods: __appendln(Object)__, since the other __appendln__ methods invoke __appendln(Object)__; and __appendln()__. You must also implement __flush()__ if you subclass.

See the class specification on ["NSLog" (page 125)](NSLog.md#apple-inauuqsgi5fes) and ["NSLog.PrintStreamLogger" (page 145)](NSLog.PrintStreamLogger.md#apple-ijbesschijdes) for more information.

## Method Types

---

> **Appending to output**
>
> : [appendln](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5qxa4dfnzsgy3q)
>
> **Maintaining logging options**
>
> : [isEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5uxgrlomfrgyzle): [isVerbose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5uxgvtfojrg643f): [setIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5zwk5cjoncw4ylcnrswi): [setIsVerbose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5zwk5cjonlgk4tcn5zwk)
>
> **Flushing the log**
>
> : [flush](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5tgy5ltna)

## Constructors

---

### NSLog.Logger

`public NSLog.Logger()`

Description forthcoming.

---

## Instance Methods

---

### appendln

`public abstract void appendln(Object anObject)`

Since this is an abstract method, it does nothing by default. It's up to the subclass to implement the behavior. As implemented in NSLog, this method appends the string representation of _anObject_ to the logging output. For example, a generic object passed to this method might output "java.lang.Object@67e5d". The string representation is derived from the __toString()__ method of the object.

`public void appendln(Throwable aThrowable)`

Calls __appendln__(Object _anObject_) with __NSLog__.__throwableAsString__(_aThrowable_) as an argument.

`public void appendln(int anInt)`

Calls __appendln__(Object _anObject_), by transforming _anInt_ into a Java Integer class object.

`public void appendln(float aFloat)`

Calls __appendln__(Object _anObject_) by transforming _aFloat_ into a Java Float class object.

`public void appendln(short aShort)`

Calls __appendln__(Object _anObject_), by transforming _aShort_ into a Java Short class object.

`public void appendln(long aLong)`

Calls __appendln__(Object _anObject_), by transforming _anInt_ into a Java Long class object.

`public void appendln(byte[] aByteArray)`

Calls __appendln__(Object _anObject_), by transforming _aByte[]_ into a Java String class object.

`public void appendln(char[] aCharArray)`

Calls __appendln__(Object _anObject_), by transforming _aChar[]_ into a Java String class object.

`public void appendln(boolean aBoolean)`

Calls __appendln__(Object _anObject_), passing `true` if _aBoolean_ is true, `false` if aBoolean is false.

`public void appendln(double aDouble)`

Calls __appendln__(Object _anObject_), by transforming _aDouble_ into a Java Double class object.

`public void appendln(char aChar)`

Calls __appendln__(Object _anObject_), by transforming _aChar[]_ into a Java String class object.

`public void appendln(byte aByte)`

Calls __appendln__(Object _anObject_), by transforming _aByte_ into a Java Byte class object.

`public void appendln()`

Since this is an abstract method, it does nothing by default. As implemented in NSLog, this method appends a new line to the logging output.

---

### flush

`public abstract void flush()`

Since this is an abstract method, it does nothing by default. As implemented in NSLog, this method allows you to flush the internal buffer.

---

### isEnabled

`public boolean isEnabled()`

Returns the value of an internal boolean, which defaults to `true`, and is set by [setIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5zwk5cjoncw4ylcnrswi). As implemented in NSLog, the internal boolean regulates whether logging is enabled or disabled. When logging is disabled, the receiver ignores all invocations of [appendln](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5qxa4dfnzsgy3q). By default, logging is enabled.

---

### isVerbose

`public boolean isVerbose()`

Returns the value of an internal boolean, which defaults to `true`, and is set by [setIsVerbose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5zwk5cjonlgk4tcn5zwk). As implemented in NSLog, the internal boolean regulates whether verbose logging is activated or deactivated. See the method description for [setIsVerbose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5zwk5cjonlgk4tcn5zwk) for more information. By default, verbose logging is disabled.

---

### setIsEnabled

`public void setIsEnabled(boolean aBoolean)`

Sets the value of an internal boolean to _aBoolean_. As implemented in NSLog, the internal boolean disables logging if _aBoolean_ is false. When logging is disabled, the receiver ignores all invocations of [appendln](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwolsmn5twozlsf5qxa4dfnzsgy3q). By default, logging is enabled.

---

### setIsVerbose

`public void setIsVerbose(boolean aBoolean)`

Sets the value of an internal boolean to _aBoolean_. As implemented in NSLog, the internal boolean enables verbose logging if _aBoolean_ is true. Verbose logging produces output of the format: "[Current Time] <Current Thread Name> object ". By default, verbose logging is disabled in NSLog.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
