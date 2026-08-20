---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOModelGroup.html
archived_at: '2026-07-18T01:28:16.893289Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](Loading%20a%20Model%20File-2.md)
[!](Setting%20Up%20A%20Model%20Group%20Programmatically-2.md)

---

# EOModelGroup

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOModelGroup.h

---

## Class Description

An EOModelGroup represents an aggregation of related models (see the [EOModel](EOModel-2.md) class specification for more information on models). When a model in the group needs to resolve a relationship to an entity in another model, it looks for that model in its group. Model groups allow applications to load entities and their properties only as they're needed, by distributing them among separate EOModels.

The _default model group_ contains all models for an application, as well as any frameworks the application references. It is automatically created on demand. The entity name space among all of these models is global; consequently, the same entity name shouldn't appear in any two of the models. All cross-model information is represented in the models by entity name only. Binding the entity name to an actual entity is done at run-time within the EOModelGroup.

In the majority of applications, the automatic creation of the default model group is sufficient. However, your code can override this automatic creation; see "[Setting Up A Model Group Programmatically](Setting%20Up%20A%20Model%20Group%20Programmatically-2.md#apple-gm2tgmq)."

---

## EOModelGroup Delegates

Your EOModelGroup object should have a delegate which can influence how it finds and loads models. In addition to the delegates you assign to EOModelGroup instances, the EOModelGroup class itself can have a delegate. The class delegate implements a single method-[`defaultModelGroup`](../Protocols/EOModelGroupClassDelegate.md#apple-gizda)-while the instance delegate can implement the methods defined in the [EOModelGroupDelegation](EOModelGroupDelegation.md) protocol. For more information on EOModelGroup class delegate and instance delegate methods, see the [EOModelGroupClassDelegation](EOModelGroupClassDelegation.md) and [EOModelGroupDelegation](EOModelGroupDelegation.md) protocol specifications, respectively.Note that the following delegate methods are set on EOModelGroup, rather than EOEntity, to provide a single point in the code where you can alter the database-to-objects mapping:

- [`entity:classForObjectWithGlobalID:`](../Protocols/EOModelGroupDelegate.md#apple-gy4dooa)
- [`entity:failedToLookupClassNamed:`](../Protocols/EOModelGroupDelegate.md#apple-gizti)
- [`entity:relationshipForRow:relationship:`](../Protocols/EOModelGroupDelegate.md#apple-gy4dmoi)
- [`subEntityForEntity:primaryKey:isFinal:`](../Protocols/EOModelGroupDelegate.md#apple-gy4dmmi)

---

## Method Types

**Accessing the group**

**[- addModel:](#apple-gi2tsma)

**[- addModelWithFile:](#apple-gi2tq)

**[- modelNamed:](#apple-ge4tk)

**[- modelNames](#apple-giytqna)

**[- models](#apple-giytina)

**[- modelWithPath:](#apple-gm3dsoa)

**[- removeModel:](#apple-giytc)**************

**Accessing model groups**

**[+ defaultGroup](#apple-he3teoi)

**[+ setDefaultGroup:](#apple-gmztsmq)

**[+ globalModelGroup](#apple-gmztomy)******

**Searching a group**

**[- entityNamed:](#apple-gezde)

**[- entityForObject:](#apple-geydemjq)

**[- fetchSpecificationNamed:entityNamed:](#apple-geydemrw)

**[- storedProcedureNamed:](#apple-geydenrt)********

**Loading all of a group's objects**

**[- loadAllModelObjects](#apple-ge4tc)**

**Assigning a delegate**

**[+ classDelegate](#apple-geydcnjw)

**[- delegate](#apple-gizdkma)

**[+ setClassDelegate:](#apple-geydaobx)

**[- setDelegate:](#apple-gi3dcma)********

---

## Class Methods

---

### classDelegate

+ (id)`classDelegate`

Returns the EOModelGroup's class delegate. This delegate optionally implements the [`defaultModelGroup`](../Protocols/EOModelGroupClassDelegate.md#apple-gizda) method (see the [EOModelGroupClassDelegation](EOModelGroupClassDelegation.md) protocol specification for more information).

__See also:__
[+ `setClassDelegate:`](#apple-geydaobx)

---

### defaultGroup

+ (EOModelGroup \*)`defaultGroup`

Returns the default EOModelGroup. Unless you've either specified a default model group with [`setDefaultGroup:`](#apple-gmztsmq) or implemented the [`defaultModelGroup`](../Protocols/EOModelGroupClassDelegate.md#apple-gizda) class delegate method to return a non-`nil` value, this method is equivalent to [`globalModelGroup`](#apple-gmztomy).

__See also:__
[+ `classDelegate`](#apple-geydcnjw)

---

### globalModelGroup

+ (EOModelGroup \*)`globalModelGroup`

Returns an EOModelGroup composed of all models in the resource directory of the main bundle, as well as those in all the bundles and frameworks loaded into the application.

__See also:__
[+ `defaultGroup`](#apple-he3teoi)

---

### setClassDelegate:

+ (void)`setClassDelegate:`(id)_anObject_

Assigns _anObject_ as the EOModelGroup's class delegate. The class delegate is optional; it allows you to determine the default model group (see the [EOModelGroupClassDelegation](EOModelGroupClassDelegation.md) protocol specification for more information).

__See also:__
[+ `classDelegate`](#apple-geydcnjw), [- `defaultModelGroup`](../Protocols/EOModelGroupClassDelegate.md#apple-gizda)

---

### setDefaultGroup:

+ (void)`setDefaultGroup:`(EOModelGroup \*)_group_

Sets the default model group to _group_. If you've implemented the [`defaultModelGroup`](../Protocols/EOModelGroupClassDelegate.md#apple-gizda) class delegate method to return a non-`nil` value, the delegate's return value overrides _group_ as the default model group.

__See also:__
[+ `defaultGroup`](#apple-he3teoi),[+ `setClassDelegate:`](#apple-geydaobx)

---

## Instance Methods

---

### addModel:

- (void)`addModel:`(EOModel \*)_model_

Adds a _model_ to the receiver, sets the _model_'s model group to the receiver, posts [EOModelAddedNotification](#apple-gi4di), then returns the newly-created EOModel. Raises if the receiver already contains an EOModel with the same name as the specified _model_.

__See also:__
[- `models`](#apple-giytina), [- `removeModel:`](#apple-giytc)

---

### addModelWithFile:

- (EOModel \*)`addModelWithFile:`(NSString \*)_path_

Creates an EOModel object with the contents of the file identified by _path_, adds the newly-created model to the receiver, and returns it. Uses the EOModel method [- `initWithContentsOfFile:`](EOModel.md#apple-geydcobv) to initialize the new model, and adds it to the receiver with [`addModel:`](#apple-gi2tsma).

---

### delegate

- (id)`delegate`

Returns the receiver's delegate, which is different from the EOModelGroup's class delegate. Each EOModelGroup object can have it's own delegate in addition to the delegate that's assigned to the EOModelGroup class. See the [EOModelGroupDelegation](EOModelGroupDelegation.md) protocol specification for more information.

__See also:__
[- `setDelegate:`](#apple-gi3dcma), [+ `classDelegate`](#apple-geydcnjw)

---

### entityForObject:

- (EOEntity \*)`entityForObject:`(id)_object_

Returns the EOEntity associated with _object_ from any of the models in the receiver that handle _object_, or `nil` if none of the entities in the receiver handles _object_.

__See also:__
[- `entityForObject:`](EOModel.md#apple-gqzto) (EOModel)

---

### entityNamed:

- (EOEntity \*)`entityNamed:`(NSString \*)_entityName_

Searches each of the EOModels in the receiver for the entity specified by _entityName_, and returns the entity if found. Returns `nil` if it is unable to find the specified entity.

__See also:__
[- `entityNamed:`](EOModel.md#apple-gm4tomy) (EOModel)

---

### fetchSpecificationNamed:entityNamed:

- (EOFetchSpecification \*)`fetchSpecificationNamed:`(NSString \*)_fetchSpecName_
`entityNamed:`(NSString \*)_entityName_

Returns the named fetch specification from the entity specified by _entityName_ in the receiving model group.

---

### loadAllModelObjects

- (void)`loadAllModelObjects`

Sends `loadAllModelObjects` to each of the receiver's EOModels, thereby loading any EOEntities, EOAttributes, EORelationships, and EOStoredProcedures that haven't yet been loaded from each of the EOModels in the receiver.

__See also:__
[- `loadAllModelObjects`](EOModel.md#apple-gq3da) (EOModel)

---

### modelNamed:

- (EOModel \*)`modelNamed:`(NSString \*)_modelName_

Returns the EOModel named _modelName_ if it's part of the receiver, or `nil` if the receiver doesn't contain an EOModel with the specified name.

__See also:__
[- `modelNames`](#apple-giytqna), [- `models`](#apple-giytina)

---

### modelNames

- (NSArray \*)`modelNames`

Returns an array containing the names of all of the EOModels in the receiver, or an empty array if the receiver contains no EOModels. The order of the model names in the array isn't defined.

__See also:__
[- `modelNamed:`](#apple-ge4tk), [- `models`](#apple-giytina)

---

### models

- (NSArray \*)`models`

Returns an array containing the receiver's EOModels, or an empty array if the receiver contains no EOModels. The order of the models in the array isn't defined.

__See also:__
[- `modelNamed:`](#apple-ge4tk), [- `modelNames`](#apple-giytqna), [- `models`](#apple-giytina)

---

### modelWithPath:

- (EOModel \*)`modelWithPath:`(NSString \*)_path_

If the receiver contains an EOModel whose path (as determined by sending [`path`](EOModel.md#apple-gq3te) to the EOModel object) is equal to _path_, that EOModel is returned. Otherwise, returns `nil`. NSString's `isEqual:` method is used to compare the paths, and each path is standardized (with `stringByStandardizingPath`) before comparison.

__See also:__
[- `modelNamed:`](#apple-ge4tk):, [- `path`](EOModel.md#apple-gq3te) (EOModel)

---

### removeModel:

- (void)`removeModel:`(EOModel \*)_aModel_

Removes _aModel_ from the receiver, and unbinds any connections to _aModel_ from other EOModels in the receiver. Posts [EOModelInvalidatedNotification](#apple-he3dc) to the default notification center after removing _aModel_ from the receiver.

---

### setDelegate:

- (void)`setDelegate:`(id)_anObject_

Sets the receiver's delegate to _anObject_. See the [EOModelGroupDelegation](EOModelGroupDelegation.md) protocol specification for more information.

__See also:__
`[- delegate](#apple-gizdkma)`

---

### storedProcedureNamed:

- (EOStoredProcedure \*)`storedProcedureNamed:`(NSString \*)_aName_

Returns the stored procedure in the receiving model group having the given name.

---

# Notifications

EOModelGroup declares and posts the following notifications.

---

### EOModelAddedNotification

Posted by an EOModelGroup when an EOModel is added to the group. This notification is sent, for instance, inside Interface Builder when the user has saved changes to a model in EOModeler and the objects in Interface Builder must be brought back in sync. The old model is flushed and receivers of the notification (like data sources) can invoke [`modelNamed:`](#apple-ge4tk) to re-fetch their models.

| Notification Object | The newly added model. |
| Userinfo | None |

```
```


---

### EOModelInvalidatedNotification

Posted by an EOModelGroup when an EOModel is removed from the group. This notification is sent, for instance, inside Interface Builder when the user has saved changes to a model in EOModeler and the objects in Interface Builder must be brought back in sync. The old model is flushed and receivers of the notification (like data sources) can invoke [`modelNamed:`](#apple-ge4tk) to re-fetch their models.

| Notification Object | The invalidated model. |
| Userinfo | None |

```
```

---

[!](Loading%20a%20Model%20File-2.md)
[!](Setting%20Up%20A%20Model%20Group%20Programmatically-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
