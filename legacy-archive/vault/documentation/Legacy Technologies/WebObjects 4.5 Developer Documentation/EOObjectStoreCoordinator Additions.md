---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOObjectStoreCrdntrAddtns.html
archived_at: '2026-07-15T08:11:33.759220Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOObjectStoreCoordinator Additions

> __Category
> of:__ EOObjectStoreCoordinator

> __Declared in:__  EOAccess/EOModelGroup.h

---

## Category Description

---

The EOAccess framework adds two methods to EOControl's EOObjectStoreCoordinator
class for accessing the coordinator's EOModelGroup. An application
can have multiple EOObjectStoreCoordinators, and each coordinator
can have a different EOModelGroup. (For more discussion of this
subject, see the chapter "Application Configurations" in the _Enterprise
Objects Framework Developer's Guide_.) Application and
framework code needing access to the EOModelGroup for a given EOEditingContext
can get that information by asking the EOEditingContext's EOObjectStoreCoordinator
for its EOModelGroup.

The methods are defined in a category of EOObjectStoreCoordinator
in EOAccess (instead of in EOControl's EOObjectStoreCoordinator
interface) to preserve the EOControl framework's independence
of the EOAccess framework.

## Instance Methods

---

### modelGroup

`- (EOModelGroup *)modelGroup`

Returns the receiver's EOModelGroup. By default,
this method returns the results of the statement [EOModelGroup defaultGroup].
If your application is using more than one EOObjectStoreCoordinator,
each coordinator can have its own EOModelGroup.

---

### setModelGroup:

`- (void)setModelGroup:(EOModelGroup
*)group`

Sets to group the EOModelGroup used by the receiver.
By default, an EOObjectStore's EOModelGroup is the model group
returned from the statement `[EOModelGroup defaultGroup]`.
However, you can override this by using [setModelGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoiqeczdenf2gs33oomxxgzlujvxwizlmi5zg65lqhi) to explicitly set
a different EOModelGroup for the receiver. Other parts of Enterprise
Objects Framework (such as EODatabaseContext) use the EOModelGroup
bound to their EOObjectStoreCoordinator.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
