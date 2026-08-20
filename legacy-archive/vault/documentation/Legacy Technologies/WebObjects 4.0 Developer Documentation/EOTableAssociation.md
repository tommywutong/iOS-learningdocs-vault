---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOTableAssociation.html
archived_at: '2026-07-18T01:28:44.111889Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EORecursiveBrowserAssociation.md)
[!](EOTableColumnAssociation.md)

---

# EOTableAssociation

__Inherits From:__
EOAssociation : .EODelayedObserver (EOControl) : Object

com.sun.java.swing.event.ListSelectionListener

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

EOTableAssociation associates the contents of its `SourceAspect`'s display group with a Swing JTable. In general use, it should never be necessary to explicitly instantiate this class, as EOTableColumnAssociation's [`setTable`](EOTableColumnAssociation.md#apple-gm2tanq) assures that an instance exists for its _table_.

EOTableAssociation is for use in Java Client applications only; the equivalent Yellow Box class is EOTableViewAssociation.

| __Usable With__ |
| com.sun.java.swing.JTable |

```
```

| __Aspects__ | __Aspects__ |
| EnabledAspect |  |
| SourceAspect |  |

```
```


---

## Constructors

public `EOTableAssociation`()

public `EOTableAssociation`(java.lang.Object _object_)

---

## Instance Methods

---

### editingAssociation

public EOTableColumnAssociation `editingAssociation`()

Returns the EOTableColumnAssociation bound to the column being edited in the receiver's display object, if any.

---

### isEditableAtRow

public boolean `isEditableAtRow`(int _row_)

Returns whether or not the display object bound to the receiver is editable at _row_ as determined by the EnabledAspect. If this aspect is bound, a non-zero value at _row_ indicates that the property may be edited. If the EnabledAspect is unbound all rows are considered editable.

---

### primaryAspect

public java.lang.String `primaryAspect`()

Returns SourceAspect.

---

### valueChanged

public void `valueChanged`(com.sun.java.swing.event.ListSelectionEvent _event_)

EOTableAssociation listens to its display object's TableModel in order to synchronize the selection indices of its SourceAspect's EODisplayGroup with those of the model. This method represents the association's implementation of the ListSelectionListener interface.

---

### 

---

[!](EORecursiveBrowserAssociation.md)
[!](EOTableColumnAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
