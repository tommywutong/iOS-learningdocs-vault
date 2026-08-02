---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOObjectStoreCoordntrAdtns.html
archived_at: '2026-07-18T01:28:16.984880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](Setting%20Up%20A%20Model%20Group%20Programmatically-2.md)
[!](EOQualifier%20Additions.md)

---

# EOObjectStoreCoordinator Additions

__Inherits From:__
EOObjectStoreCoordinator : NSObject

__Declared in:__
EOAccess/EOModelGroup.h

---

## Class Description

The EOAccess framework adds two methods to EOControl's EOObjectStoreCoordinator class for accessing the coordinator's EOModelGroup. An application can have multiple EOObjectStoreCoordinators, and each coordinator can have a different EOModelGroup. (For more discussion of this subject, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.) Application and framework code needing access to the EOModelGroup for a given EOEditingContext can get that information by asking the EOEditingContext's EOObjectStoreCoordinator for its EOModelGroup.

The methods are defined in a category of EOObjectStoreCoordinator in EOAccess (instead of in EOControl's EOObjectStoreCoordinator interface) to preserve the EOControl framework's independence of the EOAccess framework.

---

## Instance Methods

---

### modelGroup

- (EOModelGroup \*)__modelGroup__

Returns the receiver's EOModelGroup. By default, this method returns the results of the statement `[EOModelGroup defaultGroup]`. If your application is using more than one EOObjectStoreCoordinator, each coordinator can have its own EOModelGroup.

---

### setModelGroup:

- (void)__setModelGroup:__ (EOModelGroup \*)_group_

Sets to _group_ the EOModelGroup used by the receiver. By default, an EOObjectStore's EOModelGroup is the model group returned from the statement `[EOModelGroup defaultGroup]`. However, you can override this by using [`setModelGroup:`](#apple-geyti) to explicitly set a different EOModelGroup for the receiver. Other parts of Enterprise Objects Framework (such as EODatabaseContext) use the EOModelGroup bound to their EOObjectStoreCoordinator.

---

[!](Setting%20Up%20A%20Model%20Group%20Programmatically-2.md)
[!](EOQualifier%20Additions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
