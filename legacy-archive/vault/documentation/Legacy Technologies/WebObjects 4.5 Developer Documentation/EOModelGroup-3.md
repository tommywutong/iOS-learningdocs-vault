---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOModelGroup.html
archived_at: '2026-07-15T08:11:33.733958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOModelGroup

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOModelGroup.h

---

## Class Description

---

An EOModelGroup represents an aggregation of related models
(see the [EOModel](EOModel-3.md#apple-ineeoq2iizduk) class
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
this automatic creation; see ["Setting Up A Model Group Programmatically"](EOModelGroup-4.md#apple-ijbeorkbjbeuq).

## Accessing Models Within a Model Group

Each model lives within a group and can form connections to
other models in its group. A model can find a related model using
the statement:

> ```
> [[self modelGroup] modelNamed:name];
> ```

A data source can locate a model using the statement:

> ```
> [[EOModelGroup defaultGroup] modelNamed:name];
> ```

EOModeler puts models with identical names in separate groups
to allow you to load two models with the same name at the same time.

## EOModelGroup Delegates

Your EOModelGroup object should have a delegate which can
influence how it finds and loads models. In addition to the delegates
you assign to EOModelGroup instances, the EOModelGroup class itself
can have a delegate. The class delegate implements a single method- [defaultModelGroup](EOModelGroup%20Class%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya)-while
the instance delegate can implement the methods defined in the EOModelGroup
Delegate protocol. For more information on EOModelGroup
class delegate and instance delegate methods, see the [EOModelGroup Class Delegate](EOModelGroup%20Class%20Delegate.md#apple-indeerckizduo) and [EOModelGroup Delegate](EOModelGroup%20Delegate.md#apple-inbecq2ei5cec) protocol specifications,
respectively. Note that the following delegate methods are set on
EOModelGroup, rather than EOEntity, to provide a single point in
the code where you can alter the database-to-objects mapping:

- [entity:classForObjectWithGlobalID:](EOModelGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3fnz2gs5dzhjrwyyltondg64spmjvgky3uk5uxi2chnrxweylmjfcdu)
- [entity:failedToLookupClassNamed:](EOModelGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3fnz2gs5dzhjtgc2lmmvsfi32mn5xww5lqinwgc43tjzqw2zlehi)
- [entity:relationshipForRow:relationship:](EOModelGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3fnz2gs5dzhjzgk3dboruw63ttnbuxartpojjg65z2ojswyylunfxw443infydu)
- [subEntityForEntity:primaryKey:isFinal:](EOModelGroup%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bairswyzlhmf2gkl3tovrek3tunf2hsrtpojcw45djor4tu4dsnfwwc4tzjnsxsotjondgs3tbnq5a)

## Constants

---

In EOModelGroup.h, EOModelGroupEOAccess defines NSString
constants for the names of the notifications it posts. For more
information on these notifications, see ["Notifications"](#apple-ijbeoq2dizdui).

## Method Types

---

> **Accessing models**
> : [- addModelWithFile:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmfsgitlpmrswyv3joruem2lmmu5a)
> : [- modelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmjzqw2zlehi)
> : [- modelNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmjzqw2zlt)
> : [- models](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmom)
> : [- modelWithPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmk5uxi2cqmf2gqoq)
> : [- removeModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpojsw233wmvgw6zdfnq5a)
>
> **Accessing model groups**
> : [+ defaultGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6zdfmzqxk3dui5zg65lq)
> : [+ setDefaultGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forcgkztbovwhir3sn52xaoq)
> : [+ globalModelGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6z3mn5rgc3cnn5sgk3chojxxk4a)
>
> **Searching a group**
> : [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmvxhi2lupfhgc3lfmq5a)
> : [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmvxhi2lupfdg64spmjvgky3uhi)
> : [- entitiesWithSharedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmvxhi2lunfsxgv3jorufg2dbojswit3cnjswg5dt)
> : [- fetchSpecificationNamed:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmzsxiy3iknygky3jmzuwgylunfxw4ttbnvswiotfnz2gs5dzjzqw2zlehi)
> : [- storedProcedureNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpon2g64tfmrihe33dmvshk4tfjzqw2zlehi)
>
> **Loading all of a group's
> objects**
> : [- loadAllModelObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnrxwczcbnrwe233emvwe6ytkmvrxi4y)
>
> **Assigning a delegate**
> : [+ classDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6y3mmfzxgrdfnrswoylumu)
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmrswyzlhmf2gk)
> : [+ setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2)
> : [- setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2)

## Class Methods

---

### classDelegate

`+ (id)classDelegate`

Returns the EOModelGroup's class delegate.
This delegate optionally implements the [defaultModelGroup](EOModelGroup%20Class%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya) method
(see the [EOModelGroup Class Delegate](EOModelGroup%20Class%20Delegate.md#apple-indeerckizduo) protocol specification
for more information).

__See Also:__  [+ setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2)

---

### defaultGroup

`+ (EOModelGroup *)defaultGroup`

Returns the default EOModelGroup. Unless you've
either specified a default model group with [setDefaultGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forcgkztbovwhir3sn52xaoq) or
implemented the [defaultModelGroup](EOModelGroup%20Class%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya) class
delegate method to return a non-`nil` value,
this method is equivalent to [globalModelGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6z3mn5rgc3cnn5sgk3chojxxk4a).

__See
Also:__  [+ classDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6y3mmfzxgrdfnrswoylumu)

---

### globalModelGroup

`+ (EOModelGroup *)globalModelGroup`

Returns an EOModelGroup composed of all models
in the resource directory of the main bundle, as well as those in
all the bundles and frameworks loaded into the application.

__See
Also:__  [+ defaultGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6zdfmzqxk3dui5zg65lq)

---

### setClassDelegate:

`+ (void)setClassDelegate:(id)anObject`

Assigns _anObject_ as
the EOModelGroup's class delegate. The class delegate is optional;
it allows you to determine the default model group (see the [EOModelGroup Class Delegate](EOModelGroup%20Class%20Delegate.md#apple-indeerckizduo) protocol specification
for more information).

__See Also:__  [+ classDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6y3mmfzxgrdfnrswoylumu), [- defaultModelGroup](EOModelGroup%20Class%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya)

---

### setDefaultGroup:

`+ (void)setDefaultGroup:(EOModelGroup
*)group`

Sets the default model group to _group_.
If you've implemented the [defaultModelGroup](EOModelGroup%20Class%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya) class
delegate method to return a non-`nil` value,
the delegate's return value overrides _group_ as
the default model group.

__See Also:__  [+ defaultGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6zdfmzqxk3dui5zg65lq), [+ setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2)

---

## Instance Methods

---

### addModel:

`- (void)addModel:(EOModel
*)model`

Adds a _model_ to
the receiver, sets the _model_'s
model group to the receiver, and posts [EOModelAddedNotification](#apple-ijfemqsbjjcug). Raises an
exception if the receiver already contains an EOModel with the same
name as the specified _model_.

---

### __addModelWithFile:__

`- (EOModel *)addModelWithFile:(NSString
*)path`

Creates an EOModel object with the contents
of the file identified by _path_, adds
the newly-created model to the receiver, and returns it. Throws
an exception if for any reason it cannot create the model from the
file specified by _path_. Uses the
EOModel method [initWithContentsOfFile:](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnfxgs5cxnf2gqq3pnz2gk3tuonhwmrtjnrstu) to initialize
the new model, and adds it to the receiver.

---

### delegate

`- (id)delegate`

Returns the receiver's delegate, which is
different from the EOModelGroup's class delegate. Each EOModelGroup
object can have it's own delegate in addition to the delegate
that's assigned to the EOModelGroup class. See the [EOModelGroup Delegate](EOModelGroup%20Delegate.md#apple-inbecq2ei5cec) protocol specification
for more information.

__See Also:__  [- setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2), [+ classDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6y3mmfzxgrdfnrswoylumu)

---

### entitiesWithSharedObjects

`- (NSArray *)entitiesWithSharedObjects`

Returns an array of entities that have objects
to load into a shared editing context.

---

### __entityForObject:__

`- (EOEntity *)entityForObject:(id)object`

Returns the EOEntity associated with _object_ from
any of the models in the receiver that handle _object_, or nil if
none of the entities in the receiver handles _object_.

__See
Also:__  [- entityForObject:](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfdg64spmjvgky3uhi) (EOModel)

---

### entityNamed:

`- (EOEntity *)entityNamed:(NSString
*)entityName`

Searches each of the EOModels in the receiver
for the entity specified by _entityName_,
and returns the entity if found. Returns nil if it is unable to
find the specified entity.

__See Also:__  [- entityNamed:](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmvxhi2lupfhgc3lfmq5a) (EOModel)

---

### fetchSpecificationNamed:entityNamed:

`- (EOFetchSpecification *)fetchSpecificationNamed:(NSString
*)fetchSpecName
entityNamed:(NSString *)entityName`

Returns the named fetch specification from the
entity specified by _entityName_ in
the receiving model group.

---

### loadAllModelObjects

`- (void)loadAllModelObjects`

Sends __loadAllModelObjects__ to
each of the receiver's EOModels, thereby loading any EOEntities, EOAttributes,
EORelationships, and EOStoredProcedures that haven't yet been
loaded from each of the EOModels in the receiver.

__See
Also:__  [- loadAllModelObjects](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpnrxwczcbnrwe233emvwe6ytkmvrxi4y) (EOModel)

---

### modelNamed:

`- (EOModel *)modelNamed:(NSString
*)modelName`

Returns the EOModel named _modelName_ if
it's part of the receiver, or nil if the receiver doesn't contain an
EOModel with the specified name.

---

### modelNames

`- (NSArray *)modelNames`

Returns an array containing the names of all
of the EOModels in the receiver, or an empty array if the receiver
contains no EOModels. The order of the model names in the array
isn't defined.

---

### models

`- (NSArray *)models`

Returns an array containing the receiver's
EOModels, or an empty array if the receiver contains no EOModels.
The order of the models in the array isn't defined.

---

### modelWithPath:

`- (EOModel *)modelWithPath:(NSString
*)path`

If the receiver contains an EOModel whose path
(as determined by sending [path](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobqxi2a) to
the EOModel object) is equal to _path_,
that EOModel is returned. Otherwise, returns nil. NSString's isEqual: method
is used to compare the paths, and each path is standardized (with __stringByStandardizingPath__) before comparison.

__See
Also:__  [- path](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpobqxi2a) (EOModel)

---

### removeModel:

`- (void)removeModel:(EOModel
*)aModel`

Removes _aModel_ from
the receiver, and unbinds any connections to _aModel_ from
other EOModels in the receiver. Posts [EOModelInvalidatedNotification](#apple-ijfemqsjiveek) to the
default notification center after removing _aModel_ from
the receiver.

__See Also:__  - EOModelGroup, [- models](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmom)

---

### setDelegate:

`- (void)setDelegate:(id)anObject`

Sets the receiver's delegate to _anObject_.
See the [EOModelGroup Delegate](EOModelGroup%20Delegate.md#apple-inbecq2ei5cec) protocol specification
for more information.

__See Also:__  [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpmrswyzlhmf2gk)

---

### storedProcedureNamed:

`- (EOStoredProcedure *)storedProcedureNamed:(NSString
*)aName`

Returns the stored procedure in the receiving
model group having the given name.

---

## Notifications

---

EOModelGroup declares and posts the following notifications.

### EOModelAddedNotification

Posted by an EOModelGroup when an EOModel
is added to the group. This notification is sent, for instance,
inside Interface Builder when the user has saved changes to a model
in EOModeler and the objects in Interface Builder must be brought
back in sync. The old model is flushed and receivers of the notification
(like data sources) can invoke [modelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmjzqw2zlehi) to re-fetch their models.

|  |  |
| --- | --- |
| Notification Object | The newly added model. |
| Userinfo | None |

### EOModelInvalidatedNotification

Posted by an EOModelGroup when an EOModel
is removed from the group. This notification is sent, for instance,
inside Interface Builder when the user has saved changes to a model
in EOModeler and the objects in Interface Builder must be brought
back in sync. The old model is flushed and receivers of the notification
(like data sources) can invoke [modelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3chojxxk4bpnvxwizlmjzqw2zlehi) to re-fetch their models.

|  |  |
| --- | --- |
| Notification Object | The invalidated model. |
| Userinfo | None |

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
