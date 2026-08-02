---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOAdaptor.html
archived_at: '2026-07-15T08:11:33.320840Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAdaptor

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOAdaptor.h

---

## Class Description

---

EOAdaptor is an abstract class that provides concrete subclasses
with a structure for connecting to a database. A concrete subclass
of EOAdaptor provides database-specific method implementations and represents
a single database server. You never interact with instances of the
EOAdaptor class, but you use its class methods, [adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi) and [adaptorWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a),
to create instances of a concrete subclass. The EOAdaptor class
defines the methods that find and load the concrete adaptors from bundles.
However, you rarely interact with a concrete adaptor either. Generally,
adaptors are automatically created and used by other classes in
the Enterprise Objects Framework.

The EOAdaptor class has the following principal attributes:

- Dictionary of connection information
- Login panel
- Array of adaptor contexts
- Expression class

Other framework classes create EOAdaptor objects. [adaptorWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a) creates
a new adaptor with the adaptor name in the specified model. [adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi) creates
a new adaptor with the specified name.

The following table lists the most commonly-used methods in
the EOAdaptor class:

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [- assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le) | Verifies that the adaptor can connect with its connection information. |
| [- runLoginPanel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm) | Runs the login panel without affecting the connection dictionary. |
| [- runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe) | Runs the login panel until the user enters valid connection information or cancels the panel. |
| [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi) | Sets the connection dictionary. |

For information on subclassing an EOAdaptor, see ["Creating an EOAdaptor Subclass"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EOAdaptor.html#BCECDHDG).

## Constants

---

EOAccess defines one constant in EOAdaptor.h,
an NSString, as described below:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOGeneralAdaptorException | The name of exceptions raised by adaptors when errors occur during interactions with their database servers. |

## Method Types

---

> **Creating an EOAdaptor**
> : [+ adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi)
> : [+ adaptorWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a)
> : [- initWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixws3tjorlws5dijzqw2zj2)
>
> **Accessing an adaptor's
> name**
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixw4ylnmu)
>
> **Accessing the names of
> all available adaptors**
> : [+ availableAdaptorNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmf3gc2lmmfrgyzkbmrqxa5dpojhgc3lfom)
>
> **Connecting to a database
> server**
> : [- assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le)
> : [- connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg33onzswg5djn5xei2ldoruw63tboj4q)
> : [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi)
> : [- runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe)
> : [- runLoginPanel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm)
> : [- isDroppedConnectionException:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixws42eojxxa4dfmrbw63tomvrxi2lpnzcxqy3fob2gs33ohi)
> : [- handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqylomrwgkrdsn5yhazleinxw43tfmn2gs33o)
>
> **Encoding database strings**
> : [- databaseEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwiylumfrgc43fivxgg33enfxgo)
>
> **Performing database-specific
> transformations on values**
> : [- fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu)
> : [- fetchedValueForDataValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zeiylumflgc3dvmu5gc5duojuwe5lumu5a)
> : [- fetchedValueForDateValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zeiylumvlgc3dvmu5gc5duojuwe5lumu5a)
> : [- fetchedValueForNumberValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5ze45lnmjsxevtbnr2wkotbor2he2lcov2gkoq)
> : [- fetchedValueForStringValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfg5dsnfxgovtbnr2wkotbor2he2lcov2gkoq)
>
> **Servicing models**
> : [- canServiceModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwgyloknsxe5tjmnsu233emvwdu)
> : [+ internalTypeForExternalType:model:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpnfxhizlsnzqwyvdzobsum33siv4hizlsnzqwyvdzobstu3lpmrswyoq)
> : [+ externalTypesWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmv4hizlsnzqwyvdzobsxgv3jorue233emvwdu)
> : [+ assignExternalInfoForEntireModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djojsu233emvwdu)
> : [+ assignExternalInfoForEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djor4tu)
> : [+ assignExternalInfoForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojaxi5dsnfrhk5dfhi)
> : [- isValidQualifierType:model:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixws42wmfwgszcrovqwy2lgnfsxevdzobstu3lpmrswyoq)
>
> **Creating adaptor contexts**
> : [- createAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg4tfmf2gkqlemfyhi33sinxw45dfpb2a)
> : [- contexts](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg33oorsxq5dt)
>
> **Checking connection status**
> : [- hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqyltj5ygk3sdnbqw43tfnrzq)
>
> **Accessing a default expression
> class**
> : [+ setExpressionClassName:adaptorClassName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponsxirlyobzgk43tnfxw4q3mmfzxgttbnvstuylemfyhi33sinwgc43tjzqw2zj2)
> : [- expressionClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwk6dqojsxg43jn5xeg3dbonzq)
> : [- defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwizlgmf2wy5cfpbyhezltonuw63sdnrqxg4y)
>
> **Accessing an adaptor's
> login panel**
> : [+ sharedLoginPanelInstance](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponugc4tfmrgg6z3jnzigc3tfnrew443umfxggzi)
> : [- runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe)
> : [- runLoginPanel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm)
>
> **Accessing the delegate**
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwizlmmvtwc5df)
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluirswyzlhmf2gkoq)
> : [- setDefaultDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponsxirdfmzqxk3duirswyzlhmf2gkoq)
> : [- defaultDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmrswmylvnr2eizlmmvtwc5df)
>
> **Creating and dropping
> databases**
> : [- createDatabaseWithAdministrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg4tfmf2gkrdborqweyltmvlws5diifsg22lonfzxi4tboruxmzkdn5xg4zldoruw63senfrxi2lpnzqxe6j2)
> : [- dropDatabaseWithAdministrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwi4tpobcgc5dbmjqxgzkxnf2gqqlenvuw42ltorzgc5djozsug33onzswg5djn5xei2ldoruw63tboj4tu)
>
> **Providing prototype attributes**
> : [- prototypeAttributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxa4tporxxi6lqmvaxi5dsnfrhk5dfom)
>
> **Synchronizing the database
> with a model**
> : [- objectStoreChangesFromAttribute:toAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixw6ytkmvrxiu3un5zgkq3imfxgozltizzg63kbor2he2lcov2gkotun5axi5dsnfrhk5dfhi)

## Class Methods

---

### adaptorWithModel:

`+(id)adaptorWithModel:(EOModel
*)model`

Creates and returns a new adaptor by extracting
the adaptor name from _model_, invoking [adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi),
and assigning _model_'s connection
dictionary to the new adaptor. Raises an `NSInvalidArgumentException` if _model_ is nil__,__ if _model_'s
adaptor name is nil, or if the adaptor named in _model_ can't
be loaded.

A subclass of EOAdaptor doesn't need to override this
method. A subclass that does override this method must incorporate
the superclass's version.

__See Also:__  [- adaptorName](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgc4dun5ze4ylnmu) ( [EOModel](EOModel-3.md#apple-ineeoq2iizduk)), [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi)

---

### adaptorWithName:

`+ (id)adaptorWithName:(NSString
*)name`

Creates and returns a new adaptor, loading it
from the framework named _name_ if
necessary and sending it an [initWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixws3tjorlws5dijzqw2zj2) message. For example,
this code excerpt creates an adaptor from a framework named __AcmeEOAdaptor.framework__:
> ```
> EOAdaptor *myAdaptor = [EOAdaptor adaptorWithName:@"Acme"];
> ```

This
method searches the application's main bundle, __~/Library/Frameworks__, __Network/Library/Frameworks__,
and __System/Library/Frameworks__ for the first
framework whose base filename (that is, the filename without the
".framework" extension) corresponds to _name_. However,
note that dynamic loading isn't available on PDO platforms. Consequently,
you must statically link your adaptor into applications for PDO:
In this case, [adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi) simply
looks in the runtime for an adaptor class corresponding with the
specified name. Raises an `NSInvalidArgumentException` if _name_ is nil or
if an adaptor class corresponding with _name_ can't
be found.

Usually you'd use [adaptorWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a) to
create a new adaptor, but you can use this method when you don't
have a model. In fact, this method is typically used when you're
creating an adaptor for the purpose of creating a model from an
existing database.

---

### assignExternalInfoForAttribute:

`+ (void)assignExternalInfoForAttribute:(EOAttribute
*)attribute`

Overridden by adaptor subclasses to assign
database-specific characteristics to _attribute_.
EOAdaptor's implementation invokes [assignExternalTypeForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cupfygkrtpojaxi5dsnfrhk5dfhi) to
assign an external type, and then it assigns a column name based
on the attribute name. For example, __assignExternalInfoForAttribute:__ assigns
the column name "FIRST_NAME" to an attribute named "firstName".
The method makes no changes to _attribute_'s
column name if _attribute_ is derived.

A
subclass of EOAdaptor doesn't need to override this method. A
subclass that does override this method must incorporate the superclass's
version.

__See Also:__  [+ assignExternalInfoForEntireModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djojsu233emvwdu)

---

### assignExternalInfoForEntireModel:

`+ (void)assignExternalInfoForEntireModel:(EOModel
*)model`

Assigns database-specific characteristics to _model_.
Used in EOModeler to switch a model's adaptor. This method examines
each entity in _model_. If an entity's
external name is not set and all of the entity's attribute's
external names are not set, then this method uses [assignExternalInfoForEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djor4tu) and [assignExternalInfoForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojaxi5dsnfrhk5dfhi) to
assign external names. If the entity's external name is set or
if any of the entity's attributes' external names are set, then
the method doesn't assign external names to the entity or any
of its attributes. Regardless, this method assigns external types
for all the model's attributes.

A subclass of EOAdaptor doesn't
need to override this method.

---

### assignExternalInfoForEntity:

`+ (void)assignExternalInfoForEntity:(EOEntity
*)entity`

Overridden by adaptor subclasses to assign database-specific
characteristics to _entity_. EOAdaptor's implementation
assigns an external name to _entity_ based
on _entity_'s name. For example, [assignExternalInfoForEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djor4tu) assigns
the external name "MOVIE" to an entity named "Movie".

An
adaptor subclass should override this method to assign additional
database-specific characteristics, if any. A subclass that does override this
method must incorporate the superclass's version.

__See
Also:__  [+ assignExternalInfoForEntireModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djojsu233emvwdu)

---

### assignExternalTypeForAttribute:

`+ (void)assignExternalTypeForAttribute:(EOAttribute
*)attribute`

Overridden by adaptor subclasses to assign the
external type to _attribute_. EOAdaptor's implementation
does nothing.

An adaptor subclass should override this method
to assign an external type using _attribute_'s
internal type, precision, and length information. A subclass that
does override this method should incorporate the superclass's
version.

__See Also:__  [+ assignExternalInfoForEntireModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djojsu233emvwdu)

---

### availableAdaptorNames

`+ (NSArray *)availableAdaptorNames`

Returns an array containing the names of all
available adaptors, as found by searching the paths returned by
NSStandardLibraryPaths(). If no adaptors are found, this method
returns an empty array.

---

### defaultDelegate

`+ (id)defaultDelegate`

Returns the default delegate-the object that
is assigned to new adaptor instances as their delegate.

---

### externalTypesWithModel:

`+ (NSArray *)externalTypesWithModel:(EOModel
*)model`

Implemented by subclasses to return the names
of the database types (such as Sybase "varchar" or Oracle "NUMBER")
for use with the adaptor. _model_ is
an optional argument that can be used to supplement the adaptor's
set of database types with additional, user-defined database types.
See your adaptor's documentation for information on if and how
it uses _model_.

An adaptor subclass
should implement this method.

---

### internalTypeForExternalType:model:

`+ (NSString *)internalTypeForExternalType:(NSString
*)extType
model:(EOModel *)model`

Implemented by subclasses to return the name
of the class used to represent values stored in the database as _extType_. _model_ is
an optional argument that can be used to supplement the adaptor's
set of type mappings with additional mappings for user-defined database
types. See your adaptor's documentation for information on if
and how it uses _model_. Returns nil if
no mapping for _extType_ is found.

An
adaptor subclass should override this method without invoking EOAdaptor's
implementation.

---

### setDefaultDelegate:

`+ (void)setDefaultDelegate:(id)defaultDelegate`

Sets the default delegate-the object assigned
as delegate to all newly created EOAdaptor instances. By default,
there is no default delegate.

---

### setExpressionClassName:adaptorClassName:

`+ (void)setExpressionClassName:(NSString
*)sqlExpressionClassName
adaptorClassName:(NSString *)adaptorClassName`

Sets the expression class for instances of the
class named adaptorClassName to _sqlExpressionClassName_.
If _sqlExpressionClassName_ is nil,
restores the expression class to the default. Raises an `NSInvalidArgumentException` if _adaptorClassName_ is nil or
the empty string.

Use this method to substitute a subclass
of EOSQLExpression for the expression class provided by the adaptor. For
example, the default expression class for the Oracle adaptor is
OracleSQLExpression. The following statement substitutes the class
named MySQLExpression:

> ```
> [EOAdaptor setExpressionClassName:@"MySQLExpression" adaptorClassName:@"OracleAdaptor"];
> ```

A
subclass of EOAdaptor doesn't need to override this method. A
subclass that does override this method must incorporate the superclass's
version.

__See Also:__  [- defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwizlgmf2wy5cfpbyhezltonuw63sdnrqxg4y)

---

### sharedLoginPanelInstance

`+ (EOLoginPanel *)sharedLoginPanelInstance`

Returns the receiver's login panel in applications
that have a graphical user interface. Returns nil if the application
doesn't have an NSApplication object. Otherwise, looks for the
bundle named "LoginPanel" in the resources for the adaptor framework,
loads the bundle, and returns an instance of the bundle's principal
class (see the NSBundle class specification for information on loading
bundles). The returned object is used to implement [runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe) and [runLoginPanel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm).

A
subclass of EOAdaptor doesn't need to override this method. A
subclass that does override this method must incorporate the superclass's
version through a message to __super__.

---

## Instance Methods

---

### assertConnectionDictionaryIsValid

`- (void)assertConnectionDictionaryIsValid`

Implemented by subclasses to verify that the
adaptor can connect to the database server with its connection dictionary.
Briefly forms a connection to the server to validate the connection
dictionary and then closes the connection. Raises an EOGeneralAdaptorException if
the connection dictionary contains invalid information.

An
adaptor subclass must override this method without invoking EOAdaptor's
implementation.

__See Also:__  [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi), [- runLoginPanel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm), [- runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe)

---

### canServiceModel:

`- (BOOL)canServiceModel:(EOModel
*)model`

Returns YES if the receiver can service _model_, NO otherwise.
EOAdaptor's implementation returns YES if the receiver's connection
dictionary is equal to _model_'s
connection dictionary as determined by NSDictionary's __isEqual:__ method.

A
subclass of EOAdaptor doesn't need to override this method.

---

### connectionDictionary

`- (NSDictionary *)connectionDictionary`

Returns the receiver's connection dictionary,
or nil if the adaptor doesn't have one. The connection dictionary
contains the values, such as user name and password, needed to connect
to the database server. The dictionary's keys identify the information
the server expects, and its values are the values that the adaptor
will try when connecting. Each adaptor uses different keys; see
your adaptor's documentation for keys it uses.

A subclass
of EOAdaptor doesn't need to override this method.

---

### contexts

`- (NSArray *)contexts`

Returns the adaptor contexts created by the
receiver, or nil if no adaptor contexts have been created. A subclass
of EOAdaptor doesn't need to override this method.

__See
Also:__  [- createAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg4tfmf2gkqlemfyhi33sinxw45dfpb2a)

---

### createAdaptorContext

`- (EOAdaptorContext *)createAdaptorContext`

Implemented by subclasses to create and return
a new EOAdaptorContext, or nil if a new context can't be created. The
new context retains the receiver. A newly created EOAdaptor has
no contexts.

An adaptor subclass must override this method
without invoking EOAdaptor's implementation.

__See
Also:__  [- contexts](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg33oorsxq5dt), [- initWithAdaptor:](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3jnzuxiv3jorueczdbob2g64r2) ( [EOAdaptorContext](EOAdaptorContext-3.md#apple-ivhuczdbob2g64sdn5xhizlyoq))

---

### createDatabaseWithAdministrativeConnectionDictionary:

`- (void)createDatabaseWithAdministrativeConnectionDictionary:(NSDictionary
*)connectionDictionary`

Uses the administrative login information to
create the database (or user for Oracle) defined by _connectionDictionary_.

__See
Also:__  [- dropDatabaseWithAdministrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwi4tpobcgc5dbmjqxgzkxnf2gqqlenvuw42ltorzgc5djozsug33onzswg5djn5xei2ldoruw63tboj4tu), [EOLoginPanel](EOLoginPanel-2.md#apple-ijaucqsbjbbui)

---

### databaseEncoding

`- (NSStringEncoding)databaseEncoding`

Returns the string encoding used to encode and
decode database strings. A database system stores strings in a particular
character set. The Framework needs to know what character set the
database system uses so it can encode and decode strings coming
from and going to the database server. The string encoding returned
from this method specifies the character set the Framework uses.

An
adaptor's database encoding is stored in the connection dictionary
with the key "databaseEncoding". If the connection dictionary
doesn't have an entry for the database encoding, the default C
string encoding is used. This method raises an `NSInvalidArgumentException` if
the receiver's database encoding isn't valid.

A
subclass of EOAdaptor doesn't need to override this method.

__See
Also:__  - __availableStringEncodings__ (NSString),
- __defaultCStringEncoding__ (NSString)

---

### defaultExpressionClass

`- (Class)defaultExpressionClass`

Implemented by subclasses to return the subclass
of EOSQLExpression used as the default expression class for the
adaptor. You wouldn't ordinarily invoke this method directly.
It's invoked automatically to determine which class should be
used to represent query language expressions.

An adaptor subclass
must override this method without invoking EOAdaptor's implementation.

__See
Also:__  [+ setExpressionClassName:adaptorClassName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponsxirlyobzgk43tnfxw4q3mmfzxgttbnvstuylemfyhi33sinwgc43tjzqw2zj2)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate or nil if
a delegate has not been assigned. A subclass of EOAdaptor doesn't
need to override this method.

---

### dropDatabaseWithAdministrativeConnectionDictionary:

`- (void)dropDatabaseWithAdministrativeConnectionDictionary:(NSDictionary
*)connectionDictionary`

Uses the administrative login information to
drop the database (or user for Oracle) defined by the _connectionDictionary_.

__See
Also:__  [- createDatabaseWithAdministrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg4tfmf2gkrdborqweyltmvlws5diifsg22lonfzxi4tboruxmzkdn5xg4zldoruw63senfrxi2lpnzqxe6j2),
EOLoginPanel class

---

### expressionClass

`- (Class)expressionClass`

Returns the subclass of EOSQLExpression used
by the receiver for query language expressions. Returns the expression
class assigned using the class method [+ setExpressionClassName:adaptorClassName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponsxirlyobzgk43tnfxw4q3mmfzxgttbnvstuylemfyhi33sinwgc43tjzqw2zj2).
If no class has been set for the receiver's class, this method
determines the expression class by sending [defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwizlgmf2wy5cfpbyhezltonuw63sdnrqxg4y) to __self__.You
rarely need to invoke this method yourself. It's invoked by the
Framework to determine the class to use to represent query language
expressions. You should, however, use this method if you explicitly create
EOSQLExpression instances. To be sure you're using the correct
expression class, create instances of the class returned from this
method.

A subclass of EOAdaptor doesn't need to override
this method. A subclass that does override this method must incorporate
the superclass's version through a message to __super__.

---

### fetchedValueForDataValue:attribute:

`- (NSData *)fetchedValueForDataValue:(NSData
*)value
attribute:(EOAttribute *)attribute`

Overridden by subclasses to return the value
that the receiver's database server would ultimately store for _value_ if
it was inserted or updated in the column described by _attribute_.
This method is invoked from [fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) when
the value argument is an NSData.

EOAdaptor's implementation
returns _value_ unchanged. An adaptor
subclass should override this method if the adaptor's database
performs transformations on binary types, such as BLOBs.

---

### fetchedValueForDateValue:attribute:

`- (NSCalendarDate *)fetchedValueForDateValue:(NSCalendarDate
*)value
attribute:(EOAttribute *)attribute`

Overridden by subclasses to return the value
that the receiver's database server would ultimately store for _value_ if
it was inserted or updated in the column described by _attribute_.
This method is invoked from [fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) when
the value argument is a date.

EOAdaptor's implementation
returns _value_ unchanged. An adaptor
subclass should override this method to convert or format date values.
For example, a concrete adaptor subclass could set _value_'s millisecond
value to 0.

---

### fetchedValueForNumberValue:attribute:

`- (NSNumber *)fetchedValueForNumberValue:(NSNumber
*)value
attribute:(EOAttribute *)attribute`

Overridden by subclasses to return the value
that the receiver's database server would ultimately store for _value_ if
it was inserted or updated in the column described by _attribute_.
This method is invoked from [fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) when
the value argument is a number.

EOAdaptor's implementation
returns _value_ unchanged. An adaptor
subclass should override this method to convert or format numeric
values. For example, a concrete adaptor subclass should probably round _value_ according
to the precision and scale _attribute_.

---

### fetchedValueForStringValue:attribute:

`- (NSString*)fetchedValueForStringValue:(NSString
*)value
attribute:(EOAttribute *)attribute`

Overridden by subclasses to return the value
that the receiver's database server would ultimately store for _value_ if
it was inserted or updated in the column described by _attribute_.
This method is invoked from [fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) when
the value argument is a string.

EOAdaptor's implementation
trims trailing spaces and returns nil for zero-length strings. An
adaptor subclass should override this method to perform any additional
conversion or formatting on string values.

---

### fetchedValueForValue:attribute:

`- (id)fetchedValueForValue:(id)value
attribute:(EOAttribute *)attribute`

Returns the value that the receiver's database
server would ultimately store for _value_ if
it was inserted or updated in the column described by _attribute_.
The Framework uses this method to keep enterprise object snapshots
in sync with database values. For example, assume that a product's
price is marked down 15%. If the product's original price is 5.25,
the sale price is 5.25\*.85, or 4.4625. When the Framework updates
the product's price, the database server truncates the price to
4.46 (assuming the scale of the database's price column is 2).
Before performing the update, the Framework sends the adaptor a__fetchedValueForValue:attribute:__ message
with the value 4.4625. The adaptor performs the database-specific
transformation and returns 4.46. The Framework assigns the truncated
value to the product object and to the product object's snapshot
and then proceeds with the update.

An adaptor subclass can
override this method or one of the data type-specific __fetchedValue...__ methods.
EOAdaptor's implementation of __fetchedValueForValue:attribute:__ invokes
one of the data type-specific methods depending on _value_'s
class. If _value_ is not a string,
number, date, or data object (that is, an instance of NSString,
NSNumber, NSDate, NSData, or any of their subclasses),__fetchedValueForValue:attribute:__ returns _value_ unchanged.

This
method invokes the [EOAdaptor Delegate](EOAdaptor%20Delegate.md#apple-ivhuczdbob2g64q)delegate method [adaptor:fetchedValueForValue:attribute:](EOAdaptor%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpoiqeizlmmvtwc5dff5qwiylqorxxeotgmv2gg2dfmrlgc3dvmvdg64swmfwhkzj2mf2hi4tjmj2xizj2) which
can override the adaptor's default behavior.

__See
Also:__  [- fetchedValueForDataValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zeiylumflgc3dvmu5gc5duojuwe5lumu5a), [- fetchedValueForDateValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zeiylumvlgc3dvmu5gc5duojuwe5lumu5a), [- fetchedValueForNumberValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5ze45lnmjsxevtbnr2wkotbor2he2lcov2gkoq), [- fetchedValueForStringValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfg5dsnfxgovtbnr2wkotbor2he2lcov2gkoq), [- valueFactoryMethod](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3wmfwhkzkgmfrxi33spfgwk5din5sa) (EOAttribute)

---

### handleDroppedConnection

`- (void)handleDroppedConnection`

Invoked when necessary to clean up after a dropped
connection. Sends [handleDroppedConnection](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfxgi3dfirzg64dqmvseg33onzswg5djn5xa) to all of
its adaptor contexts and then clears its array of contexts. If the
delegate implements [reconnectionDictionaryForAdaptor:](EOAdaptor%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpoiqeizlmmvtwc5dff5zgky3pnzxgky3unfxw4rdjmn2gs33omfzhsrtpojawiylqorxxeoq),
that method is invoked, and the return value is assigned to the adaptor
as its new connection dictionary.

You should never invoke this
method; it is invoked automatically by the Framework. Subclasses
don't normally need to override the superclass implementation.

---

### hasOpenChannels

`- (BOOL)hasOpenChannels`

Returns YES if any of the receiver's contexts
have open channels, NO otherwise. A subclass of EOAdaptor doesn't
need to override this method.

__See Also:__  [- hasOpenChannels](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzbwqylonzswy4y) ( [EOAdaptorContext](EOAdaptorContext-3.md#apple-ivhuczdbob2g64sdn5xhizlyoq))

---

### initWithName:

`- (id)initWithName:(NSString
*)name`

The designated initializer for the EOAdaptor
class, this method is overridden by adaptor subclasses to initialize
a newly allocated EOAdaptor subclass with _name_. _name_ is
usually derived from the base filename (that is, the filename without
the ".framework" extension) of the framework from which the adaptor
is loaded. For example, an adaptor named "Acme" is loaded from
the framework __AcmeEOAdaptor.framework__.
Returns __self__.

Never invoke this method
directly. It is invoked automatically from [adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi) and [adaptorWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a)-EOAdaptor
class methods you use to create a new adaptor.

A subclass
of EOAdaptor doesn't need to override this method, but may override
it to perform additional initialization. A subclass that does override
this method must incorporate the superclass's version through
a message to __super__.

---

### isDroppedConnectionException:

`- (BOOL)isDroppedConnectionException:(NSException
*)exception`

Returns `YES` if
the exception is one that the adaptor can attempt to recover from
by reconnecting to the database, `NO` otherwise.

Invoked
if an exception is raised during fetching or saving. If the adaptor
returns `YES`, then the
adaptor attempts to reconnect to the database and retries the operation.
If the reconnection attempt fails, the exception from the failure
is raised as usual. If the adaptor returns `NO`,
reconnection isn't attempted and the exception is raised.

The
default implementation of __isDroppedConnectionException:__ returns `NO`.
Subclasses that support database reconnection should implement this
method to allow for automatic database reconnection.

__See
Also:__  [- handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqylomrwgkrdsn5yhazleinxw43tfmn2gs33o), [- reconnectionDictionaryForAdaptor:](EOAdaptor%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpoiqeizlmmvtwc5dff5zgky3pnzxgky3unfxw4rdjmn2gs33omfzhsrtpojawiylqorxxeoq) ( [EOAdaptor Delegate](EOAdaptor%20Delegate.md#apple-ivhuczdbob2g64q))

---

### isValidQualifierType:model:

`- (BOOL)isValidQualifierType:(NSString
*)typeName
model:(EOModel *)model`

Implemented by subclasses to return YES if an
attribute of type _typeName_ can be
used in a qualifier (a SQL WHERE clause) sent to the database server,
or NO otherwise. _typeName_ is the
name of a type as required by the database server, such as Sybase
"varchar" or Oracle "NUMBER". _model_ is
an optional argument that can be used to supplement the adaptor's
set of type mappings with additional mappings for user-defined database
types. See your adaptor's documentation for information on if
and how it uses _model_.

An adaptor
subclass must override this method without invoking EOAdaptor's
implementation.

---

### name

`- (NSString *)name`

Returns the adaptor's name; this is usually
the base filename of the framework from which the adaptor was loaded.
For example, if an adaptor was loaded from a framework named __AcmeEOAdaptor.framework__, this
method returns "Acme".

A subclass of EOAdaptor doesn't
need to override this method.

__See Also:__  [+ adaptorWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbhgc3lfhi), [- initWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixws3tjorlws5dijzqw2zj2)

---

### __objectStoreChangesFromAttribute:toAttribute:__

`- (NSDictionary *)objectStoreChangesFromAttribute:(EOAttribute
*)schemaAttribute
toAttribute:(EOAttribute *)modelAttribute`

Returns a dictionary describing the changes
to synchronize _schemaAttribute_ (the
attribute reflecting the definition of a column in the database)
with _modelAttribute_ (the attribute
as it's defined in the model).

---

### prototypeAttributes

`- (NSArray *)prototypeAttributes`

Returns an array of prototype attributes specific
to the adaptor class. Adaptor writers should note that this method
looks for an EOModel named EOadaptorNamePrototypes
in the resources directory of the adaptor.

---

### runLoginPanel

`- (NSDictionary *)runLoginPanel`

Runs the adaptor's login panel by sending
a [runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe)message to
the adaptor's login panel object with the validate flag NO. Returns
connection information entered in the panel without affecting the
adaptor's connection dictionary. The connection dictionary returned isn't
validated by this method.

A subclass of EOAdaptor doesn't
need to override this method. A subclass that does override this method
must incorporate the superclass's version through a message to __super__.

__See
Also:__  [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi), [- assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le), [+ sharedLoginPanelInstance](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponugc4tfmrgg6z3jnzigc3tfnrew443umfxggzi)

---

### runLoginPanelAndValidateConnectionDictionary

`- (BOOL)runLoginPanelAndValidateConnectionDictionary`

Runs the adaptor's login panel by sending
a [runPanelForAdaptor:validate:allowsCreation:](EOLoginPanel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2mn5tws3sqmfxgk3bpoj2w4udbnzswyrtpojawiylqorxxeotwmfwgszdborstuylmnrxxo42dojswc5djn5xdu)message
to the adaptor's login panel object with the validate flag YES.
Returns YES if the user enters valid connection information, or NO if
the user cancels the panel.

A subclass of EOAdaptor doesn't
need to override this method. A subclass that does override this method
must incorporate the superclass's version through a message to __super__.

__See
Also:__  [- runLoginPanel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm), [- setConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi), [- assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le), [+ sharedLoginPanelInstance](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rponugc4tfmrgg6z3jnzigc3tfnrew443umfxggzi)

---

### setConnectionDictionary:

`- (void)setConnectionDictionary:(NSDictionary
*)dictionary`

Sets the adaptor's connection dictionary to _dictionary_,
which must only contain NSString, NSData, NSDictionary, and NSArray
objects. Raises an NSInvalidArgumentException if there are any open channels-you
can't change connection information while the adaptor is connected.

A
subclass of EOAdaptor doesn't need to override this method. A
subclass that does override this method must incorporate the superclass's
version through a message to __super__.

__See
Also:__  [- connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg33onzswg5djn5xei2ldoruw63tboj4q), [- hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqyltj5ygk3sdnbqw43tfnrzq), [- assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le), [- runLoginPanelAndValidateConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe), [- runPanelForAdaptor:validate:allowsCreation:](EOLoginPanel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2mn5tws3sqmfxgk3bpoj2w4udbnzswyrtpojawiylqorxxeotwmfwgszdborstuylmnrxxo42dojswc5djn5xdu) (EOLoginPanel)

---

### setDelegate:

`- (void)setDelegate:(id)delegate`

Sets the receiver's delegate to _delegate_,
or removes its delegate if _delegate_ is nil. The
receiver does not retain delegate. A subclass of EOAdaptor doesn't
need to override this method. A subclass that does override this
method must incorporate the superclass's version through a message
to __super__.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
