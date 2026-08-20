---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOEditors.html
archived_at: '2026-07-15T08:11:38.862139Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEditingContext.Editor

> __(informal interface)__

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The [EOEditingContext.Editor](#apple-inbecrckindee) interface defines
methods for objects that act as higher-level editors of the objects
an EOEditingContext contains. An editing context sends messages
to its editors to determine whether they have any changes that need
to be saved, and to allow them to flush pending changes before a
save (possibly throwing an exception to abort the save). See the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) and EODisplayGroup
(EOInterface) class specifications for more information.

Editors are not required to provide implementations for all
of the methods in the interface. When you write an editor, you don't
have to use the `implements` keyword to specify
that the object implements the Editors interface. Instead, simply
use the EOEditingContext method [addEditor](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmfsgirlenf2g64q) method to assign your object
as one of the EOEditingContext's editors and then declare and
implement any subset of the methods declared in the Editors interface.
An EOEditingContext can determine if the editor doesn't implement
a method and only attempts to invoke the methods the editor actually
implements.

## Instance Methods

---

### editingContextWillSaveChanges

`public abstract void editingContextWillSaveChanges(EOEditingContext anEditingContext)`

Invoked by _anEditingContext_ in
its [saveChanges](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom) method, this method allows
the receiver to flush any pending edits and, if necessary, prohibit
a save operation. The receiver should validate and flush any unprocessed
edits it has, throwing an exception if it can't do so to prevent _anEditingContext_ from saving.

---

### editorHasChangesForEditingContext

`public abstract boolean editorHasChangesForEditingContext(EOEditingContext anEditingContext)`

Invoked by _anEditingContext,_
this method should return true if the receiver has any unapplied
edits that need to be saved, false if it doesn't.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
