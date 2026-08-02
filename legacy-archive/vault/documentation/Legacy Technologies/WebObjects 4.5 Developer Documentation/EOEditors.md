---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOEditors.html
archived_at: '2026-07-15T08:11:42.925902Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOEditors

> __(informal protocol)__

> __Declared in:__ : EOControl/EOEditingContext.h

---

## Protocol Description

---

The [EOEditors](#apple-inbecrckindee) informal
protocol defines methods for objects that act as higher-level editors
of the objects an EOEditingContext contains. An editing context
sends messages to its editors to determine whether they have any
changes that need to be saved, and to allow them to flush pending
changes before a save (possibly raising an exception to abort the
save). See the [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) and EODisplayGroup
(EOInterface) class specifications for more information.

## Instance Methods

---

### editingContextWillSaveChanges:

`- (void)editingContextWillSaveChanges:(EOEditingContext
*)anEditingContext`

Invoked by _anEditingContext_ in
its [saveChanges](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt) method, this method allows
the receiver to flush any pending edits and, if necessary, prohibit
a save operation. The receiver should validate and flush any unprocessed
edits it has, raising an exception if it can't do so to prevent _anEditingContext_ from
saving.

---

### editorHasChangesForEditingContext:

`- (BOOL)editorHasChangesForEditingContext:(EOEditingContext
*)anEditingContext`

Invoked by _anEditingContext_,
this method should return YES if the receiver has any unapplied
edits that need to be saved, NO if it doesn't.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
