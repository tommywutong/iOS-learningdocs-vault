---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Accelerate.html
archived_at: '2026-07-18T02:56:04.552684Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Accelerate Changes

## Accelerate

Modified SetBLASParamErrorProc(BLASParamErrorProc)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_caxpby(Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_cset(Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_daxpby(Int32, Double, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_dset(Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_saxpby(Int32, Float, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_sset(Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_zaxpby(Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified catlas_zset(Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cbdsqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_caxpy(Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ccopy(Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cdotc_sub(Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cdotu_sub(Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, Int32, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cgerc(CBLAS_ORDER, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cgeru(CBLAS_ORDER, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_chbmv(CBLAS_ORDER, CBLAS_UPLO, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_chemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_chemv(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cher(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cher2(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cher2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, Float, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cherk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, Float, UnsafePointer<Void>, Int32, Float, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_chpmv(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_chpr(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_chpr2(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_crotg(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cscal(Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_csrot(Int32, UnsafeMutablePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32, Float, Float)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_csscal(Int32, Float, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_cswap(Int32, UnsafeMutablePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_csymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_csyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_csyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctrmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctrmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctrsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ctrsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dasum(Int32, UnsafePointer<Double>, Int32) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_daxpy(Int32, Double, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dcopy(Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ddot(Int32, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, Int32, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dger(CBLAS_ORDER, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dnrm2(Int32, UnsafePointer<Double>, Int32) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_drot(Int32, UnsafeMutablePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32, Double, Double)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_drotg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_drotm(Int32, UnsafeMutablePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32, UnsafePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_drotmg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, Double, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsbmv(CBLAS_ORDER, CBLAS_UPLO, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dscal(Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsdot(Int32, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dspmv(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Double>, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dspr(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dspr2(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dswap(Int32, UnsafeMutablePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsymv(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsyr(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsyr2(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dsyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, Double, UnsafePointer<Double>, Int32, Double, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Double>, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Double>, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtrmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtrmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtrsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, Double, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dtrsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Double>, Int32, UnsafeMutablePointer<Double>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dzasum(Int32, UnsafePointer<Void>, Int32) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_dznrm2(Int32, UnsafePointer<Void>, Int32) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_icamax(Int32, UnsafePointer<Void>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_idamax(Int32, UnsafePointer<Double>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_isamax(Int32, UnsafePointer<Float>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_izamax(Int32, UnsafePointer<Void>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sasum(Int32, UnsafePointer<Float>, Int32) -> Float

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_saxpy(Int32, Float, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_scasum(Int32, UnsafePointer<Void>, Int32) -> Float

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_scnrm2(Int32, UnsafePointer<Void>, Int32) -> Float

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_scopy(Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sdot(Int32, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32) -> Float

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sdsdot(Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32) -> Float

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, Int32, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sger(CBLAS_ORDER, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_snrm2(Int32, UnsafePointer<Float>, Int32) -> Float

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_srot(Int32, UnsafeMutablePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32, Float, Float)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_srotg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_srotm(Int32, UnsafeMutablePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32, UnsafePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_srotmg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, Float, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssbmv(CBLAS_ORDER, CBLAS_UPLO, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sscal(Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sspmv(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Float>, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sspr(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sspr2(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_sswap(Int32, UnsafeMutablePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssymv(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssyr(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssyr2(CBLAS_ORDER, CBLAS_UPLO, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ssyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, Float, UnsafePointer<Float>, Int32, Float, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_stbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_stbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_stpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Float>, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_stpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Float>, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_strmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_strmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_strsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, Float, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_strsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Float>, Int32, UnsafeMutablePointer<Float>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zaxpy(Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zcopy(Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zdotc_sub(Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zdotu_sub(Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zdrot(Int32, UnsafeMutablePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32, Double, Double)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zdscal(Int32, Double, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, Int32, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zgerc(CBLAS_ORDER, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zgeru(CBLAS_ORDER, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zhbmv(CBLAS_ORDER, CBLAS_UPLO, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zhemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zhemv(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zher(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zher2(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zher2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, Double, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zherk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, Double, UnsafePointer<Void>, Int32, Double, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zhpmv(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zhpr(CBLAS_ORDER, CBLAS_UPLO, Int32, Double, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zhpr2(CBLAS_ORDER, CBLAS_UPLO, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zrotg(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zscal(Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zswap(Int32, UnsafeMutablePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zsymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zsyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_zsyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztrmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztrmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztrsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, Int32, UnsafePointer<Void>, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cblas_ztrsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, Int32, UnsafePointer<Void>, Int32, UnsafeMutablePointer<Void>, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbbrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbtf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbtrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgebak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgebal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgebd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgebrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgecon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgees_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgegs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgegv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgehd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgehrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgelq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgelqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgels_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgelsd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgelss_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgelsx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgelsy_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeql2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeqlf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeqp3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeqpf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeqr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgeqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgerfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgerq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgerqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgesc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgesdd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgesv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgesvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgesvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgetc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgetf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgetrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgetri_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgetrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggbak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggbal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgges_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggglm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgghrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgglse_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggsvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cggsvp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgtcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgtrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgtsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgtsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgttrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cgtts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbgst_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbgv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbgvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbgvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chbtrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified checon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cheequb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cheev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cheevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cheevr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cheevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chegs2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chegst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chegv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chegvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chegvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cherfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chesv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chesvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chetd2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chetf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chetrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chetrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chetri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chetrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chfrk_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chgeqz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chla_transtype__(UnsafeMutablePointer<Int8>, __CLPK_ftnlen, UnsafeMutablePointer<__CLPK_integer>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpgst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpgv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpgvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpgvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chpsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chptrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chsein_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified chseqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clabrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacgv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacn2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacp2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacpy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacrm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clacrt_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cladiv_(UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claed0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claed7_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claed8_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claein_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claesy_(UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claev2_(UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clag2z_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clags2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clagtm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clahef_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clahqr_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clahr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clahrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claic1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clals0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clalsa_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clalsd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clangb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clange_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clangt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clanhb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clanhe_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clanhf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clanhp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clanhs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clanht_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clansb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clansp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clansy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clantb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clantp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clantr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clapll_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clapmt_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqgb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqge_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqhb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqhe_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqhp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqp2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqps_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqr0_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqr1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqr2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqr3_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqr4_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqr5_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqsb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqsp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claqsy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clar1v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clar2v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarcm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarfb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarfg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarfp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarft_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarfx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clargv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarnv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarrv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarscl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clartg_(UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clartv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarzb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clarzt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clascl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clascl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claset_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clasr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified classq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified claswp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clasyf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatbs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatdf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatps_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatrz_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clatzm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clauu2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified clauum_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbstf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbtf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbtrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpftrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpftrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpocon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpoequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpoequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cporfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cposv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cposvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpotf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpotrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpotri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpotrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cppcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cppequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cppsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cppsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpstf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpstrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cptcon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cptrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cptsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cptsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cpttrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cptts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified crot_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cspcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cspmv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cspr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cspsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cspsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csrscl_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cstedc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cstegr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cstein_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cstemr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csycon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csyequb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csymv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csyr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csyrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csysv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csysvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csytf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csytrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csytri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified csytrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctfsm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctfttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctfttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgex2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgexc_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgsen_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgsja_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgsy2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctgsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctpcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctpttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctpttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrexc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrsen_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrti2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrtri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctrttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctzrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ctzrzf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cung2l_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cung2r_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunghr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunglq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungql_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungqr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungrq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cungtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunm2l_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunm2r_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmhr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunml2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmlq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmql_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmr2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmr3_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmrq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmrz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cunmtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cupgtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified cupmtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dbdsdc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dbdsqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ddisna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbbrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbtf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbtrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgebak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgebal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgebd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgebrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgecon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgees_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgegs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgegv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgehd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgehrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgejsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgelq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgelqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgels_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgelsd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgelss_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgelsx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgelsy_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeql2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeqlf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeqp3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeqpf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeqr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgeqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgerfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgerq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgerqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgesc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgesdd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgesv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgesvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgesvj_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgesvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgetc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgetf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgetrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgetri_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgetrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggbak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggbal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgges_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggglm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgghrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgglse_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggsvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dggsvp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgsvj0_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgsvj1_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgtcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgtrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgtsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgtsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgttrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dgtts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dhgeqz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dhsein_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dhseqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified disnan_(UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_logical

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlabad_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlabrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlacn2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlacon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlacpy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dladiv_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlae2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaebz_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed6_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed7_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed8_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaed9_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaeda_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaein_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaev2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaexc_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlag2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlag2s_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlags2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlagtf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlagtm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlagts_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlagv2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlahqr_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlahr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlahrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaic1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaisnan_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_logical

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaln2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlals0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlalsa_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlalsd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamc1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamc3_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamc4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamc5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamch_(UnsafeMutablePointer<Int8>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlamrg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaneg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlangb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlange_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlangt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlanhs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlansb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlansf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlansp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlanst_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlansy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlantb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlantp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlantr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlanv2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlapll_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlapmt_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlapy2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlapy3_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqgb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqge_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqp2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqps_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqr0_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqr1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqr2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqr3_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqr4_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqr5_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqsb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqsp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqsy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaqtr_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlar1v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlar2v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarfb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarfg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarfp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarft_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarfx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlargv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarnv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarra_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarre_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrj_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrk_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarrv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarscl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlartg_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlartv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaruv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarzb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlarzt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlas2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlascl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlascl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd6_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd7_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasd8_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasda_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasdq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasdt_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaset_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasq1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasq3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasq4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasq5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_logical>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasq6_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasrt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlassq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasv2_(UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlaswp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasy2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlasyf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlat2s_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatbs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatdf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatps_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatrz_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlatzm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlauu2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dlauum_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dopgtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dopmtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorg2l_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorg2r_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorghr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorglq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgql_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgqr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgrq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorgtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorm2l_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorm2r_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormhr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dorml2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormlq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormql_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormr2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormr3_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormrq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormrz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dormtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbstf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbtf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbtrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpftrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpftrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpocon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpoequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpoequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dporfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dposv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dposvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpotf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpotrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpotri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpotrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dppcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dppequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dppsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dppsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpstf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpstrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dptcon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dptrfs_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dptsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dptsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dpttrs_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dptts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified drscl_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbgst_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbgv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbgvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbgvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsbtrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsfrk_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsgesv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspgst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspgv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspgvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspgvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsposv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dspsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsptrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstebz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstedc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstegr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstein_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstemr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsterf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstevr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dstevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsycon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsyequb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsyev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsyevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsyevr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsyevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsygs2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsygst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsygv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsygvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsygvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsyrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsysv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsysvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsytd2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsytf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsytrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsytrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsytri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dsytrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtfsm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtfttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtfttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgex2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgexc_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgsen_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgsja_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgsy2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtgsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtpcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtpttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtpttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrexc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrsen_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrti2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrtri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtrttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtzrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dtzrzf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dzsum1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified icmax1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ieeeck_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaclc_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaclr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified iladiag_(UnsafeMutablePointer<Int8>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified iladlc_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified iladlr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaenv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaprec_(UnsafeMutablePointer<Int8>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaslc_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaslr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilatrans_(UnsafeMutablePointer<Int8>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilauplo_(UnsafeMutablePointer<Int8>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilaver_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilazlc_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ilazlr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified iparmq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified izmax1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kvImageBackgroundColorFill

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageCopyInPlace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageDoNotTile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageEdgeExtend

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageGetTempBufferSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageHighQualityResampling

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageLeaveAlphaUnchanged

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kvImageNoAllocate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kvImagePrintDiagnosticsToConsole

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kvImageTruncateKernel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified lsamen_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>) -> __CLPK_logical

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sbdsdc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sbdsqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified scsum1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sdisna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbbrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbtf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbtrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgebak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgebal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgebd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgebrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgecon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgees_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgegs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgegv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgehd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgehrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgejsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgelq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgelqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgels_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgelsd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgelss_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgelsx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgelsy_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeql2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeqlf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeqp3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeqpf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeqr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgeqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgerfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgerq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgerqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgesc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgesdd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgesv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgesvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgesvj_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgesvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgetc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgetf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgetrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgetri_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgetrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggbak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggbal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgges_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggglm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgghrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgglse_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggsvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sggsvp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgsvj0_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgsvj1_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgtcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgtrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgtsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgtsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgttrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sgtts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified shgeqz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified shsein_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified shseqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sisnan_(UnsafeMutablePointer<__CLPK_real>) -> __CLPK_logical

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slabad_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slabrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slacn2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slacon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slacpy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sladiv_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slae2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaebz_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed6_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed7_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed8_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaed9_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaeda_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaein_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaev2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaexc_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slag2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slag2d_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slags2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slagtf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slagtm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slagts_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slagv2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slahqr_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slahr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slahrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaic1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaisnan_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_logical

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaln2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slals0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slalsa_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slalsd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamc1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamc3_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamc4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamc5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamch_(UnsafeMutablePointer<Int8>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slamrg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaneg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slangb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slange_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slangt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slanhs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slansb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slansf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slansp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slanst_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slansy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slantb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slantp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slantr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slanv2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slapll_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slapmt_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slapy2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slapy3_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqgb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqge_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqp2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqps_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqr0_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqr1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqr2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqr3_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqr4_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqr5_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqsb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqsp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqsy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaqtr_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slar1v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slar2v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarfb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarfg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarfp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarft_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarfx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slargv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarnv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarra_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarre_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrj_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrk_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarrv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarscl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slartg_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slartv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaruv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarzb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slarzt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slas2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slascl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slascl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd6_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd7_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasd8_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasda_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasdq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasdt_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaset_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasq1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasq3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasq4_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasq5_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_logical>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasq6_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasrt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slassq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasv2_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slaswp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasy2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slasyf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatbs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatdf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatps_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatrz_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slatzm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slauu2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified slauum_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified smaxloc_(UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> __CLPK_integer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sopgtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sopmtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorg2l_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorg2r_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorghr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorglq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgql_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgqr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgrq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorgtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorm2l_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorm2r_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormhr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sorml2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormlq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormql_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormr2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormr3_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormrq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormrz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sormtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbstf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbtf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbtrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spftrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spftrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spocon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spoequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spoequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sporfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sposv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sposvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spotf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spotrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spotri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spotrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sppcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sppequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sppsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sppsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spstf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spstrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sptcon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sptrfs_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sptsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sptsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified spttrs_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sptts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified srscl_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbgst_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbgv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbgvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbgvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssbtrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssfrk_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspgst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspgv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspgvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspgvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sspsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssptrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstebz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstedc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstegr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstein_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstemr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssterf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstevr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified sstevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssycon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssyequb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssyev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssyevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssyevr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssyevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssygs2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssygst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssygv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssygvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssygvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssyrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssysv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssysvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssytd2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssytf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssytrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssytrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssytri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ssytrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stfsm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stfttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stfttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgex2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgexc_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgsen_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgsja_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgsy2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stgsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stpcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stpttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stpttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strexc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strsen_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strti2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strtri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified strttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stzrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified stzrzf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_real>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DCT_CreateSetup(vDSP_DFT_Setup, vDSP_Length, vDSP_DCT_Type) -> vDSP_DFT_Setup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_DCT_Execute(COpaquePointer, UnsafePointer<Float>, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_DFT_CreateSetup(vDSP_DFT_Setup, vDSP_Length) -> vDSP_DFT_Setup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DFT_DestroySetup(vDSP_DFT_Setup)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DFT_DestroySetupD(vDSP_DFT_SetupD)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_DFT_Execute(COpaquePointer, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DFT_ExecuteD(COpaquePointer, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_DFT_zop(COpaquePointer, UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_DFT_Direction)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DFT_zop_CreateSetup(vDSP_DFT_Setup, vDSP_Length, vDSP_DFT_Direction) -> vDSP_DFT_Setup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DFT_zop_CreateSetupD(vDSP_DFT_SetupD, vDSP_Length, vDSP_DFT_Direction) -> vDSP_DFT_SetupD

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_DFT_zrop_CreateSetup(vDSP_DFT_Setup, vDSP_Length, vDSP_DFT_Direction) -> vDSP_DFT_Setup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_DFT_zrop_CreateSetupD(vDSP_DFT_SetupD, vDSP_Length, vDSP_DFT_Direction) -> vDSP_DFT_SetupD

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_FFT16_copv(UnsafeMutablePointer<Float>, UnsafePointer<Float>, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_FFT16_zopv(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_FFT32_copv(UnsafeMutablePointer<Float>, UnsafePointer<Float>, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_FFT32_zopv(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_biquad(COpaquePointer, UnsafeMutablePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_biquadD(COpaquePointer, UnsafeMutablePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_biquad_CreateSetup(UnsafePointer<Double>, vDSP_Length) -> vDSP_biquad_Setup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_biquad_CreateSetupD(UnsafePointer<Double>, vDSP_Length) -> vDSP_biquad_SetupD

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_biquad_DestroySetup(vDSP_biquad_Setup)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_biquad_DestroySetupD(vDSP_biquad_SetupD)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_biquadm(vDSP_biquadm_Setup, UnsafeMutablePointer<UnsafePointer<Float>>, vDSP_Stride, UnsafeMutablePointer<UnsafeMutablePointer<Float>>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_biquadm_CopyState(vDSP_biquadm_Setup, COpaquePointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_biquadm_CreateSetup(UnsafePointer<Double>, vDSP_Length, vDSP_Length) -> vDSP_biquadm_Setup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_biquadm_DestroySetup(vDSP_biquadm_Setup)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_biquadm_ResetState(vDSP_biquadm_Setup)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_blkman_window(UnsafeMutablePointer<Float>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_blkman_windowD(UnsafeMutablePointer<Double>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_conv(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_convD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_create_fftsetup(vDSP_Length, FFTRadix) -> FFTSetup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_create_fftsetupD(vDSP_Length, FFTRadix) -> FFTSetupD

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_ctoz(UnsafePointer<DSPComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_ctozD(UnsafePointer<DSPDoubleComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_deq22(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_deq22D(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_desamp(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_desampD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_destroy_fftsetup(FFTSetup)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_destroy_fftsetupD(FFTSetupD)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_distancesq(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vDSP_dotpr(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_dotpr2(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_dotpr2_s1_15(UnsafePointer<Int16>, vDSP_Stride, UnsafePointer<Int16>, vDSP_Stride, UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Int16>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_dotpr2_s8_24(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_dotprD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_dotpr_s1_15(UnsafePointer<Int16>, vDSP_Stride, UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Int16>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_dotpr_s8_24(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_f3x3(UnsafePointer<Float>, vDSP_Length, vDSP_Length, UnsafePointer<Float>, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_f3x3D(UnsafePointer<Double>, vDSP_Length, vDSP_Length, UnsafePointer<Double>, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_f5x5(UnsafePointer<Float>, vDSP_Length, vDSP_Length, UnsafePointer<Float>, UnsafeMutablePointer<Float>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_f5x5D(UnsafePointer<Double>, vDSP_Length, vDSP_Length, UnsafePointer<Double>, UnsafeMutablePointer<Double>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zip(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zipD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zipt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_ziptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zopD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zopt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zoptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zrip(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zripD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zript(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zriptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zrop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zropD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zropt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft2d_zroptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft3_zop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft3_zopD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft5_zop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft5_zopD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zip(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zipD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zipt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_ziptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zopD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zopt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zoptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zrip(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zripD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zript(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zriptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zrop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zropD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zropt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fft_zroptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zip(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zipD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zipt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_ziptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zopD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zopt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zoptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zrip(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zripD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zript(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zriptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zrop(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zropD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zropt(FFTSetup, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_fftm_zroptD(FFTSetupD, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length, FFTDirection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_hamm_window(UnsafeMutablePointer<Float>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_hamm_windowD(UnsafeMutablePointer<Double>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_hann_window(UnsafeMutablePointer<Float>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_hann_windowD(UnsafeMutablePointer<Double>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_imgfir(UnsafePointer<Float>, vDSP_Length, vDSP_Length, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_imgfirD(UnsafePointer<Double>, vDSP_Length, vDSP_Length, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxmgv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxmgvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxmgvi(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxmgviD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxvi(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_maxviD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_meamgv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_meamgvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_meanv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_meanvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_measqv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_measqvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minmgv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minmgvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minmgvi(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minmgviD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minvi(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_minviD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mmov(UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Length, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mmovD(UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Length, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mmul(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mmulD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mtrans(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mtransD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mvessq(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_mvessqD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_normalize(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_normalizeD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_nzcros(UnsafePointer<Float>, vDSP_Stride, vDSP_Length, UnsafeMutablePointer<vDSP_Length>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_nzcrosD(UnsafePointer<Double>, vDSP_Stride, vDSP_Length, UnsafeMutablePointer<vDSP_Length>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_polar(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_polarD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_rect(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_rectD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_rmsqv(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_rmsqvD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svdiv(UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svdivD(UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_sve(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_sveD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_sve_svesq(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_sve_svesqD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_svemg(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svemgD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svesq(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svesqD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svs(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_svsD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vaam(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vaamD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vabs(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vabsD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vabsi(UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vadd(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vaddD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vaddi(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vam(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vamD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vasbm(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vasbmD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vasm(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vasmD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vavlin(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vavlinD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vclip(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vclipD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vclipc(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, UnsafeMutablePointer<vDSP_Length>, UnsafeMutablePointer<vDSP_Length>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vclipcD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, UnsafeMutablePointer<vDSP_Length>, UnsafeMutablePointer<vDSP_Length>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vclr(UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vclrD(UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vcmprs(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vcmprsD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdbcon(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, UInt32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdbconD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, UInt32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdist(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdistD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdiv(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdivD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdivi(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vdpsp(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_venvlp(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_venvlpD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_veqvi(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfill(UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfillD(UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfilli(UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfix16(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfix16D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfix32(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfix32D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfix8(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Int8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfix8D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Int8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixr16(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixr16D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixr32(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixr32D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixr8(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Int8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixr8D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Int8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixru16(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<UInt16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixru16D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<UInt16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixru32(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<UInt32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixru32D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<UInt32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixru8(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<UInt8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixru8D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<UInt8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixu16(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<UInt16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixu16D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<UInt16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixu32(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<UInt32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixu32D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<UInt32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixu8(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<UInt8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfixu8D(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<UInt8>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vflt16(UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vflt16D(UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vflt24(UnsafePointer<vDSP_int24>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vflt32(UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vflt32D(UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vflt8(UnsafePointer<Int8>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vflt8D(UnsafePointer<Int8>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfltsm24(UnsafePointer<vDSP_int24>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vfltsmu24(UnsafePointer<vDSP_uint24>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vfltu16(UnsafePointer<UInt16>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfltu16D(UnsafePointer<UInt16>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfltu24(UnsafePointer<vDSP_uint24>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vfltu32(UnsafePointer<UInt32>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfltu32D(UnsafePointer<UInt32>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfltu8(UnsafePointer<UInt8>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfltu8D(UnsafePointer<UInt8>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfrac(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vfracD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgathr(UnsafePointer<Float>, UnsafePointer<vDSP_Length>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgathrD(UnsafePointer<Double>, UnsafePointer<vDSP_Length>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgathra(UnsafeMutablePointer<UnsafePointer<Float>>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgathraD(UnsafeMutablePointer<UnsafePointer<Double>>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgen(UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgenD(UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgenp(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vgenpD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_viclip(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_viclipD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vindex(UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vindexD(UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vintb(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vintbD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vlim(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vlimD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vlint(UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vlintD(UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vma(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmaD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmax(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmaxD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmaxmg(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmaxmgD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmin(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vminD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vminmg(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vminmgD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmma(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmmaD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmmsb(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmmsbD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmsa(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmsaD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmsb(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmsbD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmul(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vmulD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vnabs(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vnabsD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vneg(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vnegD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vpoly(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vpolyD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vpythg(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vpythgD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vqint(UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vqintD(UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vramp(UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampD(UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmul(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmul2(UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmul2_s1_15(UnsafePointer<Int16>, UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Int16>, UnsafePointer<Int16>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmul2_s8_24(UnsafePointer<Int32>, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmul_s1_15(UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Int16>, UnsafePointer<Int16>, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmul_s8_24(UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmuladd(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmuladd2(UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmuladd2_s1_15(UnsafePointer<Int16>, UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Int16>, UnsafePointer<Int16>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmuladd2_s8_24(UnsafePointer<Int32>, UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmuladd_s1_15(UnsafePointer<Int16>, vDSP_Stride, UnsafeMutablePointer<Int16>, UnsafePointer<Int16>, UnsafeMutablePointer<Int16>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrampmuladd_s8_24(UnsafePointer<Int32>, vDSP_Stride, UnsafeMutablePointer<Int32>, UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrsum(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrsumD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrvrs(UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vrvrsD(UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsadd(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsaddD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsaddi(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsbm(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsbmD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsbsbm(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsbsbmD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsbsm(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsbsmD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsdiv(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsdivD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsdivi(UnsafePointer<Int32>, vDSP_Stride, UnsafePointer<Int32>, UnsafeMutablePointer<Int32>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsimps(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsimpsD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsma(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmaD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmfix24(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<vDSP_int24>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vsmfixu24(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<vDSP_uint24>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_vsmsa(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmsaD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmsb(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmsbD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmsma(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vDSP_vsmul(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsmulD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsort(UnsafeMutablePointer<Float>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsortD(UnsafeMutablePointer<Double>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsorti(UnsafePointer<Float>, UnsafeMutablePointer<vDSP_Length>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsortiD(UnsafePointer<Double>, UnsafeMutablePointer<vDSP_Length>, UnsafeMutablePointer<vDSP_Length>, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vspdp(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsq(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsqD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vssq(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vssqD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsub(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vsubD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vswap(UnsafeMutablePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vswapD(UnsafeMutablePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vswsum(UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vswsumD(UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vtabi(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, vDSP_Length, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vtabiD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, vDSP_Length, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vthr(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vthrD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vthres(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vthresD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vthrsc(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vthrscD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vtmerg(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vtmergD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vtrapz(UnsafePointer<Float>, vDSP_Stride, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_vtrapzD(UnsafePointer<Double>, vDSP_Stride, UnsafePointer<Double>, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_wiener(vDSP_Length, UnsafePointer<Float>, UnsafePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, Int32, UnsafeMutablePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_wienerD(vDSP_Length, UnsafePointer<Double>, UnsafePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, Int32, UnsafeMutablePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zaspec(UnsafePointer<DSPSplitComplex>, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zaspecD(UnsafePointer<DSPDoubleSplitComplex>, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zcoher(UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<DSPSplitComplex>, UnsafeMutablePointer<Float>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zcoherD(UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<DSPDoubleSplitComplex>, UnsafeMutablePointer<Double>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zconv(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zconvD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zcspec(UnsafePointer<DSPSplitComplex>, UnsafePointer<DSPSplitComplex>, UnsafePointer<DSPSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zcspecD(UnsafePointer<DSPDoubleSplitComplex>, UnsafePointer<DSPDoubleSplitComplex>, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zdotpr(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zdotprD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zidotpr(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zidotprD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmma(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmmaD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmms(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmmsD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmmul(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmmulD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmsm(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zmsmD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrdesamp(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, UnsafePointer<DSPSplitComplex>, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrdesampD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrdotpr(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrdotprD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvadd(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvaddD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvdiv(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvdivD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvmul(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvmulD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvsub(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zrvsubD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_ztoc(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafeMutablePointer<DSPComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_ztocD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafeMutablePointer<DSPDoubleComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_ztrans(UnsafePointer<Float>, UnsafePointer<DSPSplitComplex>, UnsafePointer<DSPSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_ztransD(UnsafePointer<Double>, UnsafePointer<DSPDoubleSplitComplex>, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvabs(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvabsD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvadd(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvaddD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvcma(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvcmaD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvcmul(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvcmulD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvconj(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvconjD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvdiv(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvdivD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvfill(UnsafePointer<DSPSplitComplex>, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvfillD(UnsafePointer<DSPDoubleSplitComplex>, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvma(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_zvmags(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmagsD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmgsa(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<Float>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmgsaD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<Double>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmmaa(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vDSP_zvmov(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmovD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmul(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvmulD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvneg(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvnegD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvphas(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafeMutablePointer<Float>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvphasD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafeMutablePointer<Double>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvsma(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvsmaD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvsub(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvsubD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvzsml(UnsafePointer<DSPSplitComplex>, vDSP_Stride, UnsafePointer<DSPSplitComplex>, UnsafePointer<DSPSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vDSP_zvzsmlD(UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, UnsafePointer<DSPDoubleSplitComplex>, UnsafePointer<DSPDoubleSplitComplex>, vDSP_Stride, vDSP_Length)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified vImageAffineWarpCG_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_CGAffineTransform>, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageAffineWarpCG_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_CGAffineTransform>, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageAffineWarpCG_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_CGAffineTransform>, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpCG_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_CGAffineTransform>, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpCG_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_CGAffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpCG_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_CGAffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform_Double>, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageAffineWarpD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform_Double>, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageAffineWarpD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform_Double>, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform_Double>, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform_Double>, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarpD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform_Double>, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageAffineWarp_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform>, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageAffineWarp_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform>, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageAffineWarp_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform>, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAffineWarp_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform>, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAffineWarp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAffineWarp_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImage_AffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_NonpremultipliedToPremultiplied_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_NonpremultipliedToPremultiplied_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageBoxConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UInt32, UInt32, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageBoxConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UInt32, UInt32, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageBufferFill_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageBufferFill_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageBufferFill_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageBufferFill_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageBuffer_GetSize(UnsafePointer<vImage_Buffer>) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageBuffer_Init(UnsafeMutablePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageBuffer_InitWithCGImage(UnsafeMutablePointer<vImage_Buffer>, UnsafeMutablePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>, CGImage!, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageByteSwap_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageCGImageFormat_GetComponentCount(UnsafePointer<vImage_CGImageFormat>) -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageCGImageFormat_IsEqual(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageClipToAlpha_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageClipToAlpha_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageClipToAlpha_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageClipToAlpha_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageClipToAlpha_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageClipToAlpha_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageClip_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageContrastStretch_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageContrastStretch_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageContrastStretch_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_16Fto16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_16Q12to16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_16Q12to8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_16Q12toF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_16SToF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_16UToF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_16UToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_16Uto16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_16Uto16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_8to16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB1555toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGB1555toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGB16UToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB16UtoPlanar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB8888ToARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB8888ToRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB8888toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGB8888toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB8888toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGB8888toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGB8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGB8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGBFFFFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ARGBFFFFtoPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ARGBFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_AnyToAny(vImageConverter!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_BGRA16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_BGRA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_BGRA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageConvert_BGRAFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_BGRX8888ToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_BGRXFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_ChunkyToPlanar8(UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, UInt, vImagePixelCount, vImagePixelCount, UInt, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_ChunkyToPlanarF(UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, UInt, vImagePixelCount, vImagePixelCount, UInt, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_FTo16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_FTo16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Fto16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Indexed1toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Indexed2toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Indexed4toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar16FtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar16FtoPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar16Q12toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar16Q12toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar16UtoARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar1toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar2toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar4toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8To16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8ToARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8ToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8ToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8ToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8ToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8toIndexed1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toIndexed2(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toIndexed4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toPlanar1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Int32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toPlanar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toPlanar2(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Int32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toPlanar4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Int32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_Planar8toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFtoARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFtoPlanar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarToChunky8(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32, UInt, vImagePixelCount, vImagePixelCount, UInt, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_PlanarToChunkyF(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32, UInt, vImagePixelCount, vImagePixelCount, UInt, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_RGB16UToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB16UtoARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB16UtoBGRA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB16UtoPlanar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB16UtoRGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB565toARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_RGB565toBGRA8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB565toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_RGB565toRGBA8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB888toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_RGB888toBGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageConvert_RGB888toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGB888toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_RGB888toRGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageConvert_RGBA16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGBA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGBA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageConvert_RGBAFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGBFFFtoARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGBFFFtoBGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_RGBFFFtoPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvert_RGBFFFtoRGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_XRGB8888ToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvert_XRGBFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConverter_CreateWithColorSyncCodeFragment(AnyObject!, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConverter_MustOperateOutOfPlace(vImageConverter!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageConvolveMultiKernel_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UnsafePointer<Int16>>, UInt32, UInt32, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolveMultiKernel_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UnsafePointer<Float>>, UInt32, UInt32, UnsafePointer<Float>, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolveWithBias_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>, UInt32, UInt32, Int32, Int32, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolveWithBias_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, UInt32, UInt32, Float, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolveWithBias_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>, UInt32, UInt32, Int32, Int32, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolveWithBias_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, UInt32, UInt32, Float, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>, UInt32, UInt32, Int32, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolve_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, UInt32, UInt32, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>, UInt32, UInt32, Int32, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageConvolve_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, UInt32, UInt32, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageCreateCGImageFromBuffer(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_CGImageFormat>, CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageCreateGammaFunction(Float, Int32, vImage_Flags) -> GammaFunction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageDestroyGammaFunction(GammaFunction)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageDestroyResamplingFilter(ResamplingFilter)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageDilate_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageDilate_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageDilate_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageDilate_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEndsInContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEndsInContrastStretch_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEndsInContrastStretch_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt32, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEndsInContrastStretch_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEqualization_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEqualization_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEqualization_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageEqualization_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageErode_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageErode_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageErode_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageErode_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageFlatten_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_ARGB8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageFlatten_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_ARGBFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageFlatten_BGRA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageFlatten_BGRAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageFlatten_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_RGBA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageFlatten_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageFlatten_RGBAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageGamma_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageGetResamplingFilterExtent(ResamplingFilter, vImage_Flags) -> vImagePixelCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageGetResamplingFilterSize(Float, CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, Float, vImage_Flags) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramCalculation_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramCalculation_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramCalculation_Planar8(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramCalculation_PlanarF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramSpecification_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramSpecification_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramSpecification_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHistogramSpecification_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, UnsafePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalReflect_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageHorizontalReflect_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageHorizontalReflect_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalReflect_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalReflect_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageHorizontalReflect_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalReflect_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageHorizontalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageHorizontalShearD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageHorizontalShearD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageHorizontalShearD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageHorizontalShearD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageHorizontalShear_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageHorizontalShear_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageHorizontalShear_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalShear_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalShear_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageHorizontalShear_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageInterpolatedLookupTable_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, vImagePixelCount, Float, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageLookupTable_8to64U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt64>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageLookupTable_Planar8toPlanar16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageLookupTable_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageLookupTable_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMatrixMultiply_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>, UnsafePointer<Int32>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMatrixMultiply_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMatrixMultiply_Planar16S(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, UInt32, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>, UnsafePointer<Int32>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageMatrixMultiply_Planar8(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, UInt32, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>, UnsafePointer<Int32>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMatrixMultiply_PlanarF(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, UInt32, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMax_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMax_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMax_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMax_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMin_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMin_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMin_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMin_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageMultiDimensionalInterpolatedLookupTable_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageMultidimensionalTable_Create(UnsafePointer<UInt16>, UInt32, UInt32, UnsafeMutablePointer<UInt8>, vImageMDTableUsageHint, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> vImage_MultidimensionalTable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageMultidimensionalTable_Release(vImage_MultidimensionalTable) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageMultidimensionalTable_Retain(vImage_MultidimensionalTable) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageNewResamplingFilter(Float, vImage_Flags) -> ResamplingFilter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageNewResamplingFilterForFunctionUsingBuffer(ResamplingFilter, Float, CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, Float, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannelsWithPixel_ARGB16U(UnsafePointer<UInt16>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageOverwriteChannelsWithPixel_ARGB8888(UnsafePointer<UInt8>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannelsWithPixel_ARGBFFFF(UnsafePointer<Float>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannelsWithScalar_ARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannelsWithScalar_ARGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannelsWithScalar_Planar8(Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannelsWithScalar_PlanarF(Pixel_F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageOverwriteChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePNGDecompressionFilter(UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UInt32, UInt32, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePermuteChannelsWithMaskedInsert_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePermuteChannelsWithMaskedInsert_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePermuteChannels_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePermuteChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePermuteChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePiecewiseGamma_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_16S, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewiseGamma_Planar16Q12toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_16S, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewiseGamma_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewiseGamma_Planar8toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewiseGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewiseGamma_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewiseGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Float, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePiecewisePolynomial_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePiecewisePolynomial_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePiecewisePolynomial_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePiecewiseRational_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>>, UnsafeMutablePointer<UnsafePointer<Float>>, UnsafePointer<Float>, UInt32, UInt32, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedAlphaBlendWithPermute_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePremultipliedAlphaBlendWithPermute_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePremultipliedAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedAlphaBlend_BGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedAlphaBlend_BGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedConstAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedConstAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedConstAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultipliedConstAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePremultiplyData_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImagePremultiplyData_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImagePremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImagePremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImagePremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRichardsonLucyDeConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>, UnsafePointer<Int16>, UInt32, UInt32, UInt32, UInt32, Int32, Int32, UnsafeMutablePointer<UInt8>, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRichardsonLucyDeConvolve_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, UnsafePointer<Float>, UInt32, UInt32, UInt32, UInt32, UnsafeMutablePointer<Float>, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRichardsonLucyDeConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>, UnsafePointer<Int16>, UInt32, UInt32, UInt32, UInt32, Int32, Int32, Pixel_8, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRichardsonLucyDeConvolve_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, UnsafePointer<Float>, UInt32, UInt32, UInt32, UInt32, Pixel_F, UInt32, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate90_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageRotate90_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageRotate90_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate90_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate90_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_16U, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageRotate90_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate90_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Float, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageRotate_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Float, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageRotate_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Float, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Float, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Float, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageRotate_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, Float, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageScale_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageScale_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageScale_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageScale_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageScale_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageScale_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageSelectChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageSelectChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageTableLookUp_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, UnsafePointer<Pixel_8>, UnsafePointer<Pixel_8>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageTableLookUp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageTentConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UInt32, UInt32, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageTentConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImagePixelCount, vImagePixelCount, UInt32, UInt32, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageUnpremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageUnpremultiplyData_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageUnpremultiplyData_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageUnpremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageUnpremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageUnpremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageUnpremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageUnpremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageUnpremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageUnpremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalReflect_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageVerticalReflect_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageVerticalReflect_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalReflect_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalReflect_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageVerticalReflect_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalReflect_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageVerticalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageVerticalShearD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageVerticalShearD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageVerticalShearD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageVerticalShearD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vImageVerticalShear_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<Int16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageVerticalShear_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<UInt16>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vImageVerticalShear_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<UInt8>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalShear_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, UnsafeMutablePointer<Float>, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalShear_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, Pixel_8, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vImageVerticalShear_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter, Pixel_F, vImage_Flags) -> vImage_Error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvacos(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvacosf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvacosh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvacoshf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvasin(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvasinf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvasinh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvasinhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvatan(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvatan2(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvatan2f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvatanf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvatanh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvatanhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvceil(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvceilf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcopysign(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcopysignf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcos(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcosf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcosh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcoshf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcosisin(COpaquePointer, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcosisinf(COpaquePointer, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcospi(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvcospif(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvdiv(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvdivf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvexp(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvexp2(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvexp2f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvexpf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvexpm1(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvexpm1f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvfabs(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvfabsf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvfloor(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvfloorf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvfmod(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvfmodf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvint(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvintf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog10(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog10f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog1p(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog1pf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog2(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlog2f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlogb(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlogbf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvlogf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvnextafter(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvnextafterf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvnint(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvnintf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvpow(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvpowf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvpows(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vvpowsf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified vvrec(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvrecf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvremainder(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvremainderf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvrsqrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvrsqrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsin(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsincos(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsincosf(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsinf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsinh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsinhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsinpi(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsinpif(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsqrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvsqrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvtan(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvtanf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvtanh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvtanhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvtanpi(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified vvtanpif(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified zbdsqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zcgesv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zcposv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zdrscl_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbbrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbtf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbtrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgebak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgebal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgebd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgebrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgecon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgees_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgegs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgegv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgehd2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgehrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgelq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgelqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgels_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgelsd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgelss_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgelsx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgelsy_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeql2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeqlf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeqp3_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeqpf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeqr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgeqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgerfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgerq2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgerqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgesc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgesdd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgesv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgesvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgesvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgetc2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgetf2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgetrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgetri_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgetrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggbak_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggbal_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgges_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggesx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, __CLPK_L_fp, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggglm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgghrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgglse_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggqrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggsvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zggsvp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgtcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgtrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgtsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgtsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgttrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zgtts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbgst_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbgv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbgvd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbgvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhbtrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhecon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zheequb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zheev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zheevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zheevr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zheevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhegs2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhegst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhegv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhegvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhegvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zherfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhesv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhesvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhetd2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhetf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhetrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhetrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhetri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhetrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhfrk_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhgeqz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpev_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpevd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpevx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpgst_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpgv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpgvd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpgvx_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhpsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhptrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhsein_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zhseqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlabrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacgv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacn2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacp2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacpy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacrm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlacrt_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zladiv_(UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaed0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaed7_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaed8_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaein_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaesy_(UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaev2_(UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlag2c_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlags2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlagtm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlahef_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlahqr_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlahr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlahrd_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaic1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlals0_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlalsa_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlalsd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlangb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlange_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlangt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlanhb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlanhe_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlanhf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlanhp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlanhs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlanht_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlansb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlansp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlansy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlantb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlantp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlantr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> __CLPK_doublereal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlapll_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlapmt_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqgb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqge_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqhb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqhe_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqhp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqp2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqps_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqr0_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqr1_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqr2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqr3_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqr4_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqr5_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqsb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqsp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaqsy_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlar1v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlar2v_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarcm_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarfb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarfg_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarfp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarft_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarfx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlargv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarnv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarrv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarscl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlartg_(UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlartv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarzb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlarzt_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlascl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlascl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaset_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlasr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlassq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlaswp_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlasyf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlat2c_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_complex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatbs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatdf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatps_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatrd_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatrz_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlatzm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlauu2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zlauum_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbstf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbtf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbtrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpftrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpftrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpocon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpoequ_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpoequb_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zporfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zposv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zposvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpotf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpotrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpotri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpotrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zppcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zppequ_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zppsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zppsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpstf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpstrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zptcon_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zptrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zptsv_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zptsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpttrf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zpttrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zptts2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zrot_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zspcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zspmv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zspr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zspsv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zspsvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsptrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zstedc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zstegr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zstein_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zstemr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsteqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsycon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsyequb_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsymv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsyr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsyrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsysv_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsysvx_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsytf2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsytrf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsytri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zsytrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztbcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztbrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztbtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztfsm_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztftri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztfttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztfttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgex2_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgexc_(UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgsen_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgsja_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgsy2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztgsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztpcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztprfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztptri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztptrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztpttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztpttr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrcon_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrevc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrexc_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrrfs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrsen_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrsna_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_logical>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrsyl_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublereal>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrti2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrtri_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrtrs_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrttf_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztrttp_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztzrqf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ztzrzf_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zung2l_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zung2r_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunghr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungl2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunglq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungql_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungqr_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungr2_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungrq_(UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zungtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunm2l_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunm2r_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmbr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmhr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunml2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmlq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmql_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmqr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmr2_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmr3_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmrq_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmrz_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zunmtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zupgtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified zupmtr_(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>, UnsafeMutablePointer<__CLPK_doublecomplex>, UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
