---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Accelerate.html
archived_at: '2026-07-18T02:54:24.318905Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Accelerate Changes

## Accelerate

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

Alpha.hAdded [vImagePremultipliedAlphaBlend_BGRA8888()](https://developer.apple.com/documentation/accelerate/1410682-vimagepremultipliedalphablend_bg)Added [vImagePremultipliedAlphaBlend_BGRAFFFF()](https://developer.apple.com/documentation/accelerate/1410634-vimagepremultipliedalphablend_bg)Added [#def vImagePremultipliedAlphaBlend_RGBA8888](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablend_rgba8888)Added [#def vImagePremultipliedAlphaBlend_RGBAFFFF](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablend_rgbaffff)Added [#def vImagePremultiplyData_BGRA8888](https://developer.apple.com/documentation/accelerate/vimagepremultiplydata_bgra8888)Added [#def vImagePremultiplyData_BGRAFFFF](https://developer.apple.com/documentation/accelerate/vimagepremultiplydata_bgraffff)Added [#def vImageUnpremultiplyData_BGRA8888](https://developer.apple.com/documentation/accelerate/vimageunpremultiplydata_bgra8888)Added [#def vImageUnpremultiplyData_BGRAFFFF](https://developer.apple.com/documentation/accelerate/vimageunpremultiplydata_bgraffff)Conversion.hAdded [vImageConvert_Planar8ToARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533069-vimageconvert_planar8toargbffff)Added [vImageConvert_Planar8ToBGRX8888()](https://developer.apple.com/documentation/accelerate/1533215-vimageconvert_planar8tobgrx8888)Added [vImageConvert_Planar8ToBGRXFFFF()](https://developer.apple.com/documentation/accelerate/1533138-vimageconvert_planar8tobgrxffff)Added [#def vImageConvert_Planar8ToRGBX8888](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8torgbx8888)Added [#def vImageConvert_Planar8ToRGBXFFFF](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8torgbxffff)Added [vImageConvert_Planar8ToXRGB8888()](https://developer.apple.com/documentation/accelerate/1533265-vimageconvert_planar8toxrgb8888)Added [vImageConvert_Planar8ToXRGBFFFF()](https://developer.apple.com/documentation/accelerate/1533232-vimageconvert_planar8toxrgbffff)Added [vImageConvert_PlanarFToARGB8888()](https://developer.apple.com/documentation/accelerate/1533216-vimageconvert_planarftoargb8888)Added [vImageConvert_PlanarFToBGRX8888()](https://developer.apple.com/documentation/accelerate/1533213-vimageconvert_planarftobgrx8888)Added [vImageConvert_PlanarFToBGRXFFFF()](https://developer.apple.com/documentation/accelerate/1533052-vimageconvert_planarftobgrxffff)Added [#def vImageConvert_PlanarFToRGBX8888](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftorgbx8888)Added [#def vImageConvert_PlanarFToRGBXFFFF](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftorgbxffff)Added [vImageConvert_PlanarFToXRGB8888()](https://developer.apple.com/documentation/accelerate/1533297-vimageconvert_planarftoxrgb8888)Added [vImageConvert_PlanarFToXRGBFFFF()](https://developer.apple.com/documentation/accelerate/1533208-vimageconvert_planarftoxrgbffff)cblas.hAdded [cblas_xerbla()](https://developer.apple.com/documentation/accelerate/1513114-cblas_xerbla)clapack.hRemoved clar1v_311_()Removed clarrv_311_()Removed csrot_()Removed dlar1v_311_()Removed dlarrb_311_()Removed dlarre_311_()Removed dlarrf_311_()Removed dlarrv_311_()Removed dlasd9_()Removed dlazq3_()Removed dlazq4_()Removed dsecnd_()Removed lsame_()Removed second_()Removed slar1v_311_()Removed slarrb_311_()Removed slarre_311_()Removed slarrf_311_()Removed slarrv_311_()Removed slasd9_()Removed slazq3_()Removed slazq4_()Removed xerbla_()Removed zdrot_()Removed zlar1v_311_()Removed zlarrv_311_()Added cgbequb_()Added cgeequb_()Added cheequb_()Added chfrk_()Added chla_transtype__()Added clanhf_()Added clarfp_()Added clarscl2_()Added clascl2_()Added cpftrf_()Added cpftri_()Added cpftrs_()Added cpoequb_()Added cpstf2_()Added cpstrf_()Added csyequb_()Added ctfsm_()Added ctftri_()Added ctfttp_()Added ctfttr_()Added ctpttf_()Added ctpttr_()Added ctrttf_()Added ctrttp_()Added dgbequb_()Added dgeequb_()Added dgejsv_()Added dgesvj_()Added dgsvj0_()Added dgsvj1_()Added disnan_()Added dlaisnan_()Added dlaneg_()Added dlansf_()Added dlarfp_()Added dlarscl2_()Added dlascl2_()Added dlat2s_()Added dpftrf_()Added dpftri_()Added dpftrs_()Added dpoequb_()Added dpstf2_()Added dpstrf_()Added dsfrk_()Added dsposv_()Added dsyequb_()Added dtfsm_()Added dtftri_()Added dtfttp_()Added dtfttr_()Added dtpttf_()Added dtpttr_()Added dtrttf_()Added dtrttp_()Added ilaclc_()Added ilaclr_()Added iladiag_()Added iladlc_()Added iladlr_()Added ilaprec_()Added ilaslc_()Added ilaslr_()Added ilatrans_()Added ilauplo_()Added ilazlc_()Added ilazlr_()Added iparmq_()Added sgbequb_()Added sgeequb_()Added sgejsv_()Added sgesvj_()Added sgsvj0_()Added sgsvj1_()Added sisnan_()Added slaisnan_()Added slaneg_()Added slansf_()Added slarfp_()Added slarscl2_()Added slascl2_()Added smaxloc_()Added spftrf_()Added spftri_()Added spftrs_()Added spoequb_()Added spstf2_()Added spstrf_()Added ssfrk_()Added ssyequb_()Added stfsm_()Added stftri_()Added stfttp_()Added stfttr_()Added stpttf_()Added stpttr_()Added strttf_()Added strttp_()Added zcposv_()Added zgbequb_()Added zgeequb_()Added zheequb_()Added zhfrk_()Added zlanhf_()Added zlarfp_()Added zlarscl2_()Added zlascl2_()Added zlat2c_()Added zpftrf_()Added zpftri_()Added zpftrs_()Added zpoequb_()Added zpstf2_()Added zpstrf_()Added zsyequb_()Added ztfsm_()Added ztftri_()Added ztfttp_()Added ztfttr_()Added ztpttf_()Added ztpttr_()Added ztrttf_()Added ztrttp_()Modified slarre_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int slarre_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*e, __CLPK_real \*tol, __CLPK_integer \*nsplit, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_real \*w, __CLPK_real \*woff, __CLPK_real \*gersch, __CLPK_real \*work, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int slarre_ ( char \*range, __CLPK_integer \*n, __CLPK_real \*vl, __CLPK_real \*vu, __CLPK_integer \*il, __CLPK_integer \*iu, __CLPK_real \*d__, __CLPK_real \*e, __CLPK_real \*e2, __CLPK_real \*rtol1, __CLPK_real \*rtol2, __CLPK_real \*spltol, __CLPK_integer \*nsplit, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_real \*w, __CLPK_real \*werr, __CLPK_real \*wgap, __CLPK_integer \*iblock, __CLPK_integer \*indexw, __CLPK_real \*gers, __CLPK_real \*pivmin, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |

Modified dlasq4_()

|  | Declaration |
| --- | --- |
| From | int dlasq4_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_doublereal \*z__, __CLPK_integer \*pp, __CLPK_integer \*n0in, __CLPK_doublereal \*dmin__, __CLPK_doublereal \*dmin1, __CLPK_doublereal \*dmin2, __CLPK_doublereal \*dn, __CLPK_doublereal \*dn1, __CLPK_doublereal \*dn2, __CLPK_doublereal \*tau, __CLPK_integer \*ttype); |
| To | int dlasq4_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_doublereal \*z__, __CLPK_integer \*pp, __CLPK_integer \*n0in, __CLPK_doublereal \*dmin__, __CLPK_doublereal \*dmin1, __CLPK_doublereal \*dmin2, __CLPK_doublereal \*dn, __CLPK_doublereal \*dn1, __CLPK_doublereal \*dn2, __CLPK_doublereal \*tau, __CLPK_integer \*ttype, __CLPK_doublereal \*g); |

Modified dlaqtr_()

|  | Declaration |
| --- | --- |
| From | int dlaqtr_ ( __CLPK_logical \*ltran, __CLPK_logical \*lreal, __CLPK_integer \*n, __CLPK_doublereal \*t, __CLPK_integer \*ldt, __CLPK_doublereal \*b, __CLPK_doublereal \*w, __CLPK_doublereal \*scale, __CLPK_doublereal \*x, __CLPK_doublereal \*work, __CLPK_integer \*info); |
| To | int dlaqtr_ ( __CLPK_logical \*ltran, __CLPK_logical \*l__CLPK_real, __CLPK_integer \*n, __CLPK_doublereal \*t, __CLPK_integer \*ldt, __CLPK_doublereal \*b, __CLPK_doublereal \*w, __CLPK_doublereal \*scale, __CLPK_doublereal \*x, __CLPK_doublereal \*work, __CLPK_integer \*info); |

Modified dlasq3_()

|  | Declaration |
| --- | --- |
| From | int dlasq3_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_doublereal \*z__, __CLPK_integer \*pp, __CLPK_doublereal \*dmin__, __CLPK_doublereal \*sigma, __CLPK_doublereal \*desig, __CLPK_doublereal \*qmax, __CLPK_integer \*nfail, __CLPK_integer \*iter, __CLPK_integer \*ndiv, __CLPK_logical \*ieee); |
| To | int dlasq3_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_doublereal \*z__, __CLPK_integer \*pp, __CLPK_doublereal \*dmin__, __CLPK_doublereal \*sigma, __CLPK_doublereal \*desig, __CLPK_doublereal \*qmax, __CLPK_integer \*nfail, __CLPK_integer \*iter, __CLPK_integer \*ndiv, __CLPK_logical \*ieee, __CLPK_integer \*ttype, __CLPK_doublereal \*dmin1, __CLPK_doublereal \*dmin2, __CLPK_doublereal \*dn, __CLPK_doublereal \*dn1, __CLPK_doublereal \*dn2, __CLPK_doublereal \*g, __CLPK_doublereal \*tau); |

Modified clar1v_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int clar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_real \*sigma, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_real \*lld, __CLPK_real \*gersch, __CLPK_complex \*z__, __CLPK_real \*ztz, __CLPK_real \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_real \*work); |
| To | Both | i386,x86_64 | int clar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_real \*lambda, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_real \*lld, __CLPK_real \*pivmin, __CLPK_real \*gaptol, __CLPK_complex \*z__, __CLPK_logical \*wantnc, __CLPK_integer \*negcnt, __CLPK_real \*ztz, __CLPK_real \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_real \*nrminv, __CLPK_real \*resid, __CLPK_real \*rqcorr, __CLPK_real \*work); |

Modified dlarrv_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int dlarrv_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_doublereal \*w, __CLPK_integer \*iblock, __CLPK_doublereal \*gersch, __CLPK_doublereal \*tol, __CLPK_doublereal \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int dlarrv_ ( __CLPK_integer \*n, __CLPK_doublereal \*vl, __CLPK_doublereal \*vu, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*pivmin, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_integer \*dol, __CLPK_integer \*dou, __CLPK_doublereal \*minrgp, __CLPK_doublereal \*rtol1, __CLPK_doublereal \*rtol2, __CLPK_doublereal \*w, __CLPK_doublereal \*werr, __CLPK_doublereal \*wgap, __CLPK_integer \*iblock, __CLPK_integer \*indexw, __CLPK_doublereal \*gers, __CLPK_doublereal \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |

Modified slasq4_()

|  | Declaration |
| --- | --- |
| From | int slasq4_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_real \*z__, __CLPK_integer \*pp, __CLPK_integer \*n0in, __CLPK_real \*dmin__, __CLPK_real \*dmin1, __CLPK_real \*dmin2, __CLPK_real \*dn, __CLPK_real \*dn1, __CLPK_real \*dn2, __CLPK_real \*tau, __CLPK_integer \*ttype); |
| To | int slasq4_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_real \*z__, __CLPK_integer \*pp, __CLPK_integer \*n0in, __CLPK_real \*dmin__, __CLPK_real \*dmin1, __CLPK_real \*dmin2, __CLPK_real \*dn, __CLPK_real \*dn1, __CLPK_real \*dn2, __CLPK_real \*tau, __CLPK_integer \*ttype, __CLPK_real \*g); |

Modified dlarrf_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int dlarrf_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_doublereal \*lld, __CLPK_integer \*ifirst, __CLPK_integer \*ilast, __CLPK_doublereal \*w, __CLPK_doublereal \*dplus, __CLPK_doublereal \*lplus, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int dlarrf_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_integer \*clstrt, __CLPK_integer \*clend, __CLPK_doublereal \*w, __CLPK_doublereal \*wgap, __CLPK_doublereal \*werr, __CLPK_doublereal \*spdiam, __CLPK_doublereal \*clgapl, __CLPK_doublereal \*clgapr, __CLPK_doublereal \*pivmin, __CLPK_doublereal \*sigma, __CLPK_doublereal \*dplus, __CLPK_doublereal \*lplus, __CLPK_doublereal \*work, __CLPK_integer \*info); |

Modified zcgesv_()

|  | Declaration |
| --- | --- |
| From | int zcgesv_ ( __CLPK_integer \*n, __CLPK_integer \*nrhs, __CLPK_doublecomplex \*a, __CLPK_integer \*lda, __CLPK_integer \*ipiv, __CLPK_doublecomplex \*b, __CLPK_integer \*ldb, __CLPK_doublecomplex \*x, __CLPK_integer \*ldx, __CLPK_doublecomplex \*work, __CLPK_complex \*swork, __CLPK_integer \*iter, __CLPK_integer \*info); |
| To | int zcgesv_ ( __CLPK_integer \*n, __CLPK_integer \*nrhs, __CLPK_doublecomplex \*a, __CLPK_integer \*lda, __CLPK_integer \*ipiv, __CLPK_doublecomplex \*b, __CLPK_integer \*ldb, __CLPK_doublecomplex \*x, __CLPK_integer \*ldx, __CLPK_doublecomplex \*work, __CLPK_complex \*swork, __CLPK_doublereal \*rwork, __CLPK_integer \*iter, __CLPK_integer \*info); |

Modified clarrv_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int clarrv_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_real \*w, __CLPK_integer \*iblock, __CLPK_real \*gersch, __CLPK_real \*tol, __CLPK_complex \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int clarrv_ ( __CLPK_integer \*n, __CLPK_real \*vl, __CLPK_real \*vu, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*pivmin, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_integer \*dol, __CLPK_integer \*dou, __CLPK_real \*minrgp, __CLPK_real \*rtol1, __CLPK_real \*rtol2, __CLPK_real \*w, __CLPK_real \*werr, __CLPK_real \*wgap, __CLPK_integer \*iblock, __CLPK_integer \*indexw, __CLPK_real \*gers, __CLPK_complex \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |

Modified slar1v_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int slar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_real \*sigma, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_real \*lld, __CLPK_real \*gersch, __CLPK_real \*z__, __CLPK_real \*ztz, __CLPK_real \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_real \*work); |
| To | Both | i386,x86_64 | int slar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_real \*lambda, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_real \*lld, __CLPK_real \*pivmin, __CLPK_real \*gaptol, __CLPK_real \*z__, __CLPK_logical \*wantnc, __CLPK_integer \*negcnt, __CLPK_real \*ztz, __CLPK_real \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_real \*nrminv, __CLPK_real \*resid, __CLPK_real \*rqcorr, __CLPK_real \*work); |

Modified slarrb_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int slarrb_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_real \*lld, __CLPK_integer \*ifirst, __CLPK_integer \*ilast, __CLPK_real \*sigma, __CLPK_real \*reltol, __CLPK_real \*w, __CLPK_real \*wgap, __CLPK_real \*werr, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int slarrb_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*lld, __CLPK_integer \*ifirst, __CLPK_integer \*ilast, __CLPK_real \*rtol1, __CLPK_real \*rtol2, __CLPK_integer \*offset, __CLPK_real \*w, __CLPK_real \*wgap, __CLPK_real \*werr, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_real \*pivmin, __CLPK_real \*spdiam, __CLPK_integer \*twist, __CLPK_integer \*info); |

Modified slasq3_()

|  | Declaration |
| --- | --- |
| From | int slasq3_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_real \*z__, __CLPK_integer \*pp, __CLPK_real \*dmin__, __CLPK_real \*sigma, __CLPK_real \*desig, __CLPK_real \*qmax, __CLPK_integer \*nfail, __CLPK_integer \*iter, __CLPK_integer \*ndiv, __CLPK_logical \*ieee); |
| To | int slasq3_ ( __CLPK_integer \*i0, __CLPK_integer \*n0, __CLPK_real \*z__, __CLPK_integer \*pp, __CLPK_real \*dmin__, __CLPK_real \*sigma, __CLPK_real \*desig, __CLPK_real \*qmax, __CLPK_integer \*nfail, __CLPK_integer \*iter, __CLPK_integer \*ndiv, __CLPK_logical \*ieee, __CLPK_integer \*ttype, __CLPK_real \*dmin1, __CLPK_real \*dmin2, __CLPK_real \*dn, __CLPK_real \*dn1, __CLPK_real \*dn2, __CLPK_real \*g, __CLPK_real \*tau); |

Modified zlarrv_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int zlarrv_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_doublereal \*w, __CLPK_integer \*iblock, __CLPK_doublereal \*gersch, __CLPK_doublereal \*tol, __CLPK_doublecomplex \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int zlarrv_ ( __CLPK_integer \*n, __CLPK_doublereal \*vl, __CLPK_doublereal \*vu, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*pivmin, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_integer \*dol, __CLPK_integer \*dou, __CLPK_doublereal \*minrgp, __CLPK_doublereal \*rtol1, __CLPK_doublereal \*rtol2, __CLPK_doublereal \*w, __CLPK_doublereal \*werr, __CLPK_doublereal \*wgap, __CLPK_integer \*iblock, __CLPK_integer \*indexw, __CLPK_doublereal \*gers, __CLPK_doublecomplex \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |

Modified izmax1_()

|  | Declaration |
| --- | --- |
| From | int izmax1_ ( __CLPK_integer \*n, __CLPK_doublecomplex \*cx, __CLPK_integer \*incx); |
| To | __CLPK_integer izmax1_ ( __CLPK_integer \*n, __CLPK_doublecomplex \*cx, __CLPK_integer \*incx); |

Modified ieeeck_()

|  | Declaration |
| --- | --- |
| From | int ieeeck_ ( __CLPK_integer \*ispec, __CLPK_real \*zero, __CLPK_real \*one); |
| To | __CLPK_integer ieeeck_ ( __CLPK_integer \*ispec, __CLPK_real \*zero, __CLPK_real \*one); |

Modified slarrv_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int slarrv_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_real \*w, __CLPK_integer \*iblock, __CLPK_real \*gersch, __CLPK_real \*tol, __CLPK_real \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int slarrv_ ( __CLPK_integer \*n, __CLPK_real \*vl, __CLPK_real \*vu, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*pivmin, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_integer \*dol, __CLPK_integer \*dou, __CLPK_real \*minrgp, __CLPK_real \*rtol1, __CLPK_real \*rtol2, __CLPK_real \*w, __CLPK_real \*werr, __CLPK_real \*wgap, __CLPK_integer \*iblock, __CLPK_integer \*indexw, __CLPK_real \*gers, __CLPK_real \*z__, __CLPK_integer \*ldz, __CLPK_integer \*isuppz, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |

Modified dlarre_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int dlarre_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*e, __CLPK_doublereal \*tol, __CLPK_integer \*nsplit, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_doublereal \*w, __CLPK_doublereal \*woff, __CLPK_doublereal \*gersch, __CLPK_doublereal \*work, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int dlarre_ ( char \*range, __CLPK_integer \*n, __CLPK_doublereal \*vl, __CLPK_doublereal \*vu, __CLPK_integer \*il, __CLPK_integer \*iu, __CLPK_doublereal \*d__, __CLPK_doublereal \*e, __CLPK_doublereal \*e2, __CLPK_doublereal \*rtol1, __CLPK_doublereal \*rtol2, __CLPK_doublereal \*spltol, __CLPK_integer \*nsplit, __CLPK_integer \*isplit, __CLPK_integer \*m, __CLPK_doublereal \*w, __CLPK_doublereal \*werr, __CLPK_doublereal \*wgap, __CLPK_integer \*iblock, __CLPK_integer \*indexw, __CLPK_doublereal \*gers, __CLPK_doublereal \*pivmin, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |

Modified zlar1v_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int zlar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_doublereal \*sigma, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_doublereal \*lld, __CLPK_doublereal \*gersch, __CLPK_doublecomplex \*z__, __CLPK_doublereal \*ztz, __CLPK_doublereal \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_doublereal \*work); |
| To | Both | i386,x86_64 | int zlar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_doublereal \*lambda, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_doublereal \*lld, __CLPK_doublereal \*pivmin, __CLPK_doublereal \*gaptol, __CLPK_doublecomplex \*z__, __CLPK_logical \*wantnc, __CLPK_integer \*negcnt, __CLPK_doublereal \*ztz, __CLPK_doublereal \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_doublereal \*nrminv, __CLPK_doublereal \*resid, __CLPK_doublereal \*rqcorr, __CLPK_doublereal \*work); |

Modified dlarrb_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int dlarrb_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_doublereal \*lld, __CLPK_integer \*ifirst, __CLPK_integer \*ilast, __CLPK_doublereal \*sigma, __CLPK_doublereal \*reltol, __CLPK_doublereal \*w, __CLPK_doublereal \*wgap, __CLPK_doublereal \*werr, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int dlarrb_ ( __CLPK_integer \*n, __CLPK_doublereal \*d__, __CLPK_doublereal \*lld, __CLPK_integer \*ifirst, __CLPK_integer \*ilast, __CLPK_doublereal \*rtol1, __CLPK_doublereal \*rtol2, __CLPK_integer \*offset, __CLPK_doublereal \*w, __CLPK_doublereal \*wgap, __CLPK_doublereal \*werr, __CLPK_doublereal \*work, __CLPK_integer \*iwork, __CLPK_doublereal \*pivmin, __CLPK_doublereal \*spdiam, __CLPK_integer \*twist, __CLPK_integer \*info); |

Modified slaqtr_()

|  | Declaration |
| --- | --- |
| From | int slaqtr_ ( __CLPK_logical \*ltran, __CLPK_logical \*lreal, __CLPK_integer \*n, __CLPK_real \*t, __CLPK_integer \*ldt, __CLPK_real \*b, __CLPK_real \*w, __CLPK_real \*scale, __CLPK_real \*x, __CLPK_real \*work, __CLPK_integer \*info); |
| To | int slaqtr_ ( __CLPK_logical \*ltran, __CLPK_logical \*l__CLPK_real, __CLPK_integer \*n, __CLPK_real \*t, __CLPK_integer \*ldt, __CLPK_real \*b, __CLPK_real \*w, __CLPK_real \*scale, __CLPK_real \*x, __CLPK_real \*work, __CLPK_integer \*info); |

Modified dlar1v_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int dlar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_doublereal \*sigma, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_doublereal \*lld, __CLPK_doublereal \*gersch, __CLPK_doublereal \*z__, __CLPK_doublereal \*ztz, __CLPK_doublereal \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_doublereal \*work); |
| To | Both | i386,x86_64 | int dlar1v_ ( __CLPK_integer \*n, __CLPK_integer \*b1, __CLPK_integer \*bn, __CLPK_doublereal \*lambda, __CLPK_doublereal \*d__, __CLPK_doublereal \*l, __CLPK_doublereal \*ld, __CLPK_doublereal \*lld, __CLPK_doublereal \*pivmin, __CLPK_doublereal \*gaptol, __CLPK_doublereal \*z__, __CLPK_logical \*wantnc, __CLPK_integer \*negcnt, __CLPK_doublereal \*ztz, __CLPK_doublereal \*mingma, __CLPK_integer \*r__, __CLPK_integer \*isuppz, __CLPK_doublereal \*nrminv, __CLPK_doublereal \*resid, __CLPK_doublereal \*rqcorr, __CLPK_doublereal \*work); |

Modified slarrf_()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _Unknown_ | Unknown | int slarrf_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_real \*lld, __CLPK_integer \*ifirst, __CLPK_integer \*ilast, __CLPK_real \*w, __CLPK_real \*dplus, __CLPK_real \*lplus, __CLPK_real \*work, __CLPK_integer \*iwork, __CLPK_integer \*info); |
| To | Both | i386,x86_64 | int slarrf_ ( __CLPK_integer \*n, __CLPK_real \*d__, __CLPK_real \*l, __CLPK_real \*ld, __CLPK_integer \*clstrt, __CLPK_integer \*clend, __CLPK_real \*w, __CLPK_real \*wgap, __CLPK_real \*werr, __CLPK_real \*spdiam, __CLPK_real \*clgapl, __CLPK_real \*clgapr, __CLPK_real \*pivmin, __CLPK_real \*sigma, __CLPK_real \*dplus, __CLPK_real \*lplus, __CLPK_real \*work, __CLPK_integer \*info); |

Modified ilaenv_()

|  | Declaration |
| --- | --- |
| From | int ilaenv_ ( __CLPK_integer \*ispec, char \*name__, char \*opts, __CLPK_integer \*n1, __CLPK_integer \*n2, __CLPK_integer \*n3, __CLPK_integer \*n4, __CLPK_ftnlen name_len, __CLPK_ftnlen opts_len); |
| To | __CLPK_integer ilaenv_ ( __CLPK_integer \*ispec, char \*name__, char \*opts, __CLPK_integer \*n1, __CLPK_integer \*n2, __CLPK_integer \*n3, __CLPK_integer \*n4); |

Modified icmax1_()

|  | Declaration |
| --- | --- |
| From | int icmax1_ ( __CLPK_integer \*n, __CLPK_complex \*cx, __CLPK_integer \*incx); |
| To | __CLPK_integer icmax1_ ( __CLPK_integer \*n, __CLPK_complex \*cx, __CLPK_integer \*incx); |

vDSP.hAdded vDSP_DFT_CreateSetup()Added [vDSP_DFT_DestroySetup()](https://developer.apple.com/documentation/accelerate/1450791-vdsp_dft_destroysetup)Added [vDSP_DFT_Direction](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction)Added [vDSP_DFT_Execute()](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute)Added [vDSP_DFT_FORWARD](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction/forward)Added [vDSP_DFT_INVERSE](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction/inverse)Added [vDSP_DFT_Setup](https://developer.apple.com/documentation/accelerate/vdsp_dft_setup)Added vDSP_DFT_zop()Added [vDSP_DFT_zop_CreateSetup()](https://developer.apple.com/documentation/accelerate/1450061-vdsp_dft_zop_createsetup)Added [vDSP_DFT_zrop_CreateSetup()](https://developer.apple.com/documentation/accelerate/1449739-vdsp_dft_zrop_createsetup)Added [vDSP_FFT16_copv()](https://developer.apple.com/documentation/accelerate/1450220-vdsp_fft16_copv)Added [vDSP_FFT16_zopv()](https://developer.apple.com/documentation/accelerate/1450002-vdsp_fft16_zopv)Added [vDSP_FFT32_copv()](https://developer.apple.com/documentation/accelerate/1450426-vdsp_fft32_copv)Added [vDSP_FFT32_zopv()](https://developer.apple.com/documentation/accelerate/1449684-vdsp_fft32_zopv)Added [vDSP_dotpr2()](https://developer.apple.com/documentation/accelerate/1450752-vdsp_dotpr2)Added [vDSP_dotpr2_s1_15()](https://developer.apple.com/documentation/accelerate/1449919-vdsp_dotpr2_s1_15)Added [vDSP_dotpr2_s8_24()](https://developer.apple.com/documentation/accelerate/1449663-vdsp_dotpr2_s8_24)Added [vDSP_dotpr_s1_15()](https://developer.apple.com/documentation/accelerate/1449796-vdsp_dotpr_s1_15)Added [vDSP_dotpr_s8_24()](https://developer.apple.com/documentation/accelerate/1450480-vdsp_dotpr_s8_24)Added [vDSP_vrampmul()](https://developer.apple.com/documentation/accelerate/1450226-vdsp_vrampmul)Added [vDSP_vrampmul2()](https://developer.apple.com/documentation/accelerate/1449695-vdsp_vrampmul2)Added [vDSP_vrampmul2_s1_15()](https://developer.apple.com/documentation/accelerate/1449788-vdsp_vrampmul2_s1_15)Added [vDSP_vrampmul2_s8_24()](https://developer.apple.com/documentation/accelerate/1449936-vdsp_vrampmul2_s8_24)Added [vDSP_vrampmul_s1_15()](https://developer.apple.com/documentation/accelerate/1449877-vdsp_vrampmul_s1_15)Added [vDSP_vrampmul_s8_24()](https://developer.apple.com/documentation/accelerate/1450008-vdsp_vrampmul_s8_24)Added [vDSP_vrampmuladd()](https://developer.apple.com/documentation/accelerate/1450042-vdsp_vrampmuladd)Added [vDSP_vrampmuladd2()](https://developer.apple.com/documentation/accelerate/1450406-vdsp_vrampmuladd2)Added [vDSP_vrampmuladd2_s1_15()](https://developer.apple.com/documentation/accelerate/1450845-vdsp_vrampmuladd2_s1_15)Added [vDSP_vrampmuladd2_s8_24()](https://developer.apple.com/documentation/accelerate/1450046-vdsp_vrampmuladd2_s8_24)Added [vDSP_vrampmuladd_s1_15()](https://developer.apple.com/documentation/accelerate/1450758-vdsp_vrampmuladd_s1_15)Added [vDSP_vrampmuladd_s8_24()](https://developer.apple.com/documentation/accelerate/1450347-vdsp_vrampmuladd_s8_24)Modified [vDSP_zvcmulD()](https://developer.apple.com/documentation/accelerate/1449764-vdsp_zvcmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmulD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvcmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmul()](https://developer.apple.com/documentation/accelerate/1450717-vdsp_zvcmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmul ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvcmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified zvmulD()

|  | Declaration |
| --- | --- |
| From | void zvmulD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void zvmulD ( const DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |

Modified [vDSP_zvmulD()](https://developer.apple.com/documentation/accelerate/1450390-vdsp_zvmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmulD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void vDSP_zvmulD ( const DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |

vForce.hAdded [vvcopysign()](https://developer.apple.com/documentation/accelerate/1470348-vvcopysign)Added [vvcospi()](https://developer.apple.com/documentation/accelerate/1470391-vvcospi)Added [vvcospif()](https://developer.apple.com/documentation/accelerate/1470479-vvcospif)Added [vvexp2()](https://developer.apple.com/documentation/accelerate/1470358-vvexp2)Added [vvexp2f()](https://developer.apple.com/documentation/accelerate/1470512-vvexp2f)Added [vvexpm1()](https://developer.apple.com/documentation/accelerate/1470389-vvexpm1)Added [vvfabs()](https://developer.apple.com/documentation/accelerate/1470370-vvfabs)Added [vvfabsf()](https://developer.apple.com/documentation/accelerate/1470393-vvfabsf)Added [vvfmod()](https://developer.apple.com/documentation/accelerate/1470379-vvfmod)Added [vvlog1p()](https://developer.apple.com/documentation/accelerate/1470377-vvlog1p)Added [vvlog2()](https://developer.apple.com/documentation/accelerate/1470420-vvlog2)Added [vvlog2f()](https://developer.apple.com/documentation/accelerate/1470416-vvlog2f)Added [vvlogb()](https://developer.apple.com/documentation/accelerate/1470432-vvlogb)Added [vvnextafter()](https://developer.apple.com/documentation/accelerate/1470487-vvnextafter)Added [vvremainder()](https://developer.apple.com/documentation/accelerate/1470456-vvremainder)Added [vvsinpi()](https://developer.apple.com/documentation/accelerate/1470440-vvsinpi)Added [vvsinpif()](https://developer.apple.com/documentation/accelerate/1470414-vvsinpif)Added [vvtanpi()](https://developer.apple.com/documentation/accelerate/1470404-vvtanpi)Added [vvtanpif()](https://developer.apple.com/documentation/accelerate/1470469-vvtanpif)Modified vvfabf()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
