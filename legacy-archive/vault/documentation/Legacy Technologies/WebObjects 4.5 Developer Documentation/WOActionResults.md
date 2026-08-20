---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Protocols/WOActionResults.html
archived_at: '2026-07-15T08:11:47.255572Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOActionResults

> __Implemented by:__
> [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq), [WOResponse](WOResponse.md#apple-k5hvezltobxw443f)

> __Package:__
> com.apple.yellow.webobjects

## Interface Description

---

The WOActionResults interface is the return type for direct
actions. As a convenience, direct actions can return either [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) objects or [WOResponse](WOResponse.md#apple-k5hvezltobxw443f) objects; both of which
implement the WOActionResults protocol. This interface implements
only one method: [generateResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2pifrxi2lpnzjgk43vnr2hgl3hmvxgk4tborsvezltobxw443f).

If you want to return any other class from a direct action,
then that class must implement this protocol.

## Instance Methods

---

### generateResponse

`public abstract WOResponse generateResponse()`

Returns a response object. WOResponse's implementation
of this method returns the receiver. WOComponent's implementation
of this method calls [appendToResponse](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu) on
itself and all children components in its template and returns the
result as a WOResponse object. If you want to return any other class
from a direct action, then that class must implement this method.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
