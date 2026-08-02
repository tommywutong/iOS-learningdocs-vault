---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_algo/CompositePage.html
archived_at: '2026-07-15T07:23:27.967557Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_algo.h | stl_algo.h | stl_algo.h | stl_algo.h | stl_algo.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/stl_heap.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_heap/index.html#//apple_ref/doc/header/stl_heap.h)  [<bits/stl_tempbuf.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_tempbuf/index.html#//apple_ref/doc/header/stl_tempbuf.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<bits/stl_heap.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_heap/index.html#//apple_ref/doc/header/stl_heap.h)  [<bits/stl_tempbuf.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_tempbuf/index.html#//apple_ref/doc/header/stl_tempbuf.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<bits/stl_heap.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_heap/index.html#//apple_ref/doc/header/stl_heap.h)  [<bits/stl_tempbuf.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_tempbuf/index.html#//apple_ref/doc/header/stl_tempbuf.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[__final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5tgs3tbnrpws3ttmvzhi2lpnzpxg33sorpuit2okrgestsll4yhqmtfgnsgmylfgq)**
:

**[__final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5tgs3tbnrpws3ttmvzhi2lpnzpxg33sorpuit2okrgestsll4yhqmtfgnstiojvgq)**
:

**[__gcd](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5twgzc7irhu4vcmjfhewxzqpazgkmzqgu2giyy)**
:

**[__inplace_stable_partition](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw44dmmfrwkx3torqwe3dfl5ygc4tunf2gs33ol5ce6tsujreu4s27gb4dezjtg43dizbq)**
:

**[__inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw44dmmfrwkx3torqwe3dfl5zw64tul5ce6tsujreu4s27gb4dezjumftgeold)**
:

**[__inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw44dmmfrwkx3torqwe3dfl5zw64tul5ce6tsujreu4s27gb4dezjumizdqzju)**
:

**[__insertion_sort(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw443foj2gs33ol5zw64tul5ce6tsujreu4s27gb4dezjtmmzdcmjy)**
:

**[__insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw443foj2gs33ol5zw64tul5ce6tsujreu4s27gb4dezjtmm3giold)**
:

**[__introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw45dsn5zw64tul5wg633ql5ce6tsujreu4s27gb4dezjugzrggmzq)**
:

**[__introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uw45dsn5zw64tul5wg633ql5ce6tsujreu4s27gb4dezjugm4tsytd)**
:

**[__lg](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wgox2ej5hfitcjjzfv6mdygjstgzrqme2ti)**
:

**[__median(const _Tp &, const _Tp &, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwkzdjmfxf6rcpjzkeyskojnpta6bsmuytintehaya)**
:

**[__median(const _Tp &, const _Tp &, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwkzdjmfxf6rcpjzkeyskojnpta6bsmuytkmbsgeya)**
:

**[__merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwk4thmvpwczdbob2gs5tfl5ce6tsujreu4s27gb4dezjumzrtimdd)**
:

**[__merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwk4thmvpwczdbob2gs5tfl5ce6tsujreu4s27gb4dezjvgfrdqold)**
:

**[__merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwk4thmvpweyldnn3wc4tel5ce6tsujreu4s27gb4dezjvgeygkyzu)**
:

**[__merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwk4thmvpweyldnn3wc4tel5ce6tsujreu4s27gb4dezjumu4gcmzu)**
:

**[__merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwk4thmvpxo2lunbxxk5c7mj2wmztfojpuit2okrgestsll4yhqmtfgrrtoyztga)**
:

**[__merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5wwk4thmvpxo2lunbxxk5c7mj2wmztfojpuit2okrgestsll4yhqmtfgq4tgnlgha)**
:

**[__partition(_BidirectionalIterator, _BidirectionalIterator, _Predicate, bidirectional_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5ygc4tunf2gs33ol5ce6tsujreu4s27gb4dezjtgvswemju)**
:

**[__partition(_ForwardIterator, _ForwardIterator, _Predicate, forward_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5ygc4tunf2gs33ol5ce6tsujreu4s27gb4dezjtgvrtgmju)**
:

**[__reverse(_BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zgk5tfojzwkx2ej5hfitcjjzfv6mdygjstezdbmvsti)**
:

**[__reverse(_RandomAccessIterator, _RandomAccessIterator, random_access_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zgk5tfojzwkx2ej5hfitcjjzfv6mdygjstezrrmi3dq)**
:

**[__rotate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zg65dborsv6rcpjzkeyskojnpta6bsmuztemrumm2a)**
:

**[__rotate(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zg65dborsv6rcpjzkeyskojnpta6bsmuztcoddgm2a)**
:

**[__rotate(_ForwardIterator, _ForwardIterator, _ForwardIterator, forward_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zg65dborsv6rcpjzkeyskojnpta6bsmuztazjyhfrq)**
:

**[__rotate_adaptive](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zg65dborsv6ylemfyhi2lwmvpuit2okrgestsll4yhqmtfgrtggnbwga)**
:

**[__stable_partition_adaptive](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5zxiylcnrsv64dboj2gs5djn5xf6ylemfyhi2lwmvpuit2okrgestsll4yhqmtfgm4diobxga)**
:

**[__unguarded_linear_insert(_RandomAccessIterator, _Tp)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w4z3vmfzgizlel5wgs3tfmfzf62loonsxe5c7irhu4vcmjfhewxzqpazgkm3cgftgina)**
:

**[__unguarded_linear_insert(_RandomAccessIterator, _Tp, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w4z3vmfzgizlel5wgs3tfmfzf62loonsxe5c7irhu4vcmjfhewxzqpazgkm3che2dkoa)**
:

**[__unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w4z3vmfzgizlel5ygc4tunf2gs33ol5ce6tsujreu4s27gb4dezjtmezteold)**
:

**[__unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w4z3vmfzgizlel5ygc4tunf2gs33ol5ce6tsujreu4s27gb4dezjtme2gmyju)**
:

**[__unique_copy(_InputIterator, _InputIterator, _ForwardIterator, forward_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w42lrovsv6y3pob4v6rcpjzkeyskojnpta6bsmuzdsndcmjrq)**
:

**[__unique_copy(_InputIterator, _InputIterator, _ForwardIterator, _BinaryPredicate, forward_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w42lrovsv6y3pob4v6rcpjzkeyskojnpta6bsmuzgczjuhe2a)**
:

**[__unique_copy(_InputIterator, _InputIterator, _OutputIterator, output_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w42lrovsv6y3pob4v6rcpjzkeyskojnpta6bsmuzdqyjzgmya)**
:

**[__unique_copy(_InputIterator, _InputIterator, _OutputIterator, _BinaryPredicate, output_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l52w42lrovsv6y3pob4v6rcpjzkeyskojnpta6bsmuzgcntemmya)**
:

**[adjacent_find(_ForwardIterator, _ForwardIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmrvgcy3fnz2f6ztjnzsf6rcpjzkeyskojnpta6bsmuytsmdgmmya)**
:

**[adjacent_find(_ForwardIterator, _ForwardIterator, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmrvgcy3fnz2f6ztjnzsf6rcpjzkeyskojnpta6bsmuytsn3bmfrq)**
:

**[binary_search(_ForwardIterator, _ForwardIterator, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3cnfxgc4tzl5zwkylsmnuf6rcpjzkeyskojnpta6bsmu2tqyjrg42a)**
:

**[binary_search(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3cnfxgc4tzl5zwkylsmnuf6rcpjzkeyskojnpta6bsmu2tsmzsgm2a)**
:

**[count](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3dn52w45c7irhu4vcmjfhewxzqpazgkmjzgqyggyy)**
:

**[count_if](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3dn52w45c7nftf6rcpjzkeyskojnpta6bsmuywczdbheya)**
:

**[equal_range(_ForwardIterator, _ForwardIterator, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3fof2wc3c7ojqw4z3fl5ce6tsujreu4s27gb4dezjvg4zggyzq)**
:

**[equal_range(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3fof2wc3c7ojqw4z3fl5ce6tsujreu4s27gb4dezjvg5sggzrq)**
:

**[find](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix2ej5hfitcjjzfv6mdygjstcobsmfrti)**
:

**[find(_InputIterator, _InputIterator, const _Tp &, input_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix2ej5hfitcjjzfv6mdygjstcnrrg44di)**
:

**[find(_RandomAccessIterator, _RandomAccessIterator, const _Tp &, random_access_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix2ej5hfitcjjzfv6mdygjstcnzsmqydq)**
:

**[find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3fnzsf6rcpjzkeyskojnpta6bsmu3gcmjyha2a)**
:

**[find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3fnzsf6rcpjzkeyskojnpta6bsmu3gcy3cmnrq)**
:

**[find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3gnfzhg5c7n5tf6rcpjzkeyskojnpta6bsmu3dqmjzhe4a)**
:

**[find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3gnfzhg5c7n5tf6rcpjzkeyskojnpta6bsmu3dsmbtha2a)**
:

**[find_if](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3jmzpuit2okrgestsll4yhqmtfge4gcmlfmm)**
:

**[find_if(_InputIterator, _InputIterator, _Predicate, input_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3jmzpuit2okrgestsll4yhqmtfge3dsmbxha)**
:

**[find_if(_RandomAccessIterator, _RandomAccessIterator, _Predicate, random_access_iterator_tag)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfxgix3jmzpuit2okrgestsll4yhqmtfge3wkmrxmm)**
:

**[for_each](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gn5zf6zlbmnuf6rcpjzkeyskojnpta6bsmuytkyteg42a)**
:

**[generate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3hmvxgk4tborsv6rcpjzkeyskojnpta6bsmuzdizlgge2a)**
:

**[generate_n](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3hmvxgk4tborsv63s7irhu4vcmjfhewxzqpazgkmrvg42tmyy)**
:

**[includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzrwy5lemvzv6rcpjzkeyskojnpta6bsmu2tszjsmq4a)**
:

**[includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzrwy5lemvzv6rcpjzkeyskojnpta6bsmu2wczrxgyya)**
:

**[lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3mn53wk4s7mjxxk3tel5ce6tsujreu4s27gb4dezjugvqwkyzu)**
:

**[lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3mn53wk4s7mjxxk3tel5ce6tsujreu4s27gb4dezjugy2wiyju)**
:

**[max_element(_ForwardIterator, _ForwardIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmf4f6zlmmvwwk3tul5ce6tsujreu4s27gb4dezjwg44wknbq)**
:

**[max_element(_ForwardIterator, _ForwardIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmf4f6zlmmvwwk3tul5ce6tsujreu4s27gb4dezjwgrtdanrq)**
:

**[merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmvzgozk7irhu4vcmjfhewxzqpazgkndcgu2dayy)**
:

**[merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmvzgozk7irhu4vcmjfhewxzqpazgknddmftdayy)**
:

**[min_element(_ForwardIterator, _ForwardIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nnfxf6zlmmvwwk3tul5ce6tsujreu4s27gb4dezjwguzdezdd)**
:

**[min_element(_ForwardIterator, _ForwardIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nnfxf6zlmmvwwk3tul5ce6tsujreu4s27gb4dezjwgvstqold)**
:

**[next_permutation(_BidirectionalIterator, _BidirectionalIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv4hix3qmvzg25lumf2gs33ol5ce6tsujreu4s27gb4dezjwgyzdgmjy)**
:

**[next_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv4hix3qmvzg25lumf2gs33ol5ce6tsujreu4s27gb4dezjwgzswknzq)**
:

**[nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3ooruf6zlmmvwwk3tul5ce6tsujreu4s27gb4dezjvgvsdemry)**
:

**[nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3ooruf6zlmmvwwk3tul5ce6tsujreu4s27gb4dezjvgyytqojq)**
:

**[partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfzhi2lbnrpxg33sorpwg33qpfpuit2okrgestsll4yhqmtfgqygkmtemm)**
:

**[partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfzhi2lbnrpxg33sorpwg33qpfpuit2okrgestsll4yhqmtfgqywinldha)**
:

**[partition](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfzhi2lunfxw4x2ej5hfitcjjzfv6mdygjstgntdhfrwg)**
:

**[prev_permutation(_BidirectionalIterator, _BidirectionalIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qojsxmx3qmvzg25lumf2gs33ol5ce6tsujreu4s27gb4dezjwg4zdkmby)**
:

**[prev_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qojsxmx3qmvzg25lumf2gs33ol5ce6tsujreu4s27gb4dezjwg5sdmyld)**
:

**[random_shuffle(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smfxgi33nl5zwq5lgmzwgkx2ej5hfitcjjzfv6mdygjstgnbugayta)**
:

**[random_shuffle(_RandomAccessIterator, _RandomAccessIterator, _RandomNumberGenerator &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smfxgi33nl5zwq5lgmzwgkx2ej5hfitcjjzfv6mdygjstgnddmizgg)**
:

**[remove](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvww65tfl5ce6tsujreu4s27gb4dezjsg5rteobu)**
:

**[remove_copy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvww65tfl5rw64dzl5ce6tsujreu4s27gb4dezjsgvswgmjq)**
:

**[remove_copy_if](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvww65tfl5rw64dzl5uwmx2ej5hfitcjjzfv6mdygjstentemi4gg)**
:

**[remove_if](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvww65tfl5uwmx2ej5hfitcjjzfv6mdygjstenzzmjrtq)**
:

**[replace](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvygyyldmvpuit2okrgestsll4yhqmtfgiytanzsga)**
:

**[replace_copy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvygyyldmvpwg33qpfpuit2okrgestsll4yhqmtfgizgenzvmm)**
:

**[replace_copy_if](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvygyyldmvpwg33qpfpwszs7irhu4vcmjfhewxzqpazgkmrugeytcoa)**
:

**[replace_if](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smvygyyldmvpwszs7irhu4vcmjfhewxzqpazgkmrrmy2gmna)**
:

**[reverse](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smv3gk4ttmvpuit2okrgestsll4yhqmtfgjtdimldmm)**
:

**[reverse_copy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3smv3gk4ttmvpwg33qpfpuit2okrgestsll4yhqmtfgmydcyzrga)**
:

**[rotate_copy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3sn52gc5dfl5rw64dzl5ce6tsujreu4s27gb4dezjtgm4tkojq)**
:

**[search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmvqxey3il5ce6tsujreu4s27gb4dezjrmizdqmzu)**
:

**[search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmvqxey3il5ce6tsujreu4s27gb4dezjrmmytcm3d)**
:

**[search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmvqxey3il5xf6rcpjzkeyskojnpta6bsmuywgmzwge4a)**
:

**[search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmvqxey3il5xf6rcpjzkeyskojnpta6bsmuywizjugi4a)**
:

**[set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f6zdjmztgk4tfnzrwkx2ej5hfitcjjzfv6mdygjstmmbqhfrgg)**
:

**[set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f6zdjmztgk4tfnzrwkx2ej5hfitcjjzfv6mdygjstmmjqmqzda)**
:

**[set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f62loorsxe43fmn2gs33ol5ce6tsujreu4s27gb4dezjvmuzgiyju)**
:

**[set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f62loorsxe43fmn2gs33ol5ce6tsujreu4s27gb4dezjvmyytmyjq)**
:

**[set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f643znvwwk5dsnfrv6zdjmztgk4tfnzrwkx2ej5hfitcjjzfv6mdygjstmmrqme4dq)**
:

**[set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f643znvwwk5dsnfrv6zdjmztgk4tfnzrwkx2ej5hfitcjjzfv6mdygjstmmtghfswg)**
:

**[set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f65lonfxw4x2ej5hfitcjjzfv6mdygjstkytgge2ta)**
:

**[set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tmv2f65lonfxw4x2ej5hfitcjjzfv6mdygjstky3cmvtdi)**
:

**[sort(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tn5zhix2ej5hfitcjjzfv6mdygjstinbwgmzdi)**
:

**[sort(_RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tn5zhix2ej5hfitcjjzfv6mdygjstindggfrtq)**
:

**[swap_ranges](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3to5qxax3smfxgozltl5ce6tsujreu4s27gb4dezjrmvrdimbu)**
:

**[transform(_InputIterator, _InputIterator, _OutputIterator, _UnaryOperation)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3uojqw443gn5zg2x2ej5hfitcjjzfv6mdygjstczrzga4dq)**
:

**[transform(_InputIterator1, _InputIterator1, _InputIterator2, _OutputIterator, _BinaryOperation)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3uojqw443gn5zg2x2ej5hfitcjjzfv6mdygjstembvgu3gg)**
:

**[unique(_ForwardIterator, _ForwardIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3vnzuxc5lfl5ce6tsujreu4s27gb4dezjsmqzdeyzq)**
:

**[unique(_ForwardIterator, _ForwardIterator, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3vnzuxc5lfl5ce6tsujreu4s27gb4dezjsmrqwmyzy)**
:

**[upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3vobygk4s7mjxxk3tel5ce6tsujreu4s27gb4dezjug4zgmntd)**
:

**[upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3vobygk4s7mjxxk3tel5ce6tsujreu4s27gb4dezjug5rdmmld)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> void __final_insertion_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> void __final_insertion_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __gcd | __gcd | __gcd | __gcd | __gcd |

---

```
template<typename _EuclideanRingElement> _EuclideanRingElement __gcd(
    _EuclideanRingElement __m,
    _EuclideanRingElement __n)
```

##### Discussion

@if maint
This is a helper function for the rotate algorithm specialized on RAIs.
It returns the greatest common divisor of two integer values.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __inplace_stable_partition | __inplace_stable_partition | __inplace_stable_partition | __inplace_stable_partition | __inplace_stable_partition |

---

```
template<typename _ForwardIterator, typename _Predicate, typename _Distance> _ForwardIterator __inplace_stable_partition(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred,
    _Distance __len)
```

##### Discussion

@if maint
This is a helper function...
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> void __inplace_stable_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@if maint
This is a helper function for the stable sorting routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __inplace_stable_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> void __inplace_stable_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the stable sorting routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> void __insertion_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | __insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> void __insertion_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size) |

---

```
template<typename _RandomAccessIterator, typename _Size> void __introsort_loop(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Size __depth_limit)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) | __introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Size, typename _Compare> void __introsort_loop(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Size __depth_limit,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __lg | __lg | __lg | __lg | __lg |

---

```
template<typename _Size> inline _Size __lg(
    _Size __n)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __median(const _Tp &, const _Tp &, const _Tp &) | __median(const _Tp &, const _Tp &, const _Tp &) | __median(const _Tp &, const _Tp &, const _Tp &) | __median(const _Tp &, const _Tp &, const _Tp &) | __median(const _Tp &, const _Tp &, const _Tp &) |

---

```
template<typename _Tp> inline const _Tp& __median(
    const _Tp& __a,
    const _Tp& __b,
    const _Tp& __c)
```

##### Parameters

**`a`**
: A value.

**`b`**
: A value.

**`c`**
: A value.

##### Return Value

One of @p a, @p b or @p c.

If @c {l,m,n} is some convolution of @p {a,b,c} such that @c l<=m<=n
then the value returned will be @c m.
This is an SGI extension.
@ingroup SGIextensions

##### Discussion

@brief Find the median of three values.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __median(const _Tp &, const _Tp &, const _Tp &, _Compare) | __median(const _Tp &, const _Tp &, const _Tp &, _Compare) | __median(const _Tp &, const _Tp &, const _Tp &, _Compare) | __median(const _Tp &, const _Tp &, const _Tp &, _Compare) | __median(const _Tp &, const _Tp &, const _Tp &, _Compare) |

---

```
template<typename _Tp, typename _Compare> inline const _Tp& __median(
    const _Tp& __a,
    const _Tp& __b,
    const _Tp& __c,
    _Compare __comp)
```

##### Parameters

**`a`**
: A value.

**`b`**
: A value.

**`c`**
: A value.

**`comp`**
: A binary predicate.

##### Return Value

One of @p a, @p b or @p c.

If @c {l,m,n} is some convolution of @p {a,b,c} such that @p comp(l,m)
and @p comp(m,n) are both true then the value returned will be @c m.
This is an SGI extension.
@ingroup SGIextensions

##### Discussion

@brief Find the median of three values using a predicate for comparison.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance) |

---

```
template<typename _BidirectionalIterator, typename _Distance, typename _Pointer> void __merge_adaptive(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last,
    _Distance __len1,
    _Distance __len2,
    _Pointer __buffer,
    _Distance __buffer_size)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance, _Compare) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance, _Compare) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance, _Compare) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance, _Compare) | __merge_adaptive(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Pointer, _Distance, _Compare) |

---

```
template<typename _BidirectionalIterator, typename _Distance, typename _Pointer, typename _Compare> void __merge_adaptive(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last,
    _Distance __len1,
    _Distance __len2,
    _Pointer __buffer,
    _Distance __buffer_size,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3) |

---

```
template<typename _BidirectionalIterator1, typename _BidirectionalIterator2, typename _BidirectionalIterator3> _BidirectionalIterator3 __merge_backward(
    _BidirectionalIterator1 __first1,
    _BidirectionalIterator1 __last1,
    _BidirectionalIterator2 __first2,
    _BidirectionalIterator2 __last2,
    _BidirectionalIterator3 __result)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3, _Compare) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3, _Compare) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3, _Compare) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3, _Compare) | __merge_backward(_BidirectionalIterator1, _BidirectionalIterator1, _BidirectionalIterator2, _BidirectionalIterator2, _BidirectionalIterator3, _Compare) |

---

```
template<typename _BidirectionalIterator1, typename _BidirectionalIterator2, typename _BidirectionalIterator3, typename _Compare> _BidirectionalIterator3 __merge_backward(
    _BidirectionalIterator1 __first1,
    _BidirectionalIterator1 __last1,
    _BidirectionalIterator2 __first2,
    _BidirectionalIterator2 __last2,
    _BidirectionalIterator3 __result,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance) |

---

```
template<typename _BidirectionalIterator, typename _Distance> void __merge_without_buffer(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last,
    _Distance __len1,
    _Distance __len2)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Compare) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Compare) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Compare) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Compare) | __merge_without_buffer(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, _Distance, _Distance, _Compare) |

---

```
template<typename _BidirectionalIterator, typename _Distance, typename _Compare> void __merge_without_buffer(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last,
    _Distance __len1,
    _Distance __len2,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __partition(_BidirectionalIterator, _BidirectionalIterator, _Predicate, bidirectional_iterator_tag) | __partition(_BidirectionalIterator, _BidirectionalIterator, _Predicate, bidirectional_iterator_tag) | __partition(_BidirectionalIterator, _BidirectionalIterator, _Predicate, bidirectional_iterator_tag) | __partition(_BidirectionalIterator, _BidirectionalIterator, _Predicate, bidirectional_iterator_tag) | __partition(_BidirectionalIterator, _BidirectionalIterator, _Predicate, bidirectional_iterator_tag) |

---

```
template<typename _BidirectionalIterator, typename _Predicate> _BidirectionalIterator __partition(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last,
    _Predicate __pred,
    bidirectional_iterator_tag)
```

##### Discussion

@if maint
This is a helper function...
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __partition(_ForwardIterator, _ForwardIterator, _Predicate, forward_iterator_tag) | __partition(_ForwardIterator, _ForwardIterator, _Predicate, forward_iterator_tag) | __partition(_ForwardIterator, _ForwardIterator, _Predicate, forward_iterator_tag) | __partition(_ForwardIterator, _ForwardIterator, _Predicate, forward_iterator_tag) | __partition(_ForwardIterator, _ForwardIterator, _Predicate, forward_iterator_tag) |

---

```
template<typename _ForwardIterator, typename _Predicate> _ForwardIterator __partition(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred,
    forward_iterator_tag)
```

##### Discussion

@if maint
This is a helper function...
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __reverse(_BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __reverse(_BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __reverse(_BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __reverse(_BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __reverse(_BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) |

---

```
template<typename _BidirectionalIterator> void __reverse(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last,
    bidirectional_iterator_tag)
```

##### Discussion

@if maint
This is an uglified reverse(_BidirectionalIterator,
_BidirectionalIterator)
overloaded for bidirectional iterators.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __reverse(_RandomAccessIterator, _RandomAccessIterator, random_access_iterator_tag) | __reverse(_RandomAccessIterator, _RandomAccessIterator, random_access_iterator_tag) | __reverse(_RandomAccessIterator, _RandomAccessIterator, random_access_iterator_tag) | __reverse(_RandomAccessIterator, _RandomAccessIterator, random_access_iterator_tag) | __reverse(_RandomAccessIterator, _RandomAccessIterator, random_access_iterator_tag) |

---

```
template<typename _RandomAccessIterator> void __reverse(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    random_access_iterator_tag)
```

##### Discussion

@if maint
This is an uglified reverse(_BidirectionalIterator,
_BidirectionalIterator)
overloaded for random access iterators.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __rotate | __rotate | __rotate | __rotate | __rotate |

---

```
template<typename _RandomAccessIterator> void __rotate(
    _RandomAccessIterator __first,
    _RandomAccessIterator __middle,
    _RandomAccessIterator __last,
    random_access_iterator_tag)
```

##### Discussion

@if maint
This is a helper function for the rotate algorithm.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __rotate(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __rotate(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __rotate(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __rotate(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) | __rotate(_BidirectionalIterator, _BidirectionalIterator, _BidirectionalIterator, bidirectional_iterator_tag) |

---

```
template<typename _BidirectionalIterator> void __rotate(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last,
    bidirectional_iterator_tag)
```

##### Discussion

@if maint
This is a helper function for the rotate algorithm.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __rotate(_ForwardIterator, _ForwardIterator, _ForwardIterator, forward_iterator_tag) | __rotate(_ForwardIterator, _ForwardIterator, _ForwardIterator, forward_iterator_tag) | __rotate(_ForwardIterator, _ForwardIterator, _ForwardIterator, forward_iterator_tag) | __rotate(_ForwardIterator, _ForwardIterator, _ForwardIterator, forward_iterator_tag) | __rotate(_ForwardIterator, _ForwardIterator, _ForwardIterator, forward_iterator_tag) |

---

```
template<typename _ForwardIterator> void __rotate(
    _ForwardIterator __first,
    _ForwardIterator __middle,
    _ForwardIterator __last,
    forward_iterator_tag)
```

##### Discussion

@if maint
This is a helper function for the rotate algorithm.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __rotate_adaptive | __rotate_adaptive | __rotate_adaptive | __rotate_adaptive | __rotate_adaptive |

---

```
template<typename _BidirectionalIterator1, typename _BidirectionalIterator2, typename _Distance> _BidirectionalIterator1 __rotate_adaptive(
    _BidirectionalIterator1 __first,
    _BidirectionalIterator1 __middle,
    _BidirectionalIterator1 __last,
    _Distance __len1,
    _Distance __len2,
    _BidirectionalIterator2 __buffer,
    _Distance __buffer_size)
```

##### Discussion

@if maint
This is a helper function for the merge routines.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __stable_partition_adaptive | __stable_partition_adaptive | __stable_partition_adaptive | __stable_partition_adaptive | __stable_partition_adaptive |

---

```
template<typename _ForwardIterator, typename _Pointer, typename _Predicate, typename _Distance> _ForwardIterator __stable_partition_adaptive(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred,
    _Distance __len,
    _Pointer __buffer,
    _Distance __buffer_size)
```

##### Discussion

@if maint
This is a helper function...
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unguarded_linear_insert(_RandomAccessIterator, _Tp) | __unguarded_linear_insert(_RandomAccessIterator, _Tp) | __unguarded_linear_insert(_RandomAccessIterator, _Tp) | __unguarded_linear_insert(_RandomAccessIterator, _Tp) | __unguarded_linear_insert(_RandomAccessIterator, _Tp) |

---

```
template<typename _RandomAccessIterator, typename _Tp> void __unguarded_linear_insert(
    _RandomAccessIterator __last,
    _Tp __val)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unguarded_linear_insert(_RandomAccessIterator, _Tp, _Compare) | __unguarded_linear_insert(_RandomAccessIterator, _Tp, _Compare) | __unguarded_linear_insert(_RandomAccessIterator, _Tp, _Compare) | __unguarded_linear_insert(_RandomAccessIterator, _Tp, _Compare) | __unguarded_linear_insert(_RandomAccessIterator, _Tp, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Tp, typename _Compare> void __unguarded_linear_insert(
    _RandomAccessIterator __last,
    _Tp __val,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp) |

---

```
template<typename _RandomAccessIterator, typename _Tp> _RandomAccessIterator __unguarded_partition(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Tp __pivot)
```

##### Discussion

@if maint
This is a helper function...
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp, _Compare) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp, _Compare) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp, _Compare) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp, _Compare) | __unguarded_partition(_RandomAccessIterator, _RandomAccessIterator, _Tp, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Tp, typename _Compare> _RandomAccessIterator __unguarded_partition(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Tp __pivot,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function...
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, forward_iterator_tag) |

---

```
template<typename _InputIterator, typename _ForwardIterator> _ForwardIterator __unique_copy(
    _InputIterator __first,
    _InputIterator __last,
    _ForwardIterator __result,
    forward_iterator_tag)
```

##### Discussion

@if maint
This is an uglified unique_copy(_InputIterator, _InputIterator,
_OutputIterator)
overloaded for forward iterators.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, _BinaryPredicate, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, _BinaryPredicate, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, _BinaryPredicate, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, _BinaryPredicate, forward_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _ForwardIterator, _BinaryPredicate, forward_iterator_tag) |

---

```
template<typename _InputIterator, typename _ForwardIterator, typename _BinaryPredicate> _ForwardIterator __unique_copy(
    _InputIterator __first,
    _InputIterator __last,
    _ForwardIterator __result,
    _BinaryPredicate __binary_pred,
    forward_iterator_tag)
```

##### Discussion

@if maint
This is an uglified
unique_copy(_InputIterator, _InputIterator, _OutputIterator,
_BinaryPredicate)
overloaded for forward iterators.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unique_copy(_InputIterator, _InputIterator, _OutputIterator, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, output_iterator_tag) |

---

```
template<typename _InputIterator, typename _OutputIterator> _OutputIterator __unique_copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    output_iterator_tag)
```

##### Discussion

@if maint
This is an uglified unique_copy(_InputIterator, _InputIterator,
_OutputIterator)
overloaded for output iterators.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unique_copy(_InputIterator, _InputIterator, _OutputIterator, _BinaryPredicate, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, _BinaryPredicate, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, _BinaryPredicate, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, _BinaryPredicate, output_iterator_tag) | __unique_copy(_InputIterator, _InputIterator, _OutputIterator, _BinaryPredicate, output_iterator_tag) |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _BinaryPredicate> _OutputIterator __unique_copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _BinaryPredicate __binary_pred,
    output_iterator_tag)
```

##### Discussion

@if maint
This is an uglified
unique_copy(_InputIterator, _InputIterator, _OutputIterator,
_BinaryPredicate)
overloaded for output iterators.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| adjacent_find(_ForwardIterator, _ForwardIterator) | adjacent_find(_ForwardIterator, _ForwardIterator) | adjacent_find(_ForwardIterator, _ForwardIterator) | adjacent_find(_ForwardIterator, _ForwardIterator) | adjacent_find(_ForwardIterator, _ForwardIterator) |

---

```
template<typename _ForwardIterator> _ForwardIterator adjacent_find(
    _ForwardIterator __first,
    _ForwardIterator __last)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

##### Return Value

The first iterator @c i such that @c i and @c i+1 are both
valid iterators in @p [first,last) and such that @c \*i == @c \*(i+1),
or @p last if no such iterator exists.

##### Discussion

@brief Find two adjacent values in a sequence that are equal.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| adjacent_find(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | adjacent_find(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | adjacent_find(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | adjacent_find(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | adjacent_find(_ForwardIterator, _ForwardIterator, _BinaryPredicate) |

---

```
template<typename _ForwardIterator, typename _BinaryPredicate> _ForwardIterator adjacent_find(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _BinaryPredicate __binary_pred)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`binary_pred`**
: A binary predicate.

##### Return Value

The first iterator @c i such that @c i and @c i+1 are both
valid iterators in @p [first,last) and such that
@p binary_pred(\*i,\*(i+1)) is true, or @p last if no such iterator
exists.

##### Discussion

@brief Find two adjacent values in a sequence using a predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| binary_search(_ForwardIterator, _ForwardIterator, const _Tp &) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &) |

---

```
template<typename _ForwardIterator, typename _Tp> bool binary_search(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

##### Return Value

True if @a val (or its equivelent) is in [@a first,@a last ].
@ingroup binarysearch

Note that this does not actually return an iterator to @a val. For
that, use std::find or a container's specialized find member functions.

##### Discussion

@brief Determines whether an element exists in a range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| binary_search(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | binary_search(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) |

---

```
template<typename _ForwardIterator, typename _Tp, typename _Compare> bool binary_search(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val,
    _Compare __comp)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

**`comp`**
: A functor to use for comparisons.

##### Return Value

True if @a val (or its equivelent) is in [@a first,@a last ].
@ingroup binarysearch

Note that this does not actually return an iterator to @a val. For
that, use std::find or a container's specialized find member functions.

The comparison function should have the same effects on ordering as
the function used for the initial sort.

##### Discussion

@brief Determines whether an element exists in a range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| count | count | count | count | count |

---

```
template<typename _InputIterator, typename _Tp> typename iterator_traits<_InputIterator>::difference_type count(
    _InputIterator __first,
    _InputIterator __last,
    const _Tp& __value)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`value`**
: The value to be counted.

##### Return Value

The number of iterators @c i in the range @p [first,last)
for which @c \*i == @p value

##### Discussion

@brief Count the number of copies of a value in a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| count_if | count_if | count_if | count_if | count_if |

---

```
template<typename _InputIterator, typename _Predicate> typename iterator_traits<_InputIterator>::difference_type count_if(
    _InputIterator __first,
    _InputIterator __last,
    _Predicate __pred)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`pred`**
: A predicate.

##### Return Value

The number of iterators @c i in the range @p [first,last)
for which @p pred(\*i) is true.

##### Discussion

@brief Count the elements of a sequence for which a predicate is true.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| equal_range(_ForwardIterator, _ForwardIterator, const _Tp &) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &) |

---

```
template<typename _ForwardIterator, typename _Tp> pair<_ForwardIterator, _ForwardIterator> equal_range(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

##### Return Value

An pair of iterators defining the subrange.
@ingroup binarysearch

This is equivalent to
@code
std::make_pair(lower_bound(first, last, val),
upper_bound(first, last, val))
@endcode
but does not actually call those functions.

##### Discussion

@brief Finds the largest subrange in which @a val could be inserted
at any place in it without changing the ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| equal_range(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | equal_range(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) |

---

```
template<typename _ForwardIterator, typename _Tp, typename _Compare> pair<_ForwardIterator, _ForwardIterator> equal_range(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val,
    _Compare __comp)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

**`comp`**
: A functor to use for comparisons.

##### Return Value

An pair of iterators defining the subrange.
@ingroup binarysearch

This is equivalent to
@code
std::make_pair(lower_bound(first, last, val, comp),
upper_bound(first, last, val, comp))
@endcode
but does not actually call those functions.

##### Discussion

@brief Finds the largest subrange in which @a val could be inserted
at any place in it without changing the ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find | find | find | find | find |

---

```
template<typename _InputIterator, typename _Tp> inline _InputIterator find(
    _InputIterator __first,
    _InputIterator __last,
    const _Tp& __val)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`val`**
: The value to find.

##### Return Value

The first iterator @c i in the range @p [first,last)
such that @c \*i == @p val, or @p last if no such iterator exists.

##### Discussion

@brief Find the first occurrence of a value in a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find(_InputIterator, _InputIterator, const _Tp &, input_iterator_tag) | find(_InputIterator, _InputIterator, const _Tp &, input_iterator_tag) | find(_InputIterator, _InputIterator, const _Tp &, input_iterator_tag) | find(_InputIterator, _InputIterator, const _Tp &, input_iterator_tag) | find(_InputIterator, _InputIterator, const _Tp &, input_iterator_tag) |

---

```
template<typename _InputIterator, typename _Tp> inline _InputIterator find(
    _InputIterator __first,
    _InputIterator __last,
    const _Tp& __val,
    input_iterator_tag)
```

##### Discussion

@if maint
This is an overload used by find() for the Input Iterator case.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find(_RandomAccessIterator, _RandomAccessIterator, const _Tp &, random_access_iterator_tag) | find(_RandomAccessIterator, _RandomAccessIterator, const _Tp &, random_access_iterator_tag) | find(_RandomAccessIterator, _RandomAccessIterator, const _Tp &, random_access_iterator_tag) | find(_RandomAccessIterator, _RandomAccessIterator, const _Tp &, random_access_iterator_tag) | find(_RandomAccessIterator, _RandomAccessIterator, const _Tp &, random_access_iterator_tag) |

---

```
template<typename _RandomAccessIterator, typename _Tp> _RandomAccessIterator find(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    const _Tp& __val,
    random_access_iterator_tag)
```

##### Discussion

@if maint
This is an overload used by find() for the RAI case.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) |

---

```
template<typename _ForwardIterator1, typename _ForwardIterator2> inline _ForwardIterator1 find_end(
    _ForwardIterator1 __first1,
    _ForwardIterator1 __last1,
    _ForwardIterator2 __first2,
    _ForwardIterator2 __last2)
```

##### Parameters

**`first1`**
: Start of range to search.

**`last1`**
: End of range to search.

**`first2`**
: Start of sequence to match.

**`last2`**
: End of sequence to match.

##### Return Value

The last iterator @c i in the range
@p [first1,last1-(last2-first2)) such that @c \*(i+N) == @p \*(first2+N)
for each @c N in the range @p [0,last2-first2), or @p last1 if no
such iterator exists.

Searches the range @p [first1,last1) for a sub-sequence that compares
equal value-by-value with the sequence given by @p [first2,last2) and
returns an iterator to the first element of the sub-sequence, or
@p last1 if the sub-sequence is not found. The sub-sequence will be the
last such subsequence contained in [first,last1).

Because the sub-sequence must lie completely within the range
@p [first1,last1) it must start at a position less than
@p last1-(last2-first2) where @p last2-first2 is the length of the
sub-sequence.
This means that the returned iterator @c i will be in the range
@p [first1,last1-(last2-first2))

##### Discussion

@brief Find last matching subsequence in a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | find_end(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) |

---

```
template<typename _ForwardIterator1, typename _ForwardIterator2, typename _BinaryPredicate> inline _ForwardIterator1 find_end(
    _ForwardIterator1 __first1,
    _ForwardIterator1 __last1,
    _ForwardIterator2 __first2,
    _ForwardIterator2 __last2,
    _BinaryPredicate __comp)
```

##### Parameters

**`first1`**
: Start of range to search.

**`last1`**
: End of range to search.

**`first2`**
: Start of sequence to match.

**`last2`**
: End of sequence to match.

**`comp`**
: The predicate to use.

##### Return Value

The last iterator @c i in the range
@p [first1,last1-(last2-first2)) such that @c predicate(\*(i+N), @p
(first2+N)) is true for each @c N in the range @p [0,last2-first2), or
@p last1 if no such iterator exists.

Searches the range @p [first1,last1) for a sub-sequence that compares
equal value-by-value with the sequence given by @p [first2,last2) using
comp as a predicate and returns an iterator to the first element of the
sub-sequence, or @p last1 if the sub-sequence is not found. The
sub-sequence will be the last such subsequence contained in
[first,last1).

Because the sub-sequence must lie completely within the range
@p [first1,last1) it must start at a position less than
@p last1-(last2-first2) where @p last2-first2 is the length of the
sub-sequence.
This means that the returned iterator @c i will be in the range
@p [first1,last1-(last2-first2))

##### Discussion

@brief Find last matching subsequence in a sequence using a predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator) |

---

```
template<typename _InputIterator, typename _ForwardIterator> _InputIterator find_first_of(
    _InputIterator __first1,
    _InputIterator __last1,
    _ForwardIterator __first2,
    _ForwardIterator __last2)
```

##### Parameters

**`first1`**
: Start of range to search.

**`last1`**
: End of range to search.

**`first2`**
: Start of match candidates.

**`last2`**
: End of match candidates.

##### Return Value

The first iterator @c i in the range
@p [first1,last1) such that @c \*i == @p \*(i2) such that i2 is an
interator in [first2,last2), or @p last1 if no such iterator exists.

Searches the range @p [first1,last1) for an element that is equal to
some element in the range [first2,last2). If found, returns an iterator
in the range [first1,last1), otherwise returns @p last1.

##### Discussion

@brief Find element from a set in a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator, _BinaryPredicate) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator, _BinaryPredicate) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator, _BinaryPredicate) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator, _BinaryPredicate) | find_first_of(_InputIterator, _InputIterator, _ForwardIterator, _ForwardIterator, _BinaryPredicate) |

---

```
template<typename _InputIterator, typename _ForwardIterator, typename _BinaryPredicate> _InputIterator find_first_of(
    _InputIterator __first1,
    _InputIterator __last1,
    _ForwardIterator __first2,
    _ForwardIterator __last2,
    _BinaryPredicate __comp)
```

##### Parameters

**`first1`**
: Start of range to search.

**`last1`**
: End of range to search.

**`first2`**
: Start of match candidates.

**`last2`**
: End of match candidates.

**`comp`**
: Predicate to use.

##### Return Value

The first iterator @c i in the range
@p [first1,last1) such that @c comp(\*i, @p \*(i2)) is true and i2 is an
interator in [first2,last2), or @p last1 if no such iterator exists.

Searches the range @p [first1,last1) for an element that is equal to
some element in the range [first2,last2). If found, returns an iterator in
the range [first1,last1), otherwise returns @p last1.

##### Discussion

@brief Find element from a set in a sequence using a predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_if | find_if | find_if | find_if | find_if |

---

```
template<typename _InputIterator, typename _Predicate> inline _InputIterator find_if(
    _InputIterator __first,
    _InputIterator __last,
    _Predicate __pred)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`pred`**
: A predicate.

##### Return Value

The first iterator @c i in the range @p [first,last)
such that @p pred(\*i) is true, or @p last if no such iterator exists.

##### Discussion

@brief Find the first element in a sequence for which a predicate is true.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_if(_InputIterator, _InputIterator, _Predicate, input_iterator_tag) | find_if(_InputIterator, _InputIterator, _Predicate, input_iterator_tag) | find_if(_InputIterator, _InputIterator, _Predicate, input_iterator_tag) | find_if(_InputIterator, _InputIterator, _Predicate, input_iterator_tag) | find_if(_InputIterator, _InputIterator, _Predicate, input_iterator_tag) |

---

```
template<typename _InputIterator, typename _Predicate> inline _InputIterator find_if(
    _InputIterator __first,
    _InputIterator __last,
    _Predicate __pred,
    input_iterator_tag)
```

##### Discussion

@if maint
This is an overload used by find_if() for the Input Iterator case.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| find_if(_RandomAccessIterator, _RandomAccessIterator, _Predicate, random_access_iterator_tag) | find_if(_RandomAccessIterator, _RandomAccessIterator, _Predicate, random_access_iterator_tag) | find_if(_RandomAccessIterator, _RandomAccessIterator, _Predicate, random_access_iterator_tag) | find_if(_RandomAccessIterator, _RandomAccessIterator, _Predicate, random_access_iterator_tag) | find_if(_RandomAccessIterator, _RandomAccessIterator, _Predicate, random_access_iterator_tag) |

---

```
template<typename _RandomAccessIterator, typename _Predicate> _RandomAccessIterator find_if(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Predicate __pred,
    random_access_iterator_tag)
```

##### Discussion

@if maint
This is an overload used by find_if() for the RAI case.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| for_each | for_each | for_each | for_each | for_each |

---

```
template<typename _InputIterator, typename _Function> _Function for_each(
    _InputIterator __first,
    _InputIterator __last,
    _Function __f)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`f`**
: A unary function object.

##### Return Value

@p f.

Applies the function object @p f to each element in the range
@p [first,last). @p f must not modify the order of the sequence.
If @p f has a return value it is ignored.

##### Discussion

@brief Apply a function to every element of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| generate | generate | generate | generate | generate |

---

```
template<typename _ForwardIterator, typename _Generator> void generate(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Generator __gen)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`gen`**
: A function object taking no arguments.

##### Return Value

generate() returns no value.

Performs the assignment @c \*i = @p gen() for each @c i in the range
@p [first,last).

##### Discussion

@brief Assign the result of a function object to each value in a
sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| generate_n | generate_n | generate_n | generate_n | generate_n |

---

```
template<typename _OutputIterator, typename _Size, typename _Generator> _OutputIterator generate_n(
    _OutputIterator __first,
    _Size __n,
    _Generator __gen)
```

##### Parameters

**`first`**
: A forward iterator.

**`n`**
: The length of the sequence.

**`gen`**
: A function object taking no arguments.

##### Return Value

The end of the sequence, @p first+n

Performs the assignment @c \*i = @p gen() for each @c i in the range
@p [first,first+n).

##### Discussion

@brief Assign the result of a function object to each value in a
sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) |

---

```
template<typename _InputIterator1, typename _InputIterator2> bool includes(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2)
```

##### Parameters

**`first1`**
: Start of search range.

**`last1`**
: End of search range.

**`first2`**
: Start of sequence

**`last2`**
: End of sequence.

##### Return Value

True if each element in [first2,last2) is contained in order
within [first1,last1). False otherwise.
@ingroup setoperations

This operation expects both [first1,last1) and [first2,last2) to be
sorted. Searches for the presence of each element in [first2,last2)
within [first1,last1). The iterators over each range only move forward,
so this is a linear algorithm. If an element in [first2,last2) is not
found before the search iterator reaches @a last2, false is returned.

##### Discussion

@brief Determines whether all elements of a sequence exists in a range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | includes(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _Compare> bool includes(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _Compare __comp)
```

##### Parameters

**`first1`**
: Start of search range.

**`last1`**
: End of search range.

**`first2`**
: Start of sequence

**`last2`**
: End of sequence.

**`comp`**
: Comparison function to use.

##### Return Value

True if each element in [first2,last2) is contained in order
within [first1,last1) according to comp. False otherwise.
@ingroup setoperations

This operation expects both [first1,last1) and [first2,last2) to be
sorted. Searches for the presence of each element in [first2,last2)
within [first1,last1), using comp to decide. The iterators over each
range only move forward, so this is a linear algorithm. If an element
in [first2,last2) is not found before the search iterator reaches @a
last2, false is returned.

##### Discussion

@brief Determines whether all elements of a sequence exists in a range
using comparison.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &) |

---

```
template<typename _ForwardIterator, typename _Tp> _ForwardIterator lower_bound(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

##### Return Value

An iterator pointing to the first element "not less than" @a val,
or end() if every element is less than @a val.
@ingroup binarysearch

##### Discussion

@brief Finds the first position in which @a val could be inserted
without changing the ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | lower_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) |

---

```
template<typename _ForwardIterator, typename _Tp, typename _Compare> _ForwardIterator lower_bound(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val,
    _Compare __comp)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

**`comp`**
: A functor to use for comparisons.

##### Return Value

An iterator pointing to the first element "not less than" @a val,
or end() if every element is less than @a val.
@ingroup binarysearch

The comparison function should have the same effects on ordering as
the function used for the initial sort.

##### Discussion

@brief Finds the first position in which @a val could be inserted
without changing the ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| max_element(_ForwardIterator, _ForwardIterator) | max_element(_ForwardIterator, _ForwardIterator) | max_element(_ForwardIterator, _ForwardIterator) | max_element(_ForwardIterator, _ForwardIterator) | max_element(_ForwardIterator, _ForwardIterator) |

---

```
template<typename _ForwardIterator> _ForwardIterator max_element(
    _ForwardIterator __first,
    _ForwardIterator __last)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

##### Return Value

Iterator referencing the first instance of the largest value.

##### Discussion

@brief Return the maximum element in a range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| max_element(_ForwardIterator, _ForwardIterator, _Compare) | max_element(_ForwardIterator, _ForwardIterator, _Compare) | max_element(_ForwardIterator, _ForwardIterator, _Compare) | max_element(_ForwardIterator, _ForwardIterator, _Compare) | max_element(_ForwardIterator, _ForwardIterator, _Compare) |

---

```
template<typename _ForwardIterator, typename _Compare> _ForwardIterator max_element(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

**`comp`**
: Comparison functor.

##### Return Value

Iterator referencing the first instance of the largest value
according to comp.

##### Discussion

@brief Return the maximum element in a range using comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator> _OutputIterator merge(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result)
```

##### Parameters

**`first1`**
: An iterator.

**`first2`**
: Another iterator.

**`last1`**
: Another iterator.

**`last2`**
: Another iterator.

**`result`**
: An iterator pointing to the end of the merged range.

##### Return Value

An iterator pointing to the first element "not less than" @a val.

Merges the ranges [first1,last1) and [first2,last2) into the sorted range
[result, result + (last1-first1) + (last2-first2)). Both input ranges
must be sorted, and the output range must not overlap with either of
the input ranges. The sort is @e stable, that is, for equivalent
elements in the two ranges, elements from the first range will always
come before elements from the second.

##### Discussion

@brief Merges two sorted ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | merge(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator, typename _Compare> _OutputIterator merge(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result,
    _Compare __comp)
```

##### Parameters

**`first1`**
: An iterator.

**`first2`**
: Another iterator.

**`last1`**
: Another iterator.

**`last2`**
: Another iterator.

**`result`**
: An iterator pointing to the end of the merged range.

**`comp`**
: A functor to use for comparisons.

##### Return Value

An iterator pointing to the first element "not less than" @a val.

Merges the ranges [first1,last1) and [first2,last2) into the sorted range
[result, result + (last1-first1) + (last2-first2)). Both input ranges
must be sorted, and the output range must not overlap with either of
the input ranges. The sort is @e stable, that is, for equivalent
elements in the two ranges, elements from the first range will always
come before elements from the second.

The comparison function should have the same effects on ordering as
the function used for the initial sort.

##### Discussion

@brief Merges two sorted ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| min_element(_ForwardIterator, _ForwardIterator) | min_element(_ForwardIterator, _ForwardIterator) | min_element(_ForwardIterator, _ForwardIterator) | min_element(_ForwardIterator, _ForwardIterator) | min_element(_ForwardIterator, _ForwardIterator) |

---

```
template<typename _ForwardIterator> _ForwardIterator min_element(
    _ForwardIterator __first,
    _ForwardIterator __last)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

##### Return Value

Iterator referencing the first instance of the smallest value.

##### Discussion

@brief Return the minimum element in a range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| min_element(_ForwardIterator, _ForwardIterator, _Compare) | min_element(_ForwardIterator, _ForwardIterator, _Compare) | min_element(_ForwardIterator, _ForwardIterator, _Compare) | min_element(_ForwardIterator, _ForwardIterator, _Compare) | min_element(_ForwardIterator, _ForwardIterator, _Compare) |

---

```
template<typename _ForwardIterator, typename _Compare> _ForwardIterator min_element(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

**`comp`**
: Comparison functor.

##### Return Value

Iterator referencing the first instance of the smallest value
according to comp.

##### Discussion

@brief Return the minimum element in a range using comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| next_permutation(_BidirectionalIterator, _BidirectionalIterator) | next_permutation(_BidirectionalIterator, _BidirectionalIterator) | next_permutation(_BidirectionalIterator, _BidirectionalIterator) | next_permutation(_BidirectionalIterator, _BidirectionalIterator) | next_permutation(_BidirectionalIterator, _BidirectionalIterator) |

---

```
template<typename _BidirectionalIterator> bool next_permutation(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

##### Return Value

False if wrapped to first permutation, true otherwise.

Treats all permutations of the range as a set of "dictionary" sorted
sequences. Permutes the current sequence into the next one of this set.
Returns true if there are more sequences to generate. If the sequence
is the largest of the set, the smallest is generated and false returned.

##### Discussion

@brief Permute range into the next "dictionary" ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| next_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | next_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | next_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | next_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | next_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) |

---

```
template<typename _BidirectionalIterator, typename _Compare> bool next_permutation(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

**`comp`**
:

##### Return Value

False if wrapped to first permutation, true otherwise.

Treats all permutations of the range [first,last) as a set of
"dictionary" sorted sequences ordered by @a comp. Permutes the current
sequence into the next one of this set. Returns true if there are more
sequences to generate. If the sequence is the largest of the set, the
smallest is generated and false returned.

##### Discussion

@brief Permute range into the next "dictionary" ordering using
comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> void nth_element(
    _RandomAccessIterator __first,
    _RandomAccessIterator __nth,
    _RandomAccessIterator __last)
```

##### Parameters

**`first`**
: An iterator.

**`nth`**
: Another iterator.

**`last`**
: Another iterator.

##### Return Value

Nothing.

Rearranges the elements in the range @p [first,last) so that @p \*nth
is the same element that would have been in that position had the
whole sequence been sorted.
whole sequence been sorted. The elements either side of @p \*nth are
not completely sorted, but for any iterator @i in the range
@p [first,nth) and any iterator @j in the range @p [nth,last) it
holds that @p \*j<\*i is false.

##### Discussion

@brief Sort a sequence just enough to find a particular position.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | nth_element(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> void nth_element(
    _RandomAccessIterator __first,
    _RandomAccessIterator __nth,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: An iterator.

**`nth`**
: Another iterator.

**`last`**
: Another iterator.

**`comp`**
: A comparison functor.

##### Return Value

Nothing.

Rearranges the elements in the range @p [first,last) so that @p \*nth
is the same element that would have been in that position had the
whole sequence been sorted. The elements either side of @p \*nth are
not completely sorted, but for any iterator @i in the range
@p [first,nth) and any iterator @j in the range @p [nth,last) it
holds that @p comp(\*j,\*i) is false.

##### Discussion

@brief Sort a sequence just enough to find a particular position
using a predicate for comparison.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _InputIterator, typename _RandomAccessIterator> _RandomAccessIterator partial_sort_copy(
    _InputIterator __first,
    _InputIterator __last,
    _RandomAccessIterator __result_first,
    _RandomAccessIterator __result_last)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`result_first`**
: A random-access iterator.

**`result_last`**
: Another random-access iterator.

##### Return Value

An iterator indicating the end of the resulting sequence.

Copies and sorts the smallest N values from the range @p [first,last)
to the range beginning at @p result_first, where the number of
elements to be copied, @p N, is the smaller of @p (last-first) and
@p (result_last-result_first).
After the sort if @p i and @j are iterators in the range
@p [result_first,result_first+N) such that @i precedes @j then
@p \*j<\*i is false.
The value returned is @p result_first+N.

##### Discussion

@brief Copy the smallest elements of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) | partial_sort_copy(_InputIterator, _InputIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _InputIterator, typename _RandomAccessIterator, typename _Compare> _RandomAccessIterator partial_sort_copy(
    _InputIterator __first,
    _InputIterator __last,
    _RandomAccessIterator __result_first,
    _RandomAccessIterator __result_last,
    _Compare __comp)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: Another input iterator.

**`result_first`**
: A random-access iterator.

**`result_last`**
: Another random-access iterator.

**`comp`**
: A comparison functor.

##### Return Value

An iterator indicating the end of the resulting sequence.

Copies and sorts the smallest N values from the range @p [first,last)
to the range beginning at @p result_first, where the number of
elements to be copied, @p N, is the smaller of @p (last-first) and
@p (result_last-result_first).
After the sort if @p i and @j are iterators in the range
@p [result_first,result_first+N) such that @i precedes @j then
@p comp(\*j,\*i) is false.
The value returned is @p result_first+N.

##### Discussion

@brief Copy the smallest elements of a sequence using a predicate for
comparison.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partition | partition | partition | partition | partition |

---

```
template<typename _ForwardIterator, typename _Predicate> inline _ForwardIterator partition(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`pred`**
: A predicate functor.

##### Return Value

An iterator @p middle such that @p pred(i) is true for each
iterator @p i in the range @p [first,middle) and false for each @p i
in the range @p [middle,last).

@p pred must not modify its operand. @p partition() does not preserve
the relative ordering of elements in each group, use
@p stable_partition() if this is needed.

##### Discussion

@brief Move elements for which a predicate is true to the beginning
of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| prev_permutation(_BidirectionalIterator, _BidirectionalIterator) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator) |

---

```
template<typename _BidirectionalIterator> bool prev_permutation(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

##### Return Value

False if wrapped to last permutation, true otherwise.

Treats all permutations of the range as a set of "dictionary" sorted
sequences. Permutes the current sequence into the previous one of this
set. Returns true if there are more sequences to generate. If the
sequence is the smallest of the set, the largest is generated and false
returned.

##### Discussion

@brief Permute range into the previous "dictionary" ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| prev_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) | prev_permutation(_BidirectionalIterator, _BidirectionalIterator, _Compare) |

---

```
template<typename _BidirectionalIterator, typename _Compare> bool prev_permutation(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

**`comp`**
:

##### Return Value

False if wrapped to last permutation, true otherwise.

Treats all permutations of the range [first,last) as a set of
"dictionary" sorted sequences ordered by @a comp. Permutes the current
sequence into the previous one of this set. Returns true if there are
more sequences to generate. If the sequence is the smallest of the set,
the largest is generated and false returned.

##### Discussion

@brief Permute range into the previous "dictionary" ordering using
comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| random_shuffle(_RandomAccessIterator, _RandomAccessIterator) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> inline void random_shuffle(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

##### Return Value

Nothing.

Reorder the elements in the range @p [first,last) using a random
distribution, so that every possible ordering of the sequence is
equally likely.

##### Discussion

@brief Randomly shuffle the elements of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| random_shuffle(_RandomAccessIterator, _RandomAccessIterator, _RandomNumberGenerator &) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator, _RandomNumberGenerator &) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator, _RandomNumberGenerator &) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator, _RandomNumberGenerator &) | random_shuffle(_RandomAccessIterator, _RandomAccessIterator, _RandomNumberGenerator &) |

---

```
template<typename _RandomAccessIterator, typename _RandomNumberGenerator> void random_shuffle(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _RandomNumberGenerator& __rand)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`rand`**
: The RNG functor or function.

##### Return Value

Nothing.

Reorders the elements in the range @p [first,last) using @p rand to
provide a random distribution. Calling @p rand(N) for a positive
integer @p N should return a randomly chosen integer from the
range [0,N).

##### Discussion

@brief Shuffle the elements of a sequence using a random number
generator.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| remove | remove | remove | remove | remove |

---

```
template<typename _ForwardIterator, typename _Tp> _ForwardIterator remove(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __value)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`value`**
: The value to be removed.

##### Return Value

An iterator designating the end of the resulting sequence.

All elements equal to @p value are removed from the range
@p [first,last).

remove() is stable, so the relative order of elements that are
not removed is unchanged.

Elements between the end of the resulting sequence and @p last
are still present, but their value is unspecified.

##### Discussion

@brief Remove elements from a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| remove_copy | remove_copy | remove_copy | remove_copy | remove_copy |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _Tp> _OutputIterator remove_copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    const _Tp& __value)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`result`**
: An output iterator.

**`value`**
: The value to be removed.

##### Return Value

An iterator designating the end of the resulting sequence.

Copies each element in the range @p [first,last) not equal to @p value
to the range beginning at @p result.
remove_copy() is stable, so the relative order of elements that are
copied is unchanged.

##### Discussion

@brief Copy a sequence, removing elements of a given value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| remove_copy_if | remove_copy_if | remove_copy_if | remove_copy_if | remove_copy_if |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _Predicate> _OutputIterator remove_copy_if(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _Predicate __pred)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`result`**
: An output iterator.

**`pred`**
: A predicate.

##### Return Value

An iterator designating the end of the resulting sequence.

Copies each element in the range @p [first,last) for which
@p pred returns true to the range beginning at @p result.

remove_copy_if() is stable, so the relative order of elements that are
copied is unchanged.

##### Discussion

@brief Copy a sequence, removing elements for which a predicate is true.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| remove_if | remove_if | remove_if | remove_if | remove_if |

---

```
template<typename _ForwardIterator, typename _Predicate> _ForwardIterator remove_if(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`pred`**
: A predicate.

##### Return Value

An iterator designating the end of the resulting sequence.

All elements for which @p pred returns true are removed from the range
@p [first,last).

remove_if() is stable, so the relative order of elements that are
not removed is unchanged.

Elements between the end of the resulting sequence and @p last
are still present, but their value is unspecified.

##### Discussion

@brief Remove elements from a sequence using a predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| replace | replace | replace | replace | replace |

---

```
template<typename _ForwardIterator, typename _Tp> void replace(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __old_value,
    const _Tp& __new_value)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`old_value`**
: The value to be replaced.

**`new_value`**
: The replacement value.

##### Return Value

replace() returns no value.

For each iterator @c i in the range @p [first,last) if @c \*i ==
@p old_value then the assignment @c \*i = @p new_value is performed.

##### Discussion

@brief Replace each occurrence of one value in a sequence with another
value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| replace_copy | replace_copy | replace_copy | replace_copy | replace_copy |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _Tp> _OutputIterator replace_copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    const _Tp& __old_value,
    const _Tp& __new_value)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`result`**
: An output iterator.

**`old_value`**
: The value to be replaced.

**`new_value`**
: The replacement value.

##### Return Value

The end of the output sequence, @p result+(last-first).

Copies each element in the input range @p [first,last) to the
output range @p [result,result+(last-first)) replacing elements
equal to @p old_value with @p new_value.

##### Discussion

@brief Copy a sequence, replacing each element of one value with another
value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| replace_copy_if | replace_copy_if | replace_copy_if | replace_copy_if | replace_copy_if |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _Predicate, typename _Tp> _OutputIterator replace_copy_if(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _Predicate __pred,
    const _Tp& __new_value)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`result`**
: An output iterator.

**`pred`**
: A predicate.

**`new_value`**
: The replacement value.

##### Return Value

The end of the output sequence, @p result+(last-first).

Copies each element in the range @p [first,last) to the range
@p [result,result+(last-first)) replacing elements for which
@p pred returns true with @p new_value.

##### Discussion

@brief Copy a sequence, replacing each value for which a predicate
returns true with another value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| replace_if | replace_if | replace_if | replace_if | replace_if |

---

```
template<typename _ForwardIterator, typename _Predicate, typename _Tp> void replace_if(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred,
    const _Tp& __new_value)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`pred`**
: A predicate.

**`new_value`**
: The replacement value.

##### Return Value

replace_if() returns no value.

For each iterator @c i in the range @p [first,last) if @p pred(\*i)
is true then the assignment @c \*i = @p new_value is performed.

##### Discussion

@brief Replace each value in a sequence for which a predicate returns
true with another value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| reverse | reverse | reverse | reverse | reverse |

---

```
template<typename _BidirectionalIterator> inline void reverse(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last)
```

##### Parameters

**`first`**
: A bidirectional iterator.

**`last`**
: A bidirectional iterator.

##### Return Value

reverse() returns no value.

Reverses the order of the elements in the range @p [first,last),
so that the first element becomes the last etc.
For every @c i such that @p 0<=i<=(last-first)/2), @p reverse()
swaps @p \*(first+i) and @p \*(last-(i+1))

##### Discussion

@brief Reverse a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| reverse_copy | reverse_copy | reverse_copy | reverse_copy | reverse_copy |

---

```
template<typename _BidirectionalIterator, typename _OutputIterator> _OutputIterator reverse_copy(
    _BidirectionalIterator __first,
    _BidirectionalIterator __last,
    _OutputIterator __result)
```

##### Parameters

**`first`**
: A bidirectional iterator.

**`last`**
: A bidirectional iterator.

**`result`**
: An output iterator.

##### Return Value

An iterator designating the end of the resulting sequence.

Copies the elements in the range @p [first,last) to the range
@p [result,result+(last-first)) such that the order of the
elements is reversed.
For every @c i such that @p 0<=i<=(last-first), @p reverse_copy()
performs the assignment @p \*(result+(last-first)-i) = \*(first+i).
The ranges @p [first,last) and @p [result,result+(last-first))
must not overlap.

##### Discussion

@brief Copy a sequence, reversing its elements.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| rotate_copy | rotate_copy | rotate_copy | rotate_copy | rotate_copy |

---

```
template<typename _ForwardIterator, typename _OutputIterator> _OutputIterator rotate_copy(
    _ForwardIterator __first,
    _ForwardIterator __middle,
    _ForwardIterator __last,
    _OutputIterator __result)
```

##### Parameters

**`first`**
: A forward iterator.

**`middle`**
: A forward iterator.

**`last`**
: A forward iterator.

**`result`**
: An output iterator.

##### Return Value

An iterator designating the end of the resulting sequence.

Copies the elements of the range @p [first,last) to the range
beginning at @result, rotating the copied elements by @p (middle-first)
positions so that the element at @p middle is moved to @p result, the
element at @p middle+1 is moved to @result+1 and so on for each element
in the range @p [first,last).

Performs @p \*(result+(n+(last-middle))%(last-first))=\*(first+n) for
each @p n in the range @p [0,last-first).

##### Discussion

@brief Copy a sequence, rotating its elements.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2) |

---

```
template<typename _ForwardIterator1, typename _ForwardIterator2> _ForwardIterator1 search(
    _ForwardIterator1 __first1,
    _ForwardIterator1 __last1,
    _ForwardIterator2 __first2,
    _ForwardIterator2 __last2)
```

##### Parameters

**`first1`**
: A forward iterator.

**`last1`**
: A forward iterator.

**`first2`**
: A forward iterator.

**`last2`**
: A forward iterator.

##### Return Value

The first iterator @c i in the range
@p [first1,last1-(last2-first2)) such that @c \*(i+N) == @p \*(first2+N)
for each @c N in the range @p [0,last2-first2), or @p last1 if no
such iterator exists.

Searches the range @p [first1,last1) for a sub-sequence that compares
equal value-by-value with the sequence given by @p [first2,last2) and
returns an iterator to the first element of the sub-sequence, or
@p last1 if the sub-sequence is not found.

Because the sub-sequence must lie completely within the range
@p [first1,last1) it must start at a position less than
@p last1-(last2-first2) where @p last2-first2 is the length of the
sub-sequence.
This means that the returned iterator @c i will be in the range
@p [first1,last1-(last2-first2))

##### Discussion

@brief Search a sequence for a matching sub-sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) | search(_ForwardIterator1, _ForwardIterator1, _ForwardIterator2, _ForwardIterator2, _BinaryPredicate) |

---

__See:__
> **_ForwardIter1, _ForwardIter2, _ForwardIter2)**
> :
>
> ****
> :

```
template<typename _ForwardIterator1, typename _ForwardIterator2, typename _BinaryPredicate> _ForwardIterator1 search(
    _ForwardIterator1 __first1,
    _ForwardIterator1 __last1,
    _ForwardIterator2 __first2,
    _ForwardIterator2 __last2,
    _BinaryPredicate __predicate)
```

##### Parameters

**`first1`**
: A forward iterator.

**`last1`**
: A forward iterator.

**`first2`**
: A forward iterator.

**`last2`**
: A forward iterator.

**`predicate`**
: A binary predicate.

##### Return Value

The first iterator @c i in the range
@p [first1,last1-(last2-first2)) such that
@p predicate(\*(i+N),\*(first2+N)) is true for each @c N in the range
@p [0,last2-first2), or @p last1 if no such iterator exists.

Searches the range @p [first1,last1) for a sub-sequence that compares
equal value-by-value with the sequence given by @p [first2,last2),
using @p predicate to determine equality, and returns an iterator
to the first element of the sub-sequence, or @p last1 if no such
iterator exists.

##### Discussion

@brief Search a sequence for a matching sub-sequence using a predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &) |

---

```
template<typename _ForwardIterator, typename _Integer, typename _Tp> _ForwardIterator search_n(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Integer __count,
    const _Tp& __val)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`count`**
: The number of consecutive values.

**`val`**
: The value to find.

##### Return Value

The first iterator @c i in the range @p [first,last-count)
such that @c \*(i+N) == @p val for each @c N in the range @p [0,count),
or @p last if no such iterator exists.

Searches the range @p [first,last) for @p count consecutive elements
equal to @p val.

##### Discussion

@brief Search a sequence for a number of consecutive values.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &, _BinaryPredicate) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &, _BinaryPredicate) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &, _BinaryPredicate) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &, _BinaryPredicate) | search_n(_ForwardIterator, _ForwardIterator, _Integer, const _Tp &, _BinaryPredicate) |

---

```
template<typename _ForwardIterator, typename _Integer, typename _Tp, typename _BinaryPredicate> _ForwardIterator search_n(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Integer __count,
    const _Tp& __val,
    _BinaryPredicate __binary_pred)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`count`**
: The number of consecutive values.

**`val`**
: The value to find.

**`binary_pred`**
: A binary predicate.

##### Return Value

The first iterator @c i in the range @p [first,last-count)
such that @p binary_pred(\*(i+N),val) is true for each @c N in the
range @p [0,count), or @p last if no such iterator exists.

Searches the range @p [first,last) for @p count consecutive elements
for which the predicate returns true.

##### Discussion

@brief Search a sequence for a number of consecutive values using a
predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator> _OutputIterator set_difference(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
the first range but not the second in order to the output range.
Iterators increment for each range. When the current element of the
first range is less than the second, that element is copied and the
iterator advances. If the current element of the second range is less,
the iterator advances, but no element is copied. If an element is
contained in both ranges, no elements are copied and both ranges
advance. The output range may not overlap either input range.

##### Discussion

@brief Return the difference of two sorted ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator, typename _Compare> _OutputIterator set_difference(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result,
    _Compare __comp)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

**`comp`**
: The comparison functor.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
the first range but not the second in order to the output range.
Iterators increment for each range. When the current element of the
first range is less than the second according to @a comp, that element
is copied and the iterator advances. If the current element of the
second range is less, no element is copied and the iterator advances.
If an element is contained in both ranges according to @a comp, no
elements are copied and both ranges advance. The output range may not
overlap either input range.

##### Discussion

@brief Return the difference of two sorted ranges using comparison
functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator> _OutputIterator set_intersection(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
both ranges in order to the output range. Iterators increment for each
range. When the current element of one range is less than the other,
that iterator advances. If an element is contained in both ranges, the
element from the first range is copied and both ranges advance. The
output range may not overlap either input range.

##### Discussion

@brief Return the intersection of two sorted ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_intersection(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator, typename _Compare> _OutputIterator set_intersection(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result,
    _Compare __comp)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

**`comp`**
: The comparison functor.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
both ranges in order to the output range. Iterators increment for each
range. When the current element of one range is less than the other
according to @a comp, that iterator advances. If an element is
contained in both ranges according to @a comp, the element from the
first range is copied and both ranges advance. The output range may not
overlap either input range.

##### Discussion

@brief Return the intersection of two sorted ranges using comparison
functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator> _OutputIterator set_symmetric_difference(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
one range but not the other in order to the output range. Iterators
increment for each range. When the current element of one range is less
than the other, that element is copied and the iterator advances. If an
element is contained in both ranges, no elements are copied and both
ranges advance. The output range may not overlap either input range.

##### Discussion

@brief Return the symmetric difference of two sorted ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_symmetric_difference(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator, typename _Compare> _OutputIterator set_symmetric_difference(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result,
    _Compare __comp)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

**`comp`**
: The comparison functor.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
one range but not the other in order to the output range. Iterators
increment for each range. When the current element of one range is less
than the other according to @a comp, that element is copied and the
iterator advances. If an element is contained in both ranges according
to @a comp, no elements are copied and both ranges advance. The output
range may not overlap either input range.

##### Discussion

@brief Return the symmetric difference of two sorted ranges using
comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator> _OutputIterator set_union(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
each range in order to the output range. Iterators increment for each
range. When the current element of one range is less than the other,
that element is copied and the iterator advanced. If an element is
contained in both ranges, the element from the first range is copied and
both ranges advance. The output range may not overlap either input
range.

##### Discussion

@brief Return the union of two sorted ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) | set_union(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _OutputIterator, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator, typename _Compare> _OutputIterator set_union(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _OutputIterator __result,
    _Compare __comp)
```

##### Parameters

**`first1`**
: Start of first range.

**`last1`**
: End of first range.

**`first2`**
: Start of second range.

**`last2`**
: End of second range.

**`comp`**
: The comparison functor.

##### Return Value

End of the output range.
@ingroup setoperations

This operation iterates over both ranges, copying elements present in
each range in order to the output range. Iterators increment for each
range. When the current element of one range is less than the other
according to @a comp, that element is copied and the iterator advanced.
If an equivalent element according to @a comp is contained in both
ranges, the element from the first range is copied and both ranges
advance. The output range may not overlap either input range.

##### Discussion

@brief Return the union of two sorted ranges using a comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sort(_RandomAccessIterator, _RandomAccessIterator) | sort(_RandomAccessIterator, _RandomAccessIterator) | sort(_RandomAccessIterator, _RandomAccessIterator) | sort(_RandomAccessIterator, _RandomAccessIterator) | sort(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> inline void sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

##### Return Value

Nothing.

Sorts the elements in the range @p [first,last) in ascending order,
such that @p \*(i+1)<\*i is false for each iterator @p i in the range
@p [first,last-1).

The relative ordering of equivalent elements is not preserved, use
@p stable_sort() if this is needed.

##### Discussion

@brief Sort the elements of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> inline void sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`comp`**
: A comparison functor.

##### Return Value

Nothing.

Sorts the elements in the range @p [first,last) in ascending order,
such that @p comp(\*(i+1),\*i) is false for every iterator @p i in the
range @p [first,last-1).

The relative ordering of equivalent elements is not preserved, use
@p stable_sort() if this is needed.

##### Discussion

@brief Sort the elements of a sequence using a predicate for comparison.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| swap_ranges | swap_ranges | swap_ranges | swap_ranges | swap_ranges |

---

```
template<typename _ForwardIterator1, typename _ForwardIterator2> _ForwardIterator2 swap_ranges(
    _ForwardIterator1 __first1,
    _ForwardIterator1 __last1,
    _ForwardIterator2 __first2)
```

##### Parameters

**`first1`**
: A forward iterator.

**`last1`**
: A forward iterator.

**`first2`**
: A forward iterator.

##### Return Value

An iterator equal to @p first2+(last1-first1).

Swaps each element in the range @p [first1,last1) with the
corresponding element in the range @p [first2,(last1-first1)).
The ranges must not overlap.

##### Discussion

@brief Swap the elements of two sequences.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| transform(_InputIterator, _InputIterator, _OutputIterator, _UnaryOperation) | transform(_InputIterator, _InputIterator, _OutputIterator, _UnaryOperation) | transform(_InputIterator, _InputIterator, _OutputIterator, _UnaryOperation) | transform(_InputIterator, _InputIterator, _OutputIterator, _UnaryOperation) | transform(_InputIterator, _InputIterator, _OutputIterator, _UnaryOperation) |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _UnaryOperation> _OutputIterator transform(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _UnaryOperation __unary_op)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`result`**
: An output iterator.

**`unary_op`**
: A unary operator.

##### Return Value

An output iterator equal to @p result+(last-first).

Applies the operator to each element in the input range and assigns
the results to successive elements of the output sequence.
Evaluates @p \*(result+N)=unary_op(\*(first+N)) for each @c N in the
range @p [0,last-first).

@p unary_op must not alter its argument.

##### Discussion

@brief Perform an operation on a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| transform(_InputIterator1, _InputIterator1, _InputIterator2, _OutputIterator, _BinaryOperation) | transform(_InputIterator1, _InputIterator1, _InputIterator2, _OutputIterator, _BinaryOperation) | transform(_InputIterator1, _InputIterator1, _InputIterator2, _OutputIterator, _BinaryOperation) | transform(_InputIterator1, _InputIterator1, _InputIterator2, _OutputIterator, _BinaryOperation) | transform(_InputIterator1, _InputIterator1, _InputIterator2, _OutputIterator, _BinaryOperation) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _OutputIterator, typename _BinaryOperation> _OutputIterator transform(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _OutputIterator __result,
    _BinaryOperation __binary_op)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`first2`**
: An input iterator.

**`result`**
: An output iterator.

**`binary_op`**
: A binary operator.

##### Return Value

An output iterator equal to @p result+(last-first).

Applies the operator to the corresponding elements in the two
input ranges and assigns the results to successive elements of the
output sequence.
Evaluates @p \*(result+N)=binary_op(\*(first1+N),\*(first2+N)) for each
@c N in the range @p [0,last1-first1).

@p binary_op must not alter either of its arguments.

##### Discussion

@brief Perform an operation on corresponding elements of two sequences.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| unique(_ForwardIterator, _ForwardIterator) | unique(_ForwardIterator, _ForwardIterator) | unique(_ForwardIterator, _ForwardIterator) | unique(_ForwardIterator, _ForwardIterator) | unique(_ForwardIterator, _ForwardIterator) |

---

```
template<typename _ForwardIterator> _ForwardIterator unique(
    _ForwardIterator __first,
    _ForwardIterator __last)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

##### Return Value

An iterator designating the end of the resulting sequence.

Removes all but the first element from each group of consecutive
values that compare equal.
unique() is stable, so the relative order of elements that are
not removed is unchanged.
Elements between the end of the resulting sequence and @p last
are still present, but their value is unspecified.

##### Discussion

@brief Remove consecutive duplicate values from a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| unique(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | unique(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | unique(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | unique(_ForwardIterator, _ForwardIterator, _BinaryPredicate) | unique(_ForwardIterator, _ForwardIterator, _BinaryPredicate) |

---

```
template<typename _ForwardIterator, typename _BinaryPredicate> _ForwardIterator unique(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _BinaryPredicate __binary_pred)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`binary_pred`**
: A binary predicate.

##### Return Value

An iterator designating the end of the resulting sequence.

Removes all but the first element from each group of consecutive
values for which @p binary_pred returns true.
unique() is stable, so the relative order of elements that are
not removed is unchanged.
Elements between the end of the resulting sequence and @p last
are still present, but their value is unspecified.

##### Discussion

@brief Remove consecutive values from a sequence using a predicate.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &) |

---

```
template<typename _ForwardIterator, typename _Tp> _ForwardIterator upper_bound(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

##### Return Value

An iterator pointing to the first element greater than @a val,
or end() if no elements are greater than @a val.
@ingroup binarysearch

##### Discussion

@brief Finds the last position in which @a val could be inserted
without changing the ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) | upper_bound(_ForwardIterator, _ForwardIterator, const _Tp &, _Compare) |

---

```
template<typename _ForwardIterator, typename _Tp, typename _Compare> _ForwardIterator upper_bound(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __val,
    _Compare __comp)
```

##### Parameters

**`first`**
: An iterator.

**`last`**
: Another iterator.

**`val`**
: The search term.

**`comp`**
: A functor to use for comparisons.

##### Return Value

An iterator pointing to the first element greater than @a val,
or end() if no elements are greater than @a val.
@ingroup binarysearch

The comparison function should have the same effects on ordering as
the function used for the initial sort.

##### Discussion

@brief Finds the last position in which @a val could be inserted
without changing the ordering.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unguarded_insertion_sort | __unguarded_insertion_sort | __unguarded_insertion_sort | __unguarded_insertion_sort | __unguarded_insertion_sort |

---

```
template<typename _RandomAccessIterator> inline void __unguarded_insertion_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __unguarded_insertion_sort | __unguarded_insertion_sort | __unguarded_insertion_sort | __unguarded_insertion_sort | __unguarded_insertion_sort |

---

```
template<typename _RandomAccessIterator, typename _Compare> inline void __unguarded_insertion_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@if maint
This is a helper function for the sort routine.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| inplace_merge | inplace_merge | inplace_merge | inplace_merge | inplace_merge |

---

```
template<typename _BidirectionalIterator> void inplace_merge(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last)
```

##### Discussion

@brief Merges two sorted ranges in place.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| inplace_merge | inplace_merge | inplace_merge | inplace_merge | inplace_merge |

---

```
template<typename _BidirectionalIterator, typename _Compare> void inplace_merge(
    _BidirectionalIterator __first,
    _BidirectionalIterator __middle,
    _BidirectionalIterator __last,
    _Compare __comp)
```

##### Discussion

@brief Merges two sorted ranges in place.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partial_sort | partial_sort | partial_sort | partial_sort | partial_sort |

---

```
template<typename _RandomAccessIterator> void partial_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __middle,
    _RandomAccessIterator __last)
```

##### Discussion

@brief Sort the smallest elements of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partial_sort | partial_sort | partial_sort | partial_sort | partial_sort |

---

```
template<typename _RandomAccessIterator, typename _Compare> void partial_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __middle,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@brief Sort the smallest elements of a sequence using a predicate
for comparison.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| rotate | rotate | rotate | rotate | rotate |

---

```
template<typename _ForwardIterator> inline void rotate(
    _ForwardIterator __first,
    _ForwardIterator __middle,
    _ForwardIterator __last)
```

##### Discussion

@brief Rotate the elements of a sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stable_partition | stable_partition | stable_partition | stable_partition | stable_partition |

---

```
template<typename _ForwardIterator, typename _Predicate> _ForwardIterator stable_partition(
    _ForwardIterator __first,
    _ForwardIterator __last,
    _Predicate __pred)
```

##### Discussion

@brief Move elements for which a predicate is true to the beginning
of a sequence, preserving relative ordering.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stable_sort | stable_sort | stable_sort | stable_sort | stable_sort |

---

```
template<typename _RandomAccessIterator> inline void stable_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@brief Sort the elements of a sequence, preserving the relative order
of equivalent elements.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stable_sort | stable_sort | stable_sort | stable_sort | stable_sort |

---

```
template<typename _RandomAccessIterator, typename _Compare> inline void stable_sort(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@brief Sort the elements of a sequence using a predicate for comparison,
preserving the relative order of equivalent elements.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| unique_copy | unique_copy | unique_copy | unique_copy | unique_copy |

---

```
template<typename _InputIterator, typename _OutputIterator> inline _OutputIterator unique_copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result)
```

##### Discussion

@brief Copy a sequence, removing consecutive duplicate values.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| unique_copy | unique_copy | unique_copy | unique_copy | unique_copy |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _BinaryPredicate> inline _OutputIterator unique_copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _BinaryPredicate __binary_pred)
```

##### Discussion

@brief Copy a sequence, removing consecutive values using a predicate.

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
