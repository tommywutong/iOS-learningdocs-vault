---
title: Core Services Identity Reference
apple_id: TP40004673
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2008-06-06'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/identity-functions.html
archived_at: '2026-07-15T08:18:35.830527Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md)


# Core Services Identity Reference

The Core Services Identity Reference allows developers to support user and group creation, enumeration, attribute inspection, credential management as well as group membership management in their applications.
| __Companion document__ | [Identity Services Programming Guide](../Identity%20Services%20Programming%20Guide/Introduction%20to%20Identity%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojq) |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  | | --- | | Functions |   |  |  |  | | --- | --- | --- | | [CSGetDefaultIdentityAuthority](CompositePage-2.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dkndwk5cemvtgc5lmorewizlooruxi6kbov2gq33snf2hs) |  | [CSIdentityGetUUID](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fkvkjiq) | | [CSGetLocalIdentityAuthority](CompositePage-2.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dkndwk5cmn5rwc3cjmrsw45djor4uc5lunbxxe2lupe) |  | [CSIdentityIsCommitting](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjonbw63lnnf2hi2lom4) | | [CSGetManagedIdentityAuthority](CompositePage-2.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dkndwk5cnmfxgcz3fmrewizlooruxi6kbov2gq33snf2hs) |  | [CSIdentityIsEnabled](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjoncw4ylcnrswi) | | [CSIdentityAddAlias](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbmrsec3djmfzq) |  | [CSIdentityIsHidden](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjonegszdemvxa) | | [CSIdentityAddMember](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbmrse2zlnmjsxe) |  | [CSIdentityIsMemberOfGroup](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kjongwk3lcmvze6zshojxxk4a) | | [CSIdentityAuthenticateUsingPassword](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gqzlooruwgylumvkxg2lom5igc43to5xxeza) |  | [CSIdentityQueryCopyResults](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdn5yhsutfon2wy5dt) | | [CSIdentityAuthorityCopyLocalizedName](CompositePage-2.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gq33snf2hsq3pob4uy33dmfwgs6tfmrhgc3lf) |  | [CSIdentityQueryCreate](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5df) | | [CSIdentityAuthorityGetTypeID](CompositePage-2.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kbov2gq33snf2hsr3forkhs4dfjfca) |  | [CSIdentityQueryCreateForCurrentUser](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxeq3vojzgk3tukvzwk4q) | | [CSIdentityCommit](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdn5ww22lu) |  | [CSIdentityQueryCreateForName](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxettbnvsq) | | [CSIdentityCommitAsynchronously](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdn5ww22luifzxs3tdnbzg63tpovzwy6i) |  | [CSIdentityQueryCreateForPersistentReference](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxeudfojzws43umvxhiutfmzsxezlomnsq) | | [CSIdentityCreate](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5df) |  | [CSIdentityQueryCreateForPosixID](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxeudponuxqske) | | [CSIdentityCreateCopy](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfinxxa6i) |  | [CSIdentityQueryCreateForUUID](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxevkvjfca) | | [CSIdentityCreateGroupMembershipQuery](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfi5zg65lqjvsw2ytfojzwq2lqkf2wk4tz) |  | [CSIdentityQueryExecute](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kfpbswg5lumu) | | [CSIdentityCreatePersistentReference](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kdojswc5dfkbsxe43jon2gk3tukjswmzlsmvxggzi) |  | [CSIdentityQueryExecuteAsynchronously](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kfpbswg5lumvaxg6lomnuhe33on52xg3dz) | | [CSIdentityDelete](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6kemvwgk5df) |  | [CSIdentityQueryGetTypeID](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6khmv2fi6lqmveui) | | [CSIdentityGetAliases](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ec3djmfzwk4y) |  | [CSIdentityQueryStop](CompositePage-3.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6ktorxxa) | | [CSIdentityGetAuthority](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ec5lunbxxe2lupe) |  | [CSIdentityRemoveAlias](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfifwgsylt) | | [CSIdentityGetCertificate](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2egzlsoruwm2ldmf2gk) |  | [CSIdentityRemoveClient](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfinwgszlooq) | | [CSIdentityGetClass](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2eg3dbonzq) |  | [CSIdentityRemoveMember](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ksmvww65tfjvsw2ytfoi) | | [CSIdentityGetEmailAddress](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2ek3lbnfweczdeojsxg4y) |  | [CSIdentitySetCertificate](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2egzlsoruwm2ldmf2gk) | | [CSIdentityGetFullName](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2em5lmnrhgc3lf) |  | [CSIdentitySetEmailAddress](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2ek3lbnfweczdeojsxg4y) | | [CSIdentityGetImageData](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5suiylume) |  | [CSIdentitySetFullName](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2em5lmnrhgc3lf) | | [CSIdentityGetImageDataType](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5suiylumfkhs4df) |  | [CSIdentitySetImageData](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es3lbm5suiylume) | | [CSIdentityGetImageURL](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2es3lbm5svkusm) |  | [CSIdentitySetImageURL](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es3lbm5svkusm) | | [CSIdentityGetPosixID](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fa33tnf4esra) |  | [CSIdentitySetIsEnabled](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2es42fnzqwe3dfmq) | | [CSIdentityGetPosixName](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fa33tnf4e4ylnmu) |  | [CSIdentitySetPassword](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6ktmv2faylton3w64te) | | [CSIdentityGetTypeID](CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6khmv2fi6lqmveui) |  |  | | |  | | --- | | Other References |   |  | | --- | | [Header Index](Core%20Services%20Identity%20Reference.md) | | [Data Types Index](Core%20Services%20Identity%20Reference-2.md) | | |

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
