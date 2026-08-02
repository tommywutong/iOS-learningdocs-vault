---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOClassDescClassDelegate.html
archived_at: '2026-07-15T08:11:38.819342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOClassDescription.ClassDelegate

> __(informal interface)__

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The [EOClassDescription.ClassDelegate](#apple-indeeq2eijcei) interface defines
a method that the EOClassDescription class can invoke in its delegate.
Delegates are not required to provide an implementation for the
method, and you don't have to use the implements keyword to specify
that the object implements the ClassDelegate interface. Instead,
declare and implement the method if you need it, and use the EOClassDescription method [setClassDelegate](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rponsxiq3mmfzxgrdfnrswoylumu) method
to assign your object as the class delegate. The EOClassDescription class
can determine if the delegate doesn't implement the delegate method
and only attempts to invoke it if it's actually implemented.

## Instance Methods

---

### shouldPropagateDeleteForObject

`public abstract boolean shouldPropagateDeleteForObject(
EOEnterpriseObject anObject,
EOEditingContext anEditingContext,
String key)`

Invoked from [propagateDeleteForObject](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxa4tpobqwoylumvcgk3dforsum33sj5rguzldoq).
If the class delegate returns false, it prevents _anObject_ in _anEditingContext_ from
propagating deletion to the objects at the destination of _key._
This can be useful if you have a large model and a small application
that only deals with a subset of the model's entities. In such
a case you might want to disable delete propagation to entities
that will never be accessed. You should use this method with caution,
however-returning false and not propagating deletion can lead to
dangling references in your object graph.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
