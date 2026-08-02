---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_list/CompositePage.html
archived_at: '2026-07-15T07:23:28.430944Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_list.h | stl_list.h | stl_list.h | stl_list.h | stl_list.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  <debug/support.h>  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[operator _List_const_iterator](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf6x2mnfzxix3dn5xhg5c7nf2gk4tborxxex2ej5hfitcjjzfv6mdygjtdgnddmzrwg)**
:

**[operator _List_iterator](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf6x2mnfzxix3jorsxeylun5zf6rcpjzkeyskojnpta6bsmyzteztcmi2a)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator _List_const_iterator | operator _List_const_iterator | operator _List_const_iterator | operator _List_const_iterator | operator _List_const_iterator |

---

```
template<typename _Tp> struct _List_const_iterator {
    typedef _List_const_iterator<_Tp> _Self;
    typedef const _List_node<_Tp> _Node;
    typedef _List_iterator<_Tp> iterator;
    typedef ptrdiff_t difference_type;
    typedef bidirectional_iterator_tag iterator_category;
    typedef _Tp value_type;
    typedef const _Tp*pointer;
    typedef const _Tp& reference;
    _List_const_iterator() : _M_node() {
        }  _List_const_iterator(
        const _List_node_base* __x) : _M_node(__x) {
        }  _List_const_iterator(
        const iterator& __x) : _M_node(__x._M_node) {
        }  // Must downcast from List_node_base to _List_node to get to
    // _M_data.
    reference operator*() const ;
```

##### Discussion

@brief A list::const_iterator.

@if maint
All the functions are op overloads.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator _List_iterator | operator _List_iterator | operator _List_iterator | operator _List_iterator | operator _List_iterator |

---

```
template<typename _Tp> struct _List_iterator {
    typedef _List_iterator<_Tp> _Self;
    typedef _List_node<_Tp> _Node;
    typedef ptrdiff_t difference_type;
    typedef bidirectional_iterator_tag iterator_category;
    typedef _Tp value_type;
    typedef _Tp*pointer;
    typedef _Tp& reference;
    _List_iterator() : _M_node() {
        }  _List_iterator(
        _List_node_base* __x) : _M_node(__x) {
        }  // Must downcast from List_node_base to _List_node to get to _M_data.
    reference operator*() const ;
```

##### Discussion

@brief A list::iterator.

@if maint
All the functions are op overloads.
@endif

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
