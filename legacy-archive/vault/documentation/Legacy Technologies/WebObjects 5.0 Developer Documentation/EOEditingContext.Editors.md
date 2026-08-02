---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOEditors.html
archived_at: '2026-07-15T08:13:47.850821Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOEditingContext.Editors

> __(informal interface)__

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The [EOEditingContext.Editors](#apple-inbecrckindee) interface defines methods for objects that act as higher-level editors of the objects an EOEditingContext contains. An editing context sends messages to its editors to determine whether they have any changes that need to be saved, and to allow them to flush pending changes before a save (possibly throwing an exception to abort the save). See the EOEditingContext and EODisplayGroup (EOInterface) class specifications for more information.

Editors are not required to provide implementations for all of the methods in the interface. When you write an editor, you don't have to use the __implements__ keyword to specify that the object implements the Editors interface. Instead, simply use the EOEditingContext method addEditor method to assign your object as one of the EOEditingContext's editors and then declare and implement any subset of the methods declared in the Editors interface. An EOEditingContext can determine if the editor doesn't implement a method and only attempts to invoke the methods the editor actually implements.

## Instance Methods

---

### editingContextWillSaveChanges

`public abstract void editingContextWillSaveChanges(EOEditingContext anEditingContext)`

Invoked by _anEditingContext_ in its saveChanges method, this method allows the receiver to flush any pending edits and, if necessary, prohibit a save operation. The receiver should validate and flush any unprocessed edits it has, throwing an exception if it can't do so to prevent _anEditingContext_ from saving.

---

### editorHasChangesForEditingContext

`public abstract boolean editorHasChangesForEditingContext(EOEditingContext anEditingContext)`

Invoked by _anEditingContext_, this method should return true if the receiver has any unapplied edits that need to be saved, false if it doesn't.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
