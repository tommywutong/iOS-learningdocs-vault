---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTableViewAssociation.html
archived_at: '2026-07-15T08:11:45.059713Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTableViewAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl)
> : NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)

> **__Package:__**
> : com.apple.yellow.eointerface

---

## Class Description

---

An EOTableViewAssociation object manages the individual EOColumnAssociations
between an NSTableView (Application Kit) and an EODisplayGroup.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eointerface package. |

An EOTableViewAssociation can sort the objects in the display
group by the left-to-right order of the table columns. The first
EOColumnAssociation to be bound to a table view automatically creates
the EOTableViewAssociation; you should rarely need to do so yourself.

An EOTableViewAssociation receives data source and delegate
messages from the table view, some of which it handles itself, and
some of which it forwards to the appropriate EOColumnAssociations.
For more information, see the EOColumnAssociation class specification.

|  |
| --- |
| __Usable With__ |
| NSTableView |

|  |
| --- |
| __Aspects__ |
| source | Bound to the EODisplayGroup providing objects. This aspect doesn't use a key. |
| enabled | A boolean attribute of the objects, which determines whether each object's row is editable. Note that because EOColumnAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| textColor | An NSColor attribute of the objects, which determines the color of text for each object's row in the NSTableView. |
| bold | A boolean attribute of the objects, which determines whether each objects row is displayed in bold or regular weight text. |
| italic | A boolean attribute of the objects, which determines whether each objects row is displayed in italic or normal angle text. |

|  |
| --- |
| __Object Keys Taken__ |
| dataSource | An EOTableViewAssociation responds to some data source messages and forwards others to the appropriate EOColumnAssociation. |
| delegate | An EOTableViewAssociation forwards delegate messages to the appropriate EOColumnAssociations. |
| target | Reserved, but not used. |

## Example

For an example of using an EOTableViewAssociation, see the
EOColumnAssociation class specification.

## Method Types

---

> **Setting up a table view
> association**
> : [bindToTableView](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vdbmjwgkvtjmv3uc43tn5rwsylunfxw4l3cnfxgivdpkrqwe3dfkzuwk5y)
>
> **Sorting**
> : [setSortsByColumnOrder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5zwk5ctn5zhi42cpfbw63dvnvxe64temvza)
> : [sortsByColumnOrder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5zw64tuonbhsq3pnr2w23spojsgk4q)
>
> **Accessing the active
> EOColumnAssociation**
> : [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5swi2lunfxgoqltonxwg2lboruw63q)
>
> **Table view data source
> methods**
> : [numberOfRowsInTableView](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5xhk3lcmvze6zssn53xgslokrqwe3dfkzuwk5y)
> : [tableViewSetObjectValueForLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of52gcytmmvlgszlxknsxit3cnjswg5cwmfwhkzkgn5zey33dmf2gs33o)
> : [tableViewObjectValueForLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of52gcytmmvlgszlxj5rguzldorlgc3dvmvdg64smn5rwc5djn5xa)
>
> **Table view delegate methods**
> : [tableViewShouldEditLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of52gcytmmvlgszlxknug65lmmrcwi2lujrxwgylunfxw4)
> : [tableViewWillDisplayCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of52gcytmmvlgszlxk5uwy3cenfzxa3dbpfbwk3dm)
>
> **Table view notification
> methods**
> : [tableViewSelectionDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of52gcytmmvlgszlxknswyzldoruw63senfseg2dbnztwk)
>
> **Control delegate methods**
> : [controlDidFailToFormatStringErrorDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5rw63tuojxwyrdjmrdgc2lmkrxum33snvqxiu3uojuw4z2fojzg64semvzwg4tjob2gs33o)
> : [controlIsValidObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5rw63tuojxwysltkzqwy2lej5rguzldoq)
> : [controlTextShouldBeginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5rw63tuojxwyvdfpb2fg2dpovwgiqtfm5uw4rlenf2gs3th)

## Constructors

---

### EOTableViewAssociation

`public EOTableViewAssociation(Object  aDisplayObject)`

Creates a new EOTableViewAssociation to manage
EOColumnAssociations associated with  _aDisplayObject,_
an NSTableView (Application Kit).

You normally set up associations
with the Interface Builder application, in which case you don't
need to create them programmatically. However, if you do create
them up programmatically, setting them up is a multi-step process.
After creating an association, you must bind its aspects and establish
its connections.

__See Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

## Static Methods

---

### bindToTableView

`public static void bindToTableView(
com.apple.yellow.application.NSTableView  aTableView,
EODisplayGroup  aDisplayGroup)`

Creates an EOTableViewAssociation, binding  _aTableView_ to  _aDisplayGroup,_
if there isn't already a table view association for  _aTableView._
EOColumnAssociation's `establishConnection` invokes
this method to guarantee the presence of a coordinating EOTableViewAssociation.

---

## Instance Methods

---

### controlDidFailToFormatStringErrorDescription

`public boolean controlDidFailToFormatStringErrorDescription(
com.apple.yellow.application.NSControl  aTableView,
String  aString,
String  errorDescription)`

Forwards the message to the receiver's editing
association.

__See Also:__  [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5swi2lunfxgoqltonxwg2lboruw63q)

---

### controlIsValidObject

`public boolean controlIsValidObject(
com.apple.yellow.application.NSControl  aTableView,
Object  anObject)`

Forwards the message to the receiver's editing
association.

__See Also:__  [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5swi2lunfxgoqltonxwg2lboruw63q)

---

### controlTextShouldBeginEditing

`public boolean controlTextShouldBeginEditing(
com.apple.yellow.application.NSControl  aTableView,
com.apple.yellow.application.NSText  fieldEditor)`

Forwards the message to the receiver's editing
association.

__See Also:__  [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfkzuwk52bonzw6y3jmf2gs33of5swi2lunfxgoqltonxwg2lboruw63q)

---

### editingAssociation

`public EOColumnAssociation editingAssociation()`

Returns the EOColumnAssociation for the NSTableView
cell being edited, or null if no cell is being edited.

---

### numberOfRowsInTableView

`public int numberOfRowsInTableView(com.apple.yellow.application.NSTableView  aTableView)`

Returns the number of displayed objects in the
receiver's EODisplayGroup.

__See Also:__  [displayedObjects](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) (EODisplayGroup)

---

### setSortsByColumnOrder

`public void setSortsByColumnOrder(boolean  flag)`

Controls whether the receiver applies a sort
ordering to its EODisplayGroup. If  _flag_ is true,
it builds EOSortOrderings (EOControl) for each of the EOColumnAssociations,
collects them into an NSArray based on the left-to-right order of
the columns, and assigns them to the display group with [setSortOrderings](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y). If  _flag_ is false,
it doesn't alter the sort ordering of the display group.

An
EOTableViewAssociation assigns sort orderings based on the left
to right order of the table columns, and reassigns them whenever
the user moves a column.

__See Also:__  [sortingSelector](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOColumnAssociation.html#//apple_ref/java/instm/EOColumnAssociation/sortingSelector) (EOColumnAssociation)

---

### sortsByColumnOrder

`public boolean sortsByColumnOrder()`

Returns true if the receiver assigns EOSortOrderings
(EOControl) to its EODisplayGroup based on the sorting selectors
of its EOColumnAssociations, false if it doesn't alter the display
group's sort ordering.

---

### tableViewObjectValueForLocation

`public Object tableViewObjectValueForLocation(
com.apple.yellow.application.NSTableView  aTableView,
com.apple.yellow.application.NSTableColumn  aTableColumn,
int  rowIndex)`

Forwards the message to  _aTableColumn_ 's
identifier-assumed to be the EOColumnAssociation bound to that
column-so that it can provide the value.

---

### tableViewSelectionDidChange

`public void tableViewSelectionDidChange(NSNotification  aNotification)`

Updates the receiver's EODisplayGroup based
on the new selection in the table view.

__See
Also:__  [setSelectionIndexes](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq) (EODisplayGroup)

---

### tableViewSetObjectValueForLocation

`public void tableViewSetObjectValueForLocation(
com.apple.yellow.application.NSTableView  aTableView,
Object  value,
com.apple.yellow.application.NSTableColumn  aTableColumn,
int  rowIndex)`

Forwards the message to  _aTableColumn_ 's
identifier-assumed to be the EOColumnAssociation bound to that
column-so that it can set the value.

---

### tableViewShouldEditLocation

`public boolean tableViewShouldEditLocation(
com.apple.yellow.application.NSTableView  aTableView,
com.apple.yellow.application.NSTableColumn  aTableColumn,
int  rowIndex)`

Returns false if the `enabled` aspect
is bound and its value for the object at  _rowIndex_ is 0.
Otherwise forwards the message to  _aTableColumn_ 's
identifier-assumed to be the EOColumnAssociation bound to that
column-and returns its response. Note that because the two associations' `enabled` aspects
can be bound to different keys, you can limit editability to the
whole row or to an individual cell (column) in that row.

---

### tableViewWillDisplayCell

`public void tableViewWillDisplayCell(
com.apple.yellow.application.NSTableView  aTableView,
Object  aCell,
com.apple.yellow.application.NSTableColumn  aTableColumn,
int  rowIndex)`

Alters the display characteristics for  _aCell_ according
to the values for the `enabled`, `textColor`, `bold`,
and `italic` aspects of the object at  _rowIndex._
Then forwards the message to  _aTableColumn_ 's
identifier-assumed to be the EOColumnAssociation bound to that
column-allowing it to adjust  _aCell_ based
on its own `enabled` aspect.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
