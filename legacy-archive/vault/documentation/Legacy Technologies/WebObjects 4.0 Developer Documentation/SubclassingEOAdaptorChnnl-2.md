---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/SubclassingEOAdaptorChnnl.html
archived_at: '2026-07-18T01:28:23.502376Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAdaptorChannel-2.md)
[!](EOAdaptorContext-3.md)

---

---

## Creating an EOAdaptorChannel Subclass

EOAdaptorChannel provides many default method implementations that are sufficient for concrete subclasses:

- [- adaptorContext](EOAdaptorChannel-2.md#apple-gq3dqni)
- [- delegate](EOAdaptorChannel-2.md#apple-he3tm)
- [- deleteRowDescribedByQualifier:entity:](EOAdaptorChannel-2.md#apple-guzdmna)
- [- isDebugEnabled](EOAdaptorChannel-2.md#apple-geydgoa)
- [- lockRowComparingAttributes:entity:qualifier:snapshot:](EOAdaptorChannel-2.md#apple-geydkni)
- [- performAdaptorOperation:](EOAdaptorChannel-2.md#apple-geydmnq)
- [- performAdaptorOperations:](EOAdaptorChannel-2.md#apple-geydomi)
- [- updateValues:inRowDescribedByQualifier:entity:](EOAdaptorChannel-2.md#apple-geytcmi)

The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- [- dictionaryWithObjects:forAttributes:zone:](EOAdaptorChannel-2.md#apple-ge2dioby)
- [- initWithAdaptorContext:](EOAdaptorChannel-2.md#apple-ge2dknzs)
- [- setDebugEnabled:](EOAdaptorChannel-2.md#apple-geytamq)
- [- setDelegate:](EOAdaptorChannel-2.md#apple-geytany)

If you override any of the above methods, your implementations should incorporate the superclass's implementation through a message to `super`.

The remaining EOAdaptorChannel methods must be overridden by concrete subclasses in terms of the persistent storage system with which it interacts:

- [- attributesToFetch](EOAdaptorChannel-2.md#apple-gq3dmmq)
- [- cancelFetch](EOAdaptorChannel-2.md#apple-he3do)
- [- closeChannel](EOAdaptorChannel-2.md#apple-guzdemq)
- [- deleteRowsDescribedByQualifier:entity:](EOAdaptorChannel-2.md#apple-guzdsna)
- [- describeModelWithTableNames:](EOAdaptorChannel-2.md#apple-guztcnq)
- [- describeResults](EOAdaptorChannel-2.md#apple-he4tk)
- [- describeStoredProcedureNames](EOAdaptorChannel-2.md#apple-he4ts)
- [- describeTableNames](EOAdaptorChannel-2.md#apple-geydamq)
- [- evaluateExpression:](EOAdaptorChannel-2.md#apple-geydaoi)
- [- executeStoredProcedure:withValues:](EOAdaptorChannel-2.md#apple-gyztona)
- [- fetchRowWithZone:](EOAdaptorChannel-2.md#apple-gyztsni)
- [- insertRow:forEntity:](EOAdaptorChannel-2.md#apple-geydgmi)
- [- isFetchInProgress](EOAdaptorChannel-2.md#apple-geydimq)
- [- isOpen](EOAdaptorChannel-2.md#apple-geydkmi)
- [- openChannel](EOAdaptorChannel-2.md#apple-geydmmq)
- [- primaryKeyForNewRowWithEntity:](EOAdaptorChannel-2.md#apple-geydqna)
- [- returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel-2.md#apple-geydqnq)
- [- selectAttributes:fetchSpecification:lock:entity:](EOAdaptorChannel-2.md#apple-geydsma)
- [- setAttributesToFetch:](EOAdaptorChannel-2.md#apple-geydsny)
- [- updateValues:inRowsDescribedByQualifier:entity:](EOAdaptorChannel-2.md#apple-gy3dgny)

  ****

---

[!](EOAdaptorChannel-2.md)
[!](EOAdaptorContext-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
