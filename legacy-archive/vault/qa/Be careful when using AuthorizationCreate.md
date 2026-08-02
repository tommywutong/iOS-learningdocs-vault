---
title: Be careful when using AuthorizationCreate
apple_id: DTS10001704
resource_type: QA
platform: macOS
topic: Security
technology: Security
published: '2011-07-26'
source_url: https://developer.apple.com/library/archive/qa/qa1172/_index.html
archived_at: '2026-07-18T02:30:11.996401Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1172

# Be careful when using AuthorizationCreate

## Q:  Is it possible to use `AuthorizationCreate` to create an `AuthorizationRef`, and at the same time, extend the currently authorized rights, all in one step?

A: Yes, this is possible, but you must be careful. If the request for authorization is denied, or the authorization fails for some other reason, the `AuthorizationRef` doesn't actually get created, so using it in subsequent calls will fail.

A better approach is to use `AuthorizationCreate` and pass `NULL` as the initial `AuthorizationRights` set so that the `AuthorizationRef` gets created successfully, and then later call `AuthorizationCopyRights` to determine or extend the allowable rights. Listing 1 illustrates this.

__Listing 1__  Recommended way to use AuthorizationCreate.

```
OSStatus status; AuthorizationRef authorizationRef; AuthorizationItem right = { "com.mycompany.myapplication.command1", 0, NULL, 0 }; AuthorizationRights rightSet = { 1, &right };AuthorizationFlags flags =      kAuthorizationFlagExtendRights |     kAuthorizationFlagInteractionAllowed;  /* Create a new AuthorizationRef object, but pass in NULL for the AuthorizationRights set so the AuthorizationRef can be used in future calls. */  status = AuthorizationCreate(NULL, kAuthorizationEmptyEnvironment,     kAuthorizationFlagDefaults, &authorizationRef); if (status == errAuthorizationSuccess) {     /* Now we can use the AuthorizationRef to deterimine if the user is     allowed to perform the rights contained in "rightSet". */      status = AuthorizationCopyRights(authorizationRef, &rightSet,         kAuthorizationEmptyEnvironment, flags, NULL); }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-26 | Reformatted content and made minor editorial changes. |
| 2002-09-20 | New document that explains why you should avoid determining allowable rights when creating an AuthorizationRef. |

