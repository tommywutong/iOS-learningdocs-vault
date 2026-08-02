---
title: iOS 6.0 API Diffs
apple_id: TP40011959
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS60APIDiffs/index.html
archived_at: '2026-07-18T02:55:48.701301Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 5.1 to iOS 6.0 API Differences

## Added frameworks:

- AdSupport
- MediaToolbox
- PassKit
- Social

## Accelerate

Alpha.hAdded #def vImageClipToAlpha_BGRA8888Added #def vImageClipToAlpha_BGRAFFFFAdded [vImageClipToAlpha_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410676-vimagecliptoalpha_rgba8888)Added [vImageClipToAlpha_RGBAFFFF()](https://developer.apple.com/documentation/accelerate/1410680-vimagecliptoalpha_rgbaffff)Added [vImagePremultiplyData_ARGB16U()](https://developer.apple.com/documentation/accelerate/1410642-vimagepremultiplydata_argb16u)Added #def vImagePremultiplyData_BGRA16UAdded [vImagePremultiplyData_RGBA16U()](https://developer.apple.com/documentation/accelerate/1410647-vimagepremultiplydata_rgba16u)Added [vImageUnpremultiplyData_ARGB16U()](https://developer.apple.com/documentation/accelerate/1410638-vimageunpremultiplydata_argb16u)Added #def vImageUnpremultiplyData_BGRA16UAdded [vImageUnpremultiplyData_RGBA16U()](https://developer.apple.com/documentation/accelerate/1410690-vimageunpremultiplydata_rgba16u)Conversion.hAdded [#def vImageConvert_BGR888toBGRA8888](https://developer.apple.com/documentation/accelerate/vimageconvert_bgr888tobgra8888)Added [#def vImageConvert_BGR888toRGBA8888](https://developer.apple.com/documentation/accelerate/vimageconvert_bgr888torgba8888)Added [#def vImageConvert_BGRA8888toBGR888](https://developer.apple.com/documentation/accelerate/vimageconvert_bgra8888tobgr888)Added [vImageConvert_BGRA8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533090-vimageconvert_bgra8888torgb888)Added [vImageConvert_RGB888toBGRA8888()](https://developer.apple.com/documentation/accelerate/1533212-vimageconvert_rgb888tobgra8888)Added [vImageConvert_RGB888toRGBA8888()](https://developer.apple.com/documentation/accelerate/1533228-vimageconvert_rgb888torgba8888)Added [#def vImageConvert_RGBA8888toBGR888](https://developer.apple.com/documentation/accelerate/vimageconvert_rgba8888tobgr888)Added [vImageConvert_RGBA8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533062-vimageconvert_rgba8888torgb888)Added [#def vImageFlatten_BGRA8888ToBGR888](https://developer.apple.com/documentation/accelerate/vimageflatten_bgra8888tobgr888)Added [vImageFlatten_BGRA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533119-vimageflatten_bgra8888torgb888)Added [vImageFlatten_BGRAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533156-vimageflatten_bgrafffftorgbfff)Added [#def vImageFlatten_RGBA8888ToBGR888](https://developer.apple.com/documentation/accelerate/vimageflatten_rgba8888tobgr888)Added [vImageFlatten_RGBA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533147-vimageflatten_rgba8888torgb888)Added [vImageFlatten_RGBAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533280-vimageflatten_rgbafffftorgbfff)Modified [vImageConvert_ARGB8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533276-vimageconvert_argb8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageConvert_ARGB8888toRGB888 ( const vImage_Buffer \*argbSrc, const vImage_Buffer \*rgbDest, vImage_Flags flags); |
| To | vImage_Error vImageConvert_ARGB8888toRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, vImage_Flags); |

Modified [vImageConvert_RGB888toARGB8888()](https://developer.apple.com/documentation/accelerate/1533137-vimageconvert_rgb888toargb8888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageConvert_RGB888toARGB8888 ( const vImage_Buffer \*rgbSrc, const vImage_Buffer \*aSrc, Pixel_8 alpha, const vImage_Buffer \*argbDest, bool premultiply, vImage_Flags flags); |
| To | vImage_Error vImageConvert_RGB888toARGB8888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8, const vImage_Buffer \*, bool, vImage_Flags); |

Modified [vImageFlatten_ARGBFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533210-vimageflatten_argbfffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*argbFFFFSrc, const vImage_Buffer \*rgbFFFdest, Pixel_FFFF backgroundColor, bool isImagePremultiplied, vImage_Flags flags); |
| To | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |

Modified [vImageFlatten_ARGB8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533019-vimageflatten_argb8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*argb8888Src, const vImage_Buffer \*rgb888dest, Pixel_8888 backgroundColor, bool isImagePremultiplied, vImage_Flags flags); |
| To | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |

Geometry.hAdded [vImageHorizontalReflect_Planar16U()](https://developer.apple.com/documentation/accelerate/1509287-vimagehorizontalreflect_planar16)Added [vImageRotate90_Planar16U()](https://developer.apple.com/documentation/accelerate/1509205-vimagerotate90_planar16u)Added [vImageVerticalReflect_Planar16U()](https://developer.apple.com/documentation/accelerate/1509265-vimageverticalreflect_planar16u)Modified [vImageAffineWarpCG_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509263-vimageaffinewarpcg_argbffff)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [vImageAffineWarpCG_PlanarF()](https://developer.apple.com/documentation/accelerate/1509193-vimageaffinewarpcg_planarf)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [vImageAffineWarpCG_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509276-vimageaffinewarpcg_argb8888)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [vImageAffineWarpCG_Planar8()](https://developer.apple.com/documentation/accelerate/1509190-vimageaffinewarpcg_planar8)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

vDSP.hAdded [vDSP_DCT_CreateSetup()](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup)Added [vDSP_DCT_Execute()](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute)Added vDSP_DCT_IIAdded vDSP_DCT_IIIAdded vDSP_DCT_TypeAdded [vDSP_biquad()](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad)Added [vDSP_biquadD()](https://developer.apple.com/documentation/accelerate/1450359-vdsp_biquadd)Added [vDSP_biquad_CreateSetup()](https://developer.apple.com/documentation/accelerate/1450374-vdsp_biquad_createsetup)Added [vDSP_biquad_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450239-vdsp_biquad_createsetupd)Added [vDSP_biquad_DestroySetup()](https://developer.apple.com/documentation/accelerate/1450168-vdsp_biquad_destroysetup)Added [vDSP_biquad_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450640-vdsp_biquad_destroysetupd)Added [vDSP_biquad_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquad_setup)Added [vDSP_biquad_SetupD](https://developer.apple.com/documentation/kernel/vdsp_biquad_setupd)Added [vDSP_normalize()](https://developer.apple.com/documentation/accelerate/1450106-vdsp_normalize)Added [vDSP_normalizeD()](https://developer.apple.com/documentation/accelerate/1450154-vdsp_normalized)Added [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)Added [vDSP_sve_svesqD()](https://developer.apple.com/documentation/accelerate/1450682-vdsp_sve_svesqd)Added [vDSP_vsmsma()](https://developer.apple.com/documentation/accelerate/1450324-vdsp_vsmsma)Modified [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmax ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmax ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_vmin()](https://developer.apple.com/documentation/accelerate/1450216-vdsp_vmin)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmin ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmin ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

vForce.hAdded vvpows()Added vvpowsf()vImage_Types.hAdded Pixel_16UAdded [#def VIMAGE_CGAFFINETRANSFORM_IS_AVAILABLE](https://developer.apple.com/documentation/accelerate/vimage_cgaffinetransform_is_available)Modified [vImage_CGAffineTransform](https://developer.apple.com/documentation/accelerate/vimage_cgaffinetransform)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

vfp.hAdded [vacosf()](https://developer.apple.com/documentation/accelerate/1556283-vacosf)Added [vacoshf()](https://developer.apple.com/documentation/accelerate/1556279-vacoshf)Added [vasinf()](https://developer.apple.com/documentation/accelerate/1556255-vasinf)Added [vasinhf()](https://developer.apple.com/documentation/accelerate/1556281-vasinhf)Added [vatan2f()](https://developer.apple.com/documentation/accelerate/1556295-vatan2f)Added [vatanf()](https://developer.apple.com/documentation/accelerate/1556289-vatanf)Added [vatanhf()](https://developer.apple.com/documentation/accelerate/1556251-vatanhf)Added [vceilf()](https://developer.apple.com/documentation/accelerate/1556252-vceilf)Added [vclassifyf()](https://developer.apple.com/documentation/accelerate/1556265-vclassifyf)Added [vcopysignf()](https://developer.apple.com/documentation/accelerate/1556276-vcopysignf)Added [vcosf()](https://developer.apple.com/documentation/accelerate/1556273-vcosf)Added [vcoshf()](https://developer.apple.com/documentation/accelerate/1556256-vcoshf)Added vcospif()Added [vdivf()](https://developer.apple.com/documentation/accelerate/1556290-vdivf)Added vexp2f()Added [vexpf()](https://developer.apple.com/documentation/accelerate/1556271-vexpf)Added [vexpm1f()](https://developer.apple.com/documentation/accelerate/1556259-vexpm1f)Added vfabsf()Added [vfloorf()](https://developer.apple.com/documentation/accelerate/1556275-vfloorf)Added [vfmodf()](https://developer.apple.com/documentation/accelerate/1556261-vfmodf)Added [vipowf()](https://developer.apple.com/documentation/accelerate/1556262-vipowf)Added [vlog10f()](https://developer.apple.com/documentation/accelerate/1556285-vlog10f)Added [vlog1pf()](https://developer.apple.com/documentation/accelerate/1556277-vlog1pf)Added vlog2f()Added [vlogbf()](https://developer.apple.com/documentation/accelerate/1556274-vlogbf)Added [vlogf()](https://developer.apple.com/documentation/accelerate/1556263-vlogf)Added [vnextafterf()](https://developer.apple.com/documentation/accelerate/1556280-vnextafterf)Added [vnintf()](https://developer.apple.com/documentation/accelerate/1556253-vnintf)Added [vpowf()](https://developer.apple.com/documentation/accelerate/1556269-vpowf)Added [vrecf()](https://developer.apple.com/documentation/accelerate/1556257-vrecf)Added [vremainderf()](https://developer.apple.com/documentation/accelerate/1556293-vremainderf)Added [vremquof()](https://developer.apple.com/documentation/accelerate/1556264-vremquof)Added [vrsqrtf()](https://developer.apple.com/documentation/accelerate/1556268-vrsqrtf)Added [vscalbf()](https://developer.apple.com/documentation/accelerate/1556284-vscalbf)Added [vsignbitf()](https://developer.apple.com/documentation/accelerate/1556294-vsignbitf)Added [vsincosf()](https://developer.apple.com/documentation/accelerate/1556288-vsincosf)Added [vsinf()](https://developer.apple.com/documentation/accelerate/1556250-vsinf)Added [vsinhf()](https://developer.apple.com/documentation/accelerate/1556254-vsinhf)Added vsinpif()Added [vsqrtf()](https://developer.apple.com/documentation/accelerate/1556282-vsqrtf)Added [vtablelookup()](https://developer.apple.com/documentation/accelerate/1556270-vtablelookup)Added [vtanf()](https://developer.apple.com/documentation/accelerate/1556287-vtanf)Added [vtanhf()](https://developer.apple.com/documentation/accelerate/1556267-vtanhf)Added vtanpif()Added vtruncf()

## Accounts

ACAccount.hModified [ACAccount.username](https://developer.apple.com/documentation/accounts/acaccount/1543839-username)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, copy) NSString \*username |
| To | @property(copy, nonatomic) NSString \*username |

Modified [ACAccount.accountType](https://developer.apple.com/documentation/accounts/acaccount/1543805-accounttype)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) ACAccountType \*accountType |
| To | @property(strong, nonatomic) ACAccountType \*accountType |

Modified [ACAccount.accountDescription](https://developer.apple.com/documentation/accounts/acaccount/1543836-accountdescription)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, copy) NSString \*accountDescription |
| To | @property(copy, nonatomic) NSString \*accountDescription |

Modified [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSString \*identifier |
| To | @property(readonly, weak, nonatomic) NSString \*identifier |

Modified [ACAccount.credential](https://developer.apple.com/documentation/accounts/acaccount/1543779-credential)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) ACAccountCredential \*credential |
| To | @property(strong, nonatomic) ACAccountCredential \*credential |

ACAccountCredential.hAdded [-[ACAccountCredential initWithOAuth2Token:refreshToken:expiryDate:]](https://developer.apple.com/documentation/accounts/acaccountcredential/1507892-initwithoauth2token)Added [ACAccountCredential.oauthToken](https://developer.apple.com/documentation/accounts/acaccountcredential/1507894-oauthtoken)ACAccountStore.hAdded [-[ACAccountStore removeAccount:withCompletionHandler:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493968-removeaccount)Added [-[ACAccountStore renewCredentialsForAccount:completion:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493959-renewcredentialsforaccount)Added [-[ACAccountStore requestAccessToAccountsWithType:options:completion:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493964-requestaccesstoaccounts)Added [ACAccountCredentialRenewResult](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)Added [ACAccountCredentialRenewResultFailed](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/acaccountcredentialrenewresultfailed)Added [ACAccountCredentialRenewResultRejected](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/rejected)Added [ACAccountCredentialRenewResultRenewed](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/acaccountcredentialrenewresultrenewed)Added [ACAccountStoreCredentialRenewalHandler](https://developer.apple.com/documentation/accounts/acaccountstorecredentialrenewalhandler)Added [ACAccountStoreRemoveCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstoreremovecompletionhandler)Added [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)Added [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone)Added [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends)Added [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey)Added [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme)Added [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)Added NS_ENUM() (no architecture available)Modified [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSArray \*accounts |
| To | @property(readonly, weak, nonatomic) NSArray \*accounts |

Modified [-[ACAccountStore requestAccessToAccountsWithType:withCompletionHandler:]](https://developer.apple.com/documentation/accounts/acaccountstore/1624250-requestaccesstoaccountswithtype)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

ACAccountType.hAdded [ACAccountTypeIdentifierFacebook](https://developer.apple.com/documentation/accounts/acaccounttypeidentifierfacebook)Added [ACAccountTypeIdentifierSinaWeibo](https://developer.apple.com/documentation/accounts/acaccounttypeidentifiersinaweibo)Modified [ACAccountType.accountTypeDescription](https://developer.apple.com/documentation/accounts/acaccounttype/1543834-accounttypedescription)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSString \*accountTypeDescription |
| To | @property(readonly, nonatomic) NSString \*accountTypeDescription |

Modified [ACAccountType.accessGranted](https://developer.apple.com/documentation/accounts/acaccounttype/1543838-accessgranted)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) BOOL accessGranted |
| To | @property(readonly, nonatomic) BOOL accessGranted |

Modified [ACAccountType.identifier](https://developer.apple.com/documentation/accounts/acaccounttype/1543833-identifier)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSString \*identifier |
| To | @property(readonly, nonatomic) NSString \*identifier |

ACError.hAdded [ACErrorAccessInfoInvalid](https://developer.apple.com/documentation/accounts/acerroraccessinfoinvalid)

## AddressBook

ABAddressBook.hAdded [ABAddressBookCreateWithOptions()](https://developer.apple.com/documentation/addressbook/1621991-abaddressbookcreatewithoptions)Added [ABAddressBookGetAuthorizationStatus()](https://developer.apple.com/documentation/addressbook/1622002-abaddressbookgetauthorizationsta)Added [ABAddressBookRequestAccessCompletionHandler](https://developer.apple.com/documentation/addressbook/abaddressbookrequestaccesscompletionhandler)Added [ABAddressBookRequestAccessWithCompletion()](https://developer.apple.com/documentation/addressbook/1622001-abaddressbookrequestaccesswithco)Added [ABAuthorizationStatus](https://developer.apple.com/documentation/addressbook/abauthorizationstatus)Added CF_ENUM() (no architecture available)Added [kABAuthorizationStatusAuthorized](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/kabauthorizationstatusauthorized)Added [kABAuthorizationStatusDenied](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/kabauthorizationstatusdenied)Added [kABAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/notdetermined)Added [kABAuthorizationStatusRestricted](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/restricted)Added [kABOperationNotPermittedByUserError](https://developer.apple.com/documentation/addressbook/kaboperationnotpermittedbyusererror)Modified [ABAddressBookCreate()](https://developer.apple.com/documentation/addressbook/1621998-abaddressbookcreate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

ABPerson.hAdded [kABPersonSocialProfileServiceSinaWeibo](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicesinaweibo)AddressBookDefines.hAdded #def AB_EXTERNAdded #def AddressBook_AddressBookDefines_h

## AddressBookUI

ABPersonViewController.hModified [ABPersonViewController](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | UIViewControllerRestoration |

## AdSupport

ASIdentifierManager.hAdded [ASIdentifierManager](https://developer.apple.com/documentation/adsupport/asidentifiermanager)Added [ASIdentifierManager.advertisingIdentifier](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614151-advertisingidentifier)Added [ASIdentifierManager.advertisingTrackingEnabled](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-isadvertisingtrackingenabled)Added [+[ASIdentifierManager sharedManager]](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614149-shared)AdSupport.hAdded #def AdSupport_AdSupport_h

## AssetsLibrary

ALAsset.hAdded [ALAssetPropertyAssetURL](https://developer.apple.com/documentation/assetslibrary/alassetpropertyasseturl)ALAssetsLibrary.hAdded [+[ALAssetsLibrary authorizationStatus]](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617901-authorizationstatus)Added [+[ALAssetsLibrary disableSharedPhotoStreamsSupport]](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617905-disablesharedphotostreamssupport)Added [ALAssetLibraryDeletedAssetGroupsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibrarydeletedassetgroupskey)Added [ALAssetLibraryInsertedAssetGroupsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibraryinsertedassetgroupskey)Added [ALAssetLibraryUpdatedAssetGroupsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibraryupdatedassetgroupskey)Added [ALAssetLibraryUpdatedAssetsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibraryupdatedassetskey)Added [ALAuthorizationStatus](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus)Added [ALAuthorizationStatusAuthorized](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/alauthorizationstatusauthorized)Added [ALAuthorizationStatusDenied](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/denied)Added [ALAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/alauthorizationstatusnotdetermined)Added [ALAuthorizationStatusRestricted](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/restricted)Added NS_ENUM() (no architecture available)

## AudioToolbox

AudioConverter.hAdded [kAudioConverterPropertyDitherBitDepth](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyditherbitdepth) (no architecture available)Added [kAudioConverterPropertyDithering](https://developer.apple.com/documentation/audiotoolbox/1559925-anonymous/kaudioconverterpropertydithering) (no architecture available)Added [kDitherAlgorithm_NoiseShaping](https://developer.apple.com/documentation/audiotoolbox/1559931-anonymous/kditheralgorithm_noiseshaping) (no architecture available)Added [kDitherAlgorithm_TPDF](https://developer.apple.com/documentation/audiotoolbox/kditheralgorithm_tpdf) (no architecture available)AudioFile.hAdded [kAudioFileM4BType](https://developer.apple.com/documentation/audiotoolbox/kaudiofilem4btype)AudioFormat.hAdded [kAudioFormatProperty_AreChannelLayoutsEquivalent](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_arechannellayoutsequivalent)AudioQueue.hAdded [AudioQueueChannelAssignment](https://developer.apple.com/documentation/audiotoolbox/audioqueuechannelassignment)Added [AudioQueueProcessingTapCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapcallback)Added [AudioQueueProcessingTapDispose()](https://developer.apple.com/documentation/audiotoolbox/1502310-audioqueueprocessingtapdispose)Added [AudioQueueProcessingTapGetQueueTime()](https://developer.apple.com/documentation/audiotoolbox/1502087-audioqueueprocessingtapgetqueuet)Added [AudioQueueProcessingTapGetSourceAudio()](https://developer.apple.com/documentation/audiotoolbox/1502107-audioqueueprocessingtapgetsource)Added [AudioQueueProcessingTapNew()](https://developer.apple.com/documentation/audiotoolbox/1503209-audioqueueprocessingtapnew)Added [AudioQueueProcessingTapRef](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapref)Added [kAudioQueueErr_InvalidTapContext](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidtapcontext)Added [kAudioQueueErr_InvalidTapType](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidtaptype)Added [kAudioQueueErr_TooManyTaps](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_toomanytaps)Added [kAudioQueueProcessingTap_EndOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_endofstream)Added [kAudioQueueProcessingTap_PostEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_posteffects)Added [kAudioQueueProcessingTap_PreEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502092-preeffects)Added [kAudioQueueProcessingTap_Siphon](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502728-siphon)Added [kAudioQueueProcessingTap_StartOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_startofstream)Added [kAudioQueueProperty_ChannelAssignments](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_channelassignments)AudioSession.hModified [kAudioSessionCategory_AmbientSound](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_ambientsound)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_AudioRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audioroutedescription)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_Headphones](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_headphones)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_LiveAudio](https://developer.apple.com/documentation/audiotoolbox/1618459-deprecated_audio_session_categor/kaudiosessioncategory_liveaudio)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_AudioRoute](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audioroute)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_USBAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_usbaudio)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_CategoryChange](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_categorychange)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionMode_Measurement](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_measurement)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionMode_Default](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionmode_default)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OverrideCategoryDefaultToSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorydefaulttospeaker)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OverrideCategoryMixWithOthers](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorymixwithothers)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionRemovePropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1618364-audiosessionremovepropertylisten)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionRemovePropertyListenerWithUserData()](https://developer.apple.com/documentation/audiotoolbox/1618396-audiosessionremovepropertylisten)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionUnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionunspecifiederror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionMode_GameChat](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_gamechat)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_PreferredHardwareSampleRate](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_preferredhardwaresamplerate)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_OutputDestinationKey_Description](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_outputdestinationkey_description)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1618433-audiosessiongetproperty)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_InterruptionType](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_interruptiontype)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionNotInitialized](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnotinitialized)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionPropertyID](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertyid)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInputRoute_BuiltInMic](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_builtinmic)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_BuiltInReceiver](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_builtinreceiver)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_UserInterfaceSoundEffects](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_userinterfacesoundeffects)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_AudioRouteKey_Inputs](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_inputs)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_InputSourceKey_Description](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_inputsourcekey_description)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareInputLatency](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_currenthardwareinputlatency)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_AudioRouteChangeKey_PreviousRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_previousroutedescription)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_InputSourceKey_ID](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_inputsourcekey_id)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_InputGainScalar](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_inputgainscalar)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_InputGainAvailable](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_inputgainavailable)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_AudioRouteChangeKey_CurrentRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_currentroutedescription)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_BluetoothA2DP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_bluetootha2dp)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioServicesNoHardwareError](https://developer.apple.com/documentation/audiotoolbox/kaudioservicesnohardwareerror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_SoloAmbientSound](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_soloambientsound)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionIncompatibleCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionincompatiblecategory)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OverrideAudioRoute](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_overrideaudioroute)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_AirPlay](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_airplay)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [#def kAudioSession_AudioRouteChangeKey_OldRoute](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_oldroute)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_NewDeviceAvailable](https://developer.apple.com/documentation/audiotoolbox/1618380-audio_route_change_reasons/kaudiosessionroutechangereason_newdeviceavailable)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_MediaPlayback](https://developer.apple.com/documentation/audiotoolbox/1618427-audio_session_categories/kaudiosessioncategory_mediaplayback)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_AudioRouteKey_Outputs](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_outputs)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareOutputVolume](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_currenthardwareoutputvolume)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_HDMI](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_hdmi)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_OldDeviceUnavailable](https://developer.apple.com/documentation/audiotoolbox/1618380-audio_route_change_reasons/kaudiosessionroutechangereason_olddeviceunavailable)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionNoCategorySet](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnocategoryset)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_Mode](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_mode)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInputRoute_HeadsetMic](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_headsetmic)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionInterruptionType](https://developer.apple.com/documentation/audiotoolbox/audiosessioninterruptiontype)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_AudioInputAvailable](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_audioinputavailable)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_PreferredHardwareIOBufferDuration](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_preferredhardwareiobufferduration)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionInitialize()](https://developer.apple.com/documentation/audiotoolbox/1618360-audiosessioninitialize)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionAlreadyInitialized](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionalreadyinitialized)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOverrideAudioRoute_None](https://developer.apple.com/documentation/audiotoolbox/1618372-audio_session_category_route_ove/kaudiosessionoverrideaudioroute_none)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionMode_VideoRecording](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_videorecording)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_RecordAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_recordaudio)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionPropertyListener](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertylistener)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareSampleRate](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_currenthardwaresamplerate)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_RouteChangeKey_Reason](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_routechangekey_reason)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionInterruptionListener](https://developer.apple.com/documentation/audiotoolbox/audiosessioninterruptionlistener)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionSetActive()](https://developer.apple.com/documentation/audiotoolbox/1618421-audiosessionsetactive)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInitializationError](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessioninitializationerror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionSetActiveFlag_NotifyOthersOnDeactivation](https://developer.apple.com/documentation/audiotoolbox/1618357-audio_session_activation_flags/kaudiosessionsetactiveflag_notifyothersondeactivation)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_BluetoothHFP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_bluetoothhfp)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_AudioRouteKey_Type](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_type)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_ServerDied](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_serverdied)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OutputDestinations](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_outputdestinations)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInterruptionType_ShouldResume](https://developer.apple.com/documentation/audiotoolbox/1618387-anonymous/kaudiosessioninterruptiontype_shouldresume)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionGetPropertySize()](https://developer.apple.com/documentation/audiotoolbox/1618437-audiosessiongetpropertysize)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OutputDestination](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_outputdestination)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_InputSource](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_inputsource)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionAddPropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1618442-audiosessionaddpropertylistener)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareOutputLatency](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_currenthardwareoutputlatency)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionNotActiveError](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnotactiveerror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_BuiltInSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_builtinspeaker)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionBeginInterruption](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionbegininterruption)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSession_OutputDestinationKey_ID](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_outputdestinationkey_id)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInputRoute_USBAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_usbaudio)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_Override](https://developer.apple.com/documentation/audiotoolbox/1618380-audio_route_change_reasons/kaudiosessionroutechangereason_override)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareInputNumberChannels](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_currenthardwareinputnumberchannels)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_AudioProcessing](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_audioprocessing)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_NoSuitableRouteForCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_nosuitablerouteforcategory)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInputRoute_BluetoothHFP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_bluetoothhfp)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionCategory_PlayAndRecord](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_playandrecord)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInterruptionType_ShouldNotResume](https://developer.apple.com/documentation/audiotoolbox/1618387-anonymous/kaudiosessioninterruptiontype_shouldnotresume)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_Unknown](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_unknown)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareIOBufferDuration](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_currenthardwareiobufferduration)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_InputSources](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_inputsources)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1618399-audiosessionsetproperty)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionRouteChangeReason_WakeFromSleep](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_wakefromsleep)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOverrideAudioRoute_Speaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoverrideaudioroute_speaker)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_CurrentHardwareOutputNumberChannels](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_currenthardwareoutputnumberchannels)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [AudioSessionSetActiveWithFlags()](https://developer.apple.com/documentation/audiotoolbox/1618356-audiosessionsetactivewithflags)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionBadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionbadpropertysizeerror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionNoError](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnoerror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionOutputRoute_LineOut](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_lineout)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionInputRoute_LineIn](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_linein)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_AudioRouteChange](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audioroutechange)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionUnsupportedPropertyError](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionunsupportedpropertyerror)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [#def kAudioSession_AudioRouteChangeKey_Reason](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_reason)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_AudioCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audiocategory)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OtherAudioIsPlaying](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_otheraudioisplaying)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OverrideCategoryEnableBluetoothInput](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_overridecategoryenablebluetoothinput)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionEndInterruption](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionendinterruption)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionMode_VoiceChat](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_voicechat)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

Modified [kAudioSessionProperty_OtherMixableAudioShouldDuck](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_othermixableaudioshouldduck)

|  | Header |
| --- | --- |
| From | AudioServices.h |
| To | AudioSession.h |

CAFFile.hAdded [kCAF_iXMLChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_ixmlchunkid)

## AudioUnit

AUComponent.hAdded [AudioUnitProcess()](https://developer.apple.com/documentation/audiotoolbox/1439630-audiounitprocess)Added [AudioUnitProcessMultiple()](https://developer.apple.com/documentation/audiotoolbox/1440334-audiounitprocessmultiple)Added kAudioUnitSubType_DCFilterModified [kAudioUnitSubType_NewTimePitch](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_newtimepitch)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_Splitter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_splitter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_Delay](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_delay)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_DeferredRenderer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_deferredrenderer)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_MatrixMixer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_matrixmixer)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_Merger](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_merger)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

AudioUnitParameters.hAdded [k3DMixerParam_PostAveragePower](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_postaveragepower) (no architecture available)Added [k3DMixerParam_PostPeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_postpeakholdlevel) (no architecture available)Added [k3DMixerParam_PreAveragePower](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_preaveragepower) (no architecture available)Added [k3DMixerParam_PrePeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_prepeakholdlevel) (no architecture available)Added kAUDCFilterParam_DecayTimeAdded [kAUGroupParameterID_Sostenuto](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_sostenuto)Added [kAUNBandEQParam_GlobalGain](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_globalgain)Added [kAUSamplerParam_CoarseTuning](https://developer.apple.com/documentation/audiotoolbox/kausamplerparam_coarsetuning)Added [kAUSamplerParam_FineTuning](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_finetuning)Added [kAUSamplerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_gain)Added [kAUSamplerParam_Pan](https://developer.apple.com/documentation/audiotoolbox/kausamplerparam_pan)Added [kNewTimePitchParam_EnablePeakLocking](https://developer.apple.com/documentation/audiotoolbox/knewtimepitchparam_enablepeaklocking)Added [kNewTimePitchParam_Overlap](https://developer.apple.com/documentation/audiotoolbox/knewtimepitchparam_overlap)Added [kNewTimePitchParam_Pitch](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_pitch)Added [kNewTimePitchParam_Rate](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_rate)Added [kRoundTripAACParam_BitRate](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_bitrate) (no architecture available)Added [kRoundTripAACParam_CompressedFormatSampleRate](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_compressedformatsamplerate) (no architecture available)Added [kRoundTripAACParam_EncodingStrategy](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_encodingstrategy) (no architecture available)Added [kRoundTripAACParam_Format](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_format) (no architecture available)Added [kRoundTripAACParam_Quality](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_quality) (no architecture available)Added [kRoundTripAACParam_RateOrQuality](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_rateorquality) (no architecture available)Modified [kMatrixMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_enable)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PostPeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postpeakholdlevel)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PreAveragePower](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_preaveragepower)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_Volume](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_volume)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PreAveragePowerLinear](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_preaveragepowerlinear)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDelayParam_Feedback](https://developer.apple.com/documentation/audiotoolbox/kdelayparam_feedback)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PrePeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_prepeakholdlevel)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PrePeakHoldLevelLinear](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_prepeakholdlevellinear)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDelayParam_DelayTime](https://developer.apple.com/documentation/audiotoolbox/1390010-anonymous/kdelayparam_delaytime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PostPeakHoldLevelLinear](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postpeakholdlevellinear)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PostAveragePower](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postaveragepower)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDelayParam_WetDryMix](https://developer.apple.com/documentation/audiotoolbox/1390010-anonymous/kdelayparam_wetdrymix)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kMatrixMixerParam_PostAveragePowerLinear](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postaveragepowerlinear)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDelayParam_LopassCutoff](https://developer.apple.com/documentation/audiotoolbox/kdelayparam_lopasscutoff)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

AudioUnitProperties.hAdded [AUSamplerInstrumentData](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata)Added [kAUSamplerProperty_BankAndPreset](https://developer.apple.com/documentation/audiotoolbox/1534019-anonymous/kausamplerproperty_bankandpreset)Added [kAUSamplerProperty_LoadInstrument](https://developer.apple.com/documentation/audiotoolbox/1533959-anonymous/kausamplerproperty_loadinstrument)Added [kAUVoiceIOErr_UnexpectedNumberOfInputChannels](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioerr_unexpectednumberofinputchannels) (no architecture available)Added [kAudioUnitProperty_NickName](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_nickname)Added [kInstrumentType_AUPreset](https://developer.apple.com/documentation/audiotoolbox/kinstrumenttype_aupreset)Added [kInstrumentType_Audiofile](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_audiofile)Added [kInstrumentType_DLSPreset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_dlspreset)Added [kInstrumentType_EXS24](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_exs24)Added [kInstrumentType_SF2Preset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_sf2preset)Modified [AUDependentParameter](https://developer.apple.com/documentation/audiotoolbox/audependentparameter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_DeferredRendererExtraLatency](https://developer.apple.com/documentation/audiotoolbox/1534061-anonymous/kaudiounitproperty_deferredrendererextralatency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_DeferredRendererPullSize](https://developer.apple.com/documentation/audiotoolbox/1534061-anonymous/kaudiounitproperty_deferredrendererpullsize)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_OfflineRender](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_offlinerender)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_InputSamplesInOutput](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_inputsamplesinoutput)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_DependentParameters](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_dependentparameters)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_DeferredRendererWaitFrames](https://developer.apple.com/documentation/audiotoolbox/1534061-anonymous/kaudiounitproperty_deferredrendererwaitframes)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [AUInputSamplesInOutputCallbackStruct](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallbackstruct)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

## AVFoundation

AVAsset.hAdded [-[AVAsset chapterMetadataGroupsBestMatchingPreferredLanguages:]](https://developer.apple.com/documentation/avfoundation/avasset/1390909-chaptermetadatagroupsbestmatchin)Added [AVURLAsset.resourceLoader](https://developer.apple.com/documentation/avfoundation/avurlasset/1389118-resourceloader)Added AVURLAsset(AVURLAssetURLHandling)AVAssetExportSession.hAdded [+[AVAssetExportSession determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385821-determinecompatibilityofexportpr)Added [-[AVAssetExportSession determineCompatibleFileTypesWithCompletionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387907-determinecompatiblefiletypeswith)Modified [+[AVAssetExportSession exportSessionWithAsset:presetName:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1564246-exportsessionwithasset)

|  | Declaration |
| --- | --- |
| From | + (id)exportSessionWithAsset:(AVAsset \*)asset presetName:(NSString \*)presetName |
| To | + (AVAssetExportSession \*)exportSessionWithAsset:(AVAsset \*)asset presetName:(NSString \*)presetName |

AVAssetImageGenerator.hAdded [AVAssetImageGenerator.asset](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1390689-asset)AVAssetResourceLoader.hAdded [AVAssetResourceLoader](https://developer.apple.com/documentation/avfoundation/avassetresourceloader)Added [AVAssetResourceLoader.delegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387913-delegate)Added [AVAssetResourceLoader.delegateQueue](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387678-delegatequeue)Added [-[AVAssetResourceLoader setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1388314-setdelegate)Added [AVAssetResourceLoaderDelegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate)Added [-[AVAssetResourceLoaderDelegate resourceLoader:shouldWaitForLoadingOfRequestedResource:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1388121-resourceloader)Added [AVAssetResourceLoadingRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest)Added [-[AVAssetResourceLoadingRequest finishLoadingWithError:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390491-finishloading)Added [-[AVAssetResourceLoadingRequest finishLoadingWithResponse:data:redirect:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1623677-finishloadingwithresponse)Added [AVAssetResourceLoadingRequest.finished](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389270-isfinished)Added [AVAssetResourceLoadingRequest.request](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386220-request)Added [-[AVAssetResourceLoadingRequest streamingContentKeyRequestDataForApp:contentIdentifier:options:error:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386116-streamingcontentkeyrequestdata)AVAssetWriter.hAdded [-[AVAssetWriter finishWritingWithCompletionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390432-finishwriting)Modified [-[AVAssetWriter finishWriting]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1426644-finishwriting)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

AVAssetWriterInput.hAdded [+[AVAssetWriterInput assetWriterInputWithMediaType:outputSettings:sourceFormatHint:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1449091-assetwriterinputwithmediatype)Added [-[AVAssetWriterInput initWithMediaType:outputSettings:sourceFormatHint:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389994-init)Added [AVAssetWriterInput.sourceFormatHint](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387647-sourceformathint)AVAudioMix.hAdded [AVAudioMixInputParameters.audioTapProcessor](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1388578-audiotapprocessor)Added [AVMutableAudioMixInputParameters.audioTapProcessor](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1389296-audiotapprocessor)AVAudioPlayer.hAdded [AVAudioPlayer.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1624038-channelassignments)Added [-[AVAudioPlayerDelegate audioPlayerEndInterruption:withOptions:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624040-audioplayerendinterruption)Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624039-audioplayerendinterruption)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:withFlags:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624041-audioplayerendinterruption)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

AVAudioRecorder.hAdded [AVAudioRecorder.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624903-channelassignments)Added [AVAudioRecorder.deviceCurrentTime](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624898-devicecurrenttime)Added [-[AVAudioRecorder recordAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624900-recordattime)Added [-[AVAudioRecorder recordAtTime:forDuration:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624899-recordattime)Added [-[AVAudioRecorderDelegate audioRecorderEndInterruption:withOptions:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624901-audiorecorderendinterruption)Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:withFlags:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624904-audiorecorderendinterruption)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624902-audiorecorderendinterruption)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

AVAudioSession.hAdded [AVAudioSession.IOBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616498-iobufferduration)Added [AVAudioSession.categoryOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616503-categoryoptions)Added [AVAudioSession.currentRoute](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616453-currentroute)Added [AVAudioSession.inputAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616524-isinputavailable)Added [AVAudioSession.inputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616485-inputdatasource)Added [AVAudioSession.inputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616513-inputdatasources)Added [AVAudioSession.inputGain](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616593-inputgain)Added [AVAudioSession.inputGainSettable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616502-inputgainsettable)Added [AVAudioSession.inputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616537-inputlatency)Added [AVAudioSession.inputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616475-inputnumberofchannels)Added [AVAudioSession.otherAudioPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616610-otheraudioplaying)Added [AVAudioSession.outputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616572-outputdatasource)Added [AVAudioSession.outputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616479-outputdatasources)Added [AVAudioSession.outputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616500-outputlatency)Added [AVAudioSession.outputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616471-outputnumberofchannels)Added [AVAudioSession.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616533-outputvolume)Added [-[AVAudioSession overrideOutputAudioPort:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616443-overrideoutputaudioport)Added [AVAudioSession.preferredSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616543-preferredsamplerate)Added [AVAudioSession.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616499-samplerate)Added [-[AVAudioSession setActive:withOptions:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive)Added [-[AVAudioSession setCategory:withOptions:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616442-setcategory)Added [-[AVAudioSession setInputDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616507-setinputdatasource)Added [-[AVAudioSession setInputGain:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616546-setinputgain)Added [-[AVAudioSession setOutputDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616582-setoutputdatasource)Added [-[AVAudioSession setPreferredSampleRate:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616523-setpreferredsamplerate)Added [AVAudioSessionChannelDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription)Added [AVAudioSessionChannelDescription.channelName](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616521-channelname)Added [AVAudioSessionChannelDescription.channelNumber](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616444-channelnumber)Added [AVAudioSessionChannelDescription.owningPortUID](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616562-owningportuid)Added [AVAudioSessionDataSourceDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription)Added [AVAudioSessionDataSourceDescription.dataSourceID](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616584-datasourceid)Added [AVAudioSessionDataSourceDescription.dataSourceName](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616595-datasourcename)Added [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription)Added [AVAudioSessionPortDescription.UID](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616617-uid)Added [AVAudioSessionPortDescription.channels](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616574-channels)Added [AVAudioSessionPortDescription.portName](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616497-portname)Added [AVAudioSessionPortDescription.portType](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616445-porttype)Added [AVAudioSessionRouteDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription)Added [AVAudioSessionRouteDescription.inputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616474-inputs)Added [AVAudioSessionRouteDescription.outputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616552-outputs)Added AVAudioSession(AVAudioSessionDeprecated)Added AVAudioSession(AVAudioSessionHardwareConfiguration)Added [AVAudioSessionCategoryMultiRoute](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategorymultiroute)Added [AVAudioSessionCategoryOptionAllowBluetooth](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616518-allowbluetooth)Added [AVAudioSessionCategoryOptionDefaultToSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptiondefaulttospeaker)Added [AVAudioSessionCategoryOptionDuckOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionduckothers)Added [AVAudioSessionCategoryOptionMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionmixwithothers)Added [AVAudioSessionCategoryOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions)Added [AVAudioSessionInterruptionNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification)Added [AVAudioSessionInterruptionOptionKey](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptionkey)Added [AVAudioSessionInterruptionOptionShouldResume](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions/avaudiosessioninterruptionoptionshouldresume)Added [AVAudioSessionInterruptionOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/interruptionoptions)Added [AVAudioSessionInterruptionType](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype)Added [AVAudioSessionInterruptionTypeBegan](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype/avaudiosessioninterruptiontypebegan)Added [AVAudioSessionInterruptionTypeEnded](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype/avaudiosessioninterruptiontypeended)Added [AVAudioSessionInterruptionTypeKey](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontypekey)Added [AVAudioSessionMediaServicesWereResetNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616540-mediaserviceswereresetnotificati)Added [AVAudioSessionModeMoviePlayback](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616623-movieplayback)Added [AVAudioSessionPortAirPlay](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616609-airplay)Added [AVAudioSessionPortBluetoothA2DP](https://developer.apple.com/documentation/avfoundation/avaudiosessionportbluetootha2dp)Added [AVAudioSessionPortBluetoothHFP](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616621-bluetoothhfp)Added [AVAudioSessionPortBuiltInMic](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616487-builtinmic)Added [AVAudioSessionPortBuiltInReceiver](https://developer.apple.com/documentation/avfoundation/avaudiosessionportbuiltinreceiver)Added [AVAudioSessionPortBuiltInSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616561-builtinspeaker)Added [AVAudioSessionPortHDMI](https://developer.apple.com/documentation/avfoundation/avaudiosessionporthdmi)Added [AVAudioSessionPortHeadphones](https://developer.apple.com/documentation/avfoundation/avaudiosessionportheadphones)Added [AVAudioSessionPortHeadsetMic](https://developer.apple.com/documentation/avfoundation/avaudiosessionportheadsetmic)Added [AVAudioSessionPortLineIn](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616466-linein)Added [AVAudioSessionPortLineOut](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616486-lineout)Added [AVAudioSessionPortOverride](https://developer.apple.com/documentation/avfoundation/avaudiosessionportoverride)Added [AVAudioSessionPortOverrideNone](https://developer.apple.com/documentation/avfoundation/avaudiosessionportoverride/avaudiosessionportoverridenone)Added [AVAudioSessionPortOverrideSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride/speaker)Added [AVAudioSessionPortUSBAudio](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616465-usbaudio)Added [AVAudioSessionRouteChangeNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616493-routechangenotification)Added [AVAudioSessionRouteChangePreviousRouteKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangepreviousroutekey)Added [AVAudioSessionRouteChangeReason](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason)Added [AVAudioSessionRouteChangeReasonCategoryChange](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasoncategorychange)Added [AVAudioSessionRouteChangeReasonKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereasonkey)Added [AVAudioSessionRouteChangeReasonNewDeviceAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/newdeviceavailable)Added [AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/nosuitablerouteforcategory)Added [AVAudioSessionRouteChangeReasonOldDeviceUnavailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/olddeviceunavailable)Added [AVAudioSessionRouteChangeReasonOverride](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonoverride)Added [AVAudioSessionRouteChangeReasonUnknown](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonunknown)Added [AVAudioSessionRouteChangeReasonWakeFromSleep](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonwakefromsleep)Added [AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation)Added [AVAudioSessionSetActiveOptions](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions)Added NS_ENUM() (no architecture available)Added NS_OPTIONS() (no architecture available)Modified [-[AVAudioSession setActive:withFlags:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616496-setactive)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (BOOL)setActive:(BOOL)beActive withFlags:(NSInteger)flags error:(NSError \*\*)outError |
| To | iOS 6.0 | - (BOOL)setActive:(BOOL)active withFlags:(NSInteger)flags error:(NSError \*\*)outError |

Modified [-[AVAudioSession setCategory:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616583-setcategory)

|  | Declaration |
| --- | --- |
| From | - (BOOL)setCategory:(NSString \*)theCategory error:(NSError \*\*)outError |
| To | - (BOOL)setCategory:(NSString \*)category error:(NSError \*\*)outError |

Modified [-[AVAudioSession setPreferredHardwareSampleRate:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616526-setpreferredhardwaresamplerate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVAudioSession.delegate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616556-delegate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVAudioSession.inputIsAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616514-inputisavailable)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVAudioSession.currentHardwareSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616494-currenthardwaresamplerate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVAudioSession.currentHardwareInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616489-currenthardwareinputnumberofchan)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVAudioSession.preferredHardwareSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616571-preferredhardwaresamplerate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[AVAudioSession setMode:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616614-setmode)

|  | Declaration |
| --- | --- |
| From | - (BOOL)setMode:(NSString \*)theMode error:(NSError \*\*)outError |
| To | - (BOOL)setMode:(NSString \*)mode error:(NSError \*\*)outError |

Modified [AVAudioSession.currentHardwareOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616581-currenthardwareoutputnumberofcha)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[AVAudioSession setActive:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616597-setactive)

|  | Declaration |
| --- | --- |
| From | - (BOOL)setActive:(BOOL)beActive error:(NSError \*\*)outError |
| To | - (BOOL)setActive:(BOOL)active error:(NSError \*\*)outError |

AVBase.hAdded #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Added #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_TBDAdded #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATERAVCaptureDevice.hAdded [AVCaptureDevice.automaticallyEnablesLowLightBoostWhenAvailable](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624610-automaticallyenableslowlightboos)Added [AVCaptureDevice.lowLightBoostEnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624602-lowlightboostenabled)Added [AVCaptureDevice.lowLightBoostSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624595-islowlightboostsupported)Added [-[AVCaptureDevice setTorchModeOnWithLevel:error:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624609-settorchmodeonwithlevel)Added [AVCaptureDevice.torchActive](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624578-torchactive)Added [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) (no architecture available)Added [AVCaptureDeviceFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1389445-formatdescription) (no architecture available)Added [AVCaptureDeviceFormat.mediaType](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/1388503-mediatype) (no architecture available)Added [AVCaptureDeviceFormat.videoSupportedFrameRateRanges](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1387592-videosupportedframerateranges) (no architecture available)Added [AVCaptureDeviceInputSource](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinputsource) (no architecture available)Added [AVCaptureDeviceInputSource.inputSourceID](https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsource/1387788-inputsourceid) (no architecture available)Added [AVCaptureDeviceInputSource.localizedName](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinputsource/1390422-localizedname) (no architecture available)Added [AVFrameRateRange](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/avframeraterange) (no architecture available)Added [AVFrameRateRange.maxFrameDuration](https://developer.apple.com/documentation/avfoundation/avframeraterange/1386786-maxframeduration) (no architecture available)Added [AVFrameRateRange.maxFrameRate](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/avframeraterange/1386988-maxframerate) (no architecture available)Added [AVFrameRateRange.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/avframeraterange/1388420-minframeduration) (no architecture available)Added [AVFrameRateRange.minFrameRate](https://developer.apple.com/documentation/avfoundation/avframeraterange/1389132-minframerate) (no architecture available)Added AVCaptureDevice(AVCaptureDeviceLowLightBoost)Added AVCaptureDevice(AVCaptureDeviceTransportControls) (no architecture available)Added [AVCaptureDevicePositionUnspecified](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position/unspecified)Added [AVCaptureDeviceTransportControlsNotPlayingMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode/notplaying) (no architecture available)Added [AVCaptureDeviceTransportControlsPlaybackMode](https://developer.apple.com/documentation/avfoundation/avcapturedevicetransportcontrolsplaybackmode) (no architecture available)Added [AVCaptureDeviceTransportControlsPlayingMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode/playing) (no architecture available)Added [AVCaptureDeviceTransportControlsSpeed](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsspeed) (no architecture available)Added [AVCaptureMaxAvailableTorchLevel](https://developer.apple.com/documentation/avfoundation/avcapturemaxavailabletorchlevel)AVCaptureInput.hAdded [AVCaptureScreenInput](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput) (no architecture available)Added [AVCaptureScreenInput.capturesMouseClicks](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1385722-capturesmouseclicks) (no architecture available)Added [AVCaptureScreenInput.cropRect](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1390518-croprect) (no architecture available)Added [-[AVCaptureScreenInput initWithDisplayID:]](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1386383-initwithdisplayid) (no architecture available)Added [AVCaptureScreenInput.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1387216-minframeduration) (no architecture available)Added [AVCaptureScreenInput.scaleFactor](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1390311-scalefactor) (no architecture available)AVCaptureOutput.hAdded [AVCaptureAudioFileOutput](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput) (no architecture available)Added [AVCaptureAudioFileOutput.audioSettings](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/1389958-audiosettings) (no architecture available)Added [+[AVCaptureAudioFileOutput availableOutputFileTypes]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/1390895-availableoutputfiletypes) (no architecture available)Added [AVCaptureAudioFileOutput.metadata](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/1389881-metadata) (no architecture available)Added [-[AVCaptureAudioFileOutput startRecordingToOutputFileURL:outputFileType:recordingDelegate:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/1387420-startrecording) (no architecture available)Added [AVCaptureAudioPreviewOutput](https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput) (no architecture available)Added [AVCaptureAudioPreviewOutput.outputDeviceUniqueID](https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput/1390610-outputdeviceuniqueid) (no architecture available)Added [AVCaptureAudioPreviewOutput.volume](https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput/1390510-volume) (no architecture available)Added [AVCaptureFileOutputDelegate](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate)Added [AVCaptureMetadataOutput](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput)Added [AVCaptureMetadataOutput.availableMetadataObjectTypes](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616289-availablemetadataobjecttypes)Added [AVCaptureMetadataOutput.metadataObjectTypes](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616299-metadataobjecttypes)Added [AVCaptureMetadataOutput.metadataObjectsCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616307-metadataobjectscallbackqueue)Added [AVCaptureMetadataOutput.metadataObjectsDelegate](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616300-metadataobjectsdelegate)Added [-[AVCaptureMetadataOutput setMetadataObjectsDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616309-setmetadataobjectsdelegate)Added [AVCaptureMetadataOutputObjectsDelegate](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate)Added [-[AVCaptureMetadataOutputObjectsDelegate captureOutput:didOutputMetadataObjects:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/1389481-captureoutput)Added [-[AVCaptureOutput transformedMetadataObjectForMetadataObject:connection:]](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/1616310-transformedmetadataobjectformeta)Added [-[AVCaptureVideoDataOutputSampleBufferDelegate captureOutput:didDropSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1388468-captureoutput)AVCaptureSession.hAdded [AVCaptureConnection.automaticallyAdjustsVideoMirroring](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1387082-automaticallyadjustsvideomirrori)Added [AVCaptureConnection.enablesVideoStabilizationWhenAvailable](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620482-enablesvideostabilizationwhenava)Added [AVCaptureConnection.supportsVideoStabilization](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620481-supportsvideostabilization)Added [AVCaptureConnection.videoPreviewLayer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1390614-videopreviewlayer)Added [AVCaptureConnection.videoStabilizationEnabled](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620485-videostabilizationenabled)Added [AVVideoFieldMode](https://developer.apple.com/documentation/avfoundation/avvideofieldmode)Added [AVVideoFieldModeBoth](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodeboth)Added [AVVideoFieldModeBottomOnly](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodebottomonly)Added [AVVideoFieldModeDeinterlace](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodedeinterlace)Added [AVVideoFieldModeTopOnly](https://developer.apple.com/documentation/avfoundation/avvideofieldmode/avvideofieldmodetoponly)AVCaptureVideoPreviewLayer.hAdded [-[AVCaptureVideoPreviewLayer captureDevicePointOfInterestForPoint:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623497-capturedevicepointconverted)Added [AVCaptureVideoPreviewLayer.connection](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1390893-connection)Added [-[AVCaptureVideoPreviewLayer pointForCaptureDevicePointOfInterest:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623502-layerpointconverted)Added [-[AVCaptureVideoPreviewLayer transformedMetadataObjectForMetadataObject:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623501-transformedmetadataobjectformeta)Modified [AVCaptureVideoPreviewLayer.mirrored](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623493-mirrored)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVCaptureVideoPreviewLayer.orientationSupported](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623499-orientationsupported)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVCaptureVideoPreviewLayer.automaticallyAdjustsMirroring](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623496-automaticallyadjustsmirroring)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVCaptureVideoPreviewLayer.orientation](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623494-orientation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVCaptureVideoPreviewLayer.mirroringSupported](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623500-mirroringsupported)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

AVError.hAdded [AVErrorDisplayWasDisabled](https://developer.apple.com/documentation/avfoundation/averror/code/displaywasdisabled)Added [AVErrorFailedToLoadMediaData](https://developer.apple.com/documentation/avfoundation/averror/code/failedtoloadmediadata)Added [AVErrorIncompatibleAsset](https://developer.apple.com/documentation/avfoundation/averror/averrorincompatibleasset)Added [AVErrorOperationInterrupted](https://developer.apple.com/documentation/avfoundation/averror/code/operationinterrupted)Added [AVErrorScreenCaptureFailed](https://developer.apple.com/documentation/avfoundation/averror/averrorscreencapturefailed)Added [AVErrorServerIncorrectlyConfigured](https://developer.apple.com/documentation/avfoundation/averror/code/serverincorrectlyconfigured)Added [AVErrorTorchLevelUnavailable](https://developer.apple.com/documentation/avfoundation/averror/averrortorchlevelunavailable)AVMediaFormat.hRemoved AVMediaTypeTimedMetadataAdded [AVMediaCharacteristicEasyToRead](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1389453-easytoread)Added [AVMediaTypeMetadata](https://developer.apple.com/documentation/avfoundation/avmediatypemetadata)AVMediaSelectionGroup.hAdded [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387034-mediaselectionoptions)Modified [+[AVMediaSelectionGroup playableMediaSelectionOptionsFromArray:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387351-playablemediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | + (NSArray \*)playableMediaSelectionOptionsFromArray:(NSArray \*)array |
| To | + (NSArray \*)playableMediaSelectionOptionsFromArray:(NSArray \*)mediaSelectionOptions |

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388258-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | + (NSArray \*)mediaSelectionOptionsFromArray:(NSArray \*)array withMediaCharacteristics:(NSArray \*)mediaCharacteristics |
| To | + (NSArray \*)mediaSelectionOptionsFromArray:(NSArray \*)mediaSelectionOptions withMediaCharacteristics:(NSArray \*)mediaCharacteristics |

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withLocale:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387494-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | + (NSArray \*)mediaSelectionOptionsFromArray:(NSArray \*)array withLocale:(NSLocale \*)locale |
| To | + (NSArray \*)mediaSelectionOptionsFromArray:(NSArray \*)mediaSelectionOptions withLocale:(NSLocale \*)locale |

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withoutMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387631-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | + (NSArray \*)mediaSelectionOptionsFromArray:(NSArray \*)array withoutMediaCharacteristics:(NSArray \*)mediaCharacteristics |
| To | + (NSArray \*)mediaSelectionOptionsFromArray:(NSArray \*)mediaSelectionOptions withoutMediaCharacteristics:(NSArray \*)mediaCharacteristics |

AVMetadataItem.hAdded [+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387901-metadataitemsfromarray)Modified [+[AVMetadataItem metadataItemsFromArray:withKey:keySpace:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386083-metadataitems)

|  | Declaration |
| --- | --- |
| From | + (NSArray \*)metadataItemsFromArray:(NSArray \*)array withKey:(id)key keySpace:(NSString \*)keySpace |
| To | + (NSArray \*)metadataItemsFromArray:(NSArray \*)metadataItems withKey:(id)key keySpace:(NSString \*)keySpace |

Modified [+[AVMetadataItem metadataItemsFromArray:withLocale:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389374-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | + (NSArray \*)metadataItemsFromArray:(NSArray \*)array withLocale:(NSLocale \*)locale |
| To | + (NSArray \*)metadataItemsFromArray:(NSArray \*)metadataItems withLocale:(NSLocale \*)locale |

AVMetadataObject.hAdded [AVMetadataFaceObject](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject)Added [AVMetadataFaceObject.faceID](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/1386945-faceid)Added [AVMetadataFaceObject.hasRollAngle](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/1386866-hasrollangle)Added [AVMetadataFaceObject.hasYawAngle](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/1385888-hasyawangle)Added [AVMetadataFaceObject.rollAngle](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/1389110-rollangle)Added [AVMetadataFaceObject.yawAngle](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/1386517-yawangle)Added [AVMetadataObject](https://developer.apple.com/documentation/avfoundation/avmetadataobject)Added [AVMetadataObject.bounds](https://developer.apple.com/documentation/avfoundation/avmetadataobject/1386043-bounds)Added [AVMetadataObject.duration](https://developer.apple.com/documentation/avfoundation/avmetadataobject/1386827-duration)Added [AVMetadataObject.time](https://developer.apple.com/documentation/avfoundation/avmetadataobject/1388593-time)Added [AVMetadataObject.type](https://developer.apple.com/documentation/avfoundation/avmetadataobject/1387841-type)Added [AVMetadataObjectTypeFace](https://developer.apple.com/documentation/avfoundation/avmetadataobjecttypeface)AVPlayer.hAdded [AVPlayer.allowsExternalPlayback](https://developer.apple.com/documentation/avfoundation/avplayer/1387441-allowsexternalplayback)Added [-[AVPlayer cancelPendingPrerolls]](https://developer.apple.com/documentation/avfoundation/avplayer/1388260-cancelpendingprerolls)Added [AVPlayer.externalPlaybackActive](https://developer.apple.com/documentation/avfoundation/avplayer/1388982-externalplaybackactive)Added [AVPlayer.externalPlaybackVideoGravity](https://developer.apple.com/documentation/avfoundation/avplayer/1624251-externalplaybackvideogravity)Added [AVPlayer.masterClock](https://developer.apple.com/documentation/avfoundation/avplayer/1387066-masterclock)Added [AVPlayer.outputObscuredDueToInsufficientExternalProtection](https://developer.apple.com/documentation/avfoundation/avplayer/1624254-outputobscuredduetoinsufficiente)Added [-[AVPlayer prerollAtRate:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1389712-preroll)Added [-[AVPlayer seekToDate:]](https://developer.apple.com/documentation/avfoundation/avplayer/1386114-seektodate)Added [-[AVPlayer seekToDate:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1386108-seek)Added [-[AVPlayer setRate:time:atHostTime:]](https://developer.apple.com/documentation/avfoundation/avplayer/1386591-setrate)Added [AVPlayer.usesExternalPlaybackWhileExternalScreenIsActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624255-usesexternalplaybackwhileexterna)Added AVPlayer(AVPlayerAdvancedRateControl)Added AVPlayer(AVPlayerExternalPlaybackSupport)Added AVPlayer(AVPlayerProtectedContent)Modified [AVPlayer.allowsAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avplayer/1624258-allowsairplayvideo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVPlayer.usesAirPlayVideoWhileAirPlayScreenIsActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624256-usesairplayvideowhileairplayscre)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [AVPlayer.airPlayVideoActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624259-airplayvideoactive)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

AVPlayerItem.hAdded [-[AVPlayerItem addOutput:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389782-add)Added [AVPlayerItem.canPlayReverse](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385591-canplayreverse)Added [AVPlayerItem.canPlaySlowForward](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388078-canplayslowforward)Added [AVPlayerItem.canPlaySlowReverse](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390598-canplayslowreverse)Added [AVPlayerItem.canStepBackward](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386796-canstepbackward)Added [AVPlayerItem.canStepForward](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389656-canstepforward)Added [AVPlayerItem.outputs](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389090-outputs)Added [-[AVPlayerItem removeOutput:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388756-removeoutput)Added [-[AVPlayerItem seekToDate:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389877-seektodate)Added [AVPlayerItem.seekingWaitsForVideoCompositionRendering](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385726-seekingwaitsforvideocompositionr)Added [AVPlayerItem.textStyleRules](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389681-textstylerules)Added [AVPlayerItem.timebase](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387605-timebase)Added [AVPlayerItemAccessLogEvent.numberOfMediaRequests](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388357-numberofmediarequests)Added AVPlayerItem(AVPlayerItemOutputs)Added AVPlayerItem(AVPlayerItemRateAndSteppingSupport)Added [AVPlayerItemNewAccessLogEntryNotification](https://developer.apple.com/documentation/avfoundation/avplayeritemnewaccesslogentrynotification)Added [AVPlayerItemNewErrorLogEntryNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1388450-avplayeritemnewerrorlogentry)Added [AVPlayerItemPlaybackStalledNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1387661-avplayeritemplaybackstalled)AVPlayerItemOutput.hAdded [AVPlayerItemOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput)Added [-[AVPlayerItemOutput itemTimeForHostTime:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/1386538-itemtime)Added [-[AVPlayerItemOutput itemTimeForMachAbsoluteTime:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/1386962-itemtime)Added [AVPlayerItemOutput.suppressesPlayerRendering](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/1386133-suppressesplayerrendering)Added [AVPlayerItemOutputPullDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate)Added [-[AVPlayerItemOutputPullDelegate outputMediaDataWillChange:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/1387498-outputmediadatawillchange)Added [-[AVPlayerItemOutputPullDelegate outputSequenceWasFlushed:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/1387279-outputsequencewasflushed)Added [AVPlayerItemVideoOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput)Added [-[AVPlayerItemVideoOutput copyPixelBufferForItemTime:itemTimeForDisplay:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386148-copypixelbufferforitemtime)Added [AVPlayerItemVideoOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1385827-delegate)Added [AVPlayerItemVideoOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1388108-delegatequeue)Added [-[AVPlayerItemVideoOutput hasNewPixelBufferForItemTime:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386444-hasnewpixelbufferforitemtime)Added [-[AVPlayerItemVideoOutput initWithPixelBufferAttributes:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1389231-initwithpixelbufferattributes)Added [-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeWithAdvanceInterval:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386046-requestnotificationofmediadatach)Added [-[AVPlayerItemVideoOutput setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386824-setdelegate)AVTextStyleRule.hAdded [AVTextStyleRule](https://developer.apple.com/documentation/avfoundation/avtextstylerule)Added [-[AVTextStyleRule initWithTextMarkupAttributes:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1385849-initwithtextmarkupattributes)Added [-[AVTextStyleRule initWithTextMarkupAttributes:textSelector:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389854-init)Added [+[AVTextStyleRule propertyListForTextStyleRules:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387970-propertylistfortextstylerules)Added [AVTextStyleRule.textMarkupAttributes](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387945-textmarkupattributes)Added [AVTextStyleRule.textSelector](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389451-textselector)Added [+[AVTextStyleRule textStyleRuleWithTextMarkupAttributes:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1584360-textstylerulewithtextmarkupattri)Added [+[AVTextStyleRule textStyleRuleWithTextMarkupAttributes:textSelector:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1584361-textstylerulewithtextmarkupattri)Added [+[AVTextStyleRule textStyleRulesFromPropertyList:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387802-textstylerulesfrompropertylist)AVVideoComposition.hAdded [+[AVVideoComposition videoCompositionWithPropertiesOfAsset:]](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1385892-init)AVVideoSettings.hAdded [AVVideoProfileLevelH264High40](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264high40)Added [AVVideoProfileLevelH264High41](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264high41)

## CFNetwork

CFNetworkDefs.hAdded #def CFN_CPP_BEGINAdded #def CFN_CPP_ENDCFNetworkErrors.hAdded [kCFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfstreamerrorhttpsproxyfailureunexpectedresponsetoconnectmethod)CFSocketStream.hAdded [kCFStreamPropertyConnectionIsCellular](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyconnectioniscellular)Added [kCFStreamPropertyNoCellular](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertynocellular)

## CoreAudio

CoreAudioTypes.hAdded AudioBufferList::AudioBufferList() (no architecture available)Added AudioChannelLayout::AudioChannelLayout() (no architecture available)Added [kAudioChannelLayoutTag_AAC_7_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_aac_7_1_b)

## CoreBluetooth

CBATTRequest.hAdded [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest)Added [CBATTRequest.central](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518995-central)Added [CBATTRequest.characteristic](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518716-characteristic)Added [CBATTRequest.offset](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518857-offset)Added [CBATTRequest.value](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518795-value)CBAdvertisementData.hAdded [CBAdvertisementDataOverflowServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataoverflowserviceuuidskey)Modified [CBAdvertisementDataLocalNameKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatalocalnamekey)

|  | Header |
| --- | --- |
| From | CBCentralManager.h |
| To | CBAdvertisementData.h |

Modified [CBAdvertisementDataTxPowerLevelKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatatxpowerlevelkey)

|  | Header |
| --- | --- |
| From | CBCentralManager.h |
| To | CBAdvertisementData.h |

Modified [CBAdvertisementDataServiceDataKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataservicedatakey)

|  | Header |
| --- | --- |
| From | CBCentralManager.h |
| To | CBAdvertisementData.h |

Modified [CBAdvertisementDataManufacturerDataKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatamanufacturerdatakey)

|  | Header |
| --- | --- |
| From | CBCentralManager.h |
| To | CBAdvertisementData.h |

Modified [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey)

|  | Header |
| --- | --- |
| From | CBCentralManager.h |
| To | CBAdvertisementData.h |

CBCentral.hAdded [CBCentral](https://developer.apple.com/documentation/corebluetooth/cbcentral)Added CBCentral.UUIDCBCentralManager.hAdded [CBConnectPeripheralOptionNotifyOnConnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonconnectionkey)Added [CBConnectPeripheralOptionNotifyOnNotificationKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonnotificationkey)Added NS_ENUM() (no architecture available)Modified [-[CBCentralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | - (CBCentralManager \*)initWithDelegate:(id < CBCentralManagerDelegate >)delegate queue:(dispatch_queue_t)queue |
| To | - (id)initWithDelegate:(id < CBCentralManagerDelegate >)delegate queue:(dispatch_queue_t)queue |

CBCharacteristic.hAdded [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)Added CBMutableCharacteristic.UUIDAdded [CBMutableCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518827-descriptors)Added [-[CBMutableCharacteristic initWithType:properties:value:permissions:]](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519073-init)Added [CBMutableCharacteristic.permissions](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518891-permissions)Added [CBMutableCharacteristic.properties](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519087-properties)Added [CBMutableCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519121-value)Added [CBAttributePermissions](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions)Added [CBAttributePermissionsReadEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/cbattributepermissionsreadencryptionrequired)Added [CBAttributePermissionsReadable](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/1519075-readable)Added [CBAttributePermissionsWriteEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/cbattributepermissionswriteencryptionrequired)Added [CBAttributePermissionsWriteable](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/1519119-writeable)Added [CBCharacteristicPropertyIndicateEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyindicateencryptionrequired)Added [CBCharacteristicPropertyNotifyEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518732-notifyencryptionrequired)Added NS_ENUM_AVAILABLE() (no architecture available)CBDescriptor.hAdded [CBMutableDescriptor](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor)Added [-[CBMutableDescriptor initWithType:value:]](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor/1518999-initwithtype)CBError.hAdded [CBATTErrorSuccess](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorsuccess)Added [CBErrorAlreadyAdvertising](https://developer.apple.com/documentation/corebluetooth/cberror/code/alreadyadvertising)Added [CBErrorConnectionTimeout](https://developer.apple.com/documentation/corebluetooth/cberror/code/connectiontimeout)Added [CBErrorInvalidHandle](https://developer.apple.com/documentation/corebluetooth/cberror/cberrorinvalidhandle)Added [CBErrorInvalidParameters](https://developer.apple.com/documentation/corebluetooth/cberror/code/invalidparameters)Added [CBErrorNotConnected](https://developer.apple.com/documentation/corebluetooth/cberror/cberrornotconnected)Added [CBErrorOperationCancelled](https://developer.apple.com/documentation/corebluetooth/cberror/code/operationcancelled)Added [CBErrorOutOfSpace](https://developer.apple.com/documentation/corebluetooth/cberror/code/outofspace)Added [CBErrorPeripheralDisconnected](https://developer.apple.com/documentation/corebluetooth/cberror/code/peripheraldisconnected)Added [CBErrorUUIDNotAllowed](https://developer.apple.com/documentation/corebluetooth/cberror/cberroruuidnotallowed)CBPeripheral.hAdded [-[CBPeripheralDelegate peripheralDidInvalidateServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1805265-peripheraldidinvalidateservices)Added [-[CBPeripheralDelegate peripheralDidUpdateName:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518801-peripheraldidupdatename)Modified [-[CBPeripheral setNotifyValue:forCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue)

|  | Declaration |
| --- | --- |
| From | - (void)setNotifyValue:(BOOL)notifyValue forCharacteristic:(CBCharacteristic \*)characteristic |
| To | - (void)setNotifyValue:(BOOL)enabled forCharacteristic:(CBCharacteristic \*)characteristic |

CBPeripheralManager.hAdded [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)Added [-[CBPeripheralManager addService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393255-add)Added [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)Added [-[CBPeripheralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393299-init)Added [CBPeripheralManager.isAdvertising](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393291-isadvertising)Added [-[CBPeripheralManager removeAllServices]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393269-removeallservices)Added [-[CBPeripheralManager removeService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393287-removeservice)Added [-[CBPeripheralManager respondToRequest:withResult:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond)Added [-[CBPeripheralManager setDesiredConnectionLatency:forCentral:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393277-setdesiredconnectionlatency)Added [-[CBPeripheralManager startAdvertising:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising)Added CBPeripheralManager.stateAdded [-[CBPeripheralManager stopAdvertising]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393275-stopadvertising)Added [-[CBPeripheralManager updateValue:forCharacteristic:onSubscribedCentrals:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue)Added [CBPeripheralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)Added [-[CBPeripheralManagerDelegate peripheralManager:central:didSubscribeToCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393261-peripheralmanager)Added [-[CBPeripheralManagerDelegate peripheralManager:central:didUnsubscribeFromCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393289-peripheralmanager)Added [-[CBPeripheralManagerDelegate peripheralManager:didAddService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393279-peripheralmanager)Added [-[CBPeripheralManagerDelegate peripheralManager:didReceiveReadRequest:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager)Added [-[CBPeripheralManagerDelegate peripheralManager:didReceiveWriteRequests:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager)Added [-[CBPeripheralManagerDelegate peripheralManagerDidStartAdvertising:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393321-peripheralmanagerdidstartadverti)Added [-[CBPeripheralManagerDelegate peripheralManagerDidUpdateState:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393271-peripheralmanagerdidupdatestate)Added [-[CBPeripheralManagerDelegate peripheralManagerIsReadyToUpdateSubscribers:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393248-peripheralmanagerisreadytoupdate)Added [CBPeripheralManagerConnectionLatency](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency)Added [CBPeripheralManagerConnectionLatencyHigh](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency/high)Added [CBPeripheralManagerConnectionLatencyLow](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency/cbperipheralmanagerconnectionlatencylow)Added [CBPeripheralManagerConnectionLatencyMedium](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency/medium)Added [CBPeripheralManagerState](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)Added [CBPeripheralManagerStatePoweredOff](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstatepoweredoff)Added [CBPeripheralManagerStatePoweredOn](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstatepoweredon)Added [CBPeripheralManagerStateResetting](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/resetting)Added [CBPeripheralManagerStateUnauthorized](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstateunauthorized)Added [CBPeripheralManagerStateUnknown](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/unknown)Added [CBPeripheralManagerStateUnsupported](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/unsupported)CBService.hAdded [CBMutableService](https://developer.apple.com/documentation/corebluetooth/cbmutableservice)Added CBMutableService.UUIDAdded [CBMutableService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434317-characteristics)Added [CBMutableService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434320-includedservices)Added [-[CBMutableService initWithType:primary:]](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434330-init)Added CBMutableService.isPrimaryAdded [CBService.isPrimary](https://developer.apple.com/documentation/corebluetooth/cbservice/1434326-isprimary)

## CoreData

CoreDataDefines.hAdded [#def NSCoreDataVersionNumber10_7](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_7)Added [#def NSCoreDataVersionNumber10_7_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_7_2)Added [#def NSCoreDataVersionNumber10_7_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_7_3)Added [#def NSCoreDataVersionNumber_iPhoneOS_5_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_5_0)Added [#def NSCoreDataVersionNumber_iPhoneOS_5_1](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_5_1)

## CoreFoundation

CFBase.hAdded #def CF_CONSUMEDAdded #def CF_ENUMAdded CF_ENUM() (no architecture available)Added #def CF_ENUM_AVAILABLEAdded #def CF_ENUM_AVAILABLE_IOSAdded #def CF_ENUM_AVAILABLE_MACAdded #def CF_ENUM_DEPRECATEDAdded #def CF_ENUM_DEPRECATED_IOSAdded #def CF_ENUM_DEPRECATED_MACAdded #def CF_IMPLICIT_BRIDGING_DISABLEDAdded #def CF_IMPLICIT_BRIDGING_ENABLEDAdded #def CF_OPTIONSAdded #def CF_RELEASES_ARGUMENTAdded [#def kCFCoreFoundationVersionNumber10_6_6](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_6)Added [#def kCFCoreFoundationVersionNumber10_6_7](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_7)Added [#def kCFCoreFoundationVersionNumber10_6_8](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_8)Added [#def kCFCoreFoundationVersionNumber10_7](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7)Added [#def kCFCoreFoundationVersionNumber10_7_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_1)Added [#def kCFCoreFoundationVersionNumber10_7_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_2)Added [#def kCFCoreFoundationVersionNumber10_7_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_3)Added [#def kCFCoreFoundationVersionNumber10_7_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_4)Added [#def kCFCoreFoundationVersionNumber_iOS_4_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_4_3)Added [#def kCFCoreFoundationVersionNumber_iOS_5_0](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_5_0)Added [#def kCFCoreFoundationVersionNumber_iOS_5_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_5_1)CFCalendar.hAdded CF_OPTIONS() (no architecture available)CFData.hAdded CF_ENUM_AVAILABLE() (no architecture available)CFFileSecurity.hAdded [CFFileSecurityClearProperties()](https://developer.apple.com/documentation/corefoundation/1426500-cffilesecurityclearproperties)Added [kCFFileSecurityClearAccessControlList](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426502-accesscontrollist)Added [kCFFileSecurityClearGroup](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426529-group)Added [kCFFileSecurityClearGroupUUID](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/kcffilesecuritycleargroupuuid)Added [kCFFileSecurityClearMode](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426504-mode)Added [kCFFileSecurityClearOwner](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426515-owner)Added [kCFFileSecurityClearOwnerUUID](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/kcffilesecurityclearowneruuid)CFSocket.hAdded CF_ENUM_AVAILABLE (no architecture available)CFURL.hAdded [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1543362-securityscopeallowonlyreadaccess)Added [kCFURLBookmarkCreationWithSecurityScope](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1542198-withsecurityscope)Added [kCFURLBookmarkResolutionWithSecurityScope](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/1542878-cfurlbookmarkresolutionwithsecur)Added [kCFURLPathKey](https://developer.apple.com/documentation/corefoundation/kcfurlpathkey)Modified [kCFURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentuploadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [kCFURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

## CoreGraphics

CGDataProvider.hRemoved [CGDataProviderCallbacks](https://developer.apple.com/documentation/coregraphics/cgdataprovider/cgdataprovidercallbacks)Removed [CGDataProviderDirectAccessCallbacks](https://developer.apple.com/documentation/coregraphics/cgdataprovider/cgdataproviderdirectaccesscallbacks)Removed [CGDataProviderGetBytesAtOffsetCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovider/cgdataprovidergetbytesatoffsetcallback)Removed [CGDataProviderSkipBytesCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovider/cgdataproviderskipbytescallback)CGError.hRemoved [kCGErrorApplicationAlreadyRunning](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorapplicationalreadyrunning)Removed [kCGErrorApplicationCanOnlyBeRunInOneSessionAtATime](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorapplicationcanonlyberuninonesessionatatime)Removed [kCGErrorApplicationIncorrectExecutableFormatFound](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorapplicationincorrectexecutableformatfound)Removed [kCGErrorApplicationIsLaunching](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorapplicationislaunching)Removed [kCGErrorApplicationNotPermittedToExecute](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorapplicationnotpermittedtoexecute)Removed [kCGErrorApplicationRequiresNewerSystem](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorapplicationrequiresnewersystem)Removed [kCGErrorClassicApplicationsMustBeLaunchedByClassic](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorclassicapplicationsmustbelaunchedbyclassic)Removed kCGErrorFirstRemoved [kCGErrorForkFailed](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorforkfailed)Removed kCGErrorLastRemoved [kCGErrorNameTooLong](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrornametoolong)Removed [kCGErrorNoCurrentPoint](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrornocurrentpoint)Removed [kCGErrorRetryRegistration](https://developer.apple.com/documentation/coregraphics/core_graphics_constants/kcgerrorretryregistration)

## CoreImage

CIContext.hModified [-[CIContext drawImage:atPoint:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1473521-drawimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

CIDetector.hAdded [CIDetectorMinFeatureSize](https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize)Added [CIDetectorTracking](https://developer.apple.com/documentation/coreimage/cidetectortracking)CIFeature.hAdded [CIFaceFeature.hasTrackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437731-hastrackingframecount)Added [CIFaceFeature.hasTrackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437683-hastrackingid)Added [CIFaceFeature.trackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437953-trackingframecount)Added [CIFaceFeature.trackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437709-trackingid)CIFilter.hAdded [+[CIFilter filterArrayFromSerializedXMP:inputImageExtent:error:]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)Added [+[CIFilter serializedXMPFromFilters:inputImageExtent:]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)Added [kCIInputVersionKey](https://developer.apple.com/documentation/coreimage/kciinputversionkey)CIImage.hAdded [+[CIImage imageWithTexture:size:flipped:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1547006-imagewithtexture)Added [-[CIImage initWithTexture:size:flipped:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1438015-init)CoreImageDefines.hAdded #def CORE_IMAGE_HIDDEN

## CoreLocation

CLError.hAdded [kCLErrorDeferredAccuracyTooLow](https://developer.apple.com/documentation/corelocation/clerror/code/deferredaccuracytoolow)Added [kCLErrorDeferredCanceled](https://developer.apple.com/documentation/corelocation/clerror/code/deferredcanceled)Added [kCLErrorDeferredDistanceFiltered](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferreddistancefiltered)Added [kCLErrorDeferredFailed](https://developer.apple.com/documentation/corelocation/clerror/code/deferredfailed)Added [kCLErrorDeferredNotUpdatingLocation](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferrednotupdatinglocation)CLLocation.hAdded [CLLocationDistanceMax](https://developer.apple.com/documentation/corelocation/cllocationdistancemax)Added [CLTimeIntervalMax](https://developer.apple.com/documentation/corelocation/cltimeintervalmax)CLLocationManager.hAdded [CLLocationManager.activityType](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620567-activitytype)Added [-[CLLocationManager allowDeferredLocationUpdatesUntilTraveled:timeout:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620547-allowdeferredlocationupdatesunti)Added [+[CLLocationManager deferredLocationUpdatesAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423830-deferredlocationupdatesavailable)Added [-[CLLocationManager disallowDeferredLocationUpdates]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620565-disallowdeferredlocationupdates)Added [CLLocationManager.pausesLocationUpdatesAutomatically](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620553-pauseslocationupdatesautomatical)Added [CLActivityType](https://developer.apple.com/documentation/corelocation/clactivitytype)Added [CLActivityTypeAutomotiveNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypeautomotivenavigation)Added [CLActivityTypeFitness](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypefitness)Added [CLActivityTypeOther](https://developer.apple.com/documentation/corelocation/clactivitytype/other)Added [CLActivityTypeOtherNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/othernavigation)Modified [CLLocationManager.purpose](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423742-purpose)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[CLLocationManager startMonitoringForRegion:desiredAccuracy:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620560-startmonitoringforregion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [+[CLLocationManager regionMonitoringEnabled]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423585-regionmonitoringenabled)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didFinishDeferredUpdatesWithError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager)Added [-[CLLocationManagerDelegate locationManager:didUpdateLocations:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)Added [-[CLLocationManagerDelegate locationManagerDidPauseLocationUpdates:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621553-locationmanagerdidpauselocationu)Added [-[CLLocationManagerDelegate locationManagerDidResumeLocationUpdates:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621512-locationmanagerdidresumelocation)Modified [-[CLLocationManagerDelegate locationManager:didUpdateToLocation:fromLocation:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423716-locationmanager)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

## CoreMedia

CMAudioClock.hAdded [CMAudioClockCreate()](https://developer.apple.com/documentation/coremedia/1618913-cmaudioclockcreate)CMBase.hAdded #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATERAdded #def AVAILABLE_MAC_OS_X_VERSION_10_9_AND_LATERCMFormatDescription.hRemoved [kCMMediaType_TimedMetadata](https://developer.apple.com/documentation/coremedia/cmmediatype/kcmmediatype_timedmetadata)Removed [kCMTimedMetadataFormatType_Boxed](https://developer.apple.com/documentation/coremedia/cmmetadataformattype/kcmtimedmetadataformattype_boxed)Removed [kCMTimedMetadataFormatType_ICY](https://developer.apple.com/documentation/coremedia/cmmetadataformattype/kcmtimedmetadataformattype_icy)Removed [kCMTimedMetadataFormatType_ID3](https://developer.apple.com/documentation/coremedia/cmmetadataformattype/kcmtimedmetadataformattype_id3)Added #def CMSubtitleFormatDescriptionGetFormatTypeAdded [CMSubtitleFormatType](https://developer.apple.com/documentation/coremedia/cmsubtitleformattype)Added [kCMFormatDescriptionColorPrimaries_P22](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_p22)Added [kCMMediaType_Metadata](https://developer.apple.com/documentation/coremedia/kcmmediatype_metadata)Added [kCMMetadataFormatType_Boxed](https://developer.apple.com/documentation/coremedia/kcmmetadataformattype_boxed)Added [kCMMetadataFormatType_ICY](https://developer.apple.com/documentation/coremedia/kcmmetadataformattype_icy)Added [kCMMetadataFormatType_ID3](https://developer.apple.com/documentation/coremedia/1564222-cmmetadataformattype/kcmmetadataformattype_id3)Added [kCMSubtitleFormatType_3GText](https://developer.apple.com/documentation/coremedia/1564237-cmsubtitleformattype/kcmsubtitleformattype_3gtext)Added [kCMSubtitleFormatType_WebVTT](https://developer.apple.com/documentation/coremedia/kcmsubtitleformattype_webvtt)CMMemoryPool.hAdded #def CMMEMORYPOOL_HAdded [CMMemoryPoolCreate()](https://developer.apple.com/documentation/coremedia/1489395-cmmemorypoolcreate)Added [CMMemoryPoolFlush()](https://developer.apple.com/documentation/coremedia/1489661-cmmemorypoolflush)Added [CMMemoryPoolGetAllocator()](https://developer.apple.com/documentation/coremedia/1489675-cmmemorypoolgetallocator)Added [CMMemoryPoolGetTypeID()](https://developer.apple.com/documentation/coremedia/1489215-cmmemorypoolgettypeid)Added [CMMemoryPoolInvalidate()](https://developer.apple.com/documentation/coremedia/1489674-cmmemorypoolinvalidate)Added [CMMemoryPoolRef](https://developer.apple.com/documentation/coremedia/cmmemorypoolref)Added [kCMMemoryPoolOption_AgeOutPeriod](https://developer.apple.com/documentation/coremedia/kcmmemorypooloption_ageoutperiod)CMSampleBuffer.hAdded [kCMSampleBufferAttachmentKey_DroppedFrameReason](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_droppedframereason)Added [kCMSampleBufferDroppedFrameReason_Discontinuity](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_discontinuity)Added [kCMSampleBufferDroppedFrameReason_FrameWasLate](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_framewaslate)Added [kCMSampleBufferDroppedFrameReason_OutOfBuffers](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_outofbuffers)CMSync.hAdded [CMClockConvertHostTimeToSystemUnits()](https://developer.apple.com/documentation/coremedia/1489638-cmclockconverthosttimetosystemun)Added [CMClockGetAnchorTime()](https://developer.apple.com/documentation/coremedia/1489299-cmclockgetanchortime)Added [CMClockGetHostTimeClock()](https://developer.apple.com/documentation/coremedia/1489402-cmclockgethosttimeclock)Added [CMClockGetTime()](https://developer.apple.com/documentation/coremedia/1489382-cmclockgettime)Added [CMClockGetTypeID()](https://developer.apple.com/documentation/coremedia/1489184-cmclockgettypeid)Added [CMClockInvalidate()](https://developer.apple.com/documentation/coremedia/1489202-cmclockinvalidate)Added [CMClockMakeHostTimeFromSystemUnits()](https://developer.apple.com/documentation/coremedia/1489195-cmclockmakehosttimefromsystemuni)Added [CMClockMightDrift()](https://developer.apple.com/documentation/coremedia/1489494-cmclockmightdrift)Added [CMClockOrTimebaseRef](https://developer.apple.com/documentation/coremedia/cmclockortimebaseref)Added [CMClockRef](https://developer.apple.com/documentation/coremedia/cmclockref)Added [CMSyncConvertTime()](https://developer.apple.com/documentation/coremedia/1489632-cmsyncconverttime)Added [CMSyncGetRelativeRate()](https://developer.apple.com/documentation/coremedia/1489528-cmsyncgetrelativerate)Added [CMSyncGetRelativeRateAndAnchorTime()](https://developer.apple.com/documentation/coremedia/1489570-cmsyncgetrelativerateandanchorti)Added [CMSyncGetTime()](https://developer.apple.com/documentation/coremedia/1489233-cmsyncgettime)Added [CMSyncMightDrift()](https://developer.apple.com/documentation/coremedia/1489610-cmsyncmightdrift)Added [CMTimebaseAddTimer()](https://developer.apple.com/documentation/coremedia/1489654-cmtimebaseaddtimer)Added [CMTimebaseAddTimerDispatchSource()](https://developer.apple.com/documentation/coremedia/1489429-cmtimebaseaddtimerdispatchsource)Added [CMTimebaseCreateWithMasterClock()](https://developer.apple.com/documentation/coremedia/1489367-cmtimebasecreatewithmasterclock)Added [CMTimebaseCreateWithMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489132-cmtimebasecreatewithmastertimeba)Added [CMTimebaseGetEffectiveRate()](https://developer.apple.com/documentation/coremedia/1489313-cmtimebasegeteffectiverate)Added [CMTimebaseGetMaster()](https://developer.apple.com/documentation/coremedia/1489764-cmtimebasegetmaster)Added [CMTimebaseGetMasterClock()](https://developer.apple.com/documentation/coremedia/1489691-cmtimebasegetmasterclock)Added [CMTimebaseGetMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489484-cmtimebasegetmastertimebase)Added [CMTimebaseGetRate()](https://developer.apple.com/documentation/coremedia/1489302-cmtimebasegetrate)Added [CMTimebaseGetTime()](https://developer.apple.com/documentation/coremedia/1489812-cmtimebasegettime)Added [CMTimebaseGetTimeAndRate()](https://developer.apple.com/documentation/coremedia/1489415-cmtimebasegettimeandrate)Added [CMTimebaseGetTimeWithTimeScale()](https://developer.apple.com/documentation/coremedia/1489700-cmtimebasegettimewithtimescale)Added [CMTimebaseGetTypeID()](https://developer.apple.com/documentation/coremedia/1489285-cmtimebasegettypeid)Added [CMTimebaseGetUltimateMasterClock()](https://developer.apple.com/documentation/coremedia/1489671-cmtimebasegetultimatemasterclock)Added [CMTimebaseNotificationBarrier()](https://developer.apple.com/documentation/coremedia/1489171-cmtimebasenotificationbarrier)Added [CMTimebaseRef](https://developer.apple.com/documentation/coremedia/cmtimebase)Added [CMTimebaseRemoveTimer()](https://developer.apple.com/documentation/coremedia/1489746-cmtimebaseremovetimer)Added [CMTimebaseRemoveTimerDispatchSource()](https://developer.apple.com/documentation/coremedia/1489198-cmtimebaseremovetimerdispatchsou)Added [CMTimebaseSetAnchorTime()](https://developer.apple.com/documentation/coremedia/1489504-cmtimebasesetanchortime)Added [CMTimebaseSetRate()](https://developer.apple.com/documentation/coremedia/1489590-cmtimebasesetrate)Added [CMTimebaseSetRateAndAnchorTime()](https://developer.apple.com/documentation/coremedia/1489332-cmtimebasesetrateandanchortime)Added [CMTimebaseSetTime()](https://developer.apple.com/documentation/coremedia/1489372-cmtimebasesettime)Added [CMTimebaseSetTimerDispatchSourceNextFireTime()](https://developer.apple.com/documentation/coremedia/1489489-cmtimebasesettimerdispatchsource)Added [CMTimebaseSetTimerDispatchSourceToFireImmediately()](https://developer.apple.com/documentation/coremedia/1489552-cmtimebasesettimerdispatchsource)Added [CMTimebaseSetTimerNextFireTime()](https://developer.apple.com/documentation/coremedia/1489692-cmtimebasesettimernextfiretime)Added [CMTimebaseSetTimerToFireImmediately()](https://developer.apple.com/documentation/coremedia/1489213-cmtimebasesettimertofireimmediat)Added [kCMClockError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmclockerror_allocationfailed)Added [kCMClockError_InvalidParameter](https://developer.apple.com/documentation/coremedia/1509592-cmclock_error_codes/kcmclockerror_invalidparameter)Added [kCMClockError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/1509592-cmclock_error_codes/kcmclockerror_missingrequiredparameter)Added [kCMClockError_UnsupportedOperation](https://developer.apple.com/documentation/coremedia/kcmclockerror_unsupportedoperation)Added [kCMSyncError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmsyncerror_allocationfailed)Added [kCMSyncError_InvalidParameter](https://developer.apple.com/documentation/coremedia/kcmsyncerror_invalidparameter)Added [kCMSyncError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/kcmsyncerror_missingrequiredparameter)Added [kCMSyncError_RateMustBeNonZero](https://developer.apple.com/documentation/coremedia/kcmsyncerror_ratemustbenonzero)Added [kCMTimebaseError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_allocationfailed)Added [kCMTimebaseError_InvalidParameter](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_invalidparameter)Added [kCMTimebaseError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/kcmtimebaseerror_missingrequiredparameter)Added [kCMTimebaseError_ReadOnly](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_readonly)Added [kCMTimebaseError_TimerIntervalTooShort](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_timerintervaltooshort)Added #def kCMTimebaseFarFutureCFAbsoluteTimeAdded [kCMTimebaseNotification_EffectiveRateChanged](https://developer.apple.com/documentation/coremedia/kcmtimebasenotification_effectiveratechanged)Added [kCMTimebaseNotification_TimeJumped](https://developer.apple.com/documentation/coremedia/kcmtimebasenotification_timejumped)Added #def kCMTimebaseVeryLongCFTimeIntervalCMTextMarkup.hAdded #def CMTEXTMARKUP_HAdded [kCMTextMarkupAttribute_BackgroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_backgroundcolorargb)Added [kCMTextMarkupAttribute_BoldStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_boldstyle)Added [kCMTextMarkupAttribute_FontFamilyName](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_fontfamilyname)Added [kCMTextMarkupAttribute_ForegroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_foregroundcolorargb)Added [kCMTextMarkupAttribute_ItalicStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_italicstyle)Added [kCMTextMarkupAttribute_RelativeFontSize](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_relativefontsize)Added [kCMTextMarkupAttribute_UnderlineStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_underlinestyle)

## CoreMIDI

MIDIServices.hAdded [kMIDINotPermitted](https://developer.apple.com/documentation/coremidi/kmidinotpermitted)

## CoreMotion

No changes

## CoreTelephony

CoreTelephonyDefines.hAdded [CTError](https://developer.apple.com/documentation/coretelephony/cterror)Added [kCTErrorDomainMach](https://developer.apple.com/documentation/coretelephony/1393732-anonymous/kcterrordomainmach)Added [kCTErrorDomainNoError](https://developer.apple.com/documentation/coretelephony/1393732-anonymous/kcterrordomainnoerror)Added [kCTErrorDomainPOSIX](https://developer.apple.com/documentation/coretelephony/kcterrordomainposix)

## CoreText

CTDefines.hAdded #def CT_DEPRECATED_ENUMERATORCTFont.hRemoved [CTFontCreateWithPlatformFont()](https://developer.apple.com/documentation/coretext/1510362-ctfontcreatewithplatformfont) (no architecture available)Removed [CTFontCreateWithQuickdrawInstance()](https://developer.apple.com/documentation/coretext/1509337-ctfontcreatewithquickdrawinstanc) (no architecture available)Removed [CTFontGetPlatformFont()](https://developer.apple.com/documentation/coretext/1510544-ctfontgetplatformfont) (no architecture available)Added [ATSFontRef](https://developer.apple.com/documentation/applicationservices/atsfontref) (no architecture available)Added CF_ENUM() (no architecture available)Added CF_OPTIONS() (no architecture available)Added [CTFontCopyDefaultCascadeListForLanguages()](https://developer.apple.com/documentation/coretext/1509992-ctfontcopydefaultcascadelistforl)Added [CTFontGetOpticalBoundsForGlyphs()](https://developer.apple.com/documentation/coretext/1510531-ctfontgetopticalboundsforglyphs)Added [kCTBaselineClassHanging](https://developer.apple.com/documentation/coretext/kctbaselineclasshanging)Added [kCTBaselineClassIdeographicCentered](https://developer.apple.com/documentation/coretext/kctbaselineclassideographiccentered)Added [kCTBaselineClassIdeographicHigh](https://developer.apple.com/documentation/coretext/kctbaselineclassideographichigh)Added [kCTBaselineClassIdeographicLow](https://developer.apple.com/documentation/coretext/kctbaselineclassideographiclow)Added [kCTBaselineClassMath](https://developer.apple.com/documentation/coretext/kctbaselineclassmath)Added [kCTBaselineClassRoman](https://developer.apple.com/documentation/coretext/kctbaselineclassroman)Added [kCTBaselineOriginalFont](https://developer.apple.com/documentation/coretext/kctbaselineoriginalfont)Added [kCTBaselineReferenceFont](https://developer.apple.com/documentation/coretext/kctbaselinereferencefont)Added [kCTFontTableAnkr](https://developer.apple.com/documentation/coretext/kctfonttableankr)Added [kCTFontUIFontAlertHeader](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontalertheader)Added [kCTFontUIFontApplication](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontapplication)Added [kCTFontUIFontControlContent](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontcontrolcontent)Added [kCTFontUIFontEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontemphasizedsystem)Added [kCTFontUIFontEmphasizedSystemDetail](https://developer.apple.com/documentation/coretext/ctfontuifonttype/emphasizedsystemdetail)Added [kCTFontUIFontLabel](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontlabel)Added [kCTFontUIFontMenuItem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitem)Added [kCTFontUIFontMenuItemCmdKey](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitemcmdkey)Added [kCTFontUIFontMenuItemMark](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitemmark)Added [kCTFontUIFontMenuTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmenutitle)Added [kCTFontUIFontMessage](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmessage)Added [kCTFontUIFontMiniEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/miniemphasizedsystem)Added [kCTFontUIFontMiniSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/minisystem)Added [kCTFontUIFontNone](https://developer.apple.com/documentation/coretext/ctfontuifonttype/none)Added [kCTFontUIFontPalette](https://developer.apple.com/documentation/coretext/ctfontuifonttype/palette)Added [kCTFontUIFontPushButton](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontpushbutton)Added [kCTFontUIFontSmallEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsmallemphasizedsystem)Added [kCTFontUIFontSmallSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsmallsystem)Added [kCTFontUIFontSmallToolbar](https://developer.apple.com/documentation/coretext/ctfontuifonttype/smalltoolbar)Added [kCTFontUIFontSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsystem)Added [kCTFontUIFontSystemDetail](https://developer.apple.com/documentation/coretext/ctfontuifonttype/systemdetail)Added [kCTFontUIFontToolTip](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifonttooltip)Added [kCTFontUIFontToolbar](https://developer.apple.com/documentation/coretext/ctfontuifonttype/toolbar)Added [kCTFontUIFontUser](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontuser)Added [kCTFontUIFontUserFixedPitch](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontuserfixedpitch)Added [kCTFontUIFontUtilityWindowTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontutilitywindowtitle)Added [kCTFontUIFontViews](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontviews)Added [kCTFontUIFontWindowTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontwindowtitle)Modified [CTFontCopyLocalizedName()](https://developer.apple.com/documentation/coretext/1510714-ctfontcopylocalizedname)

|  | Declaration |
| --- | --- |
| From | CFStringRef CTFontCopyLocalizedName ( CTFontRef font, CFStringRef nameKey, CFStringRef \*language); |
| To | CFStringRef CTFontCopyLocalizedName ( CTFontRef font, CFStringRef nameKey, CFStringRef \*actualLanguage); |

CTFontDescriptor.hAdded [CTFontDescriptorMatchFontDescriptorsWithProgressHandler()](https://developer.apple.com/documentation/coretext/1511433-ctfontdescriptormatchfontdescrip)Added [CTFontDescriptorMatchingState](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate)Added [CTFontDescriptorProgressHandler](https://developer.apple.com/documentation/coretext/ctfontdescriptorprogresshandler)Added [kCTFontDescriptorMatchingCurrentAssetSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingcurrentassetsize)Added [kCTFontDescriptorMatchingDescriptors](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingdescriptors)Added [kCTFontDescriptorMatchingDidBegin](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidbegin)Added [kCTFontDescriptorMatchingDidFailWithError](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfailwitherror)Added [kCTFontDescriptorMatchingDidFinish](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfinish)Added [kCTFontDescriptorMatchingDidFinishDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfinishdownloading)Added [kCTFontDescriptorMatchingDidMatch](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/didmatch)Added [kCTFontDescriptorMatchingDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdownloading)Added [kCTFontDescriptorMatchingError](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingerror)Added [kCTFontDescriptorMatchingPercentage](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingpercentage)Added [kCTFontDescriptorMatchingResult](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingresult)Added [kCTFontDescriptorMatchingSourceDescriptor](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingsourcedescriptor)Added [kCTFontDescriptorMatchingStalled](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingstalled)Added [kCTFontDescriptorMatchingTotalAssetSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingtotalassetsize)Added [kCTFontDescriptorMatchingTotalDownloadedSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingtotaldownloadedsize)Added [kCTFontDescriptorMatchingWillBeginDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/willbegindownloading)Added [kCTFontDescriptorMatchingWillBeginQuerying](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/willbeginquerying)Added [kCTFontOrientationDefault](https://developer.apple.com/documentation/coretext/ctfontorientation/default)Added [kCTFontOrientationHorizontal](https://developer.apple.com/documentation/coretext/ctfontorientation/horizontal)Added [kCTFontOrientationVertical](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontorientationvertical)CTFontTraits.hAdded [kCTFontClassClarendonSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509875-classclarendonserifs)Added [kCTFontClassFreeformSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassfreeformserifs)Added [kCTFontClassModernSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassmodernserifs)Added [kCTFontClassOldStyleSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1510458-classoldstyleserifs)Added [kCTFontClassOrnamentals](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassornamentals)Added [kCTFontClassSansSerif](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclasssansserif)Added [kCTFontClassScripts](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509011-classscripts)Added [kCTFontClassSlabSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassslabserifs)Added [kCTFontClassSymbolic](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509404-classsymbolic)Added [kCTFontClassTransitionalSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclasstransitionalserifs)Added [kCTFontClassUnknown](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassunknown)Added [kCTFontCompositeTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509332-compositetrait)Added [kCTFontTraitBold](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1510637-traitbold)Added [kCTFontTraitClassMask](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509187-traitclassmask)Added [kCTFontTraitColorGlyphs](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitcolorglyphs)Added [kCTFontTraitComposite](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1511305-traitcomposite)Added [kCTFontTraitCondensed](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1510865-traitcondensed)Added [kCTFontTraitExpanded](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1510447-traitexpanded)Added [kCTFontTraitItalic](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509535-traititalic)Added [kCTFontTraitMonoSpace](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitmonospace)Added [kCTFontTraitUIOptimized](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraituioptimized)Added [kCTFontTraitVertical](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509524-traitvertical)CTGlyphInfo.hAdded [kCTCharacterCollectionAdobeCNS1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobecns1)Added [kCTCharacterCollectionAdobeGB1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobegb1)Added [kCTCharacterCollectionAdobeJapan1](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionadobejapan1)Added [kCTCharacterCollectionAdobeJapan2](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobejapan2)Added [kCTCharacterCollectionAdobeKorea1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobekorea1)Added [kCTCharacterCollectionIdentityMapping](https://developer.apple.com/documentation/coretext/ctcharactercollection/identitymapping)CTLine.hAdded [CTLineBoundsOptions](https://developer.apple.com/documentation/coretext/ctlineboundsoptions)Added [CTLineGetBoundsWithOptions()](https://developer.apple.com/documentation/coretext/1511332-ctlinegetboundswithoptions)Added [kCTLineBoundsExcludeTypographicLeading](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1511034-excludetypographicleading)Added [kCTLineBoundsExcludeTypographicShifts](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1508724-excludetypographicshifts)Added [kCTLineBoundsUseGlyphPathBounds](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1510976-useglyphpathbounds)Added [kCTLineBoundsUseHangingPunctuation](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/kctlineboundsusehangingpunctuation)Added [kCTLineBoundsUseOpticalBounds](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/kctlineboundsuseopticalbounds)CTParagraphStyle.hAdded [kCTParagraphStyleSpecifierLineBoundsOptions](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierlineboundsoptions)Added [kCTTextAlignmentCenter](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentcenter)Added [kCTTextAlignmentJustified](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentjustified)Added [kCTTextAlignmentLeft](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentleft)Added [kCTTextAlignmentNatural](https://developer.apple.com/documentation/coretext/cttextalignment/natural)Added [kCTTextAlignmentRight](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentright)Modified [CTParagraphStyleCreate()](https://developer.apple.com/documentation/coretext/1496164-ctparagraphstylecreate)

|  | Declaration |
| --- | --- |
| From | CTParagraphStyleRef CTParagraphStyleCreate ( const CTParagraphStyleSetting \*settings, CFIndex settingCount); |
| To | CTParagraphStyleRef CTParagraphStyleCreate ( const CTParagraphStyleSetting \*settings, size_t settingCount); |

CTStringAttributes.hAdded [kCTBaselineClassAttributeName](https://developer.apple.com/documentation/coretext/kctbaselineclassattributename)Added [kCTBaselineInfoAttributeName](https://developer.apple.com/documentation/coretext/kctbaselineinfoattributename)Added [kCTBaselineReferenceInfoAttributeName](https://developer.apple.com/documentation/coretext/kctbaselinereferenceinfoattributename)Added [kCTWritingDirectionAttributeName](https://developer.apple.com/documentation/coretext/kctwritingdirectionattributename)Added [kCTWritingDirectionEmbedding](https://developer.apple.com/documentation/coretext/kctwritingdirectionembedding)Added [kCTWritingDirectionOverride](https://developer.apple.com/documentation/coretext/kctwritingdirectionoverride)CTTypesetter.hModified [kCTTypesetterOptionDisableBidiProcessing](https://developer.apple.com/documentation/coretext/kcttypesetteroptiondisablebidiprocessing)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

CoreText.hAdded [#def kCTVersionNumber10_8](https://developer.apple.com/documentation/coretext/kctversionnumber10_8)SFNTLayoutTypes.hRemoved kKERXUsesCoordinatesAdded AnchorPointAdded AnchorPointTableAdded AnkrTableAdded BslnBaselineClassAdded BslnBaselineRecordAdded BslnFormat0PartAdded BslnFormat1PartAdded BslnFormat2PartAdded BslnFormat3PartAdded BslnFormatUnionAdded BslnTableAdded BslnTableFormatAdded BslnTablePtrAdded KerxAnchorPointActionAdded OpbdSideValuesAdded OpbdTableAdded OpbdTableFormatAdded kANKRCurrentVersionAdded kAltHalfWidthTextSelectorAdded kAltProportionalTextSelectorAdded kAlternateHorizKanaOffSelectorAdded kAlternateHorizKanaOnSelectorAdded kAlternateKanaTypeAdded kAlternateVertKanaOffSelectorAdded kAlternateVertKanaOnSelectorAdded kBSLNControlPointFormatNoMapAdded kBSLNControlPointFormatWithMapAdded kBSLNCurrentVersionAdded kBSLNDistanceFormatNoMapAdded kBSLNDistanceFormatWithMapAdded kBSLNHangingBaselineAdded kBSLNIdeographicCenterBaselineAdded [kBSLNIdeographicHighBaseline](https://developer.apple.com/documentation/coretext/1446472-anonymous/kbslnideographichighbaseline)Added kBSLNIdeographicLowBaselineAdded kBSLNLastBaselineAdded kBSLNMathBaselineAdded kBSLNNoBaselineAdded kBSLNNoBaselineOverrideAdded kBSLNNumBaselineClassesAdded kBSLNRomanBaselineAdded kBSLNTagAdded kCaseSensitiveLayoutOffSelectorAdded kCaseSensitiveLayoutOnSelectorAdded kCaseSensitiveLayoutTypeAdded kCaseSensitiveSpacingOffSelectorAdded kCaseSensitiveSpacingOnSelectorAdded kContextualAlternatesOffSelectorAdded kContextualAlternatesOnSelectorAdded kContextualAlternatesTypeAdded kContextualLigaturesOffSelectorAdded kContextualLigaturesOnSelectorAdded kContextualSwashAlternatesOffSelectorAdded kContextualSwashAlternatesOnSelectorAdded kDefaultLowerCaseSelectorAdded kDefaultUpperCaseSelectorAdded kHistoricalLigaturesOffSelectorAdded kHistoricalLigaturesOnSelectorAdded kHojoCharactersSelectorAdded kJIS2004CharactersSelectorAdded kKERXActionTypeAnchorPointsAdded kKERXActionTypeControlPointsAdded kKERXActionTypeCoordinatesAdded kKERXActionTypeMaskAdded kKERXUnusedFlagsAdded kLowerCasePetiteCapsSelectorAdded kLowerCaseSmallCapsSelectorAdded kLowerCaseTypeAdded kMathematicalGreekOffSelectorAdded kMathematicalGreekOnSelectorAdded kNLCCharactersSelectorAdded kNoStylisticAlternatesSelectorAdded kOPBDControlPointFormatAdded kOPBDCurrentVersionAdded kOPBDDistanceFormatAdded kOPBDTagAdded kQuarterWidthTextSelectorAdded kScientificInferiorsSelectorAdded kStylisticAltEightOffSelectorAdded kStylisticAltEightOnSelectorAdded kStylisticAltEighteenOffSelectorAdded kStylisticAltEighteenOnSelectorAdded kStylisticAltElevenOffSelectorAdded kStylisticAltElevenOnSelectorAdded kStylisticAltFifteenOffSelectorAdded kStylisticAltFifteenOnSelectorAdded kStylisticAltFiveOffSelectorAdded kStylisticAltFiveOnSelectorAdded kStylisticAltFourOffSelectorAdded kStylisticAltFourOnSelectorAdded kStylisticAltFourteenOffSelectorAdded kStylisticAltFourteenOnSelectorAdded kStylisticAltNineOffSelectorAdded kStylisticAltNineOnSelectorAdded kStylisticAltNineteenOffSelectorAdded kStylisticAltNineteenOnSelectorAdded kStylisticAltOneOffSelectorAdded kStylisticAltOneOnSelectorAdded kStylisticAltSevenOffSelectorAdded kStylisticAltSevenOnSelectorAdded kStylisticAltSeventeenOffSelectorAdded kStylisticAltSeventeenOnSelectorAdded kStylisticAltSixOffSelectorAdded kStylisticAltSixOnSelectorAdded kStylisticAltSixteenOffSelectorAdded kStylisticAltSixteenOnSelectorAdded kStylisticAltTenOffSelectorAdded kStylisticAltTenOnSelectorAdded kStylisticAltThirteenOffSelectorAdded kStylisticAltThirteenOnSelectorAdded kStylisticAltThreeOffSelectorAdded kStylisticAltThreeOnSelectorAdded kStylisticAltTwelveOffSelectorAdded kStylisticAltTwelveOnSelectorAdded kStylisticAltTwentyOffSelectorAdded kStylisticAltTwentyOnSelectorAdded kStylisticAltTwoOffSelectorAdded kStylisticAltTwoOnSelectorAdded kStylisticAlternativesTypeAdded kSwashAlternatesOffSelectorAdded kSwashAlternatesOnSelectorAdded kThirdWidthTextSelectorAdded kTraditionalNamesCharactersSelectorAdded kUpperCasePetiteCapsSelectorAdded kUpperCaseSmallCapsSelectorAdded kUpperCaseTypeSFNTTypes.hAdded FontVariationAdded descriptorFontTableTagAdded kFontUnicode_FullRepertoireAdded nonGlyphIDAdded os2FontTableTagAdded sfntDescriptorHeaderAdded sfntFontDescriptorAdded sizeof_sfntDescriptorHeader

## CoreVideo

CVImageBuffer.hAdded [CVImageBufferIsFlipped()](https://developer.apple.com/documentation/corevideo/1418308-cvimagebufferisflipped)Added [kCVImageBufferColorPrimaries_P22](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_p22)CVOpenGLESTextureCache.hAdded #def COREVIDEO_USE_EAGLCONTEXT_CLASS_IN_APIAdded [CVEAGLContext](https://developer.apple.com/documentation/corevideo/cveaglcontext)Modified [CVOpenGLESTextureCacheCreate()](https://developer.apple.com/documentation/corevideo/1619858-cvopenglestexturecachecreate)

|  | Declaration |
| --- | --- |
| From | CVReturn CVOpenGLESTextureCacheCreate ( CFAllocatorRef allocator, CFDictionaryRef cacheAttributes, void \*eaglContext, CFDictionaryRef textureAttributes, CVOpenGLESTextureCacheRef \*cacheOut); |
| To | CVReturn CVOpenGLESTextureCacheCreate ( CFAllocatorRef allocator, CFDictionaryRef cacheAttributes, CVEAGLContext eaglContext, CFDictionaryRef textureAttributes, CVOpenGLESTextureCacheRef \*cacheOut); |

CVPixelBuffer.hAdded [kCVPixelBufferOpenGLESCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopenglescompatibilitykey)Added [kCVPixelFormatType_128RGBAFloat](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_128rgbafloat)Added [kCVPixelFormatType_64RGBAHalf](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_64rgbahalf)Added [kCVPixelFormatType_OneComponent16Half](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_onecomponent16half)Added [kCVPixelFormatType_OneComponent32Float](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_onecomponent32float)Added [kCVPixelFormatType_TwoComponent16Half](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_twocomponent16half)Added [kCVPixelFormatType_TwoComponent32Float](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_twocomponent32float)

## EventKit

EKAlarm.hAdded [EKAlarm.proximity](https://developer.apple.com/documentation/eventkit/ekalarm/1507123-proximity)Added [EKAlarm.structuredLocation](https://developer.apple.com/documentation/eventkit/ekalarm/1507331-structuredlocation)EKCalendar.hAdded [EKCalendar.allowedEntityTypes](https://developer.apple.com/documentation/eventkit/ekcalendar/1507202-allowedentitytypes)Added [+[EKCalendar calendarForEntityType:eventStore:]](https://developer.apple.com/documentation/eventkit/ekcalendar/1507516-init)Modified [+[EKCalendar calendarWithEventStore:]](https://developer.apple.com/documentation/eventkit/ekcalendar/1620447-calendarwitheventstore)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

EKCalendarItem.hAdded [EKCalendarItem.calendarItemExternalIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507283-calendaritemexternalidentifier)Added [EKCalendarItem.calendarItemIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507075-calendaritemidentifier)Modified [EKCalendarItem.UUID](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1623897-uuid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

EKError.hAdded [EKErrorAlarmProximityNotSupported](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroralarmproximitynotsupported)Added [EKErrorCalendarDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendardoesnotallowevents)Added [EKErrorCalendarDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerror/code/calendardoesnotallowreminders)Added [EKErrorInvalidEntityType](https://developer.apple.com/documentation/eventkit/ekerror/code/invalidentitytype)Added [EKErrorPriorityIsInvalid](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorpriorityisinvalid)Added [EKErrorRecurringReminderRequiresDueDate](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorrecurringreminderrequiresduedate)Added [EKErrorReminderLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorreminderlocationsnotsupported)Added [EKErrorSourceDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorsourcedoesnotallowreminders)Added [EKErrorStructuredLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/structuredlocationsnotsupported)EKEvent.hRemoved [EKEvent.recurrenceRule](https://developer.apple.com/documentation/eventkit/ekevent/1804716-recurrencerule)EKEventStore.hAdded [+[EKEventStore authorizationStatusForEntityType:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507239-authorizationstatus)Added [-[EKEventStore calendarItemWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritem)Added [-[EKEventStore calendarItemsWithExternalIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritems)Added [-[EKEventStore calendarsForEntityType:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendars)Added [-[EKEventStore cancelFetchRequest:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507342-cancelfetchrequest)Added [-[EKEventStore defaultCalendarForNewReminders]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507543-defaultcalendarfornewreminders)Added [-[EKEventStore fetchRemindersMatchingPredicate:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate)Added [-[EKEventStore predicateForCompletedRemindersWithCompletionDateStarting:ending:calendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507447-predicateforcompletedreminders)Added [-[EKEventStore predicateForIncompleteRemindersWithDueDateStarting:ending:calendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507143-predicateforincompletereminders)Added [-[EKEventStore predicateForRemindersInCalendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507086-predicateforreminders)Added [-[EKEventStore removeReminder:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507108-remove)Added [-[EKEventStore requestAccessToEntityType:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess)Added [-[EKEventStore saveReminder:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507181-savereminder)Added [EKAuthorizationStatus](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)Added [EKAuthorizationStatusAuthorized](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusauthorized)Added [EKAuthorizationStatusDenied](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/denied)Added [EKAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusnotdetermined)Added [EKAuthorizationStatusRestricted](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/restricted)Added [EKEventStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler)Added NS_ENUM() (no architecture available)Modified [EKEventStore.calendars](https://developer.apple.com/documentation/eventkit/ekeventstore/1623680-calendars)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

EKParticipant.hAdded EKParticipant.isCurrentUserEKRecurrenceDayOfWeek.hModified [+[EKRecurrenceDayOfWeek dayOfWeek:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448589-dayofweek)

|  | Declaration |
| --- | --- |
| From | + (id)dayOfWeek:(NSInteger)dayOfTheWeek |
| To | + (EKRecurrenceDayOfWeek \*)dayOfWeek:(NSInteger)dayOfTheWeek |

Modified [+[EKRecurrenceDayOfWeek dayOfWeek:weekNumber:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448591-init)

|  | Declaration |
| --- | --- |
| From | + (id)dayOfWeek:(NSInteger)dayOfTheWeek weekNumber:(NSInteger)weekNumber |
| To | + (EKRecurrenceDayOfWeek \*)dayOfWeek:(NSInteger)dayOfTheWeek weekNumber:(NSInteger)weekNumber |

EKReminder.hAdded [EKReminder](https://developer.apple.com/documentation/eventkit/ekreminder)Added [EKReminder.completed](https://developer.apple.com/documentation/eventkit/ekreminder/1507502-iscompleted)Added [EKReminder.completionDate](https://developer.apple.com/documentation/eventkit/ekreminder/1507286-completiondate)Added [EKReminder.dueDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents)Added [EKReminder.priority](https://developer.apple.com/documentation/eventkit/ekreminder/1507173-priority)Added [+[EKReminder reminderWithEventStore:]](https://developer.apple.com/documentation/eventkit/ekreminder/1507429-init)Added [EKReminder.startDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507558-startdatecomponents)EKSource.hAdded [-[EKSource calendarsForEntityType:]](https://developer.apple.com/documentation/eventkit/eksource/1507387-calendarsforentitytype)Modified [EKSource.calendars](https://developer.apple.com/documentation/eventkit/eksource/1624237-calendars)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

EKStructuredLocation.hAdded [EKStructuredLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation)Added [EKStructuredLocation.geoLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507110-geolocation)Added [+[EKStructuredLocation locationWithTitle:]](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507366-init)Added [EKStructuredLocation.radius](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507489-radius)Added [EKStructuredLocation.title](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507137-title)EKTypes.hAdded [EKAlarmProximity](https://developer.apple.com/documentation/eventkit/ekalarmproximity)Added [EKAlarmProximityEnter](https://developer.apple.com/documentation/eventkit/ekalarmproximity/ekalarmproximityenter)Added [EKAlarmProximityLeave](https://developer.apple.com/documentation/eventkit/ekalarmproximity/leave)Added [EKAlarmProximityNone](https://developer.apple.com/documentation/eventkit/ekalarmproximity/ekalarmproximitynone)Added [EKEntityMask](https://developer.apple.com/documentation/eventkit/ekentitymask)Added [EKEntityMaskEvent](https://developer.apple.com/documentation/eventkit/ekentitymask/1451980-event)Added [EKEntityMaskReminder](https://developer.apple.com/documentation/eventkit/ekentitymask/ekentitymaskreminder)Added [EKEntityType](https://developer.apple.com/documentation/eventkit/ekentitytype)Added [EKEntityTypeEvent](https://developer.apple.com/documentation/eventkit/ekentitytype/event)Added [EKEntityTypeReminder](https://developer.apple.com/documentation/eventkit/ekentitytype/reminder)

## EventKitUI

EKCalendarChooser.hAdded [-[EKCalendarChooser initWithSelectionStyle:displayStyle:entityType:eventStore:]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613977-initwithselectionstyle)EKEventEditViewController.hAdded [-[EKEventEditViewController cancelEditing]](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/1613937-cancelediting)

## ExternalAccessory

EAAccessoryManager.hAdded [-[EAAccessoryManager showBluetoothAccessoryPickerWithNameFilter:completion:]](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613913-showbluetoothaccessorypickerwith)Added [EAAccessorySelectedKey](https://developer.apple.com/documentation/externalaccessory/eaaccessoryselectedkey)Added [EABluetoothAccessoryPickerAlreadyConnected](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/code/alreadyconnected)Added [EABluetoothAccessoryPickerCompletion](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickercompletion)Added [EABluetoothAccessoryPickerErrorCode](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode)Added [EABluetoothAccessoryPickerErrorDomain](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrordomain)Added [EABluetoothAccessoryPickerResultCancelled](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/code/resultcancelled)Added [EABluetoothAccessoryPickerResultFailed](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultfailed)Added [EABluetoothAccessoryPickerResultNotFound](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultnotfound)

## Foundation

FoundationErrors.hAdded [NSFeatureUnsupportedError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsfeatureunsupportederror)Added [NSXPCConnectionErrorMaximum](https://developer.apple.com/documentation/foundation/nsxpcconnectionerrormaximum)Added [NSXPCConnectionErrorMinimum](https://developer.apple.com/documentation/foundation/nsxpcconnectionerrorminimum)Added [NSXPCConnectionInterrupted](https://developer.apple.com/documentation/foundation/nsxpcconnectioninterrupted)Added [NSXPCConnectionInvalid](https://developer.apple.com/documentation/foundation/nsxpcconnectioninvalid)Added [NSXPCConnectionReplyInvalid](https://developer.apple.com/documentation/foundation/nsxpcconnectionreplyinvalid)Added NS_ENUM_AVAILABLE (no architecture available)NSArray.hAdded -[NSArray NS_OPTIONS] (no architecture available)Added [-[NSArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsarray/1414084-subscript)Added [-[NSMutableArray setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460093-setobject)Modified [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

NSAttributedString.hAdded -[NSAttributedString NS_OPTIONS] (no architecture available)NSByteCountFormatter.hAdded [NSByteCountFormatter](https://developer.apple.com/documentation/foundation/nsbytecountformatter)Added [NSByteCountFormatter.adaptive](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1417887-adaptive)Added [NSByteCountFormatter.allowedUnits](https://developer.apple.com/documentation/foundation/bytecountformatter/1409137-allowedunits)Added [NSByteCountFormatter.allowsNonnumericFormatting](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1408929-allowsnonnumericformatting)Added [NSByteCountFormatter.countStyle](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1417194-countstyle)Added [NSByteCountFormatter.includesActualByteCount](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1411068-includesactualbytecount)Added [NSByteCountFormatter.includesCount](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1409874-includescount)Added [NSByteCountFormatter.includesUnit](https://developer.apple.com/documentation/foundation/bytecountformatter/1415784-includesunit)Added [-[NSByteCountFormatter stringFromByteCount:]](https://developer.apple.com/documentation/foundation/bytecountformatter/1415338-string)Added [+[NSByteCountFormatter stringFromByteCount:countStyle:]](https://developer.apple.com/documentation/foundation/bytecountformatter/1408178-string)Added [NSByteCountFormatter.zeroPadsFractionDigits](https://developer.apple.com/documentation/foundation/bytecountformatter/1409630-zeropadsfractiondigits)Added [NSByteCountFormatterCountStyle](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle)Added [NSByteCountFormatterCountStyleBinary](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle/nsbytecountformattercountstylebinary)Added [NSByteCountFormatterCountStyleDecimal](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle/nsbytecountformattercountstyledecimal)Added [NSByteCountFormatterCountStyleFile](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle/nsbytecountformattercountstylefile)Added [NSByteCountFormatterCountStyleMemory](https://developer.apple.com/documentation/foundation/bytecountformatter/countstyle/memory)Added [NSByteCountFormatterUnits](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits)Added [NSByteCountFormatterUseAll](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatteruseall)Added [NSByteCountFormatterUseBytes](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusebytes)Added [NSByteCountFormatterUseDefault](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusedefault)Added [NSByteCountFormatterUseEB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatteruseeb)Added [NSByteCountFormatterUseGB](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1408366-usegb)Added [NSByteCountFormatterUseKB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusekb)Added [NSByteCountFormatterUseMB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusemb)Added [NSByteCountFormatterUsePB](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1412971-usepb)Added [NSByteCountFormatterUseTB](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1408225-usetb)Added [NSByteCountFormatterUseYBOrHigher](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1418399-useyborhigher)Added [NSByteCountFormatterUseZB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusezb)Added NS_ENUM() (no architecture available)Added NS_OPTIONS() (no architecture available)NSCalendar.hAdded [-[NSDateComponents isLeapMonth]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-isleapmonth)Added [-[NSDateComponents setLeapMonth:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-leapmonth)Modified [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSCoder.hRemoved -[NSCoder NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)Added [-[NSCoder allowedClasses]](https://developer.apple.com/documentation/foundation/nscoder/1412486-allowedclasses)Added [-[NSCoder decodeObjectOfClass:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1442558-decodeobjectofclass)Added [-[NSCoder decodeObjectOfClasses:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1442560-decodeobjectofclasses)Added [-[NSCoder decodePropertyListForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1416284-decodepropertylist)Added [-[NSCoder requiresSecureCoding]](https://developer.apple.com/documentation/foundation/nscoder/1409845-requiressecurecoding)NSData.hAdded [NSDataWritingWithoutOverwriting](https://developer.apple.com/documentation/foundation/nsdatawritingoptions/nsdatawritingwithoutoverwriting)Added NS_ENUM_AVAILABLE() (no architecture available)Modified [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

NSDate.hModified [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSDateFormatter.hRemoved [NSDateFormatterBehavior10_0](https://developer.apple.com/documentation/foundation/nsdateformatterbehavior/nsdateformatterbehavior10_0) (no architecture available)Added -[NSDateFormatter NS_ENUM] (no architecture available)NSDictionary.hAdded [-[NSDictionary objectForKeyedSubscript:]](https://developer.apple.com/documentation/foundation/nsdictionary/1415430-subscript)Added [+[NSDictionary sharedKeySetForKeys:]](https://developer.apple.com/documentation/foundation/nsdictionary/1408190-sharedkeyset)Added [+[NSMutableDictionary dictionaryWithSharedKeySet:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1412658-dictionarywithsharedkeyset)Added [-[NSMutableDictionary setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574187-setobject)Added NSDictionary(NSSharedKeySetDictionary)Added NSMutableDictionary(NSSharedKeySetDictionary)Modified [-[NSMutableDictionary setObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/setObject:forKey:)

|  | Declaration |
| --- | --- |
| From | - (void)setObject:(id)anObject forKey:(id)aKey |
| To | - (void)setObject:(id)anObject forKey:(id < NSCopying >)aKey |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id[])objects forKeys:(const id[])keys count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id[])objects forKeys:(const id < NSCopying >[])keys count:(NSUInteger)cnt |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(const id[])objects forKeys:(const id[])keys count:(NSUInteger)cnt |
| To | + (id)dictionaryWithObjects:(const id[])objects forKeys:(const id < NSCopying >[])keys count:(NSUInteger)cnt |

Modified [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

Modified [+[NSDictionary dictionaryWithObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObject:forKey:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObject:(id)object forKey:(id)key |
| To | + (id)dictionaryWithObject:(id)object forKey:(id < NSCopying >)key |

NSError.hModified [NSError](https://developer.apple.com/documentation/foundation/nserror)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSFileCoordinator.hAdded [-[NSFileCoordinator itemAtURL:willMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1408668-itematurl)NSFileHandle.hModified [NSFileHandle](https://developer.apple.com/documentation/foundation/filehandle)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSSecureCoding |

NSFileManager.hAdded [-[NSFileManager ubiquityIdentityToken]](https://developer.apple.com/documentation/foundation/nsfilemanager/1408036-ubiquityidentitytoken)Added [NSUbiquityIdentityDidChangeNotification](https://developer.apple.com/documentation/foundation/nsubiquityidentitydidchangenotification)NSHashTable.hAdded [NSHashTable](https://developer.apple.com/documentation/foundation/nshashtable)Added [-[NSHashTable addObject:]](https://developer.apple.com/documentation/foundation/nshashtable/1411690-addobject)Added [-[NSHashTable allObjects]](https://developer.apple.com/documentation/foundation/nshashtable/1410223-allobjects)Added [-[NSHashTable anyObject]](https://developer.apple.com/documentation/foundation/nshashtable/1410639-anyobject)Added [-[NSHashTable containsObject:]](https://developer.apple.com/documentation/foundation/nshashtable/1415113-containsobject)Added [-[NSHashTable count]](https://developer.apple.com/documentation/foundation/nshashtable/1413142-count)Added [+[NSHashTable hashTableWithOptions:]](https://developer.apple.com/documentation/foundation/nshashtable/1415284-init)Added [-[NSHashTable initWithOptions:capacity:]](https://developer.apple.com/documentation/foundation/nshashtable/1411066-init)Added [-[NSHashTable initWithPointerFunctions:capacity:]](https://developer.apple.com/documentation/foundation/nshashtable/1416331-initwithpointerfunctions)Added [-[NSHashTable intersectHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1408509-intersect)Added [-[NSHashTable intersectsHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1416474-intersectshashtable)Added [-[NSHashTable isEqualToHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1410816-isequal)Added [-[NSHashTable isSubsetOfHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1417518-issubsetofhashtable)Added [-[NSHashTable member:]](https://developer.apple.com/documentation/foundation/nshashtable/1417991-member)Added [-[NSHashTable minusHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1414557-minushashtable)Added [-[NSHashTable objectEnumerator]](https://developer.apple.com/documentation/foundation/nshashtable/1416308-objectenumerator)Added [-[NSHashTable pointerFunctions]](https://developer.apple.com/documentation/foundation/nshashtable/1417398-pointerfunctions)Added [-[NSHashTable removeAllObjects]](https://developer.apple.com/documentation/foundation/nshashtable/1415814-removeallobjects)Added [-[NSHashTable removeObject:]](https://developer.apple.com/documentation/foundation/nshashtable/1415369-remove)Added [-[NSHashTable setRepresentation]](https://developer.apple.com/documentation/foundation/nshashtable/1414641-setrepresentation)Added [-[NSHashTable unionHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1413481-union)Added [+[NSHashTable weakObjectsHashTable]](https://developer.apple.com/documentation/foundation/nshashtable/1412241-weakobjectshashtable)Added [NSAllHashTableObjects()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSAllHashTableObjects) (no architecture available)Added [NSCompareHashTables()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCompareHashTables) (no architecture available)Added [NSCopyHashTableWithZone()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCopyHashTableWithZone) (no architecture available)Added [NSCountHashTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCountHashTable) (no architecture available)Added [NSCreateHashTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCreateHashTable) (no architecture available)Added [NSCreateHashTableWithZone()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCreateHashTableWithZone) (no architecture available)Added [NSEndHashTableEnumeration()](https://developer.apple.com/documentation/foundation/1416272-nsendhashtableenumeration) (no architecture available)Added [NSEnumerateHashTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSEnumerateHashTable) (no architecture available)Added [NSFreeHashTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSFreeHashTable) (no architecture available)Added [NSHashEnumerator](https://developer.apple.com/documentation/foundation/nshashenumerator) (no architecture available)Added [NSHashGet()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHashGet) (no architecture available)Added [NSHashInsert()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHashInsert) (no architecture available)Added [NSHashInsertIfAbsent()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHashInsertIfAbsent) (no architecture available)Added [NSHashInsertKnownAbsent()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHashInsertKnownAbsent) (no architecture available)Added [NSHashRemove()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHashRemove) (no architecture available)Added [NSHashTableCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSHashTableCallBacks) (no architecture available)Added [NSHashTableCopyIn](https://developer.apple.com/documentation/foundation/nshashtablecopyin)Added [NSHashTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nshashtableobjectpointerpersonality)Added [NSHashTableOptions](https://developer.apple.com/documentation/foundation/nshashtableoptions)Added [NSHashTableStrongMemory](https://developer.apple.com/documentation/foundation/nshashtablestrongmemory)Added [NSHashTableWeakMemory](https://developer.apple.com/documentation/foundation/nshashtablezeroingweakmemory)Added [NSNextHashEnumeratorItem()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSNextHashEnumeratorItem) (no architecture available)Added [NSNonOwnedPointerHashCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSNonOwnedPointerHashCallBacks) (no architecture available)Added [NSNonRetainedObjectHashCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSNonRetainedObjectHashCallBacks) (no architecture available)Added [NSObjectHashCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSObjectHashCallBacks) (no architecture available)Added [NSOwnedObjectIdentityHashCallBacks](https://developer.apple.com/documentation/foundation/nsownedobjectidentityhashcallbacks) (no architecture available)Added [NSOwnedPointerHashCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSOwnedPointerHashCallBacks) (no architecture available)Added [NSPointerToStructHashCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSPointerToStructHashCallBacks) (no architecture available)Added [NSResetHashTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSResetHashTable) (no architecture available)Added [NSStringFromHashTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSStringFromHashTable) (no architecture available)Added NS_ENUM_DEPRECATED_MAC (no architecture available)NSIndexPath.hModified [-[NSIndexPath initWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416906-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexes:(NSUInteger \*)indexes length:(NSUInteger)length |
| To | - (id)initWithIndexes:(const NSUInteger[])indexes length:(NSUInteger)length |

Modified [+[NSIndexPath indexPathWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1521015-indexpathwithindexes)

|  | Declaration |
| --- | --- |
| From | + (id)indexPathWithIndexes:(NSUInteger \*)indexes length:(NSUInteger)length |
| To | + (id)indexPathWithIndexes:(const NSUInteger[])indexes length:(NSUInteger)length |

NSLocale.hAdded -[NSLocale NS_ENUM] (no architecture available)Modified [NSLocale](https://developer.apple.com/documentation/foundation/nslocale)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSMapTable.hAdded [NSMapTable](https://developer.apple.com/documentation/foundation/nsmaptable)Added [-[NSMapTable count]](https://developer.apple.com/documentation/foundation/nsmaptable/1391360-count)Added [-[NSMapTable dictionaryRepresentation]](https://developer.apple.com/documentation/foundation/nsmaptable/1391402-dictionaryrepresentation)Added [-[NSMapTable initWithKeyOptions:valueOptions:capacity:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391382-init)Added [-[NSMapTable initWithKeyPointerFunctions:valuePointerFunctions:capacity:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391429-initwithkeypointerfunctions)Added [-[NSMapTable keyEnumerator]](https://developer.apple.com/documentation/foundation/nsmaptable/1391398-keyenumerator)Added [-[NSMapTable keyPointerFunctions]](https://developer.apple.com/documentation/foundation/nsmaptable/1391412-keypointerfunctions)Added [+[NSMapTable mapTableWithKeyOptions:valueOptions:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391414-init)Added [-[NSMapTable objectEnumerator]](https://developer.apple.com/documentation/foundation/nsmaptable/1391400-objectenumerator)Added [-[NSMapTable objectForKey:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391444-objectforkey)Added [-[NSMapTable removeAllObjects]](https://developer.apple.com/documentation/foundation/nsmaptable/1391386-removeallobjects)Added [-[NSMapTable removeObjectForKey:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391461-removeobjectforkey)Added [-[NSMapTable setObject:forKey:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391457-setobject)Added [+[NSMapTable strongToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391440-strongtostrongobjectsmaptable)Added [+[NSMapTable strongToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391366-strongtoweakobjectsmaptable)Added [-[NSMapTable valuePointerFunctions]](https://developer.apple.com/documentation/foundation/nsmaptable/1391467-valuepointerfunctions)Added [+[NSMapTable weakToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391346-weaktostrongobjectsmaptable)Added [+[NSMapTable weakToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391430-weaktoweakobjectsmaptable)Added [NSAllMapTableKeys()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSAllMapTableKeys) (no architecture available)Added [NSAllMapTableValues()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSAllMapTableValues) (no architecture available)Added [NSCompareMapTables()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCompareMapTables) (no architecture available)Added [NSCopyMapTableWithZone()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCopyMapTableWithZone) (no architecture available)Added [NSCountMapTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCountMapTable) (no architecture available)Added [NSCreateMapTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCreateMapTable) (no architecture available)Added [NSCreateMapTableWithZone()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCreateMapTableWithZone) (no architecture available)Added [NSEndMapTableEnumeration()](https://developer.apple.com/documentation/foundation/1391364-nsendmaptableenumeration) (no architecture available)Added [NSEnumerateMapTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSEnumerateMapTable) (no architecture available)Added [NSFreeMapTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSFreeMapTable) (no architecture available)Added [NSMapEnumerator](https://developer.apple.com/documentation/foundation/nsmapenumerator) (no architecture available)Added [NSMapGet()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapGet) (no architecture available)Added [NSMapInsert()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapInsert) (no architecture available)Added [NSMapInsertIfAbsent()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapInsertIfAbsent) (no architecture available)Added [NSMapInsertKnownAbsent()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapInsertKnownAbsent) (no architecture available)Added [NSMapMember()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapMember) (no architecture available)Added [NSMapRemove()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMapRemove) (no architecture available)Added [NSMapTableCopyIn](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptablecopyin)Added [NSMapTableKeyCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSMapTableKeyCallBacks) (no architecture available)Added [NSMapTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptableobjectpointerpersonality)Added [NSMapTableOptions](https://developer.apple.com/documentation/foundation/nsmaptableoptions)Added [NSMapTableStrongMemory](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptablestrongmemory)Added [NSMapTableValueCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSMapTableValueCallBacks) (no architecture available)Added [NSMapTableWeakMemory](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptableweakmemory)Added [NSNextMapEnumeratorPair()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSNextMapEnumeratorPair) (no architecture available)Added [NSNonOwnedPointerMapKeyCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSNonOwnedPointerMapKeyCallBacks) (no architecture available)Added [NSNonOwnedPointerMapValueCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSNonOwnedPointerMapValueCallBacks) (no architecture available)Added [NSNonOwnedPointerOrNullMapKeyCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSNonOwnedPointerOrNullMapKeyCallBacks) (no architecture available)Added [NSNonRetainedObjectMapKeyCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSNonRetainedObjectMapKeyCallBacks) (no architecture available)Added [NSNonRetainedObjectMapValueCallBacks](https://developer.apple.com/documentation/foundation/nsnonretainedobjectmapvaluecallbacks) (no architecture available)Added [NSObjectMapKeyCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSObjectMapKeyCallBacks) (no architecture available)Added [NSObjectMapValueCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSObjectMapValueCallBacks) (no architecture available)Added [NSOwnedPointerMapKeyCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSOwnedPointerMapKeyCallBacks) (no architecture available)Added [NSOwnedPointerMapValueCallBacks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSOwnedPointerMapValueCallBacks) (no architecture available)Added [NSResetMapTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSResetMapTable) (no architecture available)Added [NSStringFromMapTable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSStringFromMapTable) (no architecture available)NSNetServices.hModified [-[NSNetService getInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/netservice/1418325-getinputstream)

|  | Declaration |
| --- | --- |
| From | - (BOOL)getInputStream:(NSInputStream \*\*)inputStream outputStream:(NSOutputStream \*\*)outputStream |
| To | - (BOOL)getInputStream:(out NSInputStream \*\*)inputStream outputStream:(out NSOutputStream \*\*)outputStream |

NSNull.hModified [NSNull](https://developer.apple.com/documentation/foundation/nsnull)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSNumberFormatter.hRemoved [NSNumberFormatterBehavior10_0](https://developer.apple.com/documentation/foundation/numberformatter/behavior/behavior10_0) (no architecture available)Added -[NSNumberFormatter NS_ENUM] (no architecture available)NSObjCRuntime.hAdded [#def NSFoundationVersionNumber10_6_6](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_6)Added [#def NSFoundationVersionNumber10_6_7](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_7)Added [#def NSFoundationVersionNumber10_6_8](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_8)Added [#def NSFoundationVersionNumber10_7](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7)Added [#def NSFoundationVersionNumber10_7_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_1)Added [#def NSFoundationVersionNumber10_7_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_2)Added [#def NSFoundationVersionNumber10_7_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_3)Added [#def NSFoundationVersionNumber10_7_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_4)Added [#def NSFoundationVersionNumber_iOS_4_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_4_3)Added [#def NSFoundationVersionNumber_iOS_5_0](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_5_0)Added [#def NSFoundationVersionNumber_iOS_5_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_5_1)Added #def NS_CLASS_AVAILABLE_IOSAdded #def NS_CLASS_AVAILABLE_MACAdded #def NS_ENUMAdded #def NS_ENUM_AVAILABLEAdded #def NS_ENUM_AVAILABLE_IOSAdded #def NS_ENUM_AVAILABLE_MACAdded #def NS_ENUM_DEPRECATEDAdded #def NS_ENUM_DEPRECATED_IOSAdded #def NS_ENUM_DEPRECATED_MACAdded #def NS_OPTIONSAdded #def NS_RELEASES_ARGUMENTAdded #def NS_REPLACES_RECEIVERAdded #def NS_REQUIRES_PROPERTY_DEFINITIONSAdded #def NS_RETURNS_INNER_POINTERAdded #def NS_ROOT_CLASSAdded [#def NS_VALID_UNTIL_END_OF_SCOPE](https://developer.apple.com/documentation/foundation/ns_valid_until_end_of_scope)NSObject.hRemoved -[NSObject NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)Removed -[NSObject NS_UNAVAILABLE] (no architecture available)Added [NSSecureCoding](https://developer.apple.com/documentation/foundation/nssecurecoding)Added +[NSSecureCoding supportsSecureCoding]Modified [NSCopyObject()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCopyObject)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

NSOperation.hAdded -[NSOperation NS_ENUM] (no architecture available)NSOrderedSet.hAdded [-[NSMutableOrderedSet setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1543323-setobject)Added [-[NSOrderedSet objectAtIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414253-subscript)Modified [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

NSPathUtilities.hAdded [NSApplicationScriptsDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsapplicationscriptsdirectory)Added [NSTrashDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/trashdirectory)NSPointerArray.hAdded [NSPointerArray](https://developer.apple.com/documentation/foundation/nspointerarray)Added [-[NSPointerArray addPointer:]](https://developer.apple.com/documentation/foundation/nspointerarray/1411636-addpointer)Added [-[NSPointerArray allObjects]](https://developer.apple.com/documentation/foundation/nspointerarray/1408081-allobjects)Added [-[NSPointerArray compact]](https://developer.apple.com/documentation/foundation/nspointerarray/1413659-compact)Added [-[NSPointerArray count]](https://developer.apple.com/documentation/foundation/nspointerarray/1418453-count)Added [-[NSPointerArray initWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1408229-init)Added [-[NSPointerArray initWithPointerFunctions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1416727-init)Added [-[NSPointerArray insertPointer:atIndex:]](https://developer.apple.com/documentation/foundation/nspointerarray/1408589-insertpointer)Added [+[NSPointerArray pointerArrayWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1564845-pointerarraywithoptions)Added [+[NSPointerArray pointerArrayWithPointerFunctions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1564844-pointerarraywithpointerfunctions)Added [-[NSPointerArray pointerAtIndex:]](https://developer.apple.com/documentation/foundation/nspointerarray/1417655-pointer)Added [-[NSPointerArray pointerFunctions]](https://developer.apple.com/documentation/foundation/nspointerarray/1413669-pointerfunctions)Added [-[NSPointerArray removePointerAtIndex:]](https://developer.apple.com/documentation/foundation/nspointerarray/1407403-removepointeratindex)Added [-[NSPointerArray replacePointerAtIndex:withPointer:]](https://developer.apple.com/documentation/foundation/nspointerarray/1412654-replacepointer)Added [-[NSPointerArray setCount:]](https://developer.apple.com/documentation/foundation/nspointerarray/1418453-count)Added [+[NSPointerArray strongObjectsPointerArray]](https://developer.apple.com/documentation/foundation/nspointerarray/1413102-strongobjects)Added [+[NSPointerArray weakObjectsPointerArray]](https://developer.apple.com/documentation/foundation/nspointerarray/1412795-weakobjectspointerarray)Added NSPointerArray(NSPointerArrayConveniences)NSPointerFunctions.hAdded [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions)Added [NSPointerFunctions.acquireFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1410537-acquirefunction)Added [NSPointerFunctions.descriptionFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1415200-descriptionfunction)Added [NSPointerFunctions.hashFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1415939-hashfunction)Added [-[NSPointerFunctions initWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerfunctions/1417715-init)Added [NSPointerFunctions.isEqualFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1413473-isequalfunction)Added [+[NSPointerFunctions pointerFunctionsWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerfunctions/1451770-pointerfunctionswithoptions)Added [NSPointerFunctions.relinquishFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1408565-relinquishfunction)Added [NSPointerFunctions.sizeFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1408045-sizefunction)Added [NSPointerFunctions.usesStrongWriteBarrier](https://developer.apple.com/documentation/foundation/nspointerfunctions/1410762-usesstrongwritebarrier)Added [NSPointerFunctions.usesWeakReadAndWriteBarriers](https://developer.apple.com/documentation/foundation/nspointerfunctions/1411097-usesweakreadandwritebarriers)Added [NSPointerFunctionsCStringPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1412902-cstringpersonality)Added [NSPointerFunctionsCopyIn](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1413108-copyin)Added [NSPointerFunctionsIntegerPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsintegerpersonality)Added [NSPointerFunctionsMachVirtualMemory](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1409230-machvirtualmemory)Added [NSPointerFunctionsMallocMemory](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsmallocmemory)Added [NSPointerFunctionsObjectPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsobjectpersonality)Added [NSPointerFunctionsObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsobjectpointerpersonality)Added [NSPointerFunctionsOpaqueMemory](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsopaquememory)Added [NSPointerFunctionsOpaquePersonality](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1417363-opaquepersonality)Added [NSPointerFunctionsOptions](https://developer.apple.com/documentation/foundation/nspointerfunctions/options)Added [NSPointerFunctionsStrongMemory](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1408849-strongmemory)Added [NSPointerFunctionsStructPersonality](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsstructpersonality)Added [NSPointerFunctionsWeakMemory](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsweakmemory)NSProxy.hRemoved -[NSProxy NS_UNAVAILABLE] (no architecture available)NSSet.hModified [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id \*)objects count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id[])objects count:(NSUInteger)cnt |

Modified [+[NSSet setWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(const id \*)objects count:(NSUInteger)cnt |
| To | + (id)setWithObjects:(const id[])objects count:(NSUInteger)cnt |

NSString.hAdded -[NSString NS_OPTIONS] (no architecture available)Added [-[NSString capitalizedStringWithLocale:]](https://developer.apple.com/documentation/foundation/nsstring/1414023-capitalized)Added [-[NSString lowercaseStringWithLocale:]](https://developer.apple.com/documentation/foundation/nsstring/1417298-lowercasestringwithlocale)Added [-[NSString uppercaseStringWithLocale:]](https://developer.apple.com/documentation/foundation/nsstring/1413316-uppercased)Modified [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

NSTimeZone.hAdded -[NSTimeZone NS_ENUM] (no architecture available)Modified [NSTimeZone](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/cl/NSTimeZone)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURL.hRemoved [NSURLFileScheme](https://developer.apple.com/documentation/foundation/nsurlfilescheme)Added -[NSURL NS_ENUM_AVAILABLE] (no architecture available)Added -[NSURL NS_OPTIONS] (no architecture available)Added [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationsecurityscopeallowonlyreadaccess)Added [NSURLBookmarkCreationWithSecurityScope](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationwithsecurityscope)Added [NSURLBookmarkResolutionWithSecurityScope](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/1412803-withsecurityscope)Added [NSURLPathKey](https://developer.apple.com/documentation/foundation/nsurlpathkey)Modified [NSURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitempercentdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [NSURL](https://developer.apple.com/documentation/foundation/nsurl)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [NSURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572055-ubiquitousitempercentuploadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

NSURLRequest.hAdded [-[NSMutableURLRequest setAllowsCellularAccess:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1416749-allowscellularaccess)Added [-[NSURLRequest allowsCellularAccess]](https://developer.apple.com/documentation/foundation/nsurlrequest/1412032-allowscellularaccess)NSUUID.hAdded [NSUUID](https://developer.apple.com/documentation/foundation/nsuuid)Added [+[NSUUID UUID]](https://developer.apple.com/documentation/foundation/nsuuid/1574571-uuid)Added [-[NSUUID UUIDString]](https://developer.apple.com/documentation/foundation/nsuuid/1416585-uuidstring)Added [-[NSUUID getUUIDBytes:]](https://developer.apple.com/documentation/foundation/nsuuid/1411420-getbytes)Added [-[NSUUID init]](https://developer.apple.com/documentation/foundation/nsuuid/1415797-init)Added [-[NSUUID initWithUUIDBytes:]](https://developer.apple.com/documentation/foundation/nsuuid/1417039-init)Added [-[NSUUID initWithUUIDString:]](https://developer.apple.com/documentation/foundation/nsuuid/1411662-init)NSUbiquitousKeyValueStore.hAdded [NSUbiquitousKeyValueStoreAccountChange](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreaccountchange)NSValue.hModified [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSZone.hModified [NSRealMemoryAvailable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSRealMemoryAvailable)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

## GameKit

GKAchievement.hAdded [+[GKAchievement reportAchievements:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520509-reportachievements)Modified [GKAchievement.hidden](https://developer.apple.com/documentation/gamekit/gkachievement/1521136-ishidden)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

GKAchievementDescription.hAdded [GKAchievementDescription.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416587-groupidentifier)Added [GKAchievementDescription.replayable](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416578-replayable)GKAchievementViewController.hModified [GKAchievementViewController](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller)

|  | Superclass |
| --- | --- |
| From | UINavigationController |
| To | GKGameCenterViewController |

GKChallenge.hAdded [-[GKAchievement issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520984-issuechallenge)Added [-[GKAchievement selectChallengeablePlayerIDs:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521129-selectchallengeableplayerids)Added [GKAchievementChallenge](https://developer.apple.com/documentation/gamekit/gkachievementchallenge)Added [GKAchievementChallenge.achievement](https://developer.apple.com/documentation/gamekit/gkachievementchallenge/1520858-achievement)Added [GKChallenge](https://developer.apple.com/documentation/gamekit/gkchallenge)Added [GKChallenge.completionDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520928-completiondate)Added [-[GKChallenge decline]](https://developer.apple.com/documentation/gamekit/gkchallenge/1520675-decline)Added [GKChallenge.issueDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520803-issuedate)Added [GKChallenge.issuingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521100-issuingplayerid)Added [+[GKChallenge loadReceivedChallengesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkchallenge/1520864-loadreceivedchallenges)Added [GKChallenge.message](https://developer.apple.com/documentation/gamekit/gkchallenge/1520998-message)Added [GKChallenge.receivingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521113-receivingplayerid)Added [GKChallenge.state](https://developer.apple.com/documentation/gamekit/gkchallenge/1521179-state)Added [-[GKScore issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkscore/1520610-issuechallengetoplayers)Added [GKScoreChallenge](https://developer.apple.com/documentation/gamekit/gkscorechallenge)Added [GKScoreChallenge.score](https://developer.apple.com/documentation/gamekit/gkscorechallenge/1521014-score)Added GKAchievement(GKChallenge)Added [GKChallengeState](https://developer.apple.com/documentation/gamekit/gkchallengestate)Added [GKChallengeStateCompleted](https://developer.apple.com/documentation/gamekit/gkchallengestate/gkchallengestatecompleted)Added [GKChallengeStateDeclined](https://developer.apple.com/documentation/gamekit/gkchallengestate/declined)Added [GKChallengeStateInvalid](https://developer.apple.com/documentation/gamekit/gkchallengestate/invalid)Added [GKChallengeStatePending](https://developer.apple.com/documentation/gamekit/gkchallengestate/gkchallengestatepending)Added GKScore(GKChallenge)Added NS_ENUM() (no architecture available)GKChallengeEventHandler.hAdded [GKChallengeEventHandler](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler)Added [+[GKChallengeEventHandler challengeEventHandler]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1563241-challengeeventhandler)Added [GKChallengeEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1520556-delegate)Added [GKChallengeEventHandlerDelegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate)Added [-[GKChallengeEventHandlerDelegate localPlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521031-localplayerdidcompletechallenge)Added [-[GKChallengeEventHandlerDelegate localPlayerDidReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520987-localplayerdidreceive)Added [-[GKChallengeEventHandlerDelegate localPlayerDidSelectChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520995-localplayerdidselectchallenge)Added [-[GKChallengeEventHandlerDelegate remotePlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520880-remoteplayerdidcomplete)Added [-[GKChallengeEventHandlerDelegate shouldShowBannerForLocallyCompletedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520924-shouldshowbanner)Added [-[GKChallengeEventHandlerDelegate shouldShowBannerForLocallyReceivedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521055-shouldshowbanner)Added [-[GKChallengeEventHandlerDelegate shouldShowBannerForRemotelyCompletedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520499-shouldshowbanner)GKError.hAdded [GKErrorChallengeInvalid](https://developer.apple.com/documentation/gamekit/gkerror/code/challengeinvalid)Added [GKErrorTurnBasedInvalidParticipant](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedinvalidparticipant)Added [GKErrorTurnBasedInvalidState](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedinvalidstate)Added [GKErrorTurnBasedInvalidTurn](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedinvalidturn)Added [GKErrorTurnBasedMatchDataTooLarge](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedmatchdatatoolarge)Added [GKErrorTurnBasedTooManySessions](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedtoomanysessions)GKGameCenterViewController.hAdded [GKGameCenterControllerDelegate](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate)Added [-[GKGameCenterControllerDelegate gameCenterViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate/1520771-gamecenterviewcontrollerdidfinis)Added [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)Added [GKGameCenterViewController.gameCenterDelegate](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520845-gamecenterdelegate)Added [GKGameCenterViewController.leaderboardCategory](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520837-leaderboardcategory)Added [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)Added [GKGameCenterViewController.viewState](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1521007-viewstate)Added GKGameCenterViewController(Leaderboards)Added [GKGameCenterViewControllerState](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate)Added [GKGameCenterViewControllerStateAchievements](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/achievements)Added [GKGameCenterViewControllerStateChallenges](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/gkgamecenterviewcontrollerstatechallenges)Added [GKGameCenterViewControllerStateDefault](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/gkgamecenterviewcontrollerstatedefault)Added [GKGameCenterViewControllerStateLeaderboards](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/leaderboards)GKLeaderboard.hAdded [GKLeaderboard.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503135-groupidentifier)Added [+[GKLeaderboard loadLeaderboardsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503128-loadleaderboards)Modified [+[GKLeaderboard loadCategoriesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503155-loadcategories)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

GKLeaderboardViewController.hModified [GKLeaderboardViewController](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller)

|  | Superclass |
| --- | --- |
| From | UINavigationController |
| To | GKGameCenterViewController |

GKLocalPlayer.hAdded [GKLocalPlayer.authenticateHandler](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515399-authenticatehandler)Added [-[GKLocalPlayer loadDefaultLeaderboardCategoryIDWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515398-loaddefaultleaderboardcategoryid)Added [-[GKLocalPlayer setDefaultLeaderboardCategoryID:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515385-setdefaultleaderboardcategoryid)Modified [-[GKLocalPlayer authenticateWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515406-authenticatewithcompletionhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

GKMatch.hRemoved -[GKMatchDelegate match:connectionWithPlayerFailed:withError:]Added [-[GKMatch chooseBestHostPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502044-choosebesthostplayerwithcompleti)Added [-[GKMatch rematchWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502042-rematch)GKMatchmaker.hAdded [GKInvite.playerAttributes](https://developer.apple.com/documentation/gamekit/gkinvite/1520917-playerattributes)Added [GKInvite.playerGroup](https://developer.apple.com/documentation/gamekit/gkinvite/1520563-playergroup)Added [GKMatchRequest.defaultNumberOfPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520608-defaultnumberofplayers)Added [GKMatchRequest.inviteMessage](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521164-invitemessage)Added [GKMatchRequest.inviteeResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520511-inviteeresponsehandler)Added [+[GKMatchRequest maxPlayersAllowedForMatchOfType:]](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521150-maxplayersallowedformatch)Added [-[GKMatchmaker cancelInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520576-cancelinvite)Added [-[GKMatchmaker finishMatchmakingForMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520518-finishmatchmaking)Added [-[GKMatchmaker matchForInvite:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520847-match)Added [-[GKMatchmaker startBrowsingForNearbyPlayersWithReachableHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521023-startbrowsingfornearbyplayerswit)Added [-[GKMatchmaker stopBrowsingForNearbyPlayers]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520507-stopbrowsingfornearbyplayers)Added [GKInviteeResponse](https://developer.apple.com/documentation/gamekit/gkinviteeresponse)Added [GKInviteeResponseAccepted](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseaccepted)Added [GKInviteeResponseDeclined](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponsedeclined)Added [GKInviteeResponseFailed](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponsefailed)Added [GKInviteeResponseIncompatible](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/1521197-inviteeresponseincompatible)Added [GKInviteeResponseNoAnswer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/1520715-inviteeresponsenoanswer)Added [GKInviteeResponseUnableToConnect](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseunabletoconnect)Added [GKMatchType](https://developer.apple.com/documentation/gamekit/gkmatchtype)Added [GKMatchTypeHosted](https://developer.apple.com/documentation/gamekit/gkmatchtype/gkmatchtypehosted)Added [GKMatchTypePeerToPeer](https://developer.apple.com/documentation/gamekit/gkmatchtype/peertopeer)Added [GKMatchTypeTurnBased](https://developer.apple.com/documentation/gamekit/gkmatchtype/turnbased)Modified [-[GKMatchmaker addPlayersToMatch:matchRequest:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520561-addplayerstomatch)

|  | Declaration |
| --- | --- |
| From | - (void)addPlayersToMatch:(GKMatch \*)match matchRequest:(GKMatchRequest \*)matchRequest completionHandler:(void (^)(NSError \*))completionHandler |
| To | - (void)addPlayersToMatch:(GKMatch \*)match matchRequest:(GKMatchRequest \*)matchRequest completionHandler:(void (^)(NSError \*error))completionHandler |

GKNotificationBanner.hAdded [+[GKNotificationBanner showBannerWithTitle:message:duration:completionHandler:]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515368-showbannerwithtitle)GKPlayer.hAdded [GKPlayer.displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname)GKScore.hAdded [+[GKScore reportScores:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399252-report)GKTurnBasedMatch.hAdded [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521103-handleturnevent)Added [-[GKTurnBasedMatch acceptInviteWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520515-acceptinvite)Added [-[GKTurnBasedMatch declineInviteWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520940-declineinvite)Added [-[GKTurnBasedMatch endTurnWithNextParticipants:turnTimeout:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520765-endturnwithnextparticipants)Added [+[GKTurnBasedMatch loadMatchWithID:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521102-loadmatchwithid)Added [GKTurnBasedMatch.matchDataMaximumSize](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520731-matchdatamaximumsize)Added [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipants:turnTimeout:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520500-participantquitinturnwithoutcome)Added [-[GKTurnBasedMatch rematchWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520794-rematch)Added [-[GKTurnBasedMatch saveCurrentTurnWithMatchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520761-savecurrentturn)Added [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)Added [GKTurnTimeoutDefault](https://developer.apple.com/documentation/gamekit/gkturntimeoutdefault)Added [GKTurnTimeoutNone](https://developer.apple.com/documentation/gamekit/gkturntimeoutnone)Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[GKTurnBasedMatch endTurnWithNextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556897-endturn)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556898-participantquitinturnwithoutcome)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

GKVoiceChat.hAdded [GKVoiceChatPlayerConnecting](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate/connecting)

## GLKit

No changes

## GSS

gssapi.hRemoved #def GSSAPI_DEPRECATEDRemoved gss_store_cred()Added #def GSSAPI_CALLCONVAdded #def GSS_C_ATTR_LOCAL_LOGIN_USERAdded [#def GSS_IOV_BUFFER_FLAG_ALLOCATE](https://developer.apple.com/documentation/gss/gss_iov_buffer_flag_allocate)Added [#def GSS_IOV_BUFFER_FLAG_ALLOCATED](https://developer.apple.com/documentation/gss/gss_iov_buffer_flag_allocated)Added [#def GSS_S_BAD_MECH_ATTR](https://developer.apple.com/documentation/gss/gss_s_bad_mech_attr)Added [#def GSS_S_CRED_UNAVAIL](https://developer.apple.com/documentation/gss/gss_s_cred_unavail)Added [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)Added [gss_const_OID](https://developer.apple.com/documentation/gss/gss_const_oid)Added [gss_const_OID_set](https://developer.apple.com/documentation/gss/gss_const_oid_set)Added [gss_const_buffer_t](https://developer.apple.com/documentation/gss/gss_const_buffer_t)Added [gss_const_channel_bindings_t](https://developer.apple.com/documentation/gss/gss_const_channel_bindings_t)Added [gss_const_cred_id_t](https://developer.apple.com/documentation/gss/gss_const_cred_id_t)Added [gss_const_ctx_id_t](https://developer.apple.com/documentation/gss/gss_const_ctx_id_t)Added [gss_const_name_t](https://developer.apple.com/documentation/gss/gss_const_name_t)Added #def gss_iter_OIDAdded [#def kGSSChangePasswordNewPassword](https://developer.apple.com/documentation/gss/kgsschangepasswordnewpassword)Added [#def kGSSChangePasswordOldPassword](https://developer.apple.com/documentation/gss/kgsschangepasswordoldpassword)Added [#def kGSSICVerifyCredential](https://developer.apple.com/documentation/gss/kgssicverifycredential)gssapi_apple.hAdded #def GSS_LIB_CALLAdded #def GSS_LIB_FUNCTIONAdded #def GSS_LIB_VARIABLEModified [gss_aapl_initial_cred()](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_aapl_initial_cred ( const gss_name_t, const gss_OID, CFDictionaryRef, gss_cred_id_t \*, CFErrorRef \*); |
| To | gssapi_apple.h | OM_uint32 gss_aapl_initial_cred ( const gss_name_t, gss_const_OID, CFDictionaryRef, gss_cred_id_t \*, CFErrorRef \*); |

gssapi_oid.hAdded #def GSSAPI_GSSAPI_OIDAdded #def GSS_APPL_LKDC_SUPPORTEDAdded #def GSS_C_CRED_CERTIFICATEAdded #def GSS_C_CRED_DIAGAdded #def GSS_C_CRED_GET_DEFAULTAdded #def GSS_C_CRED_PASSWORDAdded #def GSS_C_CRED_RENEWAdded #def GSS_C_CRED_SET_DEFAULTAdded #def GSS_C_CRED_SecIdentityAdded #def GSS_C_CRED_VALIDATEAdded #def GSS_C_MA_AUTH_INITAdded #def GSS_C_MA_AUTH_INIT_ANONAdded #def GSS_C_MA_AUTH_INIT_INITAdded #def GSS_C_MA_AUTH_TARGAdded #def GSS_C_MA_AUTH_TARG_ANONAdded #def GSS_C_MA_AUTH_TARG_INITAdded #def GSS_C_MA_CBINDINGSAdded #def GSS_C_MA_COMPRESSAdded #def GSS_C_MA_CONF_PROTAdded #def GSS_C_MA_CTX_TRANSAdded #def GSS_C_MA_DELEG_CREDAdded #def GSS_C_MA_DEPRECATEDAdded #def GSS_C_MA_INTEG_PROTAdded #def GSS_C_MA_ITOK_FRAMEDAdded #def GSS_C_MA_MECH_COMPOSITEAdded #def GSS_C_MA_MECH_CONCRETEAdded #def GSS_C_MA_MECH_DESCRIPTIONAdded #def GSS_C_MA_MECH_GLUEAdded #def GSS_C_MA_MECH_NAMEAdded #def GSS_C_MA_MECH_NEGOAdded #def GSS_C_MA_MECH_PSEUDOAdded #def GSS_C_MA_MICAdded #def GSS_C_MA_NOT_DFLT_MECHAdded #def GSS_C_MA_NOT_MECHAdded #def GSS_C_MA_OOS_DETAdded #def GSS_C_MA_PFSAdded #def GSS_C_MA_PROT_READYAdded #def GSS_C_MA_REPLAY_DETAdded #def GSS_C_MA_SASL_MECH_NAMEAdded #def GSS_C_MA_WRAPAdded #def GSS_C_NTLM_FORCE_V1Added #def GSS_C_NTLM_GUESTAdded #def GSS_C_NTLM_RESET_KEYSAdded #def GSS_C_NTLM_SESSION_KEYAdded #def GSS_C_NTLM_SUPPORT_CHANNELBINDINGSAdded #def GSS_C_NTLM_SUPPORT_LM2Added #def GSS_C_NTLM_V1Added #def GSS_C_NTLM_V2Added #def GSS_C_NT_NTLMAdded #def GSS_C_NT_UUIDAdded #def GSS_NETLOGON_MECHANISMAdded #def GSS_NETLOGON_NT_NETBIOS_DNS_NAMEAdded #def GSS_NETLOGON_SET_SESSION_KEY_XAdded #def GSS_NETLOGON_SET_SIGN_ALGORITHM_XAdded #def GSS_NTLM_GET_SESSION_KEY_XAdded #def GSS_NTLM_MECHANISMModified #def GSS_KRB5_GET_AUTHTIME_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_COMPAT_DES3_MIC_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_TIME_OFFSET_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_PLUGIN_REGISTER_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_ACCEPTOR_SUBKEY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_SERVICE_KEYBLOCK_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SEND_TO_KDC_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_DNS_CANONICALIZE_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_ALLOWABLE_ENCTYPES_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_CCACHE_NAME_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_PKU2U_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_SPNEGO_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_spnego.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_REGISTER_ACCEPTOR_IDENTITY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_IAKERB_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_IMPORT_CRED_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NT_DN

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_EXPORT_LUCID_CONTEXT_V1_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_INITIATOR_SUBKEY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_EXPORT_LUCID_CONTEXT_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_DEFAULT_REALM_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_EXTRACT_AUTHZ_DATA_FROM_SEC_CONTEXT_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_PEER_HAS_UPDATED_SPNEGO

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_COPY_CCACHE_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_TKT_FLAGS_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_TIME_OFFSET_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_SUBKEY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_CRED_NO_CI_FLAGS_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

gssapi_protos.hAdded [gss_acquire_cred_with_password()](https://developer.apple.com/documentation/gss/1438426-gss_acquire_cred_with_password)Added [gss_decapsulate_token()](https://developer.apple.com/documentation/gss/1438529-gss_decapsulate_token)Added [gss_display_mech_attr()](https://developer.apple.com/documentation/gss/1438475-gss_display_mech_attr)Added [gss_encapsulate_token()](https://developer.apple.com/documentation/gss/1438463-gss_encapsulate_token)Added [gss_export_cred()](https://developer.apple.com/documentation/gss/1438500-gss_export_cred)Added [gss_import_cred()](https://developer.apple.com/documentation/gss/1438510-gss_import_cred)Added [gss_inquire_attrs_for_mech()](https://developer.apple.com/documentation/gss/1438417-gss_inquire_attrs_for_mech)Modified [gss_export_name()](https://developer.apple.com/documentation/gss/1438477-gss_export_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_cred()](https://developer.apple.com/documentation/gss/1438461-gss_release_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_oid_set()](https://developer.apple.com/documentation/gss/1438480-gss_release_oid_set)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_set_allowable_enctypes()](https://developer.apple.com/documentation/gss/1438431-gss_krb5_set_allowable_enctypes)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi_krb5.h | OM_uint32 gss_krb5_set_allowable_enctypes ( OM_uint32 \*minor_status, gss_cred_id_t cred, OM_uint32 num_enctypes, int32_t \*enctypes); |
| To | gssapi_protos.h | OM_uint32 gss_krb5_set_allowable_enctypes ( OM_uint32 \*, gss_cred_id_t, OM_uint32, int32_t \*); |

Modified [gss_pseudo_random()](https://developer.apple.com/documentation/gss/1438496-gss_pseudo_random)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_pseudo_random ( OM_uint32 \*minor_status, gss_ctx_id_t context, int prf_key, const gss_buffer_t prf_in, ssize_t desired_output_len, gss_buffer_t prf_out); |
| To | gssapi_protos.h | OM_uint32 gss_pseudo_random ( OM_uint32 \*, gss_ctx_id_t, int, const gss_buffer_t, ssize_t, gss_buffer_t); |

Modified [gss_duplicate_name()](https://developer.apple.com/documentation/gss/1438418-gss_duplicate_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_ccache_name()](https://developer.apple.com/documentation/gss/1438472-gss_krb5_ccache_name)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_seal()](https://developer.apple.com/documentation/gss/1438459-gss_seal)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_names_for_mech()](https://developer.apple.com/documentation/gss/1438523-gss_inquire_names_for_mech)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_inquire_names_for_mech ( OM_uint32 \*, const gss_OID, gss_OID_set \*); |
| To | gssapi_protos.h | OM_uint32 gss_inquire_names_for_mech ( OM_uint32 \*, gss_const_OID, gss_OID_set \*); |

Modified [gss_duplicate_oid()](https://developer.apple.com/documentation/gss/1438533-gss_duplicate_oid)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_duplicate_oid ( OM_uint32 \*, gss_OID, gss_OID \*); |
| To | gssapi_protos.h | OM_uint32 gss_duplicate_oid ( OM_uint32 \*, gss_OID, gss_OID \*dest_oid); |

Modified [gss_wrap()](https://developer.apple.com/documentation/gss/1438527-gss_wrap)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gsskrb5_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438421-gsskrb5_register_acceptor_identi)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_add_cred()](https://developer.apple.com/documentation/gss/1438473-gss_add_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_buffer_set()](https://developer.apple.com/documentation/gss/1438428-gss_release_buffer_set)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_release_buffer_set ( OM_uint32 \*minor_status, gss_buffer_set_t \*buffer_set); |
| To | gssapi_protos.h | OM_uint32 gss_release_buffer_set ( OM_uint32 \*, gss_buffer_set_t \*); |

Modified [gss_oid_to_str()](https://developer.apple.com/documentation/gss/1438512-gss_oid_to_str)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_set_sec_context_option()](https://developer.apple.com/documentation/gss/1438491-gss_set_sec_context_option)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_set_sec_context_option ( OM_uint32 \*minor_status, gss_ctx_id_t \*context_handle, const gss_OID desired_object, const gss_buffer_t value); |
| To | gssapi_protos.h | OM_uint32 gss_set_sec_context_option ( OM_uint32 \*, gss_ctx_id_t \*, const gss_OID, const gss_buffer_t); |

Modified [gss_inquire_context()](https://developer.apple.com/documentation/gss/1438458-gss_inquire_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_oid_equal()](https://developer.apple.com/documentation/gss/1438498-gss_oid_equal)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | int gss_oid_equal ( const gss_OID a, const gss_OID b); |
| To | gssapi_protos.h | int gss_oid_equal ( gss_const_OID, gss_const_OID); |

Modified [gss_delete_sec_context()](https://developer.apple.com/documentation/gss/1438435-gss_delete_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_canonicalize_name()](https://developer.apple.com/documentation/gss/1438494-gss_canonicalize_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_buffer()](https://developer.apple.com/documentation/gss/1438486-gss_release_buffer)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_destroy_cred()](https://developer.apple.com/documentation/gss/1438521-gss_destroy_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_iter_creds()](https://developer.apple.com/documentation/gss/1438515-gss_iter_creds)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_iter_creds ( OM_uint32 \*, OM_uint32 flags, gss_OID mech, void (^useriter)(gss_OID, gss_cred_id_t)); |
| To | gssapi_protos.h | OM_uint32 gss_iter_creds ( OM_uint32 \*, OM_uint32, gss_const_OID, void (^useriter)(gss_OID, gss_cred_id_t)); |

Modified [krb5_gss_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438470-krb5_gss_register_acceptor_ident)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_indicate_mechs()](https://developer.apple.com/documentation/gss/1438424-gss_indicate_mechs)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_add_oid_set_member()](https://developer.apple.com/documentation/gss/1438411-gss_add_oid_set_member)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_add_oid_set_member ( OM_uint32 \*, const gss_OID, gss_OID_set \*); |
| To | gssapi_protos.h | OM_uint32 gss_add_oid_set_member ( OM_uint32 \*, gss_const_OID, gss_OID_set \*); |

Modified [gss_test_oid_set_member()](https://developer.apple.com/documentation/gss/1438442-gss_test_oid_set_member)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_test_oid_set_member ( OM_uint32 \*, const gss_OID, const gss_OID_set, int \*); |
| To | gssapi_protos.h | OM_uint32 gss_test_oid_set_member ( OM_uint32 \*, gss_const_OID, const gss_OID_set, int \*); |

Modified [gss_context_time()](https://developer.apple.com/documentation/gss/1438487-gss_context_time)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_init_sec_context()](https://developer.apple.com/documentation/gss/1438476-gss_init_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_copy_ccache()](https://developer.apple.com/documentation/gss/1438508-gss_krb5_copy_ccache)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_create_empty_oid_set()](https://developer.apple.com/documentation/gss/1438489-gss_create_empty_oid_set)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_create_empty_buffer_set()](https://developer.apple.com/documentation/gss/1438537-gss_create_empty_buffer_set)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_create_empty_buffer_set ( OM_uint32 \*minor_status, gss_buffer_set_t \*buffer_set); |
| To | gssapi_protos.h | OM_uint32 gss_create_empty_buffer_set ( OM_uint32 \*, gss_buffer_set_t \*); |

Modified [gss_add_buffer_set_member()](https://developer.apple.com/documentation/gss/1438479-gss_add_buffer_set_member)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_add_buffer_set_member ( OM_uint32 \*minor_status, const gss_buffer_t member_buffer, gss_buffer_set_t \*buffer_set); |
| To | gssapi_protos.h | OM_uint32 gss_add_buffer_set_member ( OM_uint32 \*, const gss_buffer_t, gss_buffer_set_t \*); |

Modified [gsskrb5_extract_authz_data_from_sec_context()](https://developer.apple.com/documentation/gss/1438468-gsskrb5_extract_authz_data_from_)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_import_name()](https://developer.apple.com/documentation/gss/1438453-gss_import_name)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_import_name ( OM_uint32 \*, const gss_buffer_t, const gss_OID, gss_name_t \*); |
| To | gssapi_protos.h | OM_uint32 gss_import_name ( OM_uint32 \*, const gss_buffer_t, gss_const_OID, gss_name_t \*); |

Modified [gss_inquire_sec_context_by_oid()](https://developer.apple.com/documentation/gss/1438525-gss_inquire_sec_context_by_oid)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_inquire_sec_context_by_oid ( OM_uint32 \*minor_status, const gss_ctx_id_t context_handle, const gss_OID desired_object, gss_buffer_set_t \*data_set); |
| To | gssapi_protos.h | OM_uint32 gss_inquire_sec_context_by_oid ( OM_uint32 \*, const gss_ctx_id_t, const gss_OID, gss_buffer_set_t \*); |

Modified [gss_set_cred_option()](https://developer.apple.com/documentation/gss/1438513-gss_set_cred_option)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_set_cred_option ( OM_uint32 \*minor_status, gss_cred_id_t \*cred_handle, const gss_OID object, const gss_buffer_t value); |
| To | gssapi_protos.h | OM_uint32 gss_set_cred_option ( OM_uint32 \*, gss_cred_id_t \*, const gss_OID, const gss_buffer_t); |

Modified [gss_release_name()](https://developer.apple.com/documentation/gss/1438451-gss_release_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_display_name()](https://developer.apple.com/documentation/gss/1438464-gss_display_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_get_mic()](https://developer.apple.com/documentation/gss/1438530-gss_get_mic)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_mechs_for_name()](https://developer.apple.com/documentation/gss/1438481-gss_inquire_mechs_for_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_cred()](https://developer.apple.com/documentation/gss/1438531-gss_inquire_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_acquire_cred()](https://developer.apple.com/documentation/gss/1438466-gss_acquire_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_oid()](https://developer.apple.com/documentation/gss/1438455-gss_release_oid)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_display_status()](https://developer.apple.com/documentation/gss/1438535-gss_display_status)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_verify_mic()](https://developer.apple.com/documentation/gss/1438447-gss_verify_mic)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_wrap_size_limit()](https://developer.apple.com/documentation/gss/1438419-gss_wrap_size_limit)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_free_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438483-gss_krb5_free_lucid_sec_context)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi_krb5.h | OM_uint32 gss_krb5_free_lucid_sec_context ( OM_uint32 \*minor_status, void \*kctx); |
| To | gssapi_protos.h | OM_uint32 gss_krb5_free_lucid_sec_context ( OM_uint32 \*, void \*); |

Modified [gss_sign()](https://developer.apple.com/documentation/gss/1438416-gss_sign)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_iter_creds_f()](https://developer.apple.com/documentation/gss/1438438-gss_iter_creds_f)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_iter_creds_f ( OM_uint32 \*, OM_uint32, gss_OID, void \*, void (\*)(void \*, gss_OID, gss_cred_id_t)); |
| To | gssapi_protos.h | OM_uint32 gss_iter_creds_f ( OM_uint32 \*, OM_uint32, gss_const_OID, void \*, void (\*)(void \*, gss_OID, gss_cred_id_t)); |

Modified [gss_process_context_token()](https://developer.apple.com/documentation/gss/1438516-gss_process_context_token)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_import_sec_context()](https://developer.apple.com/documentation/gss/1438484-gss_import_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_export_sec_context()](https://developer.apple.com/documentation/gss/1438449-gss_export_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_cred_by_oid()](https://developer.apple.com/documentation/gss/1438504-gss_inquire_cred_by_oid)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_inquire_cred_by_oid ( OM_uint32 \*minor_status, const gss_cred_id_t cred_handle, const gss_OID desired_object, gss_buffer_set_t \*data_set); |
| To | gssapi_protos.h | OM_uint32 gss_inquire_cred_by_oid ( OM_uint32 \*, const gss_cred_id_t, const gss_OID, gss_buffer_set_t \*); |

Modified [gss_compare_name()](https://developer.apple.com/documentation/gss/1438437-gss_compare_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_unseal()](https://developer.apple.com/documentation/gss/1438456-gss_unseal)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_verify()](https://developer.apple.com/documentation/gss/1438414-gss_verify)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_cred_by_mech()](https://developer.apple.com/documentation/gss/1438518-gss_inquire_cred_by_mech)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_export_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438433-gss_krb5_export_lucid_sec_contex)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi_krb5.h | OM_uint32 gss_krb5_export_lucid_sec_context ( OM_uint32 \*minor_status, gss_ctx_id_t \*context_handle, OM_uint32 version, void \*\*kctx); |
| To | gssapi_protos.h | OM_uint32 gss_krb5_export_lucid_sec_context ( OM_uint32 \*, gss_ctx_id_t \*, OM_uint32, void \*\*); |

Modified [gss_unwrap()](https://developer.apple.com/documentation/gss/1438520-gss_unwrap)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_accept_sec_context()](https://developer.apple.com/documentation/gss/1438493-gss_accept_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

## iAd

ADBannerView.hAdded [ADBannerView.adType](https://developer.apple.com/documentation/iad/adbannerview/1614621-adtype)Added [-[ADBannerView initWithAdType:]](https://developer.apple.com/documentation/iad/adbannerview/1614692-initwithadtype)Added [ADAdType](https://developer.apple.com/documentation/iad/adadtype)Added [ADAdTypeBanner](https://developer.apple.com/documentation/iad/adadtype/adadtypebanner)Added [ADAdTypeMediumRectangle](https://developer.apple.com/documentation/iad/adadtype/mediumrectangle)Added [ADErrorAdUnloaded](https://developer.apple.com/documentation/iad/aderror/code/adunloaded)Added NS_ENUM() (no architecture available)Added NS_ENUM_AVAILABLE_IOS() (no architecture available)ADBannerView_Deprecated.hAdded ADBannerView(Deprecated)Modified [ADBannerView.currentContentSizeIdentifier](https://developer.apple.com/documentation/iad/adbannerview/1615513-currentcontentsizeidentifier)

|  | Header | Deprecation |
| --- | --- | --- |
| From | ADBannerView.h | _none_ |
| To | ADBannerView_Deprecated.h | iOS 6.0 |

Modified [ADBannerContentSizeIdentifier320x50](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifier320x50)

|  | Header |
| --- | --- |
| From | ADBannerView.h |
| To | ADBannerView_Deprecated.h |

Modified [ADBannerContentSizeIdentifierLandscape](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifierlandscape)

|  | Header | Deprecation |
| --- | --- | --- |
| From | ADBannerView.h | _none_ |
| To | ADBannerView_Deprecated.h | iOS 6.0 |

Modified [ADBannerContentSizeIdentifierPortrait](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifierportrait)

|  | Header | Deprecation |
| --- | --- | --- |
| From | ADBannerView.h | _none_ |
| To | ADBannerView_Deprecated.h | iOS 6.0 |

Modified [+[ADBannerView sizeFromBannerContentSizeIdentifier:]](https://developer.apple.com/documentation/iad/adbannerview/1615507-sizefrombannercontentsizeidentif)

|  | Header | Deprecation |
| --- | --- | --- |
| From | ADBannerView.h | _none_ |
| To | ADBannerView_Deprecated.h | iOS 6.0 |

Modified [ADBannerContentSizeIdentifier480x32](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifier480x32)

|  | Header |
| --- | --- |
| From | ADBannerView.h |
| To | ADBannerView_Deprecated.h |

Modified [ADBannerView.requiredContentSizeIdentifiers](https://developer.apple.com/documentation/iad/adbannerview/1615509-requiredcontentsizeidentifiers)

|  | Header | Deprecation |
| --- | --- | --- |
| From | ADBannerView.h | _none_ |
| To | ADBannerView_Deprecated.h | iOS 6.0 |

## ImageIO

No changes

## MapKit

MKDirectionsRequest.hAdded [MKDirectionsRequest](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest)Added [MKDirectionsRequest.destination](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433146-destination)Added [-[MKDirectionsRequest initWithContentsOfURL:]](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433158-init)Added [+[MKDirectionsRequest isDirectionsRequestURL:]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433150-isdirectionsrequesturl)Added [MKDirectionsRequest.source](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433144-source)MKGeometry.hAdded [-[NSValue MKCoordinateSpanValue]](https://developer.apple.com/documentation/foundation/nsvalue/1452516-mkcoordinatespanvalue)Added [-[NSValue MKCoordinateValue]](https://developer.apple.com/documentation/foundation/nsvalue/1452495-mkcoordinatevalue)Added [+[NSValue valueWithMKCoordinate:]](https://developer.apple.com/documentation/foundation/nsvalue/1452193-valuewithmkcoordinate)Added [+[NSValue valueWithMKCoordinateSpan:]](https://developer.apple.com/documentation/foundation/nsvalue/1452333-init)Added NSValue(NSValueMapKitGeometryExtensions)MKMapItem.hAdded [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem)Added [-[MKMapItem initWithPlacemark:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452285-initwithplacemark)Added [MKMapItem.isCurrentLocation](https://developer.apple.com/documentation/mapkit/mkmapitem/1452319-iscurrentlocation)Added [+[MKMapItem mapItemForCurrentLocation]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452002-mapitemforcurrentlocation)Added [MKMapItem.name](https://developer.apple.com/documentation/mapkit/mkmapitem/1452339-name)Added [-[MKMapItem openInMapsWithLaunchOptions:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions)Added [+[MKMapItem openMapsWithItems:launchOptions:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452207-openmapswithitems)Added [MKMapItem.phoneNumber](https://developer.apple.com/documentation/mapkit/mkmapitem/1452088-phonenumber)Added [MKMapItem.placemark](https://developer.apple.com/documentation/mapkit/mkmapitem/1452134-placemark)Added [MKMapItem.url](https://developer.apple.com/documentation/mapkit/mkmapitem/1452746-url)Added [MKLaunchOptionsDirectionsModeDriving](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodedriving)Added [MKLaunchOptionsDirectionsModeKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodekey)Added [MKLaunchOptionsDirectionsModeWalking](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodewalking)Added [MKLaunchOptionsMapCenterKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionsmapcenterkey)Added [MKLaunchOptionsMapSpanKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionsmapspankey)Added [MKLaunchOptionsMapTypeKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionsmaptypekey)Added [MKLaunchOptionsShowsTrafficKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionsshowstraffickey)

## MediaPlayer

MPMediaItem.hAdded [MPMediaItemPropertyBookmarkTime](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertybookmarktime)Added [MPMediaItemPropertyIsCloudItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyisclouditem)MPMediaPickerController.hAdded [MPMediaPickerController.showsCloudItems](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614675-showsclouditems)MPMoviePlayerController.hAdded [MPMoviePlayerController.readyForDisplay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620831-readyfordisplay)Added [MPMoviePlayerReadyForDisplayDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerreadyfordisplaydidchangenotification)Modified [MPMoviePlayerController.useApplicationAudioSession](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620897-useapplicationaudiosession)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

MPMusicPlayerController.hRemoved -[MPMusicPlayerController beginSeekingBackward]Removed -[MPMusicPlayerController beginSeekingForward]Removed MPMusicPlayerController.currentPlaybackTimeRemoved -[MPMusicPlayerController endSeeking]Removed -[MPMusicPlayerController pause]Removed -[MPMusicPlayerController play]Removed -[MPMusicPlayerController stop]Modified [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | MPMediaPlayback |

MPVolumeView.hAdded [-[MPVolumeView maximumVolumeSliderImageForState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620072-maximumvolumesliderimage)Added [-[MPVolumeView minimumVolumeSliderImageForState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620076-minimumvolumesliderimageforstate)Added [-[MPVolumeView routeButtonImageForState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620078-routebuttonimage)Added [-[MPVolumeView routeButtonRectForBounds:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620077-routebuttonrectforbounds)Added [-[MPVolumeView setMaximumVolumeSliderImage:forState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620074-setmaximumvolumesliderimage)Added [-[MPVolumeView setMinimumVolumeSliderImage:forState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620063-setminimumvolumesliderimage)Added [-[MPVolumeView setRouteButtonImage:forState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620069-setroutebuttonimage)Added [-[MPVolumeView setVolumeThumbImage:forState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620062-setvolumethumbimage)Added [-[MPVolumeView volumeSliderRectForBounds:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620080-volumesliderrect)Added [-[MPVolumeView volumeThumbImageForState:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620064-volumethumbimageforstate)Added [-[MPVolumeView volumeThumbRectForBounds:volumeSliderRect:value:]](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620067-volumethumbrectforbounds)

## MediaToolbox

MTAudioProcessingTap.hAdded #def MTAUDIOPROCESSINGTAP_HAdded MTAudioProcessingTapCallbacksAdded MTAudioProcessingTapCreate()Added MTAudioProcessingTapCreationFlagsAdded MTAudioProcessingTapFinalizeCallbackAdded MTAudioProcessingTapFlagsAdded MTAudioProcessingTapGetSourceAudio()Added MTAudioProcessingTapGetStorage()Added MTAudioProcessingTapGetTypeID()Added MTAudioProcessingTapInitCallbackAdded MTAudioProcessingTapPrepareCallbackAdded MTAudioProcessingTapProcessCallbackAdded MTAudioProcessingTapRefAdded MTAudioProcessingTapUnprepareCallbackAdded kMTAudioProcessingTapCallbacksVersion_0Added kMTAudioProcessingTapCreationFlag_PostEffectsAdded kMTAudioProcessingTapCreationFlag_PreEffectsAdded kMTAudioProcessingTapFlag_EndOfStreamAdded kMTAudioProcessingTapFlag_StartOfStream

## MessageUI

No changes

## MobileCoreServices

No changes

## NewsstandKit

No changes

## OpenAL

No changes

## OpenGLES

EAGL.hAdded [EAGLContext.debugLabel](https://developer.apple.com/documentation/opengles/eaglcontext/1624893-debuglabel)Added [EAGLSharegroup.debugLabel](https://developer.apple.com/documentation/opengles/eaglsharegroup/1624887-debuglabel)glext.hRemoved glGetQueryObjectivEXT()Added [#def GL_ALPHA16F_EXT](https://developer.apple.com/documentation/opengles/gl_alpha16f_ext)Added [#def GL_ALPHA32F_EXT](https://developer.apple.com/documentation/opengles/gl_alpha32f_ext)Added [#def GL_ALPHA8_EXT](https://developer.apple.com/documentation/opengles/gl_alpha8_ext)Added [#def GL_ALREADY_SIGNALED_APPLE](https://developer.apple.com/documentation/opengles/gl_already_signaled_apple)Added [#def GL_APPLE_copy_texture_levels](https://developer.apple.com/documentation/opengles/gl_apple_copy_texture_levels)Added [#def GL_APPLE_sync](https://developer.apple.com/documentation/opengles/gl_apple_sync)Added [#def GL_BGRA8_EXT](https://developer.apple.com/documentation/opengles/gl_bgra8_ext)Added [#def GL_CONDITION_SATISFIED_APPLE](https://developer.apple.com/documentation/opengles/gl_condition_satisfied_apple)Added [#def GL_DEPTH_COMPONENT32_OES](https://developer.apple.com/documentation/opengles/gl_depth_component32_oes)Added [#def GL_EXT_map_buffer_range](https://developer.apple.com/documentation/opengles/gl_ext_map_buffer_range)Added [#def GL_EXT_shader_framebuffer_fetch](https://developer.apple.com/documentation/opengles/gl_ext_shader_framebuffer_fetch)Added [#def GL_EXT_texture_storage](https://developer.apple.com/documentation/opengles/gl_ext_texture_storage)Added [#def GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT](https://developer.apple.com/documentation/opengles/gl_fragment_shader_discards_samples_ext)Added [#def GL_LUMINANCE16F_EXT](https://developer.apple.com/documentation/opengles/gl_luminance16f_ext)Added [#def GL_LUMINANCE32F_EXT](https://developer.apple.com/documentation/opengles/gl_luminance32f_ext)Added [#def GL_LUMINANCE8_ALPHA8_EXT](https://developer.apple.com/documentation/opengles/gl_luminance8_alpha8_ext)Added [#def GL_LUMINANCE8_EXT](https://developer.apple.com/documentation/opengles/gl_luminance8_ext)Added [#def GL_LUMINANCE_ALPHA16F_EXT](https://developer.apple.com/documentation/opengles/gl_luminance_alpha16f_ext)Added [#def GL_LUMINANCE_ALPHA32F_EXT](https://developer.apple.com/documentation/opengles/gl_luminance_alpha32f_ext)Added [#def GL_MAP_FLUSH_EXPLICIT_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_map_flush_explicit_bit_ext)Added [#def GL_MAP_INVALIDATE_BUFFER_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_map_invalidate_buffer_bit_ext)Added [#def GL_MAP_INVALIDATE_RANGE_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_map_invalidate_range_bit_ext)Added [#def GL_MAP_READ_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_map_read_bit_ext)Added [#def GL_MAP_UNSYNCHRONIZED_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_map_unsynchronized_bit_ext)Added [#def GL_MAP_WRITE_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_map_write_bit_ext)Added [#def GL_MAX_SERVER_WAIT_TIMEOUT_APPLE](https://developer.apple.com/documentation/opengles/gl_max_server_wait_timeout_apple)Added [#def GL_OBJECT_TYPE_APPLE](https://developer.apple.com/documentation/opengles/gl_object_type_apple)Added [#def GL_R32F_EXT](https://developer.apple.com/documentation/opengles/gl_r32f_ext)Added [#def GL_RG32F_EXT](https://developer.apple.com/documentation/opengles/gl_rg32f_ext)Added [#def GL_RGB32F_EXT](https://developer.apple.com/documentation/opengles/gl_rgb32f_ext)Added [#def GL_RGBA32F_EXT](https://developer.apple.com/documentation/opengles/gl_rgba32f_ext)Added [#def GL_RGB_RAW_422_APPLE](https://developer.apple.com/documentation/opengles/gl_rgb_raw_422_apple)Added [#def GL_SAMPLER_2D_SHADOW_EXT](https://developer.apple.com/documentation/opengles/gl_sampler_2d_shadow_ext)Added [#def GL_SIGNALED_APPLE](https://developer.apple.com/documentation/opengles/gl_signaled_apple)Added [#def GL_SYNC_CONDITION_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_condition_apple)Added [#def GL_SYNC_FENCE_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_fence_apple)Added [#def GL_SYNC_FLAGS_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_flags_apple)Added [#def GL_SYNC_FLUSH_COMMANDS_BIT_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_flush_commands_bit_apple)Added [#def GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_gpu_commands_complete_apple)Added [#def GL_SYNC_OBJECT_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_object_apple)Added [#def GL_SYNC_STATUS_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_status_apple)Added [#def GL_TEXTURE_IMMUTABLE_FORMAT_EXT](https://developer.apple.com/documentation/opengles/gl_texture_immutable_format_ext)Added [#def GL_TIMEOUT_EXPIRED_APPLE](https://developer.apple.com/documentation/opengles/gl_timeout_expired_apple)Added [#def GL_TIMEOUT_IGNORED_APPLE](https://developer.apple.com/documentation/opengles/gl_timeout_ignored_apple)Added [#def GL_UNSIGNALED_APPLE](https://developer.apple.com/documentation/opengles/gl_unsignaled_apple)Added [#def GL_WAIT_FAILED_APPLE](https://developer.apple.com/documentation/opengles/gl_wait_failed_apple)Added GLint64Added GLsyncAdded GLuint64Added [glClientWaitSyncAPPLE()](https://developer.apple.com/documentation/opengles/1624707-glclientwaitsyncapple)Added [glCopyTextureLevelsAPPLE()](https://developer.apple.com/documentation/opengles/1614355-glcopytexturelevelsapple)Added [glDeleteSyncAPPLE()](https://developer.apple.com/documentation/opengles/1624696-gldeletesyncapple)Added [glFenceSyncAPPLE()](https://developer.apple.com/documentation/opengles/1624705-glfencesyncapple)Added [glFlushMappedBufferRangeEXT()](https://developer.apple.com/documentation/opengles/1614244-glflushmappedbufferrangeext)Added [glGetInteger64vAPPLE()](https://developer.apple.com/documentation/opengles/1624695-glgetinteger64vapple)Added [glGetSyncivAPPLE()](https://developer.apple.com/documentation/opengles/1624746-glgetsyncivapple)Added [glIsSyncAPPLE()](https://developer.apple.com/documentation/opengles/1624727-glissyncapple)Added [glMapBufferRangeEXT()](https://developer.apple.com/documentation/opengles/1614197-glmapbufferrangeext)Added [glTexStorage2DEXT()](https://developer.apple.com/documentation/opengles/1614310-gltexstorage2dext)Added [glWaitSyncAPPLE()](https://developer.apple.com/documentation/opengles/1624698-glwaitsyncapple)

## PassKit

PKAddPassesViewController.hAdded [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller)Added [PKAddPassesViewController.delegate](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619220-delegate)Added [-[PKAddPassesViewController initWithPass:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619251-initwithpass)Added [PKAddPassesViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate)Added [-[PKAddPassesViewControllerDelegate addPassesViewControllerDidFinish:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate/1619236-addpassesviewcontrollerdidfinish)PKError.hAdded PKErrorCodeAdded PKErrorDomainAdded PKErrorNotEntitledAdded PKErrorPassSignatureInvalidAdded PKErrorUnknownPKPass.hAdded [PKPass](https://developer.apple.com/documentation/passkit/pkpass)Added [PKPass.authenticationToken](https://developer.apple.com/documentation/passkit/pkpass/1618766-authenticationtoken)Added [PKPass.icon](https://developer.apple.com/documentation/passkit/pkpass/1618762-icon)Added [-[PKPass initWithData:error:]](https://developer.apple.com/documentation/passkit/pkpass/1618792-init)Added [PKPass.localizedDescription](https://developer.apple.com/documentation/passkit/pkpass/1618770-localizeddescription)Added [PKPass.localizedName](https://developer.apple.com/documentation/passkit/pkpass/1618768-localizedname)Added [-[PKPass localizedValueForFieldKey:]](https://developer.apple.com/documentation/passkit/pkpass/1618798-localizedvalueforfieldkey)Added [PKPass.organizationName](https://developer.apple.com/documentation/passkit/pkpass/1618778-organizationname)Added [PKPass.passTypeIdentifier](https://developer.apple.com/documentation/passkit/pkpass/1618783-passtypeidentifier)Added [PKPass.passURL](https://developer.apple.com/documentation/passkit/pkpass/1618781-passurl)Added [PKPass.relevantDate](https://developer.apple.com/documentation/passkit/pkpass/1618776-relevantdate)Added [PKPass.serialNumber](https://developer.apple.com/documentation/passkit/pkpass/1618788-serialnumber)Added [PKPass.webServiceURL](https://developer.apple.com/documentation/passkit/pkpass/1618772-webserviceurl)Added NS_ENUM() (no architecture available)Added NS_ENUM_AVAILABLE_IOS() (no architecture available)Added [PKInvalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkinvaliddataerror)Added [PKInvalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invalidsignature)Added [PKPassKitErrorCode](https://developer.apple.com/documentation/passkit/pkpasskiterror/code)Added [PKPassKitErrorDomain](https://developer.apple.com/documentation/passkit/pkpasskiterrordomain)Added [PKUnknownError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/unknownerror)Added [PKUnsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/unsupportedversionerror)PKPassLibrary.hAdded [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary)Added [-[PKPassLibrary containsPass:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617110-containspass)Added [+[PKPassLibrary isPassLibraryAvailable]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617080-ispasslibraryavailable)Added [-[PKPassLibrary passWithPassTypeIdentifier:serialNumber:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617104-passwithpasstypeidentifier)Added [-[PKPassLibrary passes]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617109-passes)Added [-[PKPassLibrary removePass:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617083-removepass)Added [-[PKPassLibrary replacePassWithPass:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617082-replacepasswithpass)Added [PKPassLibraryAddedPassesUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryaddedpassesuserinfokey)Added [PKPassLibraryDidChangeNotification](https://developer.apple.com/documentation/passkit/pkpasslibrarydidchangenotification)Added [PKPassLibraryPassTypeIdentifierUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617094-passtypeidentifieruserinfokey)Added [PKPassLibraryRemovedPassInfosUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617090-removedpassinfosuserinfokey)Added [PKPassLibraryReplacementPassesUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617077-replacementpassesuserinfokey)Added [PKPassLibrarySerialNumberUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617085-serialnumberuserinfokey)

## QuartzCore

CABase.hRemoved #def CGFLOAT_DEFINEDRemoved [#def CGFLOAT_IS_DOUBLE](https://developer.apple.com/documentation/coregraphics/cgfloat_is_double)Removed [#def CGFLOAT_MAX](https://developer.apple.com/documentation/coregraphics/cgfloat_max)Removed [#def CGFLOAT_MIN](https://developer.apple.com/documentation/coregraphics/cgfloat_min)Removed [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) (no architecture available)CALayer.hAdded [CALayer.drawsAsynchronously](https://developer.apple.com/documentation/quartzcore/calayer/1410974-drawsasynchronously)

## QuickLook

No changes

## Security

SecKey.hAdded [kSecPaddingPKCS1SHA224](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1sha224)Added [kSecPaddingPKCS1SHA256](https://developer.apple.com/documentation/security/secpadding/1617989-pkcs1sha256)Added [kSecPaddingPKCS1SHA384](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1sha384)Added [kSecPaddingPKCS1SHA512](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1sha512)SecTrust.hModified [SecTrustCreateWithCertificates()](https://developer.apple.com/documentation/security/1401555-sectrustcreatewithcertificates)

|  | Declaration |
| --- | --- |
| From | OSStatus SecTrustCreateWithCertificates ( CFTypeRef certificates, CFTypeRef policies, SecTrustRef \*trustRef); |
| To | OSStatus SecTrustCreateWithCertificates ( CFTypeRef certificates, CFTypeRef policies, SecTrustRef \*trust); |

SecureTransport.hAdded [errSSLUnexpectedRecord](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslunexpectedrecord)

## Social

SLComposeViewController.hAdded [SLComposeViewController](https://developer.apple.com/documentation/social/slcomposeviewcontroller)Added [-[SLComposeViewController addImage:]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624855-addimage)Added [-[SLComposeViewController addURL:]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624849-add)Added [SLComposeViewController.completionHandler](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624836-completionhandler)Added [+[SLComposeViewController composeViewControllerForServiceType:]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624837-composeviewcontrollerforservicet)Added [+[SLComposeViewController isAvailableForServiceType:]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624851-isavailableforservicetype)Added [-[SLComposeViewController removeAllImages]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624841-removeallimages)Added [-[SLComposeViewController removeAllURLs]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624838-removeallurls)Added [SLComposeViewController.serviceType](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624854-servicetype)Added [-[SLComposeViewController setInitialText:]](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624852-setinitialtext)Added NS_ENUM() (no architecture available)Added [SLComposeViewControllerCompletionHandler](https://developer.apple.com/documentation/social/slcomposeviewcontrollercompletionhandler)Added [SLComposeViewControllerResult](https://developer.apple.com/documentation/social/slcomposeviewcontrollerresult)Added [SLComposeViewControllerResultCancelled](https://developer.apple.com/documentation/social/slcomposeviewcontrollerresult/slcomposeviewcontrollerresultcancelled)Added [SLComposeViewControllerResultDone](https://developer.apple.com/documentation/social/slcomposeviewcontrollerresult/done)SLRequest.hAdded [SLRequest](https://developer.apple.com/documentation/social/slrequest)Added [SLRequest.URL](https://developer.apple.com/documentation/social/slrequest/1488602-url)Added [SLRequest.account](https://developer.apple.com/documentation/social/slrequest/1488582-account)Added [-[SLRequest addMultipartData:withName:type:filename:]](https://developer.apple.com/documentation/social/slrequest/1488593-addmultipartdata)Added [SLRequest.parameters](https://developer.apple.com/documentation/social/slrequest/1488603-parameters)Added [-[SLRequest performRequestWithHandler:]](https://developer.apple.com/documentation/social/slrequest/1488560-perform)Added [-[SLRequest preparedURLRequest]](https://developer.apple.com/documentation/social/slrequest/1488592-preparedurlrequest)Added [+[SLRequest requestForServiceType:requestMethod:URL:parameters:]](https://developer.apple.com/documentation/social/slrequest/1488580-requestforservicetype)Added [SLRequest.requestMethod](https://developer.apple.com/documentation/social/slrequest/1488589-requestmethod)Added [SLRequestHandler](https://developer.apple.com/documentation/social/slrequesthandler)Added [SLRequestMethod](https://developer.apple.com/documentation/social/slrequestmethod)Added [SLRequestMethodDELETE](https://developer.apple.com/documentation/social/slrequestmethod/slrequestmethoddelete)Added [SLRequestMethodGET](https://developer.apple.com/documentation/social/slrequestmethod/slrequestmethodget)Added [SLRequestMethodPOST](https://developer.apple.com/documentation/social/slrequestmethod/slrequestmethodpost)SLServiceTypes.hAdded [SLServiceTypeFacebook](https://developer.apple.com/documentation/social/slservicetypefacebook)Added [SLServiceTypeSinaWeibo](https://developer.apple.com/documentation/social/slservicetypesinaweibo)Added [SLServiceTypeTwitter](https://developer.apple.com/documentation/social/slservicetypetwitter)SocialDefines.hAdded #def SOCIAL_CLASS_AVAILABLEAdded #def SOCIAL_EXTERN

## StoreKit

SKDownload.hAdded [SKDownload](https://developer.apple.com/documentation/storekit/skdownload)Added [SKDownload.contentIdentifier](https://developer.apple.com/documentation/storekit/skdownload/1458941-contentidentifier)Added [SKDownload.contentLength](https://developer.apple.com/documentation/storekit/skdownload/1458932-contentlength)Added [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)Added [SKDownload.contentVersion](https://developer.apple.com/documentation/storekit/skdownload/1458916-contentversion)Added [SKDownload.downloadState](https://developer.apple.com/documentation/storekit/skdownload/1620412-downloadstate)Added [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)Added [SKDownload.progress](https://developer.apple.com/documentation/storekit/skdownload/1458945-progress)Added [SKDownload.timeRemaining](https://developer.apple.com/documentation/storekit/skdownload/1458943-timeremaining)Added [SKDownload.transaction](https://developer.apple.com/documentation/storekit/skdownload/1458949-transaction)Added [SKDownloadState](https://developer.apple.com/documentation/storekit/skdownloadstate)Added [SKDownloadStateActive](https://developer.apple.com/documentation/storekit/skdownloadstate/active)Added [SKDownloadStateCancelled](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatecancelled)Added [SKDownloadStateFailed](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefailed)Added [SKDownloadStateFinished](https://developer.apple.com/documentation/storekit/skdownloadstate/finished)Added [SKDownloadStatePaused](https://developer.apple.com/documentation/storekit/skdownloadstate/paused)Added [SKDownloadStateWaiting](https://developer.apple.com/documentation/storekit/skdownloadstate/waiting)Added [SKDownloadTimeRemainingUnknown](https://developer.apple.com/documentation/storekit/skdownloadtimeremainingunknown)SKError.hAdded [SKErrorStoreProductNotAvailable](https://developer.apple.com/documentation/storekit/skerror/code/storeproductnotavailable)SKPaymentQueue.hAdded [-[SKPaymentQueue cancelDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-cancel)Added [-[SKPaymentQueue pauseDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pause)Added [-[SKPaymentQueue resumeDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume)Added [-[SKPaymentQueue startDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-start)Added [-[SKPaymentTransactionObserver paymentQueue:updatedDownloads:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506073-paymentqueue)SKPaymentTransaction.hAdded [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)SKProduct.hAdded [SKProduct.downloadContentLengths](https://developer.apple.com/documentation/storekit/skproduct/1615752-downloadcontentlengths)Added [SKProduct.downloadContentVersion](https://developer.apple.com/documentation/storekit/skproduct/1615754-downloadcontentversion)Added [SKProduct.downloadable](https://developer.apple.com/documentation/storekit/skproduct/1506161-downloadable)SKStoreProductViewController.hAdded [SKStoreProductViewController](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)Added [SKStoreProductViewController.delegate](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/1620634-delegate)Added [-[SKStoreProductViewController loadProductWithParameters:completionBlock:]](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/1620632-loadproductwithparameters)Added [SKStoreProductViewControllerDelegate](https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate)Added [-[SKStoreProductViewControllerDelegate productViewControllerDidFinish:]](https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate/1620620-productviewcontrollerdidfinish)Added [SKStoreProductParameterITunesItemIdentifier](https://developer.apple.com/documentation/storekit/skstoreproductparameteritunesitemidentifier)

## SystemConfiguration

SystemConfiguration.hAdded [kSCStatusConnectionIgnore](https://developer.apple.com/documentation/systemconfiguration/1518026-status_and_error_codes/kscstatusconnectionignore)

## Twitter

No changes

## UIKit

NSAttributedString.hAdded [NSBackgroundColorAttributeName](https://developer.apple.com/documentation/uikit/nsbackgroundcolorattributename)Added [NSFontAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528839-font)Added [NSForegroundColorAttributeName](https://developer.apple.com/documentation/uikit/nsforegroundcolorattributename)Added [NSKernAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1527891-kern)Added [NSLigatureAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524592-ligature)Added [NSParagraphStyleAttributeName](https://developer.apple.com/documentation/appkit/nsparagraphstyleattributename)Added [NSShadowAttributeName](https://developer.apple.com/documentation/uikit/nsshadowattributename)Added [NSStrikethroughStyleAttributeName](https://developer.apple.com/documentation/appkit/nsstrikethroughstyleattributename)Added [NSStrokeColorAttributeName](https://developer.apple.com/documentation/appkit/nsstrokecolorattributename)Added [NSStrokeWidthAttributeName](https://developer.apple.com/documentation/uikit/nsstrokewidthattributename)Added [NSUnderlineStyleAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524865-underlinestyle)Added [NSUnderlineStyleNone](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylenone)Added [NSUnderlineStyleSingle](https://developer.apple.com/documentation/appkit/nsunderlinestyle/1530283-single)Added [NSVerticalGlyphFormAttributeName](https://developer.apple.com/documentation/appkit/nsverticalglyphformattributename)NSLayoutConstraint.hAdded [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint)Added [NSLayoutConstraint.constant](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526928-constant)Added [+[NSLayoutConstraint constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526954-init)Added [+[NSLayoutConstraint constraintsWithVisualFormat:options:metrics:views:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526944-constraints)Added [NSLayoutConstraint.firstAttribute](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1525204-firstattribute)Added [NSLayoutConstraint.firstItem](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526860-firstitem)Added [NSLayoutConstraint.multiplier](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526920-multiplier)Added [NSLayoutConstraint.priority](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526946-priority)Added [NSLayoutConstraint.relation](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526549-relation)Added [NSLayoutConstraint.secondAttribute](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526941-secondattribute)Added [NSLayoutConstraint.secondItem](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526868-seconditem)Added [NSLayoutConstraint.shouldBeArchived](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1525647-shouldbearchived)Added [#def NSDictionaryOfVariableBindings](https://developer.apple.com/documentation/uikit/nsdictionaryofvariablebindings)Added [NSLayoutAttribute](https://developer.apple.com/documentation/uikit/nslayoutattribute)Added [NSLayoutAttributeBaseline](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributebaseline)Added [NSLayoutAttributeBottom](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/bottom)Added [NSLayoutAttributeCenterX](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributecenterx)Added [NSLayoutAttributeCenterY](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributecentery)Added [NSLayoutAttributeHeight](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/height)Added [NSLayoutAttributeLeading](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributeleading)Added [NSLayoutAttributeLeft](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/left)Added [NSLayoutAttributeNotAnAttribute](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributenotanattribute)Added [NSLayoutAttributeRight](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/right)Added [NSLayoutAttributeTop](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/top)Added [NSLayoutAttributeTrailing](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributetrailing)Added [NSLayoutAttributeWidth](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/width)Added [NSLayoutFormatAlignAllBaseline](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatalignallbaseline)Added [NSLayoutFormatAlignAllBottom](https://developer.apple.com/documentation/appkit/nslayoutconstraint/formatoptions/1526947-alignallbottom)Added [NSLayoutFormatAlignAllCenterX](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignallcenterx)Added [NSLayoutFormatAlignAllCenterY](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatalignallcentery)Added [NSLayoutFormatAlignAllLeading](https://developer.apple.com/documentation/appkit/nslayoutconstraint/formatoptions/1526925-alignallleading)Added [NSLayoutFormatAlignAllLeft](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignallleft)Added [NSLayoutFormatAlignAllRight](https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions/1525250-alignallright)Added [NSLayoutFormatAlignAllTop](https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions/1526952-alignalltop)Added [NSLayoutFormatAlignAllTrailing](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignalltrailing)Added [NSLayoutFormatAlignmentMask](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignmentmask)Added [NSLayoutFormatDirectionLeadingToTrailing](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatdirectionleadingtotrailing)Added [NSLayoutFormatDirectionLeftToRight](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatdirectionlefttoright)Added [NSLayoutFormatDirectionMask](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatdirectionmask)Added [NSLayoutFormatDirectionRightToLeft](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatdirectionrighttoleft)Added [NSLayoutFormatOptions](https://developer.apple.com/documentation/appkit/nslayoutformatoptions)Added [NSLayoutRelation](https://developer.apple.com/documentation/appkit/nslayoutrelation)Added [NSLayoutRelationEqual](https://developer.apple.com/documentation/appkit/nslayoutrelation/nslayoutrelationequal)Added [NSLayoutRelationGreaterThanOrEqual](https://developer.apple.com/documentation/uikit/nslayoutrelation/nslayoutrelationgreaterthanorequal)Added [NSLayoutRelationLessThanOrEqual](https://developer.apple.com/documentation/uikit/nslayoutrelation/nslayoutrelationlessthanorequal)Added NS_ENUM() (no architecture available)Added NS_OPTIONS() (no architecture available)Added [UILayoutPriority](https://developer.apple.com/documentation/uikit/uilayoutpriority)Added UILayoutPriorityDefaultHighAdded UILayoutPriorityDefaultLowAdded UILayoutPriorityFittingSizeLevelAdded UILayoutPriorityRequiredNSParagraphStyle.hAdded [NSMutableParagraphStyle](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle)Added [NSMutableParagraphStyle.alignment](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1534368-alignment)Added [NSMutableParagraphStyle.baseWritingDirection](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1534601-basewritingdirection)Added [NSMutableParagraphStyle.firstLineHeadIndent](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528392-firstlineheadindent)Added [NSMutableParagraphStyle.headIndent](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1525135-headindent)Added [NSMutableParagraphStyle.hyphenationFactor](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535553-hyphenationfactor)Added [NSMutableParagraphStyle.lineBreakMode](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535126-linebreakmode)Added [NSMutableParagraphStyle.lineHeightMultiple](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1524596-lineheightmultiple)Added [NSMutableParagraphStyle.lineSpacing](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528742-linespacing)Added [NSMutableParagraphStyle.maximumLineHeight](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1524351-maximumlineheight)Added [NSMutableParagraphStyle.minimumLineHeight](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531118-minimumlineheight)Added [NSMutableParagraphStyle.paragraphSpacing](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1532528-paragraphspacing)Added [NSMutableParagraphStyle.paragraphSpacingBefore](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1527729-paragraphspacingbefore)Added [NSMutableParagraphStyle.tailIndent](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531666-tailindent)Added [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)Added [NSParagraphStyle.alignment](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532321-alignment)Added [NSParagraphStyle.baseWritingDirection](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527354-basewritingdirection)Added [+[NSParagraphStyle defaultParagraphStyle]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532681-default)Added [+[NSParagraphStyle defaultWritingDirectionForLanguage:]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1535327-defaultwritingdirection)Added [NSParagraphStyle.firstLineHeadIndent](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527764-firstlineheadindent)Added [NSParagraphStyle.headIndent](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530760-headindent)Added [NSParagraphStyle.hyphenationFactor](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1529275-hyphenationfactor)Added [NSParagraphStyle.lineBreakMode](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1529937-linebreakmode)Added [NSParagraphStyle.lineHeightMultiple](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1528614-lineheightmultiple)Added [NSParagraphStyle.lineSpacing](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1524635-linespacing)Added [NSParagraphStyle.maximumLineHeight](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1533343-maximumlineheight)Added [NSParagraphStyle.minimumLineHeight](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535639-minimumlineheight)Added [NSParagraphStyle.paragraphSpacing](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530912-paragraphspacing)Added [NSParagraphStyle.paragraphSpacingBefore](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1533011-paragraphspacingbefore)Added [NSParagraphStyle.tailIndent](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1525556-tailindent)Added [NSLineBreakByCharWrapping](https://developer.apple.com/documentation/uikit/nslinebreakmode/nslinebreakbycharwrapping)Added [NSLineBreakByClipping](https://developer.apple.com/documentation/uikit/nslinebreakmode/byclipping)Added [NSLineBreakByTruncatingHead](https://developer.apple.com/documentation/uikit/nslinebreakmode/bytruncatinghead)Added [NSLineBreakByTruncatingMiddle](https://developer.apple.com/documentation/appkit/nsparagraphstyle/nslinebreakmode/bytruncatingmiddle)Added [NSLineBreakByTruncatingTail](https://developer.apple.com/documentation/uikit/nslinebreakmode/bytruncatingtail)Added [NSLineBreakByWordWrapping](https://developer.apple.com/documentation/uikit/nslinebreakmode/nslinebreakbywordwrapping)Added [NSLineBreakMode](https://developer.apple.com/documentation/uikit/nslinebreakmode)Added NS_ENUM_AVAILABLE_IOS() (no architecture available)NSShadow.hAdded [NSShadow](https://developer.apple.com/documentation/uikit/nsshadow)Added [NSShadow.shadowBlurRadius](https://developer.apple.com/documentation/uikit/nsshadow/1429846-shadowblurradius)Added [NSShadow.shadowColor](https://developer.apple.com/documentation/uikit/nsshadow/1429855-shadowcolor)Added [NSShadow.shadowOffset](https://developer.apple.com/documentation/appkit/nsshadow/1429851-shadowoffset)NSStringDrawing.hAdded [-[NSAttributedString boundingRectWithSize:options:context:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1529154-boundingrect)Added [-[NSAttributedString drawAtPoint:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1529478-drawatpoint)Added [-[NSAttributedString drawInRect:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1531631-drawinrect)Added [-[NSAttributedString drawWithRect:options:context:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1524971-draw)Added [-[NSAttributedString size]](https://developer.apple.com/documentation/foundation/nsattributedstring/1528362-size)Added [NSStringDrawingContext](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext)Added [NSStringDrawingContext.actualScaleFactor](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1531498-actualscalefactor)Added [NSStringDrawingContext.actualTrackingAdjustment](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1624042-actualtrackingadjustment)Added [NSStringDrawingContext.minimumScaleFactor](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1534020-minimumscalefactor)Added [NSStringDrawingContext.minimumTrackingAdjustment](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1624043-minimumtrackingadjustment)Added [NSStringDrawingContext.totalBounds](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext/1530525-totalbounds)Added NSAttributedString(NSExtendedStringDrawing)Added NSAttributedString(NSStringDrawing)Added [NSStringDrawingOptions](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions)Added [NSStringDrawingTruncatesLastVisibleLine](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions/1527952-truncateslastvisibleline)Added [NSStringDrawingUsesDeviceMetrics](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions/1524942-usesdevicemetrics)Added [NSStringDrawingUsesFontLeading](https://developer.apple.com/documentation/appkit/nsstringdrawingoptions/nsstringdrawingusesfontleading)Added [NSStringDrawingUsesLineFragmentOrigin](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions/nsstringdrawinguseslinefragmentorigin)NSText.hAdded [NSTextAlignment](https://developer.apple.com/documentation/uikit/nstextalignment)Added [NSTextAlignmentCenter](https://developer.apple.com/documentation/uikit/nstextalignment/center)Added [NSTextAlignmentFromCTTextAlignment()](https://developer.apple.com/documentation/uikit/nstextalignment/1624537-init)Added [NSTextAlignmentJustified](https://developer.apple.com/documentation/uikit/nstextalignment/justified)Added [NSTextAlignmentLeft](https://developer.apple.com/documentation/uikit/nstextalignment/left)Added [NSTextAlignmentNatural](https://developer.apple.com/documentation/uikit/nstextalignment/nstextalignmentnatural)Added [NSTextAlignmentRight](https://developer.apple.com/documentation/appkit/nstextalignment/right)Added [NSTextAlignmentToCTTextAlignment()](https://developer.apple.com/documentation/coretext/cttextalignment/1624536-init)Added [NSWritingDirection](https://developer.apple.com/documentation/uikit/nswritingdirection)Added [NSWritingDirectionLeftToRight](https://developer.apple.com/documentation/uikit/nswritingdirection/nswritingdirectionlefttoright)Added [NSWritingDirectionNatural](https://developer.apple.com/documentation/uikit/nswritingdirection/nswritingdirectionnatural)Added [NSWritingDirectionRightToLeft](https://developer.apple.com/documentation/uikit/nswritingdirection/righttoleft)UIAccessibility.hAdded -[NSObject NS_ENUM] (no architecture available)Added [-[NSObject accessibilityPerformMagicTap]](https://developer.apple.com/documentation/objectivec/nsobject/1615137-accessibilityperformmagictap)Added [NSObject.shouldGroupAccessibilityChildren](https://developer.apple.com/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren)Added [UIAccessibilityGuidedAccessStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibilityguidedaccessstatusdidchangenotification)Added [UIAccessibilityInvertColorsStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615196-invertcolorsstatusdidchangenotif)Added [UIAccessibilityIsGuidedAccessEnabled()](https://developer.apple.com/documentation/uikit/1615173-uiaccessibilityisguidedaccessena)Added [UIAccessibilityIsInvertColorsEnabled()](https://developer.apple.com/documentation/uikit/1615167-uiaccessibilityisinvertcolorsena)UIAccessibilityAdditions.hAdded [UIScrollViewAccessibilityDelegate](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate)Added [-[UIScrollViewAccessibilityDelegate accessibilityScrollStatusForScrollView:]](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/1621055-accessibilityscrollstatus)UIAccessibilityConstants.hAdded [UIAccessibilityAnnouncementDidFinishNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1620202-announcementdidfinishnotificatio)Added [UIAccessibilityAnnouncementKeyStringValue](https://developer.apple.com/documentation/uikit/uiaccessibility/1620183-announcementstringvalueuserinfok)Added [UIAccessibilityAnnouncementKeyWasSuccessful](https://developer.apple.com/documentation/uikit/uiaccessibility/1620209-announcementwassuccessfuluserinf)Added [UIAccessibilityTraitHeader](https://developer.apple.com/documentation/uikit/uiaccessibilitytraitheader)UIActivity.hAdded [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity)Added [-[UIActivity activityDidFinish:]](https://developer.apple.com/documentation/uikit/uiactivity/1620679-activitydidfinish)Added [-[UIActivity activityImage]](https://developer.apple.com/documentation/uikit/uiactivity/1620658-activityimage)Added [-[UIActivity activityTitle]](https://developer.apple.com/documentation/uikit/uiactivity/1620674-activitytitle)Added [-[UIActivity activityType]](https://developer.apple.com/documentation/uikit/uiactivity/1620671-activitytype)Added [-[UIActivity activityViewController]](https://developer.apple.com/documentation/uikit/uiactivity/1620678-activityviewcontroller)Added [-[UIActivity canPerformWithActivityItems:]](https://developer.apple.com/documentation/uikit/uiactivity/1620677-canperform)Added [-[UIActivity performActivity]](https://developer.apple.com/documentation/uikit/uiactivity/1620659-perform)Added [-[UIActivity prepareWithActivityItems:]](https://developer.apple.com/documentation/uikit/uiactivity/1620668-prepare)Added [UIActivityTypeAssignToContact](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620682-assigntocontact)Added [UIActivityTypeCopyToPasteboard](https://developer.apple.com/documentation/uikit/uiactivitytypecopytopasteboard)Added [UIActivityTypeMail](https://developer.apple.com/documentation/uikit/uiactivitytypemail)Added [UIActivityTypeMessage](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620655-message)Added [UIActivityTypePostToFacebook](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620657-posttofacebook)Added [UIActivityTypePostToTwitter](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620675-posttotwitter)Added [UIActivityTypePostToWeibo](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620661-posttoweibo)Added [UIActivityTypePrint](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620684-print)Added [UIActivityTypeSaveToCameraRoll](https://developer.apple.com/documentation/uikit/uiactivity/activitytype/1620681-savetocameraroll)UIActivityIndicatorView.hRemoved UIActivityIndicatorView.UI_APPEARANCE_SELECTOR (no architecture available)UIActivityItemProvider.hAdded [UIActivityItemProvider](https://developer.apple.com/documentation/uikit/uiactivityitemprovider)Added [UIActivityItemProvider.activityType](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620459-activitytype)Added [-[UIActivityItemProvider initWithPlaceholderItem:]](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620463-initwithplaceholderitem)Added [-[UIActivityItemProvider item]](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620457-item)Added [UIActivityItemProvider.placeholderItem](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620454-placeholderitem)Added [UIActivityItemSource](https://developer.apple.com/documentation/uikit/uiactivityitemsource)Added [-[UIActivityItemSource activityViewController:itemForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620453-activityviewcontroller)Added [-[UIActivityItemSource activityViewControllerPlaceholderItem:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620458-activityviewcontrollerplaceholde)UIActivityViewController.hAdded [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)Added [UIActivityViewController.completionHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622010-completionhandler)Added [UIActivityViewController.excludedActivityTypes](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622009-excludedactivitytypes)Added [-[UIActivityViewController initWithActivityItems:applicationActivities:]](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622019-initwithactivityitems)Added [UIActivityViewControllerCompletionHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontrollercompletionhandler)UIApplication.hAdded [-[UIApplication completeStateRestoration]](https://developer.apple.com/documentation/uikit/uiapplication/1623081-completestaterestoration)Added [-[UIApplication extendStateRestoration]](https://developer.apple.com/documentation/uikit/uiapplication/1623060-extendstaterestoration)Added [-[UIApplication supportedInterfaceOrientationsForWindow:]](https://developer.apple.com/documentation/uikit/uiapplication/1623091-supportedinterfaceorientations)Added [-[UIApplicationDelegate application:didDecodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623006-application)Added [-[UIApplicationDelegate application:shouldRestoreApplicationState:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application)Added [-[UIApplicationDelegate application:shouldSaveApplicationState:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623089-application)Added [-[UIApplicationDelegate application:supportedInterfaceOrientationsForWindow:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623107-application)Added [-[UIApplicationDelegate application:viewControllerWithRestorationIdentifierPath:coder:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623062-application)Added [-[UIApplicationDelegate application:willEncodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623099-application)Added [-[UIApplicationDelegate application:willFinishLaunchingWithOptions:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application)Added UIApplication(UIStateRestoration)Added [UIApplicationInvalidInterfaceOrientationException](https://developer.apple.com/documentation/uikit/uiapplicationinvalidinterfaceorientationexception)Added [UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask)Added [UIInterfaceOrientationMaskAll](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/uiinterfaceorientationmaskall)Added [UIInterfaceOrientationMaskAllButUpsideDown](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/1622957-allbutupsidedown)Added [UIInterfaceOrientationMaskLandscape](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/uiinterfaceorientationmasklandscape)Added [UIInterfaceOrientationMaskLandscapeLeft](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/uiinterfaceorientationmasklandscapeleft)Added [UIInterfaceOrientationMaskLandscapeRight](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/uiinterfaceorientationmasklandscaperight)Added [UIInterfaceOrientationMaskPortrait](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/uiinterfaceorientationmaskportrait)Added [UIInterfaceOrientationMaskPortraitUpsideDown](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/1623118-portraitupsidedown)UIBarButtonItem.hRemoved UIBarButtonItem.UI_APPEARANCE_SELECTOR (no architecture available)Added [-[UIBarButtonItem backgroundImageForState:style:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617117-backgroundimageforstate)Added [-[UIBarButtonItem setBackgroundImage:forState:style:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617161-setbackgroundimage)UIBezierPath.hAdded [-[UIBezierPath bezierPathByReversingPath]](https://developer.apple.com/documentation/uikit/uibezierpath/1624348-reversing)UIButton.hAdded [-[UIButton attributedTitleForState:]](https://developer.apple.com/documentation/uikit/uibutton/1623991-attributedtitle)Added [UIButton.currentAttributedTitle](https://developer.apple.com/documentation/uikit/uibutton/1624002-currentattributedtitle)Added [-[UIButton setAttributedTitle:forState:]](https://developer.apple.com/documentation/uikit/uibutton/1624012-setattributedtitle)Modified [UIButton.lineBreakMode](https://developer.apple.com/documentation/uikit/uibutton/1623995-linebreakmode)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UILineBreakMode lineBreakMode |
| To | @property(nonatomic) NSLineBreakMode lineBreakMode |

UICollectionView.hAdded [+[NSIndexPath indexPathForItem:inSection:]](https://developer.apple.com/documentation/foundation/nsindexpath/1526053-indexpathforitem)Added [NSIndexPath.item](https://developer.apple.com/documentation/foundation/nsindexpath/1528293-item)Added [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview)Added [UICollectionView.allowsMultipleSelection](https://developer.apple.com/documentation/uikit/uicollectionview/1618024-allowsmultipleselection)Added [UICollectionView.allowsSelection](https://developer.apple.com/documentation/uikit/uicollectionview/1618009-allowsselection)Added [UICollectionView.backgroundView](https://developer.apple.com/documentation/uikit/uicollectionview/1618074-backgroundview)Added [-[UICollectionView cellForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618088-cellforitematindexpath)Added [UICollectionView.collectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionview/1618047-collectionviewlayout)Added [UICollectionView.dataSource](https://developer.apple.com/documentation/uikit/uicollectionview/1618091-datasource)Added [UICollectionView.delegate](https://developer.apple.com/documentation/uikit/uicollectionview/1618033-delegate)Added [-[UICollectionView deleteItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618060-deleteitemsatindexpaths)Added [-[UICollectionView deleteSections:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618102-deletesections)Added [-[UICollectionView dequeueReusableCellWithReuseIdentifier:forIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618063-dequeuereusablecell)Added [-[UICollectionView dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618068-dequeuereusablesupplementaryview)Added [-[UICollectionView deselectItemAtIndexPath:animated:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618040-deselectitematindexpath)Added [-[UICollectionView indexPathForCell:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618094-indexpath)Added [-[UICollectionView indexPathForItemAtPoint:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618030-indexpathforitem)Added [-[UICollectionView indexPathsForSelectedItems]](https://developer.apple.com/documentation/uikit/uicollectionview/1618099-indexpathsforselecteditems)Added [-[UICollectionView indexPathsForVisibleItems]](https://developer.apple.com/documentation/uikit/uicollectionview/1618020-indexpathsforvisibleitems)Added [-[UICollectionView initWithFrame:collectionViewLayout:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618053-init)Added [-[UICollectionView insertItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618097-insertitems)Added [-[UICollectionView insertSections:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618090-insertsections)Added [-[UICollectionView layoutAttributesForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618093-layoutattributesforitematindexpa)Added [-[UICollectionView layoutAttributesForSupplementaryElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618012-layoutattributesforsupplementary)Added [-[UICollectionView moveItemAtIndexPath:toIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618059-moveitematindexpath)Added [-[UICollectionView moveSection:toSection:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618042-movesection)Added [-[UICollectionView numberOfItemsInSection:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618016-numberofitemsinsection)Added [-[UICollectionView numberOfSections]](https://developer.apple.com/documentation/uikit/uicollectionview/1618028-numberofsections)Added [-[UICollectionView performBatchUpdates:completion:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618045-performbatchupdates)Added [-[UICollectionView registerClass:forCellWithReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618089-register)Added [-[UICollectionView registerClass:forSupplementaryViewOfKind:withReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618103-register)Added [-[UICollectionView registerNib:forCellWithReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618083-register)Added [-[UICollectionView registerNib:forSupplementaryViewOfKind:withReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618101-registernib)Added [-[UICollectionView reloadData]](https://developer.apple.com/documentation/uikit/uicollectionview/1618078-reloaddata)Added [-[UICollectionView reloadItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618055-reloaditemsatindexpaths)Added [-[UICollectionView reloadSections:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618092-reloadsections)Added [-[UICollectionView scrollToItemAtIndexPath:atScrollPosition:animated:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618046-scrolltoitem)Added [-[UICollectionView selectItemAtIndexPath:animated:scrollPosition:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618057-selectitem)Added [-[UICollectionView setCollectionViewLayout:animated:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618086-setcollectionviewlayout)Added [-[UICollectionView visibleCells]](https://developer.apple.com/documentation/uikit/uicollectionview/1618056-visiblecells)Added [UICollectionViewDataSource](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource)Added [-[UICollectionViewDataSource collectionView:cellForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618029-collectionview)Added [-[UICollectionViewDataSource collectionView:numberOfItemsInSection:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618058-collectionview)Added [-[UICollectionViewDataSource collectionView:viewForSupplementaryElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618037-collectionview)Added [-[UICollectionViewDataSource numberOfSectionsInCollectionView:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618023-numberofsections)Added [UICollectionViewDelegate](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate)Added [-[UICollectionViewDelegate collectionView:canPerformAction:forItemAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618051-collectionview)Added [-[UICollectionViewDelegate collectionView:didDeselectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618035-collectionview)Added [-[UICollectionViewDelegate collectionView:didEndDisplayingCell:forItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618006-collectionview)Added [-[UICollectionViewDelegate collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618036-collectionview)Added [-[UICollectionViewDelegate collectionView:didHighlightItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618049-collectionview)Added [-[UICollectionViewDelegate collectionView:didSelectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618032-collectionview)Added [-[UICollectionViewDelegate collectionView:didUnhighlightItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618027-collectionview)Added [-[UICollectionViewDelegate collectionView:performAction:forItemAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618073-collectionview)Added [-[UICollectionViewDelegate collectionView:shouldDeselectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618067-collectionview)Added [-[UICollectionViewDelegate collectionView:shouldHighlightItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618070-collectionview)Added [-[UICollectionViewDelegate collectionView:shouldSelectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618095-collectionview)Added [-[UICollectionViewDelegate collectionView:shouldShowMenuForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618010-collectionview)Added NSIndexPath(UICollectionViewAdditions)Added [UICollectionViewScrollPosition](https://developer.apple.com/documentation/uikit/uicollectionviewscrollposition)Added [UICollectionViewScrollPositionBottom](https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition/1618043-bottom)Added [UICollectionViewScrollPositionCenteredHorizontally](https://developer.apple.com/documentation/uikit/uicollectionviewscrollposition/uicollectionviewscrollpositioncenteredhorizontally)Added [UICollectionViewScrollPositionCenteredVertically](https://developer.apple.com/documentation/uikit/uicollectionviewscrollposition/uicollectionviewscrollpositioncenteredvertically)Added [UICollectionViewScrollPositionLeft](https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition/1618039-left)Added [UICollectionViewScrollPositionNone](https://developer.apple.com/documentation/uikit/uicollectionviewscrollposition/uicollectionviewscrollpositionnone)Added [UICollectionViewScrollPositionRight](https://developer.apple.com/documentation/uikit/uicollectionviewscrollposition/uicollectionviewscrollpositionright)Added [UICollectionViewScrollPositionTop](https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition/1618085-top)UICollectionViewCell.hAdded [UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionreusableview)Added [-[UICollectionReusableView applyLayoutAttributes:]](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620139-apply)Added [-[UICollectionReusableView didTransitionFromLayout:toLayout:]](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620129-didtransition)Added [-[UICollectionReusableView prepareForReuse]](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620141-prepareforreuse)Added [UICollectionReusableView.reuseIdentifier](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620136-reuseidentifier)Added [-[UICollectionReusableView willTransitionFromLayout:toLayout:]](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620140-willtransitionfromlayout)Added [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)Added [UICollectionViewCell.backgroundView](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620131-backgroundview)Added [UICollectionViewCell.contentView](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620133-contentview)Added [UICollectionViewCell.highlighted](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620134-ishighlighted)Added [UICollectionViewCell.selected](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620130-isselected)Added [UICollectionViewCell.selectedBackgroundView](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620138-selectedbackgroundview)UICollectionViewController.hAdded [UICollectionViewController](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller)Added [UICollectionViewController.clearsSelectionOnViewWillAppear](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623977-clearsselectiononviewwillappear)Added [UICollectionViewController.collectionView](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623983-collectionview)Added [-[UICollectionViewController initWithCollectionViewLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623976-initwithcollectionviewlayout)UICollectionViewFlowLayout.hAdded [UICollectionViewDelegateFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout)Added [-[UICollectionViewDelegateFlowLayout collectionView:layout:insetForSectionAtIndex:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617718-collectionview)Added [-[UICollectionViewDelegateFlowLayout collectionView:layout:minimumInteritemSpacingForSectionAtIndex:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617696-collectionview)Added [-[UICollectionViewDelegateFlowLayout collectionView:layout:minimumLineSpacingForSectionAtIndex:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617705-collectionview)Added [-[UICollectionViewDelegateFlowLayout collectionView:layout:referenceSizeForFooterInSection:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617713-collectionview)Added [-[UICollectionViewDelegateFlowLayout collectionView:layout:referenceSizeForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617702-collectionview)Added [-[UICollectionViewDelegateFlowLayout collectionView:layout:sizeForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617708-collectionview)Added [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout)Added [UICollectionViewFlowLayout.footerReferenceSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617703-footerreferencesize)Added [UICollectionViewFlowLayout.headerReferenceSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617710-headerreferencesize)Added [UICollectionViewFlowLayout.itemSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617711-itemsize)Added [UICollectionViewFlowLayout.minimumInteritemSpacing](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617706-minimuminteritemspacing)Added [UICollectionViewFlowLayout.minimumLineSpacing](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617717-minimumlinespacing)Added [UICollectionViewFlowLayout.scrollDirection](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617720-scrolldirection)Added [UICollectionViewFlowLayout.sectionInset](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617714-sectioninset)Added [UICollectionElementKindSectionFooter](https://developer.apple.com/documentation/uikit/uicollectionelementkindsectionfooter)Added [UICollectionElementKindSectionHeader](https://developer.apple.com/documentation/uikit/uicollectionelementkindsectionheader)Added [UICollectionViewScrollDirection](https://developer.apple.com/documentation/uikit/uicollectionview/scrolldirection)Added [UICollectionViewScrollDirectionHorizontal](https://developer.apple.com/documentation/uikit/uicollectionviewscrolldirection/uicollectionviewscrolldirectionhorizontal)Added [UICollectionViewScrollDirectionVertical](https://developer.apple.com/documentation/uikit/uicollectionviewscrolldirection/uicollectionviewscrolldirectionvertical)UICollectionViewLayout.hAdded [UICollectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout)Added [UICollectionViewLayout.collectionView](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617751-collectionview)Added [-[UICollectionViewLayout collectionViewContentSize]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617796-collectionviewcontentsize)Added [-[UICollectionViewLayout finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617762-finallayoutattributesfordisappea)Added [-[UICollectionViewLayout finalLayoutAttributesForDisappearingItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617740-finallayoutattributesfordisappea)Added [-[UICollectionViewLayout finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617742-finallayoutattributesfordisappea)Added [-[UICollectionViewLayout finalizeAnimatedBoundsChange]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617745-finalizeanimatedboundschange)Added [-[UICollectionViewLayout finalizeCollectionViewUpdates]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617787-finalizecollectionviewupdates)Added [-[UICollectionViewLayout initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617726-initiallayoutattributesforappear)Added [-[UICollectionViewLayout initialLayoutAttributesForAppearingItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617789-initiallayoutattributesforappear)Added [-[UICollectionViewLayout initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617737-initiallayoutattributesforappear)Added [-[UICollectionViewLayout invalidateLayout]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617728-invalidatelayout)Added [+[UICollectionViewLayout layoutAttributesClass]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617774-layoutattributesclass)Added [-[UICollectionViewLayout layoutAttributesForDecorationViewOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617809-layoutattributesfordecorationvie)Added [-[UICollectionViewLayout layoutAttributesForElementsInRect:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec)Added [-[UICollectionViewLayout layoutAttributesForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617797-layoutattributesforitematindexpa)Added [-[UICollectionViewLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617792-layoutattributesforsupplementary)Added [-[UICollectionViewLayout prepareForAnimatedBoundsChange:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617761-prepareforanimatedboundschange)Added [-[UICollectionViewLayout prepareForCollectionViewUpdates:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617784-prepareforcollectionviewupdates)Added [-[UICollectionViewLayout prepareLayout]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617752-preparelayout)Added [-[UICollectionViewLayout registerClass:forDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617739-registerclass)Added [-[UICollectionViewLayout registerNib:forDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617732-registernib)Added [-[UICollectionViewLayout shouldInvalidateLayoutForBoundsChange:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617781-shouldinvalidatelayoutforboundsc)Added [-[UICollectionViewLayout targetContentOffsetForProposedContentOffset:withScrollingVelocity:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617729-targetcontentoffset)Added [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)Added [UICollectionViewLayoutAttributes.alpha](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617743-alpha)Added [UICollectionViewLayoutAttributes.center](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617735-center)Added [UICollectionViewLayoutAttributes.frame](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617753-frame)Added [UICollectionViewLayoutAttributes.hidden](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617799-ishidden)Added [UICollectionViewLayoutAttributes.indexPath](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617776-indexpath)Added [+[UICollectionViewLayoutAttributes layoutAttributesForCellWithIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617759-layoutattributesforcellwithindex)Added [+[UICollectionViewLayoutAttributes layoutAttributesForDecorationViewOfKind:withIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617786-layoutattributesfordecorationvie)Added [+[UICollectionViewLayoutAttributes layoutAttributesForSupplementaryViewOfKind:withIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617801-init)Added [UICollectionViewLayoutAttributes.representedElementCategory](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617738-representedelementcategory)Added [UICollectionViewLayoutAttributes.representedElementKind](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617806-representedelementkind)Added [UICollectionViewLayoutAttributes.size](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617733-size)Added [UICollectionViewLayoutAttributes.transform3D](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617764-transform3d)Added [UICollectionViewLayoutAttributes.zIndex](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617768-zindex)Added [UICollectionViewUpdateItem](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem)Added [UICollectionViewUpdateItem.indexPathAfterUpdate](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617765-indexpathafterupdate)Added [UICollectionViewUpdateItem.indexPathBeforeUpdate](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617772-indexpathbeforeupdate)Added [UICollectionViewUpdateItem.updateAction](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617748-updateaction)Added [UICollectionElementCategory](https://developer.apple.com/documentation/uikit/uicollectionelementcategory)Added [UICollectionElementCategoryCell](https://developer.apple.com/documentation/uikit/uicollectionview/elementcategory/cell)Added [UICollectionElementCategoryDecorationView](https://developer.apple.com/documentation/uikit/uicollectionelementcategory/uicollectionelementcategorydecorationview)Added [UICollectionElementCategorySupplementaryView](https://developer.apple.com/documentation/uikit/uicollectionview/elementcategory/supplementaryview)Added [UICollectionUpdateAction](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action)Added [UICollectionUpdateActionDelete](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action/delete)Added [UICollectionUpdateActionInsert](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action/insert)Added [UICollectionUpdateActionMove](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action/move)Added [UICollectionUpdateActionNone](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action/none)Added [UICollectionUpdateActionReload](https://developer.apple.com/documentation/uikit/uicollectionupdateaction/uicollectionupdateactionreload)Added UICollectionViewLayout(SubclassingHooks)Added UICollectionViewLayout(UpdateSupportHooks)UIColor.hModified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSCopying |

UIDatePicker.hModified [UIDatePicker.locale](https://developer.apple.com/documentation/uikit/uidatepicker/1615995-locale)

|  | Deprecation |
| --- | --- |
| From | iOS 5.0 |
| To | _none_ |

UIDevice.hAdded [UIDevice.identifierForVendor](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor)UIDocumentInteractionController.hModified [-[UIDocumentInteractionControllerDelegate documentInteractionController:canPerformAction:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616800-documentinteractioncontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionController:performAction:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616823-documentinteractioncontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

UIFont.hModified [UIFont](https://developer.apple.com/documentation/uikit/uifont)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

UIImage.hAdded [UIImage.alignmentRectInsets](https://developer.apple.com/documentation/uikit/uiimage/1624139-alignmentrectinsets)Added [+[UIImage animatedResizableImageNamed:capInsets:resizingMode:duration:]](https://developer.apple.com/documentation/uikit/uiimage/1624103-animatedresizableimagenamed)Added [-[UIImage imageWithAlignmentRectInsets:]](https://developer.apple.com/documentation/uikit/uiimage/1624100-withalignmentrectinsets)Added [+[UIImage imageWithCIImage:scale:orientation:]](https://developer.apple.com/documentation/uikit/uiimage/1624152-imagewithciimage)Added [+[UIImage imageWithData:scale:]](https://developer.apple.com/documentation/uikit/uiimage/1624099-imagewithdata)Added [-[UIImage initWithCIImage:scale:orientation:]](https://developer.apple.com/documentation/uikit/uiimage/1624150-init)Added [-[UIImage initWithData:scale:]](https://developer.apple.com/documentation/uikit/uiimage/1624109-initwithdata)Added [-[UIImage resizableImageWithCapInsets:resizingMode:]](https://developer.apple.com/documentation/uikit/uiimage/1624127-resizableimagewithcapinsets)Added [UIImage.resizingMode](https://developer.apple.com/documentation/uikit/uiimage/1624157-resizingmode)Added [UIImageResizingMode](https://developer.apple.com/documentation/uikit/uiimageresizingmode)Added [UIImageResizingModeStretch](https://developer.apple.com/documentation/uikit/uiimage/resizingmode/stretch)Added [UIImageResizingModeTile](https://developer.apple.com/documentation/uikit/uiimageresizingmode/uiimageresizingmodetile)UIKitDefines.hRemoved #def UIKIT_CLASS_AVAILABLEAdded #def instancetypeUILabel.hAdded [UILabel.adjustsLetterSpacingToFitWidth](https://developer.apple.com/documentation/uikit/uilabel/1620535-adjustsletterspacingtofitwidth)Added [UILabel.attributedText](https://developer.apple.com/documentation/uikit/uilabel/1620542-attributedtext)Added [UILabel.minimumScaleFactor](https://developer.apple.com/documentation/uikit/uilabel/1620544-minimumscalefactor)Added [UILabel.preferredMaxLayoutWidth](https://developer.apple.com/documentation/uikit/uilabel/1620534-preferredmaxlayoutwidth)Modified [UILabel.textAlignment](https://developer.apple.com/documentation/uikit/uilabel/1620541-textalignment)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UITextAlignment textAlignment |
| To | @property(nonatomic) NSTextAlignment textAlignment |

Modified [UILabel.minimumFontSize](https://developer.apple.com/documentation/uikit/uilabel/1620529-minimumfontsize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [UILabel.lineBreakMode](https://developer.apple.com/documentation/uikit/uilabel/1620525-linebreakmode)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UILineBreakMode lineBreakMode |
| To | @property(nonatomic) NSLineBreakMode lineBreakMode |

UILongPressGestureRecognizer.hModified [UILongPressGestureRecognizer.numberOfTapsRequired](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/1616424-numberoftapsrequired)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) NSInteger numberOfTapsRequired |
| To | @property(nonatomic) NSUInteger numberOfTapsRequired |

Modified [UILongPressGestureRecognizer.numberOfTouchesRequired](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/1616425-numberoftouchesrequired)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) NSInteger numberOfTouchesRequired |
| To | @property(nonatomic) NSUInteger numberOfTouchesRequired |

UINavigationBar.hRemoved UINavigationBar.UI_APPEARANCE_SELECTOR (no architecture available)Added [UINavigationBar.shadowImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624963-shadowimage)UINavigationController.hAdded [-[UINavigationController initWithNavigationBarClass:toolbarClass:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621866-initwithnavigationbarclass)UIPageControl.hAdded [UIPageControl.currentPageIndicatorTintColor](https://developer.apple.com/documentation/uikit/uipagecontrol/1621233-currentpageindicatortintcolor)Added [UIPageControl.pageIndicatorTintColor](https://developer.apple.com/documentation/uikit/uipagecontrol/1621239-pageindicatortintcolor)UIPageViewController.hAdded [-[UIPageViewControllerDataSource presentationCountForPageViewController:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614095-presentationcount)Added [-[UIPageViewControllerDataSource presentationIndexForPageViewController:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614116-presentationindex)Added [-[UIPageViewControllerDelegate pageViewController:willTransitionToViewControllers:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614091-pageviewcontroller)Added [UIPageViewControllerOptionInterPageSpacingKey](https://developer.apple.com/documentation/uikit/uipageviewcontrolleroptioninterpagespacingkey)Added [UIPageViewControllerTransitionStyleScroll](https://developer.apple.com/documentation/uikit/uipageviewcontroller/transitionstyle/scroll)UIPickerView.hAdded [-[UIPickerViewDelegate pickerView:attributedTitleForRow:forComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614375-pickerview)UIPopoverBackgroundView.hAdded [+[UIPopoverBackgroundView wantsDefaultContentAppearance]](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/1619357-wantsdefaultcontentappearance)UIPrintFormatter.hModified [UISimpleTextPrintFormatter.textAlignment](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621832-textalignment)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UITextAlignment textAlignment |
| To | @property(nonatomic) NSTextAlignment textAlignment |

UIProgressView.hRemoved UIProgressView.UI_APPEARANCE_SELECTOR (no architecture available)UIRefreshControl.hAdded [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol)Added [UIRefreshControl.attributedTitle](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624845-attributedtitle)Added [-[UIRefreshControl beginRefreshing]](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624842-beginrefreshing)Added [-[UIRefreshControl endRefreshing]](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624848-endrefreshing)Added [-[UIRefreshControl init]](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624846-init)Added [UIRefreshControl.refreshing](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624844-refreshing)Added [UIRefreshControl.tintColor](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624847-tintcolor)UIResponder.hAdded -[NSObject toggleBoldface:]Added -[NSObject toggleItalics:]Added -[NSObject toggleUnderline:]UISearchBar.hRemoved UISearchBar.UI_APPEARANCE_SELECTOR (no architecture available)Added [UISearchBar.inputAccessoryView](https://developer.apple.com/documentation/uikit/uisearchbar/1624279-inputaccessoryview)UISegmentedControl.hRemoved UISegmentedControl.UI_APPEARANCE_SELECTOR (no architecture available)UISlider.hRemoved UISlider.UI_APPEARANCE_SELECTOR (no architecture available)UIStateRestoration.hAdded [UIDataSourceModelAssociation](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation)Added [-[UIDataSourceModelAssociation indexPathForElementWithModelIdentifier:inView:]](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/1616850-indexpathforelementwithmodeliden)Added [-[UIDataSourceModelAssociation modelIdentifierForElementAtIndexPath:inView:]](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/1616862-modelidentifierforelement)Added [UIViewControllerRestoration](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration)Added [+[UIViewControllerRestoration viewControllerWithRestorationIdentifierPath:coder:]](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration/1616859-viewcontroller)Added [UIApplicationStateRestorationBundleVersionKey](https://developer.apple.com/documentation/uikit/uiapplication/1616852-staterestorationbundleversionkey)Added [UIApplicationStateRestorationUserInterfaceIdiomKey](https://developer.apple.com/documentation/uikit/uiapplication/1616853-staterestorationuserinterfaceidi)Added [UIStateRestorationViewControllerStoryboardKey](https://developer.apple.com/documentation/uikit/uiapplication/1616861-staterestorationviewcontrollerst)UIStepper.hAdded [-[UIStepper backgroundImageForState:]](https://developer.apple.com/documentation/uikit/uistepper/1624069-backgroundimageforstate)Added [-[UIStepper decrementImageForState:]](https://developer.apple.com/documentation/uikit/uistepper/1624077-decrementimageforstate)Added [-[UIStepper dividerImageForLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uistepper/1624072-dividerimageforleftsegmentstate)Added [-[UIStepper incrementImageForState:]](https://developer.apple.com/documentation/uikit/uistepper/1624080-incrementimageforstate)Added [-[UIStepper setBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uistepper/1624081-setbackgroundimage)Added [-[UIStepper setDecrementImage:forState:]](https://developer.apple.com/documentation/uikit/uistepper/1624074-setdecrementimage)Added [-[UIStepper setDividerImage:forLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uistepper/1624071-setdividerimage)Added [-[UIStepper setIncrementImage:forState:]](https://developer.apple.com/documentation/uikit/uistepper/1624070-setincrementimage)Added [UIStepper.tintColor](https://developer.apple.com/documentation/uikit/uistepper/1624073-tintcolor)UIStoryboardSegue.hAdded [+[UIStoryboardSegue segueWithIdentifier:source:destination:performHandler:]](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621910-init)UIStringDrawing.hModified [-[NSString sizeWithFont:constrainedToSize:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619915-sizewithfont)

|  | Declaration |
| --- | --- |
| From | - (CGSize)sizeWithFont:(UIFont \*)font constrainedToSize:(CGSize)size lineBreakMode:(UILineBreakMode)lineBreakMode |
| To | - (CGSize)sizeWithFont:(UIFont \*)font constrainedToSize:(CGSize)size lineBreakMode:(NSLineBreakMode)lineBreakMode |

Modified [-[NSString drawAtPoint:forWidth:withFont:minFontSize:actualFontSize:lineBreakMode:baselineAdjustment:]](https://developer.apple.com/documentation/foundation/nsstring/1619894-drawatpoint)

|  | Declaration |
| --- | --- |
| From | - (CGSize)drawAtPoint:(CGPoint)point forWidth:(CGFloat)width withFont:(UIFont \*)font minFontSize:(CGFloat)minFontSize actualFontSize:(CGFloat \*)actualFontSize lineBreakMode:(UILineBreakMode)lineBreakMode baselineAdjustment:(UIBaselineAdjustment)baselineAdjustment |
| To | - (CGSize)drawAtPoint:(CGPoint)point forWidth:(CGFloat)width withFont:(UIFont \*)font minFontSize:(CGFloat)minFontSize actualFontSize:(CGFloat \*)actualFontSize lineBreakMode:(NSLineBreakMode)lineBreakMode baselineAdjustment:(UIBaselineAdjustment)baselineAdjustment |

Modified [-[NSString drawAtPoint:forWidth:withFont:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619896-drawatpoint)

|  | Declaration |
| --- | --- |
| From | - (CGSize)drawAtPoint:(CGPoint)point forWidth:(CGFloat)width withFont:(UIFont \*)font lineBreakMode:(UILineBreakMode)lineBreakMode |
| To | - (CGSize)drawAtPoint:(CGPoint)point forWidth:(CGFloat)width withFont:(UIFont \*)font lineBreakMode:(NSLineBreakMode)lineBreakMode |

Modified [-[NSString drawInRect:withFont:lineBreakMode:alignment:]](https://developer.apple.com/documentation/foundation/nsstring/1619912-drawinrect)

|  | Declaration |
| --- | --- |
| From | - (CGSize)drawInRect:(CGRect)rect withFont:(UIFont \*)font lineBreakMode:(UILineBreakMode)lineBreakMode alignment:(UITextAlignment)alignment |
| To | - (CGSize)drawInRect:(CGRect)rect withFont:(UIFont \*)font lineBreakMode:(NSLineBreakMode)lineBreakMode alignment:(NSTextAlignment)alignment |

Modified [-[NSString drawInRect:withFont:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619908-drawinrect)

|  | Declaration |
| --- | --- |
| From | - (CGSize)drawInRect:(CGRect)rect withFont:(UIFont \*)font lineBreakMode:(UILineBreakMode)lineBreakMode |
| To | - (CGSize)drawInRect:(CGRect)rect withFont:(UIFont \*)font lineBreakMode:(NSLineBreakMode)lineBreakMode |

Modified [-[NSString drawAtPoint:forWidth:withFont:fontSize:lineBreakMode:baselineAdjustment:]](https://developer.apple.com/documentation/foundation/nsstring/1619919-drawatpoint)

|  | Declaration |
| --- | --- |
| From | - (CGSize)drawAtPoint:(CGPoint)point forWidth:(CGFloat)width withFont:(UIFont \*)font fontSize:(CGFloat)fontSize lineBreakMode:(UILineBreakMode)lineBreakMode baselineAdjustment:(UIBaselineAdjustment)baselineAdjustment |
| To | - (CGSize)drawAtPoint:(CGPoint)point forWidth:(CGFloat)width withFont:(UIFont \*)font fontSize:(CGFloat)fontSize lineBreakMode:(NSLineBreakMode)lineBreakMode baselineAdjustment:(UIBaselineAdjustment)baselineAdjustment |

Modified [-[NSString sizeWithFont:forWidth:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619914-sizewithfont)

|  | Declaration |
| --- | --- |
| From | - (CGSize)sizeWithFont:(UIFont \*)font forWidth:(CGFloat)width lineBreakMode:(UILineBreakMode)lineBreakMode |
| To | - (CGSize)sizeWithFont:(UIFont \*)font forWidth:(CGFloat)width lineBreakMode:(NSLineBreakMode)lineBreakMode |

Modified [-[NSString sizeWithFont:minFontSize:actualFontSize:forWidth:lineBreakMode:]](https://developer.apple.com/documentation/foundation/nsstring/1619903-sizewithfont)

|  | Declaration |
| --- | --- |
| From | - (CGSize)sizeWithFont:(UIFont \*)font minFontSize:(CGFloat)minFontSize actualFontSize:(CGFloat \*)actualFontSize forWidth:(CGFloat)width lineBreakMode:(UILineBreakMode)lineBreakMode |
| To | - (CGSize)sizeWithFont:(UIFont \*)font minFontSize:(CGFloat)minFontSize actualFontSize:(CGFloat \*)actualFontSize forWidth:(CGFloat)width lineBreakMode:(NSLineBreakMode)lineBreakMode |

UISwitch.hRemoved UISwitch.UI_APPEARANCE_SELECTOR (no architecture available)Added [UISwitch.offImage](https://developer.apple.com/documentation/uikit/uiswitch/1623683-offimage)Added [UISwitch.onImage](https://developer.apple.com/documentation/uikit/uiswitch/1623689-onimage)Added [UISwitch.thumbTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623684-thumbtintcolor)Added [UISwitch.tintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623688-tintcolor)UITabBar.hRemoved UITabBar.UI_APPEARANCE_SELECTOR (no architecture available)Added [UITabBar.shadowImage](https://developer.apple.com/documentation/uikit/uitabbar/1623452-shadowimage)UITabBarItem.hRemoved -[UITabBarItem UI_APPEARANCE_SELECTOR] (no architecture available)UITableView.hAdded [-[UITableView dequeueReusableCellWithIdentifier:forIndexPath:]](https://developer.apple.com/documentation/uikit/uitableview/1614878-dequeuereusablecellwithidentifie)Added [-[UITableView dequeueReusableHeaderFooterViewWithIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614975-dequeuereusableheaderfootervieww)Added [-[UITableView footerViewForSection:]](https://developer.apple.com/documentation/uikit/uitableview/1614972-footerview)Added [-[UITableView headerViewForSection:]](https://developer.apple.com/documentation/uikit/uitableview/1614965-headerview)Added [-[UITableView registerClass:forCellReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614888-registerclass)Added [-[UITableView registerClass:forHeaderFooterViewReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614964-registerclass)Added [-[UITableView registerNib:forHeaderFooterViewReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614921-register)Added [UITableView.sectionIndexColor](https://developer.apple.com/documentation/uikit/uitableview/1614915-sectionindexcolor)Added [UITableView.sectionIndexTrackingBackgroundColor](https://developer.apple.com/documentation/uikit/uitableview/1614992-sectionindextrackingbackgroundco)Added [-[UITableViewDelegate tableView:didEndDisplayingCell:forRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614870-tableview)Added [-[UITableViewDelegate tableView:didEndDisplayingFooterView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614856-tableview)Added [-[UITableViewDelegate tableView:didEndDisplayingHeaderView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614971-tableview)Added [-[UITableViewDelegate tableView:didHighlightRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614982-tableview)Added [-[UITableViewDelegate tableView:didUnhighlightRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614868-tableview)Added [-[UITableViewDelegate tableView:shouldHighlightRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614988-tableview)Added [-[UITableViewDelegate tableView:willDisplayFooterView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614941-tableview)Added [-[UITableViewDelegate tableView:willDisplayHeaderView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614905-tableview)UITableViewCell.hModified [UITableViewCell.textAlignment](https://developer.apple.com/documentation/uikit/uitableviewcell/1623284-textalignment)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UITextAlignment textAlignment |
| To | @property(nonatomic) NSTextAlignment textAlignment |

Modified [UITableViewCell.lineBreakMode](https://developer.apple.com/documentation/uikit/uitableviewcell/1623259-linebreakmode)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UILineBreakMode lineBreakMode |
| To | @property(nonatomic) NSLineBreakMode lineBreakMode |

UITableViewController.hAdded [UITableViewController.refreshControl](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614752-refreshcontrol)UITableViewHeaderFooterView.hAdded [UITableViewHeaderFooterView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview)Added [UITableViewHeaderFooterView.backgroundView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624913-backgroundview)Added [UITableViewHeaderFooterView.contentView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624914-contentview)Added [UITableViewHeaderFooterView.detailTextLabel](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624910-detailtextlabel)Added [-[UITableViewHeaderFooterView initWithReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624918-initwithreuseidentifier)Added [-[UITableViewHeaderFooterView prepareForReuse]](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624916-prepareforreuse)Added [UITableViewHeaderFooterView.reuseIdentifier](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624909-reuseidentifier)Added [UITableViewHeaderFooterView.textLabel](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624912-textlabel)Added UITableViewHeaderFooterView.tintColorUITextField.hAdded [UITextField.allowsEditingTextAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619628-allowseditingtextattributes)Added [UITextField.attributedPlaceholder](https://developer.apple.com/documentation/uikit/uitextfield/1619610-attributedplaceholder)Added [UITextField.attributedText](https://developer.apple.com/documentation/uikit/uitextfield/1619602-attributedtext)Added [UITextField.clearsOnInsertion](https://developer.apple.com/documentation/uikit/uitextfield/1619631-clearsoninsertion)Added [UITextField.typingAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619632-typingattributes)Modified [UITextField.textAlignment](https://developer.apple.com/documentation/uikit/uitextfield/1619643-textalignment)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UITextAlignment textAlignment |
| To | @property(nonatomic) NSTextAlignment textAlignment |

UITextInput.hAdded [-[UITextInput frameForDictationResultPlaceholder:]](https://developer.apple.com/documentation/uikit/uitextinput/1614493-framefordictationresultplacehold)Added [-[UITextInput insertDictationResultPlaceholder]](https://developer.apple.com/documentation/uikit/uitextinput/1614466-insertdictationresultplaceholder)Added [-[UITextInput removeDictationResultPlaceholder:willInsertResult:]](https://developer.apple.com/documentation/uikit/uitextinput/1614546-removedictationresultplaceholder)Added [-[UITextInput selectionRectsForRange:]](https://developer.apple.com/documentation/uikit/uitextinput/1614458-selectionrectsforrange)Added [-[UITextInput shouldChangeTextInRange:replacementText:]](https://developer.apple.com/documentation/uikit/uitextinput/1614495-shouldchangetext)Added [UITextSelectionRect](https://developer.apple.com/documentation/uikit/uitextselectionrect)Added [UITextSelectionRect.containsEnd](https://developer.apple.com/documentation/uikit/uitextselectionrect/1614516-containsend)Added [UITextSelectionRect.containsStart](https://developer.apple.com/documentation/uikit/uitextselectionrect/1614560-containsstart)Added [UITextSelectionRect.isVertical](https://developer.apple.com/documentation/uikit/uitextselectionrect/1614561-isvertical)Added [UITextSelectionRect.rect](https://developer.apple.com/documentation/uikit/uitextselectionrect/1614461-rect)Added [UITextSelectionRect.writingDirection](https://developer.apple.com/documentation/uikit/uitextselectionrect/1614569-writingdirection)UITextView.hAdded [UITextView.allowsEditingTextAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618622-allowseditingtextattributes)Added [UITextView.attributedText](https://developer.apple.com/documentation/uikit/uitextview/1618626-attributedtext)Added [UITextView.clearsOnInsertion](https://developer.apple.com/documentation/uikit/uitextview/1618605-clearsoninsertion)Added [UITextView.typingAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618629-typingattributes)Modified [UITextView.textAlignment](https://developer.apple.com/documentation/uikit/uitextview/1618618-textalignment)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic) UITextAlignment textAlignment |
| To | @property(nonatomic) NSTextAlignment textAlignment |

UIToolbar.hRemoved UIToolbar.UI_APPEARANCE_SELECTOR (no architecture available)Added [-[UIToolbar setShadowImage:forToolbarPosition:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617991-setshadowimage)Added [-[UIToolbar shadowImageForToolbarPosition:]](https://developer.apple.com/documentation/uikit/uitoolbar/1618000-shadowimage)UITouch.hRemoved #def UITOUCH_IVARS_PRIVATEUIView.hAdded [-[UIView addConstraint:]](https://developer.apple.com/documentation/uikit/uiview/1622523-addconstraint)Added [-[UIView addConstraints:]](https://developer.apple.com/documentation/uikit/uiview/1622513-addconstraints)Added [-[UIView alignmentRectForFrame:]](https://developer.apple.com/documentation/uikit/uiview/1622576-alignmentrectforframe)Added [-[UIView alignmentRectInsets]](https://developer.apple.com/documentation/uikit/uiview/1622648-alignmentrectinsets)Added [-[UIView constraints]](https://developer.apple.com/documentation/uikit/uiview/1622464-constraints)Added [-[UIView constraintsAffectingLayoutForAxis:]](https://developer.apple.com/documentation/uikit/uiview/1622432-constraintsaffectinglayoutforaxi)Added [-[UIView contentCompressionResistancePriorityForAxis:]](https://developer.apple.com/documentation/uikit/uiview/1622465-contentcompressionresistanceprio)Added [-[UIView contentHuggingPriorityForAxis:]](https://developer.apple.com/documentation/uikit/uiview/1622556-contenthuggingpriorityforaxis)Added [-[UIView decodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiview/1622638-decoderestorablestate)Added [-[UIView encodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiview/1622516-encoderestorablestate)Added [-[UIView exerciseAmbiguityInLayout]](https://developer.apple.com/documentation/uikit/uiview/1622545-exerciseambiguityinlayout)Added [-[UIView frameForAlignmentRect:]](https://developer.apple.com/documentation/uikit/uiview/1622603-frameforalignmentrect)Added [-[UIView gestureRecognizerShouldBegin:]](https://developer.apple.com/documentation/uikit/uiview/1622460-gesturerecognizershouldbegin)Added [-[UIView hasAmbiguousLayout]](https://developer.apple.com/documentation/uikit/uiview/1622517-hasambiguouslayout)Added [-[UIView intrinsicContentSize]](https://developer.apple.com/documentation/uikit/uiview/1622600-intrinsiccontentsize)Added [-[UIView invalidateIntrinsicContentSize]](https://developer.apple.com/documentation/uikit/uiview/1622457-invalidateintrinsiccontentsize)Added [-[UIView needsUpdateConstraints]](https://developer.apple.com/documentation/uikit/uiview/1622567-needsupdateconstraints)Added [-[UIView removeConstraint:]](https://developer.apple.com/documentation/uikit/uiview/1622659-removeconstraint)Added [-[UIView removeConstraints:]](https://developer.apple.com/documentation/uikit/uiview/1622593-removeconstraints)Added [+[UIView requiresConstraintBasedLayout]](https://developer.apple.com/documentation/uikit/uiview/1622549-requiresconstraintbasedlayout)Added [UIView.restorationIdentifier](https://developer.apple.com/documentation/uikit/uiview/1622494-restorationidentifier)Added [-[UIView setContentCompressionResistancePriority:forAxis:]](https://developer.apple.com/documentation/uikit/uiview/1622526-setcontentcompressionresistancep)Added [-[UIView setContentHuggingPriority:forAxis:]](https://developer.apple.com/documentation/uikit/uiview/1622485-setcontenthuggingpriority)Added [-[UIView setNeedsUpdateConstraints]](https://developer.apple.com/documentation/uikit/uiview/1622450-setneedsupdateconstraints)Added [-[UIView setTranslatesAutoresizingMaskIntoConstraints:]](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco)Added [-[UIView systemLayoutSizeFittingSize:]](https://developer.apple.com/documentation/uikit/uiview/1622624-systemlayoutsizefittingsize)Added [-[UIView translatesAutoresizingMaskIntoConstraints]](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco)Added [-[UIView updateConstraints]](https://developer.apple.com/documentation/uikit/uiview/1622512-updateconstraints)Added [-[UIView updateConstraintsIfNeeded]](https://developer.apple.com/documentation/uikit/uiview/1622595-updateconstraintsifneeded)Added [-[UIView viewForBaselineLayout]](https://developer.apple.com/documentation/uikit/uiview/1622439-forbaselinelayout)Added [UILayoutConstraintAxis](https://developer.apple.com/documentation/uikit/uilayoutconstraintaxis)Added [UILayoutConstraintAxisHorizontal](https://developer.apple.com/documentation/uikit/nslayoutconstraint/axis/horizontal)Added [UILayoutConstraintAxisVertical](https://developer.apple.com/documentation/uikit/nslayoutconstraint/axis/vertical)Added [UILayoutFittingCompressedSize](https://developer.apple.com/documentation/uikit/uiview/1622568-layoutfittingcompressedsize)Added [UILayoutFittingExpandedSize](https://developer.apple.com/documentation/uikit/uiview/1622532-layoutfittingexpandedsize)Added UIView(UIConstraintBasedCompatibility)Added UIView(UIConstraintBasedLayoutCoreMethods)Added UIView(UIConstraintBasedLayoutDebugging)Added UIView(UIConstraintBasedLayoutFittingSize)Added UIView(UIConstraintBasedLayoutInstallingConstraints)Added UIView(UIConstraintBasedLayoutLayering)Added UIView(UIStateRestoration)Added [UIViewNoIntrinsicMetric](https://developer.apple.com/documentation/uikit/uiview/1622486-nointrinsicmetric)Modified [UIView.contentStretch](https://developer.apple.com/documentation/uikit/uiview/1622511-contentstretch)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

UIViewController.hAdded [-[UIViewController beginAppearanceTransition:animated:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621387-beginappearancetransition)Added [-[UIViewController canPerformUnwindSegueAction:fromViewController:withSender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621449-canperformunwindsegueaction)Added [-[UIViewController decodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621429-decoderestorablestatewithcoder)Added [-[UIViewController encodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621461-encoderestorablestatewithcoder)Added [-[UIViewController endAppearanceTransition]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621503-endappearancetransition)Added [-[UIViewController preferredInterfaceOrientationForPresentation]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621438-preferredinterfaceorientationfor)Added [UIViewController.restorationClass](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621472-restorationclass)Added [UIViewController.restorationIdentifier](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621499-restorationidentifier)Added [-[UIViewController segueForUnwindingToViewController:fromViewController:identifier:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621500-segueforunwinding)Added [-[UIViewController shouldAutomaticallyForwardAppearanceMethods]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621389-shouldautomaticallyforwardappear)Added [-[UIViewController shouldAutomaticallyForwardRotationMethods]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621480-shouldautomaticallyforwardrotati)Added [-[UIViewController shouldAutorotate]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621419-shouldautorotate)Added [-[UIViewController shouldPerformSegueWithIdentifier:sender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621502-shouldperformseguewithidentifier)Added [-[UIViewController supportedInterfaceOrientations]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations)Added [-[UIViewController updateViewConstraints]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621379-updateviewconstraints)Added [-[UIViewController viewControllerForUnwindSegueAction:fromViewController:withSender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621448-forunwindsegueaction)Added UIViewController(UIConstraintBasedLayoutCoreMethods)Added UIViewController(UIStateRestoration)Modified [UIViewController.modalViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621479-modalviewcontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIViewController automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621393-automaticallyforwardappearancean)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIViewController dismissModalViewControllerAnimated:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621369-dismissmodalviewcontrolleranimat)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIViewController viewDidUnload]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621383-viewdidunload)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIViewController presentModalViewController:animated:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIViewController viewWillUnload]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621427-viewwillunload)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

Modified [-[UIViewController shouldAutorotateToInterfaceOrientation:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621459-shouldautorotatetointerfaceorien)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 6.0 |

UIWebView.hAdded [UIWebView.keyboardDisplayRequiresUserAction](https://developer.apple.com/documentation/uikit/uiwebview/1617967-keyboarddisplayrequiresuseractio)Added [UIWebView.suppressesIncrementalRendering](https://developer.apple.com/documentation/uikit/uiwebview/1617984-suppressesincrementalrendering)

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
