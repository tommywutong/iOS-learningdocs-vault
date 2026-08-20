---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOTableColumnAssociation.html
archived_at: '2026-07-18T01:28:44.185354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOTableAssociation.md)
[!](EOTableViewAssociation.md)

---

# EOTableColumnAssociation

__Inherits From:__
EOAssociation : .EODelayedObserver (EOControl) : Object

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

An EOTableColumnAssociation associates a single attribute of all enterprise objects in its ValueAspect's EODisplayGroup with a Swing JTable TableColumn. The value of each object's attribute is displayed in its corresponding row.

By far the easiest way to configure EOTableColumnAssociations is in InterfaceBuilder, but they may also be instantiated programmatically. Because Swing's TableColumn maintains no reference to its containing JTable, this relationship must be explicitly specified via [`setTable`](#apple-gm2tanq) before `establishConnection` is invoked.

EOTableColumnAssociation is for use in Java Client applications only; the equivalent Yellow Box class is EOColumnAssociation.

| __Usable With__ |
| com.sun.java.swing.table.TableColumn |

```
```

| __Aspects__ | __Aspects__ |
| BoldAspect |  |
| EnabledAspect | A boolean attribute of the objects, which determines whether each object's value cell is editable. Note that because EOTableViewAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| ItalicAspect |  |
| ValueAspect | An attribute of the objects, displayed in each row of the TableColumn. |

```
```


---

## Constructors

public `EOTableColumnAssociation`(java.lang.Object _anObject_)

---

## Instance Methods

---

### format

public java.text.Format `format`()

Returns the java.lang.text.Format used to format values bound to the receiver's ValueAspect for display and editing .

---

### isEditableAtRow

public boolean `isEditableAtRow`(int _row_)

Returns whether or not the property bound to the receiver's ValueAspect is editable at _row_, as determined by the EnabledAspect. If this aspect is bound, a non-zero value at _row_ indicates that the property may be edited. If the EnabledAspect is unbound all rows are considered editable.

---

### primaryAspect

public java.lang.String `primaryAspect`()

Returns ValueAspect.

---

### setFormat

public void `setFormat`(java.text.Format _aFormat_)

Sets the java.lang.text.Format object to use in formatting values bound to the receiver's ValueAspect for display and editing.

---

### setTable

public void `breakConnection`()

Because TableColumn maintains no reference to its containing JTable, the consumer must explicitly specify this relationship by invoking `setTable` _before_ `establishConnection`. This method also assures that an instance of EOTableAssociation exists for _table_.

---

[!](EOTableAssociation.md)
[!](EOTableViewAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
