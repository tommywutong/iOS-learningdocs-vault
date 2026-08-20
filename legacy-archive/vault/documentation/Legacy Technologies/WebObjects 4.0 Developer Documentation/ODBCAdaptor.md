---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/ODBCAdaptor.html
archived_at: '2026-07-18T01:28:48.257771Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20ODBCEOAdaptor%20Framework.md)
[!](ODBCChannel.md)

---

# ODBCAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Inherits From:__
com.apple.yellow.odbceoadaptor

---

## Class Description

An ODBCAdaptor represents a single connection to an ODBC database server, and is responsible for keeping login and model information, performing ODBC-specific formatting of SQL expressions, and reporting errors.

ODBC (Open Data Base Connectivity) defines a standard interface that Windows applications can use to access any data source. Unlike the other Enterprise Objects Frameworks adaptors that support a single type of database, the ODBC adaptor supports any data source that has an ODBC driver. Consequently, in addition to having standard adaptor features, the ODBC adaptor also manages information relating to the driver and to the data types defined by the data source the driver supports.

The ODBCAdaptor class doesn't support nested transactions.

---

## Method Types

**Mapping external types to internal types**

**[externalTypeForOdbcType](#apple-gq3q)

**[getOdbcInfoWithConnectionDictionary](#apple-gu2q)

**[odbcTypeForExternalType](#apple-gyzq)

**[odbcTypeForStringRepresentation](#apple-gy3q)

**[resetOdbcInfoWithConnectionDictionary](#apple-g4yq)

**[stringRepresentationForOdbcType](#apple-g42q)************

**Access information in the connection dictionary**

**[driverInfoForModel](#apple-gqzq)

**[typeInfoForModel](#apple-g44q)

**[driverInfo](#apple-he2q)

**[typeInfo](#apple-geytc)********

**Testing the connection dictionary**

**[odbcConnectionString](#apple-geydg)**

#

---

### driverInfoForModel

public static com.apple.yellow.foundation.NSDictionary `driverInfoForModel`(com.apple.yellow.eoaccess.EOModel _model_)

Returns an NSDictionary containing the driver information cached in the connection dictionary of _model_. If the information is not yet cached in _model_, connects to the database to get it.

__See also:__
[`typeInfoForModel`](#apple-g44q), [`driverInfo`](#apple-he2q), [`typeInfo`](#apple-geytc)

---

### externalTypeForOdbcType

public static java.lang.String `externalTypeForOdbcType`(int _type_, com.apple.yellow.eoaccess.EOModel _model_)

Returns the external type that represents the best match for an ODBC _type_ in _model_.

---

### getOdbcInfoWithConnectionDictionary

public static com.apple.yellow.foundation.NSDictionary `getOdbcInfoWithConnectionDictionary`(com.apple.yellow.foundation.NSDictionary _connectionDictionary_)

Sets up the typeInfo and driverInfo dictionaries in _connectionDictionary_, and returns an updated connection dictionary. Creates an ODBCAdaptor, ODBCContext, and ODBCChannel, and connects to the database to get the information for the typeInfo and driverInfo dictionaries.

---

### odbcTypeForExternalType

public static java.lang.String `odbcTypeForExternalType`(java.lang.String _externalType_, com.apple.yellow.eoaccess.EOModel _model_)

Returns the ODBC type for _externalType_, as defined in the typeInfo dictionary in _model_'s connection dictionary.

---

### odbcTypeForStringRepresentation

public static int `odbcTypeForStringRepresentation`(java.lang.String _type_)

Returns the ODBC type (such as SQL_CHAR) for _type_ (such as @"CHAR"). The method [`stringRepresentationForOdbcType`](#apple-g42q) performs the opposite function: returning a string for a specified ODBC type. These methods are used in conjunction to encode ODBC types in the typeInfo dictionary.

---

### resetOdbcInfoWithConnectionDictionary

public static com.apple.yellow.foundation.NSDictionary `resetOdbcInfoWithConnectionDictionary`(com.apple.yellow.foundation.NSDictionary _connectionDictionary_)

Removes the typeInfo and driverInfo dictionaries from a copy of _connectionDictionary_ and returns the modified connection dictionary.

---

### stringRepresentationForOdbcType

public static java.lang.String `stringRepresentationForOdbcType`(int _type_)

Returns the string representation of _type_-for example, for the type SQL_CHAR this method would return the string @"CHAR". The method [`odbcTypeForStringRepresentation`](#apple-gy3q) performs the opposite function: returning the ODBC type for a specified string. These methods are used in conjunction to encode ODBC types in the typeInfo dictionary.

---

### typeInfoForModel

public static com.apple.yellow.foundation.NSDictionary `typeInfoForModel`(com.apple.yellow.eoaccess.EOModel _model_)

Returns an NSDictionary containing the type information cached in the connection dictionary of _model_. If the information is not yet cached in _model_, connects to the database to get it.

__See also:__
[`driverInfoForModel`](#apple-gqzq), [`driverInfo`](#apple-he2q), [`typeInfo`](#apple-geytc)

---

## Instance Methods

---

### driverInfo

public com.apple.yellow.foundation.NSDictionary `driverInfo`()

Returns an NSDictionary containing the driver information cached in the receiver's model's connection dictionary. If the information is not yet cached in the model, connects to the database to get it.

__See also:__
[`typeInfo`](#apple-geytc)

---

### odbcConnectionString

public java.lang.String `odbcConnectionString`()

Returns the user name, password, and data source as a string that's used to connect to the database.

---

### typeInfo

public com.apple.yellow.foundation.NSDictionary `typeInfo`()

Returns an NSDictionary containing the type information cached in the receiver's model's connection dictionary. If the information is not yet cached in the model, connects to the database to get it.

__See also:__
[`driverInfo`](#apple-he2q), [`driverInfoForModel`](#apple-gqzq), [`typeInfoForModel`](#apple-g44q)

---

[!](The%20ODBCEOAdaptor%20Framework.md)
[!](ODBCChannel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
