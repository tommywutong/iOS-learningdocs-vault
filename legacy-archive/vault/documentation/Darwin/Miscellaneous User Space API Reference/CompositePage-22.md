---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/char_traits/CompositePage.html
archived_at: '2026-07-15T07:23:26.201391Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| char_traits.h | char_traits.h | char_traits.h | char_traits.h | char_traits.h |

|  |  |
| --- | --- |
| __Includes:__ | <cstring>  [<bits/stl_algobase.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_algobase/index.html#//apple_ref/doc/header/stl_algobase.h)  [<bits/postypes.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/postypes/index.html#//apple_ref/doc/header/postypes.h)  <cstring>  [<bits/fpos.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/fpos/index.html#//apple_ref/doc/header/fpos.h)  <cstring>  [<bits/stl_algobase.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_algobase/index.html#//apple_ref/doc/header/stl_algobase.h)  [<bits/postypes.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/postypes/index.html#//apple_ref/doc/header/postypes.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Char_types | _Char_types | _Char_types | _Char_types | _Char_types |

---

```
template <class _CharT> struct _Char_types {
    typedef unsigned long int_type;
    typedef std::streampos pos_type;
    typedef std::streamoff off_type;
    typedef std::mbstate_t state_type;
};
```

##### Discussion

@brief Mapping from character type to associated types.

@note This is an implementation class for the generic version
of char_traits. It defines int_type, off_type, pos_type, and
state_type. By default these are unsigned long, streamoff,
streampos, and mbstate_t. Users who need a different set of
types, but who don't need to change the definitions of any function
defined in char_traits, can specialize __gnu_cxx::_Char_types
\* while leaving __gnu_cxx::char_traits alone.

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
