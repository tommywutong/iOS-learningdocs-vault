---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAdaptor.html
archived_at: '2026-07-18T01:28:08.526203Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAccessGenericFaultHandler.md)
[!](SubclassingEOAdaptor.md)

---

# EOAdaptor

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

EOAdaptor is an abstract class that provides concrete subclasses with a structure for connecting to a database. A concrete subclass of EOAdaptor provides database-specific method implementations and represents a single database server. You never interact with instances of the EOAdaptor class, but you use its static methods, [`adaptorWithName`](#apple-g44di) and [`adaptorWithModel`](#apple-gq2tmmi), to create instances of a concrete subclass. The EOAdaptor class defines the methods that find and load the concrete adaptors from bundles. However, you rarely interact with a concrete adaptor either. Generally, adaptors are automatically created and used by other classes in the Enterprise Objects Framework.

The EOAdaptor class has the following principal attributes:

- Dictionary of connection information
- Array of adaptor contexts

Other framework classes create EOAdaptor objects. [`adaptorWithModel`](#apple-gq2tmmi) creates a new adaptor with the adaptor name in the specified model. [`adaptorWithName`](#apple-g44di) creates a new adaptor with the specified name.

The following table lists the most commonly-used methods in the EOAdaptor class:

| [assertConnectionDictionaryIsValid](#apple-gq4dcmq) | Verifies that the adaptor can connect with its connection information. |
| [setConnectionDictionary](#apple-hezdg) | Sets the connection dictionary. |

```
```

| [assertConnectionDictionaryIsValid](#apple-gq4dcmq) | Verifies that the adaptor can connect with its connection information. |
| [runLoginPanel](#apple-he3tsny) | Runs the login panel without affecting the connection dictionary. |
| [runLoginPanelAndValidateConnectionDictionary](#apple-he4dcny) | Runs the login panel until the user enters valid connection information or cancels the panel. |
| [setConnectionDictionary](#apple-hezdg) | Sets the connection dictionary. |

```
```

For information on subclassing an EOAdaptor, see ["Creating an EOAdaptor Subclass"](SubclassingEOAdaptor.md#apple-gm3domy).

---

## Method Types

**Creating an EOAdaptor**

**[adaptorWithName](#apple-g44di)

**[adaptorWithModel](#apple-gq2tmmi)****

**Accessing an adaptor's name**

**[name](#apple-gm4tooa)**

**Accessing the names of all available adaptors**

**[availableAdaptorNames](#apple-gq3dqmi)**

**Accessing connection information**

**[assertConnectionDictionaryIsValid](#apple-gq4dcmq)

**[connectionDictionary](#apple-gqydqnq)

**[setConnectionDictionary](#apple-hezdg)

**[runLoginPanelAndValidateConnectionDictionary](#apple-he4dcny)

**[runLoginPanel](#apple-he3tsny)

**[databaseEncoding](#apple-ha2tg)************

**Performing database-specific transformations on values**

**[fetchedValueForValue](#apple-ha4ds)

**[fetchedValueForDataValue](#apple-gq4tmma)

**[fetchedValueForDateValue](#apple-ha3to)

**[fetchedValueForNumberValue](#apple-ha4dc)

**[fetchedValueForStringValue](#apple-ha4dk)**********

**Servicing models**

**[canServiceModel](#apple-gq4dinq)

**[internalTypeForExternalTypeInModel](#apple-gqytcnq)

**[externalTypesWithModel](#apple-gq3tcmy)

**[assignExternalInfoForEntireModel](#apple-gq3dgna)

**[assignExternalInfoForEntity](#apple-gq3dona)

**[assignExternalInfoForAttribute](#apple-g44tc)

**[isValidQualifierTypeInModel](#apple-gm4tqni)**************

**Creating adaptor contexts**

**[createAdaptorContext](#apple-gqydmoa)

**[contexts](#apple-gqydooi)****

**Checking connection status**

**[hasOpenChannels](#apple-ha4tk)**

**Accessing a default expression class**

**[setExpressionClassNameForAdaptorClassName](#apple-gq3tema)

**[expressionClass](#apple-he2dcna)

**[defaultExpressionClass](#apple-heztkoa)******

**Accessing an adaptor's login panel**

**[sharedLoginPanelInstance](#apple-he4tmny)

**[runLoginPanelAndValidateConnectionDictionary](#apple-he4dcny)

**[runLoginPanel](#apple-he3tsny)******

**Accessing the delegate**

**[delegate](#apple-gqydimy)

**[setDelegate](#apple-hezdq)****

**Other**

**[createDatabaseWithAdministrativeConnectionDictionary](#apple-geydinzt)

**[dropDatabaseWithAdministrativeConnectionDictionary](#apple-geydmnzt)

**[prototypeAttributes](#apple-geydkmzr)

**********

---

## Constructors

public `EOAdaptor`()

public `EOAdaptor`(java.lang.String _name_)

Creates and returns a new EOAdaptor with _name_. _name_ is usually derived from the base filename (that is, the filename without the ".framework" extension) of the framework from which the adaptor is loaded. For example, the Oracle adaptor is loaded from the framework `OracleEOAdaptor.framework`. When you create an adaptor subclass, override this method to create a new adaptor with _name_.

Never use this constructor directly. It is invoked automatically from `[adaptorWithName](#apple-g44di)` and `[adaptorWithModel](#apple-gq2tmmi)`-EOAdaptor static methods you use to create a new adaptor.

---

## Class Methods

---

### adaptorWithModel

public static java.lang.Object `adaptorWithModel`(EOModel _model_)

Creates and returns a new adaptor by extracting the adaptor name from _model_, invoking `[adaptorWithName](#apple-g44di)`, and assigning _model_'s connection dictionary to the new adaptor. Throws an exception if _model_ is `null,` if _model_'s adaptor name is `null`, or if the adaptor named in _model_ can't be loaded.

__See also:__
__-__ `adaptorName` (EOModel), [`setConnectionDictionary`](#apple-hezdg)

---

### adaptorWithName

public static java.lang.Object `adaptorWithName`(java.lang.String _name_)

Creates and returns a new adaptor, loading it from the framework named _name_ if necessary. For example, this code excerpt creates an adaptor from a framework named `AcmeEOAdaptor.framework`:

> ```
> EOAdaptor myAdaptor = EOAdaptor.adaptorWithName("Acme");
> ```

This method searches the application's main bundle, `~/Library/Frameworks`, `Network/Library/Frameworks`, and `System/Library/Frameworks` for the first framework whose base filename (that is, the filename without the ".framework" extension) corresponds to _name_. However, note that dynamic loading isn't available on PDO platforms. Consequently, you must statically link your adaptor into applications for PDO: In this case, [`adaptorWithName`](#apple-g44di) simply looks in the runtime for an adaptor class corresponding with the specified name. Throws an exception if _name_ is `null` or if an adaptor class corresponding with _name_ can't be found.

Usually you'd use [`adaptorWithModel`](#apple-gq2tmmi) to create a new adaptor, but you can use this method when you don't have a model. In fact, this method is typically used when you're creating an adaptor for the purpose of creating a model from an existing database.

---

### assignExternalInfoForAttribute

public static void `assignExternalInfoForAttribute`(EOAttribute _attribute_)

Overridden by adaptor subclasses to assign database-specific characteristics to _attribute_. EOAdaptor's implementation assigns an external type and then assigns a column name based on the attribute name. For example, __assignExternalInfoForAttribute:__  assigns the column name "FIRST_NAME" to an attribute named "firstName". The method makes no changes to _attribute_'s column name if _attribute_ is derived.

__See also:__
[`assignExternalInfoForEntireModel`](#apple-gq3dgna)

---

### assignExternalInfoForEntireModel

public static void `assignExternalInfoForEntireModel`(EOModel _model_)

Assigns database-specific characteristics to _model_. Used in EOModeler to switch a model's adaptor. This method examines each entity in _model_. If an entity's external name is not set and all of the entity's attribute's external names are not set, then this method uses [`assignExternalInfoForEntity`](#apple-gq3dona) and [`assignExternalInfoForAttribute`](#apple-g44tc) to assign external names. If the entity's external name is set or if any of the entity's attributes' external names are set, then the method doesn't assign external names to the entity or any of its attributes. Regardless, this method assigns external types for all the model's attributes.

---

### assignExternalInfoForEntity

public static void `assignExternalInfoForEntity`(EOEntity _entity_)

Overridden by adaptor subclasses to assign database-specific characteristics to _entity_. EOAdaptor's implementation assigns an external name to _entity_ based on _entity_'s name. For example, ____`assignExternalInfoForEntity` assigns the external name "MOVIE" to an entity named "Movie". An adaptor subclass should override this method to assign additional database-specific characteristics, if any.

__See also:__
[`assignExternalInfoForEntireModel`](#apple-gq3dgna)

---

### assignExternalTypeForAttribute

public static void `assignExternalTypeForAttribute`(EOAttribute _attribute_)

Overridden by adaptor subclasses to assign the external type to _attribute_. EOAdaptor's implementation does nothing. A subclass of EOAdaptor should override this method to assign an external type using _attribute_'s internal type, precision, and length information.

__See also:__
[`assignExternalInfoForEntireModel`](#apple-gq3dgna)

---

### availableAdaptorNames

public static NSArray `availableAdaptorNames`()

Returns an array containing the names of all available adaptors. If no adaptors are found, this method returns an empty array.

__See also:__
[`assignExternalInfoForEntireModel`](#apple-gq3dgna)

---

### externalTypesWithModel

public static NSArray `externalTypesWithModel`(EOModel _model_)

Implemented by subclasses to return the names of the database types (such as Sybase "varchar" or Oracle "NUMBER") for use with the adaptor. _model_ is an optional argument that can be used to supplement the adaptor's set of database types with additional, user-defined database types. See your adaptor's documentation for information on if and how it uses _model_.

An adaptor subclass should implement this method.

---

### internalTypeForExternalTypeInModel

public static java.lang.String `internalTypeForExternalTypeInModel`(java.lang.String _extType_, EOModel _model_)

Implemented by subclasses to return the name of the Java class used to represent values stored in the database as _extType_. _model_ is an optional argument that can be used to supplement the adaptor's set of type mappings with additional mappings for user-defined database types. See your adaptor's documentation for information on if and how it uses _model_. Returns `null` if no mapping for _extType_ is found.An adaptor subclass should implement this method.

---

### setExpressionClassNameForAdaptorClassName

public static void `setExpressionClassNameForAdaptorClassName`(java.lang.String _sqlExpressionClassName_, java.lang.String _adaptorClassName_)

Sets the expression class for instances of the class named _adaptorClassName_ to _sqlExpressionClassName_. If _sqlExpressionClassName_ is `null`, restores the expression class to the default. Throws an exception if _adaptorClassName_ is `null` or the empty string.

Use this method to substitute a subclass of EOSQLExpression for the expression class provided by the adaptor.

---

## Instance Methods

---

### assertConnectionDictionaryIsValid

public void `assertConnectionDictionaryIsValid`()

Implemented by subclasses to verify that the adaptor can connect to the database server with its connection dictionary. Briefly forms a connection to the server to validate the connection dictionary and then closes the connection. Throws an exception if the connection dictionary contains invalid information.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

__See also:__
[`setConnectionDictionary`](#apple-hezdg)

---

### canServiceModel

public boolean `canServiceModel`(EOModel _model_)

Returns `true` if the receiver can service _model_, `false` otherwise. EOAdaptor's implementation returns `true` if the receiver's connection dictionary is equal to _model_'s connection dictionary as determined by NSDictionary's `isEqual:` method.

A subclass of EOAdaptor doesn't need to override this method.

---

### connectionDictionary

public NSDictionary `connectionDictionary`()

Returns the receiver's connection dictionary, or `null` if the adaptor doesn't have one. The connection dictionary contains the values, such as user name and password, needed to connect to the database server. The dictionary's keys identify the information the server expects, and its values are the values that the adaptor will try when connecting. Each adaptor uses different keys; see your adaptor's documentation for keys it uses.

A subclass of EOAdaptor doesn't need to override this method.

__See also:__
[`setConnectionDictionary`](#apple-hezdg)

---

### contexts

public NSArray `contexts`()

Returns the adaptor contexts created by the receiver, or `null` if no adaptor contexts have been created. A subclass of EOAdaptor doesn't need to override this method.

__See also:__
[`createAdaptorContext`](#apple-gqydmoa)

---

### createAdaptorContext

public EOAdaptorContext `createAdaptorContext`()

Implemented by subclasses to create and return a new EOAdaptorContext, or `null` if a new context can't be created. A newly created EOAdaptor has no contexts.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

__See also:__
[`contexts`](#apple-gqydooi)

---

### createDatabaseWithAdministrativeConnectionDictionary

public void `createDatabaseWithAdministrativeConnectionDictionary`(
NSDictionary _connectionDictionary_)

Uses the administrative login information to create the database (or user for Oracle) defined by the _connectionDictionary_.

__See also:__
[`dropDatabaseWithAdministrativeConnectionDictionary`](#apple-geydmnzt), EOLoginPanel class

---

### databaseEncoding

public int `databaseEncoding()`

Returns the string encoding used to encode and decode database strings. An adaptor's database encoding is stored in the connection dictionary with the key "databaseEncoding". If the connection dictionary doesn't have an entry for the database encoding, the default C string encoding is used. This method throws an exception if the receiver's database encoding isn't valid.

A database system stores strings in a particular character set. The Framework needs to know what character set the database system uses so it can encode and decode strings coming from and going to the database server. The string encoding returned from this method specifies the character set the Framework uses.

A subclass of EOAdaptor doesn't need to override this method.

__See also:__
- `availableStringEncodings` (NSString), - `defaultCStringEncoding` (NSString)

---

### defaultExpressionClass

public java.lang.Class `defaultExpressionClass`()

Implemented by subclasses to return the subclass of EOSQLExpression used as the default expression class for the adaptor. You wouldn't ordinarily invoke this method directly. It's invoked automatically to determine which class should be used to represent query language expressions.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

__See also:__
[`setExpressionClassNameForAdaptorClassName`](#apple-gq3tema)

---

### delegate

public java.lang.Object `delegate`()

__See also:__
Returns the receiver's delegate or `null` if a delegate has not been assigned. A subclass of
EOAdaptor doesn't need to override this method.[`setDelegate`](#apple-hezdq)

---

### dropDatabaseWithAdministrativeConnectionDictionary

public void `dropDatabaseWithAdministrativeConnectionDictionary`(
NSDictionary _connectionDictionary_)

Uses the administrative login information to drop the database (or user for Oracle) defined by the _connectionDictionary_.

__See also:__
[`createDatabaseWithAdministrativeConnectionDictionary`](#apple-geydinzt), EOLoginPanel class

---

### expressionClass

public java.lang.Class `expressionClass`()

Returns the subclass of EOSQLExpression used by the receiver for query language expressions. Returns the expression class assigned using the class method [`setExpressionClassNameForAdaptorClassName`](#apple-gq3tema). If no class has been set for the receiver's class, this method determines the expression class by sending `[defaultExpressionClass](#apple-heztkoa)` to `this`.

You wouldn't ordinarily invoke this method directly. It's invoked automatically to determine which class should be used to represent query language expressions.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

---

### fetchedValueForDataValue

public NSData `fetchedValueForDataValue`(
NSData _value_,
EOAttribute _attribute_)

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [`fetchedValueForValue`](#apple-ha4ds) when the value argument is an NSData.

EOAdaptor's implementation returns _value_ unchanged. An adaptor subclass should override this method if the adaptor's database performs transformations on binary types, such as BLOBs.

---

### fetchedValueForDateValue

public NSGregorianDate `fetchedValueForDateValue`(
NSGregorianDate _value_,
EOAttribute _attribute_)

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [`fetchedValueForValue`](#apple-ha4ds) when the value argument is a date.

EOAdaptor's implementation returns _value_ unchanged. An adaptor subclass should override this method to convert or format date values. For example, a concrete adaptor subclass could set _value_'s millisecond value to 0.

---

### fetchedValueForNumberValue

public java.lang.Number `fetchedValueForNumberValue`(java.lang.Number _value_, EOAttribute _attribute_)

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [`fetchedValueForValue`](#apple-ha4ds) when the value argument is a number.

EOAdaptor's implementation returns _value_ unchanged. An adaptor subclass should override this method to convert or format numeric values. For example, a concrete adaptor subclass should probably round _value_ according to the precision and scale _attribute_.

---

### fetchedValueForStringValue

public java.lang.String `fetchedValueForStringValue`(java.lang.String _value_, EOAttribute _attribute_)

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [`fetchedValueForValue`](#apple-ha4ds) when the value argument is a string.

EOAdaptor's implementation trims trailing spaces and returns `nullnil` for zero-length strings. An adaptor subclass should override this method to perform any additional conversion or formatting on string values.

---

### fetchedValueForValue

public java.lang.Object `fetchedValueForValue`(java.lang.Object _value_, EOAttribute _attribute_)

Returns the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. The Framework uses this method to keep enterprise object snapshots in sync with database values. For example, assume that a product's price is marked down 15%. If the product's original price is 5.25, the sale price is 5.25\*.85, or 4.4625. When the Framework updates the product's price, the database server truncates the price to 4.46 (assuming the scale of the database's price column is 2). Before performing the update, the Framework sends the adaptor a`[fetchedValueForValue](#apple-ha4ds)` message with the value 4.4625. The adaptor performs the database-specific transformation and returns 4.46. The Framework assigns the truncated value to the product object and to the product object's snapshot and then proceeds with the update.

An adaptor subclass can override this method or one of the data type-specific `fetchedValue...` methods. EOAdaptor's implementation of `[fetchedValueForValue](#apple-ha4ds)` invokes one of the data type-specific methods depending on _value_'s class. If _value_ is not a string, number, date, or data object (that is, an instance of java.lang.String, java.lang.Number, NSGregorianDate, NSData, or any of their subclasses),`[fetchedValueForValue](#apple-ha4ds)` returns _value_ unchanged.

This method invokes the EOAdaptorDelegates method `adaptor:fetchedValueForAttributeValue:attribute:` which can override the adaptor's default behavior.

__See also:__
[`fetchedValueForDataValue`](#apple-gq4tmma), [`fetchedValueForDateValue`](#apple-ha3to), [`fetchedValueForNumberValue`](#apple-ha4dc),
[`fetchedValueForStringValue`](#apple-ha4dk), __- valueFactoryMethod__  (EOAttribute)

---

### hasOpenChannels

public boolean `hasOpenChannels()`

Returns `true` if any of the receiver's contexts have open channels, `false` otherwise. A subclass of EOAdaptor doesn't need to override this method.

__See also:__
__- hasOpenChannels__  (EOAdaptorContext)

---

### isValidQualifierTypeInModel

public boolean `isValidQualifierTypeInModel`(java.lang.String _typeName_, EOModel _model_)

Implemented by subclasses to return `true` if an attribute of type _typeName_ can be used in a qualifier (a SQL WHERE clause) sent to the database server, or `false` otherwise. _typeName_ is the name of a type as required by the database server, such as Sybase "varchar" or Oracle "NUMBER". _model_ is an optional argument that can be used to supplement the adaptor's set of type mappings with additional mappings for user-defined database types. See your adaptor's documentation for information on if and how it uses _model_.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

---

### name

public java.lang.String `name`()

Returns the adaptor's name; this is usually the base filename of the framework from which the adaptor was loaded. For example, if an adaptor was loaded from a framework named `AcmeEOAdaptor.framework`, this method returns "Acme".

A subclass of EOAdaptor doesn't need to override this method.

__See also:__
[`adaptorWithName`](#apple-g44di)

---

### prototypeAttributes

public NSArray `prototypeAttributes`()

Returns an array of prototype attributes specific to the adaptor class. Adaptor implementers should note that this method looks for an EOModel named EO_adaptorName_Prototypes in the resources directory of the adaptor.

---

### runLoginPanel

public NSDictionary `runLoginPanel`()

Runs the adaptor's login panel by sending a __runPanelForAdaptor:validate:__  message to the adaptor's login panel object with the validate flag `false`. Returns connection information entered in the panel without affecting the adaptor's connection dictionary. The connection dictionary returned isn't validated by this method.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

__See also:__
[`runLoginPanelAndValidateConnectionDictionary`](#apple-he4dcny), [`setConnectionDictionary`](#apple-hezdg),
[`assertConnectionDictionaryIsValid`](#apple-gq4dcmq), [`sharedLoginPanelInstance`](#apple-he4tmny)

---

### runLoginPanelAndValidateConnectionDictionary

public boolean `runLoginPanelAndValidateConnectionDictionary`()

Runs the adaptor's login panel by sending a __runPanelForAdaptor:validate:__  message to the adaptor's login panel object with the validate flag `true`. Returns `true` if the user enters valid connection information, or `false` if the user cancels the panel.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

__See also:__
[`runLoginPanel`](#apple-he3tsny), [`setConnectionDictionary`](#apple-hezdg), [`assertConnectionDictionaryIsValid`](#apple-gq4dcmq),
[`sharedLoginPanelInstance`](#apple-he4tmny)

---

### setConnectionDictionary

public void `setConnectionDictiona`ry(NSDictionary _dictionary_)

Sets the adaptor's connection dictionary to _dictionary_, which must only contain java.lang.String, NSData,NSDictionary, and NSArray objects. Throws an exception if there are any open channels-you can't change connection information while the adaptor is connected.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

__See also:__
[`connectionDictionary`](#apple-gqydqnq), [`hasOpenChannels`](#apple-ha4tk), [`assertConnectionDictionaryIsValid`](#apple-gq4dcmq)

---

### setDelegate

public void `setDelegate`(java.lang.Object _delegate_)

Sets the receiver's delegate to _delegate_, or removes its delegate if _delegate_ is `null`. A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

__See also:__
[`delegate`](#apple-gqydimy)

---

### sharedLoginPanelInstance

public static EOLoginPanel `sharedLoginPanelInstance`()

Returns the receiver's login panel in applications that have a graphical user interface. Returns `null` if the application doesn't have an NSApplication object. Otherwise, looks for the bundle named "LoginPanel" in the resources for the adaptor framework, loads the bundle, and returns an instance of the bundle's principal class (see the NSBundle class specification for information on loading bundles). The returned object is used to implement `[runLoginPanelAndValidateConnectionDictionary](#apple-he4dcny)` and `[runLoginPanel](#apple-he3tsny)`.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

---

[!](EOAccessGenericFaultHandler.md)
[!](SubclassingEOAdaptor.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
