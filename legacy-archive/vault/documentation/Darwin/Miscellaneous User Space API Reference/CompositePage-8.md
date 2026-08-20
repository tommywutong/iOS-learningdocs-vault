---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html
archived_at: '2026-07-15T07:23:26.017304Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| basic_string.h | basic_string.h | basic_string.h | basic_string.h | basic_string.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/atomicity.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/atomicity/index.html#//apple_ref/doc/header/atomicity.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<bits/atomicity.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/atomicity/index.html#//apple_ref/doc/header/atomicity.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<bits/atomicity.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/atomicity/index.html#//apple_ref/doc/header/atomicity.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Classes

**[basic_string](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/Classes/basic_string/index.html#//apple_ref/cpp/cl/basic_string_DONTLINK_0x2c2f01a4)**
:

---

## Functions

**[operator](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf6rcpjzkeyskojnpta6ddmu4taztdmm)**
:

**[operator !=](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html#//apple_ref/c/func/operator!a_DONTLINK_0x2c3e2960)**
:

**[operator !=(const _CharT \*, const basic_string _CharT _Traits _Alloc &)](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html#//apple_ref/c/func/operator!a_DONTLINK_0x2c3ce738)**
:

**[operator !=(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &)](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html#//apple_ref/c/func/operator!a_DONTLINK_0x2c3a2e90)**
:

**[operator ==](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html#//apple_ref/c/func/operatoraa_DONTLINK_0x2c395b2c)**
:

**[operator ==(const _CharT \*, const basic_string _CharT _Traits _Alloc &)](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html#//apple_ref/c/func/operatoraa_DONTLINK_0x18770a4c)**
:

**[operator ==(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &)](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/CompositePage.html#//apple_ref/c/func/operatoraa_DONTLINK_0x2c3667c8)**
:

**[operator basic_string(_CharT, const basic_string _CharT _Traits _Alloc &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zgeyltnfrv643uojuw4z27irhu4vcmjfhewxzqpazggmzthezgena)**
:

**[operator basic_string(const _CharT \*, const basic_string _CharT _Traits _Alloc &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zgeyltnfrv643uojuw4z27irhu4vcmjfhewxzqpazggmzshbsdkna)**
:

**[operator basic_string(const basic_string _CharT _Traits _Alloc &, const _CharT \*)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zgeyltnfrv643uojuw4z27irhu4vcmjfhewxzqpazggmzug4zgena)**
:

**[operator basic_string(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zgeyltnfrv643uojuw4z27irhu4vcmjfhewxzqpazggmzsg43dgyy)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator | operator | operator | operator | operator |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator<(
        const basic_string<_CharT, _Traits, _Alloc>& __lhs,
        const basic_string<_CharT, _Traits, _Alloc>& __rhs)
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Second string.

##### Return Value

True if @a lhs precedes @a rhs. False otherwise.

##### Discussion

@brief Test if string precedes string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator != | operator != | operator != | operator != | operator != |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator!=(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    const _CharT*__rhs)
```

##### Parameters

**`lhs`**
: String.

**`rhs`**
: C string.

##### Return Value

True if @a lhs.compare(@a rhs) != 0. False otherwise.

##### Discussion

@brief Test difference of string and C string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator !=(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator !=(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator !=(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator !=(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator !=(const _CharT \*, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator!=(
    const _CharT*__lhs,
    const basic_string<_CharT, _Traits, _Alloc>& __rhs)
```

##### Parameters

**`lhs`**
: C string.

**`rhs`**
: String.

##### Return Value

True if @a rhs.compare(@a lhs) != 0. False otherwise.

##### Discussion

@brief Test difference of C string and string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator !=(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator !=(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator !=(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator !=(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator !=(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator!=(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    const basic_string<_CharT, _Traits, _Alloc>& __rhs)
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Second string.

##### Return Value

True if @a lhs.compare(@a rhs) != 0. False otherwise.

##### Discussion

@brief Test difference of two strings.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator == | operator == | operator == | operator == | operator == |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator==(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    const _CharT*__rhs)
```

##### Parameters

**`lhs`**
: String.

**`rhs`**
: C string.

##### Return Value

True if @a lhs.compare(@a rhs) == 0. False otherwise.

##### Discussion

@brief Test equivalence of string and C string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator ==(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator ==(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator ==(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator ==(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator ==(const _CharT \*, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator==(
    const _CharT*__lhs,
    const basic_string<_CharT, _Traits, _Alloc>& __rhs)
```

##### Parameters

**`lhs`**
: C string.

**`rhs`**
: String.

##### Return Value

True if @a rhs.compare(@a lhs) == 0. False otherwise.

##### Discussion

@brief Test equivalence of C string and string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator ==(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator ==(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator ==(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator ==(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator ==(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline bool operator==(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    const basic_string<_CharT, _Traits, _Alloc>& __rhs)
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Second string.

##### Return Value

True if @a lhs.compare(@a rhs) == 0. False otherwise.

##### Discussion

@brief Test equivalence of two strings.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator basic_string(_CharT, const basic_string _CharT _Traits _Alloc &) | operator basic_string(_CharT, const basic_string _CharT _Traits _Alloc &) | operator basic_string(_CharT, const basic_string _CharT _Traits _Alloc &) | operator basic_string(_CharT, const basic_string _CharT _Traits _Alloc &) | operator basic_string(_CharT, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> basic_string<_CharT,_Traits,_Alloc> operator+(
    _CharT __lhs,
    const basic_string<_CharT,_Traits,_Alloc>& __rhs);
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Last string.

##### Return Value

New string with @a lhs followed by @a rhs.

##### Discussion

@brief Concatenate character and string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator basic_string(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const _CharT \*, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const _CharT \*, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> basic_string<_CharT,_Traits,_Alloc> operator+(
    const _CharT*__lhs,
    const basic_string<_CharT,_Traits,_Alloc>& __rhs);
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Last string.

##### Return Value

New string with value of @a lhs followed by @a rhs.

##### Discussion

@brief Concatenate C string and string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator basic_string(const basic_string _CharT _Traits _Alloc &, const _CharT \*) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const _CharT \*) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const _CharT \*) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const _CharT \*) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const _CharT \*) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline basic_string<_CharT, _Traits, _Alloc> operator+(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    const _CharT*__rhs)
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Last string.

##### Return Value

New string with @a lhs followed by @a rhs.

##### Discussion

@brief Concatenate string and C string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator basic_string(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) | operator basic_string(const basic_string _CharT _Traits _Alloc &, const basic_string _CharT _Traits _Alloc &) |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> basic_string<_CharT, _Traits, _Alloc> operator+(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    const basic_string<_CharT, _Traits, _Alloc>& __rhs)
```

##### Parameters

**`lhs`**
: First string.

**`rhs`**
: Last string.

##### Return Value

New string with value of @a lhs followed by @a rhs.

##### Discussion

@brief Concatenate two strings.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| basic_string | basic_string | basic_string | basic_string | basic_string |

---

```
template<typename _CharT, typename _Traits, typename _Alloc> inline basic_string<_CharT, _Traits, _Alloc> operator+(
    const basic_string<_CharT, _Traits, _Alloc>& __lhs,
    _CharT __rhs)
```

##### Discussion

@brief Concatenate string and character.

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2006-06-20
