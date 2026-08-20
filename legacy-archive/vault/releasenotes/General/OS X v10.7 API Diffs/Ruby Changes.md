---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Ruby.html
archived_at: '2026-07-18T02:54:38.997914Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Ruby Changes

## Ruby

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

defines.hRemoved #def WORDS_BIGENDIANintern.hAdded rb_mark_set()Modified ruby_stack_length()

|  | Declaration |
| --- | --- |
| From | int ruby_stack_length ( VALUE \*\*); |
| To | size_t ruby_stack_length ( VALUE \*\*); |

re.hAdded #def RMATCH_REGSruby.hRemoved #def RUBY_THREADSWITCH_FREERemoved #def RUBY_THREADSWITCH_INITRemoved #def RUBY_THREADSWITCH_RESTORERemoved #def RUBY_THREADSWITCH_SAVERemoved rb_add_threadswitch_hook()Removed rb_remove_threadswitch_hook()Removed rb_threadswitch_event_tRemoved rb_threadswitch_hook_func_tAdded #def RBIGNUM_DIGITSAdded #def RBIGNUM_LENAdded #def RBIGNUM_NEGATIVE_PAdded #def RBIGNUM_POSITIVE_PAdded #def RBIGNUM_SET_SIGNAdded #def RBIGNUM_SIGNAdded #def RFLOAT_VALUEAdded #def RREGEXP_SRC_LENAdded #def RREGEXP_SRC_PTRAdded #def RSTRING_ENDrubysig.hModified rb_thread_pending

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

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

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
