---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/SubclassingEOAdaptor.html
archived_at: '2026-07-18T01:28:23.439365Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAdaptor-2.md)
[!](EOAdaptorChannel-2.md)

---

---

## Creating an EOAdaptor Subclass

Enterprise Objects Framework provides concrete adaptors for three standard relational database management systems-Informix, Oracle, and Sybase-as well as a concrete adaptor for ODBC-compliant databases. You may want to create a subclass of one of these adaptors to extend its behavior, or you may want to create a concrete EOAdaptor subclass for a different database or persistent storage system. EOAdaptor provides many default method implementations that are sufficient for concrete subclasses:

- [+ assignExternalInfoForEntireModel:](EOAdaptor-2.md#apple-gq3dgna)
- [- connectionDictionary](EOAdaptor-2.md#apple-gqydqnq)
- [- contexts](EOAdaptor-2.md#apple-gqydooi)
- [- databaseEncoding](EOAdaptor-2.md#apple-ha2tg)
- [- delegate](EOAdaptor-2.md#apple-gqydimy)
- [- hasOpenChannels](EOAdaptor-2.md#apple-ha4tk)
- [- name](EOAdaptor-2.md#apple-gm4tooa)

The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- [+ adaptorWithModel:](EOAdaptor-2.md#apple-gq2tmmi)
- [+ adaptorWithName:](EOAdaptor-2.md#apple-g44di)
- [+ setExpressionClassName:adaptorClassName:](EOAdaptor-2.md#apple-gq3tema)
- [+ sharedLoginPanelInstance](EOAdaptor-2.md#apple-he4tmny)
- [- initWithName:](EOAdaptor-2.md#apple-he3dqmi)
- [- expressionClass](EOAdaptor-2.md#apple-he2dcna)
- [- runLoginPanel](EOAdaptor-2.md#apple-he3tsny)
- [- runLoginPanelAndValidateConnectionDictionary](EOAdaptor-2.md#apple-he4dcny)
- [- setConnectionDictionary:](EOAdaptor-2.md#apple-hezdg)
- [- setDelegate:](EOAdaptor-2.md#apple-hezdq)

If you override any of the above methods, your implementations should incorporate the superclass's implementation through a message to `super`.

The remaining EOAdaptor methods must be overridden by concrete adaptor subclasses in terms of the persistent storage system with which it interacts:

- [+ assignExternalInfoForAttribute:](EOAdaptor-2.md#apple-g44tc)
- [+ assignExternalInfoForEntity:](EOAdaptor-2.md#apple-gq3dona)
- [+ externalTypesWithModel:](EOAdaptor-2.md#apple-gq3tcmy)
- [+ internalTypeForExternalType:model:](EOAdaptor-2.md#apple-gqytcnq)
- [- assertConnectionDictionaryIsValid](EOAdaptor-2.md#apple-gq4dcmq)
- [- createAdaptorContext](EOAdaptor-2.md#apple-gqydmoa)
- [- defaultExpressionClass](EOAdaptor-2.md#apple-heztkoa)
- [- fetchedValueForDataValue:attribute:](EOAdaptor-2.md#apple-gq4tmma)
- [- fetchedValueForDateValue:attribute:](EOAdaptor-2.md#apple-ha3to)
- [- fetchedValueForNumberValue:attribute:](EOAdaptor-2.md#apple-ha4dc)
- [- fetchedValueForStringValue:attribute:](EOAdaptor-2.md#apple-ha4dk)
- [- fetchedValueForValue:attribute:](EOAdaptor-2.md#apple-ha4ds)
- [- isValidQualifierTypeIn:model:](EOAdaptor-2.md#apple-gm4tqni)

  ****

---

[!](EOAdaptor-2.md)
[!](EOAdaptorChannel-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
