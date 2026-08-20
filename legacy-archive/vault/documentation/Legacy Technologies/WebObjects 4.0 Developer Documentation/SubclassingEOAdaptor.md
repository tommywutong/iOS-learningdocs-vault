---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/SubclassingEOAdaptor.html
archived_at: '2026-07-18T01:28:14.068616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptor.md)
[!](EOAdaptorChannel.md)

---

---

## Creating an EOAdaptor Subclass

Enterprise Objects Framework provides concrete adaptors for three standard relational database management systems-Informix, Oracle, and Sybase-as well as a concrete adaptor for ODBC-compliant databases. You may want to create a subclass of one of these adaptors to extend its behavior, or you may want to create a concrete EOAdaptor subclass for a different database or persistent storage system. EOAdaptor provides many default method implementations that are sufficient for concrete subclasses:

- [assignExternalInfoForEntireModel](EOAdaptor.md#apple-gq3dgna)
- [connectionDictionary](EOAdaptor.md#apple-gqydqnq)
- [contexts](EOAdaptor.md#apple-gqydooi)
- [databaseEncoding](EOAdaptor.md#apple-ha2tg)
- [delegate](EOAdaptor.md#apple-gqydimy)
- [hasOpenChannels](EOAdaptor.md#apple-ha4tk)
- [name](EOAdaptor.md#apple-gm4tooa)

The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- [adaptorWithModel](EOAdaptor.md#apple-gq2tmmi)
- [adaptorWithName](EOAdaptor.md#apple-g44di)
- [setExpressionClassNameForAdaptorClassName](EOAdaptor.md#apple-gq3tema)
- [setConnectionDictionary](EOAdaptor.md#apple-hezdg)
- [setDelegate](EOAdaptor.md#apple-hezdq)

If you override `setConnectionDictionary` or `setDelegate`, your implementations should incorporate the superclass's implementation through a message to `super`.

The remaining EOAdaptor methods must be overridden by concrete adaptor subclasses in terms of the persistent storage system with which it interacts:

- [assignExternalInfoForAttribute](EOAdaptor.md#apple-g44tc)
- [assignExternalInfoForEntity](EOAdaptor.md#apple-gq3dona)
- [externalTypesWithModel](EOAdaptor.md#apple-gq3tcmy)
- [internalTypeForExternalTypeInModel](EOAdaptor.md#apple-gqytcnq)
- [assertConnectionDictionaryIsValid](EOAdaptor.md#apple-gq4dcmq)
- [createAdaptorContext](EOAdaptor.md#apple-gqydmoa)
- [fetchedValueForDataValue](EOAdaptor.md#apple-gq4tmma)
- [fetchedValueForDateValue](EOAdaptor.md#apple-ha3to)
- [fetchedValueForNumberValue](EOAdaptor.md#apple-ha4dc)
- [fetchedValueForStringValue](EOAdaptor.md#apple-ha4dk)
- [fetchedValueForValue](EOAdaptor.md#apple-ha4ds)
- [isValidQualifierTypeInModel](EOAdaptor.md#apple-gm4tqni)

  ****

---

[!](EOAdaptor.md)
[!](EOAdaptorChannel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
