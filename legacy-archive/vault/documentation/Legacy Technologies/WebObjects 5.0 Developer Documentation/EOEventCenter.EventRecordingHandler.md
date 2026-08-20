---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOEventRecordingHandler.html
archived_at: '2026-07-15T08:13:47.956955Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOEventCenter.EventRecordingHandler

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The EOEventCenter. EventRecordingHandler interface, a part of the event logging system, declares the setLoggingEnabled method, which is invoked by the event logging system when event logging is enabled or disabled for an event class. Event recording handlers are responsible for enabling logging in instrumented code. An event recording handler only receives messages about event classes registered with registerEventClass. For more information on the event logging mechanism, see the EOEventCenter class specification.

## Instance Methods

---

### setLoggingEnabled

`public abstract void setLoggingEnabled( boolean flag, Class aClass)`

If _flag_ is true, then instrumented code should log events of class _aClass_, and the receiver should enable updating in instrumented code (usually by setting a flag).

__See Also:__ registerEventClass (EOEventCenter)

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
