---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EODisplayGroup.html
archived_at: '2026-07-15T08:13:55.202698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EODisplayGroup

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.webobjects.eointerface

---

### Class at a Glance

---

An EODisplayGroup collects an array of objects from an EODataSource, and works with a group of EOAssociation objects to display and edit the properties of those objects.

#### Principal Attributes

---

- Array of objects supplied by an EODataSource
- EOQualifier and EOSortOrderings to filter the objects for display
- Array of selection indexes
- Delegate

#### Commonly Used Methods

---

|  |  |
| --- | --- |
| [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg) | Returns all objects in the EODisplayGroup. |
| [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) | Returns the subset of all objects made available for display. |
| [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg) | Returns the selected objects. |
| [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkylmnftgszls) | Sets a filter that limits the objects displayed. |
| [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y) | Sets the ordering used to sort the objects. |
| [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) | Filters, sorts, and redisplays the objects. |
| [insertNewObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly) | Creates a new object and inserts it into the EODataSource. |

## Class Description

---

An EODisplayGroup is the basic user interface manager for an Enterprise Objects Framework or Java Client application. It collects objects from an EODataSource, filters and sorts them, and maintains a selection in the filtered subset. It interacts with user interface objects and other display objects through EOAssociations, which bind the values of objects to various aspects of the display objects.

An EODisplayGroup manipulates its EODataSource by sending it __fetchObjects__, __insertObject__, and other messages, and registers itself as an editor and message handler of the EODataSource's EOEditingContext. The EOEditingContext allows the EODisplayGroup to intercede in certain operations, as described in the EOEditingContext.Editor and EOEditingContext.MessageHandler interface specifications (both interfaces are defined in EOControl). EODisplayGroup implements all the methods of these informal protocols; see their specifications for more information.

Most of an EODisplayGroup's interactions are with its associations, its EODataSource, and its EOEditingContext. See the EOAssociation, EODataSource, and EOEditingContext class specifications for more information on these interactions.

## Creating an EODisplayGroup

You create most EODisplayGroups in Interface Builder, by dragging an entity icon from the EOModeler application, which creates an EODisplayGroup with an EODatabaseDataSource (EODistributedDataSource, for Java Client applications), or by dragging an EODisplayGroup with no EODataSource from the EOPalette. EODisplayGroups with EODataSources operate independent of other EODisplayGroups, while those without EODataSources must be set up in a master-detail association with another EODisplayGroup.

To create an EODisplayGroup programmatically, simply initialize it and set its EODataSource:

> ```
> EODistributedDataSource dataSource;    /* Assume this exists. */
> EODisplayGroup displayGroup;
>
> displayGroup = new EODisplayGroup();
> displayGroup.setDataSource(dataSource);
> ```

After creating the EODisplayGroup, you can add associations as described in the EOAssociation class specification.

## Getting Objects

Since an EODisplayGroup isn't much use without objects to manage, the first thing you do with an EODisplayGroup is send it a fetch message. You can use the basic [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq) method or you can configure the EODisplayGroup in Interface Builder to fetch automatically when its nib file is loaded. These methods all ask the EODisplayGroup's EODataSource to fetch from its persistent store with a __fetchObjects__ message.

### Filtering and Sorting

An EODisplayGroup's fetched objects are available through its [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg) method. These objects are treated only as candidates for display, however. The array of objects actually displayed is filtered and sorted by the EODisplayGroup's delegate, or by a qualifier and sort ordering array. You set the qualifier and sort orderings using the [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkylmnftgszls) and [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y) methods. The [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) method returns this filtered and sorted array; index arguments to other EODisplayGroup methods are defined in terms of this array.

If the EODisplayGroup has a delegate that responds to displayGroupDisplayArrayForObjects, it invokes this method rather than using its own qualifier and sort ordering array. The delegate is then responsible for filtering the objects and returning a sorted array. If the delegate only needs to perform one of these steps, it can get the qualifier or sort orderings from the EODisplayGroup and apply either itself using EOQualifier's __filteredArrayUsingQualifier__ and EOSortOrdering's __sortedArrayUsingKeyOrderArray__ methods, which are added by the control layer.

If you change the qualifier or sort ordering, or alter the delegate in a way that changes how it filters and sorts the EODisplayGroup's objects, you can send [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) to the EODisplayGroup to get it to refilter and resort its objects. Note that this doesn't cause the EODisplayGroup to refetch.

## Changing and Examining the Selection

An EODisplayGroup keeps a selection in terms of indexes into the array of displayed objects. EOAssociations that display values for multiple objects are responsible for updating the selection in their EODisplayGroups according to user actions on their display objects. This is typically done with the [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq) method. Other methods available for indirect manipulation of the selection are the action methods [selectNext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5comv4hi) and [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cqojsxm2lpovzq), as well as [selectObjectsIdenticalTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxq) and [selectObjectsIdenticalToSelectFirstOnNoMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxvgzlmmvrxirtjojzxit3ojzxu2ylumnua).

To get the selection, you can use the [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y) method, which returns an array of NSNumbers, or [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg), which returns an array containing the selected objects themselves. Another method, [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a), returns the first selected object if there is one.

## The Delegate

EODisplayGroup offers a number of methods for its delegate to implement; if the delegate does, it invokes them as appropriate. Besides the aforementioned displayGroupDisplayArrayForObjects, there are methods that inform the delegate that the EODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return true to permit the action or false to deny it. For more information, see each method's description in the EODisplayGroup.Delegate interface specification.

## Methods for Use by EOAssociations

While most of your application code interacts with objects directly, EODisplayGroup also defines methods for its associations to access properties of individual objects without having to know anything about which methods they implement. Accessing properties through the EODisplayGroup offers associations the benefit of automatic validation, as well.

Associations access objects by index into the displayed objects array, or by object identifier. [valueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2ec5cjnzsgk6a) returns the value of a named property for the object at a given index, and [setValueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3uif2es3temv4a) sets it. Similarly, [valueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2a) and [setValueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3u)access the objects by object identifier. EOAssociations can also get and set values for the first object in the selection using [selectedObjectValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2fmylmovsum33sjnsxs) and [setSelectedObjectValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3ukzqwy5lf).

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonyg643f)
>
> :

## Method Types

---

> **Configuring behavior**
>
> : [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a): [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q): [fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwqzltj5xey33bmq): [queryBindingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhsqtjnzsgs3thkzqwy5lfom): [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpojlgc3dvmvzq): [selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dtizuxe43uj5rguzldorawm5dfojdgk5ddna): [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu): [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za): [setFetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fordgk5ddnbsxgt3ojrxwcza): [setQueryBindingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkzlspfbgs3tenfxgovtbnr2wk4y): [setQueryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkzlspfhxazlsmf2g64swmfwhkzlt): [setSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3u): [setSelectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3uom): [setSelectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2hgrtjojzxit3cnjswg5cbmz2gk4sgmv2gg2a): [setUsesOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forkxgzltj5yhi2lnnfzxi2ldkjswm4tfonua): [setValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs): [usesOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65ltmvzu64dunfwws43unfrvezlgojsxg2a): [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz)
>
> **Setting the data source**
>
> : [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgc5dbknxxk4tdmu): [dataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdborqvg33vojrwk)
>
> **Setting the qualifier and sort ordering**
>
> : [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkylmnftgszls): [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza): [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y): [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)
>
> **Managing queries**
>
> : [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq): [setEqualToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcxc5lbnrkg6ulvmvzhsvtbnr2wk4y): [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom): [setGreaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fordxezlborsxevdimfxfc5lfoj4vmylmovsxg): [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt): [setLessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forggk43tkrugc3srovsxe6kwmfwhkzlt): [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq): [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f): [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya): [enterQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zloorsxeulvmvzhstlpmrsq): [inQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62lokf2wk4tzjvxwizi): [setInQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forew4ulvmvzhstlpmrsq): [enabledToSetSelectedObjectValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomfrgyzlekrxvgzluknswyzldorswit3cnjswg5cwmfwhkzkgn5zewzlz)
>
> **Fetching objects from the data source**
>
> : [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq)
>
> **Getting the objects**
>
> : [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg): [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y)
>
> **Updating display of values**
>
> : [redisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q): [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt)
>
> **Setting the objects**
>
> : [setObjectArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forhwe2tfmn2ec4tsmf4q)
>
> **Changing the selection**
>
> : [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq): [selectObjectsIdenticalTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxq): [selectObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3u): [clearSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6y3mmvqxeu3fnrswg5djn5xa): [selectNext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5comv4hi): [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cqojsxm2lpovzq)
>
> **Examining the selection**
>
> : [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y): [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a): [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg)
>
> **Adding keys**
>
> : [setLocalKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forgg6y3bnrfwk6lt): [localKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dpmnqwys3fpfzq)
>
> **Getting the associations**
>
> : [observingAssociations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc633consxe5tjnztuc43tn5rwsylunfxw44y)
>
> **Setting the delegate**
>
> : [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgk3dfm5qxizi): [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfnrswoylumu)
>
> **Changing values from associations**
>
> : [setSelectedObjectValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3ukzqwy5lf): [selectedObjectValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2fmylmovsum33sjnsxs): [setValueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3u): [valueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2a): [setValueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3uif2es3temv4a): [valueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2ec5cjnzsgk6a)
>
> **Editing by associations**
>
> : [associationDidBeginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfseezlhnfxekzdjoruw4zy): [associationDidEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfsek3teivsgs5djnztq): [associationFailedToValidateValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63sgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lf): [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thifzxg33dnfqxi2lpny): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomrcwi2lunfxgo)
>
> **Querying changes for associations**
>
> : [contentsChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6y3pnz2gk3tuonbwqylom5swi): [selectionChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xeg2dbnztwkza): [updatedObjectIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizlej5rguzldorew4zdfpa)
>
> **Interacting withthe EOEditingContext**
>
> : [editorHasChangesForEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2g64simfzug2dbnztwk42gn5zekzdjoruw4z2dn5xhizlyoq): [editingContextWillSaveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thinxw45dfpb2fo2lmnrjwc5tfinugc3thmvzq): [editingContextPresentErrorMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thinxw45dfpb2fa4tfonsw45cfojzg64snmvzxgylhmu)
>
> **Other methods**
>
> : [EODisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6rkpiruxg4dmmf4uo4tpovya): [globalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5cgn5zfmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i): [globalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq): [globalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe): [setGlobalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2em33skzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4q): [setGlobalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5a): [setGlobalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi): [awakeFromNib](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylxmfvwkrtsn5wu42lc): [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfnrsxizi): [deleteObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfnrsxizkpmjvgky3uif2es3temv4a): [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfnrsxizktmvwgky3unfxw4): [editingContextShouldContinueFetching](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thinxw45dfpb2fg2dpovwgiq3pnz2gs3tvmvdgk5ddnbuw4zy): [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5a): [insertNewObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly): [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5cpmjvgky3uif2es3temv4a): [insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5dfmrhwe2tfmn2eizlgmf2wy5cwmfwhkzlt): [objectsChangedInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc633cnjswg5dtinugc3thmvses3sfmruxi2lom5bw63tumv4hi): [objectsInvalidatedInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc633cnjswg5dtjfxhmylmnfsgc5dfmrew4rlenf2gs3thinxw45dfpb2a): [selectObjectsIdenticalToSelectFirstOnNoMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxvgzlmmvrxirtjojzxit3ojzxu2ylumnua): [setInsertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forew443foj2gkzcpmjvgky3uirswmylvnr2fmylmovsxg): [undoManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lomrxu2ylomftwk4q): [willChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc653jnrweg2dbnztwk)

## Constructors

---

### EODisplayGroup

`public EODisplayGroup()`

Creates a new EODisplayGroup. The new display group needs to have an EODataSource set with [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgc5dbknxxk4tdmu).

__See Also:__ bindAspect (EOAssociation)

---

## Static Methods

---

### globalDefaultForValidatesChangesImmediately

`public static boolean globalDefaultForValidatesChangesImmediately()`

Returns `true` if the default behavior for new display group instances is to immediately handle validation errors, or `false` if the default behavior leaves errors for the EOEditingContext to handle when saving changes.

__See Also:__ [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz)

---

### globalDefaultStringMatchFormat

`public static String globalDefaultStringMatchFormat()`

Returns the default string match format string used by display group instances.

__See Also:__ [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a)

---

### globalDefaultStringMatchOperator

`public static String globalDefaultStringMatchOperator()`

Returns the default string match operator used by display group instances.

__See Also:__ [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q)

---

### setGlobalDefaultForValidatesChangesImmediately

`public static void setGlobalDefaultForValidatesChangesImmediately(boolean flag)`

Sets the default behavior display group instances use when they encounter a validation error. If _flag_ is `true`, the default behavior is for display groups to immediately present an attention panel indicating a validation error. If _flag_ is `false`, the default behavior if for display groups to leave validation errors to be handled when changes are saved. By default, display groups don't validate changes immediately.

__See Also:__ [setValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs)

---

### setGlobalDefaultStringMatchFormat

`public static void setGlobalDefaultStringMatchFormat(String format)`

Sets the default string match format to be used by display group instances. The default format string for pattern matching is "__%@\*__".

__See Also:__ [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu)

---

### setGlobalDefaultStringMatchOperator

`public static void setGlobalDefaultStringMatchOperator(String op)`

Sets the default string match operator to be used by display group instances. The default operator is case insensitive like.

__See Also:__ [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za)

---

## Instance Methods

---

### allObjects

`public NSArray allObjects()`

Returns all of the objects collected by the receiver.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq)

---

### associationDidBeginEditing

`public void associationDidBeginEditing(EOAssociation anEOAssociation)`

Invoked by _anAssociation_ when its display object begins editing to record that EOAssociation as the editing association.

__See Also:__ [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thifzxg33dnfqxi2lpny), [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomrcwi2lunfxgo), [associationFailedToValidateValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63sgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lf)

---

### associationDidEndEditing

`public void associationDidEndEditing(EOAssociation anEOAssociation)`

Invoked by _anAssociation_ to clear the editing association. If _anAssociation_ is the receiver's editing association, clears the editing association. Otherwise does nothing.

__See Also:__ [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thifzxg33dnfqxi2lpny), [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomrcwi2lunfxgo), [associationFailedToValidateValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63sgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lf)

---

### associationFailedToValidateValue

`public boolean associationFailedToValidateValue( EOAssociation anEOAssociation, String value, String key, Object anObject, String errorDescription)`

Invoked by _anAssociation_ from its shouldEndEditingAtIndex method to let the receiver handle a validation error. This method opens an attention panel with _errorDescription_ as the message and returns false.

__See Also:__ displayGroupShouldDisplayAlert (EODisplayGroup.Delegate)

---

### awakeFromNib

`public void awakeFromNib()`

Invoked when the receiver is unarchived from a nib file to prepare it for use in an application. You should never invoke this method directly. Finishes initializing the receiver and updates the display.

__See Also:__ [redisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q)

---

### clearSelection

`public boolean clearSelection()`

Invokes [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq) to clear the selection, returning true on success and false on failure.

---

### contentsChanged

`public boolean contentsChanged()`

Returns true if the receiver's array of objects has changed and not all observers have been notified, false otherwise. EOAssociations use this in their subjectChanged methods to determine what they need to update.

__See Also:__ [selectionChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xeg2dbnztwkza), [updatedObjectIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizlej5rguzldorew4zdfpa)

---

### dataSource

`public com.webobjects.eocontrol.EODataSource dataSource()`

Returns the receiver's EODataSource.

__See Also:__ [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgc5dbknxxk4tdmu)

---

### defaultStringMatchFormat

`public String defaultStringMatchFormat()`

Returns the format string that specifies how pattern matching will be performed on string values in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)). If a key in the __queryMatch__ dictionary does not have an associated operator in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpojlgc3dvmvzq) dictionary, then its value is matched using pattern matching, and the format string returned by this method specifies how it will be matched.

__See Also:__ [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q), [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu)

---

### defaultStringMatchOperator

`public String defaultStringMatchOperator()`

Returns the operator used to perform pattern matching for string values in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)). If a key in one of the query dictionaries does not have an associated operator in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpojlgc3dvmvzq) dictionary, then the operator returned by this method is used to perform pattern matching.

__See Also:__ [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a), [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate.

__See Also:__ [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgk3dfm5qxizi)

---

### delete

`public void delete()`

Deprecated. Use [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfnrsxizktmvwgky3unfxw4). instead.

---

### deleteObjectAtIndex

`public boolean deleteObjectAtIndex(int index)`

Attempts to delete the object at _index_, returning true if successful and false if not. Checks with the delegate using displayGroupShouldDeleteObject. If the delegate returns false, this method fails and returns false. If successful, sends the delegate a displayGroupDidDeleteObject message.

This method performs the delete by sending __deleteObject__ to the EODataSource. If that message throws an exception, this method fails and returns false.

---

### deleteSelection

`public boolean deleteSelection()`

Attempts to delete the selected objects, returning true if successful and false if not.

---

### displayedObjects

`public NSArray displayedObjects()`

Returns the objects that should be displayed or otherwise made available to the user, as filtered by the receiver's delegate or by its qualifier and sort ordering.

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg), [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt), displayGroupDisplayArrayForObjects (EODisplayGroup.Delegate), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)

---

### dispose

`public void dispose()`

See the method description in the documentation for NSDisposable.

---

### editingAssociation

`public EOAssociation editingAssociation()`

Returns the EOAssociation editing a value if there is one, false if there isn't.

__See Also:__ [associationDidBeginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfseezlhnfxekzdjoruw4zy), [associationDidEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfsek3teivsgs5djnztq)

---

### editingContextPresentErrorMessage

`public void editingContextPresentErrorMessage( com.webobjects.eocontrol.EOEditingContext anEOEditingContext, String errorMessage)`

Invoked by _anEditingContext_ as part of the EOEditingContext.MessageHandlers interface, this method presents an attention panel with _errorMessage_ as the message to display.

---

### editingContextShouldContinueFetching

`public boolean editingContextShouldContinueFetching( com.webobjects.eocontrol.EOEditingContext anEOEditingContext, int count, int limit, com.webobjects.eocontrol.EOObjectStore anEOObjectStore)`

Invoked by _anEditingContext_ as part of the EOEditingContext.MessageHandlers interface, this method presents an attention panel prompting the user about whether or not to continue fetching the current result set.

---

### editingContextWillSaveChanges

`public void editingContextWillSaveChanges( com.webobjects.eocontrol.EOEditingContext anEOEditingContext)`

Invoked by anEditingContext in its __saveChanges__ method as part of the EOEditors informal protocol, this method allows the EODisplayGroup to prohibit a save operation. EODisplayGroup's implementation of this method invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomrcwi2lunfxgo), and throws an exception if it returns false. Thus, if there's an association that refuses to end editing, anEditingContext doesn't save changes.

---

### editorHasChangesForEditingContext

`public boolean editorHasChangesForEditingContext( com.webobjects.eocontrol.EOEditingContext anEOEditingContext)`

Invoked by _anEditingContext_ as part of the EOEditors interface, this method returns false if any association is editing, trueotherwise.

__See Also:__ [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thifzxg33dnfqxi2lpny), [associationDidBeginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfseezlhnfxekzdjoruw4zy), [associationDidEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfsek3teivsgs5djnztq)

---

### enabledToSetSelectedObjectValueForKey

`public boolean enabledToSetSelectedObjectValueForKey(String key)`

Returns true to indicate that a single value association (such as an EOControlAssociation for a NSTextField) should be enabled for setting _key_, false otherwise. Normally this is the case if the receiver has a selected object. However, if _key_ is a special query key (for example, "@query=.name"), then the control should be enabled even without a selected object.

---

### endEditing

`public boolean endEditing()`

Attempts to end any editing taking place. If there's no editing association or if the editing association responds true to an __endEditing__ message, returns true. Otherwise returns false.

__See Also:__ [editingAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlenf2gs3thifzxg33dnfqxi2lpny)

---

### enterQueryMode

`public void enterQueryMode()`

This action method invokes [setInQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forew4ulvmvzhstlpmrsq) with an argument of true.

---

### equalToQueryValues

`public NSDictionary equalToQueryValues()`

Returns the receiver's dictionary of equalTo query values. This dictionary is typically manipulated by associations bound to keys of the form @query=.propertyName. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the lessThan and greaterThan dictionaries to construct qualifiers.

__See Also:__ [setEqualToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcxc5lbnrkg6ulvmvzhsvtbnr2wk4y), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)

---

### fetch

`public boolean fetch()`

Attempts to fetch objects from the EODataSource, returning true on success and false on failure.

Before fetching, invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomrcwi2lunfxgo) and sends displayGroupShouldFetch to the delegate, returning false if either of these methods does. If both return true, sends a __fetchObjects__ message to the receiver's EODataSource to replace the object array, and if successful sends the delegate a displayGroupDidFetchObjects message.

---

### fetchesOnLoad

`public boolean fetchesOnLoad()`

Returns true if the receiver fetches automatically after being loaded from a nib file, false if it must be told explicitly to fetch. The default is false. You can set this behavior in Interface Builder using the Inspector panel.

__See Also:__ [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq), [fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwqzltj5xey33bmq)

---

### greaterThanQueryValues

`public NSDictionary greaterThanQueryValues()`

Returns the receiver's dictionary of greaterThan query values. This dictionary is typically manipulated by associations bound to keys of the form @query>.propertyName. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the lessThan and equalTo dictionaries to construct qualifiers.

__See Also:__ [setGreaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fordxezlborsxevdimfxfc5lfoj4vmylmovsxg),, [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom)

---

### inQueryMode

`public boolean inQueryMode()`

Returns true to indicate that the receiver is in query mode, false otherwise. In query mode, user interface controls that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query By Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty equalTo query values dictionary. When [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya) or [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See Also:__ [setInQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forew4ulvmvzhstlpmrsq), [enterQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zloorsxeulvmvzhstlpmrsq)

---

### insert

`public void insert()`

This action method invokes [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5cpmjvgky3uif2es3temv4a) with an index just past the first index in the selection, or 0 if there's no selection.

---

### insertNewObjectAtIndex

`public Object insertNewObjectAtIndex(int anIndex)`

Asks the receiver's EODataSource to create a new object by sending it a __createObject__ message, then inserts the new object using [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5cpmjvgky3uif2es3temv4a). The EODataSource createObject method has the effect of inserting the object into the EOEditingContext.

If a new object can't be created, this method sends the delegate a displayGroupCreateObjectFailed message or, if the delegate doesn't respond, opens an attention panel to inform the user of the error.

__See Also:__ [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5a)

---

### insertObjectAtIndex

`public boolean insertObjectAtIndex( Object anObject, int index)`

Inserts _anObject_ into the receiver's EODataSource and [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) array at _index_, if possible. This method checks with the delegate before actually inserting, using displayGroupShouldInsertObject. If the delegate refuses, _anObject_ isn't inserted. After successfully inserting the object, this method informs the delegate with a displayGroupDidInsertObject message, and selects the newly inserted object. Throws an exception if _index_ is out of bounds.

Unlike the [insertNewObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly) method, this method does not insert the object into the EOEditingContext. If you use this method, you're responsible for inserting the object into the EOEditingContext yourself.

---

### insertedObjectDefaultValues

`public NSDictionary insertedObjectDefaultValues()`

Returns the default values to be used for newly inserted objects. The keys into the dictionary are the properties of the entity that the display group manages. If the dictionary returned by this method is empty, the __insert...__ method adds an object that is initially empty. Because the object is empty, the display group has no value to display on the HTML page for that object, meaning that there is nothing for the user to select and modify. Use the [setInsertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forew443foj2gkzcpmjvgky3uirswmylvnr2fmylmovsxg) method to set up a default value so that there is something to display on the page.

---

### lessThanQueryValues

`public NSDictionary lessThanQueryValues()`

Returns the receiver's dictionary of lessThan query values. This dictionary is typically manipulated by associations bound to keys of the form @query<.propertyName. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the greaterThan and equalTo dictionaries to construct qualifiers.

__See Also:__ [setLessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forggk43tkrugc3srovsxe6kwmfwhkzlt), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom)

---

### localKeys

`public NSArray localKeys()`

Returns the additional keys that EOAssociations can be bound to. An EODisplayGroup's basic keys are typically those of the attributes and relationships of its objects, as defined by their EOClassDescription through an EOEntity in the model. Local keys are typically used to form associations with key paths, with arbitrary methods of objects, or with properties of objects not associated with an EOEntity. Interface Builder allows the user to add and remove local keys in the EODisplayGroup Attributes Inspector panel.

__See Also:__ [setLocalKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forgg6y3bnrfwk6lt)

---

### objectsChangedInEditingContext

`public void objectsChangedInEditingContext(NSNotification aNSNotification)`

Description forthcoming.

---

### objectsInvalidatedInEditingContext

`public void objectsInvalidatedInEditingContext(NSNotification aNSNotification)`

Description forthcoming.

---

### observingAssociations

`public NSArray observingAssociations()`

Returns all EOAssociations that observe the receiver's objects.

---

### qualifier

`public com.webobjects.eocontrol.EOQualifier qualifier()`

Returns the receiver's qualifier, which it uses to filter its array of objects for display when the delegate doesn't do so itself.

__See Also:__ [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt), [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkylmnftgszls)

---

### qualifierFromQueryValues

`public com.webobjects.eocontrol.EOQualifier qualifierFromQueryValues()`

Builds a qualifier constructed from entries in the three query dictionaries: equalTo, greaterThan, and lessThan. These, in turn, are typically manipulated by associations bound to keys of the form @query=.firstName, @query>.budget, @query<.budget.

__See Also:__ [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya), [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f)

---

### qualifyDataSource

`public void qualifyDataSource()`

Takes the result of [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) and applies to the receiver's data source. The receiver then sends itself a [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq) message. If the receiver is in query mode, query mode is exited. This method differs from [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya) as follows: whereas __qualifyDisplayGroup__ performs in-memory filtering of already fetched objects, __qualifyDataSource__ triggers a new qualified fetch against the database.

---

### qualifyDisplayGroup

`public void qualifyDisplayGroup()`

Takes the result of [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) and applies to the receiver using [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forixkylmnftgszls). The method [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) is invoked to refresh the display. If the receiver is in query mode, query mode is exited.

---

### queryBindingValues

`public NSDictionary queryBindingValues()`

Returns a dictionary containing the actual values that the user wants to query upon. You use this method to perform a query stored in the model file. Bind keys in this dictionary to elements on your component that specify query values, then pass this dictionary to the fetch specification that performs the fetch.

---

### queryOperatorValues

`public NSDictionary queryOperatorValues()`

Returns a dictionary of operators to use on items in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)). If a key in a query dictionary also exists in __queryOperatorValues__, that operator for that key is used.

__See Also:__ [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq)

---

### redisplay

`public void redisplay()`

Notifies all observing associations to redisplay their values.

__See Also:__ [observingAssociations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc633consxe5tjnztuc43tn5rwsylunfxw44y)

---

### selectNext

`public boolean selectNext()`

Attempts to select the object just after the currently selected one, returning true if successful and false if not. The selection is altered in this way:

- If there are no objects, does nothing and returns false.
- If there's no selection, selects the object at index zero and returns true.
- If the first selected object is the last object in the displayed objects array, selects the first object and returns true.
- Otherwise selects the object after the first selected object.

---

### selectObject

`public boolean selectObject(Object anObject)`

Returns true to indicate that the receiver has found and selected _anObject_, false if it can't find a match for _anObject_ (in which case it clears the selection). The selection is performed on the receiver's [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), not on [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg).

---

### selectObjectsIdenticalTo

`public boolean selectObjectsIdenticalTo(NSArray objectSelection)`

Attempts to select the objects in the receiver's displayed objects array which are equal to those of _objects_, returning true if successful and false otherwise.

---

### selectObjectsIdenticalToSelectFirstOnNoMatch

`public boolean selectObjectsIdenticalToSelectFirstOnNoMatch( NSArray objectSelection, boolean flag)`

Selects the objects in the receiver's displayed objects array that are equal to those of _objects_, returning true if successful and false otherwise. If no objects in the displayed objects array match _objects_ and _flag_ is true, attempts to select the first object in the displayed objects array.

__See Also:__ [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq)

---

### selectPrevious

`public boolean selectPrevious()`

Attempts to select the object just before the presently selected one, returning true if successful and false if not. The selection is altered in this way:

- If there are no objects, does nothing and returns false.
- If there's no selection, selects the object at index zero and returns true.
- If the first selected object is at index zero, selects the last object and returns true.
- Otherwise selects the object before the first selected object.

---

### selectedObject

`public Object selectedObject()`

Returns the first selected object in the displayed objects array, or null if there's no such object.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y)

---

### selectedObjectValueForKey

`public Object selectedObjectValueForKey(String key)`

Returns the value corresponding to _key_ for the first selected object in the receiver's displayed objects array, or null if exactly one object isn't selected.

__See Also:__ [valueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2ec5cjnzsgk6a)

---

### selectedObjects

`public NSArray selectedObjects()`

Returns the objects selected in the receiver's displayed objects array.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y)

---

### selectionChanged

`public boolean selectionChanged()`

Returns true if the selection has changed and not all observers have been notified, false otherwise. EOAssociations use this in their subjectChanged methods to determine what they need to update.

__See Also:__ [contentsChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6y3pnz2gk3tuonbwqylom5swi)

---

### selectionIndexes

`public NSArray selectionIndexes()`

Returns the indexes of the receiver's selected objects as Numbers, in terms of its displayed objects array.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg), [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a), [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq)

---

### selectsFirstObjectAfterFetch

`public boolean selectsFirstObjectAfterFetch()`

Returns true if the receiver automatically selects its first displayed object after a fetch if there was no selection, false if it leaves an empty selection as-is.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq), [setSelectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2hgrtjojzxit3cnjswg5cbmz2gk4sgmv2gg2a)

---

### setDataSource

`public void setDataSource(com.webobjects.eocontrol.EODataSource anEODataSource)`

Sets the receiver's EODataSource to _aDataSource_. In the process, it performs these actions:

- Unregisters __self__ as an editor and message handler for the previous EODataSource's EOEditingContext, if necessary, and registers __self__ with _aDataSource's_ editing context. If the new editing context already has a message handler, however, the receiver doesn't assume that role.
- Registers __self__ for `ObjectsChangedInEditingContextNotification` and `InvalidatedAllObjectsInStoreNotification` from the new editing context.
- Clears the receiver's array of objects.
- Sends displayGroupDidChangeDataSource to the delegate if there is one.

__See Also:__ [dataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdborqvg33vojrwk)

---

### setDefaultStringMatchFormat

`public void setDefaultStringMatchFormat(String format)`

Sets how pattern matching will be performed on String values in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)). This format is used for query dictionary properties that have String values and that do not have an associated entry in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpojlgc3dvmvzq) dictionary. In these cases, the value is matched using pattern matching and format specifies how it will be matched.

The default format string for pattern matching is "__%@\*__" which means that the string value in the __queryMatch__ dictionary is used as a prefix. For example, if the query dictionary contains a value "Jo" for the key "Name", the query returns all records whose name values begin with "Jo".

__See Also:__ [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a), [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za)

---

### setDefaultStringMatchOperator

`public void setDefaultStringMatchOperator(String matchOperator)`

Sets the operator used to perform pattern matching for String values in the __queryMatch__ dictionary. This operator is used for properties listed in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)) that have String values and that do not have an associated entry in the [queryOperatorValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpojlgc3dvmvzq) dictionary. In these cases, the operator _matchOperator_ is used to perform pattern matching.

The default value for the query match operator is __caseInsensitiveLike__, which means that the query does not consider case when matching letters. The other possible value for this operator is __like__, which matches the case of the letters exactly.

__See Also:__ [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q), [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu)

---

### setDelegate

`public void setDelegate(Object anObject)`

Sets the receiver's delegate to _anObject_.

__See Also:__ [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdfnrswoylumu)

---

### setEqualToQueryValues

`public void setEqualToQueryValues(NSDictionary values)`

Sets to _values_ the receiver's dictionary of equalTo query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the lessThan and greaterThan dictionaries to construct qualifiers.

__See Also:__ [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [setLessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forggk43tkrugc3srovsxe6kwmfwhkzlt), [setGreaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fordxezlborsxevdimfxfc5lfoj4vmylmovsxg)

---

### setFetchesOnLoad

`public void setFetchesOnLoad(boolean flag)`

Controls whether the receiver automatically fetches its objects after being loaded from a nib file. If _flag_ is true it does; if _flag_ is false the receiver must be told explicitly to fetch. The default is false. You can also set this behavior in Interface Builder using the Inspector panel.

__See Also:__ [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq), [fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwqzltj5xey33bmq)

---

### setGreaterThanQueryValues

`public void setGreaterThanQueryValues(NSDictionary values)`

Sets to _values_ the receiver's dictionary of greaterThan query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the lessThan and equalTo dictionaries to construct qualifiers.

__See Also:__ [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), [setLessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forggk43tkrugc3srovsxe6kwmfwhkzlt), [setEqualToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcxc5lbnrkg6ulvmvzhsvtbnr2wk4y)

---

### setInQueryMode

`public void setInQueryMode(boolean flag)`

Sets according to _flag_ whether the receiver is in query mode.

__See Also:__ [inQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62lokf2wk4tzjvxwizi), [enterQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zloorsxeulvmvzhstlpmrsq)

---

### setInsertedObjectDefaultValues

`public void setInsertedObjectDefaultValues(NSDictionary defaultValues)`

Sets default values to be used for newly inserted objects. When you use the __insert...__ method to add an object, that object is initially empty. Because the object is empty, there is no value to be displayed on the HTML page, meaning there is nothing for the user to select and modify. You use this method to provide at least one field that can be displayed for the newly inserted object. The possible keys into the dictionary are the properties of the entity managed by this display group.

__See Also:__ [insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5dfmrhwe2tfmn2eizlgmf2wy5cwmfwhkzlt)

---

### setLessThanQueryValues

`public void setLessThanQueryValues(NSDictionary values)`

Sets to values the receiver's dictionary of lessThan query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the greaterThan and equalTo dictionaries to construct qualifiers.

__See Also:__ [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq), [setGreaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fordxezlborsxevdimfxfc5lfoj4vmylmovsxg), [setEqualToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcxc5lbnrkg6ulvmvzhsvtbnr2wk4y)

---

### setLocalKeys

`public void setLocalKeys(NSArray keys)`

Sets the additional keys to which EOAssociations can be bound to the strings in _keys_. Instead of invoking this method programmatically, you can use Interface Builder to add and remove local keys in the EODisplayGroup Attributes Inspector panel.

__See Also:__ [localKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dpmnqwys3fpfzq)

---

### setObjectArray

`public void setObjectArray(NSArray objects)`

Sets the receiver's objects to _objects_, regardless of what its EODataSource provides. This method doesn't affect the EODataSource's objects at all; specifically, it results in neither inserts or deletes of objects in the EODataSource. _objects_ should contain objects with the same property names or methods as those accessed by the receiver. This method is used by [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq) to set the array of fetched objects; you should rarely need to invoke it directly.

After setting the object array, this method restores as much of the original selection as possible by invoking [selectObjectsIdenticalTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxq). If there's no match and the receiver selects after fetching, then the first object is selected.

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg), [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dtizuxe43uj5rguzldorawm5dfojdgk5ddna)

---

### setQualifier

`public void setQualifier(com.webobjects.eocontrol.EOQualifier anEOQualifier)`

Sets the receiver's qualifier to _aQualifier_. This qualifier is used to filter (in memory) the receiver's array of objects for display when the delegate doesn't do so itself. Use [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) to apply the qualifier.

|  |
| --- |
| __Note:__ To set the qualifier used to fetch objects from the database, set the qualifier of the display group's [dataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdborqvg33vojrwk) (assuming that the data source is an EODatabaseDataSource). |

If the receiver's delegate responds to displayGroupDisplayArrayForObjects, that method is used instead of the qualifier to filter the objects.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq)

---

### setQueryBindingValues

`public void setQueryBindingValues(NSDictionary values)`

Sets the dictionary of values that a user wants to query on. You use this method to perform a query stored in the model file. Bind keys in the [queryBindingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmvzhsqtjnzsgs3thkzqwy5lfom) dictionary to elements of your component that specify query values.

---

### setQueryOperatorValues

`public void setQueryOperatorValues(NSDictionary values)`

Sets the dictionary of operators to use on items in the query dictionaries ( [equalToQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlrovqwyvdpkf2wk4tzkzqwy5lfom), [greaterThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6z3smvqxizlskrugc3srovsxe6kwmfwhkzlt), and [lessThanQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dfonzvi2dbnzixkzlspflgc3dvmvzq)). If a key in a query dictionary also exists in __queryOperatorValues__, that operator for that key is used.

---

### setSelectedObject

`public void setSelectedObject(Object anObject)`

Sets the selected objects to _anObject_.

---

### setSelectedObjectValue

`public boolean setSelectedObjectValue( Object value , String key)`

Invokes [setValueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3u) with the first selected object, returning true if successful and false otherwise. This method should be invoked only by EOAssociation objects to propagate changes from display objects.

__See Also:__ [setValueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3uif2es3temv4a), [valueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2a)

---

### setSelectedObjects

`public void setSelectedObjects(NSArray objects)`

Sets the selected objects to _objects_.

---

### setSelectionIndexes

`public boolean setSelectionIndexes(NSArray indexes)`

Selects the objects at _indexes_ in the receiver's array if possible, returning true if successful and false if not (in which case the selection remains unaltered). _indexes_ is an array of Numbers. This method is the primitive method for altering the selection; all other such methods invoke this one to make the change.

This method invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zlomrcwi2lunfxgo) to wrap up any changes being made by the user. If __endEditing__ returns false, this method fails and returns false. This method then checks the delegate with a displayGroupShouldChangeSelection message. If the delegate returns false, this method also fails and returns false. If the receiver successfully changes the selection, its observers (typically EOAssociations) each receive a subjectChanged message.

---

### setSelectsFirstObjectAfterFetch

`public void setSelectsFirstObjectAfterFetch(boolean flag)`

Controls whether the receiver automatically selects its first displayed object after a fetch when there were no selected objects before the fetch. If _flag_ is true it does; if _flag_ is false then no objects are selected. By default, display groups select the first object after a fetch when there was no previous selection.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq), [selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dtizuxe43uj5rguzldorawm5dfojdgk5ddna)

---

### setSortOrderings

`public void setSortOrderings(NSArray orderings)`

Sets the EOSortOrdering objects that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) uses to sort the displayed objects to _orderings_. Use [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) to apply the sort orderings.

If the receiver's delegate responds to displayGroupDisplayArrayForObjects, that method is used instead of the sort orderings to order the objects.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)

---

### setUsesOptimisticRefresh

`public void setUsesOptimisticRefresh(boolean flag)`

Controls how the receiver redisplays on changes to objects. If _flag_ is true it redisplays only when elements of its displayed objects array change; if _flag_ is false it redisplays on any change in its EOEditingContext. Because changes to other objects can affect the displayed objects (through flattened attributes or custom methods, for example), EODisplayGroups by default use the more pessimistic refresh technique of redisplaying on any change in the EOEditingContext. If you know that none of the EOAssociations for a particular EODisplayGroup display derived values, you can turn on optimistic refresh to reduce redisplay time.

The default is false. You can also change this setting in Interface Builder's Inspector panel using the Refresh All check box.

__See Also:__ [usesOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65ltmvzu64dunfwws43unfrvezlgojsxg2a)

---

### setValidatesChangesImmediately

`public void setValidatesChangesImmediately(boolean flag)`

Controls the receiver's behavior on encountering a validation error. Whenever an EODisplayGroup sets a value in an object, it sends the object a __validateValueForKey__ message, allowing the object to coerce the value's type to a more appropriate one or to return an exception indicating that the value isn't valid. If this method is invoked with a _flag_ of true, the receiver immediately presents an attention panel indicating the validation error. If this method is invoked with a _flag_ of false, the receiver leaves validation errors to be handled when changes are saved. By default, display groups don't validate changes immediately.

__See Also:__ - __saveChanges__ (EOEditingContext), [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz)

---

### setValueForObject

`public boolean setValueForObject( Object value, Object anObject, String key)`

Sets a property of _anObject_, identified by _key_, to _value_. Returns true if successful and false otherwise. If a new value is set, sends the delegate a displayGroupDidSetValueForObject message.

This method should be invoked only by EOAssociation objects to propagate changes from display objects. Other application code should interact with the objects directly.

If the receiver validates changes immediately, it sends _anObject_ a __validateValueForKey__ message, returning false if the object refuses to validate _value_. Otherwise, validation errors are checked by the EOEditingContext when it attempts to save changes

__See Also:__ [setValueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3uif2es3temv4a), [setSelectedObjectValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3ukzqwy5lf), [valueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2a), [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz)

---

### setValueForObjectAtIndex

`public boolean setValueForObjectAtIndex( Object value, int index, String key)`

Invokes [setValueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3u) with the object at _index_, returning true if successful and false otherwise. This method should be invoked only by EOAssociation objects to propagate changes from display objects.

__See Also:__ [setSelectedObjectValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3ukzqwy5lf), [valueForObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2ec5cjnzsgk6a)

---

### sortOrderings

`public NSArray sortOrderings()`

Returns an array of EOSortOrdering objects that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) uses to sort the displayed objects, as returned by the [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) method.

__See Also:__ [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y)

---

### undoManager

`public NSUndoManager undoManager()`

Returns the receiver's undo manager.

---

### updateDisplayedObjects

`public void updateDisplayedObjects()`

Recalculates the receiver's displayed objects array and redisplays. If the receiver's delegate responds to displayGroupDisplayArrayForObjects, it's sent this message and the returned array is set as the display group's displayed object. Otherwise, the receiver applies its qualifier and sort ordering to its array of objects. In either case, any objects that were selected before remain selected in the new displayed objects array.

__See Also:__ [redisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q), [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)

---

### updatedObjectIndex

`public int updatedObjectIndex()`

Returns the index in the displayed objects array of the most recently updated object, or -1 if more than one object has changed. The return value is meaningful only when [contentsChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6y3pnz2gk3tuonbwqylom5swi) returns true. EOAssociations can use this method to optimize redisplay of their user interface objects.

---

### usesOptimisticRefresh

`public boolean usesOptimisticRefresh()`

Returns true if the receiver redisplays only when its displayed objects change, false if it redisplays on any change in its EOEditingContext.

__See Also:__ [setUsesOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forkxgzltj5yhi2lnnfzxi2ldkjswm4tfonua)

---

### validatesChangesImmediately

`public boolean validatesChangesImmediately()`

Returns true if the receiver immediately handles validation errors, or false if it leaves errors for the EOEditingContext to handle when saving changes.

__See Also:__ [setValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs)

---

### valueForObject

`public Object valueForObject( NSKeyValueCodingAdditions anObject, String key)`

Returns _anObject_'s value for the property identified by _key_.

---

### valueForObjectAtIndex

`public Object valueForObjectAtIndex( int index, String key)`

Returns the value of the object at _index_ for the property identified by _key_.

---

### willChange

`public void willChange()`

Notifies observers that the receiver will change.

---

## Notifications

---

### DisplayGroupWillFetchNotification

`public static final String DisplayGroupWillFetchNotification`

Posted whenever an EODisplayGroup receives a [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6ztforrwq) message. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The EODisplayGroup that received the __fetch__ message. |
| Userinfo | None |

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
