---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOEventRecordingHandler.html
archived_at: '2026-07-15T08:11:38.898992Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEventCenter.EventRecordingHandler

> **__Package:__**
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOEventCenter.EventRecordingHandler interface,
a part of the event logging system, declares the [setLoggingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiv3gk3tuinsw45dfoixek5tfnz2fezldn5zgi2lom5egc3tenrsxel3tmv2ey33hm5uw4z2fnzqwe3dfmq) method,
which is invoked by the event logging system when event logging
is enabled or disabled for an event class. Event recording handlers
are responsible for enabling logging in instrumented code. An event
recording handler only receives messages about event classes registered
with [registerEventClass](EOEventCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojswo2ltorsxerlwmvxhiq3mmfzxg). For more information
on the event logging mechanism, see the [EOEventCenter](EOEventCenter.md#apple-inauqqsjindei) class specification.

|  |
| --- |
| __Note:__  This interface doesn't exist in the Java Client package, com.apple.client.eocontrol. The event logging system is not available for Java Client. In a Java Client application, you can view event logging information for the server side of the application, but not on the client side. |

## Instance Methods

---

### setLoggingEnabled

`public abstract void setLoggingEnabled(
boolean flag,
Class aClass)`

If _flag_ is true,
then instrumented code should log events of class _aClass,_
and the receiver should enable updating in instrumented code (usually
by setting a flag).

__See Also:__
[registerEventClass](EOEventCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlwmvxhiq3fnz2gk4rpojswo2ltorsxerlwmvxhiq3mmfzxg) ( [EOEventCenter](EOEventCenter.md#apple-inauqqsjindei))

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
