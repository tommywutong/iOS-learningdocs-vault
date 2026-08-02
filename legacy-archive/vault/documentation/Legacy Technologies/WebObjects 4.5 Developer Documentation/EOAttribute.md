---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOAttribute.html
archived_at: '2026-07-15T08:11:31.598975Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAttribute

> __Inherits
> from:__  NSObject

> __Implements:__  [EOPropertyListEncoding](EOPropertyListEncoding.md#apple-ijauiq2hindeq)

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

An EOAttribute represents a column, field or property in a
database, and associates an internal name with an external name
or expression by which the property is known to the database. The
property an EOAttribute represents may be a meaningful value, such
as a salary or a name, or it may be an arbitrary value used for
identification but with no real-world applicability (ID numbers
and foreign keys for relationships fall into this category). An
EOAttribute also maintains type information for binding values to
the instance variables of objects.

EOAttributes are also used to represent arguments for EOStoredProcedures.

You usually define attributes in your EOModel with the EOModeler
application, which is documented in _Enterprise Objects
Framework Tools and Techniques_. Your code probably won't
need to programmatically interact with EOAttribute unless you're
working at the adaptor level. See ["Creating Attributes"](EOAttribute-2.md#apple-incuqq2eireug) for information
on creating your own attribute objects.

Fore detailed discussion of using attribute objects to map
database data types to Java objects, see ["Mapping from Database to Objects"](EOAttribute-2.md#apple-incuqqsgi5cei) and ["Working with Custom Data Types"](EOAttribute-2.md#apple-ineegq2fijbuk).
EOAttributes can also alter the way values are selected, inserted,
and updated in the database by defining special format strings;
see ["SQL Statement Formats"](EOAttribute-2.md#apple-incuqrkbjbauo) for
more information.

## Constants

---

EOAttribute defines the following `int` constants
as possible return values for the EOAttribute method [adaptorValueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsvi6lqmu).
The return value indicates the data type that will be fetched from
the database for the receiving attribute.

- AdaptorNumberType
- AdaptorCharactersType
- AdaptorBytesType
- AdaptorDateType

EOAttribute defines the additional `int` constants
to be used by [factoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmzqwg5dpoj4u2zlunbxwiqlsm52w2zloorkhs4df) and [setFactoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirtbmn2g64tzjvsxi2dpmraxez3vnvsw45cupfygk) to specify
the type of argument that should be passed to the attribute's "factory
method". For more information, see ["Working with Custom Data Types"](EOAttribute-2.md#apple-ineegq2fijbuk).

- FactoryMethodArgumentIsData
- FactoryMethodArgumentIsString
- FactoryMethodArgumentIsBytes

EOAttribute also defines `int` constants
to represent parameter direction for EOAttributes that represent arguments
to a stored procedure. For more information, see the [parameterDirection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobqxeylnmv2gk4senfzgky3unfxw4) method description.

- Void
- InParameter
- OutParameter
- InOutParameter

## Interfaces Implemented

---

> [EOPropertyListEncoding](EOPropertyListEncoding.md#apple-ijauiq2hindeq): [awakeWithPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5qxoyllmvlws5dikbzg64dfoj2hstdjon2a)
> : [encodeIntoPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5sw4y3pmrsus3tun5ihe33qmvzhi6kmnfzxi)

## Method Types

---

> **Constructors**
> : [EOAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpivhuc5duojuwe5lumu)
>
> **Accessing the entity**
> : [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmvxhi2lupe)
> : [parent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobqxezlooq)
>
> **Accessing the name**
> : [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxittbnvsq)
> : [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnzqw2zi)
> : [validateName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy2lemf2gkttbnvsq)
> : [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmjswc5lunfthsttbnvsq)
>
> **Accessing date information**
> : [serverTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxe5tfojkgs3lfljxw4zi)
> : [setServerTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiu3foj3gk4sunfwwkwtpnzsq)
>
> **Accessing external definitions**
> : [setColumnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiq3pnr2w23somfwwk)
> : [columnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf)
> : [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirdfmzuw42lunfxw4)
> : [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o)
> : [setExternalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirlyorsxe3tbnrkhs4df)
> : [externalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmv4hizlsnzqwyvdzobsq)
>
> **Accessing value type
> information**
> : [setValueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkq3mmfzxgttbnvsq)
> : [valueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfinwgc43tjzqw2zi)
> : [setValueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkvdzobsq)
> : [valueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfkr4xazi)
> : [setAllowsNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiqlmnrxxo42oovwgy)
> : [allowsNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfwgy33xonhhk3dm)
> : [setPrecision](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiudsmvrws43jn5xa)
> : [precision](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzgky3jonuw63q)
> : [setScale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiu3dmfwgk)
> : [scale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponrwc3df)
> : [setWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiv3jmr2gq)
> : [width](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5uwi5di)
> : [validateValue:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy2lemf2gkvtbnr2wkoq)
>
> **Converting to adaptor
> value types**
> : [adaptorValueByConvertingAttributeValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsue6kdn5xhmzlsoruw4z2bor2he2lcov2gkvtbnr2wk)
> : [adaptorValueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsvi6lqmu)
>
> **Working with custom value
> types**
> : [setValueFactoryMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkrtbmn2g64tzjvsxi2dpmrhgc3lf)
> : [valueFactoryMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfizqwg5dpoj4u2zlunbxwi)
> : [valueFactoryMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfizqwg5dpoj4u2zlunbxwittbnvsq)
> : [setFactoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirtbmn2g64tzjvsxi2dpmraxez3vnvsw45cupfygk)
> : [factoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmzqwg5dpoj4u2zlunbxwiqlsm52w2zloorkhs4df)
> : [setAdaptorValueConversionMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiqlemfyhi33skzqwy5lfinxw45tfojzws33ojvsxi2dpmrhgc3lf)
> : [adaptorValueConversionMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsug33oozsxe43jn5xe2zlunbxwi)
> : [adaptorValueConversionMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsug33oozsxe43jn5xe2zlunbxwittbnvsq)
> : [archiveDataForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qluorzgsytvorss6ylsmnugs5tfirqxiykgn5ze6ytkmvrxi)
>
> **Accessing attribute characteristics**
> : [setReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiutfmfse63tmpe)
> : [isReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzvezlbmrhw43dz)
> : [isDerived](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzuizlsnf3gkza)
> : [isFlattened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzum3dbor2gk3tfmq)
>
> **Accessing SQL statement
> formats**
> : [setReadFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiutfmfsem33snvqxi)
> : [readFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpojswczcgn5zg2ylu)
> : [setWriteFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiv3snf2gkrtpojwwc5a)
> : [writeFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5zgs5dfizxxe3lboq)
>
> **Accessing the user dictionary**
> : [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivltmvzes3tgn4)
> : [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpovzwk4sjnztg6)
>
> **Working with stored procedures**
> : [setParameterDirection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiudbojqw2zlumvzei2lsmvrxi2lpny)
> : [parameterDirection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobqxeylnmv2gk4senfzgky3unfxw4)
> : [storedProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpon2g64tfmrihe33dmvshk4tf)
>
> **Working with prototypes**
> : [overridesPrototypeDefinitionForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpn53gk4tsnfsgk42qojxxi33upfygkrdfmzuw42lunfxw4rtpojfwk6i)
> : [prototype](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzg65dpor4xazi)
> : [prototypeName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzg65dpor4xazkomfwwk)
> : [setPrototype](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiudsn52g65dzobsq)

## Constructors

---

### EOAttribute

`public EOAttribute(
NSDictionary propertyList,
Object owner)`

Creates a new EOAttribute initialized
from _propertyList_-a dictionary
containing only property list data types (that is, String, NSDictionary,
NSArray, and NSData objects). This constructor is used by EOModeler
when it reads in a Model from a file, for example. The _owner_ argument
should be the EOAttribute's EOEntity or EOStoredProcedure. EOAttributes
created from a property list must receive an [awakeWithPropertyList](EOPropertyListEncoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5qxoyllmvlws5dikbzg64dfoj2hstdjon2a) message immediately
after creation before they are fully functional, but the __awake...__ message
should be deferred until the all of the other objects in the model
have also been created.

---

## Static Methods

---

### archiveDataForObject

`public static NSData archiveDataForObject(NSObject anObject)`

Return _anObject_'s
value as a NSData object whose bytes can be stored in an external
repository.

---

## Instance Methods

---

### adaptorValueByConvertingAttributeValue

`public Object adaptorValueByConvertingAttributeValue(Object value)`

Ensures that _value_ is
either a String, Number, NSData, or NSDate, converting it if necessary.
If _value_ needs to be converted, __adaptorValueByConvertingAttributeValue__ uses
the adaptor conversion method to convert _value_ to
one of these four primitive types. If the attribute hasn't a specific
adaptor conversion method, and the type to be fetched from the database
is [AdaptorBytesType](#apple-incuqskijfbug), [archiveDataForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qluorzgsytvorss6ylsmnugs5tfirqxiykgn5ze6ytkmvrxi) will be
invoked to convert the attribute value.

__See
Also:__  [adaptorValueConversionMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsug33oozsxe43jn5xe2zlunbxwi), [adaptorValueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsvi6lqmu)

---

### adaptorValueConversionMethod

`public NSSelector adaptorValueConversionMethod()`

Returns the method used to convert a custom
class into one of the primitive types that the adaptor knows how
to manipulate: String, Number, NSData, or NSDate. The return value
of this method is derived from the attribute's adaptor value conversion
method name. If that name doesn't map to a valid selector in the Java run-time, null is
returned.

__See Also:__  [adaptorValueByConvertingAttributeValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsue6kdn5xhmzlsoruw4z2bor2he2lcov2gkvtbnr2wk), [adaptorValueConversionMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsug33oozsxe43jn5xe2zlunbxwittbnvsq)

---

### adaptorValueConversionMethodName

`public String adaptorValueConversionMethodName()`

Returns the name of the method used to convert
a custom class into one of the primitive types that the adaptor
knows how to manipulate: String, Number, NSData, or NSDate.

__See
Also:__  [adaptorValueByConvertingAttributeValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsue6kdn5xhmzlsoruw4z2bor2he2lcov2gkvtbnr2wk)

---

### adaptorValueType

`public int adaptorValueType()`

Returns a constant that indicates the data type
that will be fetched from the database. Currently, this method returns
one of the following values:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| `AdaptorNumberType` | A number value |
| `AdaptorCharactersType` | A string of characters |
| `AdaptorBytesType` | Raw bytes |
| `AdaptorDateType` | A date |

__See Also:__  [factoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmzqwg5dpoj4u2zlunbxwiqlsm52w2zloorkhs4df)

---

### allowsNull

`public boolean allowsNull()`

Returns true to indicate that the attribute
can have a null value, false otherwise. If the attribute maps directly
to a column in the database, it also is used to determine whether
the database column can have a NULL value.

__See
Also:__  [setAllowsNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiqlmnrxxo42oovwgy)

---

### beautifyName

`public void beautifyName()`

Makes the attribute name conform to a standard
convention. Names that conform to this style are all lower-case
except for the initial letter of each embedded word other than the
first, which is upper case. Thus, "NAME" becomes "name",
and "FIRST_NAME" becomes "firstName". This method is used
in reverse-engineering an EOModel.

__See Also:__  [nameForExternalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rlooruxi6jpnzqw2zkgn5zek6dumvzg4ylmjzqw2zi) (EOEntity), [validateName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy2lemf2gkttbnvsq), [beautifyNames](EOModel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjvxwizlmf5rgkylvoruwm6komfwwk4y) (EOModel)

---

### columnName

`public String columnName()`

Returns the name of the column in the database
that corresponds to this attribute, or null if the attribute isn't
simple (that is, if it's derived or flattened). An adaptor uses
this name to identify the column corresponding to the attribute.
Your application should never need to use this name. Note that __columnName__ and [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o) are mutually
exclusive; if one returns a value, the other returns null.

__See
Also:__  , [externalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmv4hizlsnzqwyvdzobsq)

---

### definition

`public String definition()`

Returns a derived or flattened attribute's
definition, or null if the attribute is simple. An attribute's definition
is either a value expression defining a derived attribute, such
as "salary \* 12", or a data path for a flattened attribute,
such as "toAuthor.name". Note that [columnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf) and __definition__ are
mutually exclusive; if one returns a value, the other returns null.

__See
Also:__  [externalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmv4hizlsnzqwyvdzobsq), [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirdfmzuw42lunfxw4)

---

### entity

`public EOEntity entity()`

Returns the entity that owns the attribute,
or null if this attribute is acting as an argument for a stored procedure.

__See
Also:__  [storedProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpon2g64tfmrihe33dmvshk4tf)

---

### externalType

`public String externalType()`

Returns the attribute's type as understood
by the database; for example, a Sybase "varchar" or an Oracle
"NUMBER".

__See Also:__  [columnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf), [setExternalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirlyorsxe3tbnrkhs4df)

---

### factoryMethodArgumentType

`public int factoryMethodArgumentType()`

Returns the type of argument that should be
passed to the "factory method"-which is invoked by the attribute
to create an attribute value for a custom class. This method returns
one of the following values:

|  |  |
| --- | --- |
| __Constant__ | __Argument Type__ |
| `FactoryMethodArgumentIsData` | NSData |
| `FactoryMethodArgumentIsString` | String |
| `FactoryMethodArgumentIsBytes` | raw bytes |

__See Also:__  [valueFactoryMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfizqwg5dpoj4u2zlunbxwi), [setFactoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirtbmn2g64tzjvsxi2dpmraxez3vnvsw45cupfygk)

---

### isDerived

`public boolean isDerived()`

Returns false if the attribute corresponds exactly
to one column in the table associated with its entity, and true if
it doesn't. For example, an attribute with a definition of "otherAttributeName
+ 1" is derived.

Note that flattened attributes are also
considered as derived attributes.

__See
Also:__  [isFlattened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzum3dbor2gk3tfmq), [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o)

---

### isFlattened

`public boolean isFlattened()`

Returns true if the attribute is flattened, false otherwise.
A flattened attribute is one that's accessed through an entity's
relationships but belongs to another entity.

Note that flattened
attributes are also considered to be derived attributes.

__See
Also:__  [isDerived](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzuizlsnf3gkza), [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o)

---

### isReadOnly

`public boolean isReadOnly()`

Returns true if the value of the attribute can't
be modified, false if it can.

__See Also:__  [setReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiutfmfse63tmpe)

---

### name

`public String name()`

Returns the attribute's name.

__See
Also:__  [columnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf), [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o), [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxittbnvsq)

---

### overridesPrototypeDefinitionForKey

`public boolean overridesPrototypeDefinitionForKey(String key)`

Returns false if the requested key gets its
value from the prototype attribute. If the attribute has an override,
then this method returns true. Valid values for key include "columnName," "valueClass," and
so on.

__See Also:__  [prototype](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzg65dpor4xazi)

---

### parameterDirection

`public int parameterDirection()`

Returns the parameter direction for attributes
that are arguments to a stored procedure. This method returns one
of the following values:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| `Void` | No parameters |
| `InParameter` | Input only parameters |
| `OutParameter` | Output only parameters |
| `InOutParameter` | Bidirectional parameters (input and output) |

__See Also:__  [storedProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpon2g64tfmrihe33dmvshk4tf), [storedProcedureForOperation](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxg5dpojswiudsn5rwkzdvojsum33sj5ygk4tboruw63q) (EOEntity), [setParameterDirection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiudbojqw2zlumvzei2lsmvrxi2lpny)

---

### parent

`public Object parent()`

Returns the attribute's parent, which is either
an EOEntity or an EOStoredProcedure. Use this method when you need
to find the model for an attribute.

---

### precision

`public int precision()`

Returns the precision of the database representation
for attributes with a value class of Number or java.math.BigDecimal.

__See
Also:__  [scale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponrwc3df)

---

### prototype

`public EOAttribute prototype()`

Returns the prototype attribute that is used
to define default settings for the receiver.

__See
Also:__  [overridesPrototypeDefinitionForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpn53gk4tsnfsgk42qojxxi33upfygkrdfmzuw42lunfxw4rtpojfwk6i)

---

### prototypeName

`public String prototypeName()`

Returns the name of the prototype attribute
of the receiver.

__See Also:__  [prototype](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzg65dpor4xazi)

---

### readFormat

`public String readFormat()`

Returns a format string of the appropriate type
that can be used when building an expression that contains the value
of the attribute.

__See Also:__  [setReadFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiutfmfsem33snvqxi), [writeFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5zgs5dfizxxe3lboq)

---

### scale

`public int scale()`

Returns the scale of the database representation
for attributes with a value class of Number or java.math.BigDecimal.
The returned value can be negative.

__See Also:__  [precision](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzgky3jonuw63q), [setScale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiu3dmfwgk)

---

### serverTimeZone

`public NSTimeZone serverTimeZone()`

Returns the time zone assumed for NSDates in
the database server, or the local time zone if one hasn't been
set. An EOAdaptorChannel automatically converts dates between the
time zones used by the server and the client when fetching and saving
values. Applies only to attributes that represent dates.

__See
Also:__  [setServerTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiu3foj3gk4sunfwwkwtpnzsq)

---

### setAdaptorValueConversionMethodName

`public void setAdaptorValueConversionMethodName(String conversionMethodName)`

Sets to _conversionMethodName_ the
name of the method used to convert a custom class into one of the primitive
types that the adaptor knows how to manipulate: String, Number,
NSData, or NSDate.

__See Also:__  [adaptorValueConversionMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsug33oozsxe43jn5xe2zlunbxwittbnvsq)

---

### setAllowsNull

`public void setAllowsNull(boolean allowsNull)`

Sets according to _allowsNull_ whether
or not the attribute can have a nullvalue. If the attribute maps directly
to a column in the database, it also controls whether the database
column can have a NULL value.

__See Also:__  [allowsNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfwgy33xonhhk3dm)

---

### setColumnName

`public void setColumnName(String columnName)`

Sets to _columnName_ the
name of the attribute used in communication with the database server.
An adaptor uses this name to identify the column corresponding to
the attribute; this name must match the name of a column in the
database table corresponding to the attribute's entity.

This
method makes a derived or flattened attribute simple; the [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o) is released
and the column name takes its place for use with the server.

|  |
| --- |
| __setColumnName__ and [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirdfmzuw42lunfxw4) are closely related. Only one can be set at any given time. Invoking either of these methods causes the other value to be set to null |

__See Also:__  [columnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf)

---

### setDefinition

`public void setDefinition(String definition)`

Sets to _definition_ the
attribute's definition as recognized by the database server. _definition_ should
be either a value expression defining a derived attribute, such
as "salary \* 12", or a data path for a flattened attribute,
such as "toAuthor.name".

Prior to invoking this method,
the attribute's entity must have been set by adding the attribute
to an entity. This method will not function correctly if the attribute's
entity has not been set.

This method converts a simple
attribute into a derived or flattened attribute; the [columnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf) is removed and
the definition takes its place for use with the server.

|  |
| --- |
| [setColumnName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiq3pnr2w23somfwwk) and __setDefinition__ are closely related. Only one can be set at any given time. Invoking either of these methods causes the other value to be set to null. |

__See Also:__  [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmrswm2lonf2gs33o)

---

### setExternalType

`public void setExternalType(String typeName)`

Sets to _typeName_ the
type used for the attribute in the database adaptor; for example,
a Sybase "varchar" or an Oracle7 "NUMBER". Each adaptor
defines the set of types that can be supplied to __setExternalType__.
The external type you specify for a given attribute must correspond
to the type used in the database server.

__See
Also:__  [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirdfmzuw42lunfxw4), [externalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmv4hizlsnzqwyvdzobsq)

---

### setFactoryMethodArgumentType

`public void setFactoryMethodArgumentType(int argumentType)`

Sets the type of argument that should be passed
to the "factory method"-which is invoked by the receiver to
create a value for a custom class. Factory methods can accept Strings,
NSDatas, or raw bytes; specify an _argumentType_ as [FactoryMethodArgumentIsString](#apple-incuqscejjauq), [FactoryMethodArgumentIsData](#apple-incuqsccjfbug),
or [FactoryMethodArgumentIsBytes](#apple-incuqssijjeuq) as
appropriate.

__See Also:__  [setValueFactoryMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkrtbmn2g64tzjvsxi2dpmrhgc3lf), [factoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmzqwg5dpoj4u2zlunbxwiqlsm52w2zloorkhs4df)

---

### setName

`public void setName(String name)`

Sets the attribute's name to _name_. Throws
an exception if _name_ is already in
use by another attribute or relationship of the same entity, or
if _name_ is not a valid attribute
name.

__See Also:__  [validateName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy2lemf2gkttbnvsq), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnzqw2zi)

---

### setParameterDirection

`public void setParameterDirection(int parameterDirection)`

Sets the parameter direction for attributes
that are arguments to a stored procedure. _parameterDirection_ should
be one of the following values:

- [Void](#apple-incuqsccivcue)
- [InParameter](#apple-incuqrkdizfeo)
- [OutParameter](#apple-incuqq2difcus)
- [InOutParameter](#apple-incuqr2hivceq)

__See
Also:__  [setStoredProcedure](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxgzlukn2g64tfmrihe33dmvshk4tf) (EOEntity), [parameterDirection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobqxeylnmv2gk4senfzgky3unfxw4)

---

### setPrecision

`public void setPrecision(int precision)`

Sets to _precision_ the
precision of the database representation for attributes with a value
class of Number or java.math.BigDecimal.

__See
Also:__  [setScale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiu3dmfwgk), [precision](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzgky3jonuw63q)

---

### setPrototype

`public void setPrototype(EOAttribute prototype)`

Sets the prototype attribute. This overrides
any existing settings in the attribute.

__See
Also:__  [prototype](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzg65dpor4xazi)

---

### setReadFormat

`public void setReadFormat(String aString)`

Sets the format string that's used to format
the attribute's value for SELECT statements. In _aString_,
%P is replaced by the attribute's external name.

The read
format string is used whenever the attribute is referenced in a
select list or qualifier.

__See Also:__  [setWriteFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiv3snf2gkrtpojwwc5a), [readFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpojswczcgn5zg2ylu)

---

### setReadOnly

`public void setReadOnly(boolean flag)`

Sets whether the value of the attribute can
be modified according to _flag_. Throws an exception if _flag_ is false and
the argument is derived but not flattened.

__See
Also:__  [isDerived](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzuizlsnf3gkza), [isFlattened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzum3dbor2gk3tfmq), [isReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpnfzvezlbmrhw43dz)

---

### setScale

`public void setScale(int scale)`

Sets to _scale_ the
scale of the database representation for attributes with a value
class of Number or java.math.BigDecimal. _scale_ can
be negative.

__See Also:__  [setPrecision](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiudsmvrws43jn5xa), [scale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponrwc3df)

---

### setServerTimeZone

`public void setServerTimeZone(NSTimeZone aTimeZone)`

Sets to _aTimeZone_ the
time zone used for NSDates in the database server. If _aTimeZone_ is null then
the local time zone is used. An EOAdaptorChannel automatically converts
dates between the time zones used by the server and the client when
fetching and saving values. Applies only to attributes that represent
dates.

__See Also:__  [serverTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxe5tfojkgs3lfljxw4zi)

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets to _dictionary_ the
dictionary of auxiliary data, which your application can use for
whatever it needs. _dictionary_ can
only contain property list data types (that is, NSDictionary, NSArray,
NSData, and String).

__See Also:__  [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpovzwk4sjnztg6)

---

### setValueClassName

`public void setValueClassName(String name)`

Sets the class name for values of this attribute
to _name_. When an EOAdaptorChannel
fetches data for the attribute, it's presented to the application
as an instance of this class.

The class need not exist in the
run-time system when this message is sent, but it must exist when
an adaptor channel performs a fetch; if the class isn't present
the result depends on the adaptor. See your adaptor's documentation
for information on how absent value classes are handled.

__See
Also:__  [setValueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkvdzobsq), [valueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfinwgc43tjzqw2zi)

---

### setValueFactoryMethodName

`public void setValueFactoryMethodName(String factoryMethodName)`

Sets the "factory method"-which is invoked
by the attribute to create an attribute value for a custom class-to _factoryMethodName_.
The factory method should be a static method returning an object
of your custom value class. Use [setFactoryMethodArgumentType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxirtbmn2g64tzjvsxi2dpmraxez3vnvsw45cupfygk)to specify
the type of argument that is to be passed to your factory method.

__See
Also:__  [valueFactoryMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfizqwg5dpoj4u2zlunbxwittbnvsq)

---

### setValueType

`public void setValueType(String typeName)`

Sets to _typeName_ the
conversion character (such as "i" or "d") for the data type a
Number attribute is converted to and from in your application. Value
types are scalars such as __int__, __float__,
and __double__. Each adaptor supports a different
set of conversion characters for numeric types. However, in most
(if not all) cases it's safe to supply a value of "i" (int)
or "d" (double).

__See Also:__  [setValueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkq3mmfzxgttbnvsq), [valueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfkr4xazi)

---

### setWidth

`public void setWidth(int length)`

Sets to _length_ the
maximum amount of bytes the attribute's value may contain. Adaptors
may use this information to allocate space for fetch buffers.

__See
Also:__  [width](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5uwi5di)

---

### setWriteFormat

`public void setWriteFormat(String string)`

Sets the format string that's used to format
the attribute's value for INSERT or UPDATE expressions. In _string_,
%P is replaced by the attribute's value.

__See
Also:__  [setReadFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiutfmfsem33snvqxi), [writeFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5zgs5dfizxxe3lboq)

---

### storedProcedure

`public EOStoredProcedure storedProcedure()`

Returns the stored procedure for which this
attribute is an argument. If this attribute isn't an argument to
a stored procedure but instead is owned by an entity, this method
returns null.

__See Also:__  [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmvxhi2lupe)

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application
can use this to store any auxiliary information it needs.

__See
Also:__  [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivltmvzes3tgn4)

---

### validateName

`public void validateName(String name)`

Validates _name_ and
returns null if it is a valid name, or an exception if it isn't.
A name is invalid if it has zero length; starts with a character
other than a letter, a number, or "@", "#", or "_";
or contains a character other than a letter, a number, "@",
"#", "_", or "$". A name is also invalid if the receiver's EOEntity
already has an EOAttribute with the same name, or if the model has
a stored procedure that has an argument with the same name.

__setName:__ uses
this method to validate its argument.

---

### validateValue:

`public Object validateValue(Object value)`

Validates value by converting it to the attribute's
value type and by testing other attribute validation constraints
(such as __allowsNull__, __width__,
and so on). If, during the validation process, any coercion was performed,
the converted value is returned.

__See Also:__  [adaptorValueByConvertingAttributeValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfsgc4dun5zfmylmovsue6kdn5xhmzlsoruw4z2bor2he2lcov2gkvtbnr2wk), [allowsNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfwgy33xonhhk3dm), [valueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfkr4xazi), [valueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfinwgc43tjzqw2zi), [width](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5uwi5di)

---

### valueClassName

`public String valueClassName()`

Returns the name of the class for custom value
types. When data is fetched for the attribute, it's presented
to the application as an instance of this class.

This class
must be present in the run-time system when an EOAdaptorChannel
fetches data for the attribute; if the class isn't present the
result depends on the adaptor. See your adaptor's documentation for
information on how absent value classes are handled.

__See
Also:__  [valueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfkr4xazi), [setValueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkq3mmfzxgttbnvsq)

---

### valueFactoryMethod

`public NSSelector valueFactoryMethod()`

Returns the factory method that's invoked
by the attribute when creating an attribute value that's of a custom
class. The value returned from this method is derived from the attribute's [valueFactoryMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfizqwg5dpoj4u2zlunbxwittbnvsq). If that name
doesn't map to a valid method in the Java run-time, this method returns null.

---

### valueFactoryMethodName

`public String valueFactoryMethodName()`

Returns the name of the factory method that's
used for creating a custom class value.

__See
Also:__  [valueFactoryMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfizqwg5dpoj4u2zlunbxwi), [setValueFactoryMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkrtbmn2g64tzjvsxi2dpmrhgc3lf)

---

### valueType

`public String valueType()`

Returns the conversion character (such as "i"
or "d") for the data type a Number attribute is converted to
and from in your application. Value types are scalars such as __int__, __float__,
and __double__.

__See
Also:__  [valueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpozqwy5lfinwgc43tjzqw2zi), [setValueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxivtbnr2wkvdzobsq)

---

### width

`public int width()`

Returns the maximum length (in bytes) for values
that are mapped to this attribute. Returns zero for numeric and
date types.

__See Also:__  [setWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiv3jmr2gq)

---

### writeFormat

`public String writeFormat()`

Returns the format string that's used to format
the attribute's value for INSERT or UPDATE expressions. In the
returned string, %P is replaced by the attribute's value.

__See
Also:__  [readFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpojswczcgn5zg2ylu), [setWriteFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjponsxiv3snf2gkrtpojwwc5a)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
