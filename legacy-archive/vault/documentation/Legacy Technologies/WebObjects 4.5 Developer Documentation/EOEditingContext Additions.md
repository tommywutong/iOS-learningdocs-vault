---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/EOEditingContextAdditions.html
archived_at: '2026-07-15T08:11:47.295908Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)

# EOEditingContext Additions

> __Inherits
> from:__  NSObject

> __Declared in:__  WebObjects/WODisplayGroup.h

---

## Class Description

---

The WebObjects Framework adds one method to the Enterprise
Objects Framework's EOEditingContext class that atempts to commit
changes made in the receiver to its parent EOObjectStore.

## Instance Methods

---

### tryToSaveChanges

`- (NSException *)tryToSaveChanges`

Attempts to commit changes made in the receiver
to its parent EOObjectStore by sending it the message __saveChangesInEditingContext:__.
If the parent is an EOObjectStoreCoordinator, it guides its EOCooperatingObjectStores,
typically EODatabaseContexts, through a multi-pass save operation
(see the EOObjectStoreCoordinator class specification for more information).
If no message handler or delegate is available and a database error
occurs, an exception is raised that can be caught in WebScript; the
error message indicates the nature of the problem.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
