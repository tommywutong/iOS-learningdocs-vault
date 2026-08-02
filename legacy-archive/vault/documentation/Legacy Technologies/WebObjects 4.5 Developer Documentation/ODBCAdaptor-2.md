---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/ODBCEOAdaptor.framework/ObjC_classic/Classes/ODBCAdaptor.html
archived_at: '2026-07-15T08:11:46.102648Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
ODBCEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md) 

# ODBCAdaptor

> __Inherits
> from:__  EOAdaptor : NSObject

> __Declared in:__  ODBCEOAdaptor/ODBCAdaptor.h

---

## Class Description

---

An ODBCAdaptor represents a single connection to an ODBC database
server, and is responsible for keeping login and model information,
performing ODBC-specific formatting of SQL expressions, and reporting
errors.

ODBC (Open Data Base Connectivity) defines a standard interface
that Windows applications can use to access any data source. Unlike
the other Enterprise Objects Frameworks adaptors that support a single
type of database, the ODBC adaptor supports any data source that
has an ODBC driver. Consequently, in addition to having standard
adaptor features, the ODBC adaptor also manages information relating
to the driver and to the data types defined by the data source the
driver supports.

The ODBCAdaptor class doesn't support nested transactions.

## Constants

---

ODBCAdaptor defines the following string constants for use
as connection dictionary keys.

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in the connection dictionary__ |
| dataSourceKey | The name of the data source to connect to. |
| userNameKey | The name of the user to log in as. |
| passwordKey | The user's password. |
| connectionStringKey | The complete string used to connect to the database. If this key is present in the dictionary, [dataSourceKey](#apple-ijeugqsgirbee), [userNameKey](#apple-ijeugr2iindeu), and [passwordKey](#apple-ijeugrsiizdum) are ignored. |
| typeInfoKey | Information about the types supported by the driver. |
| driverInfoKey | Information about driver, including the driver name, version, and so on. |

For more information on the connection dictionary, see ["The Connection Dictionary"](ODBCEOAdaptor%20Framework-2.md#apple-ijbukrsbiraug) in
the ODBCEOAdaptor Framework introduction.

Additionally, ODBCAdaptor defines a string constant for use
as a key in an exception's userInfo dictionary.

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in an exception's userInfo dictionary__ |
| SQLStatesKey | An array of strings. Each string is a five character code corresponding to an ODBC SQL state. |

## Method Types

---

> **Mapping external types
> to internal types**
> : [+ assignExternalTypeForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixwc43tnftw4rlyorsxe3tbnrkhs4dfizxxeqluorzgsytvorstu)
> : [+ externalTypeForOdbcType:model:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixwk6dumvzg4ylmkr4xazkgn5ze6zdcmnkhs4dfhjww6zdfnq5a)
> : [+ getOdbcInfoWithConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixwozluj5sgey2jnztg6v3jorueg33onzswg5djn5xei2ldoruw63tboj4tu)
> : [+ odbcTypeForExternalType:model:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixw6zdcmnkhs4dfizxxerlyorsxe3tbnrkhs4dfhjww6zdfnq5a)
> : [+ odbcTypeForStringRepresentation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixw6zdcmnkhs4dfizxxeu3uojuw4z2smvyhezltmvxhiylunfxw4oq)
> : [+ resetOdbcInfoWithConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixxezltmv2e6zdcmnew4ztpk5uxi2cdn5xg4zldoruw63senfrxi2lpnzqxe6j2)
> : [+ stringRepresentationForOdbcType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixxg5dsnfxgoutfobzgk43fnz2gc5djn5xem33sj5sgey2upfygkoq)
>
> **Access information in
> the connection dictionary**
> : [- odbcConnectionString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3pmrrggq3pnzxgky3unfxw4u3uojuw4zy)
> : [+ driverInfoForModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixwi4tjozsxeslomzxum33sjvxwizlmhi)
> : [+ typeInfoForModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixxi6lqmvew4ztpizxxetlpmrswyoq)
> : [- driverInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3eojuxmzlsjfxgm3y)
> : [- typeInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3upfygkslomzxq)
>
> **Getting the default Expression
> Class**
> : [- defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3emvtgc5lmorcxq4dsmvzxg2lpnzbwyyltom)
>
> **Getting ODBC environment
> information**
> : [- odbcEnvironment](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3pmrrggrloozuxe33onvsw45a)

## Class Methods

---

### assignExternalTypeForAttribute:

`+ (void)assignExternalTypeForAttribute:(EOAttribute
*)attribute`

Sets the external information for _attribute_ based
on the internal type, precision, and width.

---

### driverInfoForModel:

`+ (NSDictionary *)driverInfoForModel:(EOModel
*)model`

Returns an NSDictionary containing the driver
information cached in the connection dictionary of _model_.
If the information is not yet cached in _model_,
connects to the database to get it.

__See Also:__  [+ typeInfoForModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixxi6lqmvew4ztpizxxetlpmrswyoq), [- driverInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3eojuxmzlsjfxgm3y), [- typeInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3upfygkslomzxq)

---

### externalTypeForOdbcType:model:

`+ (NSString *)externalTypeForOdbcType:(int)type
model:(EOModel *)model`

Returns the external type that represents the
best match for an ODBC _type_ in _model_.

---

### getOdbcInfoWithConnectionDictionary:

`+ (NSDictionary *)getOdbcInfoWithConnectionDictionary:(NSDictionary
*)connectionDictionary`

Sets up the typeInfo and driverInfo dictionaries
in _connectionDictionary_, and returns
an updated connection dictionary. Creates an `ODBCAdaptor`, `ODBCContext`,
and `ODBCChannel`, and
connects to the database to get the information for the typeInfo
and driverInfo dictionaries.

---

### odbcTypeForExternalType:model:

`+ (NSString *)odbcTypeForExternalType:(NSString
*)externalType
model:(EOModel *)model`

Returns the ODBC type for _externalType_,
as defined in the typeInfo dictionary in _model_'s
connection dictionary.

---

### odbcTypeForStringRepresentation:

`+ (int)odbcTypeForStringRepresentation:(NSString
*)type`

Returns the ODBC type (such as SQL_CHAR) for _type_ (such
as @"CHAR"). The method [stringRepresentationForOdbcType:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixxg5dsnfxgoutfobzgk43fnz2gc5djn5xem33sj5sgey2upfygkoq) performs
the opposite function: returning a string for a specified ODBC type.
These methods are used in conjunction to encode ODBC types in the
typeInfo dictionary.

---

### resetOdbcInfoWithConnectionDictionary:

`+ (NSDictionary *)resetOdbcInfoWithConnectionDictionary:(NSDictionary
*)connectionDictionary`

Removes the typeInfo and driverInfo dictionaries
from a copy of _connectionDictionary_ and
returns the modified connection dictionary.

---

### stringRepresentationForOdbcType:

`+ (NSString *)stringRepresentationForOdbcType:(int)type`

Returns the string representation of _type_-for
example, for the type SQL_CHAR this method would return the string
@"CHAR". The method [odbcTypeForStringRepresentation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixw6zdcmnkhs4dfizxxeu3uojuw4z2smvyhezltmvxhiylunfxw4oq) performs
the opposite function: returning the ODBC type for a specified string.
These methods are used in conjunction to encode ODBC types in the
typeInfo dictionary.

---

### typeInfoForModel:

`+ (NSDictionary *)typeInfoForModel:(EOModel
*)model`

Returns an NSDictionary containing the type
information cached in the connection dictionary of _model_. If
the information is not yet cached in _model_,
connects to the database to get it.

__See Also:__  [+ driverInfoForModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixwi4tjozsxeslomzxum33sjvxwizlmhi), [- driverInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3eojuxmzlsjfxgm3y), [- typeInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3upfygkslomzxq)

---

## Instance Methods

---

### defaultExpressionClass

`- (Class)defaultExpressionClass`

Returns the ODBCSQLExpression class.

---

### driverInfo

`- (NSDictionary *)driverInfo`

Returns an NSDictionary containing the driver
information cached in the receiver's model's connection dictionary.
If the information is not yet cached in the model, connects to the
database to get it.

__See Also:__  [- typeInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3upfygkslomzxq)

---

### odbcConnectionString

`- (NSString *)odbcConnectionString`

Returns the user name, password, and data source
as a string that's used to connect to the database.

---

### odbcEnvironment

`- (void *)odbcEnvironment`

Returns the ODBC Environment Handle HENV as
a __void\*__; to work with it, you must cast
it to HENV.

---

### typeInfo

`- (NSDictionary *)typeInfo`

Returns an NSDictionary containing the type
information cached in the receiver's model's connection dictionary.
If the information is not yet cached in the model, connects to the
database to get it.

__See Also:__  [- driverInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu6rccinawiylqorxxel3eojuxmzlsjfxgm3y), [+ driverInfoForModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixwi4tjozsxeslomzxum33sjvxwizlmhi), [+ typeInfoForModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2bmrqxa5dpoixxi6lqmvew4ztpizxxetlpmrswyoq)

---

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md)
