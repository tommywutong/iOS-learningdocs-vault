---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/Java/Classes/InformixAdaptor.html
archived_at: '2026-07-15T08:11:45.748608Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md) 

# InformixAdaptor

> __Inherits
> from:__  EOAdaptor : NSObject

> __Package:__ com.apple.yellow.informixeoadaptor

---

## Class Description

---

An InformixAdaptor represents a single connection to an Informix
database server, and is responsible for keeping login and model
information, performing Informix-specific formatting of SQL expressions, and
reporting errors.

The InformixAdaptor doesn't support full outer joins.

## Constants

---

InformixAdaptor defines the following string constants for
use as connection dictionary keys.

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in the connection dictionary__ |
| dbNameKey | The name of the database. |
| userNameKey | The name of the user to log in as. |
| passwordKey | The user's password. |

It defines a string constant for use as a key in an exception's
userInfo dictionary (see [raiseInformixError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3smfuxgzkjnztg64tnnf4ek4tsn5za)).

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in an exception's userInfo dictionary__ |
| InformixErrorKey | The error code raised in the Informix server. |

InformixAdaptor also defines a string constant to identify
the user defaults domain for the Informix adaptor.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOF_INFORMIX_ADAPTOR | The name of the user defaults domain for the Informix adaptor. |

## Method Types

---

> **Mapping external types
> to internal types**
> : [externalToInternalTypeMap](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5ew4ztpojwws6cbmrqxa5dpoixwk6dumvzg4ylmkrxus3tumvzg4ylmkr4xazknmfya)
>
> **Getting information from
> the connection dictionary**
> : [informixConnectionString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4eg33onzswg5djn5xfg5dsnfxgo)
> : [informixDefaultForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4eizlgmf2wy5cgn5zewzlz)
> : [informixPassword](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4faylton3w64te)
> : [informixUserName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4fk43fojhgc3lf)
> : [connectionKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3dn5xg4zldoruw63slmv4xg)
>
> **Error handling**
> : [raiseInformixError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3smfuxgzkjnztg64tnnf4ek4tsn5za)
>
> **Preparing to connect**
> : [prepareEnvironmentForConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3qojsxaylsmvcw45tjojxw43lfnz2em33sinxw43tfmn2a)
> : [resetEnvironmentAfterConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3smvzwk5cfnz3gs4tpnzwwk3tuifthizlsinxw43tfmn2a)
>
> **Callback methods**
> : [informixContextDidDisconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4eg33oorsxq5cenfsei2ltmnxw43tfmn2a)
> : [informixContextWillConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4eg33oorsxq5cxnfwgyq3pnzxgky3u)
>
> **Getting adaptor-specific
> classes**
> : [adaptorContextClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3bmrqxa5dpojbw63tumv4hiq3mmfzxg)
> : [adaptorChannelClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3bmrqxa5dpojbwqylonzswyq3mmfzxg)

## Static Methods

---

### externalToInternalTypeMap

`public static NSDictionary externalToInternalTypeMap()`

Returns the mapping between each predefined
external (database) type known by the adaptor to a default internal
type. For information on the mapping, see the section in the InformixEOAdaptor Framework
introduction titled ["Data Type Mapping"](InformixEOAdaptor.md#apple-ijbukrcjivfeg).

---

## Instance Methods

---

### adaptorChannelClass

`public Class adaptorChannelClass()`

Returns the InformixChannel class.

---

### adaptorContextClass

`public Class adaptorContextClass()`

Returns the InformixContext class.

---

### connectionKeys

`public NSArray connectionKeys()`

Returns an NSArray containing the keys in the
receiver's connection dictionary. You can use this method to prompt
the user to supply values for the connection dictionary.

---

### informixConnectionString

`public String informixConnectionString()`

Returns the user name, password, and database
name as a string suitable to be supplied as an argument to db_connect().

---

### informixContextDidDisconnect

`public void informixContextDidDisconnect(InformixContext logon)`

Callback method that is invoked after the associated
Informix context disconnects.

---

### informixContextWillConnect

`public void informixContextWillConnect(InformixContext logon)`

Callback method that is invoked just before
the associated Informix context disconnects.

---

### informixDefaultForKey

`public String informixDefaultForKey(String key)`

Returns the user default setting for _key_.
To get this information it first checks the user defaults, and then the
adaptor's internal defaults dictionary.

---

### informixPassword

`public String informixPassword()`

Returns the password in the connection dictionary.

---

### informixUserName

`public String informixUserName()`

Returns the user name in the connection dictionary.

---

### prepareEnvironmentForConnect

`public void prepareEnvironmentForConnect()`

Prepares the user environment for connection
to an Informix server. Preserves existing environment variables,
replacing them with values obtained from the adaptor's connection
dictionary. Unset variables are set to values obtained from [informixDefaultForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3jnztg64tnnf4eizlgmf2wy5cgn5zewzlz),
if any.

__See Also:__  [resetEnvironmentAfterConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3smvzwk5cfnz3gs4tpnzwwk3tuifthizlsinxw43tfmn2a)

---

### raiseInformixError

`public void raiseInformixError(String sqlString)`

Examines Informix structures for error flags
and raises an exception if one is found. Extracts the error information
in the connection structure and uses it to build and raise an exception.
The error code is available in the exception's user info dictionary
in the entry for the key, `InformixErrorKey`.

---

### resetEnvironmentAfterConnect

`public void resetEnvironmentAfterConnect()`

Restores any environment variables overwritten
by [prepareEnvironmentForConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbawiylqorxxel3qojsxaylsmvcw45tjojxw43lfnz2em33sinxw43tfmn2a).

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
