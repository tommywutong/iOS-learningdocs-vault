---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOAdaptor.html
archived_at: '2026-07-15T08:13:41.167085Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOAdaptor

> __Inherits from:__ Object

> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

EOAdaptor is an abstract class that provides concrete subclasses with a structure for connecting to a database. A concrete subclass of EOAdaptor provides database-specific method implementations and represents a single database server. You never interact with instances of the EOAdaptor class, but you use its static methods, [adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu) and [adaptorWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue233emvwa), to create instances of a concrete subclass. The EOAdaptor class defines the methods that find and load the concrete adaptors from bundles. However, you rarely interact with a concrete adaptor either. Generally, adaptors are automatically created and used by other classes in the Enterprise Objects Framework.

|  |
| --- |
| __Note:__ EOAdaptor is abstract. Never create instances of the EOAdaptor class. |

The EOAdaptor class has the following principal attributes:

- Dictionary of connection information
- Array of adaptor contexts
- Expression class

Other framework classes create EOAdaptor objects. [adaptorWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue233emvwa) creates a new adaptor with the adaptor name in the specified model. [adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu) creates a new adaptor with the specified name.

The following table lists the most commonly-used methods in the EOAdaptor class:

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonsxe5cdn5xg4zldoruw63senfrxi2lpnzqxe6kjonlgc3djmq) | Verifies that the adaptor can connect with its connection information. |
| [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forbw63tomvrxi2lpnzcgsy3unfxw4ylspe) | Sets the connection dictionary. |

For information on subclassing an EOAdaptor, see ["Creating an EOAdaptor Subclass" (page 35)](EOAdaptor.Concepts.md#apple-ijbukq2ejbceo).

## Method Types

---

> Creating an EOAdaptor[adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu)[adaptorWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue233emvwa)Accessing an adaptor's name[name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc63tbnvsq)Connecting to a database server[assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonsxe5cdn5xg4zldoruw63senfrxi2lpnzqxe6kjonlgc3djmq)[connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3pnzxgky3unfxw4rdjmn2gs33omfzhs)[setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forbw63tomvrxi2lpnzcgsy3unfxw4ylspe)[isDroppedConnectionException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62ltirzg64dqmvseg33onzswg5djn5xek6ddmvyhi2lpny)[handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbnzsgyzkeojxxa4dfmrbw63tomvrxi2lpny)Performing database-specific transformations on values[fetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk)[fetchedValueForDataValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxerdborqvmylmovsq)[fetchedValueForDateValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxerdborsvmylmovsq)[fetchedValueForNumberValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxettvnvrgk4swmfwhkzi)[fetchedValueForStringValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxeu3uojuw4z2wmfwhkzi)Servicing models[canServiceModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3bnzjwk4twnfrwktlpmrswy)[internalTypeForExternalType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62loorsxe3tbnrkhs4dfizxxerlyorsxe3tbnrkhs4df)[externalTypesWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zlyorsxe3tbnrkhs4dfonlws5dijvxwizlm)[assignExternalInfoForEntireModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs4tfjvxwizlm)[assignExternalInfoForEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs5dz)[assignExternalInfoForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sbor2he2lcov2gk)[isValidQualifierType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62ltkzqwy2lekf2wc3djmzuwk4supfygk)Creating adaptor contexts[createAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3smvqxizkbmrqxa5dpojbw63tumv4hi)[contexts](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3pnz2gk6duom)Checking connection status[hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbonhxazloinugc3tomvwhg)Accessing a default expression class[setExpressionClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5zwk5cfpbyhezltonuw63sdnrqxg42omfwwk)[expressionClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zlyobzgk43tnfxw4q3mmfzxg)[defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdfmzqxk3duiv4ha4tfonzws33oinwgc43t)Accessing the delegate[delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdfnrswoylumu)[setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forcgk3dfm5qxizi)[setDefaultDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5zwk5cemvtgc5lmorcgk3dfm5qxizi)[defaultDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5sgkztbovwhirdfnrswoylumu)Creating and dropping databases[createDatabaseWithAdministrativeConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3smvqxizkemf2gcytbonsvo2lunbawi3ljnzuxg5dsmf2gs5tfinxw43tfmn2gs33oiruwg5djn5xgc4tz)[dropDatabaseWithAdministrativeConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdsn5yeiylumfrgc43fk5uxi2cbmrwws3tjon2heylunf3gkq3pnzxgky3unfxw4rdjmn2gs33omfzhs)Providing prototype attributes[prototypeAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc64dsn52g65dzobsuc5duojuwe5lumvzq)

## Constructors

---

### EOAdaptor

`public EOAdaptor(String name)`

Creates and returns a new EOAdaptor with _name_. _name_ is usually derived from the base filename (that is, the filename without the ".framework" extension) of the framework from which the adaptor is loaded. For example, the Oracle adaptor is loaded from the framework __OracleEOAdaptor.framework__. When you create an adaptor subclass, override this method to create a new adaptor with _name_.

Never use this constructor directly. It is invoked automatically from [adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu) and [adaptorWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue233emvwa)-EOAdaptor static methods you use to create a new adaptor.

---

## Static Methods

---

### adaptorWithModel

`public static EOAdaptor adaptorWithModel(EOModel model)`

Creates and returns a new adaptor by extracting the adaptor name from _model_, invoking [adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu), and assigning _model_'s connection dictionary to the new adaptor. Throws an exception if _model_ is `null`__,__ if _model_'s adaptor name is `null`, or if the adaptor named in _model_ can't be loaded.

A subclass of EOAdaptor doesn't need to implement this method. A subclass that does implement this method must incorporate the superclass's version.

__See Also:__ adaptorName (EOModel), [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forbw63tomvrxi2lpnzcgsy3unfxw4ylspe)

---

### adaptorWithName

`public static synchronized EOAdaptor adaptorWithName(String name)`

Creates and returns a new adaptor, loading it from the framework named _name_ if necessary. For example, this code excerpt creates an adaptor from a framework named __AcmeEOAdaptor.framework__:

```
EOAdaptor myAdaptor = (EOAdaptor)EOAdaptor.adaptorWithName("Acme");
```

This method searches the application's main bundle, __~/Library/Frameworks__, __Network/Library/Frameworks__, and __System/Library/Frameworks__ for the first framework whose base filename (that is, the filename without the ".framework" extension) corresponds to _name_. Throws an exception if _name_ is `null` or if an adaptor class corresponding with _name_ can't be found.

Usually you'd use [adaptorWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue233emvwa) to create a new adaptor, but you can use this method when you don't have a model. In fact, this method is typically used when you're creating an adaptor for the purpose of creating a model from an existing database.

---

### defaultDelegate

`public static Object defaultDelegate()`

Returns the default delegate-the object that is assigned to new adaptor instances as their delegate.

---

### __expressionClassName__

`public static String expressionClassName(String className)`

Description forthcoming.

---

### setDefaultDelegate

`public static void setDefaultDelegate(Object anObject)`

Sets the default delegate-the object assigned as delegate to all newly created EOAdaptor instances. By default, there is no default delegate.

---

### setExpressionClassName

`public synchronized static void setExpressionClassName( String sqlExpressionClassName, String adaptorClassName)`

Sets the expression class for instances of the class named adaptorClassName to _sqlExpressionClassName_. If _sqlExpressionClassName_ is `null`, restores the expression class to the default. Throws an exception if _adaptorClassName_ is `null` or the empty string.

Use this method to substitute a subclass of EOSQLExpression for the expression class provided by the adaptor.

A subclass of EOAdaptor doesn't need to implement this method. A subclass that does implement this method must incorporate the superclass's version.

__See Also:__ [defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdfmzqxk3duiv4ha4tfonzws33oinwgc43t)

---

## Instance Methods

---

### administrativeConnectionDictionaryForAdaptor

`public NSDictionary administrativeConnectionDictionaryForAdaptor(EOAdaptor adaptor)`

This method, formerly provided by the EOLoginPanel class, returns the administrative connection dictionary for the specified adaptor.

---

### assertConnectionDictionaryIsValid

`public abstract void assertConnectionDictionaryIsValid()`

Implemented by subclasses to verify that the adaptor can connect to the database server with its connection dictionary. Briefly forms a connection to the server to validate the connection dictionary and then closes the connection. Throws an exception if the connection dictionary contains invalid information.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

__See Also:__ [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forbw63tomvrxi2lpnzcgsy3unfxw4ylspe)

---

### assignExternalInfoForAttribute

`public void assignExternalInfoForAttribute(EOAttribute attribute)`

Implemented by adaptor subclasses to assign database-specific characteristics to _attribute_. EOAdaptor's implementation invokes [assignExternalTypeForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwfi6lqmvdg64sbor2he2lcov2gk) to assign an external type, and then it assigns a column name based on the attribute name. For example, __assignExternalInfoForAttribute__ assigns the column name "FIRST_NAME" to an attribute named "firstName". The method makes no changes to _attribute_'s column name if _attribute_ is derived.

A subclass of EOAdaptor doesn't need to implement this method. A subclass that does implement this method must incorporate the superclass's version.

__See Also:__ [assignExternalInfoForEntireModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs4tfjvxwizlm)

---

### assignExternalInfoForEntireModel

`public void assignExternalInfoForEntireModel(EOModel model)`

Assigns database-specific characteristics to _model_. Used in EOModeler to switch a model's adaptor. This method examines each entity in _model_. If an entity's external name is not set and all of the entity's attribute's external names are not set, then this method uses [assignExternalInfoForEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs5dz) and [assignExternalInfoForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sbor2he2lcov2gk) to assign external names. If the entity's external name is set or if any of the entity's attributes' external names are set, then the method doesn't assign external names to the entity or any of its attributes. Regardless, this method assigns external types for all the model's attributes.

A subclass of EOAdaptor doesn't need to implement this method.

---

### assignExternalInfoForEntity

`public void assignExternalInfoForEntity(EOEntity entity)`

Implemented by adaptor subclasses to assign database-specific characteristics to _entity_. EOAdaptor's implementation assigns an external name to _entity_ based on _entity_'s name. For example, [assignExternalInfoForEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs5dz) assigns the external name "MOVIE" to an entity named "Movie".

An adaptor subclass should implement this method to assign additional database-specific characteristics, if any. A subclass that does implement this method must incorporate the superclass's version.

__See Also:__ [assignExternalInfoForEntireModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs4tfjvxwizlm)

---

### assignExternalTypeForAttribute

`public void assignExternalTypeForAttribute(EOAttribute attribute)`

Overridden by adaptor subclasses to assign the external type to _attribute_. EOAdaptor's implementation does nothing.

An adaptor subclass should implement this method to assign an external type using _attribute_'s internal type, precision, and length information. A subclass that does implement this method should incorporate the superclass's version.

__See Also:__ [assignExternalInfoForEntireModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonuwo3sfpb2gk4tomfwes3tgn5dg64sfnz2gs4tfjvxwizlm)

---

### canServiceModel

`public boolean canServiceModel(EOModel model)`

Returns `true` if the receiver can service _model_, `false` otherwise. EOAdaptor's implementation returns `true` if the receiver's connection dictionary is equal to _model_'s connection dictionary as determined by NSDictionary's __isEqual__ method.

A subclass of EOAdaptor doesn't need to override this method.

---

### connectionDictionary

`public NSDictionary connectionDictionary()`

Returns the receiver's connection dictionary, or `null` if the adaptor doesn't have one. The connection dictionary contains the values, such as user name and password, needed to connect to the database server. The dictionary's keys identify the information the server expects, and its values are the values that the adaptor will try when connecting. Each adaptor uses different keys; see your adaptor's documentation for keys it uses.

A subclass of EOAdaptor doesn't need to override this method.

---

### contexts

`public NSArray contexts()`

Returns the adaptor contexts created by the receiver, or `null` if no adaptor contexts have been created. A subclass of EOAdaptor doesn't need to override this method.

__See Also:__ [createAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3smvqxizkbmrqxa5dpojbw63tumv4hi)

---

### createAdaptorContext

`public abstract EOAdaptorContext createAdaptorContext()`

Implemented by subclasses to create and return a new EOAdaptorContext, or `null` if a new context can't be created. A newly created EOAdaptor has no contexts.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

__See Also:__ [contexts](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3pnz2gk6duom)

---

### createDatabaseWithAdministrativeConnectionDictionary

`public void createDatabaseWithAdministrativeConnectionDictionary( NSDictionary connectionDictionary)`

Uses the administrative login information to create the database (or user for Oracle) defined by _connectionDictionary_.

__See Also:__ [dropDatabaseWithAdministrativeConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdsn5yeiylumfrgc43fk5uxi2cbmrwws3tjon2heylunf3gkq3pnzxgky3unfxw4rdjmn2gs33omfzhs)

---

### defaultExpressionClass

`public abstract Class defaultExpressionClass()`

Implemented by subclasses to return the subclass of EOSQLExpression used as the default expression class for the adaptor. You wouldn't ordinarily invoke this method directly. It's invoked automatically to determine which class should be used to represent query language expressions.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

__See Also:__ [setExpressionClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5zwk5cfpbyhezltonuw63sdnrqxg42omfwwk)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate or `null` if a delegate has not been assigned. A subclass of EOAdaptor doesn't need to override this method.

---

### dropDatabaseWithAdministrativeConnectionDictionary

`public void dropDatabaseWithAdministrativeConnectionDictionary( NSDictionary connectionDictionary)`

Uses the administrative login information to drop the database (or user for Oracle) defined by the _connectionDictionary_.

__See Also:__ [createDatabaseWithAdministrativeConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3smvqxizkemf2gcytbonsvo2lunbawi3ljnzuxg5dsmf2gs5tfinxw43tfmn2gs33oiruwg5djn5xgc4tz)

---

### expressionClass

`public Class expressionClass()`

Returns the subclass of EOSQLExpression used by the receiver for query language expressions. Returns the expression class assigned using the class method [setExpressionClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5zwk5cfpbyhezltonuw63sdnrqxg42omfwwk). If no class has been set for the receiver's class, this method determines the expression class by sending [defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdfmzqxk3duiv4ha4tfonzws33oinwgc43t) to `this`.You rarely need to invoke this method yourself. It's invoked by the Framework to determine the class to use to represent query language expressions. You should, however, use this method if you explicitly create EOSQLExpression instances. To be sure you're using the correct expression class, create instances of the class returned from this method.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to __super__.

---

### expressionFactory

`public abstract EOSQLExpressionFactory expressionFactory()`

Supports changes made to EOSQLExpression and related classes and interfaces. Returns the EOExpressionFactory for the adaptor. For more information, see the section for EOSQLExpression.

---

### externalTypesWithModel

`public NSArray externalTypesWithModel(EOModel model)`

Implemented by subclasses to return the names of the database types (such as Sybase "varchar" or Oracle "NUMBER") for use with the adaptor. _model_ is an optional argument that can be used to supplement the adaptor's set of database types with additional, user-defined database types. See your adaptor's documentation for information on if and how it uses _model_.

An adaptor subclass should implement this method.

---

### fetchedValueForDataValue

`public NSData fetchedValueForDataValue( NSData value, EOAttribute attribute)`

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [fetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) when the value argument is an NSData.

EOAdaptor's implementation returns _value_ unchanged. An adaptor subclass should override this method if the adaptor's database performs transformations on binary types, such as BLOBs.

---

### fetchedValueForDateValue

`public NSTimestamp fetchedValueForDateValue( NSTimestamp value, EOAttribute attribute)`

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [fetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) when the value argument is a date.

EOAdaptor's implementation returns _value_ unchanged. An adaptor subclass should override this method to convert or format date values. For example, a concrete adaptor subclass could set _value_'s millisecond value to 0.

---

### fetchedValueForNumberValue

`public Number fetchedValueForNumberValue( Number value, EOAttribute attribute)`

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [fetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) when the value argument is a number.

EOAdaptor's implementation returns _value_ unchanged. An adaptor subclass should override this method to convert or format numeric values. For example, a concrete adaptor subclass should probably round _value_ according to the precision and scale _attribute_.

---

### fetchedValueForStringValue

`public String fetchedValueForStringValue( String value, EOAttribute attribute)`

Overridden by subclasses to return the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. This method is invoked from [fetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) when the value argument is a string.

EOAdaptor's implementation trims trailing spaces and returns `null` for zero-length strings. An adaptor subclass should override this method to perform any additional conversion or formatting on string values.

---

### fetchedValueForValue

`public Object fetchedValueForValue( Object value, EOAttribute attribute)`

Returns the value that the receiver's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute_. The Framework uses this method to keep enterprise object snapshots in sync with database values. For example, assume that a product's price is marked down 15%. If the product's original price is 5.25, the sale price is 5.25\*.85, or 4.4625. When the Framework updates the product's price, the database server truncates the price to 4.46 (assuming the scale of the database's price column is 2). Before performing the update, the Framework sends the adaptor a__fetchedValueForValue__ message with the value 4.4625. The adaptor performs the database-specific transformation and returns 4.46. The Framework assigns the truncated value to the product object and to the product object's snapshot and then proceeds with the update.

An adaptor subclass can override this method or one of the data type-specific __fetchedValue...__ methods. EOAdaptor's implementation of __fetchedValueForValue__ invokes one of the data type-specific methods depending on _value_'s class. If _value_ is not a string, number, date, or data object (that is, an instance of String, Number, NSGregorianDate, NSData, or any of their subclasses),__fetchedValueForValue__ returns _value_ unchanged.

This method invokes the [EOAdaptor](#apple-ivhuczdbob2g64q) method adaptorFetchedValueForValue which can override the adaptor's default behavior.

__See Also:__ [fetchedValueForDataValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxerdborqvmylmovsq), [fetchedValueForDateValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxerdborsvmylmovsq), [fetchedValueForNumberValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxettvnvrgk4swmfwhkzi), [fetchedValueForStringValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxeu3uojuw4z2wmfwhkzi), valueFactoryMethod (EOAttribute)

---

### handleDroppedConnection

`public void handleDroppedConnection()`

Invoked when necessary to clean up after a dropped connection. Sends handleDroppedConnection to all of its adaptor contexts and then clears its array of contexts. If the delegate implements reconnectionDictionaryForAdaptor, that method is invoked, and the return value is assigned to the adaptor as its new connection dictionary.

You should never invoke this method; it is invoked automatically by the Framework. Subclasses don't normally need to override the superclass implementation.

---

### hasOpenChannels

`public boolean hasOpenChannels()`

Returns `true` if any of the receiver's contexts have open channels, `false` otherwise. A subclass of EOAdaptor doesn't need to override this method.

__See Also:__ [hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbonhxazloinugc3tomvwhg) (EOAdaptorContext)

---

### internalTypeForExternalType

`public String internalTypeForExternalType( String extType, EOModel model)`

Implemented by subclasses to return the name of the class used to represent values stored in the database as _extType_. _model_ is an optional argument that can be used to supplement the adaptor's set of type mappings with additional mappings for user-defined database types. See your adaptor's documentation for information on if and how it uses _model_. Returns `null` if no mapping for _extType_ is found.

An adaptor subclass should implement this method without invoking EOAdaptor's implementation.

---

### isDatabaseConnectionException

`public boolean isDatabaseConnectionException(Exception exception)`

Returns `true` if the specified exception has been raised due to a database connection failure or `false` otherwise.

---

### isDroppedConnectionException

`public boolean isDroppedConnectionException(Exception anException)`

Returns `true` if the exception is one that the adaptor can attempt to recover from by reconnecting to the database, `false` otherwise.

Invoked if an exception is raised during fetching or saving. If the adaptor returns `true`, then the adaptor attempts to reconnect to the database and retries the operation. If the reconnection attempt fails, the exception from the failure is raised as usual. If the adaptor returns `false`, reconnection isn't attempted and the exception is raised.

The default implementation of __isDroppedConnectionException:__ returns `false`. Subclasses that support database reconnection should implement this method to allow for automatic database reconnection.

__See Also:__ [handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbnzsgyzkeojxxa4dfmrbw63tomvrxi2lpny), reconnectionDictionaryForAdaptor ( [EOAdaptor](#apple-ivhuczdbob2g64q))

---

### isValidQualifierType

`public abstract boolean isValidQualifierType( String typeName, EOModel model)`

Implemented by subclasses to return `true` if an attribute of type _typeName_ can be used in a qualifier (a SQL WHERE clause) sent to the database server, or `false` otherwise. _typeName_ is the name of a type as required by the database server, such as Sybase "varchar" or Oracle "NUMBER". _model_ is an optional argument that can be used to supplement the adaptor's set of type mappings with additional mappings for user-defined database types. See your adaptor's documentation for information on if and how it uses _model_.

An adaptor subclass must override this method without invoking EOAdaptor's implementation.

---

### name

`public String name()`

Returns the adaptor's name; this is usually the base filename of the framework from which the adaptor was loaded. For example, if an adaptor was loaded from a framework named __AcmeEOAdaptor.framework__, this method returns "Acme".

A subclass of EOAdaptor doesn't need to override this method.

__See Also:__ [adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu)

---

### prototypeAttributes

`public NSArray prototypeAttributes()`

Returns an array of prototype attributes specific to the adaptor class. Adaptor writers should note that this method looks for an EOModel named EOadaptorNamePrototypes in the resources directory of the adaptor.

---

### setConnectionDictionary

`public void setConnectionDictionary(NSDictionary dictionary)`

Sets the adaptor's connection dictionary to _dictionary_, which must only contain String, NSData, NSDictionary, and NSArray objects. Throws an exception if there are any open channels-you can't change connection information while the adaptor is connected.

A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to __super__.

__See Also:__ [connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3pnzxgky3unfxw4rdjmn2gs33omfzhs), [hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbonhxazloinugc3tomvwhg), [assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonsxe5cdn5xg4zldoruw63senfrxi2lpnzqxe6kjonlgc3djmq),

---

### setDelegate

`public void setDelegate(Object delegate)`

Sets the receiver's delegate to _delegate_, or removes its delegate if _delegate_ is `null`. A subclass of EOAdaptor doesn't need to override this method. A subclass that does override this method must incorporate the superclass's version through a message to __super__.

---

### synchronizationFactory

`public abstract EOSchemaGeneration synchronizationFactory()`

Supports changes made to EOSQLExpression and related classes and interfaces. Returns the EOSynchronizationFactory for the adaptor. For more information, see the section for EOSQLExpression.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
