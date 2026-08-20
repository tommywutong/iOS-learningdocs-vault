---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOEditors.html
archived_at: '2026-07-18T01:28:32.620831Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOEditingContext.Delegate.md)
[!](EOEnterpriseObject.md)

---

# EOEditingContext.Editor

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Interface Description

The EOEditingContext.Editor interface defines methods for objects that act as higher-level editors of the objects an EOEditingContext contains. An editing context sends messages to its editors to determine whether they have any changes that need to be saved, and to allow them to flush pending changes before a save (possibly throwing an exception to abort the save). See the [EOEditingContext](EOEditingContext.md) and EODisplayGroup (EOInterface) class specifications for more information.

Editors are not required to provide implementations for all of the methods in the interface. When you write an editor, you don't have to use the __implements__ keyword to specify that the object implements the Editors interface. Instead, simply use the EOEditingContext method [__addEditor__](EOEditingContext.md)method to assign your object as one of the EOEditingContext's editors and then declare and implement any subset of the methods declared in the Editors interface. An EOEditingContext can determine if the editor doesn't implement a method and only attempts to invoke the methods the editor actually implements.

## Instance Methods

---

#### editingContextWillSaveChanges

public abstract void __editingContextWillSaveChanges__ (EOEditingContext _anEditingContext_)

Invoked by _anEditingContext_ in its [__saveChanges__](EOEditingContext.md)method, this method allows the receiver to flush any pending edits and, if necessary, prohibit a save operation. The receiver should validate and flush any unprocessed edits it has, throwing an exception if it can't do so to prevent _anEditingContext_ from saving.

---

#### editorHasChangesForEditingContext

public abstract boolean __editorHasChangesForEditingContext__ (EOEditingContext _anEditingContext_)

Invoked by _anEditingContext_, this method should return __true__ if the receiver has any unapplied edits that need to be saved, __false__ if it doesn't.

---

[!](EOEditingContext.Delegate.md)
[!](EOEnterpriseObject.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
