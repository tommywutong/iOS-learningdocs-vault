---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOQualifierComparison.html
archived_at: '2026-07-15T08:11:38.989594Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOQualifier.Comparison

> **__Package:__**
> : com.apple.client.eocontrol

---

## Interface Description

---

The EOQualifierComparison interface defines
methods for comparing values. These methods are used for evaluating
qualifiers in memory.

|  |
| --- |
| __Note:__  This interface doesn't exist in the Yellow Box package, com.apple.yellow.eocontrol |

In Java Client, support for these methods is provided for
String, Number, and Date using [EOQualifier.ComparisonSupport](EOQualifier.ComparisonSupport.md#apple-ivhuwzlzkzqwy5lfinxwi2lom4xfg5lqobxxe5a).
You should implement this interface for any value classes you write that
you want to be evaluated in memory by EOQualifier instances.

## Method Types

---

> **Testing value objects**
> : [doesContain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5sg6zltinxw45dbnfxa)
> : [isEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgrlrovqwyvdp)
> : [isGreaterThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgr3smvqxizlskrugc3q)
> : [isGreaterThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgr3smvqxizlskrugc3q)
> : [isLessThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgtdfonzvi2dbny)
> : [isLessThanOrEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgtdfonzvi2dbnzhxerlrovqwyvdp)
> : [isLike](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgtdjnnsq)
> : [isCaseInsensitiveLike](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgq3bonsus3ttmvxhg2lunf3gktdjnnsq)
> : [isNotEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33of5uxgttporcxc5lbnrkg6)

## Instance Methods

---

### doesContain

`public abstract boolean doesContain(Object anObject)`

Returns `true` if
the receiver contains _anObject,_ `false` if
it doesn't.

---

### isCaseInsensitiveLike

`public abstract boolean isCaseInsensitiveLike(Object anObject)`

Returns `true` if
the receiver is a case-insensitive match for _anObject,_ `false` if
it isn't. See ["Using Wildcards and the like Operator" on page 299](EOQualifier-2.md#apple-ijbesqsjijaue) for the wildcard characters allowed.

---

### isEqualTo

`public abstract boolean isEqualTo(Object anObject)`

Returns `true` if
the receiver is equal to _anObject,_ `false` if
it isn't.

---

### isGreaterThan

`public abstract boolean isGreaterThan(Object anObject)`

Returns `true` if
the receiver is greater than _anObject,_ `false` if
it isn't.

---

### isGreaterThanOrEqualTo

`public abstract boolean isGreaterThanOrEqualTo(Object anObject)`

Returns `true` if
the receiver is greater than or equal to _anObject,_ `false` if
it isn't.

---

### isLessThan

`public abstract boolean isLessThan(Object anObject)`

Returns `true` if
the receiver is less than _anObject,_ `false` if
it isn't.

---

### isLessThanOrEqualTo

`public abstract boolean isLessThanOrEqualTo(Object anObject)`

Returns `true` if
the receiver is less than or equal to _anObject,_ `false` if
it isn't.

---

### isLike

`public abstract boolean isLike(Object anObject)`

Returns `true` if
the receiver matches _aString_ according
to the semantics of the SQL `like` comparison operator, `false` if
it doesn't. See ["Using Wildcards and the like Operator" on page 299](EOQualifier-2.md#apple-ijbesqsjijaue) for the wildcard characters allowed.

---

### isNotEqualTo

`public abstract boolean isNotEqualTo(Object anObject)`

Returns `true` if
the receiver is not equal to _anObject,_ `false` if
it is.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
