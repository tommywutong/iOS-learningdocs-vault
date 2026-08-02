---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOQualifierEvaluation.html
archived_at: '2026-07-15T08:11:39.006017Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOQualifierEvaluation

> __Implemented by:__ : [EOAndQualifier](EOAndQualifier.md#apple-ifxgiulvmfwgsztjmvza)
> : [EOKeyComparisonQualifier](EOKeyComparisonQualifier.md#apple-jnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvza)
> : [EOKeyValueQualifier](EOKeyValueQualifier.md#apple-jnsxsvtbnr2wkulvmfwgsztjmvza)
> : [EONotQualifier](EONotQualifier.md#apple-ivhu433ukf2wc3djmzuwk4q)
> : [EOOrQualifier](EOOrQualifier.md#apple-ivhu64srovqwy2lgnfsxe)
> :

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOQualifierEvaluation interface defines a method, [evaluateWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi),
that performs in-memory evaluation of qualifiers. All qualifier
classes whose objects can be evaluated in memory must implement
this interface.

## Instance Methods

---

### evaluateWithObject

`public boolean evaluateWithObject(Object object)`

Returns true if the argument _object_ satisfies
the qualifier, false otherwise. This method can throw one of several
possible exceptions if an error occurs, depending on the implementation.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
