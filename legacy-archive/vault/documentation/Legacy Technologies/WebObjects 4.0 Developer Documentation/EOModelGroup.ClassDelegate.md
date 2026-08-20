---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOModelGroupClassDelegate.html
archived_at: '2026-07-18T01:28:14.728710Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOUtilities.md)
[!](EOModelGroup.Delegate.md)

---

# EOModelGroup.ClassDelegate

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

An EOModelGroup object should have a delegate which can influence how it finds and loads models. In addition to the delegates you assign to EOModelGroup instances, the EOModelGroup class itself can have a delegate. The class delegate implements a single method-[`defaultModelGroup`](#apple-gizda).

For more information on EOModelGroup instance delegate methods, see the [EOModelGroup.Delegate](EOModelGroup.Delegate.md) specifications.

---

## Instance Methods

---

### defaultModelGroup

public abstract EOModelGroup `defaultModelGroup`()

If implemented by the EOModelGroup class delegate, this method should return the EOModelGroup to be returned in response to the message `defaultModelGroup`. If this delegate method returns `null`, EOModelGroup uses the default behavior of the `defaultModelGroup` class method.

__Note:__
This method is implemented by the delegate assigned to the EOModelGroup class object.

__See also:__
[`classDelegate`](../Classes/EOModelGroup.md#apple-geydcnjw) (EOModelGroup class), [`setClassDelegate`](../Classes/EOModelGroup.md#apple-geydaobx) (EOModelGroup class)

---

[!](EOUtilities.md)
[!](EOModelGroup.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
