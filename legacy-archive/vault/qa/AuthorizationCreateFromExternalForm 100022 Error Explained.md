---
title: AuthorizationCreateFromExternalForm 100022 Error Explained
apple_id: DTS10004156
resource_type: QA
platform: macOS
topic: Security
technology: Security
published: '2007-01-04'
source_url: https://developer.apple.com/library/archive/qa/qa1498/_index.html
archived_at: '2026-07-18T02:31:37.943920Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1498

# AuthorizationCreateFromExternalForm 100022 Error Explained

## Q:  What does the return value of 100022 mean after I call `AuthorizationCreateFromExternalForm`?

A: What does the return value of 100022 mean after I call `AuthorizationCreateFromExternalForm`?

Authorization Services routines can return unexpected errors (explained in detail in [Technical Q&A QA1499, 'Security Framework Error Codes'](https://developer.apple.com/qa/qa2006/qa1499.html)). In this case, the error is `EINVAL (22) + 100000`.

If you receive this return value from `AuthorizationCreateFromExternalForm` it means that the `AuthorizationRef` from which the `AuthorizationExternalForm` was created is no longer valid. Typically this is because the process associated with that `AuthorizationRef` has quit.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-01-04 | New document that explains the undocumented 100022 return value from AuthorizationCreateFromExternalForm. |

