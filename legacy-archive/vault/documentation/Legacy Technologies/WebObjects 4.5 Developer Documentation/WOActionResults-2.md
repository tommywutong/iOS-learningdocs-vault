---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Protocols/WOActionResults.html
archived_at: '2026-07-15T08:11:47.894385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOActionResults

> __Adopted by:__
> [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq), [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f)

> __Declared in:__  WebObjects/WOResponse.h

## Protocol Description

---

The WOActionResults protocol is the return type for direct
actions. As a convenience, direct actions can return either [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq) objects or [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f) objects; both of which
implement the WOActionResults protocol. This protocol implements
only one method: [generateResponse](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxvot2bmn2gs33okjsxg5lmorzs6z3fnzsxeylumvjgk43qn5xhgzi).

If you want to return any other class from a direct action,
then that class must implement this protocol.

## Instance Methods

---

### generateResponse

`- (WOResponse *)generateResponse`

Returns a response object. WOResponse's implementation
of this method returns the receiver. WOComponent's implementation
of this method calls [appendToResponse:inContext:](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi) on
itself and all children components in its template and returns the
result as a WOResponse object. If you want to return any other class
from a direct action, then that class must implement this method.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
