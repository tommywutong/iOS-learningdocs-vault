---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOClassDescClassDelegate.html
archived_at: '2026-07-15T08:11:42.285254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOClassDescription ClassDelegate

> __(informal protocol)__

> __Declared in:__ : EOControl/EOClassDescription.h

---

## Protocol Description

---

The [EOClassDescription ClassDelegate](#apple-indeeq2eijcei) informal
protocol defines a method that the EOClassDescription class can
invoke in its delegate. Delegates are not required to provide an implementation
for the method. Instead, declare and implement the method if you
need it, and use the EOClassDescription method [setClassDelegate:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3tmv2eg3dbonzuizlmmvtwc5dfhi) method
to assign your object as the class delegate. The EOClassDescription
class can determine if the delegate doesn't implement the delegate
method and only attempts to invoke it if it's actually implemented.

## Instance Methods

---

### shouldPropagateDeleteForObject:inEditingContext:forRelationshipKey:

`- (BOOL)shouldPropagateDeleteForObject:(id)anObject
inEditingContext:(EOEditingContext
*)anEditingContext
forRelationshipKey:(NSString *)key`

Invoked from [propagateDeleteForObject:editingContext:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5yhe33qmftwc5dfirswyzlumvdg64spmjvgky3uhjswi2lunfxgoq3pnz2gk6duhi).
If the class delegate returns NO, it prevents _anObject_ in _anEditingContext_ from
propagating deletion to the objects at the destination of _key_.
This can be useful if you have a large model and a small application
that only deals with a subset of the model's entities. In such
a case you might want to disable delete propagation to entities
that will never be accessed. You should use this method with caution,
however-returning NO and not propagating deletion can lead to
dangling references in your object graph.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
