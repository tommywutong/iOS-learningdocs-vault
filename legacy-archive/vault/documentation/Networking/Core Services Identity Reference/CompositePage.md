---
title: Core Services Identity Reference
apple_id: TP40004673
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2008-06-06'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/CSIdentity/CompositePage.html
archived_at: '2026-07-18T01:32:58.098957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Networking](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000429) __>__ Core Foundation __>__ [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5uwizlooruxi6i) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentity | CSIdentity | CSIdentity | CSIdentity | CSIdentity |

|  |  |
| --- | --- |
| __Framework:__ | /System/Library/Frameworks/CoreServices.framework/Frameworks/OSServices.framework |
| __See Also:__ | **[Identity Services Programming Guide](../Identity%20Services%20Programming%20Guide/Introduction%20to%20Identity%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojq)** :   **** : |
| __Includes:__ | <CoreFoundation.i>  <SecBase.i>  <Authorization.i>  [<CSIdentityAuthority.i>](https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/CSIdentityAuthority/index.html#//apple_ref/doc/header/CSIdentityAuthority.i) |

## Overview

A CSIdentity object represents a user or group entity known to the system. An
identity object has the following required attributes: a class (user
or group), a unique identitfier (UUID), a full name, a Posix ID
(UID or GID), and a Posix name (a.k.a. "short" name). There are also a number
of optional attributes such as email address, image data, etc.

Group identities have a membership which may include both users as well as
other groups. An identity can be tested for membership in a specific group.

A CSIdentity object is a private copy of the identity information. It can be
modified in memory, but requires authorization to commit changes back to
the identity authority database. On OS X version 10.5, only local identities
can be created, modified or deleted, and only by users with Administrator
credentials.

Changes may be committed synchronously or asynchronously. All data validation
occurs at commit time.

Two identities are CFEqual if they have the same class and UUID.

---

## Groups

### Permanent

> Deletion

#### Group members:

> **[CSIdentityDelete](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kemvwgk5df)**
> : Permanently delete an identity from the identity database

### Committing

> changes

#### Group members:

> **[CSIdentityCommit](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdn5ww22lu)**
> : Synchronously commit all pending changes to the identity authority database
>
> **[CSIdentityCommitAsynchronously](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdn5ww22luifzxs3tdnbzg63tpovzwy6i)**
> : Asychronously commit all pending changes to the identity authority's database
>
> **[CSIdentityIsCommitting](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjonbw63lnnf2hi2lom4)**
> : Determine if a commit operation is in progress
>
> **[CSIdentityRemoveClient](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfinwgszlooq)**
> : Invalidate an identity's client structure to stop client callbacks

### User

> Methods

#### Group members:

> **[CSIdentityAuthenticateUsingPassword](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gqzlooruwgylumvkxg2lom5igc43to5xxeza)**
> : Attempt to autenticate a password for a user identity
>
> **[CSIdentityGetCertificate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2egzlsoruwm2ldmf2gk)**
> : Get a user's authentication certificate
>
> **[CSIdentityIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjoncw4ylcnrswi)**
> : Determine if a user is enabled

### Group

> Methods

#### Group members:

> **[CSIdentityCreateGroupMembershipQuery](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfi5zg65lqjvsw2ytfojzwq2lqkf2wk4tz)**
> : Creates a query to find a group's members

### Getting

> Identity Attributes

#### Group members:

> **[CSIdentityCreatePersistentReference](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfkbsxe43jon2gk3tukjswmzlsmvxggzi)**
> : Create an opaque, persistent data reference to an identity
>
> **[CSIdentityGetAliases](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ec3djmfzwk4y)**
> : Retrieve the aliases of an identity.
>
> **[CSIdentityGetAuthority](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ec5lunbxxe2lupe)**
> : Returns the identity authority of an identity
>
> **[CSIdentityGetClass](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2eg3dbonzq)**
> : Returns an identity's class
>
> **[CSIdentityGetEmailAddress](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ek3lbnfweczdeojsxg4y)**
> : Retrieve the email address of a user identity
>
> **[CSIdentityGetFullName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2em5lmnrhgc3lf)**
> : Retrieve the full name of an identity
>
> **[CSIdentityGetImageData](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5suiylume)**
> : Retrieve the image associated with a user identity
>
> **[CSIdentityGetImageDataType](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5suiylumfkhs4df)**
> : Retrieve the uniform type identifier (UTI) of an identity's image
>
> **[CSIdentityGetImageURL](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5svkusm)**
> : Retrieve the URL to an identity's image file
>
> **[CSIdentityGetPosixID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fa33tnf4esra)**
> : Retrieve POSIX ID of an identity.
>
> **[CSIdentityGetPosixName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fa33tnf4e4ylnmu)**
> : Retrieve the POSIX name (short name) of an identity.
>
> **[CSIdentityGetUUID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fkvkjiq)**
> : Returns an identity's UUID.
>
> **[CSIdentityIsHidden](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjonegszdemvxa)**
> : Determine if a identity's hidden attribute is enabled
>
> **[CSIdentityIsMemberOfGroup](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjongwk3lcmvze6zshojxxk4a)**
> : Check if an identity is a memeber of a group

### Modifying

> group membership

#### Group members:

> **[CSIdentityAddAlias](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbmrsec3djmfzq)**
> : Add a name alias to an identity
>
> **[CSIdentityAddMember](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbmrse2zlnmjsxe)**
> : Add an identity to a group
>
> **[CSIdentityRemoveAlias](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfifwgsylt)**
> : Remove an alias name from an identity
>
> **[CSIdentityRemoveMember](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfjvsw2ytfoi)**
> : Remove a member from a group
>
> **[CSIdentitySetCertificate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2egzlsoruwm2ldmf2gk)**
> : Set a user's authentication certificate
>
> **[CSIdentitySetEmailAddress](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2ek3lbnfweczdeojsxg4y)**
> : Set an identity's email address
>
> **[CSIdentitySetFullName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2em5lmnrhgc3lf)**
> : Sets an identity's full name.
>
> **[CSIdentitySetImageData](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es3lbm5suiylume)**
> : Set the internally-stored image data and data type for an identity
>
> **[CSIdentitySetImageURL](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es3lbm5svkusm)**
> : Set the URL of an identity's external image storage
>
> **[CSIdentitySetIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es42fnzqwe3dfmq)**
> : Enable or disable a user
>
> **[CSIdentitySetPassword](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2faylton3w64te)**
> : Set a user password

### Creating

> Identities

#### Group members:

> **[CSIdentityCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5df)**
> : Creates a new identity
>
> **[CSIdentityCreateCopy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfinxxa6i)**
> : Creates a copy of an identity

### Modifying user credentials

#### Group members:

> **[CSIdentitySetIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es42fnzqwe3dfmq)**
> : Enable or disable a user

---

## Functions

**[CSIdentityAddAlias](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbmrsec3djmfzq)**
: Add a name alias to an identity

**[CSIdentityAddMember](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbmrse2zlnmjsxe)**
: Add an identity to a group

**[CSIdentityAuthenticateUsingPassword](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gqzlooruwgylumvkxg2lom5igc43to5xxeza)**
: Attempt to autenticate a password for a user identity

**[CSIdentityCommit](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdn5ww22lu)**
: Synchronously commit all pending changes to the identity authority database

**[CSIdentityCommitAsynchronously](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdn5ww22luifzxs3tdnbzg63tpovzwy6i)**
: Asychronously commit all pending changes to the identity authority's database

**[CSIdentityCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5df)**
: Creates a new identity

**[CSIdentityCreateCopy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfinxxa6i)**
: Creates a copy of an identity

**[CSIdentityCreateGroupMembershipQuery](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfi5zg65lqjvsw2ytfojzwq2lqkf2wk4tz)**
: Creates a query to find a group's members

**[CSIdentityCreatePersistentReference](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfkbsxe43jon2gk3tukjswmzlsmvxggzi)**
: Create an opaque, persistent data reference to an identity

**[CSIdentityDelete](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kemvwgk5df)**
: Permanently delete an identity from the identity database

**[CSIdentityGetAliases](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ec3djmfzwk4y)**
: Retrieve the aliases of an identity.

**[CSIdentityGetAuthority](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ec5lunbxxe2lupe)**
: Returns the identity authority of an identity

**[CSIdentityGetCertificate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2egzlsoruwm2ldmf2gk)**
: Get a user's authentication certificate

**[CSIdentityGetClass](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2eg3dbonzq)**
: Returns an identity's class

**[CSIdentityGetEmailAddress](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ek3lbnfweczdeojsxg4y)**
: Retrieve the email address of a user identity

**[CSIdentityGetFullName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2em5lmnrhgc3lf)**
: Retrieve the full name of an identity

**[CSIdentityGetImageData](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5suiylume)**
: Retrieve the image associated with a user identity

**[CSIdentityGetImageDataType](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5suiylumfkhs4df)**
: Retrieve the uniform type identifier (UTI) of an identity's image

**[CSIdentityGetImageURL](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5svkusm)**
: Retrieve the URL to an identity's image file

**[CSIdentityGetPosixID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fa33tnf4esra)**
: Retrieve POSIX ID of an identity.

**[CSIdentityGetPosixName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fa33tnf4e4ylnmu)**
: Retrieve the POSIX name (short name) of an identity.

**[CSIdentityGetTypeID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fi6lqmveui)**
: Returns the CSIdentity type identifier

**[CSIdentityGetUUID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fkvkjiq)**
: Returns an identity's UUID.

**[CSIdentityIsCommitting](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjonbw63lnnf2hi2lom4)**
: Determine if a commit operation is in progress

**[CSIdentityIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjoncw4ylcnrswi)**
: Determine if a user is enabled

**[CSIdentityIsHidden](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjonegszdemvxa)**
: Determine if a identity's hidden attribute is enabled

**[CSIdentityIsMemberOfGroup](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjongwk3lcmvze6zshojxxk4a)**
: Check if an identity is a memeber of a group

**[CSIdentityRemoveAlias](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfifwgsylt)**
: Remove an alias name from an identity

**[CSIdentityRemoveClient](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfinwgszlooq)**
: Invalidate an identity's client structure to stop client callbacks

**[CSIdentityRemoveMember](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfjvsw2ytfoi)**
: Remove a member from a group

**[CSIdentitySetCertificate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2egzlsoruwm2ldmf2gk)**
: Set a user's authentication certificate

**[CSIdentitySetEmailAddress](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2ek3lbnfweczdeojsxg4y)**
: Set an identity's email address

**[CSIdentitySetFullName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2em5lmnrhgc3lf)**
: Sets an identity's full name.

**[CSIdentitySetImageData](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es3lbm5suiylume)**
: Set the internally-stored image data and data type for an identity

**[CSIdentitySetImageURL](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es3lbm5svkusm)**
: Set the URL of an identity's external image storage

**[CSIdentitySetIsEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es42fnzqwe3dfmq)**
: Enable or disable a user

**[CSIdentitySetPassword](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2faylton3w64te)**
: Set a user password

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAddAlias | CSIdentityAddAlias | CSIdentityAddAlias | CSIdentityAddAlias | CSIdentityAddAlias |

---

Add a name alias to an identity

```
extern void CSIdentityAddAlias(
    CSIdentityRef identity,
    CFStringRef alias );
```

##### Parameters

**`identity`**
: The identity to access

**`alias`**
: The alias to add

##### Discussion

This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAddMember | CSIdentityAddMember | CSIdentityAddMember | CSIdentityAddMember | CSIdentityAddMember |

---

Add an identity to a group

```
extern void CSIdentityAddMember(
    CSIdentityRef group,
    CSIdentityRef member );
```

##### Parameters

**`group`**
: The group identity to access

**`member`**
: The identity to add to the group. Can be a user or group identity.

##### Discussion

This change to the group must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityAuthenticateUsingPassword | CSIdentityAuthenticateUsingPassword | CSIdentityAuthenticateUsingPassword | CSIdentityAuthenticateUsingPassword | CSIdentityAuthenticateUsingPassword |

---

Attempt to autenticate a password for a user identity

```
extern Boolean CSIdentityAuthenticateUsingPassword(
    CSIdentityRef user,
    CFStringRef password );
```

##### Parameters

**`user`**
: The user identity to access

**`password`**
: The password to authenticate

##### Return Value

Returns true if the passord is correct for the specified user

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityCommit | CSIdentityCommit | CSIdentityCommit | CSIdentityCommit | CSIdentityCommit |

---

Synchronously commit all pending changes to the identity authority database

```
extern Boolean CSIdentityCommit(
    CSIdentityRef identity,
    AuthorizationRef authorization,
    CFErrorRef *error );
```

##### Parameters

**`identity`**
: The identity to commit

**`authorization`**
: The authorization object holding credentials necessary to allow modification to the identity database. As a convenience,
callers may pass NULL for the authorization, and the implmentation will attempt to acquire the necessary credentials from
Authorization Services.

**`error`**
: Optional pointer to a CFErrorRef which will be set if this function returns false. When this occurs,
the caller is responsible for releasing the error.

##### Return Value

Returns true if successful, false if an error occurred

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityCommitAsynchronously | CSIdentityCommitAsynchronously | CSIdentityCommitAsynchronously | CSIdentityCommitAsynchronously | CSIdentityCommitAsynchronously |

---

Asychronously commit all pending changes to the identity authority's database

```
extern Boolean CSIdentityCommitAsynchronously(
    CSIdentityRef identity,
    const CSIdentityClientContext *clientContext,
    CFRunLoopRef runLoop,
    CFStringRef runLoopMode,
    AuthorizationRef authorization );
```

##### Parameters

**`identity`**
: The identity to commit

**`clientContext`**
: The client structure specifying context and callbacks for the asynchronous operation

**`runLoop`**
: The run loop on which to schedule the statusUpdated callback

**`runLoopMode`**
: The run loop mode in which the callback can be scheduled

**`authorization`**
: The authorization object holding credentials necessary to allow modification to the identity database. As a convenience,
callers may pass NULL for the authorization, and the implmentation will attempt to acquire the necessary credentials from
Authorization Services. Modifying the local system identity database requires Admin credentials.

##### Return Value

Returns true if the commit operation is started, indicated that an statusUpdated callback will follow.
Returns false if the identity has no uncommitted changes or a commit is already in progress

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityCreate | CSIdentityCreate | CSIdentityCreate | CSIdentityCreate | CSIdentityCreate |

---

Creates a new identity

```
extern CSIdentityRef CSIdentityCreate(
    CFAllocatorRef allocator,
    CSIdentityClass identityClass,
    CFStringRef fullName,
    CFStringRef posixName,
    CSIdentityFlags flags,
    CSIdentityAuthorityRef authority );
```

##### Parameters

**`allocator`**
: The allocator to use when creating the object. NULL is equivalent to specifying kCFAllocatorDefault.

**`identityClass`**
: The type of identity to be created. Specifying kCSIdentityClassUser creates a user, while kCSIdentityClassGroup creates a group.

**`fullName`**
: The primary name of the new identity.

**`posixName`**
: The POSIX name of the new identity. Specify kCSIdentityGeneratePosixName to have a name generated autmatically from the full name.

**`flags`**
: A CSIdentityFlags mask defining attributes of the new identity

**`authority`**
: The identity authority to host the identity. Caller must have write access to the identity authority or commit will fail.
Currently, only local identities may be created, so callers must specify the local identity authority for this argument.

##### Return Value

The CSIdentityRef of the newly created identity object. Returns NULL only if allocation fails.

##### Discussion

The new identity is allocated but is not committed to the identity authority's database. It will become persistent
and available to other clients after being committed using CSIdentityCommit or CSIdentityCommitAsynchronously.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityCreateCopy | CSIdentityCreateCopy | CSIdentityCreateCopy | CSIdentityCreateCopy | CSIdentityCreateCopy |

---

Creates a copy of an identity

```
extern CSIdentityRef CSIdentityCreateCopy(
    CFAllocatorRef allocator,
    CSIdentityRef identity );
```

##### Parameters

**`allocator`**
: The allocator to use for the new identity. NULL is equivalent to specifying kCFAllocatorDefault.

**`identity`**
: The identity to copy

##### Return Value

The CSIdentityRef of the newly created identity object

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityCreateGroupMembershipQuery | CSIdentityCreateGroupMembershipQuery | CSIdentityCreateGroupMembershipQuery | CSIdentityCreateGroupMembershipQuery | CSIdentityCreateGroupMembershipQuery |

---

Creates a query to find a group's members

```
extern CSIdentityQueryRef CSIdentityCreateGroupMembershipQuery(
    CFAllocatorRef allocator,
    CSIdentityRef group );
```

##### Parameters

**`allocator`**
: The allocator to use for the query

**`group`**
: The group identity whose members are to be queried

##### Return Value

The CSIdentityQueryRef of the newly created object. The query is ready to be executed.

##### Discussion

Using a query to lookup group membership allows the caller to execute the query synchronously or asynchronously.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityCreatePersistentReference | CSIdentityCreatePersistentReference | CSIdentityCreatePersistentReference | CSIdentityCreatePersistentReference | CSIdentityCreatePersistentReference |

---

Create an opaque, persistent data reference to an identity

```
extern CFDataRef CSIdentityCreatePersistentReference(
    CFAllocatorRef allocator,
    CSIdentityRef identity );
```

##### Parameters

**`allocator`**
: The allocator for the data

**`identity`**
: The identity to reference

##### Return Value

Returns a new persistent reference for the identity

##### Discussion

A persistent identity reference is an opaque data object from which an identity object
may queried the future (see CSIdentityQueryCreateForPersistentReference).
A persistent reference is suitable for storage in an external data store, for example, as an entry in an
application-specific access control list associated with a shared resource. Use of a persistent identity
reference is preferred over a pure UUID-based identity reference because the persistent reference contains
additional information needed to optimize the identity query and to improve the user experience when
working in a distributed identity environment (LDAP, Active Directory, etc.).

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityDelete | CSIdentityDelete | CSIdentityDelete | CSIdentityDelete | CSIdentityDelete |

---

Permanently delete an identity from the identity database

```
extern void CSIdentityDelete(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to delete

##### Discussion

Sets an identity to deleted state. This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetAliases | CSIdentityGetAliases | CSIdentityGetAliases | CSIdentityGetAliases | CSIdentityGetAliases |

---

Retrieve the aliases of an identity.

```
extern CFArrayRef CSIdentityGetAliases(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns an array containing the identity's name aliases as CFStringRefs. The array may be empty. The identity object may release its reference to
the return value when the identity is modified.

##### Discussion

Aliases are alternate names for identities. As with all identity names,
aliases must be unique within the entire namespace of of the identity authority.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetAuthority | CSIdentityGetAuthority | CSIdentityGetAuthority | CSIdentityGetAuthority | CSIdentityGetAuthority |

---

Returns the identity authority of an identity

```
extern CSIdentityAuthorityRef CSIdentityGetAuthority(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity object to access

##### Return Value

A CSIdentityAuthorityRef object

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetCertificate | CSIdentityGetCertificate | CSIdentityGetCertificate | CSIdentityGetCertificate | CSIdentityGetCertificate |

---

Get a user's authentication certificate

```
extern SecCertificateRef CSIdentityGetCertificate(
    CSIdentityRef user );
```

##### Parameters

**`user`**
: The user identity to access

##### Return Value

The identity's certificate, or NULL if there is no certificate. The identity object may release its reference to
the return value when the identity is modified.

##### Discussion

The authentication certificate can be used in PKI-based protocols to authenticate users.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetClass | CSIdentityGetClass | CSIdentityGetClass | CSIdentityGetClass | CSIdentityGetClass |

---

Returns an identity's class

```
extern CSIdentityClass CSIdentityGetClass(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity object to access

##### Return Value

The CSIdentityClass of an identity

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetEmailAddress | CSIdentityGetEmailAddress | CSIdentityGetEmailAddress | CSIdentityGetEmailAddress | CSIdentityGetEmailAddress |

---

Retrieve the email address of a user identity

```
extern CFStringRef CSIdentityGetEmailAddress(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns the email address of the identity or NULL if there is no email address. The identity object may release its reference to
the return value when the identity is modified.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetFullName | CSIdentityGetFullName | CSIdentityGetFullName | CSIdentityGetFullName | CSIdentityGetFullName |

---

Retrieve the full name of an identity

```
extern CFStringRef CSIdentityGetFullName(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity object to access

##### Return Value

Returns an identity's full name as a CFStringRef. This attribute is always non-NULL. The identity object may release its reference to
the return value when the identity is modified.

##### Discussion

The full name is the name that is displayed in the user interface.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetImageData | CSIdentityGetImageData | CSIdentityGetImageData | CSIdentityGetImageData | CSIdentityGetImageData |

---

Retrieve the image associated with a user identity

```
extern CFDataRef CSIdentityGetImageData(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns the identity's image data as a CFDataRef or NULL if there is no image data. The identity object may release its reference to
the return value when the identity is modified.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetImageDataType | CSIdentityGetImageDataType | CSIdentityGetImageDataType | CSIdentityGetImageDataType | CSIdentityGetImageDataType |

---

Retrieve the uniform type identifier (UTI) of an identity's image

```
extern CFStringRef CSIdentityGetImageDataType(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns a UTI as a CFStringRef for this identity's image data or NULL if there is no image data. The identity object may release its reference to
the return value when the identity is modified.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetImageURL | CSIdentityGetImageURL | CSIdentityGetImageURL | CSIdentityGetImageURL | CSIdentityGetImageURL |

---

Retrieve the URL to an identity's image file

```
extern CFURLRef CSIdentityGetImageURL(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns a CFURLRef that contains the location of the user's image file, or NULL if there is no image URL.
The identity object may release its reference to
the return value when the identity is modified.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetPosixID | CSIdentityGetPosixID | CSIdentityGetPosixID | CSIdentityGetPosixID | CSIdentityGetPosixID |

---

Retrieve POSIX ID of an identity.

```
extern id_t CSIdentityGetPosixID(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns an identity's POSIX identifier (a UID or GID).

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetPosixName | CSIdentityGetPosixName | CSIdentityGetPosixName | CSIdentityGetPosixName | CSIdentityGetPosixName |

---

Retrieve the POSIX name (short name) of an identity.

```
extern CFStringRef CSIdentityGetPosixName(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity object to access.

##### Return Value

Returns an identity's POSIX name. This attribute is always non-NULL. The identity object may release its reference to
the return value when the identity is modified.

##### Discussion

The POSIX name cannot be changed after an identity has been created.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetTypeID | CSIdentityGetTypeID | CSIdentityGetTypeID | CSIdentityGetTypeID | CSIdentityGetTypeID |

---

Returns the CSIdentity type identifier

```
extern CFTypeID CSIdentityGetTypeID(
    void );
```

##### Return Value

The CFTypeID of the CSIdentity Core Foundation type

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityGetUUID | CSIdentityGetUUID | CSIdentityGetUUID | CSIdentityGetUUID | CSIdentityGetUUID |

---

Returns an identity's UUID.

```
extern CFUUIDRef CSIdentityGetUUID(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity object to access

##### Return Value

A CFUUID object containing identity's UUID. Will never return NULL.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityIsCommitting | CSIdentityIsCommitting | CSIdentityIsCommitting | CSIdentityIsCommitting | CSIdentityIsCommitting |

---

Determine if a commit operation is in progress

```
extern Boolean CSIdentityIsCommitting(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Return Value

Returns true if a commit operation is in progress

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityIsEnabled | CSIdentityIsEnabled | CSIdentityIsEnabled | CSIdentityIsEnabled | CSIdentityIsEnabled |

---

Determine if a user is enabled

```
extern Boolean CSIdentityIsEnabled(
    CSIdentityRef user );
```

##### Parameters

**`user`**
: The user identity to access

##### Return Value

Returns true if the user is enabled. A user that is not enabled cannot authenticate.

##### Discussion

A user that is not enabled cannot authenticate. This setting may be used to temporarily allow a user's access to all services and resources.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityIsHidden | CSIdentityIsHidden | CSIdentityIsHidden | CSIdentityIsHidden | CSIdentityIsHidden |

---

Determine if a identity's hidden attribute is enabled

```
extern Boolean CSIdentityIsHidden(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity object to access

##### Return Value

Returns true if the identity was created with the hidden attribute

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityIsMemberOfGroup | CSIdentityIsMemberOfGroup | CSIdentityIsMemberOfGroup | CSIdentityIsMemberOfGroup | CSIdentityIsMemberOfGroup |

---

Check if an identity is a memeber of a group

```
extern Boolean CSIdentityIsMemberOfGroup(
    CSIdentityRef identity,
    CSIdentityRef group );
```

##### Parameters

**`identity`**
: The identity whose membership is in question

**`group`**
: The group identity whose membership is to be checked

##### Return Value

Returns true if the identity is a member (directly or indirectly) of the specified group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityRemoveAlias | CSIdentityRemoveAlias | CSIdentityRemoveAlias | CSIdentityRemoveAlias | CSIdentityRemoveAlias |

---

Remove an alias name from an identity

```
extern void CSIdentityRemoveAlias(
    CSIdentityRef identity,
    CFStringRef alias );
```

##### Parameters

**`identity`**
: The identity to access

**`alias`**
: The alias name to remove

##### Discussion

This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityRemoveClient | CSIdentityRemoveClient | CSIdentityRemoveClient | CSIdentityRemoveClient | CSIdentityRemoveClient |

---

Invalidate an identity's client structure to stop client callbacks

```
extern void CSIdentityRemoveClient(
    CSIdentityRef identity );
```

##### Parameters

**`identity`**
: The identity to access

##### Discussion

After returning, this function guarantees that client callbacks will never be invoked again.
Use this function when releasing an identity which may have an outstanding asynchronous request.
This function does not cancel an outstanding commit operation because a commit cannot be interrupted.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityRemoveMember | CSIdentityRemoveMember | CSIdentityRemoveMember | CSIdentityRemoveMember | CSIdentityRemoveMember |

---

Remove a member from a group

```
extern void CSIdentityRemoveMember(
    CSIdentityRef group,
    CSIdentityRef member );
```

##### Parameters

**`group`**
: The group identity to access

**`member`**
: The member identity to remove

##### Discussion

This change to the group must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetCertificate | CSIdentitySetCertificate | CSIdentitySetCertificate | CSIdentitySetCertificate | CSIdentitySetCertificate |

---

Set a user's authentication certificate

```
extern void CSIdentitySetCertificate(
    CSIdentityRef user,
    SecCertificateRef certificate );
```

##### Parameters

**`user`**
: The user identity to access

**`certificate`**
: The user's certificate, or NULL to remove the current certificate

##### Discussion

The subject name in the certificate will function as an alias for the identity. As with all
identity names, the subject name must be unique within the entire name space of the identity authority.
This change must be submitted.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetEmailAddress | CSIdentitySetEmailAddress | CSIdentitySetEmailAddress | CSIdentitySetEmailAddress | CSIdentitySetEmailAddress |

---

Set an identity's email address

```
extern void CSIdentitySetEmailAddress(
    CSIdentityRef identity,
    CFStringRef emailAddress );
```

##### Parameters

**`identity`**
: The user identity to access

**`emailAddress`**
: The user's new email address value. Pass NULL to remove an email address.

##### Discussion

This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetFullName | CSIdentitySetFullName | CSIdentitySetFullName | CSIdentitySetFullName | CSIdentitySetFullName |

---

Sets an identity's full name.

```
extern void CSIdentitySetFullName(
    CSIdentityRef identity,
    CFStringRef fullName );
```

##### Parameters

**`identity`**
: The identity object to access

**`fullName`**
: The new full name of the identity

##### Discussion

This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetImageData | CSIdentitySetImageData | CSIdentitySetImageData | CSIdentitySetImageData | CSIdentitySetImageData |

---

Set the internally-stored image data and data type for an identity

```
extern void CSIdentitySetImageData(
    CSIdentityRef identity,
    CFDataRef imageData,
    CFStringRef imageDataType );
```

##### Parameters

**`identity`**
: The identity to access

**`imageData`**
: The image data. Pass NULL to remove image data.

**`imageDataType`**
: The uniform type identitier (UTI) of the image data.
Currently, kUTTypeJPEG ("public.jpeg") is the only type supported.

##### Discussion

This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetImageURL | CSIdentitySetImageURL | CSIdentitySetImageURL | CSIdentitySetImageURL | CSIdentitySetImageURL |

---

Set the URL of an identity's external image storage

```
extern void CSIdentitySetImageURL(
    CSIdentityRef identity,
    CFURLRef url );
```

##### Parameters

**`identity`**
: The identity to access

**`url`**
: The URL file of the image. For local identities, this must be a file URL. Pass NULL to remove the image URL from the identity.

##### Discussion

This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetIsEnabled | CSIdentitySetIsEnabled | CSIdentitySetIsEnabled | CSIdentitySetIsEnabled | CSIdentitySetIsEnabled |

---

Enable or disable a user

```
 extern void CSIdentitySetIsEnabled(
    CSIdentityRef user,
    Boolean isEnabled );
```

##### Parameters

**`user`**
: The identity object to access

**`isEnabled`**
: The new value of the isEnabled attribute

##### Discussion

A disabled user account cannot authenticate. Credentials (password and certificate) are not affected.
This change must be committed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentitySetPassword | CSIdentitySetPassword | CSIdentitySetPassword | CSIdentitySetPassword | CSIdentitySetPassword |

---

Set a user password

```
extern void CSIdentitySetPassword(
    CSIdentityRef user,
    CFStringRef password );
```

##### Parameters

**`user`**
: The user identity to access

**`password`**
: The new password, or NULL to remove the current password and disable password-based authentication

##### Discussion

Setting the password to NULL removes the current password and disables password authentication for
the user. Setting the password to a zero-length string allows authentication with a blank password.
This change must be committed.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryRef | CSIdentityQueryRef | CSIdentityQueryRef | CSIdentityQueryRef | CSIdentityQueryRef |

---

```
typedef opaque CSIdentityQueryRef;
```

##### Discussion

A reference to an identity query object, used to lookup identities in an
identity authority's database.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityRef | CSIdentityRef | CSIdentityRef | CSIdentityRef | CSIdentityRef |

---

```
typedef opaque CSIdentityRef;
```

##### Discussion

A reference to an identity object. Can be either a user or group.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityClientContext | CSIdentityClientContext | CSIdentityClientContext | CSIdentityClientContext | CSIdentityClientContext |

---

```
struct CSIdentityClientContext {
    CFIndex version;
    void *info;
    CFAllocatorRetainCallBack retain;
    CFAllocatorReleaseCallBack release;
    CFAllocatorCopyDescriptionCallBack copyDescription;
    CSIdentityStatusUpdatedCallback statusUpdated;
};
```

##### Fields

> **`version`**
> : The version number of the client structure type. The current version number is 0.
>
> **`info`**
> : An arbitrary pointer to client-defined data, which can be associated with the client and is passed to the callbacks.
>
> **`retain`**
> : The callback used to add a retain for the on the client object for the life of the asynchronous operation,
> and may be used for temporary references the identity needs to take. This callback returns the actual info pointer
> to be passed to the statusUpdated callback. May be NULL.
>
> **`release`**
> : The callback used to remove a retain previously acquired for the client object. May be NULL.
>
> **`copyDescription`**
> : The callback used to create a descriptive string representation of the client object
> for debugging purposes. This is used by the CFCopyDescription() function. May be NULL.
>
> **`statusUpdated`**
> : The client callback invoked when the status of an asnchronous operation changes

##### Discussion

Structure containing the user-defined data and callbacks used during asynchronous commits

## Enumerations

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentity error codes | CSIdentity error codes | CSIdentity error codes | CSIdentity error codes | CSIdentity error codes |

---

```
enum {
    kCSIdentityUnknownAuthorityErr = -1,
    kCSIdentityAuthorityNotAccessibleErr = -2,
    kCSIdentityPermissionErr = -3,
    kCSIdentityDeletedErr = -4,
    kCSIdentityInvalidFullNameErr = -5,
    kCSIdentityDuplicateFullNameErr = -6,
    kCSIdentityInvalidPosixNameErr = -7,
    kCSIdentityDuplicatePosixNameErr = -8
};
```

##### Constants

> **`kCSIdentityUnknownAuthorityErr`**
> : The specified authority is not recognized
>
> **`kCSIdentityAuthorityNotAccessibleErr`**
> : The specified authority is currently not accessible
>
> **`kCSIdentityPermissionErr`**
> : The caller does not have permission to perform the operation
>
> **`kCSIdentityDeletedErr`**
> : The requested identity has been deteled
>
> **`kCSIdentityInvalidFullNameErr`**
> : The full name is not valid (length: [1-255])
>
> **`kCSIdentityDuplicateFullNameErr`**
> : The full name is aleady assigned to another identity
>
> **`kCSIdentityInvalidPosixNameErr`**
> : The Posix name is not valid (char set: [a-zA-Z0-9_-] length: [1-255])
>
> **`kCSIdentityDuplicatePosixNameErr`**
> : The Posix name is aleady assigned to another identity

##### Discussion

Error codes in the CSIdentity error domain

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityClass | CSIdentityClass | CSIdentityClass | CSIdentityClass | CSIdentityClass |

---

```
enum {
    kCSIdentityClassUser = 1,
    kCSIdentityClassGroup = 2
};
```

##### Constants

> **`kCSIdentityClassUser`**
> : The class value for user identities
>
> **`kCSIdentityClassGroup`**
> : The class value for group identities

##### Discussion

Enum specifying an identity class

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityFlags | CSIdentityFlags | CSIdentityFlags | CSIdentityFlags | CSIdentityFlags |

---

```
enum {
    kCSIdentityFlagNone = 0,
    kCSIdentityFlagHidden = 1
};
```

##### Constants

> **`kCSIdentityFlagNone`**
> : Use this flag to set no optional attributes for a new identity
>
> **`kCSIdentityFlagHidden`**
> : This flag causes the identity to be "hidden," that is, excluded from most user-visible
> identity lists. Hidden identities include administrative users and groups such as root, www, and mysql. System service access
> control groups should be created with the hidden flag.

##### Discussion

Flags used when creating new identities

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Status | Status | Status | Status | Status |

---

```
enum {
    kCSIdentityCommitCompleted = 1
};
```

##### Constants

> **`kCSIdentityCommitCompleted`**
> : The identity has been committed to the authority database

##### Discussion

values

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
