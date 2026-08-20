---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/SubclassingEOAdaptorChnnl.html
archived_at: '2026-07-18T01:28:14.126320Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptorChannel.md)
[!](EOAdaptorContext.md)

---

---

## Creating an EOAdaptorChannel Subclass

EOAdaptorChannel provides many default method implementations that are sufficient for concrete subclasses:

- [adaptorContext](EOAdaptorChannel.md#apple-gq3dqni)
- [delegate](EOAdaptorChannel.md#apple-he3tm)
- [deleteRowDescribedByQualifier](EOAdaptorChannel.md#apple-guzdmna)
- [isDebugEnabled](EOAdaptorChannel.md#apple-geydgoa)
- [lockRowComparingAttributes](EOAdaptorChannel.md#apple-geydkni)
- [performAdaptorOperation](EOAdaptorChannel.md#apple-geydmnq)
- [performAdaptorOperations](EOAdaptorChannel.md#apple-geydomi)
- [updateValues:inRowDescribedByQualifier](EOAdaptorChannel.md#apple-geytcmi)

The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- [setDebugEnabled](EOAdaptorChannel.md#apple-geytamq)
- [setDelegate](EOAdaptorChannel.md#apple-geytany)

If you override any of the above methods, your implementations should incorporate the superclass's implementation through a message to `super`.

The remaining EOAdaptorChannel methods must be overridden by concrete subclasses in terms of the persistent storage system with which it interacts:

- [attributesToFetch](EOAdaptorChannel.md#apple-gq3dmmq)
- [cancelFetch](EOAdaptorChannel.md#apple-he3do)
- [closeChannel](EOAdaptorChannel.md#apple-guzdemq)
- [deleteRowsDescribedByQualifier](EOAdaptorChannel.md#apple-guzdsna)
- [describeModelWithTableNames](EOAdaptorChannel.md#apple-guztcnq)
- [describeResults](EOAdaptorChannel.md#apple-he4tk)
- [describeStoredProcedureNames](EOAdaptorChannel.md#apple-he4ts)
- [describeTableNames](EOAdaptorChannel.md#apple-geydamq)
- [evaluateExpression](EOAdaptorChannel.md#apple-geydaoi)
- [executeStoredProcedure](EOAdaptorChannel.md#apple-gyztona)
- [fetchRow](EOAdaptorChannel.md#apple-gyztsni)
- [insertRow](EOAdaptorChannel.md#apple-geydgmi)
- [isFetchInProgress](EOAdaptorChannel.md#apple-geydimq)
- [isOpen](EOAdaptorChannel.md#apple-geydkmi)
- [openChannel](EOAdaptorChannel.md#apple-geydmmq)
- [primaryKeyForNewRowWithEntity](EOAdaptorChannel.md#apple-geydqna)
- [returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel.md#apple-geydqnq)
- [selectAttributes:fetchSpecification](EOAdaptorChannel.md#apple-geydsma)
- [setAttributesToFetch](EOAdaptorChannel.md#apple-geydsny)
- [updateValues:inRowsDescribedByQualifier](EOAdaptorChannel.md#apple-gy3dgny)

  ****

---

[!](EOAdaptorChannel.md)
[!](EOAdaptorContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
