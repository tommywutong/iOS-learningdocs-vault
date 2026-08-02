---
title: Core Services Identity Reference
apple_id: TP40004673
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2008-06-06'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/CSIdentityAuthority/CompositePage.html
archived_at: '2026-07-18T01:32:58.412039Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Networking](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000429) __>__ Core Foundation __>__ [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5uwizlooruxi6i) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAuthority | CSIdentityAuthority | CSIdentityAuthority | CSIdentityAuthority | CSIdentityAuthority |

|  |  |
| --- | --- |
| __Framework:__ | /System/Library/Frameworks/CoreServices.framework/Frameworks/OSServices.framework |
| __See Also:__ | **[Identity Services Programming Guide](../Identity%20Services%20Programming%20Guide/Introduction%20to%20Identity%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojq)** :   **** : |
| __Includes:__ | <CoreFoundation.i> |

## Overview

A CSIdentityAuthority object represents an identity authority. An identity authority is a
logical repository of user and group information, such the users and groups database on a
local system or on a directory server.

The local authority contains all users and groups defined on the local system. The managed
authority contains all users and groups defined in directory servers to which the system is
bound (LDAP, ActiveDirectory, etc.). The Default authority is a union of the local and
managed authorities and is used to locate user/group info from both sources in one query.

Use one of the class factory methods to return an CSIdentityAuthority object, which can be
used to search for an identity with an CSIdentityQuery object

---

## Functions

**[CSGetDefaultIdentityAuthority](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dkndwk5cemvtgc5lmorewizlooruxi6kbov2gq33snf2hs)**
: Returns the system's default identity authority

**[CSGetLocalIdentityAuthority](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dkndwk5cmn5rwc3cjmrsw45djor4uc5lunbxxe2lupe)**
: Returns the identity authority for identities defined on the local host

**[CSGetManagedIdentityAuthority](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dkndwk5cnmfxgcz3fmrewizlooruxi6kbov2gq33snf2hs)**
: Returns the identity authority for identities defined in the system's managed directory server(s)

**[CSIdentityAuthorityCopyLocalizedName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gq33snf2hsq3pob4uy33dmfwgs6tfmrhgc3lf)**
: Returns the localized name of an identity authority

**[CSIdentityAuthorityGetTypeID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gq33snf2hsr3forkhs4dfjfca)**
: Returns the CSIdentityAuthority type identifier

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSGetDefaultIdentityAuthority | CSGetDefaultIdentityAuthority | CSGetDefaultIdentityAuthority | CSGetDefaultIdentityAuthority | CSGetDefaultIdentityAuthority |

---

Returns the system's default identity authority

```
extern CSIdentityAuthorityRef CSGetDefaultIdentityAuthority(
    void );
```

##### Return Value

The CSIdentityAuthorityRef of the default authority

##### Discussion

The default identity authority is a pseudo-authority representing
the union of the local identity authority and the managed identity
authority. The function CSIdentityGetAuthority will never return
the default authority instance.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSGetLocalIdentityAuthority | CSGetLocalIdentityAuthority | CSGetLocalIdentityAuthority | CSGetLocalIdentityAuthority | CSGetLocalIdentityAuthority |

---

Returns the identity authority for identities defined on the local host

```
extern CSIdentityAuthorityRef CSGetLocalIdentityAuthority(
    void );
```

##### Return Value

The CSIdentityAuthorityRef of the local authority

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSGetManagedIdentityAuthority | CSGetManagedIdentityAuthority | CSGetManagedIdentityAuthority | CSGetManagedIdentityAuthority | CSGetManagedIdentityAuthority |

---

Returns the identity authority for identities defined in the system's managed directory server(s)

```
extern CSIdentityAuthorityRef CSGetManagedIdentityAuthority(
    void );
```

##### Return Value

The CSIdentityAuthorityRef of the managed authority

##### Discussion

There is always a valid managed identity authority instance, but if the system is
not bound to any managed directory servers, the managed identity authority will contain
no identities.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAuthorityCopyLocalizedName | CSIdentityAuthorityCopyLocalizedName | CSIdentityAuthorityCopyLocalizedName | CSIdentityAuthorityCopyLocalizedName | CSIdentityAuthorityCopyLocalizedName |

---

Returns the localized name of an identity authority

```
extern CFStringRef CSIdentityAuthorityCopyLocalizedName(
    CSIdentityAuthorityRef authority );
```

##### Parameters

**`authority`**
: The identity authority to access

##### Return Value

A CFStringRef containing the localized authority name

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAuthorityGetTypeID | CSIdentityAuthorityGetTypeID | CSIdentityAuthorityGetTypeID | CSIdentityAuthorityGetTypeID | CSIdentityAuthorityGetTypeID |

---

Returns the CSIdentityAuthority type identifier

```
extern CFTypeID CSIdentityAuthorityGetTypeID(
    void );
```

##### Return Value

The CFTypeID of the CSIdentityAuthority Core Foundation type

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAuthorityRef | CSIdentityAuthorityRef | CSIdentityAuthorityRef | CSIdentityAuthorityRef | CSIdentityAuthorityRef |

---

```
typedef opaque <structname=__CSIdentityAuthority> CSIdentityAuthorityRef;
```

##### Discussion

A reference to an identity authority object. An identity authority is a logical
repository for identities.

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

Last Updated: 2008-03-11
