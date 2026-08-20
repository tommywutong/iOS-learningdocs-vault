---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Client/Classes/EODistributedObjectStore.html
archived_at: '2026-07-15T08:13:48.558400Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md) 

# EODistributedObjectStore

> **__Inherits from:__**
> : com.webobjects.eocontrol.EOObjectStore

> **__Package:__**
> : com.webobjects.eodistribution.client

---

## Class Description

---

An EODistributedObjectStore functions as an object store on the Java client. It handles interaction with the distribution layer's channel (an EODistributionChannel object), incorporating knowledge of that channel so it can forward messages it receives from the server to its editing contexts and forward messages from its editing contexts to the server. With the channel, it represents a single connection to the server, fetching and saving objects on behalf of one or more client-side editing contexts. In this regard, an EODistributedObjectStore acts like an EODatabaseContext on the server; it differs from EODatabaseContext in that its editing contexts interact directly with it without the intervention of an object store coordinator.

EODistributedObjectStore provides several methods in addition to those defined by EOObjectStore. The invocation methods [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozxwwzksmvww65dfjvsxi2dpmq) (two overloaded versions) and [invokeRemoteMethodWithKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozxwwzksmvww65dfjvsxi2dpmrlws5dijnsxsudborua) allow you to send messages to any object on the server and receive responses from them. The methods [classDescriptionForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6y3mmfzxgrdfonrxe2lqoruw63sgn5zeo3dpmjqwyske) and [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreui) return information related to enterprise objects in the distributed object store given an object's global ID.

## Method Types

---

> **Initializing objects**
>
> : [initializeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62lonf2gsylmnf5gkt3cnjswg5a)
>
> **Getting objects**
>
> : [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss633cnjswg5dtk5uxi2cgmv2gg2ctobswg2lgnfrwc5djn5xa): [objectsForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss633cnjswg5dtizxxeu3povzggzkhnrxweylmjfca)
>
> **Getting faults**
>
> : [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6ztbovwhirtpojdwy33cmfwesra): [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6ylsojqxsrtbovwhiv3jorufg33vojrwkr3mn5rgc3cjiq): [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss64tfmzqxk3duj5rguzldoq)
>
> **Saving changes to objects**
>
> : [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du)
>
> **Invalidating objects**
>
> : [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozqwy2lemf2gkqlmnrhwe2tfmn2hg): [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozqwy2lemf2gkt3cnjswg5dtk5uxi2chnrxweylmjfchg)
>
> **Invoking methods on the server**
>
> : [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozxwwzksmvww65dfjvsxi2dpmq): [invokeRemoteMethodWithKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozxwwzksmvww65dfjvsxi2dpmrlws5dijnsxsudborua)
>
> **Getting object data via global IDs**
>
> : [classDescriptionForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6y3mmfzxgrdfonrxe2lqoruw63sgn5zeo3dpmjqwyske): [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreui)

## Constructors

---

### EODistributedObjectStore

`public EODistributedObjectStore(EODistributionChannel aDistributionChannel)`

Returns an EODistributedObjectStore instance initialized with a distribution channel.

---

## Instance Methods

---

### arrayFaultWithSourceGlobalID

`public NSArray arrayFaultWithSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String relationshipName, com.webobjects.eocontrol.EOEditingContext editingContext)`

Creates a to-many fault in the editing context _editingContext_ and returns the destination objects for the to-many relationship identified by _relationshipName_; _globalID_ identifies the source object for the relationship (which doesn't necessarily exist in memory yet).

__See Also:__ [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6ztbovwhirtpojdwy33cmfwesra), [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss64tfmzqxk3duj5rguzldoq)

---

### classDescriptionForGlobalID

`public com.webobjects.eocontrol.EOClassDescription classDescriptionForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Returns the class description for the enterprise object identified by _globalID_.

__See Also:__ [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreui)

---

### faultForGlobalID

`public com.webobjects.eocontrol.EOEnterpriseObject faultForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext editingContext)`

Creates a to-one fault from the enterprise object identified by _globalID_, registers it in _editingContext_, and returns the fault. This method could return an already existing object.

__See Also:__ [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6ylsojqxsrtbovwhiv3jorufg33vojrwkr3mn5rgc3cjiq), [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss64tfmzqxk3duj5rguzldoq)

---

### initializeObject

`public void initializeObject( com.webobjects.eocontrol.EOEnterpriseObject anObject, com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext editingContext)`

Initializes the enterprise object _anObject_ with its attributes and relationships using key-value coding; the properties of _anObject_ are identified and accessed using the global ID _globalID_. For properties with EONullValues, a __null__ is substituted.

__See Also:__ [classDescriptionForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6y3mmfzxgrdfonrxe2lqoruw63sgn5zeo3dpmjqwyske)

---

### invalidateAllObjects

`public void invalidateAllObjects()`

Invoked to notify the receiver that all the properties it caches are no longer valid and that they should be refaulted. Any child object stores are also notified that the objects are no longer valid. Posts InvalidatedAllObjectsInStoreNotification after removing objects from the object store.

__See Also:__ [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozqwy2lemf2gkt3cnjswg5dtk5uxi2chnrxweylmjfchg)

---

### invalidateObjectsWithGlobalIDs

`public void invalidateObjectsWithGlobalIDs(NSArray gidArray)`

Invoked to notify the receiver that all of the objects identified by the global IDs in _gidArray_ are no longer valid. Any child object stores are also notified that the specified objects are no longer valid. After invalidating the objects, this method posts [ObjectsChangedInStoreNotification](#apple-inbuurcjivdeq).

---

### invokeRemoteMethod

`public Object invokeRemoteMethod( com.webobjects.eocontrol.EOEditingContext editingContext, com.webobjects.eocontrol.EOGlobalID globalID, String methodName, Class[] anArray Object[] arguments)`

`public Object invokeRemoteMethod( com.webobjects.eocontrol.EOEditingContext editingContext, com.webobjects.eocontrol.EOGlobalID globalID, String methodName, Object[] arguments, Class[] anArray boolean shouldPush)`

Invokes the method identified by _methodName_ on the server-side enterprise object identified by the editing context _editingContext_ and the EOGlobalID _globalID_. The result of the invocation is returned. The four-argument method (and the five-argument method, if _shouldPush_ is __true__) pushes all changes pending on the client to the server before sending the invocation; this ensures that the states of the server and client are synchronized before the method is executed. If for performance or other reasons you do not want to push pending changes to the server, use the second method with _shouldPush_ set to __false__. Note that the method without the _shouldPush_ argument typically originates with one of the receiver's editing contexts.

The EODistributionContext on the server by default refuses the remote invocation unless _methodName_ is prefixed with "clientSideRequest" or unless its delegate (usually the session object) implements the distributionContextShouldAllowInvocation method to return `true`. This mechanism exists to provide security on the server.

---

### invokeRemoteMethodWithKeyPath

`public Object invokeRemoteMethodWithKeyPath( com.webobjects.eocontrol.EOEditingContext editingContext, String keyPath, String methodName, Class[] anArray Object[] arguments, boolean shouldPush)`

This method is similar to [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozxwwzksmvww65dfjvsxi2dpmq) except for two things. The receiver of the invocation can be any object (not just an enterprise object) that can be specified with a key path (_keyPath_). The _keyPath_ argument has special semantics:

- If _keyPath_ is a fully qualified key path (for example, "session.editingContext") the key path is followed starting from the WOComponent that is the invocation target of the EODistributionContext.
- If _keyPath_ is an empty string, the method is invoked on the WOComponent that is the invocation target of the EODistributionContext (typically a subclass of WOJavaClientApplet).
- If _keyPath_ is `null`, the method is invoked on the server side EODistributionContext.

If an actual key path is specified, the EODistributionContext on the server blocks all invocations sent with this method unless _methodName_ is prefixed with "clientSideRequest" or unless the EODistributionContext's delegate (on the server) implements distributionContextShouldAllowInvocation _and_ distributionContextShouldFetchObjectsWithFetchSpecification. For security reasons, the delegate must authorize the invocation and the key path in these methods.

---

### objectsForSourceGlobalID

`public NSArray objectsForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String relationshipName, com.webobjects.eocontrol.EOEditingContext editingContext)`

Returns the destination objects for the to-many relationship identified by _relationshipName_. The source object for the relationship is identified by its global ID (_globalID_). The source object and all destination objects for the relationship belong to _editingContext_. This method first looks to find the destination objects for the relationship in a client-side cache; if that cache is empty, it requests the server to send it those objects and updates the client-side cache with them.

---

### objectsWithFetchSpecification

`public NSArray objectsWithFetchSpecification( com.webobjects.eocontrol.EOFetchSpecification fetchSpecification, com.webobjects.eocontrol.EOEditingContext editingContext)`

Fetches objects from the server according to the criteria specified by fetchSpecification and returns them in an array for inclusion in _editingContext_. Updates the client-side caches with the fetched enterprise objects. Throws an exception if an error occurs.

---

### refaultObject

`public void refaultObject( com.webobjects.eocontrol.EOEnterpriseObject anObject, com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext editingContext)`

Turns enterprise object _anObject_ back into a fault (an empty enterprise object, identified by _globalID_ in _editingContext_. Objects that have been inserted but not saved, or that have been deleted, shouldn't be refaulted.

__See Also:__ [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6ylsojqxsrtbovwhiv3jorufg33vojrwkr3mn5rgc3cjiq), [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6ztbovwhirtpojdwy33cmfwesra)

---

### saveChangesInEditingContext

`public void saveChangesInEditingContext(com.webobjects.eocontrol.EOEditingContext editingContext)`

Requests the server to commit changes to the enterprise objects in _editingContext_; this message is invoked by the editing context (_editingContext_). The receiver calls back to the editing context to get the updated, deleted, and inserted objects to save and commits these changes in a single transaction. Raises an exception if any error occurs.

---

### snapshotForSourceGlobalID

`public NSArray snapshotForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String relationshipName)`

Returns an array of global IDs identifying the destination objects for the to-many relationship _relationshipName_ having the source global ID of _globalID_. Returns __null__ if the object identified by the source global ID does not currently exist in the object store or if there is no relationship with the given name.

__See Also:__ [classDescriptionForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss6y3mmfzxgrdfonrxe2lqoruw63sgn5zeo3dpmjqwyske)

---

## Notifications

---

EOGlobalID's GlobalIDChangedNotification is posted when the global ID of an object in the store changes. See the EOGlobalID documentation for more information.

### InvalidatedAllObjectsInStoreNotification

This notification is posted when all objects in the object store are invalidated; see [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrhwe2tfmn2fg5dpojss62loozqwy2lemf2gkqlmnrhwe2tfmn2hg).

|  |  |
| --- | --- |
| Notification Object | `this` |
| userInfo Dictionary | None. |

### GlobalIDChangedNotification

This EOGlobalID notification is posted when the global ID of an object in the store changes.

|  |  |
| --- | --- |
| Notification Object | `this` |
| userInfo Dictionary | Use the old global ID as the key to find the new global ID. |

### ObjectsChangedInStoreNotification

This notification is posted on when specific objects in the object store are inserted, deleted, updated, or invalidated. This can happen as a result of an update from the server.

|  |  |
| --- | --- |
| Notification Object | `this` |
| userInfo Dictionary | The global IDs of inserted, deleted, updated, and invalidated objects, accessible with EOObjectStore's (respectively) InsertedKey, DeletedKey, UpdatedKey, and InvalidatedKey. |

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
