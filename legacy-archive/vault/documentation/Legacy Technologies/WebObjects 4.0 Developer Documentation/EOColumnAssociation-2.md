---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOColumnAssociation.html
archived_at: '2026-07-18T01:28:45.468210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAssociation-4.md)
[!](EOComboBoxAssociation-2.md)

---

# EOColumnAssociation

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

An EOColumnAssociation object cooperates with an EOTableViewAssociation to display values in a column of an NSTableView (Application Kit). A column association links an NSTableColumn (Application Kit) to a single attribute of all displayed objects in an EODisplayGroup. The value of each object is displayed in its corresponding row.

The EOTableViewAssociation receives target, delegate, and data source messages from the table view, and forwards them as needed to the appropriate column association. Column associations provide values for the cells of each NSTableColumn, and also accept edited values to set in their display groups.

EOColumnAssociations provide values using NSTableView's DataSource methods

---

tableView:setObjectValue:forTableColumn:row:
and

---

tableView:objectValueForTableColumn:
. This allows values with non-string representations to be displayed. For example, if an NSImageCell (Application Kit) is used as an NSTableColumn's data cell, an EOColumnAssociation can be used to display NSImages (Application Kit) in the NSTableView.

| __Usable With__ |
| NSTableColumn (Application Kit) |

```
```

| __Aspects__ | __Aspects__ |
| value | An attribute of the objects, displayed in each row of the NSTableColumn. |
| enabled | A boolean attribute of the objects, which determines whether each object's value cell is editable. Note that because EOTableViewAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| identifier | An EOColumnAssociations sets itself as the identifer of its NSTableColumn. (Note: This key isn't formally reserved by the `objectKeysTaken` method, as Interface Builder doesn't treat it as an outlet.) |

```
```


---

## Example

To display the last and first names of objects in a Talent display group, in Interface Builder, Control-drag a connection from the last name column to the display group. Select EOColumnAssociation in the Connections inspector, and bind the `value` aspect to the "lastName" key (this automatically creates an EOTableViewAssociation to manage the individual columns). Repeat to set up a column association for the first name. Now when you run the application, the last and first names of each Talent object in the display group's `displayedObjects` array are put in the correponding row.

---

## Method Types

**Sorting rows**

**- setSortingSelector:

**- sortingSelector****

**Table view data source methods**

**- tableView:setObjectValue:forTableColumn:row:

**- tableViewObjectValueForLocationtableView:
objectValueForTableColumn:row:****

**Table view delegate methods**

**- tableView:shouldEditTableColumn:row:

**- tableView:willDisplayCell:forTableColumn:row:****

**Control delegate methods**

**- controlDidFailToFormatStringErrorDescriptioncontrol:
didFailToFormatString:errorDescription:

**- control:isValidObject:

**- control:textShouldBeginEditing:******

---

## Instance Methods

---

### setSortingSelector:

- (void)`setSortingSelector:`(SEL)_aSelector_

Sets the method selector used to sort rows to _aSelector_, one of:

- EOCompareAscending
- EOCompareDescending
- EOCompareCaseInsensitiveAscending
- EOCompareCaseInsensitiveDescending
- `nil` (to tell the receiver not to sort)

For more information on these selectors, see the section "Comparison Methods" in the EOSortOrdering class specification (EOControl). Additionally, for details on the sorting methods themselves, see the `compare...` methods in the Value Class Additions specification.

If the EOTableViewAssociation for the receiver's NSTableView (Application Kit) sorts its rows, it applies this method as needed to sort them. The default sorting selector is EOCompareAscending.

---

### sortingSelector

- (SEL)`sortingSelector`

Returns the method selector used to sort rows, or `nil` if the column isn't sorted.

# Data Source and Delegate Methods

These methods are forwarded by the corresponding NSTableView's EOTableViewAssociation to the appropriate EOColumnAssociation.

---

### control:didFailToFormatString:errorDescription:

- (BOOL)`control:`(NSControl \*)_aTableView_`didFailToFormatString:`(NSString \*)_aString_`errorDescription:`(NSString \*)_errorDescription_

Invokes `shouldEndEditingForAspect:invalidInput:errorDescription:` (defined by EOAssociation) and returns the result.

---

### control:isValidObject:

- (BOOL)`control:`(NSControl \*)_aTableView_`isValidObject:`(id)_anObject_

Saves the value of any cell being edited using `setValue:forAspect:`, and if successful sends an `associationDidEndEditing:` message to the receiver's EODisplayGroup. Returns YES if successful (or if no changes need be saved), NO if unsuccessful.

---

### control:textShouldBeginEditing:

- (BOOL)`control:`(NSControl \*)_aTableView_`textShouldBeginEditing:`(NSText \*)_fieldEditor_

Sends an `associationDidBeginEditing:` message to the receiver's EODisplayGroup and returns YES.

---

### tableView:objectValueForTableColumn:row:

- (id)`tableView:`(NSTableView \*)_aTableView_`objectValueForTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Returns the value of the property of the object at _rowIndex_ bound to the `value` aspect.

---

### tableView:setObjectValue:forTableColumn:row:

- (void)`tableView:`(NSTableView \*)_aTableView_`setObjectValue:`(id)_value_`forTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Sets the property of the object at _rowIndex_ bound to the `value` aspect to _value_.

---

### tableView:shouldEditTableColumn:row:

- (BOOL)`tableView:`(NSTableView \*)_aTableView_`shouldEditTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Returns NO if the `enabled` aspect is bound and its value for the object at _rowIndex_ is NO. Otherwise returns YES. Note that because the `enabled` aspects of EOTableViewAssociation and EOColumnAssociation can be bound to different keys, you can limit editability to the whole row or to an individual cell (column) in that row.

---

### tableView:willDisplayCell:forTableColumn:row:

- (void)`tableView:`(NSTableView \*)_aTableView_`willDisplayCell:`(id)_aCell_`forTableColumn:`(NSTableColumn \*)_aTableColumn_`row:`(int)_rowIndex_

Alters the display characteristics for _aCell_ according to the values for the `enabled` aspect of the object at _rowIndex_.

---

[!](EOAssociation-4.md)
[!](EOComboBoxAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
