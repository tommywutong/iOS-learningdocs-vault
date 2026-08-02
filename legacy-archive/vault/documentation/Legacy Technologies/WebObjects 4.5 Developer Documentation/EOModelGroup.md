---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOModelGroup.html
archived_at: '2026-07-15T08:11:31.888303Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOModelGroup

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

An EOModelGroup represents an aggregation of related models
(see the [EOModel](EOModel.md#apple-ineeoq2iizduk) class
specification for more information on models). When a model in the
group needs to resolve a relationship to an entity in another model,
it looks for that model in its group. Model groups allow applications
to load entities and their properties only as they're needed,
by distributing them among separate EOModels.

The __default model group__ contains all models
for an application, as well as any frameworks the application references.
It is automatically created on demand. The entity name space among
all of these models is global; consequently, the same entity name
shouldn't appear in any two of the models. All cross-model information
is represented in the models by entity name only. Binding the entity
name to an actual entity is done at run-time within the EOModelGroup.

In the majority of applications, the automatic creation of
the default model group is sufficient. However, your code can override
this automatic creation; see ["Setting Up A Model Group Programmatically"](EOModelGroup-2.md#apple-ijbeorkbjbeuq).

## Accessing Models Within a Model Group

Each model lives within a group and can form connections to
other models in its group. A model can find a related model using
the statement:

> ```
> this.modelGroup().modelNamed(name);
> ```

A data source can locate a model using the statement:

> ```
> EOModelGroup.defaultGroup().modelNamed(name);
> ```

EOModeler puts models with identical names in separate groups
to allow you to load two models with the same name at the same time.

## EOModelGroup Delegates

Your EOModelGroup object should have a delegate which can
influence how it finds and loads models. In addition to the delegates
you assign to EOModelGroup instances, the EOModelGroup class itself
can have a delegate. The class delegate implements a single method- [defaultModelGroup](EOModelGroup.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya)-while
the instance delegate can implement the methods defined in the EOModelGroup.Delegate interface.
For more information on EOModelGroup class delegate and instance
delegate methods, see the [EOModelGroup.ClassDelegate](EOModelGroup.ClassDelegate.md#apple-indeerckizduo) and [EOModelGroup.Delegate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#CBACDGDA) interface specifications,
respectively. Note that the following delegate methods are set on
EOModelGroup, rather than EOEntity, to provide a single point in
the code where you can alter the database-to-objects mapping:

- [classForObjectWithGlobalID](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#//apple_ref/java/intfm/EOModelGroup.Delegate/classForObjectWithGlobalID)
- [entityFailedToLookupClassNamed](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#//apple_ref/java/intfm/EOModelGroup.Delegate/entityFailedToLookupClassNamed)
- [entityRelationshipForRow](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#//apple_ref/java/intfm/EOModelGroup.Delegate/entityRelationshipForRow)
- [subEntityForEntity](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#//apple_ref/java/intfm/EOModelGroup.Delegate/subEntityForEntity)

## Constants

---

EOModelGroup defines String constants for the names of the
notifications it posts. For more information on these notifications,
see ["Notifications"](#apple-ijbeoq2dizdui).

## Method Types

---

> **Accessing models**
> : [addModelWithPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5qwizcnn5sgk3cxnf2gqudborua)
> : [modelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrhgc3lfmq)
> : [modelNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrhgc3lfom)
> : [models](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrzq)
> : [modelWithPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrlws5dikbqxi2a)
> : [removeModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5zgk3lpozsu233emvwa)
>
> **Accessing model groups**
> : [defaultGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3emvtgc5lmordxe33voa)
> : [setDefaultGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eizlgmf2wy5chojxxk4a)
> : [globalModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3hnrxweylmjvxwizlmi5zg65lq)
> : [modelGroupForObjectStoreCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3nn5sgk3chojxxk4cgn5ze6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64q)
> : [setModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2e233emvweo4tpovya)
>
> **Searching a group**
> : [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5sw45djor4u4ylnmvsa)
> : [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5sw45djor4um33sj5rguzldoq)
> : [entitiesWithSharedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5sw45djoruwk42xnf2gqu3imfzgkzcpmjvgky3uom)
> : [fetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5tgk5ddnbjxazldnftgsy3boruw63somfwwkza)
> : [storedProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5zxi33smvsfa4tpmnswi5lsmvhgc3lfmq)
>
> **Loading all of a group's
> objects**
> : [loadAllModelObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5wg6yleifwgytlpmrswyt3cnjswg5dt)
>
> **Assigning a delegate**
> : [classDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3dnrqxg42emvwgkz3borsq)
> : [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5sgk3dfm5qxizi)
> : [setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eg3dbonzuizlmmvtwc5df)
> : [setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eg3dbonzuizlmmvtwc5df)

## Static Methods

---

### classDelegate

`public static Object classDelegate()`

Returns the EOModelGroup's class delegate.
This delegate optionally implements the [defaultModelGroup](EOModelGroup.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya) method
(see the [EOModelGroup.ClassDelegate](EOModelGroup.ClassDelegate.md#apple-indeerckizduo) interface specification
for more information).

__See Also:__  [setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eg3dbonzuizlmmvtwc5df)

---

### defaultGroup

`public static EOModelGroup defaultGroup()`

Returns the default EOModelGroup. Unless you've
either specified a default model group with [setDefaultGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eizlgmf2wy5chojxxk4a) or
implemented the [defaultModelGroup](EOModelGroup.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya) class
delegate method to return a non-`null` value,
this method is equivalent to [globalModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3hnrxweylmjvxwizlmi5zg65lq).

__See
Also:__  [classDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3dnrqxg42emvwgkz3borsq)

---

### globalModelGroup

`public static EOModelGroup globalModelGroup()`

Returns an EOModelGroup composed of all models
in the resource directory of the main bundle, as well as those in
all the bundles and frameworks loaded into the application.

__See
Also:__  [defaultGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3emvtgc5lmordxe33voa)

---

### modelGroupForObjectStoreCoordinator

`public static EOModelGroup modelGroupForObjectStoreCoordinator(com.apple.yellow.eocontrol.EOObjectStoreCoordinator anObjectStoreCoordinator)`

Returns the EOModelGroup used by _anObjectStoreCoordinator_.

__See
Also:__  [setModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2e233emvweo4tpovya)

---

### setClassDelegate

`public static void setClassDelegate(Object anObject)`

Assigns _anObject_ as
the EOModelGroup's class delegate. The class delegate is optional;
it allows you to determine the default model group (see the [EOModelGroup.ClassDelegate](EOModelGroup.ClassDelegate.md#apple-indeerckizduo) interface specification
for more information).

__See Also:__  [classDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3dnrqxg42emvwgkz3borsq), [defaultModelGroup](EOModelGroup.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya)

---

### setDefaultGroup

`public static void setDefaultGroup(EOModelGroup group)`

Sets the default model group to _group_.
If you've implemented the [defaultModelGroup](EOModelGroup.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya) class
delegate method to return a non-`null` value,
the delegate's return value overrides _group_ as
the default model group.

__See Also:__  [defaultGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3emvtgc5lmordxe33voa), [setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eg3dbonzuizlmmvtwc5df)

---

### setModelGroup

`public static void setModelGroup(
EOModelGroup group,
com.apple.yellow.eocontrol.EOObjectStoreCoordinator anObjectStoreCoordinator)`

Assigns _group_ to _anObjectStoreCoordinator_.
By default, an EOObjectStoreCoordinator uses the [defaultGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3emvtgc5lmordxe33voa). You
might want to assign a different group to an EOObjectStoreCoordinator
if you need to scope models to particular coordinators-if different
models have the same name, or if different entities in different
models have the same name.

__See Also:__  [modelGroupForObjectStoreCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3nn5sgk3chojxxk4cgn5ze6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64q)

---

## Instance Methods

---

### addModel

`public void addModel(EOModel model)`

Adds a _model_ to
the receiver, sets the _model_'s
model group to the receiver, and posts [ModelAddedNotification](#apple-ijfemqsbjjcug). Throws an exception
if the receiver already contains an EOModel with the same name as
the specified _model_.

---

### addModelWithPath

`public EOModel addModelWithPath(String path)`

Creates an EOModel object with the contents
of the file identified by _path_, and
adds the newly created model to the receiver. Adds the new model
to the receiver. Throws an exception if for any reason it cannot
create the model from the file specified by _path_.

---

### delegate

`public Object delegate()`

Returns the receiver's delegate, which is
different from the EOModelGroup's class delegate. Each EOModelGroup
object can have it's own delegate in addition to the delegate
that's assigned to the EOModelGroup class. See the [EOModelGroup.Delegate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#CBACDGDA) interface specification
for more information.

__See Also:__  [setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eg3dbonzuizlmmvtwc5df), [classDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3dnrqxg42emvwgkz3borsq)

---

### entitiesWithSharedObjects

`public NSArray entitiesWithSharedObjects()`

Returns an array of entities that have objects
to load into a shared editing context.

---

### __entityForObject__

`public EOEntity entityForObject(Object object)`

Returns the EOEntity associated with _object_ from
any of the models in the receiver that handle _object_, or null if
none of the entities in the receiver handles _object_.

__See
Also:__  [entityForObject](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4um33sj5rguzldoq) (EOModel)

---

### entityNamed

`public EOEntity entityNamed(String entityName)`

Searches each of the EOModels in the receiver
for the entity specified by _entityName_,
and returns the entity if found. Returns null if it is unable to
find the specified entity.

__See Also:__  [entityNamed](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5sw45djor4u4ylnmvsa) (EOModel)

---

### fetchSpecificationNamed

`public com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecificationNamed(
String fetchSpecName,
String entityName)`

Returns the named fetch specification from the
entity specified by _entityName_ in
the receiving model group.

---

### loadAllModelObjects

`public void loadAllModelObjects()`

Sends __loadAllModelObjects__ to
each of the receiver's EOModels, thereby loading any EOEntities, EOAttributes,
EORelationships, and EOStoredProcedures that haven't yet been
loaded from each of the EOModels in the receiver.

__See
Also:__  [loadAllModelObjects](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5wg6yleifwgytlpmrswyt3cnjswg5dt) (EOModel)

---

### modelNamed

`public EOModel modelNamed(String modelName)`

Returns the EOModel named _modelName_ if
it's part of the receiver, or null if the receiver doesn't contain an
EOModel with the specified name.

---

### modelNames

`public NSArray modelNames()`

Returns an array containing the names of all
of the EOModels in the receiver, or an empty array if the receiver
contains no EOModels. The order of the model names in the array
isn't defined.

---

### models

`public NSArray models()`

Returns an array containing the receiver's
EOModels, or an empty array if the receiver contains no EOModels.
The order of the models in the array isn't defined.

---

### modelWithPath

`public EOModel modelWithPath(String path)`

If the receiver contains an EOModel whose path
(as determined by sending [path](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ygc5di) to
the EOModel object) is equal to _path_,
that EOModel is returned. Otherwise, returns null. String's equals method
is used to compare the paths, and each path is standardized before
comparison.

__See Also:__  [path](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5ygc5di) (EOModel)

---

### removeModel

`public void removeModel(EOModel aModel)`

Removes _aModel_ from
the receiver, and unbinds any connections to _aModel_ from
other EOModels in the receiver. Posts [ModelInvalidatedNotification](#apple-ijfemqsjiveek) to the
default notification center after removing _aModel_ from
the receiver.

__See Also:__  EOModelGroup, [models](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrzq)

---

### setDelegate

`public void setDelegate(Object anObject)`

Sets the receiver's delegate to _anObject_.
See the [EOModelGroup.Delegate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#CBACDGDA) interface specification
for more information.

__See Also:__  [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5sgk3dfm5qxizi)

---

### storedProcedureNamed

`public EOStoredProcedure storedProcedureNamed(String aName)`

Returns the stored procedure in the receiving
model group having the given name.

---

## Notifications

---

EOModelGroup declares and posts the following notifications.

### ModelAddedNotification

Posted by an EOModelGroup when an EOModel
is added to the group. This notification is sent, for instance,
inside Interface Builder when the user has saved changes to a model
in EOModeler and the objects in Interface Builder must be brought
back in sync. The old model is flushed and receivers of the notification
(like data sources) can invoke [modelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrhgc3lfmq) to re-fetch their models.

|  |  |
| --- | --- |
| Notification Object | The newly added model. |
| Userinfo | None |

### ModelInvalidatedNotification

Posted by an EOModelGroup when an EOModel
is removed from the group. This notification is sent, for instance,
inside Interface Builder when the user has saved changes to a model
in EOModeler and the objects in Interface Builder must be brought
back in sync. The old model is flushed and receivers of the notification
(like data sources) can invoke [modelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmi5zg65lqf5ww6zdfnrhgc3lfmq) to re-fetch their models.

|  |  |
| --- | --- |
| Notification Object | The invalidated model. |
| Userinfo | None |

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
