---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAttribute.html
archived_at: '2026-07-18T01:28:09.018814Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptorOperation.md)
[!](Creating%20Attributes.md)

---

# EOAttribute

__Inherits From:__
NSObject

[EOPropertyListEncoding](EOPropertyListEncoding.md)

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

An EOAttribute represents a column, field or property in a database, and associates an internal name with an external name or expression by which the property is known to the database. The property an EOAttribute represents may be a meaningful value, such as a salary or a name, or it may be an arbitrary value used for identification but with no real-world applicability (ID numbers and foreign keys for relationships fall into this category). An EOAttribute also maintains type information for binding values to the instance variables of objects.

EOAttributes are also used to represent arguments for EOStoredProcedures.

You usually define attributes in your EOModel with the EOModeler application, which is documented in _WebObjects Tools and Techniques_. Your code probably won't need to programmatically interact with EOAttribute unless you're working at the adaptor level. See "[Creating Attributes](Creating%20Attributes.md)" for information on creating your own attribute objects.

Fore detailed discussion of using attribute objects to map database data types to JavaObjective-C objects, see "[Mapping Attributes](Mapping%20Attributes.md)." EOAttributes can also alter the way values are selected, inserted, and updated in the database by defining special format strings; see "[SQL Statement Formats](SQL%20Statement%20Formats.md)" for more information.

**[EOPropertyListEncoding](EOPropertyListEncoding.md)**

**[awakeWithPropertyList](EOPropertyListEncoding.md#apple-hazto)

**[encodeIntoPropertyList](EOPropertyListEncoding.md#apple-ha3di)****

---

## Method Types

**Constructors**

**[EOAttribute](#apple-ge2dcnrv)**

**Accessing the entity**

**[entity](#apple-hazdi)

**[parent](#apple-g44tmmi)****

**Accessing the name**

**[setName](#apple-heytq)

**[name](#apple-ha2tg)

**[validateName](#apple-he4de)

**[beautifyName](#apple-ge4dcmzs)********

**Accessing date information**

**[serverTimeZone](#apple-ha4do)

**[setServerTimeZone](#apple-he2dk)****

**Accessing external definitions**

**[setColumnName](#apple-ha4to)

**[columnName](#apple-ge4dcnbz)

**[setDefinition](#apple-heydg)

**[definition](#apple-ge4dcnrw)

**[setExternalType](#apple-heyta)

**[externalType](#apple-hazdq)************

**Accessing value type information**

**[setValueClassName](#apple-gqzdaoa)

**[valueClassName](#apple-he4ta)

**[setValueType](#apple-he3dc)

**[valueType](#apple-geydamq)

**[setAllowsNull](#apple-ha4ti)

**[allowsNull](#apple-gq4dmoi)

**[setPrecision](#apple-hezdo)

**[precision](#apple-ha3tk)

**[setScale](#apple-he2dc)

**[scale](#apple-ha4dg)

**[setWidth](#apple-he3dk)

**[width](#apple-geydanq)************************

**Converting to adaptor value types**

**[adaptorValueByConvertingAttributeValue](#apple-guydkny)

**[adaptorValueType](#apple-gq4dkoa)****

**Working with custom value types**

**[setValueFactoryMethodName](#apple-he2tq)

**[valueFactoryMethod](#apple-he4tk)

**[valueFactoryMethodName](#apple-he4tq)

**[setFactoryMethodArgumentType](#apple-heyti)

**[factoryMethodArgumentType](#apple-hazte)

**[setAdaptorValueConversionMethodName](#apple-ha4tc)

**[adaptorValueConversionMethod](#apple-guydama)

**[adaptorValueConversionMethodName](#apple-gq4dioa)

**[archiveDataForObject](#apple-ge2dcobs)******************

**Accessing attribute characteristics**

**[setReadOnly](#apple-hezto)

**[isReadOnly](#apple-ha2ta)

**[isDerived](#apple-ha2da)

**[isFlattened](#apple-ha2dk)********

**Accessing SQL statement formats**

**[setReadFormat](#apple-heztc)

**[readFormat](#apple-ha3ts)

**[setWriteFormat](#apple-he3ds)

**[writeFormat](#apple-geydcma)********

**Accessing the user dictionary**

**[setUserInfo](#apple-he2dq)

**[userInfo](#apple-he3tq)****

**Working with stored procedures**

**[setParameterDirection](#apple-hezde)

**[parameterDirection](#apple-ha3dm)

**[storedProcedure](#apple-he3ti)******

**Working with prototypes**

**[overridesPrototypeDefinitionForKey](#apple-ge3tqnrr)

**[prototype](#apple-ge3tqnbt)

**[prototypeName](#apple-ge3tqmjr)

**[setPrototype](#apple-ge3tqobt)********

---

## Constructors

---

### EOAttribute

public `EOAttribute`()

Creates a new EOAttribute.

public `EOAttribute`(NSDictionary _propertyList_, java.lang.Object _owner_)

Creates a new EOAttribute initialized from _propertyList_-a dictionary containing only property list data types (that is, java.lang.Strings, NSDictionary, NSArrays, and NSDatas). This constructor is used by EOModeler when it reads in a Model from a file, for example. The _owner_ argument should be the EOAttribute's EOEntity or EOStoredProcedure. EOAttributes created from a property list must receive an [`awakeWithPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-hazto) message immediately after creation before they are fully functional, but the `awake...` message should be deferred until the all of the other objects in the model have also been created.

__See also:__
[`awakeWithPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-hazto) (EOPropertyListEncoding), [`encodeIntoPropertyList`](../Protocols/EOPropertyListEncoding.md#apple-ha3di)
(EOPropertyListEncoding)

#

---

### archiveDataForObject

public static NSData `archiveDataForObject`(NSObject _anObject_)

Return _anObject_'s value as a NSData object whose bytes can be stored in an external repository.

<<Need to add more info to this on the implications to custom value classes.>>

---

## Instance Methods

---

### adaptorValueByConvertingAttributeValue

public java.lang.Object `adaptorValueByConvertingAttributeValue`(java.lang.Object _value_)

Ensures that _value_ is either a String, Number, NSData, or NSDate, converting it if necessary. If _value_ needs to be converted, `adaptorValueByConvertingAttributeValue:` uses the adaptor conversion method to convert _value_ to one of these four primitive types. If the attribute hasn't a specific adaptor conversion method, and the type to be fetched from the database is EOAdaptorBytesType, [`archiveDataForObject`](#apple-ge2dcobs) will be invoked to convert the attribute value.

__See also:__
[`adaptorValueConversionMethod`](#apple-guydama), [`adaptorValueType`](#apple-gq4dkoa)

---

### adaptorValueConversionMethod

public NSSelector `adaptorValueConversionMethod`()

Returns the method used to convert a custom class into one of the primitive types that the adaptor knows how to manipulate: String, Number, NSData, or NSDate. The return value of this method is derived from the attribute's adaptor value conversion method name. If that name doesn't map to a valid selector in the Java run-time, `null` is returned.

__See also:__
`[adaptorValueByConvertingAttributeValue](#apple-guydkny)`, `[adaptorValueConversionMethodName](#apple-gq4dioa)`

---

### adaptorValueConversionMethodName

public java.lang.String `adaptorValueConversionMethodName`()

Returns the name of the method used to convert a custom class into one of the primitive types that the adaptor knows how to manipulate: String, Number, NSData, or NSDate.

__See also:__
`[adaptorValueByConvertingAttributeValue](#apple-guydkny)`

---

### adaptorValueType

public int `adaptorValueType`()

Returns a constant that indicates the data type that will be fetched from the database. Currently, this method returns one of the following values:

| __Constant__ | __Description__ |
| AdaptorNumberType | A number value |
| AdaptorCharactersType | A string of characters |
| AdaptorBytesType | Raw bytes |
| AdaptorDateType | A date |

```
```

__See also:__
[`factoryMethodArgumentType`](#apple-hazte)

---

### allowsNull

public boolean `allowsNull`()

Returns `true` to indicate that the attribute can have a `null` value, `false` otherwise. If the attribute maps directly to a column in the database, it also is used to determine whether the database column can have a NULL value.

__See also:__
[`setAllowsNull`](#apple-ha4ti)

---

### awakeWithPropertyList

public void `awakeWithPropertyList`(NSDictionary _propertyList_)

Finishes initializing the receiver from _propertyList_, which must have been created with a constructor of the form:

public _ClassName_(NSDictionary _propertyList_, java.lang.Object _owner_)

`awakeWithPropertyList` is responsible for restoring references to other objects. Consequently, it should not be invoked until all other objects that the receiver might reference have been created from _propertyList_.

__See also:__
[`encodeIntoPropertyList`](#apple-ge4dcobt)

---

### beautifyName

public void `beautifyName`()

Makes the attribute name conform to a standard convention. Names that conform to this style are all lower-case except for the initial letter of each embedded word other than the first, which is upper case. Thus, "NAME" becomes "name", and "FIRST_NAME" becomes "firstName". This method is used in reverse-engineering an EOModel.

__See also:__
[`nameForExternalName`](EOEntity.md#apple-ge2danzw) (EOEntity), [`validateName`](#apple-he4de), [`beautifyNames`](EOModel.md#apple-gqzde) (EOModel)

---

### columnName

public java.lang.String `columnName`()

Returns the name of the column in the database that corresponds to this attribute, or `null` if the attribute isn't simple (that is, if it's derived or flattened). An adaptor uses this name to identify the column corresponding to the attribute. Your application should never need to use this name. Note that `columnName` and [`definition`](#apple-ge4dcnrw) are mutually exclusive; if one returns a value, the other returns `null`.

__See also:__
, [`externalType`](#apple-hazdq)

---

### definition

public java.lang.String `definition`()

Returns a derived or flattened attribute's definition, or `null` if the attribute is simple. An attribute's definition is either a value expression defining a derived attribute, such as "salary \* 12", or a data path for a flattened attribute, such as "toAuthor.name". Note that [`columnName`](#apple-ge4dcnbz) and `definition` are mutually exclusive; if one returns a value, the other returns `null`.

__See also:__
[`externalType`](#apple-hazdq)`, [setDefinition](#apple-heydg)`

---

### encodeIntoPropertyList

public void `encodeIntoPropertyList`(NSMutableDictionary _propertyList_)

Returns the receiver as a property list.

__See also:__
[`awakeWithPropertyList`](#apple-ge3tsnrv)

---

### entity

public EOEntity `entity`()

Returns the entity that owns the attribute, or `null` if this attribute is acting as an argument for a stored procedure.

__See also:__
[`storedProcedure`](#apple-he3ti)

---

### externalType

public java.lang.String `externalType`()

Returns the attribute's type as understood by the database; for example, a Sybase "varchar" or an Oracle "NUMBER".

__See also:__
[`columnName`](#apple-ge4dcnbz)`, [setExternalType](#apple-heyta)`

---

### factoryMethodArgumentType

public int `factoryMethodArgumentType()`

Returns the type of argument that should be passed to the "factory method"-which is invoked by the attribute to create an attribute value for a custom class. This method returns one of the following values:

| ____Constant____ | __Argument Type__ |
| FactoryMethodArgumentIsData | NSData |
| FactoryMethodArgumentIsString | java.lang.String NSString |
| FactoryMethodArgumentIsBytes | raw bytes |

```
```

__See also:__
[`valueFactoryMethod`](#apple-he4tk), [`setFactoryMethodArgumentType`](#apple-heyti)

---

### isDerived

public boolean `isDerived()`

Returns `false` if the attribute corresponds exactly to one column in the table associated with its entity, and `true` if it doesn't. For example, an attribute with a definition of "otherAttributeName + 1" is derived.

Note that flattened attributes are also considered as derived attributes.

__See also:__
[`isFlattened`](#apple-ha2dk), [`definition`](#apple-ge4dcnrw)

---

### isFlattened

public boolean `isFlattened()`

Returns `true` if the attribute is flattened, `false` otherwise. A flattened attribute is one that's accessed through an entity's relationships but belongs to another entity.

Note that flattened attributes are also considered to be derived attributes.

__See also:__
[`isDerived`](#apple-ha2da), [`definition`](#apple-ge4dcnrw)

---

### isReadOnly

public boolean `isReadOnly()`

Returns `true` if the value of the attribute can't be modified, `false` if it can.

__See also:__
[`setReadOnly`](#apple-hezto)

---

### name

public java.lang.String `name`()

Returns the attribute's name.

__See also:__
[`columnName`](#apple-ge4dcnbz), [`definition`](#apple-ge4dcnrw)`, [setName](#apple-heytq)`

---

### overridesPrototypeDefinitionForKey

public boolean `overridesPrototypeDefinitionForKey`(java.lang.String _key_)

Returns false if the requested key gets its value from the prototype attribute. If the attribute has an override, then this method returns true. Valid values for key include "columnName," "valueClass," and so on.

__See also:__
[`prototype`](#apple-ge3tqnbt)

---

### parameterDirection

public int `parameterDirection()`

Returns the parameter direction for attributes that are arguments to a stored procedure. This method returns one of the following values:

| __Constant__ | __Description__ |
| Void | No parameters |
| InParameter | Input only parameters |
| OutParameter | Output only parameters |
| InOutParameter | Bidirectional parameters (input and output) |

```
```

__See also:__
[`storedProcedure`](#apple-he3ti), [`storedProcedureForOperation`](EOEntity.md#apple-he2do) (EOEntity), [`setParameterDirection`](#apple-hezde)

---

### parent

public java.lang.Object `parent`()

Returns the attribute's parent, which is either an EOEntity or an EOStoredProcedure. Use this method when you need to find the model for an attribute.

---

### precision

public int `precision()`

Returns the precision of the database representation for attributes with a value class of java.lang.Number or java.math.BigDecimal.

__See also:__
[`scale`](#apple-ha4dg)

---

### prototype

public EOAttribute `prototype()`

Returns the prototype attribute that is used to define default settings for the receiver.

__See also:__
[`overridesPrototypeDefinitionForKey`](#apple-ge3tqnrr)

---

### prototypeName

public java.lang.String `prototypeName()`

Returns the name of the prototype attribute of the receiver.

__See also:__
[`prototype`](#apple-ge3tqnbt)

---

### readFormat

public java.lang.String `readFormat`()

Returns a format string of the appropriate type that can be used when building an expression that contains the value of the attribute.

__See also:__
[`setReadFormat`](#apple-heztc), [`writeFormat`](#apple-geydcma)

---

### scale

public int `scale()`

Returns the scale of the database representation for attributes with a value class of Number or java.math.BigDecimal. The returned value can be negative.

__See also:__
[`precision`](#apple-ha3tk)`, [setScale](#apple-he2dc)`

---

### serverTimeZone

public TimeZone `serverTimeZone`()

Returns the time zone assumed for NSDates in the database server, or the local time zone if one hasn't been set. An EOAdaptorChannel automatically converts dates between the time zones used by the server and the client when fetching and saving values. Applies only to attributes that represent dates.

__See also:__
[`setServerTimeZone`](#apple-he2dk)

---

### setAdaptorValueConversionMethodName

public void `setAdaptorValueConversionMethodName`(java.lang.String _conversionMethodName_)

Sets to _conversionMethodName_ the name of the method used to convert a custom class into one of the primitive types that the adaptor knows how to manipulate: java.lang.String, java.lang.Number, com.apple.yellow.foundation.NSData, or com.apple.yellow.foundation.NSDate..

__See also:__
[`adaptorValueConversionMethodName`](#apple-gq4dioa)

---

### setAllowsNull

public void `setAllowsNull`(boolean _allowsNull_)

Sets according to _allowsNull_ whether or not the attribute can have a `null`value. If the attribute maps directly to a column in the database, it also controls whether the database column can have a NULL value.

__See also:__
[`allowsNull`](#apple-gq4dmoi)

---

### setColumnName

public void `setColumnName`(java.lang.String _columnName_)

Sets to _columnName_ the name of the attribute used in communication with the database server. An adaptor uses this name to identify the column corresponding to the attribute; this name must match the name of a column in the database table corresponding to the attribute's entity.

This method makes a derived or flattened attribute simple; the [`definition`](#apple-ge4dcnrw) is released and the column name takes its place for use with the server.

__Note:__
`setColumnName:` and [`setDefinition`](#apple-heydg) are closely related. Only one can be set at any given time.
Invoking either of these methods causes the other value to be set to `null`

__See also:__
`[columnName](#apple-ge4dcnbz)`

---

### setDefinition

public void `setDefinition`(java.lang.String _definition_)

Sets to _definition_ the attribute's definition as recognized by the database server. _definition_ should be either a value expression defining a derived attribute, such as "salary \* 12", or a data path for a flattened attribute, such as "toAuthor.name".

Prior to invoking this method, the attribute's entity must have been set by adding the attribute to an entity. This method will not function correctly if the attribute's entity has not been set.

This method converts a simple attribute into a derived or flattened attribute; the [`columnName`](#apple-ge4dcnbz) is removed and the definition takes its place for use with the server.

__Note:__
[`setColumnName`](#apple-ha4to) and `setDefinition:` are closely related. Only one can be set at any given time.
Invoking either of these methods causes the other value to be set to `null`.

__See also:__
`[definition](#apple-ge4dcnrw)`

---

### setExternalType

public void `setExternalType`(java.lang.String _typeName_)

Sets to _typeName_ the type used for the attribute in the database adaptor; for example, a Sybase "varchar" or an Oracle7 "NUMBER". Each adaptor defines the set of types that can be supplied to `setExternalType:`. The external type you specify for a given attribute must correspond to the type used in the database server.

__See also:__
[`setDefinition`](#apple-heydg)`, [externalType](#apple-hazdq)`

---

### setFactoryMethodArgumentType

public void `setFactoryMethodArgumentType`(int _argumentType_)

Sets the type of argument that should be passed to the "factory method"-which is invoked by the receiver to create a value for a custom class. Factory methods can accept java.lang.Strings, com.apple.yellow.foundation.NSDatas, or raw bytes; specify an _argumentType_ as EOFactoryMethodArgumentIsNSString, EOFactoryMethodArgumentIsNSData, or EOFactoryMethodArgumentIsBytes as appropriate.

__See also:__
[`setValueFactoryMethodName`](#apple-he2tq)`, [factoryMethodArgumentType](#apple-hazte)`

---

### setName

public void `setName`(java.lang.String _name_)

Sets the attribute's name to _name_. Throws an exception if _name_ is already in use by another attribute or relationship of the same entity, or if _name_ is not a valid attribute name.

__See also:__
[`validateName`](#apple-he4de)`, [name](#apple-ha2tg)`

---

### setParameterDirection

public void `setParameterDirection`(int _parameterDirection_)

Sets the parameter direction for attributes that are arguments to a stored procedure. _parameterDirection_ should be one of the following values:

- EOVoid
- EOInParameter
- EOOutParameter
- EOInOutParameter

__See also:__
`[setStoredProcedure](EOEntity.md#apple-hezti)` (EOEntity), [`parameterDirection`](#apple-ha3dm)

---

### setPrecision

public void `setPrecision`(int _precision_)

Sets to _precision_ the precision of the database representation for attributes with a value class of Number or java.math.BigDecimal.

__See also:__
[`setScale`](#apple-he2dc)`, [precision](#apple-ha3tk)`

---

### setPrototype

public void `setPrototype`(EOAttribute _prototype_)

Sets the prototype attribute. This overrides any existing settings in the attribute.

__See also:__
[`prototype`](#apple-ge3tqnbt)

---

### setReadFormat

public void `setReadFormat`(java.lang.String _aString_)

Sets the format string that's used to format the attribute's value for SELECT statements. In _aString_, %P is replaced by the attribute's external name.

The read format string is used whenever the attribute is referenced in a select list or qualifier.

__See also:__
[`setWriteFormat`](#apple-he3ds)`, [readFormat](#apple-ha3ts)`

---

### setReadOnly

public void `setReadOnly`(boolean _flag_)

Sets whether the value of the attribute can be modified according to _flag_. Throws an exception if _flag_ is `false` and the argument is derived but not flattened.

__See also:__
[`isDerived`](#apple-ha2da), [`isFlattened`](#apple-ha2dk)`, [isReadOnly](#apple-ha2ta)`

---

### setScale

public void `setScale`(int _scale_)

Sets to _scale_ the scale of the database representation for attributes with a value class of Number or java.math.BigDecimal. _scale_ can be negative.

__See also:__
[`setPrecision`](#apple-hezdo)`, [scale](#apple-ha4dg)`

---

### setServerTimeZone

public void `setServerTimeZone`(NSTimeZone _aTimeZone_)

Sets to _aTimeZone_ the time zone used for NSDates in the database server. If _aTimeZone_ is `null` then the local time zone is used. An EOAdaptorChannel automatically converts dates between the time zones used by the server and the client when fetching and saving values. Applies only to attributes that represent dates.

__See also:__
[`serverTimeZone`](#apple-ha4do)

---

### setUserInfo

public void `setUserInfo`(NSDictionary _dictionary_)

Sets to _dictionary_ the dictionary of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, NSDictionary, NSArray, NSData, and java.lang.String).

__See also:__
[`userInfo`](#apple-he3tq)

---

### setValueClassName

public void `setValueClassName`(java.lang.String _name_)

Sets the class name for values of this attribute to _name_. When an EOAdaptorChannel fetches data for the attribute, it's presented to the application as an instance of this class.

The class need not exist in the run-time system when this message is sent, but it must exist when an adaptor channel performs a fetch; if the class isn't present the result depends on the adaptor. See your adaptor's documentation for information on how absent value classes are handled.

__See also:__
[`setValueType`](#apple-he3dc)`, [valueClassName](#apple-he4ta)`

---

### setValueFactoryMethodName

public void `setValueFactoryMethodName`(java.lang.String _factoryMethodName_)

Sets the "factory method"-which is invoked by the attribute to create an attribute value for a custom class-to _factoryMethodName_. The factory method should be a static method returning an object of your custom value class. Use [`setFactoryMethodArgumentType`](#apple-heyti)to specify the type of argument that is to be passed to your factory method.

__See also:__
[`valueFactoryMethodName`](#apple-he4tq)

---

### setValueType

public void `setValueType`(java.lang.String _typeName_)

Sets to _typeName_ the conversion character (such as "i" or "d") for the data type a Number attribute is converted to and from in your application. Value types are scalars such as `int`, `float`, and `double`. Each adaptor supports a different set of conversion characters for numeric types. However, in most (if not all) cases it's safe to supply a value of "i" (int) or "d" (double).

__See also:__
[`setValueClassName`](#apple-gqzdaoa)`, [valueType](#apple-geydamq)`

---

### setWidth

public void `setWidth`(int _length_)

Sets to _length_ the maximum amount of bytes the attribute's value may contain. Adaptors may use this information to allocate space for fetch buffers.

__See also:__
`[width](#apple-geydanq)`

---

### setWriteFormat

public void `setWriteFormat`(java.lang.String _string_)

Sets the format string that's used to format the attribute's value for INSERT or UPDATE expressions. In _string_, %P is replaced by the attribute's value.

__See also:__
`[setReadFormat](#apple-heztc), [writeFormat](#apple-geydcma)`

---

### storedProcedure

public EOStoredProcedure `storedProcedure`()

Returns the stored procedure for which this attribute is an argument. If this attribute isn't an argument to a stored procedure but instead is owned by an entity, this method returns `null`.

__See also:__
[`entity`](#apple-hazdi)

---

### userInfo

public NSDictionary `userInfo`()

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__
[`setUserInfo`](#apple-he2dq)

---

### validateName

public java.lang.Throwable `validateName`(java.lang.String _name_)

Validates _name_ and returns `null` if it is a valid name, or an exception if it isn't. A name is invalid if it has zero length; starts with a character other than a letter, a number, or "@", "#", or "_"; or contains a characterother than a letter, a number, "@", "#", "_", or "$". A name is also invalid if the receiver's EOEntity already has an EOAttribute with the same name, or if the model has a stored procedure that has an argument with the same name.

`setName:` uses this method to validate its argument.

---

### valueClassName

public java.lang.String `valueClassName`()

Returns the name of the class for custom value types. When data is fetched for the attribute, it's presented to the application as an instance of this class.

This class must be present in the run-time system when an EOAdaptorChannel fetches data for the attribute; if the class isn't present the result depends on the adaptor. See your adaptor's documentation for information on how absent value classes are handled.

__See also:__
[`valueType`](#apple-geydamq)`, [setValueClassName](#apple-gqzdaoa)`

---

### valueFactoryMethod

public NSSelector `valueFactoryMethod`()

Returns the factory method that's invoked by the attribute when creating an attribute value that's of a custom class. The value returned from this method is derived from the attribute's [`valueFactoryMethodName`](#apple-he4tq). If that name doesn't map to a valid method in the Java run-time, this method returns `null`.

---

### valueFactoryMethodName

public java.lang.String `valueFactoryMethodName`()

Returns the name of the factory method that's used for creating a custom class value.

__See also:__
[`valueFactoryMethod`](#apple-he4tk)`, [setValueFactoryMethodName](#apple-he2tq)`

---

### valueType

public java.lang.String `valueType`()

Returns the conversion character (such as "i" or "d") for the data type a Number attribute is converted to and from in your application. Value types are scalars such as `int`, `float`, and `double`.

__See also:__
[`valueClassName`](#apple-he4ta)`, [setValueType](#apple-he3dc)`

---

### width

public int `width()`

Returns the maximum length (in bytes) for values that are mapped to this attribute. Returns zero for numeric and date types.

__See also:__
[`setWidth`](#apple-he3dk)

---

### writeFormat

public java.lang.String `writeFormat`()

Returns the format string that's used to format the attribute's value for INSERT or UPDATE expressions. In the returned string, %P is replaced by the attribute's value.

__See also:__
[`readFormat`](#apple-ha3ts)`, [setWriteFormat](#apple-he3ds)`

---

[!](EOAdaptorOperation.md)
[!](Creating%20Attributes.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
