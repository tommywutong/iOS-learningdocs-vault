---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOEditingContext.html
archived_at: '2026-07-15T08:13:46.760019Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOEditingContext

> __Inherits from:__ [EOObjectStore](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu6ytkmvrxiu3un5zgk)
>
> __Implements:__
> EOObserving
> NSDisposable
> NSLocking
> EOKeyValueArchiving
> Serializable
>
> __Package:__ com.webobjects.eocontrol

---

### Class at a Glance

---

An EOEditingContext object manages a graph of enterprise objects in an application; this object graph represents an internally consistent view of one or more external stores (most often a database).

#### Principal Attributes

---

- Set of enterprise objects managed by the EOEditingContext
- Parent EOObjectStore
- Set of EOEditor objects messaged by the EOEditingContext
- A message handler

#### Commonly Used Methods

---

|  |  |
| --- | --- |
| [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q) | Fetches objects from an external store. |
| [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2a) | Registers a new object to be inserted into the parent EOObjectStore when changes are saved. |
| [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvhwe2tfmn2a) | Registers that an object should be removed from the parent EOObjectStore when changes are saved. |
| [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u) | Attempts to lock an object in the external store. |
| [hasChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnbqxgq3imfxgozlt) | Returns `true` if any of the receiver has any pending changes to the parent EOObjectStore. |
| [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom) | Commits changes made in the receiver to the parent EOObjectStore. |
| [objectForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldordg64shnrxweylmjfca) | Given a globalID, returns its associated object. |
| [globalIDForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpm5wg6ytbnreuirtpojhwe2tfmn2a) | Given an object, returns its globalID. |
| [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxirdfnrswoylumu) | Sets the receiver's delegate. |
| [parentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobqxezloorhwe2tfmn2fg5dpojsq) | Returns the receiver's parent EOObjectStore. |
| [rootObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojxw65cpmjvgky3ukn2g64tf) | Returns the receiver's root EOObjectStore. |

## Class Description

---

An EOEditingContext object represents a single "object space" or document in an application. Its primary responsibility is managing a graph of enterprise objects. This _object graph_ is a group of related business objects that represent an internally consistent view of one or more external stores (usually a database).

All objects fetched from an external store are registered in an editing context along with a global identifier (EOGlobalID) that's used to uniquely identify each object to the external store. The editing context is responsible for watching for changes in its objects (using the EOObserving interface) and recording snapshots for object-based undo. A single enterprise object instance exists in one and only one editing context, but multiple copies of an object can exist in different editing contexts. Thus object uniquing is scoped to a particular editing context.

For more information on EOEditingContext, see the sections:

- ["Other Classes That Participate in Object Graph Management" (page 71)](EOEditingContext.Concepts.md#apple-irauoq2cijauu)
- ["Programmatically Creating an EOEditingContext" (page 71)](EOEditingContext.Concepts.md#apple-irauorcgjfbek)
- ["Using EOEditingContexts in Different Configurations" (page 73)](EOEditingContext.Concepts.md#apple-ijeucrcbjfeeq)
- ["Fetching Objects" (page 76)](EOEditingContext.Concepts.md#apple-irauorcbjfbeq)
- ["Managing Changes in Your Application" (page 77)](EOEditingContext.Concepts.md#apple-irauoqsgizeue)
- ["Methods for Managing the Object Graph" (page 78)](EOEditingContext.Concepts.md#apple-irauoqsbizeus)
- ["General Guidelines for Managing the Object Graph" (page 82)](EOEditingContext.Concepts.md#apple-irauorcfijfec)
- ["Using EOEditingContext to Archive Custom Objects in WebObjects Framework" (page 83)](EOEditingContext.Concepts.md#apple-irauoqsejfeee)

## Constants

---

EOEditingContext defines the following `int` constant to specifies the order in which editing contexts perform end of event processing in [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt).

- EditingContextFlushChangesRunLoopOrdering

Messages with lower order numbers are processed before messages with higher order numbers. In an application built with the Application Kit, the constant order value schedules the editing context to perform its processing before the undo stack group is closed or window display is updated.

EOEditingContext also defines String constants for the names of the notifications it posts. See the section ["Notifications" (page 181)](#apple-ijeuiq2hindec) for more information.

## Interfaces Implemented

---

> EOObserving
> [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorlws3dminugc3thmu)
>
> NSLocking
> [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg2y)
> [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovxgy33dnm)

## Method Types

---

> Constructors
> [EOEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpivhukzdjoruw4z2dn5xhizlyoq)
>
> Committing or discarding changes
> [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom)[refaultObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswmylvnr2e6ytkmvrxi4y)[refetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswmzlumnua)[invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt)
>
> Registering changes
> [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvhwe2tfmn2a)[insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2a)[insertObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2fo2lunbdwy33cmfwesra)[objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorlws3dminugc3thmu)[processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt)
>
> Checking changes
> [deletedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y)[insertedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorswit3cnjswg5dt)[updatedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovygiylumvse6ytkmvrxi4y)[hasChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnbqxgq3imfxgozlt)
>
> Object registration and snapshotting
> [forgetObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzxxez3forhwe2tfmn2a)
> [recordObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswg33smrhwe2tfmn2a)
> [committedSnapshotForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmnxw23ljor2gkzctnzqxa43in52em33sj5rguzldoq)
> [currentEventSnapshotForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmn2xe4tfnz2ek5tfnz2fg3tbobzwq33uizxxet3cnjswg5a)
> [objectForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldordg64shnrxweylmjfca)
> [globalIDForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpm5wg6ytbnreuirtpojhwe2tfmn2a)
> [registeredObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswo2ltorsxezlej5rguzldorzq)
>
> Timestamping snapshots
> [defaultFetchTimestampLag](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zdfmzqxk3duizsxiy3ikruw2zltorqw24cmmftq)
> [setDefaultFetchTimestampLag](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forcgkztbovwhirtforrwqvdjnvsxg5dbnvyeyylh)
> [fetchTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzsxiy3ikruw2zltorqw24a)
> [setFetchTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxirtforrwqvdjnvsxg5dbnvya)
>
> Locking objects
> [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u)
> [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfca)
> [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq)
> [setLocksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxitdpmnvxgt3cnjswg5dtijswm33smvdgs4ttorgw6zdjmzuwgylunfxw4)
> [locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg23tj5rguzldorzuezlgn5zgkrtjojzxitlpmruwm2ldmf2gs33o)
>
> Undoing operations
> [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswi3y)
> [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovxgi3y)
> [setUndoManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxivlomrxu2ylomftwk4q)
> [undoManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovxgi32nmfxgcz3foi)
>
> Accessing the shared editing context
> [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du)
> [setSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiu3imfzgkzcfmruxi2lom5bw63tumv4hi)
>
> Deletion and Validation Behavior
> [setPropagatesDeletesAtEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiudsn5ygcz3borsxgrdfnrsxizltif2ek3tej5tek5tfnz2a)
> [propagatesDeletesAtEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg64dbm5qxizltirswyzlumvzuc5cfnzse6zsfozsw45a)
> [setStopsValidationAfterFirstError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiu3un5yhgvtbnruwiylunfxw4qlgorsxertjojzxirlsojxxe)
> [stopsValidationAfterFirstError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpon2g64dtkzqwy2lemf2gs33oifthizlsizuxe43uivzhe33s)
>
> Returning related object stores
> [parentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobqxezloorhwe2tfmn2fg5dpojsq)
> [rootObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojxw65cpmjvgky3ukn2g64tf)
>
> Managing editors
> [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq)[addEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmfsgirlenf2g64q)
> [removeEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojsw233wmvcwi2lun5za)
>
> Setting the delegate
> [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxirdfnrswoylumu)[delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlhmf2gk)
>
> Setting the message handler
> [setMessageHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxitlfonzwcz3fjbqw4zdmmvza)
> [messageHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnvsxg43bm5suqylomrwgk4q)
>
> Invalidating objects
> [invalidatesObjectsWhenFinalized](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfonhwe2tfmn2hgv3imvxem2lomfwgs6tfmq)
>
> Interacting with the server
> [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhm33lmvjgk3lporsu2zlunbxwi)
>
> Locking
> [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg2y)
> [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovxgy33dnm)
>
> Working with raw rows
> [faultForRawRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzqxk3duizxxeutbo5jg65y)
>
> Unarchiving from nib
> [defaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zdfmzqxk3dukbqxezloorhwe2tfmn2fg5dpojsq)
> [setDefaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forcgkztbovwhiudbojsw45cpmjvgky3ukn2g64tf)
> [setSubstitutionEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forjxkyttoruxi5lunfxw4rlenf2gs3thinxw45dfpb2a)
> [substitutionEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643vmjzxi2luov2gs33oivsgs5djnztug33oorsxq5a)
>
> Nested EOEditingContext support
> [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q)
> [objectsForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorzum33sknxxk4tdmvdwy33cmfwesra)
> [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmfzheylzizqxk3duk5uxi2ctn52xey3fi5wg6ytbnreui)
> [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzqxk3duizxxer3mn5rgc3cjiq)
> [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a)
> [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswmylvnr2e6ytkmvrxi)
> [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfj5rguzldorzvo2lunbdwy33cmfwesrdt)
> [initializeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxgs5djmfwgs6tfj5rguzldoq)
>
> Archiving and unarchiving objects
> [encodeObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zlomnxwizkpmjvgky3uk5uxi2cdn5sgk4q)
> [initObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c62lonf2e6ytkmvrxiv3jorueg33emvza)
> [setUsesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forkxgzltinxw45dfpb2fezlmmf2gs5tfivxgg33enfxgo)
> [usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c65ltmvzug33oorsxq5csmvwgc5djozsuk3tdn5sgs3th)

## Constructors

---

### EOEditingContext

`public EOEditingContext()`

Creates a new EOEditingContext object with the default parent object store as its parent object store. Shares objects with the default shared editing context (if any) unless you change its shared editing context with [setSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiu3imfzgkzcfmruxi2lom5bw63tumv4hi).

`public EOEditingContext(EOObjectStore anObjectStore)`

Creates a new EOEditingContext object with _anObjectStore_ as its parent object store. Shares objects with the default shared editing context (if any) unless you change its shared editing context with [setSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiu3imfzgkzcfmruxi2lom5bw63tumv4hi). For more discussion of parent object stores, see ["Other Classes That Participate in Object Graph Management" (page 71)](EOEditingContext.Concepts.md#apple-irauoq2cijauu).

__See Also:__ [parentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobqxezloorhwe2tfmn2fg5dpojsq), [defaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zdfmzqxk3dukbqxezloorhwe2tfmn2fg5dpojsq)

---

## Static Methods

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

### defaultFetchTimestampLag

`public static long defaultFetchTimestampLag()`

Returns the default timestamp lag.

---

### defaultParentObjectStore

`public static EOObjectStore defaultParentObjectStore()`

Returns the EOObjectStore that is the default parent object store for new editing contexts. Normally this is the EOObjectStoreCoordinator returned from the EOObjectStoreCoordinator static method defaultCoordinator.

__See Also:__ [setDefaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forcgkztbovwhiudbojsw45cpmjvgky3ukn2g64tf)

---

### encodeObjectWithCoder

`public static void encodeObjectWithCoder( EOEnterpriseObject object, NSCoder encoder)`

Invoked by an enterprise object _object_ to ask the EOEditingContext to encode _object_ using _encoder_. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in WebObjects Framework" (page 83)](EOEditingContext.Concepts.md#apple-irauoqsejfeee).

__See Also:__ [initObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c62lonf2e6ytkmvrxiv3jorueg33emvza), [setUsesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forkxgzltinxw45dfpb2fezlmmf2gs5tfivxgg33enfxgo), [usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c65ltmvzug33oorsxq5csmvwgc5djozsuk3tdn5sgs3th)

---

### initObjectWithCoder

`public static Object initObjectWithCoder( EOEnterpriseObject object, NSCoder decoder)`

Invoked by an enterprise object _object_ to ask the EOEditingContext to initialize _object_ from data in _decoder_. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in WebObjects Framework" (page 83)](EOEditingContext.Concepts.md#apple-irauoqsejfeee).

__See Also:__ [encodeObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zlomnxwizkpmjvgky3uk5uxi2cdn5sgk4q), [setUsesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forkxgzltinxw45dfpb2fezlmmf2gs5tfivxgg33enfxgo), [usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c65ltmvzug33oorsxq5csmvwgc5djozsuk3tdn5sgs3th)

---

### setDefaultFetchTimestampLag

`public static void setDefaultFetchTimestampLag(long lag)`

Sets the default timestamp lag for newly instantiated editing contexts to _lag_. The default lag is 3600.0 seconds (one hour).

When a new editing context is initialized, it is assigned a fetch timestamp equal to the current time less the default timestamp lag. Setting the lag to a large number might cause every new editing context to accept very old cached data. Setting the lag to too low a value might degrade performance due to excessive fetching. A negative lag value is treated as 0.0.

---

### setDefaultParentObjectStore

`public static void setDefaultParentObjectStore(EOObjectStore store)`

Sets thedefault parent EOObjectStore to _store_. You use this method before loading a nib file to change the default parent EOObjectStores of the EOEditingContexts in the nib file. The object you supply for _store_ can be a different EOObjectStoreCoordinator or another EOEditingContext (if you're using a nested EOEditingContext). After loading a nib with an EOEditingContext substituted as the default parent EOObjectStore, you should restore the default behavior by setting the default parent EOObjectStore to null.

A default parent object store is global until it is changed again. For more discussion of this topic, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

__See Also:__ [defaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zdfmzqxk3dukbqxezloorhwe2tfmn2fg5dpojsq)

---

### setSubstitutionEditingContext

`public static void setSubstitutionEditingContext(EOEditingContext anEditingContext)`

Assigns _anEditingContext_ as the EOEditingContext to substitute for the one specified in a nib file you're about to load. Using this method causes all of the connections in your nib file to be redirected to _anEditingContext_. This can be useful when you want an interface loaded from a second nib file to use an existing EOEditingContext. After loading a nib with a substitution EOEditingContext, you should restore the default behavior by setting the substitution EOEditingContext to null.

A substitution editing context is global until it is changed again. For more discussion of this topic, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

__See Also:__ [substitutionEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643vmjzxi2luov2gs33oivsgs5djnztug33oorsxq5a)

---

### setUsesContextRelativeEncoding

`public static void setUsesContextRelativeEncoding(boolean flag)`

Sets according to _flag_ whether [encodeObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zlomnxwizkpmjvgky3uk5uxi2cdn5sgk4q) uses context-relative encoding. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in WebObjects Framework" (page 83)](EOEditingContext.Concepts.md#apple-irauoqsejfeee).

__See Also:__ [usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c65ltmvzug33oorsxq5csmvwgc5djozsuk3tdn5sgs3th), [encodeObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zlomnxwizkpmjvgky3uk5uxi2cdn5sgk4q)

---

### substitutionEditingContext

`public static EOEditingContext substitutionEditingContext()`

Returns the substitution EOEditingContext if one has been specified. Otherwise returns null.

__See Also:__ [setSubstitutionEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forjxkyttoruxi5lunfxw4rlenf2gs3thinxw45dfpb2a)

---

### usesContextRelativeEncoding

`public static boolean usesContextRelativeEncoding()`

Returns true to indicate that [encodeObjectWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c6zlomnxwizkpmjvgky3uk5uxi2cdn5sgk4q) uses context relative encoding, false otherwise. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in WebObjects Framework" (page 83)](EOEditingContext.Concepts.md#apple-irauoqsejfeee).

__See Also:__ [setUsesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlenf2gs3thinxw45dfpb2c643forkxgzltinxw45dfpb2fezlmmf2gs5tfivxgg33enfxgo)

---

## Instance Methods

---

### addEditor

`public void addEditor(Object editor)`

Adds _editor_ to the receiver's set of EOEditingContext.Editors. For more explanation, see the method description for [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq) and the EOEditingContext.Editors interface specification.

__See Also:__ [removeEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojsw233wmvcwi2lun5za)

---

### arrayFaultWithSourceGlobalID

`public NSArray arrayFaultWithSourceGlobalID( EOGlobalID globalID, String name, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore. If the objects associated with the EOGlobalID _globalID_ are already registered in the receiver, returns those objects. Otherwise, propagates the message down the object store hierarchy, through the parent object store, ultimately to the associated EODatabaseContext. The EODatabaseContext creates and returns a to-many fault.

When a parent EOEditingContext receives this on behalf of a child EOEditingContext and the EOGlobalID _globalID_ identifies a newly inserted object in the parent, the parent returns a copy of its object's relationship array with the member objects translated into objects in the child EOEditingContext.

For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), and EOFaultHandler class specifications.

__See Also:__ [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzqxk3duizxxer3mn5rgc3cjiq)

---

### committedSnapshotForObject

`public NSDictionary committedSnapshotForObject(EOEnterpriseObject object)`

Returns a dictionary containing a snapshot of _object_ that reflects its committed values (that is, its values as they were last committed to the database).In other words, this snapshot represents the state of the object before any modifications were made to it. The snapshot is updated to the newest object state after a save.

__See Also:__ [currentEventSnapshotForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmn2xe4tfnz2ek5tfnz2fg3tbobzwq33uizxxet3cnjswg5a)

---

### currentEventSnapshotForObject

`public NSDictionary currentEventSnapshotForObject(EOEnterpriseObject object)`

Returns a dictionary containing a snapshot of _object_ that reflects its state as it was at the beginning of the current event loop. After the end of the current event-upon invocation of __processRecentChanges__-this snapshot is updated to hold the modified state of the object.

__See Also:__ [committedSnapshotForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmnxw23ljor2gkzctnzqxa43in52em33sj5rguzldoq), [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate.

__See Also:__ [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxirdfnrswoylumu)

---

### deleteObject

`public void deleteObject(EOEnterpriseObject object)`

Specifies that _object_ should be removed from the receiver's parent EOObjectStore when changes are committed. At that time, the object will be removed from the uniquing tables.

__See Also:__ [deletedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y)

---

### deletedObjects

`public NSArray deletedObjects()`

Returns the objects that have been deleted from the receiver's object graph.

__See Also:__ [updatedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovygiylumvse6ytkmvrxi4y), [insertedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorswit3cnjswg5dt)

---

### __dispose__

`public void dispose()`

Description forthcoming.

---

### __editingContextDidForgetObjectWithGlobalID__

`public void editingContextDidForgetObjectWithGlobalID( EOEditingContext context, EOGlobalID gid)`

See the superclass's method description of editingContextDidForgetObjectWithGlobalID in the class specification for EOObjectStore.

---

### editors

`public NSArray editors()`

Returns the receiver's editors. Editors are special-purpose delegate objects that may contain uncommitted changes that need to be validated and applied to enterprise objects before the EOEditingContext saves changes. For example, EODisplayGroups (EOInterface) register themselves as editors with the EOEditingContext of their data sources so that they can save any changes in the key text field. For more information, see the EOEditingContext.Editors interface specification and the EODisplayGroup class specification.

__See Also:__ [addEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmfsgirlenf2g64q), [removeEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojsw233wmvcwi2lun5za)

---

### encodeWithKeyValueUnarchiver

`public Object encodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

### faultForGlobalID

`public EOEnterpriseObject faultForGlobalID( EOGlobalID globalID, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore. If the object associated with the EOGlobalID _globalID_ is already registered in the receiver (or in the receiver's [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du)), this method returns that object. Otherwise, the method propagates the message down the object store hierarchy, through the parent object store, ultimately to the associated EODatabaseContext. The EODatabaseContext creates and returns a to-one fault.

For example, suppose you want the department object whose __deptID__ has a particular value. The most efficient way to get it is to look it up by its globalID using __faultForGlobalID__.

If the department object is already registered in the EOEditingContext, __faultForGlobalID__ returns the object (without going to the database). If not, a fault for this object is created, and the object is fetched only when you trigger the fault.

In a nested editing context configuration, when a parent EOEditingContext is sent __faultForGlobalID__ on behalf of a child EOEditingContext and _globalID_ identifies a newly inserted object in the parent, the parent registers a copy of the object in the child.

For more discussion of this method, see the section ["Working with Objects Across Multiple EOEditingContexts" (page 81)](EOEditingContext.Concepts.md#apple-ijeucq2fiveei). For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), and EOFaultHandler class specifications.

__See Also:__ [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmfzheylzizqxk3duk5uxi2ctn52xey3fi5wg6ytbnreui)

---

### faultForRawRow

`public EOEnterpriseObject faultForRawRow( NSDictionary row, String entityName)`

`public EOEnterpriseObject faultForRawRow( NSDictionary row, String entityName, EOEditingContext context)`

Returns a fault for the raw row _row_ by invoking faultForRawRow with __this__ as the editing context.

---

### fetchTimestamp

`public long fetchTimestamp()`

Returns the receiver's fetch timestamp.

---

### forgetObject

`public void forgetObject(EOEnterpriseObject object)`

Removes _object_ from the uniquing tables and causes the receiver to remove itself as the object's observer. This method is invoked whenever an object being observed by an EOEditingContext is finalized. You should never invoke this method directly. The correct way to remove an object from its editing context is to remove every reference to the object by refaulting any object that references it (using [refaultObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswmylvnr2e6ytkmvrxi4y) or [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt)). Also note that this method does _not_ have the effect of deleting an object-to delete an object you should either use the [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvhwe2tfmn2a) method or remove the object from an owning relationship.

---

### globalIDForObject

`public EOGlobalID globalIDForObject(EOEnterpriseObject object)`

Returns the EOGlobalID for _object_. All objects fetched from an external store are registered in an EOEditingContext along with a global identifier (EOGlobalID) that's used to uniquely identify each object to the external store. If _object_ hasn't been registered in the EOEditingContext or in its [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du) (that is, if no match is found), this method returns null. Objects are registered in an EOEditingContext using the [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2a) method, or, when fetching, with [recordObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswg33smrhwe2tfmn2a).

__See Also:__ [objectForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldordg64shnrxweylmjfca)

---

### hasChanges

`public boolean hasChanges()`

Returns true if any of the objects in the receiver's object graph have been modified-that is, if any objects have been inserted, deleted, or updated.

---

### initializeObject

`public void initializeObject( EOEnterpriseObject object, EOGlobalID globalID, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore to build the properties for the _object_ identified by _globalID_. When a parent EOEditingContext receives this on behalf of a child EOEditingContext (as represented by _anEditingContext_), and the _globalID_ identifies an object instantiated in the parent, the parent returns properties extracted from its object and translated into the child's context. This ensures that a nested context "inherits" modified values from its parent EOEditingContext. If the receiver doesn't have _object_, the request is forwarded the receiver's parent EOObjectStore.

---

### insertedObjects

`public NSArray insertedObjects()`

Returns the objects that have been inserted into the receiver's object graph.

__See Also:__ [deletedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y), [updatedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovygiylumvse6ytkmvrxi4y)

---

### insertObject

`public void insertObject(EOEnterpriseObject object)`

Registers (by invoking [insertObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2fo2lunbdwy33cmfwesra)) _object_ to be inserted in the receiver's parent EOObjectStore the next time changes are saved. In the meantime, _object_ is registered in the receiver with a temporary globalID.

__See Also:__ [insertedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorswit3cnjswg5dt), [deletedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y), [insertObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2fo2lunbdwy33cmfwesra)

---

### insertObjectWithGlobalID

`public void insertObjectWithGlobalID( EOEnterpriseObject anEOEnterpriseObject, EOGlobalID anEOGlobalID)`

Registers a new _object_ identified by _globalID_ that should be inserted in the parent EOObjectStore when changes are saved. Works by invoking [recordObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswg33smrhwe2tfmn2a), unless the receiver already contains the object. Sends _object_ the message awakeFromInsertion. _globalID_ must respond true to isTemporary. When the external store commits _object_, it re-records it with the appropriate permanent globalID.

It is an error to insert an object that's already registered in an editing context unless you are effectively undeleting the object by reinserting it.

__See Also:__ [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2a)

---

### invalidateAllObjects

`public void invalidateAllObjects()`

Overrides the implementation inherited from EOObjectStore to discard the values of objects cached in memory and refault them, which causes them to be refetched from the external store the next time they're accessed. This method sends the message __invalidateObjectsWithGlobalIDs__ to the parent object store with the globalIDs of all of the objects cached in the receiver. When an EOEditingContext receives this message, it propagates the message down the object store hierarchy. EODatabaseContexts discard their snapshots for invalidated objects and broadcast an [ObjectsChangedInStoreNotification](#apple-ijeuirceifbuu). (EODatabaseContext is defined in EOAccess.)

The final effect of this method is to refault all objects currently in memory. The next time you access one of these objects, it's refetched from the database.

To flush the entire application's cache of all values fetched from an external store, use a statement such as the following:

```
EOEditingContext.rootObjectStore().invalidateAllObjects();
```

If you just want to discard uncommitted changes but you don't want to sacrifice the values cached in memory, use the EOEditingContext [revert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojsxmzlsoq) method, which reverses all changes and clears the undo stack. For more discussion of this topic, see the section ["Methods for Managing the Object Graph" (page 78)](EOEditingContext.Concepts.md#apple-irauoqsbizeus).

__See Also:__ [refetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswmzlumnua), [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfj5rguzldorzvo2lunbdwy33cmfwesrdt)

---

### invalidateObjectsWithGlobalIDs

`public void invalidateObjectsWithGlobalIDs(NSArray globalIDs)`

Overrides the implementation inherited from EOObjectStore to signal to the parent object store that the cached values for the objects identified by _globalID_s should no longer be considered valid and that they should be refaulted. Invokes [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt) before refaulting the objects. This message is propagated to any underlying object store, resulting in a refetch the next time the objects are accessed. Any related (child or peer) object stores are notified that the objects are no longer valid. All uncommitted changed to the objects are lost. For more discussion of this topic, see the section ["Methods for Managing the Object Graph" (page 78)](EOEditingContext.Concepts.md#apple-irauoqsbizeus).

__See Also:__ [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt)

---

### invalidatesObjectsWhenFinalized

`public boolean invalidatesObjectsWhenFinalized()`

Returns true to indicate that the receiver clears and "booby-traps" all of the objects registered with it when the receiver is finalized, false otherwise. The default is true. In this method, "invalidate" has a different meaning than it does in the other __invalidate...__ methods.

---

### invokeRemoteMethod

`public Object invokeRemoteMethod( EOEditingContext editingContext, EOGlobalID globalID, String methodName, Class[] argumentTypes Object[] objects)`

Executes a remote method on the server. This method has the side effect of saving the changes in the receiver to the editing context in the server session. Note that none of the arguments or the result should be enterprise objects: use globalIDs to specify enterprise objects. The _argumentTypes_ argument holds the types of the remote method's (specified by _methodName_) arguments.

---

### isObjectLockedWithGlobalID

`public boolean isObjectLockedWithGlobalID( EOGlobalID globalID, EOEditingContext anEditingContext)`

Returns true if the object identified by _globalID_ in _anEditingContext_ is locked, false otherwise. This method works by forwarding the message __isObjectLockedWithGlobalID__ to its parent object store.

__See Also:__ [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfca), [locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg23tj5rguzldorzuezlgn5zgkrtjojzxitlpmruwm2ldmf2gs33o)

---

### lock

`public void lock()`

Locks access to the receiver to prevent other threads from accessing it. If the receiver has a [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du), the receiver takes a reader lock on it, as well. You should lock an editing context when you are accessing or modifying objects managed by the editing context. The thread-safety provided by Enterprise Objects Framework allows one thread to be active in each EOEditingContext and one thread to be active in each EODatabaseContext (EOAccess). In other words, multiple threads can access and modify objects concurrently in different editing contexts, but only one thread can access the database at a time (to save, fetch, or fault).

This method creates an NSAutoreleasePool that is released when __unlock__ is called. Consequently, objects that have been autoreleased within the scope of a __lock__/__unlock__ pair may not be valid after the __unlock__.

Similarly, when you catch exceptions, you need to retain the local exception before raising because the exception is in the lock's pool.

---

### lockObject

`public void lockObject(EOEnterpriseObject anObject)`

Attempts to lock _anObject_ in the external store. This method works by invoking [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfca). Throws an exception if it can't find the globalID for _anObject_ to pass to __lockObjectWithGlobalID__.

__See Also:__ [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq), [locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg23tj5rguzldorzuezlgn5zgkrtjojzxitlpmruwm2ldmf2gs33o)

---

### lockObjectWithGlobalID

`public void lockObjectWithGlobalID( EOGlobalID globalID, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore to attempt to lock the object identified by _globalID_ in _anEditingContext_ in the external store. Throws an exception if unable to obtain the lock. This method works by forwarding the message __lockObjectWithGlobalID__ to its parent object store.

__See Also:__ [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq), [locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg23tj5rguzldorzuezlgn5zgkrtjojzxitlpmruwm2ldmf2gs33o)

---

### locksObjectsBeforeFirstModification

`public boolean locksObjectsBeforeFirstModification()`

Returns true if the receiver locks _object_ in the external store (with [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u)) the first time _object_ is modified.

__See Also:__ [setLocksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxitdpmnvxgt3cnjswg5dtijswm33smvdgs4ttorgw6zdjmzuwgylunfxw4), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq), [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfca)

---

### messageHandler

`public Object messageHandler()`

Returns the EOEditingContext's message handler. A message handler is a special-purpose delegate responsible for presenting errors to the user. Typically, an EODisplayGroup (EOInterface) registers itself as the message handler for its EOEditingContext. For more information, see the EOEditingContext.MessageHandler interface specification.

__See Also:__ [setMessageHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxitlfonzwcz3fjbqw4zdmmvza)

---

### objectForGlobalID

`public EOEnterpriseObject objectForGlobalID(EOGlobalID globalID)`

Returns the object identified by _globalID_, or null if no object has been registered in the EOEditingContext (or its [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du)) with _globalID_.

__See Also:__ [globalIDForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpm5wg6ytbnreuirtpojhwe2tfmn2a)

---

### objectsForSourceGlobalID

`public NSArray objectsForSourceGlobalID( EOGlobalID globalID, String name, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore to service a to-many fault for a relationship named _name_. When a parent EOEditingContext receives a __objectsForSourceGlobalID__ message on behalf of a child editing context and _globalID_ matches an object instantiated in the parent, the parent returns a copy of its relationship array and translates its objects into the child editing context. This ensures that a child editing context "inherits" modified values from its parent. If the receiving editing context does not have the specified object or if the parent's relationship property is still a fault, the request is fowarded to its parent object store.

---

### objectsWithFetchSpecification

`public NSArray objectsWithFetchSpecification(EOFetchSpecification fetchSpecification)`

`public NSArray objectsWithFetchSpecification( EOFetchSpecification fetchSpecification, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore to fetch objects from an external store according to the criteria specified by _fetchSpecification_ and return them in an array. If one of these objects is already present in memory, this method doesn't overwrite its values with the new values from the database. This method throws an exception if an error occurs; the error message indicates the nature of the problem.

When an EOEditingContext receives this message, it forwards the message to its root object store. Typically the root object store is an EOObjectStoreCoordinator with underlying EODatabaseContexts. In this case, the object store coordinator forwards the request to the appropriate database context based on the entity name in _fetchSpecification_. The database context then obtains an EODatabaseChannel and performs the fetch, registering all fetched objects in _anEditingContext_ or in the receiver if _anEditingContext_ isn't provided. (Note that EODatabaseContext and EODatabaseChannel are defined in EOAccess.)

---

### objectWillChange

`public void objectWillChange(Object object)`

This method is automatically invoked when any of the objects registered in the receiver invokes its willChange method. This method is EOEditingContext's implementation of the EOObserving protocol.

---

### parentObjectStore

`public EOObjectStore parentObjectStore()`

Returns the EOObjectStore from which the receiver fetches and to which it saves objects.

---

### processRecentChanges

`public void processRecentChanges()`

Forces the receiver to process pending insertions, deletions, and updates.Normally, when objects are changed, the processing of the changes is deferred until the end of the current event. At that point, an EOEditingContext moves objects to the inserted, updated, and deleted lists, delete propagation is performed, undos are registered, and [ObjectsChangedInStoreNotification](#apple-ijeuirceifbuu) and [ObjectsChangedInEditingContextNotification](#apple-ijeuiq2gjbeem) are posted. You can use this method to explicitly force changes to be processed. An EOEditingContext automatically invokes this method on itself before performing certain operations such as [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom). This method does nothing in Java Client applications.

---

### propagatesDeletesAtEndOfEvent

`public boolean propagatesDeletesAtEndOfEvent()`

Returns true if the receiver propagates deletes at the end of the event in which a change was made, false if it propagates deletes only right before saving changes. The default is true.

__See Also:__ [setPropagatesDeletesAtEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiudsn5ygcz3borsxgrdfnrsxizltif2ek3tej5tek5tfnz2a)

---

### recordObject

`public void recordObject( EOEnterpriseObject object, EOGlobalID globalID)`

Makes the receiver aware of an object identified by _globalID_ existing in its parent object store. EOObjectStores (such as the access layer's EODatabaseContext) usually invoke this method for each object fetched. When it receives this message, the receiver enters the object in its uniquing table and registers itself as an observer of the object.

---

### redo

`public void redo()`

Sends editingContextWillSaveChanges messages to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq), and sends a __redo__ message to the receiver's NSUndoManager, asking it to reverse the latest undo operation applied to objects in the object graph.

__See Also:__ [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovxgi3y)

---

### refaultObject

`public void refaultObject( EOEnterpriseObject anObject, EOGlobalID globalID, EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore to refault the enterprise object _object_ identified by _globalID_ in _anEditingContext_. This method should be used with caution since refaulting an object does not remove the object snapshot from the undo stack. Objects that have been newly inserted or deleted should not be refaulted.

The main purpose of this method is to break reference cycles between enterprise objects. For example, suppose you have an Employee object that has a to-one relationship to its Department, and the Department object in turn has an array of Employee objects. You can use this method to break the reference cycle. Note that reference cycles are automatically broken if the EOEditingContext is finalized. For more discussion of this topic, see the section ["Methods for Managing the Object Graph" (page 78)](EOEditingContext.Concepts.md#apple-irauoqsbizeus).

__See Also:__ [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfj5rguzldorzvo2lunbdwy33cmfwesrdt)

---

### refaultObjects

`public void refaultObjects()`

Refaults all objects cached in the receiver that haven't been inserted, deleted, or updated. Invokes [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt), then invokes [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswmylvnr2e6ytkmvrxi) for all objects that haven't been inserted, deleted, or updated. For more discussion of this topic, see the section ["Methods for Managing the Object Graph" (page 78)](EOEditingContext.Concepts.md#apple-irauoqsbizeus) in the class description.

---

### refetch

`public void refetch()`

Sends editingContextWillSaveChanges messages to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq), and invokes the [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt)method.

---

### registeredObjects

`public NSArray registeredObjects()`

Returns the enterprise objects managed by the receiver.

---

### removeEditor

`public void removeEditor(Object anObject)`

Unregisters _editor_ from the receiver. For more discussion of EOEditors, see the [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq) method description and the EOEditingContext.Editors interface specification.

__See Also:__ [addEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmfsgirlenf2g64q)

---

### reset

`public void reset()`

Forgets all objects and makes them unusable. This method also resets the [fetchTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzsxiy3ikruw2zltorqw24a) as if the editing context were just initialized.

---

### revert

`public void revert()`

Sends editingContextWillSaveChanges messages to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq), and removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values. Does not refetch from the database. Note that __revert__ doesn't automatically cause higher level display groups (WebObject's WODisplayGroups or the interface layer's EODisplayGroups) to refetch. Display groups that allow insertion and deletion of objects need to be explicitly synchronized whenever this method is invoked on their EOEditingContext.

__See Also:__ [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt)

---

### rootObjectStore

`public EOObjectStore rootObjectStore()`

Returns the EOObjectStore at the base of the object store hierarchy (usually an EOObjectStoreCoordinator).

---

### saveChanges

`public void saveChanges()`

Sends editingContextWillSaveChanges messages to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq), and commits changes made in the receiver to its parent EOObjectStore by sending it the message [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a). If the parent is an EOObjectStoreCoordinator, it guides its EOCooperatingObjectStores, typically EODatabaseContexts, through a multi-pass save operation (see the EOObjectStoreCoordinator class specification for more information). If a database error occurs, an exception is thrown. The error message indicates the nature of the problem.

`public void saveChanges(Object anObject)`

Invokes the no-argument version, handling an exception using the message handler. For example, if a validation error occurs, the message handler (usually an EODisplayGroup) presents an alert panel with the text of the validation exception.

---

### saveChangesInEditingContext

`public void saveChangesInEditingContext(EOEditingContext anEditingContext)`

Overrides the implementation inherited from EOObjectStore to tell the receiver's EOObjectStore to accept changes from a child EOEditingContext. This method shouldn't be invoked directly. It's invoked by a nested EOEditingContext when it's committing changes to a parent EOEditingContext. The receiving parent EOEditingContext incorporates all changes from the nested EOEditingContext into its own copies of the objects, but it doesn't immediately save those changes to the database. If the parent itself is later sent [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom), it propagates any changes received from the child along with any other changes to its parent EOObjectStore. Throws an exception if an error occurs; the error message indicates the nature of the problem.

---

### setDelegate

`public void setDelegate(Object anObject)`

Set the receiver's delegate to be _anObject_.

__See Also:__ [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlhmf2gk)

---

### setFetchTimestamp

`public void setFetchTimestamp(long timestamp)`

Sets the receiver's fetch timestamp. When an editing context fetches objects from its parent object store, the parent object store can use the timestamp to determine whether to use cached data or to refetch the most current values. An editing context prefers that fetched values are at least as recent as its fetch timestamp. Note that the parent object store is free to ignore the timestamp; so this value should be considered a hint or request and not a guarantee.

|  |
| --- |
| __Note:__ Changing the fetch timestamp has no effect on existing objects in the editing context; it can affect only subsequent fetches. To refresh existing objects, invoke __refaultObjects__ before you invoke __setFetchTimestamp:__. |

The initial value for the fetch timestamp of a new non-nested editing context is the current time less the __defaultFetchTimestampLag__. A nested editing context always uses its parent's fetch timestamp. __setFetchTimestamp:__ raises if it's invoked on a nested editing context.

---

### __setInvalidatesObjectsWhenFinalized__

`public void setInvalidatesObjectsWhenFinalized(boolean flag)`

Description forthcoming.

---

### setSharedEditingContext

`public void setSharedEditingContext(EOSharedEditingContext sharedEC)`

Sets the receiver's shared editing context. Raises if the receiver and _sharedEC_ both contain the same object (otherwise object uniquing would be violated) or if _sharedEC_ is not an instance of the EOSharedEditingContext class.By default, an editing context that has no shared editing context listens for DefaultSharedEditingContextWasInitializedNotifications. If a notification is posted while the context has no registered objects, the editing context sets its shared editing context to the newly initialized default shared editing context. Invoke this method with null to remove the receiver as an observer of this notification and to prevent the context from accessing any objects in the default shared editing context.

---

### setLocksObjectsBeforeFirstModification

`public void setLocksObjectsBeforeFirstModification(boolean flag)`

Sets according to _flag_ whether the receiver locks _object_ in the external store (with [lockObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg22pmjvgky3u)) the first time _object_ is modified. The default is false. If _flag_ is true, an exception will be thrown if a lock can't be obtained when _object_ invokes willChange. There are two reasons a lock might fail: because the row is already locked in the server, or because your snapshot is out of date. If your snapshot is out of date, you can explicitly refetch the object using an EOFetchSpecification with setRefreshesRefetchedObjects set to true. To handle the exception, you can implement the EODatabaseContext delegate method __databaseContextShouldRaiseExceptionForLockFailure:__.

You should avoid using this method or pessimistic locking in an interactive end-user application. For example, a user might make a change in a text field and neglect to save it, thereby leaving the data locked in the server indefinitely. Consider using optimistic locking or application level explicit check-in/check-out instead.

__See Also:__ [locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg23tj5rguzldorzuezlgn5zgkrtjojzxitlpmruwm2ldmf2gs33o)

---

### setMessageHandler

`public void setMessageHandler(Object handler)`

Set the receiver's message handler to be _handler_.

__See Also:__ [messageHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnvsxg43bm5suqylomrwgk4q)

---

### setPropagatesDeletesAtEndOfEvent

`public void setPropagatesDeletesAtEndOfEvent(boolean flag)`

Sets according to _flag_ whether the receiver propagates deletes at the end of the event in which a change was made, or only just before saving changes.

If _flag_ is true, deleting an enterprise object triggers delete propagation at the end of the event in which the deletion occurred (this is the default behavior). If _flag_ is false, delete propagation isn't performed until [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom) is invoked.

You can delete enterprise objects explicitly by using the [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvhwe2tfmn2a) method or implicitly by removing the enterprise object from an owning relationship. Delete propagation uses the delete rules in the EOClassDescription to determine whether objects related to the deleted object should also be deleted (for more information, see the EOClassDescription class specification and the EOEnterpriseObject interface informal protocol specification). If delete propagation fails (that is, if an enterprise object refuses to be deleted-possibly due to a deny rule), all changes made during the event are rolled back.

__See Also:__ [propagatesDeletesAtEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg64dbm5qxizltirswyzlumvzuc5cfnzse6zsfozsw45a)

---

### setStopsValidationAfterFirstError

`public void setStopsValidationAfterFirstError(boolean flag)`

Sets according to _flag_ whether the receiver stops validating after the first error is encountered, or continues for all objects (validation typically occurs during a save operation). The default is true. Setting it to false is useful if the delegate implements editingContextShouldPresentException to handle the presentation of aggregate exceptions.

__See Also:__ [stopsValidationAfterFirstError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpon2g64dtkzqwy2lemf2gs33oifthizlsizuxe43uivzhe33s)

---

### setUndoManager

`public void setUndoManager(NSUndoManager undoManager)`

Sets the receiver's NSUndoManager to _undoManager_. You might invoke this method with null if your application doesn't need undo and you want to avoid the overhead of an undo stack. For more information on editing context's undo support, see the section ["Undo and Redo" (page 77)](EOEditingContext.Concepts.md#apple-irauoq2eivcuo).

__See Also:__ [undoManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovxgi32nmfxgcz3foi)

---

### sharedEditingContext

`public EOSharedEditingContext sharedEditingContext()`

Returns the shared editing context used by the receiver.

---

### stopsValidationAfterFirstError

`public boolean stopsValidationAfterFirstError()`

Returns true to indicate that the receiver should stop validating after it encounters the first error, or false to indicate that it should continue for all objects.

__See Also:__ [setStopsValidationAfterFirstError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxiu3un5yhgvtbnruwiylunfxw4qlgorsxertjojzxirlsojxxe)

---

### __tryToSaveChanges__

`public Throwable tryToSaveChanges()`

Description forthcoming.

---

### undo

`public void undo()`

Sends editingContextWillSaveChanges messages to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmvsgs5dpojzq), and sends an undo message to the receiver's NSUndoManager, asking it to reverse the latest uncommitted changes applied to objects in the object graph. For more information on editing context's undo support, see the section ["Undo and Redo" (page 77)](EOEditingContext.Concepts.md#apple-irauoq2eivcuo).

__See Also:__ [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswi3y)

---

### undoManager

`public NSUndoManager undoManager()`

Returns the receiver's NSUndoManager.

__See Also:__ [setUndoManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxivlomrxu2ylomftwk4q)

---

### unlock

`public void unlock()`

Unlocks access to the receiver so that other threads may access it. If the receiver has a [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du), the receiver unlocks a reader lock on the shared context.

__See Also:__ [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnrxwg2y)

---

### updatedObjects

`public NSArray updatedObjects()`

Returns the objects in the receiver's object graph that have been updated.

__See Also:__ [deletedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y), [insertedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorswit3cnjswg5dt)

---

## Notifications

---

The following notifications are declared (except where otherwise noted) and posted by EOEditingContext.

### EditingContextDidSaveChangesNotification

`public static final String EditingContextDidSaveChangesNotification`

This notification is broadcast after changes are saved to the EOEditingContext's parent EOObjectStore. The notification contains: Notification ObjectThe EOEditingContextuserInfoA dictionary with the following keys (constants) and values

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| `EOObjectStore.`UpdatedKey | An NSArray containing the changed objects |
| `EOObjectStore.`InsertedKey | An NSArray containing the inserted objects |
| `EOObjectStore.`DeletedKey | An NSArray containing the deleted objects |

### InvalidatedAllObjectsInStoreNotification

This notification is defined by EOObjectStore. When posted by an EOEditingContext, it's the result of the editing context invalidating all its objects. When an EOEditingContext receives an `InvalidatedAllObjectsInStoreNotification` from its parent EOObjectStore, it clears its lists of inserted, updated, and deleted objects, and resets its undo stack. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The EOEditingContext |
| userInfo Dictionary | None. |

An interface layer EODisplayGroup (not a WebObjects WODisplayGroup) listens for this notification to refetch its contents. See the EOObjectStore class specification for more information on this notification.

### ObjectsChangedInStoreNotification

This notification is defined by EOObjectStore. When posted by an EOEditingContext, it's the result of the editing context processing [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorlws3dminugc3thmu) observer notifications in [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt), which is usually as the end of the event in which the changes occurred. See the EOObjectStore class specification for more information on `ObjectsChangedInStoreNotification`.

This notification contains:

Notification ObjectThe EOEditingContextuserInfoA dictionary with the following keys (constants) and values

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| `EOObjectStore.`UpdatedKey | An NSArray of EOGlobalIDs for objects whose properties have changed. A receiving EOEditingContext typically responds by refaulting the objects. |
| `EOObjectStore.`InsertedKey | An NSArray of EOGlobalIDs for objects that have been inserted into the EOObjectStore. |
| `EOObjectStore.`DeletedKey | An NSArray of EOGlobalIDs for objects that have been deleted from the EOObjectStore. |
| `EOObjectStore.`InvalidatedKey | An NSArray of EOGlobalIDs for objects that have been turned into faults. Invalidated objects are those for which the cached view should no longer be trusted. Invalidated objects should be refaulted so that they are refetched when they're next examined. |

### ObjectsChangedInEditingContextNotification

`public static final String ObjectsChangedInEditingContextNotification`

This notification is broadcast whenever changes are made in an EOEditingContext. It's similar to `ObjectsChangedInStoreNotification`, except that it contains objects rather than globalIDs. The notification contains: Notification ObjectThe EOEditingContextuserInfoA dictionary with the following keys (constants) and values

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| `EOObjectStore.`UpdatedKey | An NSArray containing the changed objects |
| `EOObjectStore.`DeletedKey | An NSArray containing the deleted objects |
| `EOObjectStore.`InsertedKey | An NSArray containing the inserted objects |
| `EOObjectStore.`InvalidatedKey | An NSArray containing invalidated objects. |

Interface layer EODisplayGroups (not WebObjects WODisplayGroups) listen for this notification to redisplay their contents.

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
