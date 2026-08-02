---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/WOActionResults.html
archived_at: '2026-07-18T01:28:54.840583Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEditingContext%20Additions.md)
[!](WODisplayGroupDelegate.md)

---

# WOActionResults

__Adopted By:__
[WOComponent](WOComponent-2.md), [WOResponse](WOResponse-2.md)

__Declared in:__
WebObjects/WOResponse.h

# Protocol Description

The WOActionResults protocol is the return type for direct actions. As a convenience, direct actions can return either [WOComponent](WOComponent-2.md) objects or [WOResponse](WOResponse-2.md) objects; both of which implement the WOActionResults protocol. This protocol implement only one method [__generateResponse__](#apple-ge4dgny).

If you want to return any other class from a direct action, then that class must implement this protocol.

---

### generateResponse

- (WOResponse \*)`generateResponse`

Returns a response object. WOResponse's implementation of this method returns the receiver. WOComponent's implementation of this method calls [__appendToResponse:inContext:__](WOComponent-2.md#apple-geydgmq) on itself and all children components in its template and returns the result as a WOResponse object. If you want to return any other class from a direct action, then that class must implement this method.

---

[!](EOEditingContext%20Additions.md)
[!](WODisplayGroupDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
