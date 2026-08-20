---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOEditingContextAdditions.html
archived_at: '2026-07-18T01:28:53.067545Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOStatisticsStore-2.md)
[!](WOActionResults-2.md)

---

# EOEditingContext __Additions__

__Inherits From:__
NSObject

__Declared in:__
WebObjects/WODisplayGroup.h

---

## Class Description

The WebObjects Framework adds one method to the Enterprise Objects Framework's EOEditingContext class that atempts to commit changes made in the receiver to its parent EOObjectStore.

---

## Instance Methods

---

### tryToSaveChanges

- (NSException \*)`tryToSaveChanges`

Attempts to commit changes made in the receiver to its parent EOObjectStore by sending it the message __saveChangesInEditingContext:__ . If the parent is an EOObjectStoreCoordinator, it guides its EOCooperatingObjectStores, typically EODatabaseContexts, through a multi-pass save operation (see the EOObjectStoreCoordinator class specification for more information). If no message handler or delegate is available and a database error occurs, an exception is raised that can be caught in WebScript; the error message indicates the nature of the problem.

---

[!](WOStatisticsStore-2.md)
[!](WOActionResults-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
