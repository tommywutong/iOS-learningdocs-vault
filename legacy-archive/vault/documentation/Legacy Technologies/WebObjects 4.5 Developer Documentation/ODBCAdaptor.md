---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/ODBCEOAdaptor.framework/Java/Classes/ODBCAdaptor.html
archived_at: '2026-07-15T08:11:46.013218Z'
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

> __Package:__ com.apple.yellow.odbceoadaptor

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

For more information on the connection dictionary, see ["The Connection Dictionary"](ODBCEOAdaptor%20Framework.md#apple-ijbukrsbiraug) in
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
> : [assignExternalTypeForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwfi6lqmvdg64sbor2he2lcov2gk)
> : [externalTypeForOdbcType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc6zlyorsxe3tbnrkhs4dfizxxet3emjrvi6lqmu)
> : [getOdbcInfoWithConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc6z3forhwiytdjfxgm32xnf2gqq3pnzxgky3unfxw4rdjmn2gs33omfzhs)
> : [odbcTypeForExternalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc633emjrvi6lqmvdg64sfpb2gk4tomfwfi6lqmu)
> : [odbcTypeForStringRepresentation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc633emjrvi6lqmvdg64storzgs3thkjsxa4tfonsw45dboruw63q)
> : [resetOdbcInfoWithConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc64tfonsxit3emjrus3tgn5lws5diinxw43tfmn2gs33oiruwg5djn5xgc4tz)
> : [stringRepresentationForOdbcType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc643uojuw4z2smvyhezltmvxhiylunfxw4rtpojhwiytdkr4xazi)
>
> **Access information in
> the connection dictionary**
> : [odbcConnectionString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpn5sgey2dn5xg4zldoruw63storzgs3th)
> : [driverInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc6zdsnf3gk4sjnztg6rtpojgw6zdfnq)
> : [typeInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc65dzobsus3tgn5dg64snn5sgk3a)
> : [driverInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpmrzgs5tfojew4ztp)
> : [typeInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpor4xazkjnztg6)

## Static Methods

---

### assignExternalTypeForAttribute

`public static void assignExternalInfoForAttribute(EOAttribute attribute)`

Sets the external information for _attribute_ based
on the internal type, precision, and width.

---

### driverInfoForModel

`public static NSDictionary driverInfoForModel(com.apple.yellow.eoaccess.EOModel model)`

Returns an NSDictionary containing the driver
information cached in the connection dictionary of _model_.
If the information is not yet cached in _model_,
connects to the database to get it.

__See Also:__  [typeInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc65dzobsus3tgn5dg64snn5sgk3a), [driverInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpmrzgs5tfojew4ztp), [typeInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpor4xazkjnztg6)

---

### externalTypeForOdbcType

`public static String externalTypeForOdbcType(
int type,
com.apple.yellow.eoaccess.EOModel model)`

Returns the external type that represents the
best match for an ODBC _type_ in _model_.

---

### getOdbcInfoWithConnectionDictionary

`public static NSDictionary getOdbcInfoWithConnectionDictionary(NSDictionary connectionDictionary)`

Sets up the typeInfo and driverInfo dictionaries
in _connectionDictionary_, and returns
an updated connection dictionary. Creates an `ODBCAdaptor`, `ODBCContext`,
and `ODBCChannel`, and
connects to the database to get the information for the typeInfo
and driverInfo dictionaries.

---

### odbcTypeForExternalType

`public static String odbcTypeForExternalType(
String externalType,
com.apple.yellow.eoaccess.EOModel model)`

Returns the ODBC type for _externalType_,
as defined in the typeInfo dictionary in _model_'s
connection dictionary.

---

### odbcTypeForStringRepresentation

`public static int odbcTypeForStringRepresentation(String type)`

Returns the ODBC type (such as SQL_CHAR) for _type_ (such
as @"CHAR"). The method [stringRepresentationForOdbcType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc643uojuw4z2smvyhezltmvxhiylunfxw4rtpojhwiytdkr4xazi) performs
the opposite function: returning a string for a specified ODBC type.
These methods are used in conjunction to encode ODBC types in the
typeInfo dictionary.

---

### resetOdbcInfoWithConnectionDictionary

`public static NSDictionary resetOdbcInfoWithConnectionDictionary(NSDictionary connectionDictionary)`

Removes the typeInfo and driverInfo dictionaries
from a copy of _connectionDictionary_ and
returns the modified connection dictionary.

---

### stringRepresentationForOdbcType

`public static String stringRepresentationForOdbcType(int type)`

Returns the string representation of _type_-for
example, for the type SQL_CHAR this method would return the string
@"CHAR". The method [odbcTypeForStringRepresentation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc633emjrvi6lqmvdg64storzgs3thkjsxa4tfonsw45dboruw63q) performs
the opposite function: returning the ODBC type for a specified string.
These methods are used in conjunction to encode ODBC types in the
typeInfo dictionary.

---

### typeInfoForModel

`public static NSDictionary typeInfoForModel(com.apple.yellow.eoaccess.EOModel model)`

Returns an NSDictionary containing the type
information cached in the connection dictionary of _model_. If
the information is not yet cached in _model_,
connects to the database to get it.

__See Also:__  [driverInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc6zdsnf3gk4sjnztg6rtpojgw6zdfnq), [driverInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpmrzgs5tfojew4ztp), [typeInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpor4xazkjnztg6)

---

## Instance Methods

---

### driverInfo

`public NSDictionary driverInfo()`

Returns an NSDictionary containing the driver
information cached in the receiver's model's connection dictionary.
If the information is not yet cached in the model, connects to the
database to get it.

__See Also:__  [typeInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpor4xazkjnztg6)

---

### odbcConnectionString

`public String odbcConnectionString()`

Returns the user name, password, and data source
as a string that's used to connect to the database.

---

### typeInfo

`public NSDictionary typeInfo()`

Returns an NSDictionary containing the type
information cached in the receiver's model's connection dictionary.
If the information is not yet cached in the model, connects to the
database to get it.

__See Also:__  [driverInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t2eijbuczdbob2g64rpmrzgs5tfojew4ztp), [driverInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc6zdsnf3gk4sjnztg6rtpojgw6zdfnq), [typeInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5huiqsdifsgc4dun5zc65dzobsus3tgn5dg64snn5sgk3a)

---

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md)
