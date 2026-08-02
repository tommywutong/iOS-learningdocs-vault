---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/Java/Classes/SybaseAdaptor.html
archived_at: '2026-07-15T08:11:46.406538Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md) 

# SybaseAdaptor

> __Inherits
> from:__  EOAdaptor : NSObject

> __Package:__ com.apple.yellow.sybaseeoadaptor

---

## Class Description

---

A SybaseAdaptor represents a single connection to a Sybase
database server, and is responsible for keeping login and model
information, performing Sybase-specific formatting of SQL expressions,
and reporting errors.

The features SybaseAdaptor adds to EOAdaptor are as follows:

- The ability to specify a client character set
  and language
- Sybase password encryption

The SybaseAdaptor class has these restrictions: A context
can only manage one channel at a time, and the adaptor doesn't
support full outer joins because the Sybase server itself doesn't
support them.

## Constants

---

SybaseAdaptor defines the following string constants for use
as connection dictionary keys.

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in the connection dictionary__ |
| HOSTNAME | The name of the machine on which the database server runs. |
| DATABASENAME | The name of the database. |
| USERNAME | The name of the user to log in as. |
| PASSWORD | The user's password. |
| LC_ALL_KEY | The setting to LC_ALL, which is used to specify the language and character set for server connections. On J systems this option defaults to japanese. |
| ENCRYPTPASSWORD | Either the string "Yes" or the string "No". If the value is "Yes", the adaptor enables the System 10 password encryption feature before attempting to open a connection. |
| PRIMITIVE_TYPE_MAP | A dictionary representing the database's primitive type map. Sybase allows user defined types in a database that map onto primitive types. For instance, you could define a user type, `primary_key`, and map it to `int`. The primitive type map dictionary would then contain the key "primary_key" with the value "int". |

For more information on the connection dictionary, see ["The Connection Dictionary"](SybaseEOAdaptor%20Framework.md#apple-ijeugrkbjjeuk) in
the SybaseEOAdaptor framework introduction.

## Method Types

---

> **Mapping external types
> to internal types**
> : [externalToInternalTypeMap](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsuczdbob2g64rpmv4hizlsnzqwyvdpjfxhizlsnzqwyvdzobsu2ylq)
> : [primitiveTypeForExternalTypeInModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsuczdbob2g64rpobzgs3ljoruxmzkupfygkrtpojcxq5dfojxgc3cupfygkslojvxwizlm)
>
> **Getting information from
> the connection dictionary**
> : [connectionKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixwg33onzswg5djn5xewzlzom)
>
> **Bracketing calls to ct_connect()**
> : [prepareEnvironmentForConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixxa4tfobqxezkfnz3gs4tpnzwwk3tuizxxeq3pnzxgky3u)
> : [resetEnvironmentAfterConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixxezltmv2ek3twnfzg63tnmvxhiqlgorsxeq3pnzxgky3u)
>
> **Callback methods**
> : [sybaseContextDidDisconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixxg6lcmfzwkq3pnz2gk6duiruwirdjonrw63tomvrxi)
> : [sybaseContextWillConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixxg6lcmfzwkq3pnz2gk6duk5uwy3cdn5xg4zldoq)

## Static Methods

---

### externalToInternalTypeMap

`public static NSDictionary externalToInternalTypeMap()`

Returns the mapping between each predefined
external (database) type known by the adaptor to a default internal
type. For information on the mapping, see the section in the SybaseEOAdaptorFramework
introduction titled ["Data Type Mapping"](SybaseEOAdaptor%20Framework.md#apple-ijbukqscjfbuo).

---

### primitiveTypeForExternalTypeInModel

`public static String primitiveTypeForExternalTypeInModel(
String externalType,
com.apple.yellow.eoaccess.EOModel model)`

Returns the primitive type on which a given
custom type, defined on the server, is based.

---

## Instance Methods

---

### connectionKeys

`public NSArray connectionKeys()`

Returns an NSArray containing the keys in the
receiver's connection dictionary. You can use this method to prompt
the user to supply values for the connection dictionary.

---

### prepareEnvironmentForConnect

`public void prepareEnvironmentForConnect()`

A call to this method should precede all calls
to __ct_connect__() to set the __LC_ALL__ environment
variable setting to the value specified in the model connection
dictionary.

__See Also:__  [resetEnvironmentAfterConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixxezltmv2ek3twnfzg63tnmvxhiqlgorsxeq3pnzxgky3u)

---

### resetEnvironmentAfterConnect

`public void resetEnvironmentAfterConnect()`

A call to this method should follow all calls
to __ct_connect__() to set the __LC_ALL__ environment
variable setting to the value specified in the model connection
dictionary.

__See Also:__  [prepareEnvironmentForConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkbmrqxa5dpoixxa4tfobqxezkfnz3gs4tpnzwwk3tuizxxeq3pnzxgky3u)

---

### sybaseContextDidDisconnect

`public void sybaseContextDidDisconnect(SybaseContext aSybaseContext)`

Callback method that is invoked after the associated
Sybase context disconnects.

---

### sybaseContextWillConnect

`public void sybaseContextWillDisconnect(SybaseContext aSybaseContext)`

Callback method that is invoked just before
the associated Sybase context disconnects.

---

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
