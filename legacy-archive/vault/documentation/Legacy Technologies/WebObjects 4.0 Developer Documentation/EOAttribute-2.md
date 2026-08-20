---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAttribute.html
archived_at: '2026-07-18T01:28:15.768770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAdaptorOperation-2.md)
[!](Creating%20Attributes-2.md)

---

# EOAttribute

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOAttribute.h

---

## Class Description

An EOAttribute represents a column, field or property in a database, and associates an internal name with an external name or expression by which the property is known to the database. The property an EOAttribute represents may be a meaningful value, such as a salary or a name, or it may be an arbitrary value used for identification but with no real-world applicability (ID numbers and foreign keys for relationships fall into this category). An EOAttribute also maintains type information for binding values to the instance variables of objects.

EOAttributes are also used to represent arguments for EOStoredProcedures.

You usually define attributes in your EOModel with the EOModeler application, which is documented in _WebObjects Tools and Techniques_. Your code probably won't need to programmatically interact with EOAttribute unless you're working at the adaptor level. See "[Creating Attributes](Creating%20Attributes-2.md#apple-gm2tgmq)" for information on creating your own attribute objects.

Fore detailed discussion of using attribute objects to map database data types to JavaObjective-C objects, see "[Mapping Attributes](Mapping%20Attributes-2.md#apple-gm2tgmq)." EOAttributes can also alter the way values are selected, inserted, and updated in the database by defining special format strings; see "[SQL Statement Formats](SQL%20Statement%20Formats-2.md#apple-gm2tgmq)" for more information.

---

# Adopted Protocols

**[EOPropertyListEncoding](EOPropertyListEncoding-2.md)**

**---

#

[- awakeWithPropertyList](EOPropertyListEncoding-2.md#apple-hazto)

**---

#

[- encodeIntoPropertyList:](EOPropertyListEncoding-2.md#apple-ha3di)

**[- initWithPropertyList:owner:](EOPropertyListEncoding-2.md#apple-gi3tgny)******

---

## Method Types

**Accessing the entity**

**[- entity](#apple-hazdi)

**[- parent](#apple-g44tmmi)****

**Accessing the name**

**[- setName:](#apple-heytq)

**[- name](#apple-ha2tg)

**[- validateName:](#apple-he4de)

**[- beautifyName](#apple-ge4dcmzs)********

**Accessing date information**

**[- serverTimeZone](#apple-ha4do)

**[- setServerTimeZone:](#apple-he2dk)****

**Accessing external definitions**

**[- setColumnName:](#apple-ha4to)

**[- columnName](#apple-ge4dcnbz)

**[- setDefinition:](#apple-heydg)

**[- definition](#apple-ge4dcnrw)

**[- setExternalType:](#apple-heyta)

**[- externalType](#apple-hazdq)************

**Accessing value type information**

**[- setValueClassName:](#apple-gqzdaoa)

**[- valueClassName](#apple-he4ta)

**[- setValueType:](#apple-he3dc)

**[- valueType](#apple-geydamq)

**[- setAllowsNull:](#apple-ha4ti)

**[- allowsNull](#apple-gq4dmoi)

**[- setPrecision:](#apple-hezdo)

**[- precision](#apple-ha3tk)

**[- setScale:](#apple-he2dc)

**[- scale](#apple-ha4dg)

**[- setWidth:](#apple-he3dk)

**[- width](#apple-geydanq)

**[- validateValue:](#apple-ge3tmmju)**************************

**Converting to adaptor value types**

**[- adaptorValueByConvertingAttributeValue:](#apple-guydkny)

**[- adaptorValueType](#apple-gq4dkoa)****

**Working with custom value types**

**[- setValueFactoryMethodName:](#apple-he2tq)

**[- valueFactoryMethod](#apple-he4tk)

**[- valueFactoryMethodName](#apple-he4tq)

**[- setFactoryMethodArgumentType:](#apple-heyti)

**[- factoryMethodArgumentType](#apple-hazte)

**[- setAdaptorValueConversionMethodName:](#apple-ha4tc)

**[- adaptorValueConversionMethod](#apple-guydama)

**[- adaptorValueConversionMethodName](#apple-gq4dioa)****************

**Accessing attribute characteristics**

**[- setReadOnly:](#apple-hezto)

**[- isReadOnly](#apple-ha2ta)

**[- isDerived](#apple-ha2da)

**[- isFlattened](#apple-ha2dk)********

**Accessing SQL statement formats**

**[- setReadFormat:](#apple-heztc)

**[- readFormat](#apple-ha3ts)

**[- setWriteFormat:](#apple-he3ds)

**[- writeFormat](#apple-geydcma)********

**Accessing the user dictionary**

**[- setUserInfo:](#apple-he2dq)

**[- userInfo](#apple-he3tq)****

**Methods used by the adaptor**

**[- newDateForYear:month:day:hour:minute:second:millisecond:
timezone:zone:](#apple-ge3tcnzr)

**[- newValueForBytes:length:](#apple-ge3tcnzx)

**[- newValueForBytes:length:encoding:](#apple-ge3tcobt)******

**Working with stored procedures**

**[- setParameterDirection:](#apple-hezde)

**[- parameterDirection](#apple-ha3dm)

**[- storedProcedure](#apple-he3ti)******

**Working with prototypes**

**[- overridesPrototypeDefinitionForKey:](#apple-ge3tqnrr)

**[- prototype](#apple-ge3tqnbt)

**[- prototypeName](#apple-ge3tqmjr)

**[- setPrototype:](#apple-ge3tqobt)********

<<Need to add more info to this on the implications to custom value classes.>>

---

## Instance Methods

---

### adaptorValueByConvertingAttributeValue:

- (id)`adaptorValueByConvertingAttributeValue:`(id)_value_

Ensures that _value_ is eitheran NSString, NSNumber, NSData, or NSDate, converting it if necessary. If _value_ needs to be converted, `adaptorValueByConvertingAttributeValue:` uses the adaptor conversion method to convert _value_ to one of these four primitive types. If the attribute hasn't a specific adaptor conversion method, and the type to be fetched from the database is [EOAdaptorBytesType](#apple-gq4dkoa), "archiveData" will be invoked to convert the attribute value.

__See also:__
[- `adaptorValueConversionMethod`](#apple-guydama), [- `adaptorValueType`](#apple-gq4dkoa)

---

### adaptorValueConversionMethod

- (SEL)`adaptorValueConversionMethod`

Returns the method used to convert a custom class into one of the primitive types that the adaptor knows how to manipulate: NSString, NSNumber, NSData, or NSDate. The return value of this method is derived from the attribute's adaptor value conversion method name. If that name doesn't map to a valid selector in the Objective-C run-time, `nil` is returned.

__See also:__
`[- adaptorValueByConvertingAttributeValue:](#apple-guydkny)`, `[- adaptorValueConversionMethodName](#apple-gq4dioa)`

---

### adaptorValueConversionMethodName

- (NSString \*)`adaptorValueConversionMethodName`

Returns the name of the method used to convert a custom class into one of the primitive types that the adaptor knows how to manipulate: NSString, NSNumber, NSData, or NSDate.

__See also:__
`[- adaptorValueByConvertingAttributeValue:](#apple-guydkny)`

---

### adaptorValueType

- (EOAdaptorValueType)`adaptorValueType`

Returns an EOAdaptorValueType that indicates the data type that will be fetched from the database. Currently, this method returns one of the following values:

| __Constant__ | __Description__ |
| EOAdaptorNumberType | A number value |
| EOAdaptorCharactersType | A string of characters |
| EOAdaptorBytesType | Raw bytes |
| EOAdaptorDateType | A date |

```
```

__See also:__
[- `factoryMethodArgumentType`](#apple-hazte)

---

### allowsNull

- (BOOL)`allowsNull`

Returns YES to indicate that the attribute can have a `nil` value, NO otherwise. If the attribute maps directly to a column in the database, it also is used to determine whether the database column can have a NULL value.

__See also:__
[- `setAllowsNull:`](#apple-ha4ti)

---

### beautifyName

- (void)`beautifyName`

Makes the attribute name conform to a standard convention. Names that conform to this style are all lower-case except for the initial letter of each embedded word other than the first, which is upper case. Thus, "NAME" becomes "name", and "FIRST_NAME" becomes "firstName". This method is used in reverse-engineering an EOModel.

__See also:__
[- `validateName:`](#apple-he4de), [- `beautifyNames`](EOModel.md#apple-gqzde) (EOModel)

---

### columnName

- (NSString \*)`columnName`

Returns the name of the column in the database that corresponds to this attribute, or `nil` if the attribute isn't simple (that is, if it's derived or flattened). An adaptor uses this name to identify the column corresponding to the attribute. Your application should never need to use this name. Note that `columnName` and [`definition`](#apple-ge4dcnrw) are mutually exclusive; if one returns a value, the other returns `nil`.

__See also:__
, [- `externalType`](#apple-hazdq)

---

### definition

- (NSString \*)`definition`

Returns a derived or flattened attribute's definition, or `nil` if the attribute is simple. An attribute's definition is either a value expression defining a derived attribute, such as "salary \* 12", or a data path for a flattened attribute, such as "toAuthor.name". Note that [`columnName`](#apple-ge4dcnbz) and `definition` are mutually exclusive; if one returns a value, the other returns `nil`.

__See also:__
[- `externalType`](#apple-hazdq)`, [- setDefinition:](#apple-heydg)`

---

### entity

- (EOEntity \*)`entity`

Returns the entity that owns the attribute, or `nil` if this attribute is acting as an argument for a stored procedure.

__See also:__
[- `storedProcedure`](#apple-he3ti)

---

### externalType

- (NSString \*)`externalType`

Returns the attribute's type as understood by the database; for example, a Sybase "varchar" or an Oracle "NUMBER".

__See also:__
[- `columnName`](#apple-ge4dcnbz)`, [- setExternalType:](#apple-heyta)`

---

### factoryMethodArgumentType

- (EOFactoryMethodArgumentType)`factoryMethodArgumentType`

Returns the type of argument that should be passed to the "factory method"-which is invoked by the attribute to create an attribute value for a custom class. This method returns one of the following values:

| ____Constant____ | __Argument Type__ |
| EOFactoryMethodArgumentIsNSData | NSData |
| EOFactoryMethodArgumentIsNSString | NSString |
| EOFactoryMethodArgumentIsBytes | raw bytes |

```
```

__See also:__
[- `valueFactoryMethod`](#apple-he4tk), [- `setFactoryMethodArgumentType:`](#apple-heyti)

---

### isDerived

- (BOOL)`isDerived`

Returns NO if the attribute corresponds exactly to one column in the table associated with its entity, and YES if it doesn't. For example, an attribute with a definition of "otherAttributeName + 1" is derived.

Note that flattened attributes are also considered as derived attributes.

__See also:__
[- `isFlattened`](#apple-ha2dk), [- `definition`](#apple-ge4dcnrw)

---

### isFlattened

- (BOOL)`isFlattened`

Returns YES if the attribute is flattened, NO otherwise. A flattened attribute is one that's accessed through an entity's relationships but belongs to another entity.

Note that flattened attributes are also considered to be derived attributes.

__See also:__
[- `isDerived`](#apple-ha2da), [- `definition`](#apple-ge4dcnrw)

---

### isReadOnly

- (BOOL)`isReadOnly`

Returns YES if the value of the attribute can't be modified, NO if it can.

__See also:__
[- `setReadOnly:`](#apple-hezto)

---

### name

- (NSString \*)`name`

Returns the attribute's name.

__See also:__
[- `columnName`](#apple-ge4dcnbz), [- `definition`](#apple-ge4dcnrw)`, [- setName:](#apple-heytq)`

---

### newDateForYear:month:day:hour:minute:second:millisecond:timezone:zone:

- (NSCalendarDate \*)`newDateForYear:`(int)_year_ `month:`(unsigned)_month_ `day:`(unsigned)_day_ `hour:`(unsigned)_hour_ `minute:`(unsigned)_minute_ `second:`(unsigned)_second_ `millisecond:`(unsigned)_millisecond_ `timezone:`(NSTimeZone \*)_timezone_ `zone:`(NSZone \*)_zone_

Returns an NSCalendarDate given discrete values for year, month, day, and so on. This method is used by EOAdaptorChannel subclasses to create a calendar date object to return in an adaptor row. For efficiency reasons, the caller is responsible for releasing the return value.

---

### newValueForBytes:length:

- (id)`newValueForBytes:`(const void \*)_bytes_ `length:`(int)_length_

Generates an NSString or custom class value object from a supplied set of bytes. This method is called by the adaptor during value creation while fetching from the database. For efficiency reasons, the caller is responsible for releasing the return value.

---

### newValueForBytes:length:encoding:

- (id)`newValueForBytes:`(const void \*)_bytes_ `length:`(int)_length_ `encoding:`(NSStringEncoding)_encoding_

Generates an NSData or custom class value object from a supplied set of bytes with a given NSStringEncoding. This method is called by the adaptor during value creation while fetching from the database. For efficiency reasons, the caller is responsible for releasing the return value.

---

### overridesPrototypeDefinitionForKey:

- (BOOL)`overridesPrototypeDefinitionForKey:`(NSString \*)_key_

Returns NO if the requested key gets its value from the prototype attribute. If the attribute has an override, then this method returns YES. Valid values for key include @"columnName," @"valueClass," and so on.

__See also:__
[- `prototype`](#apple-ge3tqnbt)

---

### parameterDirection

- (EOParameterDirection)`parameterDirection`

Returns the parameter direction for attributes that are arguments to a stored procedure. This method returns one of the following values:

| __Constant__ | __Description__ |
| EOVoid | No parameters |
| EOInParameter | Input only parameters |
| EOOutParameter | Output only parameters |
| EOInOutParameter | Bidirectional parameters (input and output) |

```
```

__See also:__
[- `storedProcedure`](#apple-he3ti), [- `storedProcedureForOperation:`](EOEntity.md#apple-he2do) (EOEntity), [- `setParameterDirection:`](#apple-hezde)

---

### parent

- (id)`parent`

Returns the attribute's parent, which is either an EOEntity or an EOStoredProcedure. Use this method when you need to find the model for an attribute:

> ```
> EOModel *myModel = [[anAttribute parent] model];
> ```

---

### precision

- (unsigned)`precision`

Returns the precision of the database representation for attributes with a value class of NSNumber or NSDecimalNumber.

__See also:__
[- `scale`](#apple-ha4dg)

---

### prototype

- (EOAttribute \*)`prototype`

Returns the prototype attribute that is used to define default settings for the receiver.

__See also:__
[- `overridesPrototypeDefinitionForKey:`](#apple-ge3tqnrr)

---

### prototypeName

- (NSString \*)`prototypeName`

Returns the name of the prototype attribute of the receiver.

__See also:__
[- `prototype`](#apple-ge3tqnbt)

---

### readFormat

- (NSString \*)`readFormat`

Returns a format string of the appropriate type that can be used when building an expression that contains the value of the attribute.

__See also:__
[- `setReadFormat:`](#apple-heztc), [- `writeFormat`](#apple-geydcma)

---

### scale

- (int)`scale`

Returns the scale of the database representation for attributes with a value class of NSNumber or NSDecimalNumber. The returned value can be negative.

__See also:__
[- `precision`](#apple-ha3tk)`, [- setScale:](#apple-he2dc)`

---

### serverTimeZone

- (NSTimeZone \*)`serverTimeZone`

Returns the time zone assumed for NSDates in the database server, or the local time zone if one hasn't been set. An EOAdaptorChannel automatically converts dates between the time zones used by the server and the client when fetching and saving values. Applies only to attributes that represent dates.

__See also:__
+ __localTimeZone__  (NSTimeZone), [- `setServerTimeZone:`](#apple-he2dk)

---

### setAdaptorValueConversionMethodName:

- (void)`setAdaptorValueConversionMethodName:`(NSString \*)_conversionMethodName_

Sets to _conversionMethodName_ the name of the method used to convert a custom class into one of the primitive types that the adaptor knows how to manipulate: NSString, NSNumber, NSData, or NSDate. Note that your adaptor value conversion method should return an autoreleased object.

__See also:__
[- `adaptorValueConversionMethodName`](#apple-gq4dioa)

---

### setAllowsNull:

- (void)`setAllowsNull:`(BOOL)_allowsNull_

Sets according to _allowsNull_ whether or not the attribute can have a `nil` value. If the attribute maps directly to a column in the database, it also controls whether the database column can have a NULL value.

__See also:__
[- `allowsNull`](#apple-gq4dmoi)

---

### setColumnName:

- (void)`setColumnName:`(NSString \*)_columnName_

Sets to _columnName_ the name of the attribute used in communication with the database server. An adaptor uses this name to identify the column corresponding to the attribute; this name must match the name of a column in the database table corresponding to the attribute's entity.

This method makes a derived or flattened attribute simple; the [`definition`](#apple-ge4dcnrw) is released and the column name takes its place for use with the server.

__Note:__
`setColumnName:` and [`setDefinition:`](#apple-heydg) are closely related. Only one can be set at any given time.
Invoking either of these methods causes the other value to be set to `nil`.

__See also:__
`[- columnName](#apple-ge4dcnbz)`

---

### setDefinition:

- (void)`setDefinition:`(NSString \*)_definition_

Sets to _definition_ the attribute's definition as recognized by the database server. _definition_ should be either a value expression defining a derived attribute, such as "salary \* 12", or a data path for a flattened attribute, such as "toAuthor.name".

Prior to invoking this method, the attribute's entity must have been set by adding the attribute to an entity. This method will not function correctly if the attribute's entity has not been set.

This method converts a simple attribute into a derived or flattened attribute; the [`columnName`](#apple-ge4dcnbz) is released and the definition takes its place for use with the server.

__Note:__
[`setColumnName:`](#apple-ha4to) and `setDefinition:` are closely related. Only one can be set at any given time.
Invoking either of these methods causes the other value to be set to `nil`.

__See also:__
`[- definition](#apple-ge4dcnrw)`

---

### setExternalType:

- (void)`setExternalType:`(NSString \*)_typeName_

Sets to _typeName_ the type used for the attribute in the database adaptor; for example, a Sybase "varchar" or an Oracle7 "NUMBER". Each adaptor defines the set of types that can be supplied to `setExternalType:`. The external type you specify for a given attribute must correspond to the type used in the database server.

__See also:__
[- `setDefinition:`](#apple-heydg)`, [- externalType](#apple-hazdq)`

---

### setFactoryMethodArgumentType:

- (void)`setFactoryMethodArgumentType:`(EOFactoryMethodArgumentType)_argumentType_

Sets the type of argument that should be passed to the "factory method"-which is invoked by the receiver to create a value for a custom class. Factory methods can accept NSStrings, NSDatas, or raw bytes; specify an _argumentType_ as [EOFactoryMethodArgumentIsNSString](#apple-hazte), EOFactoryMethodArgumentIsNSData, or EOFactoryMethodArgumentIsBytes as appropriate.

__See also:__
[- `setValueFactoryMethodName:`](#apple-he2tq)`, [- factoryMethodArgumentType](#apple-hazte)`

---

### setName:

- (void)`setName:`(NSString \*)_name_

Sets the attribute's name to _name_. Raises an NSInvalidArgumentException if _name_ is already in use by another attribute or relationship of the same entity, or if _name_ is not a valid attribute name.

__See also:__
[- `validateName:`](#apple-he4de)`, [- name](#apple-ha2tg)`

---

### setParameterDirection:

- (void)`setParameterDirection:`(EOParameterDirection)_parameterDirection_

Sets the parameter direction for attributes that are arguments to a stored procedure. _parameterDirection_ should be one of the following values:

- [EOVoid](#apple-ha3dm)
- [EOInParameter](#apple-ha3dm)
- [EOOutParameter](#apple-ha3dm)
- [EOInOutParameter](#apple-ha3dm)

__See also:__
`[- setStoredProcedure:forOperation:](EOEntity.md#apple-hezti)` (EOEntity), [- `parameterDirection`](#apple-ha3dm)

---

### setPrecision:

- (void)`setPrecision:`(unsigned)_precision_

Sets to _precision_ the precision of the database representation for attributes with a value class of NSNumber or NSDecimalNumber.

__See also:__
[- `setScale:`](#apple-he2dc)`, [- precision](#apple-ha3tk)`

---

### setPrototype:

- (void)`setPrototype:`(EOAttribute \*)_prototype_

Sets the prototype attribute. This overrides any existing settings in the attribute.

__See also:__
[- `prototype`](#apple-ge3tqnbt)

---

### setReadFormat:

- (void)`setReadFormat:`(NSString \*)_aString_

Sets the format string that's used to format the attribute's value for SELECT statements. In _aString_, %P is replaced by the attribute's external name. For example:

> ```
> [myAttribute setReadFormat:@"TO_UPPER(%P)"];
> ```

The read format string is used whenever the attribute is referenced in a select list or qualifier.

__See also:__
[- `setWriteFormat:`](#apple-he3ds)`, [- readFormat](#apple-ha3ts)`

---

### setReadOnly:

- (void)`setReadOnly:`(BOOL)_flag_

Sets whether the value of the attribute can be modified according to _flag_. Raises an NSInvalidArgumentException if _flag_ is NO and the argument is derived but not flattened.

__See also:__
[- `isDerived`](#apple-ha2da), [- `isFlattened`](#apple-ha2dk)`, [- isReadOnly](#apple-ha2ta)`

---

### setScale:

- (void)`setScale:`(int)_scale_

Sets to _scale_ the scale of the database representation for attributes with a value class of NSNumber or NSDecimalNumber. _scale_ can be negative.

__See also:__
[- `setPrecision:`](#apple-hezdo)`, [- scale](#apple-ha4dg)`

---

### setServerTimeZone:

- (void)`setServerTimeZone:`(NSTimeZone \*)_aTimeZone_

Sets to _aTimeZone_ the time zone used for NSDates in the database server. If _aTimeZone_ is `nil` then the local time zone is used. An EOAdaptorChannel automatically converts dates between the time zones used by the server and the client when fetching and saving values. Applies only to attributes that represent dates.

__See also:__
[- `serverTimeZone`](#apple-ha4do)

---

### setUserInfo:

- (void)`setUserInfo:`(NSDictionary \*)_dictionary_

Sets to _dictionary_ the dictionary of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, NSDictionary, NSArray, NSData, and NSString).

__See also:__
[- `userInfo`](#apple-he3tq)

---

### setValueClassName:

- (void)`setValueClassName:`(NSString \*)_name_

Sets the class name for values of this attribute to _name_. When an EOAdaptorChannel fetches data for the attribute, it's presented to the application as an instance of this class.

The class need not exist in the run-time system when this message is sent, but it must exist when an adaptor channel performs a fetch; if the class isn't present the result depends on the adaptor. See your adaptor's documentation for information on how absent value classes are handled.

As an example, if your attribute's values are instances of NSImage, send the following:

> ```
> [myAttribute setValueClassName:@"NSImage"];
> ```

__See also:__
[- `setValueType:`](#apple-he3dc)`, [- valueClassName](#apple-he4ta)`

---

### setValueFactoryMethodName:

- (void)`setValueFactoryMethodName:`(NSString \*)_factoryMethodName_

Sets the "factory method"-which is invoked by the attribute to create an attribute value for a custom class-to _factoryMethodName_. The factory method should be a class method returning an autoreleased object of your custom value class. Use [`setFactoryMethodArgumentType:`](#apple-heyti)to specify the type of argument that is to be passed to your factory method.

__See also:__
[- `valueFactoryMethodName`](#apple-he4tq)

---

### setValueType:

- (void)`setValueType:`(NSString \*)_typeName_

Sets to _typeName_ the conversion character (such as "i" or "d") for the data type an NSNumber attribute is converted to and from in your application. Value types are scalars such as `int`, `float`, and `double`. Each adaptor supports a different set of conversion characters for numeric types. However, in most (if not all) cases it's safe to supply a value of "i" (int) or "d" (double).

__See also:__
[- `setValueClassName:`](#apple-gqzdaoa)`, [- valueType](#apple-geydamq)`

---

### setWidth:

- (void)`setWidth:`(unsigned)_length_

Sets to _length_ the maximum amount of bytes the attribute's value may contain. Adaptors may use this information to allocate space for fetch buffers.

__See also:__
`[- width](#apple-geydanq)`

---

### setWriteFormat:

- (void)`setWriteFormat:`(NSString \*)_string_

Sets the format string that's used to format the attribute's value for INSERT or UPDATE expressions. In _string_, %P is replaced by the attribute's value. For example:

> ```
> [myAttribute setWriteFormat:@"TO_LOWER(%P)"];
> ```

__See also:__
`[- setReadFormat:](#apple-heztc), [- writeFormat](#apple-geydcma)`

---

### storedProcedure

- (EOStoredProcedure \*)`storedProcedure`

Returns the stored procedure for which this attribute is an argument. If this attribute isn't an argument to a stored procedure but instead is owned by an entity, this method returns `nil`.

__See also:__
[- `entity`](#apple-hazdi)

---

### userInfo

- (NSDictionary \*)`userInfo`

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__
[- `setUserInfo:`](#apple-he2dq)

---

### validateName:

- (NSException \*)`validateName:`(NSString \*)_name_

Validates _name_ and returns `nil` if it is a valid name, or an exception if it isn't. A name is invalid if it has zero length; starts with a character other than a letter, a number, or "@", "#", or "_"; or contains a character other than a letter, a number, "@", "#", "_", or "$". A name is also invalid if the receiver's EOEntity already has an EOAttribute with the same name, or if the model has a stored procedure that has an argument with the same name.

`setName:` uses this method to validate its argument.

---

### validateValue:

- (NSException \*)`validateValue:`(id \*)_valueP_

Validates the argument by converting it to the attribute's value type and by testing other attribute validation constraints (such as `allowsNull`, `width`, and so on). Returns `nil` if _\*valueP_ is deemed to be a legal value for this attribute. Returns a validation exception otherwise. If, during the validation process, any coercion was performed, the converted value is assigned to _\*valueP_.

__See also:__
[- `adaptorValueByConvertingAttributeValue:`](#apple-guydkny), [- `allowsNull`](#apple-gq4dmoi), [- `valueType`](#apple-geydamq), [- `valueClassName`](#apple-he4ta),
[- `width`](#apple-geydanq)

---

### valueClassName

- (NSString \*)`valueClassName`

Returns the name of the class for custom value types. When data is fetched for the attribute, it's presented to the application as an instance of this class. For example, if a column from the database is represented by instances of NSImage, this method returns "NSImage".

This class must be present in the run-time system when an EOAdaptorChannel fetches data for the attribute; if the class isn't present the result depends on the adaptor. See your adaptor's documentation for information on how absent value classes are handled.

__See also:__
[- `valueType`](#apple-geydamq)`, [- setValueClassName:](#apple-gqzdaoa)`

---

### valueFactoryMethod

- (SEL)`valueFactoryMethod`

Returns the factory method that's invoked by the attribute when creating an attribute value that's of a custom class. The value returned from this method is derived from the attribute's [`valueFactoryMethodName`](#apple-he4tq). If that name doesn't map to a valid selector in the Objective-C run-time, this method returns `nil`.

---

### valueFactoryMethodName

- (NSString \*)`valueFactoryMethodName`

Returns the name of the factory method that's used for creating a custom class value.

__See also:__
[- `valueFactoryMethod`](#apple-he4tk)`, [- setValueFactoryMethodName:](#apple-he2tq)`

---

### valueType

- (NSString \*)`valueType`

Returns the conversion character (such as "i" or "d") for the data type an NSNumber attribute is converted to and from in your application. Value types are scalars such as `int`, `float`, and `double`.

__See also:__
[- `valueClassName`](#apple-he4ta)`, [- setValueType:](#apple-he3dc)`

---

### width

- (unsigned)`width`

Returns the maximum length (in bytes) for values that are mapped to this attribute. Returns zero for numeric and date types.

__See also:__
[- `setWidth:`](#apple-he3dk)

---

### writeFormat

- (NSString \*)`writeFormat`

Returns the format string that's used to format the attribute's value for INSERT or UPDATE expressions. In the returned string, %P is replaced by the attribute's value.

__See also:__
[- `readFormat`](#apple-ha3ts)`, [- setWriteFormat:](#apple-he3ds)`

---

[!](EOAdaptorOperation-2.md)
[!](Creating%20Attributes-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
