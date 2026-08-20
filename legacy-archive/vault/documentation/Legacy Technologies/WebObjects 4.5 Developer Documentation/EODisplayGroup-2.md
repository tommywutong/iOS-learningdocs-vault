---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EODisplayGroup.html
archived_at: '2026-07-15T08:11:45.442046Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EODisplayGroup

> **__Inherits
> from:__**
> : NSObject (Yellow Box)Object (Java Client)

> **__Conforms to:__**
> : NSCoding
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EODisplayGroup.h

---

### Class at a Glance

---

An EODisplayGroup collects an array of objects
from an EODataSource, and works with a group of EOAssociation objects
to display and edit the properties of those objects.

#### Principal Attributes

---

- Array of objects supplied by an EODataSource
- EOQualifier and EOSortOrderings to filter the objects for
  display
- Array of selection indexes
- Delegate

#### Commonly Used Methods

---

|  |  |
| --- | --- |
| [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq) | Returns all objects in the EODisplayGroup. |
| [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) | Returns the subset of all objects made available for display. |
| [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq) | Returns the selected objects. |
| [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2) | Sets a filter that limits the objects displayed. |
| [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq) | Sets the ordering used to sort the objects. |
| [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) | Filters, sorts, and redisplays the objects. |
| [- insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a) | Creates a new object and inserts it into the EODataSource. |

## Class Description

---

An EODisplayGroup is the basic user interface manager for
an Enterprise Objects Framework or Java Client application. It collects
objects from an EODataSource, filters and sorts them, and maintains
a selection in the filtered subset. It interacts with user interface
objects and other display objects through EOAssociations, which
bind the values of objects to various aspects of the display objects.

An EODisplayGroup manipulates its EODataSource by sending
it __fetchObjects__, __insertObject:__,
and other messages, and registers itself as an editor and message
handler of the EODataSource's EOEditingContext. The EOEditingContext
allows the EODisplayGroup to intercede in certain operations, as
described in the EOEditors and EOMessageHandlers informal protocol specifications (both protocols
are defined in EOControl). EODisplayGroup implements all the methods
of these informal protocols; see their specifications for more information.

Most of an EODisplayGroup's interactions are with its associations,
its EODataSource, and its EOEditingContext. See the EOAssociation,
EODataSource, and EOEditingContext class specifications for more
information on these interactions.

## Creating an EODisplayGroup

You create most EODisplayGroups in Interface Builder, by dragging
an entity icon from the EOModeler application, which creates an
EODisplayGroup with an EODatabaseDataSource (EODistributedDataSource,
for Java Client applications), or by dragging an EODisplayGroup
with no EODataSource from the EOPalette. EODisplayGroups with EODataSources
operate independent of other EODisplayGroups, while those without
EODataSources must be set up in a master-detail association with
another EODisplayGroup.

To create an EODisplayGroup programmatically, simply initialize
it and set its EODataSource:

> ```
> EODataSource *myDataSource;    /* Assume this exists. */
> EODisplayGroup *myDisplayGroup;
>
> myDisplayGroup = [[EODisplayGroup alloc] init];
> [myDisplayGroup setDataSource:myDataSource];
> ```

After creating the EODisplayGroup, you can add associations
as described in the EOAssociation class specification.

## Getting Objects

Since an EODisplayGroup isn't much use without objects to
manage, the first thing you do with an EODisplayGroup is send it
a fetch message. You can use the basic [fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua) method; the [fetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnudu) action method, which can be
invoked by a control in the EODisplayGroup's nib file; or you
can configure the EODisplayGroup in Interface Builder to fetch automatically
when its nib file is loaded. These methods all ask the EODisplayGroup's
EODataSource to fetch from its persistent store with a __fetchObjects__ message.

## Filtering and Sorting

An EODisplayGroup's fetched objects are available through
its [allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq) method.
These objects are treated only as candidates for display, however.
The array of objects actually displayed is filtered and sorted by
the EODisplayGroup's delegate, or by a qualifier and sort ordering
array. You set the qualifier and sort orderings using the [setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2) and [setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq) methods.
The [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) method
returns this filtered and sorted array; index arguments to other
EODisplayGroup methods are defined in terms of this array.

If the EODisplayGroup has a delegate that responds to [displayGroup:displayArrayForObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a),
it invokes this method rather than using its own qualifier and sort
ordering array. The delegate is then responsible for filtering the
objects and returning a sorted array. If the delegate only needs
to perform one of these steps, it can get the qualifier or sort
orderings from the EODisplayGroup and apply either itself using the
NSArray methods __filteredArrayUsingQualifier:__ and __sortedArrayUsingKeyOrderArray:__,
which are added by the control layer.

If you change the qualifier or sort ordering, or alter the
delegate in a way that changes how it filters and sorts the EODisplayGroup's
objects, you can send [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) to
the EODisplayGroup to get it to refilter and resort its objects.
Note that this doesn't cause the EODisplayGroup to refetch.

## Changing and Examining the Selection

An EODisplayGroup keeps a selection in terms of indexes into
the array of displayed objects. EOAssociations that display values
for multiple objects are responsible for updating the selection
in their EODisplayGroups according to user actions on their display
objects. This is typically done with the [setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a) method.
Other methods available for indirect manipulation of the selection are
the action methods [selectNext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2a) and [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom),
as well as [selectObjectsIdenticalTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45a) and [selectObjectsIdenticalTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45a).

To get the selection, you can use the [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg) method,
which returns an array of NSNumbers, or [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq), which returns an
array containing the selected objects themselves. Another method, [selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq),
returns the first selected object if there is one.

## The Delegate

EODisplayGroup offers a number of methods for its delegate
to implement; if the delegate does, it invokes them as appropriate.
Besides the aforementioned [displayGroup:displayArrayForObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a), there
are methods that inform the delegate that the EODisplayGroup has
fetched, created an object (or failed to create one), inserted or
deleted an object, changed the selection, or set a value for a property. There
are also methods that request permission from the delegate to perform
most of these same actions. The delegate can return YES to permit
the action or NO to deny it. For more information, see each method's
description in the [EODisplayGroup Delegate](EODisplayGroup%20Delegate.md#apple-inbecrcbi5eek) informal
protocol specification.

## Methods for Use by EOAssociations

While most of your application code interacts with objects
directly, EODisplayGroup also defines methods for its associations
to access properties of individual objects without having to know
anything about which methods they implement. Accessing properties
through the EODisplayGroup offers associations the benefit of automatic
validation, as well.

Associations access objects by index into the displayed objects
array, or by object identifier. [valueForObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoraxislomrsxqotlmv4tu) returns
the value of a named property for the object at a given index, and [setValue:forObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uif2es3temv4du23fpe5a) sets
it. Similarly, [valueForObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoq5gwzlzhi) and [setValue:forObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2)access
the objects by object identifier. EOAssociations can also get and
set values for the first object in the selection using [selectedObjectValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorlgc3dvmvdg64slmv4tu) and [setSelectedObjectValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5cwmfwhkzj2mzxxes3fpe5a).

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__

## Method Types

---

> **Creating instances**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3tjoq)
>
> **Configuring behavior**
> : [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq)
> : [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe)
> : [- fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnugk42pnzgg6yle)
> : [- queryBindingValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4ue2lomruw4z2wmfwhkzlt)
> : [- queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33skzqwy5lfom)
> : [- selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi42gnfzhg5cpmjvgky3uifthizlsizsxiy3i)
> : [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2)
> : [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a)
> : [- setFetchesOnLoad:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluizsxiy3imvzu63smn5qwioq)
> : [- setQueryBindingValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wk4tzijuw4zdjnztvmylmovsxgoq)
> : [- setQueryOperatorValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wk4tzj5ygk4tborxxevtbnr2wk4z2)
> : [- setSelectsFirstObjectAfterFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorzum2lson2e6ytkmvrxiqlgorsxertforrwqoq)
> : [- setUsesOptimisticRefresh:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukvzwk42pob2gs3ljon2gsy2smvthezltna5a)
> : [- setValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4tu)
> : [- usesOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk43fonhxa5djnvuxg5djmnjgkztsmvzwq)
> : [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)
>
> **Setting the data source**
> : [- setDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirqxiyktn52xey3fhi)
> : [- dataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwiylumfjw65lsmnsq)
>
> **Setting the qualifier
> and sort ordering**
> : [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2)
> : [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi)
> : [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq)
> : [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)
>
> **Managing queries**
> : [- qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom)
> : [- setEqualToQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluivyxkylmkrxvc5lfoj4vmylmovsxgoq)
> : [- equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt)
> : [- setGreaterThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlui5zgkylumvzfi2dbnzixkzlspflgc3dvmvztu)
> : [- greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y)
> : [- setLessThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujrsxg42unbqw4ulvmvzhsvtbnr2wk4z2)
> : [- lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom)
> : [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa)
> : [- qualifyDisplayGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa5a)
> : [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi)
> : [- qualifyDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzj2)
> : [- enterQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3tumvzfc5lfoj4u233emu5a)
> : [- inQueryMode](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3srovsxe6knn5sgk)
> : [- setInQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujfxfc5lfoj4u233emu5a)
> : [- enabledToSetSelectedObjectValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3tbmjwgkzcun5jwk5ctmvwgky3umvse6ytkmvrxivtbnr2wkrtpojfwk6j2)
>
> **Fetching objects from
> the data source**
> : [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua)
> : [- fetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnudu)
>
> **Getting the objects**
> : [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq)
> : [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg)
>
> **Updating display of values**
> : [- redisplay](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)
> : [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y)
>
> **Setting the objects**
> : [- setObjectArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluj5rguzldoraxe4tbpe5a)
>
> **Changing the selection**
> : [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)
> : [- selectObjectsIdenticalTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45a)
> : [- selectObjectsIdenticalTo:selectFirstOnNoMatch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45hgzlmmvrxirtjojzxit3ojzxu2ylumnudu)
> : [- selectObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5b2)
> : [- clearSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwg3dfmfzfgzlmmvrxi2lpny)
> : [- selectNext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2a)
> : [- selectNext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2du)
> : [- selectPrevious](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom)
> : [- selectPrevious:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom5a)
>
> **Examining the selection**
> : [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg)
> : [- selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq)
> : [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq)
>
> **Inserting and deleting
> objects**
> : [- delete:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlmmv2gkoq)
> : [- deleteObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlmmv2gkt3cnjswg5cborew4zdfpa5a)
> : [- deleteSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlmmv2gku3fnrswg5djn5xa)
> : [- insert:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhioq)
> : [- insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhizlej5rguzldorcgkztbovwhivtbnr2wk4y) (Yellow
> Box applications only)
> : [- insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a)
> : [- insertObject:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5b2mf2es3temv4du)
> : [- setInsertedObjectDefaultValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujfxhgzlsorswit3cnjswg5cemvtgc5lmorlgc3dvmvztu)(Yellow
> Box applications only)
>
> **Adding keys**
> : [- setLocalKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujrxwgylmjnsxs4z2)
> : [- localKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwy33dmfwewzlzom)
>
> **Getting the associations**
> : [- observingAssociations](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxw6yttmvzhm2lom5axg43pmnuwc5djn5xhg)
>
> **Setting the delegate**
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswyzlhmf2gkoq)
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlmmvtwc5df)
>
> **Changing values from
> associations**
> : [- setSelectedObjectValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5cwmfwhkzj2mzxxes3fpe5a)
> : [- selectedObjectValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorlgc3dvmvdg64slmv4tu)
> : [- setValue:forObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2)
> : [- valueForObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoq5gwzlzhi)
> : [- setValue:forObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uif2es3temv4du23fpe5a)
> : [- valueForObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoraxislomrsxqotlmv4tu)
>
> **Editing by associations**
> : [- associationDidBeginEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrbgkz3jnzcwi2lunfxgooq)
> : [- association:failedToValidateValue:forKey:object:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4otgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lfhjtg64slmv4tu33cnjswg5b2mvzhe33sirsxgy3snfyhi2lpny5a)
> : [- associationDidEndEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrcw4zcfmruxi2lom45a)
> : [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2bonzw6y3jmf2gs33o)
> : [- endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3teivsgs5djnztq)
>
> **Querying changes for
> associations**
> : [- contentsChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwg33oorsw45dtinugc3thmvsa)
> : [- selectionChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzbwqylom5swi)
> : [- updatedObjectIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkzcpmjvgky3ujfxgizly)
>
> **Interacting with the
> EOEditingContext**
> : [- editorHasChangesForEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjorxxesdbonbwqylom5sxgrtpojcwi2lunfxgoq3pnz2gk6duhi)
> : [- editingContextWillSaveChanges:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a)
> : [- editingContext:presentErrorMessage:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2dn5xhizlyoq5ha4tfonsw45cfojzg64snmvzxgylhmu5a)

## Class Methods

---

### globalDefaultForValidatesChangesImmediately

`+ (BOOL)globalDefaultForValidatesChangesImmediately`

Returns `YES` if
the default behavior for new display group instances is to immediately
handle validation errors, or `NO` if
the default behavior leaves errors for the EOEditingContext to handle
when saving changes.

__See Also:__  [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)

---

### globalDefaultStringMatchFormat

`+ (NSString *)globalDefaultStringMatchFormat`

Returns the default string match format string
used by display group instances.

__See Also:__  [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq)

---

### globalDefaultStringMatchOperator

`+ (NSString *)globalDefaultStringMatchOperator`

Returns the default string match operator used
by display group instances.

__See Also:__  [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe)

---

### setGlobalDefaultForValidatesChangesImmediately:

`+ (void)setGlobalDefaultForValidatesChangesImmediately:(BOOL)flag`

Sets the default behavior display group instances
use when they encounter a validation error. If _flag_ is `YES`,
the default behavior is for display groups to immediately present
an attention panel indicating a validation error. If _flag_ is `NO`,
the default behavior if for display groups to leave validation errors
to be handled when changes are saved. By default, display groups
don't validate changes immediately.

__See
Also:__  - __saveChanges__ (EOEditingContext), [- setValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4tu)

---

### setGlobalDefaultStringMatchFormat:

`+ (void)setGlobalDefaultStringMatchFormat:(NSString
*)format`

Sets the default string match format to be used
by display group instances. The default format string for pattern
matching is "__%@\*__".

__See
Also:__  [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2)

---

### setGlobalDefaultStringMatchOperator:

`+ (void)setGlobalDefaultStringMatchOperator:(NSString
*)op`

Sets the default string match operator to be
used by display group instances. The default operator is case insensitive
like.

__See Also:__  [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a)

---

## Instance Methods

---

### allObjects

`- (NSArray *)allObjects`

Returns all of the objects collected by the
receiver.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua)

---

### associationDidBeginEditing:

`- (void)associationDidBeginEditing:(EOAssociation
*)anAssociation`

Invoked by _anAssociation_ when
its display object begins editing to record that EOAssociation as
the editing association.

__See Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2bonzw6y3jmf2gs33o), [- endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3teivsgs5djnztq), [- association:failedToValidateValue:forKey:object:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4otgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lfhjtg64slmv4tu33cnjswg5b2mvzhe33sirsxgy3snfyhi2lpny5a)

---

### associationDidEndEditing:

`- (void)associationDidEndEditing:(EOAssociation
*)anAssociation`

Invoked by _anAssociation_ to
clear the editing association. If _anAssociation_ is
the receiver's editing association, clears the editing association.
Otherwise does nothing.

__See Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2bonzw6y3jmf2gs33o), [- endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3teivsgs5djnztq), [- association:failedToValidateValue:forKey:object:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4otgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lfhjtg64slmv4tu33cnjswg5b2mvzhe33sirsxgy3snfyhi2lpny5a)

---

### association:failedToValidateValue:forKey:object:errorDescription:

`- (BOOL)association:(EOAssociation
*)anAssociation
failedToValidateValue:(NSString
*)value
forKey:(NSString *)key
object:(id)anObject
errorDescription:(NSString *)errorDescription`

Invoked by _anAssociation_ from
its [shouldEndEditingForAspect:invalidInput:errorDescription:index:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5gs3temv4du) method
to let the receiver handle a validation error. This method opens
an attention panel with _errorDescription_ as
the message and returns NO.

__See Also:__  [- displayGroup:shouldDisplayAlertWithTitle:message:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3deiruxg4dmmf4uc3dfoj2fo2lunbkgs5dmmu5g2zltonqwozj2) ( [EODisplayGroup Delegate](EODisplayGroup%20Delegate.md#apple-inbecrcbi5eek))

---

### clearSelection

`- (BOOL)clearSelection`

Invokes [setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a) to
clear the selection, returning YES on success and NO on failure.

---

### contentsChanged

`- (BOOL)contentsChanged`

Returns YES if the receiver's array of objects
has changed and not all observers have been notified, NO otherwise.
EOAssociations use this in their [subjectChanged](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zxkytkmvrxiq3imfxgozle) methods to determine
what they need to update.

__See Also:__  [- selectionChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzbwqylom5swi), [- updatedObjectIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkzcpmjvgky3ujfxgizly)

---

### dataSource

`- (EODataSource *)dataSource`

Returns the receiver's EODataSource.

__See
Also:__  [- setDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirqxiyktn52xey3fhi)

---

### defaultStringMatchFormat

`- (NSString *)defaultStringMatchFormat`

Returns the format string that specifies how
pattern matching will be performed on string values in the query
dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom)).
If a key in the __queryMatch__ dictionary does
not have an associated operator in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33skzqwy5lfom) dictionary, then
its value is matched using pattern matching, and the format string
returned by this method specifies how it will be matched.

__See
Also:__  [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe), [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2)

---

### defaultStringMatchOperator

`- (NSString *)defaultStringMatchOperator`

Returns the operator used to perform pattern
matching for string values in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom)).
If a key in one of the query dictionaries does not have an associated
operator in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33skzqwy5lfom) dictionary,
then the operator returned by this method is used to perform pattern
matching.

__See Also:__  [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq), [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate.

__See
Also:__  [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswyzlhmf2gkoq)

---

### delete:

`- (void)delete:(id)sender`

This action method invokes [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlmmv2gku3fnrswg5djn5xa).

---

### deleteObjectAtIndex:

`- (BOOL)deleteObjectAtIndex:(unsigned
int)index`

Attempts to delete the object at _index_,
returning YES if successful and NO if not. Checks with the delegate using [displayGroup:shouldDeleteObject:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3deirswyzlumvhwe2tfmn2du).
If the delegate returns NO, this method fails and returns NO. If successful,
sends the delegate a [displayGroup:didDeleteObject:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfseizlmmv2gkt3cnjswg5b2) message.

This
method performs the delete by sending __deleteObject:__ to
the EODataSource. If that message raises an exception, this method
fails and returns NO.

---

### deleteSelection

`- (BOOL)deleteSelection`

Attempts to delete the selected objects, returning YES if
successful and NO if not.

---

### displayedObjects

`- (NSArray *)displayedObjects`

Returns the objects that should be displayed
or otherwise made available to the user, as filtered by the receiver's
delegate or by its qualifier and sort ordering.

__See
Also:__  [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq), [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y), [- displayGroup:displayArrayForObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a) ( [EODisplayGroup Delegate](EODisplayGroup%20Delegate.md#apple-inbecrcbi5eek)), [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)

---

### editingAssociation

`- (EOAssociation *)editingAssociation`

Returns the EOAssociation editing a value if
there is one, NO if there isn't.

__See Also:__  [- associationDidBeginEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrbgkz3jnzcwi2lunfxgooq), [- associationDidEndEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrcw4zcfmruxi2lom45a)

---

### editingContext:presentErrorMessage:

`- (void)editingContext:(EOEditingContext
*)anEditingContext
presentErrorMessage:(NSString
*)errorMessage`

Invoked by _anEditingContext_ as
part of the EOMessageHandlers informal protocol, this method presents
an attention panel with _errorMessage_ as
the message to display.

---

### editingContextWillSaveChanges:

`- (void)editingContextWillSaveChanges:(EOEditingContext
*)anEditingContext`

Invoked by anEditingContext in its __saveChanges__ method
as part of the EOEditors informal protocol, this method allows the
EODisplayGroup to prohibit a save operation. EODisplayGroup's
implementation of this method invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3teivsgs5djnztq), and raises an NSInternalInconsistencyException if
it returns NO. Thus, if there's an association that refuses to
end editing, anEditingContext doesn't save changes.

---

### editorHasChangesForEditingContext:

`- (BOOL)editorHasChangesForEditingContext:(EOEditingContext
*)anEditingContext`

Invoked by _anEditingContext_ as
part of the EOEditors informal protocol, this method returns NO if
any association is editing, YESotherwise.

__See
Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2bonzw6y3jmf2gs33o), [- associationDidBeginEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrbgkz3jnzcwi2lunfxgooq), [- associationDidEndEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrcw4zcfmruxi2lom45a)

---

### enabledToSetSelectedObjectValueForKey:

`- (BOOL)enabledToSetSelectedObjectValueForKey:(NSString
*)key`

Returns YES to indicate that a single value
association (such as an EOControlAssociation for a NSTextField)
should be enabled for setting _key_, NO otherwise.
Normally this is the case if the receiver has a selected object.
However, if _key_ is a special query
key (for example, "@query=.name"), then the control should be
enabled even without a selected object.

---

### endEditing

`- (BOOL)endEditing`

Attempts to end any editing taking place. If
there's no editing association or if the editing association responds YES to
an __endEditing__ message, returns YES. Otherwise
returns NO.

__See Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwkzdjoruw4z2bonzw6y3jmf2gs33o)

---

### enterQueryMode:

`- (void)enterQueryMode:(id)sender`

This action method invokes [setInQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujfxfc5lfoj4u233emu5a) with
an argument of YES.

---

### equalToQueryValues

`- (NSDictionary *)equalToQueryValues`

Returns the receiver's dictionary of equalTo
query values. This dictionary is typically manipulated by associations
bound to keys of the form @query=.propertyName. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the lessThan and greaterThan dictionaries
to construct qualifiers.

__See Also:__  [- setEqualToQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluivyxkylmkrxvc5lfoj4vmylmovsxgoq), [- greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), [- lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom),

---

### fetch

`- (BOOL)fetch`

Attempts to fetch objects from the EODataSource,
returning YES on success and NO on failure.

Before fetching,
invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3teivsgs5djnztq) and
sends [displayGroupShouldFetch:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xau3in52wyzcgmv2gg2b2) to the delegate,
returning NO if either of these methods does. If both return YES,
sends a __fetchObjects__ message to the receiver's EODataSource
to replace the object array, and if successful sends the delegate
a [displayGroup:didFetchObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfsemzlumnue6ytkmvrxi4z2) message.

---

### fetch:

`- (void)fetch:(id)sender`

This action method invokes [fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua).

---

### fetchesOnLoad

`- (BOOL)fetchesOnLoad`

Returns YES if the receiver fetches automatically
after being loaded from a nib file, NO if it must be told explicitly
to fetch. The default is NO. You can set this behavior in Interface
Builder using the Inspector panel.

__See Also:__  [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua), [- setFetchesOnLoad:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluizsxiy3imvzu63smn5qwioq)

---

### greaterThanQueryValues

`- (NSDictionary *)greaterThanQueryValues`

Returns the receiver's dictionary of greaterThan
query values. This dictionary is typically manipulated by associations
bound to keys of the form @query>.propertyName. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the lessThan and equalTo dictionaries
to construct qualifiers.

__See Also:__  [- setGreaterThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlui5zgkylumvzfi2dbnzixkzlspflgc3dvmvztu), [- lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom), [- equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt)

---

### init

`- (id)init`

Initializes a newly allocated EODisplayGroup.
The new display group then needs to have an EODataSource set with [setDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirqxiyktn52xey3fhi).
This is the designated initializer for the EODisplayGroup class. Returns __self__.

__See
Also:__  [- bindAspect:displayGroup:key:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rgs3teifzxazldoq5gi2ltobwgc6khojxxk4b2nnsxsoq) (EOAssociation)

---

### inQueryMode

`- (BOOL)inQueryMode`

Returns YES to indicate that the receiver is
in query mode, NO otherwise. In query mode, user interface controls
that normally display values become empty, allowing users to type
queries directly into them (this is also known as a "Query By
Example" interface). In effect, the receiver's "displayedObjects"
are replaced with an empty equalTo query values dictionary. When [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa) or [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi) is
subsequently invoked, the query is performed and the display reverts
to displaying values-this time, the objects returned by the query.

__See
Also:__  [- setInQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujfxfc5lfoj4u233emu5a), [- enterQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3tumvzfc5lfoj4u233emu5a)

---

### insert:

`- (void)insert:(id)sender`

This action method invokes [insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a) with
an index just past the first index in the selection, or 0 if there's
no selection.

---

### insertedObjectDefaultValues

`- (NSDictionary *)insertedObjectDefaultValues`

Returns the default values to be used for newly
inserted objects. The keys into the dictionary are the properties
of the entity that the display group manages. If the dictionary
returned by this method is empty, the __insert...__ method
adds an object that is initially empty. Because the object is empty,
the display group has no value to display on the HTML page for that
object, meaning that there is nothing for the user to select and
modify. Use the [setInsertedObjectDefaultValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujfxhgzlsorswit3cnjswg5cemvtgc5lmorlgc3dvmvztu) method
to set up a default value so that there is something to display
on the page.

---

### insertObjectAtIndex:

`- (id)insertObjectAtIndex:(unsigned
int)anIndex`

Asks the receiver's EODataSource to
create a new object by sending it a __createObject__ message,
then inserts the new object using [insertObject:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5b2mf2es3temv4du). The EODataSource
createObject method has the effect of inserting the object into
the EOEditingContext.

If a new object can't be created,
this method sends the delegate a [displayGroup:createObjectFailedForDataSource:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotdojswc5dfj5rguzldordgc2lmmvsem33sirqxiyktn52xey3fhi) message
or, if the delegate doesn't respond, opens an attention panel
to inform the user of the error.

__See
Also:__  [- insert:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhioq)

---

### insertObject:atIndex:

`- (void)insertObject:(id)anObject
atIndex:(unsigned int)index`

Inserts _anObject_ into
the receiver's EODataSource and [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) array at _index_,
if possible. This method checks with the delegate before actually
inserting, using [displayGroup:shouldInsertObject:atIndex:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3dejfxhgzlsorhwe2tfmn2duylujfxgizlyhi).
If the delegate refuses, _anObject_ isn't
inserted. After successfully inserting the object, this method informs
the delegate with a [displayGroup:didInsertObject:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfses3ttmvzhit3cnjswg5b2) message,
and selects the newly inserted object. Raises an NSRangeException if _index_ is
out of bounds.

Unlike the [insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a) method, this
method does not insert the object into the EOEditingContext. If
you use this method, you're responsible for inserting the object
into the EOEditingContext yourself.

---

### lessThanQueryValues

`- (NSDictionary *)lessThanQueryValues`

Returns the receiver's dictionary of lessThan
query values. This dictionary is typically manipulated by associations
bound to keys of the form @query<.propertyName. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the greaterThan and equalTo dictionaries
to construct qualifiers.

__See Also:__  [- setLessThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujrsxg42unbqw4ulvmvzhsvtbnr2wk4z2), [- greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), [- equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt)

---

### localKeys

`- (NSArray *)localKeys`

Returns the additional keys that EOAssociations
can be bound to. An EODisplayGroup's basic keys are typically
those of the attributes and relationships of its objects, as defined
by their EOClassDescription through an EOEntity in the model. Local
keys are typically used to form associations with key paths, with
arbitrary methods of objects, or with properties of objects not
associated with an EOEntity. Interface Builder allows the user to
add and remove local keys in the EODisplayGroup Attributes Inspector
panel.

__See Also:__  [- setLocalKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujrxwgylmjnsxs4z2)

---

### observingAssociations

`- (NSArray *)observingAssociations`

Returns all EOAssociations that observe the
receiver's objects.

---

### qualifier

`- (EOQualifier *)qualifier`

Returns the receiver's qualifier, which it
uses to filter its array of objects for display when the delegate doesn't
do so itself.

__See Also:__  [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y), [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2)

---

### qualifierFromQueryValues

`- (EOQualifier *)qualifierFromQueryValues`

Builds a qualifier constructed from entries
in the three query dictionaries: equalTo, greaterThan, and lessThan.
These, in turn, are typically manipulated by associations bound
to keys of the form @query=.firstName, @query>.budget, @query<.budget.

__See
Also:__  [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa), [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi)

---

### qualifyDataSource

`- (void)qualifyDataSource`

Takes the result of [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) and applies
to the receiver's data source. The receiver then sends itself a [fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua) message. If
the receiver is in query mode, query mode is exited. This method differs
from [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa) as
follows: whereas __qualifyDisplayGroup__ performs
in-memory filtering of already fetched objects, __qualifyDataSource__ triggers
a new qualified fetch against the database.

---

### qualifyDataSource:

`- (void)qualifyDataSource:(id)sender`

This action method invokes qualifyDataSource.

---

### qualifyDisplayGroup

`- (void)qualifyDisplayGroup`

Takes the result of [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) and applies
to the receiver using [setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2).
The method [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) is invoked
to refresh the display. If the receiver is in query mode, query
mode is exited.

---

### qualifyDisplayGroup:

`- (void)qualifyDisplayGroup:(id)sender`

This action method invokes qualifyDisplayGroup:.

---

### queryBindingValues

`- (NSDictionary *)queryBindingValues`

Returns a dictionary containing the actual values
that the user wants to query upon. You use this method to perform
a query stored in the model file. Bind keys in this dictionary to
elements on your component that specify query values, then pass
this dictionary to the fetch specification that performs the fetch.

---

### queryOperatorValues

`- (NSDictionary *)queryOperatorValues`

Returns a dictionary of operators to use on
items in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom)).
If a key in a query dictionary also exists in __queryOperatorValues__,
that operator for that key is used.

__See Also:__  [- qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom)

---

### redisplay

`- (void)redisplay`

Notifies all observing associations to redisplay
their values.

__See Also:__  [- observingAssociations](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxw6yttmvzhm2lom5axg43pmnuwc5djn5xhg)

---

### selectedObject

`- (id)selectedObject`

Returns the first selected object in the displayed
objects array, or nil if there's no such object.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg)

---

### selectedObjects

`- (NSArray *)selectedObjects`

Returns the objects selected in the receiver's
displayed objects array.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg)

---

### selectedObjectValueForKey:

`- (id)selectedObjectValueForKey:(NSString
*)key`

Returns the value corresponding to _key_ for
the first selected object in the receiver's displayed objects array,
or nil if exactly one object isn't selected.

__See
Also:__  [- valueForObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoraxislomrsxqotlmv4tu)

---

### selectionChanged

`- (BOOL)selectionChanged`

Returns YES if the selection has changed and
not all observers have been notified, NO otherwise. EOAssociations
use this in their [subjectChanged](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zxkytkmvrxiq3imfxgozle) methods to determine
what they need to update.

__See Also:__  [- contentsChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwg33oorsw45dtinugc3thmvsa)

---

### selectionIndexes

`- (NSArray *)selectionIndexes`

Returns the indexes of the receiver's selected
objects as NSNumbers, in terms of its displayed objects array.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq), [- selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq), [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)

---

### selectNext

`- (BOOL)selectNext`

Attempts to select the object just after the
currently selected one, returning YES if successful and NO if not.
The selection is altered in this way:

- If there
  are no objects, does nothing and returns NO.
- If there's no selection, selects the object at index zero
  and returns YES.
- If the first selected object is the last object in the displayed
  objects array, selects the first object and returns YES.
- Otherwise selects the object after the first selected object.

---

### selectNext:

`- (void)selectNext:(id)sender`

This action method invokes [selectNext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2a).

__See
Also:__  [- selectPrevious:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom5a), [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)

---

### selectObject:

`- (BOOL)selectObject:(id)anObject`

Returns YES to indicate that the receiver has
found and selected anObject, NO if it can't find a match for anObject
(in which case it clears the selection). The selection is performed
on the receiver's [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), not on [allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq).

---

### selectObjectsIdenticalTo:

`- (BOOL)selectObjectsIdenticalTo:(NSArray
*)objects`

Attempts to select the objects in the receiver's
displayed objects array whose ids are equal to those of _objects_,
returning YES if successful and NO otherwise.

---

### selectObjectsIdenticalTo:selectFirstOnNoMatch:

`- (BOOL)selectObjectsIdenticalTo:(NSArray
*)objects
selectFirstOnNoMatch:(BOOL)flag`

Selects the objects in the receiver's displayed
objects array whose __id__s are equal to those
of _objects_, returning YES if successful
and NO otherwise. If no objects in the displayed objects array match _objects_ and _flag_ is YES,
attempts to select the first object in the displayed objects array.

__See
Also:__  [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)

---

### selectPrevious

`- (BOOL)selectPrevious`

Attempts to select the object just before the
presently selected one, returning YES if successful and NO if not.
The selection is altered in this way:

- If there
  are no objects, does nothing and returns NO.
- If there's no selection, selects the object at index zero
  and returns YES.
- If the first selected object is at index zero, selects the
  last object and returns YES.
- Otherwise selects the object before the first selected object.

---

### selectPrevious:

`- (void)selectPrevious:(id)sender`

This action method invokes [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom).

__See
Also:__  [- selectNext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2du), [- redisplay](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)

---

### selectsFirstObjectAfterFetch

`- (BOOL)selectsFirstObjectAfterFetch`

Returns YES if the receiver automatically selects
its first displayed object after a fetch if there was no selection, NO if
it leaves an empty selection as-is.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua), [- setSelectsFirstObjectAfterFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorzum2lson2e6ytkmvrxiqlgorsxertforrwqoq)

---

### setDataSource:

`- (void)setDataSource:(EODataSource
*)aDataSource`

Sets the receiver's EODataSource to _aDataSource_.
In the process, it performs these actions:

- Unregisters __self__ as
  an editor and message handler for the previous EODataSource's EOEditingContext,
  if necessary, and registers __self__ with _aDataSource's_ editing
  context. If the new editing context already has a message handler,
  however, the receiver doesn't assume that role.
- Registers __self__ for `EOObjectsChangedInEditingContextNotification` and `EOInvalidatedAllObjectsInStoreNotification` from
  the new editing context.
- Clears the receiver's array of objects.
- Sends [displayGroupDidChangeDataSource:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xardjmrbwqylom5suiylumfjw65lsmnstu) to
  the delegate if there is one.

__See
Also:__  [- dataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwiylumfjw65lsmnsq)

---

### setDefaultStringMatchFormat:

`- (void)setDefaultStringMatchFormat:(NSString
*)format`

Sets how pattern matching will be performed
on NSString values in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom)).
This format is used for query dictionary properties that have NSString
values and that do not have an associated entry in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33skzqwy5lfom) dictionary.
In these cases, the value is matched using pattern matching and
format specifies how it will be matched.

The default format
string for pattern matching is "__%@\*__"
which means that the string value in the __queryMatch__ dictionary
is used as a prefix. For example, if the query dictionary contains
a value "Jo" for the key "Name", the query returns all records
whose name values begin with "Jo".

__See
Also:__  [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq), [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a)

---

### setDefaultStringMatchOperator:

`- (void)setDefaultStringMatchOperator:(NSString
*)matchOperator`

Sets the operator used to perform pattern matching
for NSString values in the __queryMatch__ dictionary. This
operator is used for properties listed in the query dictionaries
( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom))
that have NSString values and that do not have an associated entry
in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33skzqwy5lfom) dictionary.
In these cases, the operator _matchOperator_ is used
to perform pattern matching.

The default value for the query
match operator is __caseInsensitiveLike__,
which means that the query does not consider case when matching
letters. The other possible value for this operator is __like__,
which matches the case of the letters exactly.

__See
Also:__  [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe), [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2)

---

### setDelegate:

`- (void)setDelegate:(id)anObject`

Sets the receiver's delegate to _anObject_,
without retaining it.

__See Also:__  [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwizlmmvtwc5df)

---

### setEqualToQueryValues:

`- (void)setEqualToQueryValues:(NSDictionary
*)values`

Sets to _values_ the
receiver's dictionary of equalTo query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the lessThan and greaterThan dictionaries
to construct qualifiers.

__See Also:__  [- equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [- setLessThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujrsxg42unbqw4ulvmvzhsvtbnr2wk4z2), [- setGreaterThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlui5zgkylumvzfi2dbnzixkzlspflgc3dvmvztu)

---

### setFetchesOnLoad:

`- (void)setFetchesOnLoad:(BOOL)flag`

Controls whether the receiver automatically
fetches its objects after being loaded from a nib file. If _flag_ is YES it
does; if _flag_ is NO the receiver
must be told explicitly to fetch. The default is NO. You can also
set this behavior in Interface Builder using the Inspector panel.

__See
Also:__  [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua), [- fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnugk42pnzgg6yle)

---

### setGreaterThanQueryValues:

`- (void)setGreaterThanQueryValues:(NSDictionary
*)values`

Sets to _values_ the
receiver's dictionary of greaterThan query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the lessThan and equalTo dictionaries
to construct qualifiers.

__See Also:__  [- greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), [- setLessThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlujrsxg42unbqw4ulvmvzhsvtbnr2wk4z2), [- setEqualToQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluivyxkylmkrxvc5lfoj4vmylmovsxgoq)

---

### setInQueryMode:

`- (void)setInQueryMode:(BOOL)flag`

Sets according to flag whether the receiver
is in query mode.

__See Also:__  [- inQueryMode](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3srovsxe6knn5sgk), [- enterQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3tumvzfc5lfoj4u233emu5a)

---

### setInsertedObjectDefaultValues:

`- (void)setInsertedObjectDefaultValues:(NSDictionary
*)defaultValues`

Sets default values to be used for newly inserted
objects. When you use the __insert...__ method
to add an object, that object is initially empty. Because the object
is empty, there is no value to be displayed on the HTML page, meaning
there is nothing for the user to select and modify. You use this
method to provide at least one field that can be displayed for the
newly inserted object. The possible keys into the dictionary are
the properties of the entity managed by this display group. For
example, a component that displays a list of movie titles and allows
the user to insert new movie titles might contain these statements
to ensure that all new objects have something to display as a movie
title:
> ```
> [defaultValues setObject:@"New title" forKey:@"title"];
> [movies setInsertedObjectDefaultValues:defaultValues];
> ```

__See
Also:__  [- insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhizlej5rguzldorcgkztbovwhivtbnr2wk4y)

---

### setLessThanQueryValues:

`- (void)setLessThanQueryValues:(NSDictionary
*)values`

Sets to values the receiver's dictionary of
lessThan query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the greaterThan and equalTo dictionaries
to construct qualifiers.

__See Also:__  [- lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom), [- setGreaterThanQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlui5zgkylumvzfi2dbnzixkzlspflgc3dvmvztu), [- setEqualToQueryValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluivyxkylmkrxvc5lfoj4vmylmovsxgoq)

---

### setLocalKeys:

`- (void)setLocalKeys:(NSArray
*)keys`

Sets the additional keys to which EOAssociations
can be bound to the strings in _keys_.
Instead of invoking this method programmatically, you can use Interface
Builder to add and remove local keys in the EODisplayGroup Attributes
Inspector panel.

__See Also:__  [- localKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwy33dmfwewzlzom)

---

### setObjectArray:

`- (void)setObjectArray:(NSArray
*)objects`

Sets the receiver's objects to _objects_,
regardless of what its EODataSource provides. This method doesn't
affect the EODataSource's objects at all; specifically, it results
in neither inserts or deletes of objects in the EODataSource. _objects_ should
contain objects with the same property names or methods as those
accessed by the receiver. This method is used by [fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua) to set the array of fetched
objects; you should rarely need to invoke it directly.

After
setting the object array, this method restores as much of the original
selection as possible by invoking [selectObjectsIdenticalTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45a). If there's
no match and the receiver selects after fetching, then the first
object is selected.

__See Also:__  [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq), [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi42gnfzhg5cpmjvgky3uifthizlsizsxiy3i)

---

### setQualifier:

`- (void)setQualifier:(EOQualifier
*)aQualifier`

Sets the receiver's qualifier to _aQualifier_.
This qualifier is used to filter (in memory) the receiver's array of
objects for display when the delegate doesn't do so itself. Use [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) to apply the qualifier.

If
the receiver's delegate responds to [displayGroup:displayArrayForObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a),
that method is used instead of the qualifier to filter the objects.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom), __- setAuxiliaryQualifier:__ (EODatabaseDataSource
in EOAccess)

---

### setQueryBindingValues:

`- (void)setQueryBindingValues:(NSDictionary
*)values`

Sets the dictionary of values that a user wants
to query on. You use this method to perform a query stored in the
model file. Bind keys in the [queryBindingValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lfoj4ue2lomruw4z2wmfwhkzlt) dictionary
to elements of your component that specify query values.

---

### setQueryOperatorValues:

`- (void)setQueryOperatorValues:(NSDictionary
*)values`

Sets the dictionary of operators to use on items
in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk4lvmfwfi32rovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwo4tfmf2gk4sunbqw4ulvmvzhsvtbnr2wk4y), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwyzltonkgqylokf2wk4tzkzqwy5lfom)).
If a key in a query dictionary also exists in __queryOperatorValues__,
that operator for that key is used.

---

### setSelectedObjectValue:forKey:

`- (BOOL)setSelectedObjectValue:(id)value
forKey:(NSString *)key`

Invokes [setValue:forObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2) with the
first selected object, returning YES if successful and NO otherwise.
This method should be invoked only by EOAssociation objects to propagate
changes from display objects.

__See Also:__  [- setValue:forObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uif2es3temv4du23fpe5a), [- valueForObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoq5gwzlzhi)

---

### setSelectionIndexes:

`- (BOOL)setSelectionIndexes:(NSArray
*)indexes`

Selects the objects at _indexes_ in
the receiver's array if possible, returning YES if successful
and NO if not (in which case the selection remains unaltered). _indexes_ is
an array of NSNumbers. This method is the primitive method for altering
the selection; all other such methods invoke this one to make the
change.

This method invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwk3teivsgs5djnztq) to wrap up any changes
being made by the user. If __endEditing__ returns NO,
this method fails and returns NO. This method then checks the delegate
with a [displayGroup:shouldChangeSelectionToIndexes:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3deinugc3thmvjwk3dfmn2gs33okrxus3temv4gk4z2) message.
If the delegate returns NO, this method also fails and returns NO.
If the receiver successfully changes the selection, its observers
(typically EOAssociations) each receive a [subjectChanged](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zxkytkmvrxiq3imfxgozle) message.

---

### setSelectsFirstObjectAfterFetch:

`- (void)setSelectsFirstObjectAfterFetch:(BOOL)flag`

Controls whether the receiver automatically
selects its first displayed object after a fetch when there were
no selected objects before the fetch. If _flag_ is YES it
does; if _flag_ is NO then no objects
are selected. By default, display groups select the first object
after a fetch when there was no previous selection.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua), [- selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi42gnfzhg5cpmjvgky3uifthizlsizsxiy3i)

---

### setSortOrderings:

`- (void)setSortOrderings:(NSArray
*)orderings`

Sets the EOSortOrdering objects that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) uses to sort
the displayed objects to _orderings_.
Use [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) to apply the
sort orderings.

If the receiver's delegate responds to [displayGroup:displayArrayForObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a),
that method is used instead of the sort orderings to order the objects.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)

---

### setUsesOptimisticRefresh:

`- (void)setUsesOptimisticRefresh:(BOOL)flag`

Controls how the receiver redisplays on changes
to objects. If _flag_ is YES it redisplays
only when elements of its displayed objects array change; if _flag_ is NO it
redisplays on any change in its EOEditingContext. Because changes
to other objects can affect the displayed objects (through flattened attributes
or custom methods, for example), EODisplayGroups by default use
the more pessimistic refresh technique of redisplaying on any change
in the EOEditingContext. If you know that none of the EOAssociations
for a particular EODisplayGroup display derived values, you can
turn on optimistic refresh to reduce redisplay time.

The default
is NO. You can also change this setting in Interface Builder's
Inspector panel using the Refresh All check box.

__See
Also:__  [- usesOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk43fonhxa5djnvuxg5djmnjgkztsmvzwq)

---

### setValidatesChangesImmediately:

`- (void)setValidatesChangesImmediately:(BOOL)flag`

Controls the receiver's behavior on encountering
a validation error. Whenever an EODisplayGroup sets a value in an
object, it sends the object a __validateValue:forKey:__ message,
allowing the object to coerce the value's type to a more appropriate
one or to return an exception indicating that the value isn't
valid. If this method is invoked with a _flag_ of YES,
the receiver immediately presents an attention panel indicating
the validation error. If this method is invoked with a _flag_ of NO,
the receiver leaves validation errors to be handled when changes
are saved. By default, display groups don't validate changes immediately.

__See
Also:__  - __saveChanges__ (EOEditingContext), [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)

---

### setValue:forObject:key:

`- (BOOL)setValue:(id)value
forObject:(id)anObject
key:(NSString *)key`

Sets a property of _anObject_,
identified by _key_, to _value_.
Returns YES if successful and NO otherwise. If a new value is set,
sends the delegate a [displayGroup:didSetValue:forObject:key:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfsfgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2) message.

This
method should be invoked only by EOAssociation objects to propagate
changes from display objects. Other application code should interact
with the objects directly.

If the receiver validates
changes immediately, it sends _anObject_ a __validateValue:forKey:__ message, returning NO if
the object refuses to validate _value_.
Otherwise, validation errors are checked by the EOEditingContext
when it attempts to save changes.

__See
Also:__  [- setValue:forObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uif2es3temv4du23fpe5a), [- setSelectedObjectValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5cwmfwhkzj2mzxxes3fpe5a), [- valueForObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoq5gwzlzhi), [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)

---

### setValue:forObjectAtIndex:key:

whose ids
Invokes [setValue:forObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2) with the
object at _index_, returning YES if
successful and NO otherwise. This method should be invoked only
by EOAssociation objects to propagate changes from display objects.

__See
Also:__  [- setSelectedObjectValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5cwmfwhkzj2mzxxes3fpe5a), [- valueForObjectAtIndex:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoraxislomrsxqotlmv4tu)

---

### sortOrderings

`- (NSArray *)sortOrderings`

Returns an array of EOSortOrdering objects that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) uses to sort
the displayed objects, as returned by the [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) method.

__See
Also:__  [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq)

---

### updateDisplayedObjects

`- (void)updateDisplayedObjects`

Recalculates the receiver's displayed objects
array and redisplays. If the receiver's delegate responds to [displayGroup:displayArrayForObjects:](EODisplayGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a),
it's sent this message and the returned array is set as the display
group's displayed object. Otherwise, the receiver applies its
qualifier and sort ordering to its array of objects. In either case,
any objects that were selected before remain selected in the new displayed
objects array.

__See Also:__  [- redisplay](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe), [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq), [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)

---

### updatedObjectIndex

`- (int)updatedObjectIndex`

Returns the index in the displayed objects array
of the most recently updated object, or -1 if more than one object
has changed. The return value is meaningful only when [contentsChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwg33oorsw45dtinugc3thmvsa) returns YES. EOAssociations
can use this method to optimize redisplay of their user interface
objects.

---

### usesOptimisticRefresh

`- (BOOL)usesOptimisticRefresh`

Returns YES if the receiver redisplays only
when its displayed objects change, NO if it redisplays on any change
in its EOEditingContext.

__See Also:__  [- setUsesOptimisticRefresh:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukvzwk42pob2gs3ljon2gsy2smvthezltna5a)

---

### validatesChangesImmediately

`- (BOOL)validatesChangesImmediately`

Returns YES if the receiver immediately handles
validation errors, or NO if it leaves errors for the EOEditingContext
to handle when saving changes.

__See Also:__  [- setValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4tu)

---

### valueForObject:key:

`- (id)valueForObject:(id)anObject
key:(NSString *)key`

Returns _anObject_'s
value for the property identified by _key_.

---

### valueForObjectAtIndex:key:

`- (id)valueForObjectAtIndex:(unsigned
int)index
key:(NSString *)key`

Returns the value of the object at _index_ for
the property identified by _key_.

---

## Notifications

---

### EODisplayGroupWillFetchNotification

Posted whenever an EODisplayGroup receives
a [fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwmzlumnua) message. The
notification contains:

|  |  |
| --- | --- |
| Notification Object | The EODisplayGroup that received the __fetch__ message. |
| Userinfo | None |

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
