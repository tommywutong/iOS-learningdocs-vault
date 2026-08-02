---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOStoredProcedure.html
archived_at: '2026-07-15T08:11:32.030367Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOStoredProcedure

> __Inherits
> from:__  NSObject

> __Implements:__  [EOPropertyListEncoding](EOPropertyListEncoding.md#apple-ijauiq2hindeq)

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

An EOStoredProcedure represents a stored procedure defined
in a database, and associates a name internal to the Framework with
an external name by which the stored procedure is known to the database.
If a stored procedure has arguments, its EOStoredProcedure object
also maintains a group of EOAttributes which represent the stored
procedure's arguments. See the [EOAttribute](EOAttribute.md#apple-incuqq2ijfeue) class specification for
more information

You usually define stored procedures in your EOModel with
the EOModeler application, which is documented in the _Enterprise
Objects Framework Developer's Guide_. EOStoredProcedures
are primarily used by the Enterprise Objects Framework to map operations
for an EOEntity to stored procedures (see the description for EOEntity's [setStoredProcedure](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukn2g64tfmrihe33dmvshk4tf) method). You can
assign stored procedures to an entity for any of the following scenarios:

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

## Interfaces Implemented

---

> [EOPropertyListEncoding](EOPropertyListEncoding.md#apple-ijauiq2hindeq): [awakeWithPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5qxoyllmvlws5dikbzg64dfoj2hstdjon2a)
> : [encodeIntoPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5sw4y3pmrsus3tun5ihe33qmvzhi6kmnfzxi)

## Method Types

---

> **Constructors**
> : [EOStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5cu6u3un5zgkzcqojxwgzleovzgk)
>
> **Accessing the model**
> : [model](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5ww6zdfnq)
>
> **Accessing the name**
> : [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5comfwwk)
> : [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5rgkylvoruwm6komfwwk)
> : [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5xgc3lf)
>
> **Accessing the external
> name**
> : [setExternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cfpb2gk4tomfwe4ylnmu)
> : [externalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5sxq5dfojxgc3comfwwk)
>
> **Accessing the arguments**
> : [setArguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cbojtxk3lfnz2hg)
> : [arguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5qxez3vnvsw45dt)
>
> **Accessing the user dictionary**
> : [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cvonsxeslomzxq)
> : [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff52xgzlsjfxgm3y)

## Constructors

---

### EOStoredProcedure

`public EOEOStoredProcedure(String name)`

Creates and returns a new EOStoredProcedure
named _name_.

`public EOStoredProcedure(
NSDictionary propertyList,
Object owner)`

Creates and returns a new EOStoredProcedure
initialized from _propertyList_-a
dictionary containing only property list data types (that is, String,
NSDictionary, NSArray, and NSData). This constructor is used by
EOModeler when it reads in an EOModel object from a file, for example.
The _owner_ argument should be the
EOStoredProcedure's EOModel. EOStoredProcedures created from a
property list must receive an [awakeWithPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5qxoyllmvlws5dikbzg64dfoj2hstdjon2a) message immediately
after creation before they are fully functional, but the __awake...__ message
should be deferred until the all of the other objects in the model
have also been created.

__See Also:__  [encodeIntoPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5sw4y3pmrsus3tun5ihe33qmvzhi6kmnfzxi) ( [EOPropertyListEncoding](EOPropertyListEncoding.md#apple-ijauiq2hindeq)) [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5comfwwk), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5xgc3lf)

---

## Instance Methods

---

### arguments

`public NSArray arguments()`

Returns the EOAttribute objects that describe
the stored procedure's arguments or null if the stored procedure
has no arguments.

---

### beautifyName

`public void beautifyName()`

Renames the receiver's name and its arguments
to conform to the Framework's naming conventions. For example,
"NAME" is renamed "name" and "FIRST_NAME" is renamed
"firstName". This method is used in reverse-engineering a model.

__See
Also:__  [setArguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cbojtxk3lfnz2hg), [beautifyNames](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5rgkylvoruwm6komfwwk4y) (EOModel)

---

### externalName

`public String externalName()`

Returns the name of the stored procedure as
it is defined in the database, or null if the receiver doesn't have
an external name.

__See Also:__  [setExternalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cfpb2gk4tomfwe4ylnmu)

---

### model

`public EOModel model()`

Returns the model to which the receiver belongs.

__See
Also:__  [addStoredProcedure](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5qwizctorxxezlekbzg6y3fmr2xezi) (EOModel)

---

### name

`public String name()`

Returns the name of the receiver.

__See
Also:__  [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5comfwwk), [EOStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5cu6u3un5zgkzcqojxwgzleovzgk) constructor

---

### setArguments

`public void setArguments(NSArray arguments)`

Sets _arguments_ as
the array of EOAttributes that describe the receiver's arguments.
The EOAttribute objects in _arguments_ must
be ordered to match the database stored procedure definition.

__See
Also:__  [arguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5qxez3vnvsw45dt)

---

### setExternalName

`public void setExternalName(String name)`

Sets the external name of the stored procedure
to _name_. _name_ should
be the name of the stored procedure as it is defined in the database.

__See
Also:__  [externalName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5sxq5dfojxgc3comfwwk)

---

### setName

`public void setName(String name)`

Sets the name of the receiver.

__See
Also:__  [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5xgc3lf), [EOStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5cu6u3un5zgkzcqojxwgzleovzgk) constructor

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of
auxiliary data, which your application can use for whatever it needs. _dictionary_ can
only contain property list data types (that is, String, NSDictionary,
NSArray, and NSData).

__See Also:__  [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff52xgzlsjfxgm3y)

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application
can use this to store any auxiliary information it needs.

__See
Also:__  [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn2g64tfmrihe33dmvshk4tff5zwk5cvonsxeslomzxq)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
