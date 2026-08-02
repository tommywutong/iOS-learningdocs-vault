---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOQualifierEvaluation.html
archived_at: '2026-07-15T08:11:43.546793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOQualifierEvaluation

> __Adopted by:__
> [EOAndQualifier](EOAndQualifier-2.md#apple-ifxgiulvmfwgsztjmvza)
> [EOKeyComparisonQualifier](EOKeyComparisonQualifier-2.md#apple-jnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvza)
> [EOKeyValueQualifier](EOKeyValueQualifier-2.md#apple-jnsxsvtbnr2wkulvmfwgsztjmvza)
> [EONotQualifier](EONotQualifier-2.md#apple-ivhu433ukf2wc3djmzuwk4q)
> [EOOrQualifier](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOOrQualifier.html#EOOrQualifier)

> __Declared in:__ : EOControl/EOQualifier.h

---

## Protocol Description

---

The EOQualifierEvaluation protocol defines a method, [evaluateWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du),
that performs in-memory evaluation of qualifiers. All qualifier
classes whose objects can be evaluated in memory must implement
this protocol.

## Instance Methods

---

### evaluateWithObject:

`- (BOOL)evaluateWithObject:object`

Returns YES if the argument _object_ satisfies
the qualifier, NO otherwise. This method can raise one of several
possible exceptions if an error occurs, depending on the implementation.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
