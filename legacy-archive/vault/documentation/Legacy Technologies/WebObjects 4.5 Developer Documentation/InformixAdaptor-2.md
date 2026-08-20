---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/ObjC_classic/Classes/InformixAdaptor.html
archived_at: '2026-07-15T08:11:45.876204Z'
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

> __Declared in:__  InformixEOAdaptor/InformixAdaptor.h

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
userInfo dictionary (see [raiseInformixError:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc64tbnfzwkslomzxxe3ljpbcxe4tpoi5a)).

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in an exception's userInfo dictionary__ |
| InformixErrorKey | The error code raised in the Informix server. The value is an NSNumber with the error code as its `long` value, typically a negative number. |

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
> : [+ externalToInternalTypeMap](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjfxgm33snvuxqqlemfyhi33sf5sxq5dfojxgc3cun5ew45dfojxgc3cupfygktlboa)
>
> **Getting information from
> the connection dictionary**
> : [- informixConnectionString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbbw63tomvrxi2lpnzjxi4tjnztq)
> : [- informixDefaultForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbcgkztbovwhirtpojfwk6j2)
> : [- informixPassword](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbigc43to5xxeza)
> : [- informixUserName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbkxgzlsjzqw2zi)
> : [- connectionKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc6y3pnzxgky3unfxw4s3fpfzq)
>
> **Error handling**
> : [- raiseInformixError:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc64tbnfzwkslomzxxe3ljpbcxe4tpoi5a)
>
> **Preparing to connect**
> : [- prepareEnvironmentForConnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc64dsmvygc4tfivxhm2lsn5xg2zloordg64sdn5xg4zldoq)
> : [- resetEnvironmentAfterConnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc64tfonsxirloozuxe33onvsw45cbmz2gk4sdn5xg4zldoq)
>
> **Callback methods**
> : [- informixContextDidDisconnect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbbw63tumv4hirdjmrcgs43dn5xg4zldoq5a)
> : [- informixContextWillConnect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbbw63tumv4hiv3jnrweg33onzswg5b2)
>
> **Getting adaptor-specific
> classes**
> : [- adaptorContextClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc6ylemfyhi33sinxw45dfpb2eg3dbonzq)
> : [- adaptorChannelClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc6ylemfyhi33sinugc3tomvweg3dbonzq)
> : [- defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc6zdfmzqxk3duiv4ha4tfonzws33oinwgc43t)

## Class Methods

---

### externalToInternalTypeMap

`+ (NSDictionary *)externalToInternalTypeMap`

Returns the mapping between each predefined
external (database) type known by the adaptor to a default internal
type. For information on the mapping, see the section in the InformixEOAdaptor Framework
introduction titled ["Data Type Mapping"](InformixEOAdaptor-2.md#apple-ijbukrcjivfeg).

---

## Instance Methods

---

### adaptorChannelClass

`- (Class)adaptorChannelClass`

Returns the InformixChannel class.

---

### adaptorContextClass

`- (Class)adaptorContextClass`

Returns the InformixContext class.

---

### connectionKeys

`- (NSArray *)connectionKeys`

Returns an NSArray containing the keys in the
receiver's connection dictionary. You can use this method to prompt
the user to supply values for the connection dictionary.

---

### defaultExpressionClass

`- (Class)defaultExpressionClass`

Returns the InformixSQLExpression class.

---

### informixConnectionString

`- (NSString *)informixConnectionString`

Returns the user name, password, and database
name as a string suitable to be supplied as an argument to db_connect().

---

### informixContextDidDisconnect:

`- (void)informixContextDidDisconnect:(InformixContext
*)logon`

Callback method that is invoked after the associated
Informix context disconnects.

---

### informixContextWillConnect:

`- (void)informixContextWillConnect:(InformixContext
*)logon`

Callback method that is invoked just before
the associated Informix context disconnects.

---

### informixDefaultForKey:

`- (NSString *)informixDefaultForKey:(NSString
*)key`

Returns the user default setting for _key_.
To get this information it first checks the user defaults, and then the
adaptor's internal defaults dictionary.

---

### informixPassword

`- (NSString *)informixPassword`

Returns the password in the connection dictionary.

---

### informixUserName

`- (NSString *)informixUserName`

Returns the user name in the connection dictionary.

---

### prepareEnvironmentForConnect

`- (void)prepareEnvironmentForConnect`

Prepares the user environment for connection
to an Informix server. Preserves existing environment variables,
replacing them with values obtained from the adaptor's connection
dictionary. Unset variables are set to values obtained from [informixDefaultForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc62lomzxxe3ljpbcgkztbovwhirtpojfwk6j2),
if any.

__See Also:__  [- resetEnvironmentAfterConnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc64tfonsxirloozuxe33onvsw45cbmz2gk4sdn5xg4zldoq)

---

### raiseInformixError:

`- (void)raiseInformixError:(NSString
*)sqlString`

Examines Informix structures for error flags
and raises an exception if one is found. Extracts the error information
in the connection structure and uses it to build and raise an exception.
The error code is available in the exception's user info dictionary
in the entry for the key, `InformixErrorKey`.

---

### resetEnvironmentAfterConnect

`- (void)resetEnvironmentAfterConnect`

Restores any environment variables overwritten
by [prepareEnvironmentForConnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyifsgc4dun5zc64dsmvygc4tfivxhm2lsn5xg2zloordg64sdn5xg4zldoq).

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
