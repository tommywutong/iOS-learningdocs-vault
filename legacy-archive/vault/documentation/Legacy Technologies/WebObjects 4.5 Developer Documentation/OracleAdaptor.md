---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/Java/Classes/OracleAdaptor.html
archived_at: '2026-07-15T08:11:46.206003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
OracleEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)

# OracleAdaptor

> __Inherits
> from:__  EOAdaptor : NSObject

> __Package:__ com.apple.yellow.oracleeoadaptorjava

---

## Class Description

---

An OracleAdaptor represents a single connection to an Oracle
database server, and is responsible for keeping login and model
information, performing Oracle-specific formatting of SQL expressions,
and reporting errors.

The OracleAdaptor class has these restrictions: You can't
have nested transactions, and the adaptor doesn't support full outer
joins.

## Constants

---

OracleAdaptor defines the following string constants for use
as connection dictionary keys.

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in the connection dictionary__ |
| ServerIdKey | The server ID. Used as the string to connect to the database if values for [HostMachineKey](#apple-inceeq2firbek), [UserNameKey](#apple-inceersdjjauo), and [PasswordKey](#apple-inceeqsfivfek) are not present in the database. |
| HostMachineKey | The name of the host machine. If this key is not present, the string used to log in to the database is of the form "userName/password@serverId". |
| UserNameKey | The name of the user to log in as. |
| PasswordKey | The user's password. |
| ConnectionStringKey | The connection string used to log in to a database server. If this key is present, [ServerIdKey](#apple-inceerseiveem), [HostMachineKey](#apple-inceeq2firbek), [UserNameKey](#apple-inceersdjjauo), and [PasswordKey](#apple-inceeqsfivfek) are ignored. |
| NlsLangKey | The setting to NLS_LANG, which is used to specify the language and character set for server connections. On J systems this option defaults to japanese_japan.jeuc. |

See ["The Connection Dictionary" (page 6)](OracleEOAdaptor%20Framework.md#apple-ijeugrkiijees) in
the OracleEOAdaptor framework introduction for more information
on the connection dictionary and its entries.

OracleAdaptor also defines a string constant for use as a
key in an exception's userInfo dictionary (see [raiseOracleError](OracleChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdnbqw43tfnqxxeyljonsu64tbmnwgkrlsojxxe) in the OracleChannel class
specification).

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in an exception's userInfo dictionary__ |
| OracleErrorKey | The Oracle OCI client library error code. |

## Instance Methods

---

### connectionKeys

`public NSArray connectionKeys()`

Returns an NSArray containing the keys in the
receiver's connection dictionary. You can use this method to prompt
the user to supply values for the connection dictionary.

---

### fetchedValueForDateValue

`public NSGregorianDate fetchedValueForDateValue(
NSGregorianDate value,
EOAttribute attribute)`

Returns an NSGregorianDate based on date whose
millisecond value is set to 0.

---

### fetchedValueForNumberValue

`public Number fetchedValueForNumberValue(
Number value,
EOAttribute attribute)`

Returns a Number based on _numberValue_ that
has been rounded according to the precision and scale specified
for attribute.

---

### oracleConnectionString

`public String oracleConnectionString()`

Returns the user name, password, host machine,
and server id as a string suitable to be supplied as an argument
to `orlon()`.

---

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)
