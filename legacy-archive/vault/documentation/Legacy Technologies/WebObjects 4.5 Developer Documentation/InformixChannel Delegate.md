---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/ObjC_classic/Protocols/InformixChannelDelegate.html
archived_at: '2026-07-15T08:11:45.998990Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md) 

# InformixChannel Delegate

> __(informal protocol)__

> __Declared in:__  InformixEOAdaptor/InformixChannel.h

## Protocol Description

---

InformixChannel's delegate allows you to process errors
that occur in the Informix server.

## Instance Methods

---

### informixChannel:willReportDatabaseError:

`- (BOOL)informixChannel:(InformixChannel
*)channel
willReportDatabaseError:(NSString
*)error`

Invoked whenever _channel_ encounters
an error reported by the Informix server. The _error_ argument
is the text of the Informix error message which will be sent to
the adaptor's __reportError:__ method. The delegate
can return NO to prevent the channel from calling __reportError:__.

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
