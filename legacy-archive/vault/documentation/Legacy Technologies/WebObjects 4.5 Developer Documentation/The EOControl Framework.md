---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Introduction.html
archived_at: '2026-07-15T08:11:38.793604Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](EOControlTOC.md)

# The EOControl Framework

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Introduction

The EOControl framework defines one of the layers of the Enterprise
Objects Framework architecture-the control layer. It provides
an infrastructure for enterprise objects that is independent of
your application's user interface and its storage mechanism. The
control layer dynamically manages the interaction between enterprise
objects, the access layer, and the interface layer by:

- Tracking changes to enterprise objects
- Prompting the user interface to change when object values
  change
- Prompting the database to change when changes to objects are
  committed
- Managing undo in the object graph
- Managing uniquing (the mechanism by which Enterprise Objects
  Framework uniquely identifies enterprise objects and maintains their
  mapping to stored data in the database)

The control layer's major areas of responsibility and the
key classes involved are described in the following table:

|  |  |
| --- | --- |
| __Responsibility__ | __Classes__ |
| ["Tracking Enterprise Objects Changes"](#apple-ijeucrchivauo) | [EOObserverCenter](EOObserverCenter.md#apple-ivhu6yttmvzhmzlsinsw45dfoi)   [EODelayedObserverQueue](EODelayedObserverQueue.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovsq)   [EODelayedObserver](EODelayedObserver.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvza)   [EOObserverProxy](EOObserverProxy.md#apple-ivhu6yttmvzhmzlskbzg66dz)   [EOObserving](EOObserving.md#apple-ijaumqsbjbcuk) (interface) |
| ["Object Storage Abstraction"](#apple-ijeucq2bjffek) | [EOObjectStore](EOObjectStore.md#apple-ivhu6ytkmvrxiu3un5zgk)   [EOCooperatingObjectStore](EOCooperatingObjectStore.md#apple-ivhug33pobsxeylunfxgot3cnjswg5ctorxxezi) (com.apple.yellow.eocontrol only)   [EOObjectStoreCoordinator](EOObjectStoreCoordinator.md#apple-ivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64q) (com.apple.yellow.eocontrol only)   [EOGlobalID](EOGlobalID.md#apple-ivhuo3dpmjqwyske)   [EOKeyGlobalID](EOKeyGlobalID.md#apple-ivhuwzlzi5wg6ytbnreui)   [EOTemporaryGlobalID](EOTemporaryGlobalID.md#apple-ivhvizlnobxxeylspfdwy33cmfwesra) |
| Query specification | [EOFetchSpecification](EOFetchSpecification.md#apple-ijduoqsjjfbeq)   [EOQualifier](EOQualifier.md#apple-ijbesrcgjfees)   [EOSortOrdering](EOSortOrdering.md#apple-onxxe5cpojsgk4tjnztvo2lunbfwk6k7onswyzldorxxexy) |
| Interaction with enterprise objects | [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq) (basic enterprise object behavior)   [EOClassDescription](EOClassDescription.md#apple-ivhug3dbonzuizltmnzgs4dunfxw4) (validation support)   [EOGenericRecord](EOGenericRecord.md#apple-ivhuozlomvzgsy2smvrw64te)   [EOCustomObject](EOCustomObject.md#apple-inbuuq2jifauc) |
| Simple source of objects (for display groups) | [EODataSource](EODataSource.md#apple-ivhuiylumfjw65lsmnsq)   [EODetailDataSource](EODetailDataSource.md#apple-ineeurcdjjbus) |

The following sections describe each responsibility in greater
detail.

## Tracking Enterprise Objects Changes

EOControl provides four classes and an interface that form
an efficient, specialized mechanism for tracking changes to enterprise
objects and for managing the notification of those changes to interested observers.
EOObserverCenter is the central manager of change notification.
It records observers and the objects they observe, and it distributes
notifications when the observable objects change. Observers implement
the EOObserving interface, which defines one method, [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu).
Observable objects (generally enterprise objects) invoke their [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) method before altering
their state, which causes all observers to receive an [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) message.

The other three classes add to the basic observation mechanism.
EODelayedObserverQueue alters the basic, synchronous change notification
mechanism by offering different priority levels, which allows observers
to specify the order in which they're notified of changes. EODelayedObserver
is an abstract superclass for objects that observe other objects
(such as the EOInterface layer's EOAssociation classes). Finally,
EOObserverProxy is a subclass of EODelayedObserver that forwards
change messages to a target object, allowing objects that don't
inherit from EODelayedObserver to take advantage of this mechanism.

The major observer in Enterprise Objects Framework is EOEditingContext,
which implements its [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) method
to record a snapshot for the object about to change, register undo
operations in an NSUndoManager, and record the changes needed to
update objects in its EOObjectStore. Because some of these actions-such
as examining the object's new state-can only be performed after
the object has changed, an EOEditingContext sets up a delayed message
to itself, which it gets at the end of the run loop. Observers that
only need to examine an object after it has changed can use the
delayed observer mechanism, described in the EODelayedObserver and
EODelayedObserverQueue class specifications.

## Object Storage Abstraction

The control layer provides an infrastructure that's independent
of your application's storage mechanism (typically a database)
by defining an API for an "intelligent" repository of objects,
whether it's based on external data or whether it manages objects
entirely in memory. EOObjectStore is an abstract class that defines
that basic API, setting up the framework for constructing and registering enterprise
objects, servicing object faults, and committing changes made in
an EOEditingContext. Subclasses of EOObjectStore implement the API
in terms of their specific storage mechanism.

## Subclasses of EOObjectStore

EOEditingContext is the principal subclass of EOObjectStore
and is used for managing objects in memory. For stores based on
external data, there are several subclasses. EOCooperatingObjectStore defines
stores that work together to manage data from several distinct sources
(such as different databases). The access layer's EODatabaseContext
is actually a subclass of this class. A group of cooperating stores
is managed by another subclass of EOObjectStore, EOObjectStoreCoordinator.
If you're defining a subclass of EOObjectStore, it's probably
one based on an external data repository, and it should therefore
inherit from EOCooperatingObjectStore so as to work well with an EOObjectStoreCoordinator-though
this isn't required.

EODatabaseContext provides objects from relational databases
and is therefore provided by Enterprise Objects Framework's access
layer. It is the class that defines the interaction between the
control and access layers. Database contexts and other object stores
based on external data are often shared by several editing contexts
to conserve database connections.

Object store subclasses cooperate with one another as illustrated
in the following:

![[image: Classes/Art/DBasic2.GIF]](Classes/Art/DBasic2.GIF)

|  |
| --- |
| __Note:__  Note that EOCooperatingObjectStore, EOObjectStoreCoordinator, and EODatabaseContext are not provided by Java Client |

## Registering Enterprise Objects

An object store identifies its objects in two ways:

- By reference for identification within a specific
  editing context
- By global ID for universal identification of the same record
  among multiple stores.

A global ID is defined by three classes: EOGlobalID, EOKeyGlobalID,
and EOTemporaryGlobalID. EOGlobalID is an abstract class that forms
the basis for uniquing in Enterprise Objects Framework. EOKeyGlobalID
is a concrete subclass of EOGlobalID whose instances represent persistent
IDs based on the access layer's EOModel information: an entity
and the primary key values for the object being identified. An EOTemporaryGlobalID
object is used to identify a newly created enterprise object before it's
saved to an external store. For more information, see the [EOGlobalID](EOGlobalID.md#apple-ivhuo3dpmjqwyske) class specification.

## Servicing Faults

For external repositories, an object store might delay fetching
an object's data, instead creating an empty enterprise object
(called a fault). When a fault is accessed (sent a message), it
triggers its object store to fetch its data and fill the fault with
its data. This preserves both the object's reference and
its EOGlobalID, while saving the cost of fetching data that might
not be used. Faults are typically created for the destinations of
relationships for objects that are explicitly fetched. See the [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q) class specification for
more information.

[![Table of Contents](attachments/images/up.gif)](EOControlTOC.md)
