---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOTableViewAssociation.html
archived_at: '2026-07-18T01:28:46.878447Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EORecursiveBrowserAssociation-2.md)
[!](EOTextAssociation-2.md)

---

# EOTableViewAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOColumnAssociation.h

---

## Class Description

An EOTableViewAssociation object manages the individual EOColumnAssociations between an NSTableView (Application Kit) and an EODisplayGroup. An EOTableViewAssociation can sort the objects in the display group by the left-to-right order of the table columns. The first EOColumnAssociation to be bound to a table view automatically creates the EOTableViewAssociation; you should rarely need to do so yourself.

An EOTableViewAssociation receives data source and delegate messages from the table view, some of which it handles itself, and some of which it forwards to the appropriate EOColumnAssociations. For more information, see the EOColumnAssociation class specification.

| __Usable With__ |
| NSTableView |

```
```

| __Aspects__ | __Aspects__ |
| source | Bound to the EODisplayGroup providing objects. This aspect doesn't use a key. |
| enabled | A boolean attribute of the objects, which determines whether each object's row is editable. Note that because EOColumnAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| textColor | An NSColor attribute of the objects, which determines the color of text for each object's row in the NSTableView. |
| bold | A boolean attribute of the objects, which determines whether each objects row is displayed in bold or regular weight text. |
| italic | A boolean attribute of the objects, which determines whether each objects row is displayed in italic or normal angle text. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| dataSource | An EOTableViewAssociation responds to some data source messages and forwards others to the appropriate EOColumnAssociation. |
| delegate | An EOTableViewAssociation forwards delegate messages to the appropriate EOColumnAssociations. |
| target | Reserved, but not used. |

```
```


---

## Example

For an example of using an EOTableViewAssociation, see the EOColumnAssociation class specification.

---

## Method Types

**Setting up a table view association**

**[+ bindToTableView:displayGroup:](#apple-gezte)**

**Sorting**

**[- setSortsByColumnOrder:](#apple-gezts)

**[- sortsByColumnOrder](#apple-ge2di)****

**Accessing the active EOColumnAssociation**

**[- editingAssociation](#apple-geztm)**

**Table view data source methods**

**[- numberOfRowsInTableView:](#apple-ge3de)

**[- tableView:setObjectValue:forTableColumn:row:](#apple-ge3ds)

**- tableViewObjectValueForLocationtableView:
objectValueForTableColumn:row:******

**Table view delegate methods**

**[- tableView:shouldEditTableColumn:row:](#apple-ge3te)

**[- tableView:willDisplayCell:forTableColumn:row:](#apple-ge3tk)****

**Table view notification methods**

**[- tableViewSelectionDidChange:](#apple-geytsoa)**

**Control delegate methods**

**- controlDidFailToFormatStringErrorDescriptioncontrol:
didFailToFormatString:errorDescription:

**[- control:isValidObject:](#apple-geytenq)

**- controlTextShouldBeginEditingcontrol:textShouldBeginEditing:******

---

## Class Methods

---

### bindToTableView:displayGroup:

+ (void)`bindToTableView:`(NSTableView \*)_aTableView_`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_

Creates an EOTableViewAssociation, binding _aTableView_ to _aDisplayGroup_, if there isn't already a table view association for _aTableView_.

---

## Instance Methods

---

### editingAssociation

- (EOColumnAssociation \*)`editingAssociation`

Returns the EOColumnAssociation for the NSTableView cell being edited, or `nil` if no cell is being edited.

---

### setSortsByColumnOrder:

- (void)`setSortsByColumnOrder:`(BOOL)_flag_

Controls whether the receiver applies a sort ordering to its EODisplayGroup. If _flag_ is YES, it builds EOSortOrderings (EOControl) for each of the EOColumnAssociations, collects them into an NSArray based on the left-to-right order of the columns, and assigns them to the display group with [`setSortOrderings:`](EODisplayGroup.md#apple-ge2teoa). If _flag_ is NO, it doesn't alter the sort ordering of the display group.

An EOTableViewAssociation assigns sort orderings based on the left to right order of the table columns, and reassigns them whenever the user moves a column.

__See also:__
[- `sortingSelector`](EOColumnAssociation.md#apple-gezda) (EOColumnAssociation)

---

### sortsByColumnOrder

- (BOOL)`sortsByColumnOrder`

Returns YES if the receiver assigns EOSortOrderings (EOControl) to its EODisplayGroup based on the sorting selectors of its EOColumnAssociations, NO if it doesn't alter the display group's sort ordering.

---

## Data Source, Delegate, and Notification Methods

---

### control:didFailToFormatString:errorDescription:

- (BOOL)`control:`(NSControl \*)_aTableView_`didFailToFormatString:`(NSString \*)_aString_`errorDescription:`(NSString \*)_errorDescription_

Forwards the message to the receiver's editing association.

__See also:__
[- `editingAssociation`](#apple-geztm)

---

### control:isValidObject:

- (BOOL)`control:`(NSControl \*)_aTableView_`isValidObject:`(id)_anObject_

Forwards the message to the receiver's editing association.

__See also:__
[- `editingAssociation`](#apple-geztm)

---

### control:textShouldBeginEditing:

- (BOOL)`control:`(NSControl \*)_aTableView_`textShouldBeginEditing:`(NSText \*)_fieldEditor_

Forwards the message to the receiver's editing association.

__See also:__
[- `editingAssociation`](#apple-geztm)

---

### numberOfRowsInTableView:

- (int)`numberOfRowsInTableView:`(NSTableView \*)_aTableView_

Returns the number of displayed objects in the receiver's EODisplayGroup.

__See also:__
[- `displayedObjects`](EODisplayGroup.md#apple-geztmmi) (EODisplayGroup)

---

### tableView:objectValueForTableColumn:row:

- (id)`tableView:`(NSTableView \*)_aTableView_`objectValueForTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-so that it can provide the value.

---

### tableViewSelectionDidChange:

- (void)`tableViewSelectionDidChange:`(NSNotification \*)_aNotification_

Updates the receiver's EODisplayGroup based on the new selection in the table view.

__See also:__
[- `setSelectionIndexes:`](EODisplayGroup.md#apple-ge2tcoa) (EODisplayGroup)

---

### tableView:setObjectValue:forTableColumn:row:

- (void)`tableView:`(NSTableView \*)_aTableView_`setObjectValue:`(id)_value_`forTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-so that it can set the value.

---

### tableView:shouldEditTableColumn:row:

- (BOOL)`tableView:`(NSTableView \*)_aTableView_`shouldEditTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Returns NO if the "enabled" aspect is bound and its value for the object at _rowIndex_ is NO. Otherwise forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-and returns its response. Note that because the two associations' `enabled` aspects can be bound to different keys, you can limit editability to the whole row or to an individual cell (column) in that row.

---

### tableView:willDisplayCell:forTableColumn:row:

- (void)`tableView:`(NSTableView \*)_aTableView_`willDisplayCell:`(id)_aCell_`forTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Alters the display characteristics for _aCell_ according to the values for the `enabled`, `textColor`, `bold`, and `italic` aspects of the object at _rowIndex_. Then forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-allowing it to adjust _aCell_ based on its own `enabled` aspect.

---

[!](EORecursiveBrowserAssociation-2.md)
[!](EOTextAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
