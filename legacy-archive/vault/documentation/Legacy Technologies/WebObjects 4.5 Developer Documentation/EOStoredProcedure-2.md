---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOStoredProcedure.html
archived_at: '2026-07-15T08:11:33.854206Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOStoredProcedure

> __Inherits
> from:__  NSObject

> __Conforms to:__  [EOPropertyListEncoding](EOPropertyListEncoding-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgf5cu6udsn5ygk4tupfggs43uivxgg33enfxgo)
> NSObject (NSObject)

> __Declared in:__  EOAccess/EOStoredProcedure.h

---

## Class Description

---

An EOStoredProcedure represents a stored procedure defined
in a database, and associates a name internal to the Framework with
an external name by which the stored procedure is known to the database.
If a stored procedure has arguments, its EOStoredProcedure object
also maintains a group of EOAttributes which represent the stored
procedure's arguments. See the [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue) class specification for
more information

You usually define stored procedures in your EOModel with
the EOModeler application, which is documented in the _Enterprise
Objects Framework Developer's Guide_. EOStoredProcedures
are primarily used by the Enterprise Objects Framework to map operations
for an EOEntity to stored procedures (see the description for EOEntity's [setStoredProcedure:forOperation:](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwk5ctorxxezlekbzg6y3fmr2xezj2mzxxet3qmvzgc5djn5xdu) method).
You can assign stored procedures to an entity for any of the following
scenarios:

- Fetching all the objects for the entity
- Fetching a single object by its primary key
- Inserting a new object
- Deleting an object
- Generating a new primary key

Your code probably won't use EOStoredProcedures unless you're
working at the adaptor level.

Like the other major modeling classes, EOStoredProcedure provides
a user dictionary for your application to store any application-specific
information related to the stored procedure.

## Adopted Protocols

---

> [EOPropertyListEncoding](EOPropertyListEncoding-2.md#apple-ijauiq2hindeq): [- awakeWithPropertyList](EOPropertyListEncoding-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpmf3wc23fk5uxi2cqojxxazlsor4uy2ltoq)
> : [- encodeIntoPropertyList:](EOPropertyListEncoding-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpmvxgg33emvew45dpkbzg64dfoj2hstdjon2du)

## Method Types

---

> **Creating a new EOStoredProcedure**
> : [- initWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnfxgs5cxnf2gqttbnvstu)
>
> **Accessing the model**
> : [- model](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnvxwizlm)
>
> **Accessing the name**
> : [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxittbnvstu)
> : [- beautifyName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpmjswc5lunfthsttbnvsq)
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnzqw2zi)
>
> **Accessing the external
> name**
> : [- setExternalName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxirlyorsxe3tbnrhgc3lfhi)
> : [- externalName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpmv4hizlsnzqwyttbnvsq)
>
> **Accessing the arguments**
> : [- setArguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxiqlsm52w2zloorztu)
> : [- arguments](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpmfzgo5lnmvxhi4y)
>
> **Accessing the user dictionary**
> : [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxivltmvzes3tgn45a)
> : [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpovzwk4sjnztg6)

## Instance Methods

---

### arguments

`- (NSArray *)arguments`

Returns the EOAttribute objects that describe
the stored procedure's arguments or nil if the stored procedure
has no arguments.

---

### beautifyName

`- (void)beautifyName`

Renames the receiver's name and its arguments
to conform to the Framework's naming conventions. For example,
"NAME" is renamed "name" and "FIRST_NAME" is renamed
"firstName". This method is used in reverse-engineering a model.

__See
Also:__  [- setArguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxiqlsm52w2zloorztu), [- beautifyNames](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmjswc5lunfthsttbnvsxg) (EOModel)

---

### externalName

`- (NSString *)externalName`

Returns the name of the stored procedure as
it is defined in the database, or nil if the receiver doesn't have
an external name.

__See Also:__  [- setExternalName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxirlyorsxe3tbnrhgc3lfhi)

---

### initWithName:

`- (EOStoredProcedure *)initWithName:(NSString
*)name`

The designated initializer for EOStoredProcedure,
this method initializes a new EOStoredProcedure object and sets
its name to _name_. Returns __self__.

__See
Also:__  [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxittbnvstu), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnzqw2zi)

---

### model

`- (EOModel *)model`

Returns the model to which the receiver belongs.

__See
Also:__  [- addStoredProcedure:](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgiu3un5zgkzcqojxwgzleovzgkoq) (EOModel)

---

### name

`- (NSString *)name`

Returns the name of the receiver.

__See
Also:__  [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxittbnvstu), [- initWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnfxgs5cxnf2gqttbnvstu)

---

### setArguments:

`- (void)setArguments:(NSArray
*)arguments`

Sets _arguments_ as
the array of EOAttributes that describe the receiver's arguments.
The EOAttribute objects in _arguments_ must
be ordered to match the database stored procedure definition.

__See
Also:__  [- arguments](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpmfzgo5lnmvxhi4y)

---

### setExternalName:

`- (void)setExternalName:(NSString
*)name`

Sets the external name of the stored procedure
to _name_. _name_ should
be the name of the stored procedure as it is defined in the database.

__See
Also:__  [- externalName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpmv4hizlsnzqwyttbnvsq)

---

### setName:

`- (void)setName:(NSString
*)name`

Sets the name of the receiver.

__See
Also:__  [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnzqw2zi), [- initWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpnfxgs5cxnf2gqttbnvstu)

---

### setUserInfo:

`- (void)setUserInfo:(NSDictionary
*)dictionary`

Sets the _dictionary_ of
auxiliary data, which your application can use for whatever it needs. _dictionary_ can
only contain property list data types (that is, NSString, NSDictionary,
NSArray, and NSData).

__See Also:__  [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjpovzwk4sjnztg6)

---

### userInfo

`- (NSDictionary *)userInfo`

Returns a dictionary of user data. Your application
can use this to store any auxiliary information it needs.

__See
Also:__  [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2torxxezlekbzg6y3fmr2xezjponsxivltmvzes3tgn45a)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
