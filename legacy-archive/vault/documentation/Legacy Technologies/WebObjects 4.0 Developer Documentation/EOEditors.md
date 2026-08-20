---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOEditors.html
archived_at: '2026-07-18T01:28:41.004243Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEditingContextDelegate.md)
[!](EOEnterpriseObject-3.md)

---

# EOEditors

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOEditingContext.h

## Category Description

The EOEditors informal protocol defines methods for objects that act as higher-level editors of the objects an EOEditingContext contains. An editing context sends messages to its editors to determine whether they have any changes that need to be saved, and to allow them to flush pending changes before a save (possibly raising an exception to abort the save). See the [EOEditingContext](EOEditingContext-3.md) and EODisplayGroup (EOInterface) class specifications for more information.

---

#### editingContextWillSaveChanges:

- (void)__editingContextWillSaveChanges:__ (EOEditingContext \*)_anEditingContext_

Invoked by _anEditingContext_ in its [__saveChanges__](EOEditingContext-3.md)method, this method allows the receiver to flush any pending edits and, if necessary, prohibit a save operation. The receiver should validate and flush any unprocessed edits it has, raising an exception if it can't do so to prevent _anEditingContext_ from saving.

---

#### editorHasChangesForEditingContext:

- (BOOL)__editorHasChangesForEditingContext:__ (EOEditingContext \*)_anEditingContext_

Invoked by _anEditingContext_, this method should return YES if the receiver has any unapplied edits that need to be saved, NO if it doesn't.

---

[!](EOEditingContextDelegate.md)
[!](EOEnterpriseObject-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
