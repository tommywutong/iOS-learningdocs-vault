---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOValidation.html
archived_at: '2026-07-18T01:28:33.536746Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOSortOrdering.Comparison.md)
[!](EOValidation-2.md)

---

# EOValidation

__Implemented By:__
EOEnterpriseObject
EOCustomObject
EOGenericRecord

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

__Inherits From:__
java.lang.Object

__Package:__
com.apple.client.eocontrol

## Interface Description

The EOValidation interface defines the way that enterprise objects validate their values. The validation methods check for illegal value types, values outside of established limits, illegal relationships, and so on. EOCustomObject and EOGenericRecord provide default implementations of EOValidation, which are described in detail in this specification.

There are two kinds of validation methods. The first validates individual properties, and the second validates an entire object to see if it's ready for a specific operation (inserting, updating, and deleting). The two different types are discussed in more detail in the sections "[Validating Individual Properties](EOValidation-2.md)" and "[Validating Before an Operation](EOValidation-2.md)."

## Instance Methods

---

#### validateForDelete

public abstract void __validateForDelete__ () throws EOValidation.Exception

Confirms that the receiver can be deleted in its current state, throwing an EOValidation.Exception if it can't. For example, an object can't be deleted if it has a relationship with a delete rule of EOClassDescription.[DeleteRuleDeny](EOClassDescription.md) and that relationship has a destination object.

EOCustomObject's implementation sends the receiver's EOClassDescription a message (which performs basic checking based on the presence or absence of values). Subclasses should invoke __super__ 's implementation before performing their own validation, and should combine any exception thrown by __super__ 's implementation with their own.

__See also:__ [- __propagateDeleteWithEditingContext__](EOEnterpriseObject.md)(EOEnterpriseObject),
"Constructors" (EOValidationException)

---

#### validateForInsert

public abstract void __validateForInsert__ () throws EOValidation.Exception

Confirms that the receiver can be inserted in its current state, throwing an EOValidation.Exception if it can't. EOCustomObject's implementation simply invokes __validateForSave__ .

The method __validateForSave__ is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to insertion, it should go in __validateForSave__ .

---

#### validateForSave

public abstract void __validateForSave__ ()

Confirms that the receiver can be saved in its current state, throwing an EOValidation.Exception if it can't. EOCustomObject's implementation sends the receiver's EOClassDescription a [__validateObjectForSave__](EOClassDescription.md)message, then iterates through all of the receiver's properties, invoking __validateValueForKey__ for each one. If this results in more than one exception, the exception returned contains the additional ones in its __userInfo__ dictionary under the EOValidation.Exception.AdditionalExceptions key. Subclasses should invoke __super__ 's implementation before performing their own validation, and should combine any exception thrown by __super__ 's implementation with their own.

Enterprise objects can implement this method to check that certain relations between properties hold; for example, that the end date of a vacation period follows the begin date. To validate an individual property, you can simply implement a method for it as described under __validateValueForKey__ .

__See also:__
"Constructors" (EOValidationException)

---

#### validateForUpdate

public abstract void __validateForUpdate__ () throws EOValidation.Exception

Confirms that the receiver can be inserted in its current state, throwing an EOValidation.Exception if it can't. EOCustomObject's implementation simply invokes __validateForSave__ .

The method __validateForSave__ is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to updating, it should go in __validateForSave__ .

---

#### validateValueForKey

public abstract java.lang.Object __validateValueForKey__ (
java.lang.Object _value_,
java.lang.String _key_) throws EOValidation.Exception

Confirms that _value_ is legal for the receiver's property named by _key_. Throws an EOValidation.Exception if it can't confirm that the value is legal. The implementation can provide a coerced value by returning the value. This lets you convert strings to dates or numbers or maybe convert strings to an enumerated type value. EOCustomObject's implementation sends a [__validateValueForKey__](EOClassDescription.md)message to the receiver's EOClassDescription.

Enterprise objects can implement individual __validate__ _Key_ methods to check limits, test for nonsense values, and otherwise confirm individual properties. To validate multiple properties based on relations among them, override the appropriate __validateFor...__ method.

"Constructors" (EOValidationException)

---

[!](EOSortOrdering.Comparison.md)
[!](EOValidation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
