---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Python.html
archived_at: '2026-07-18T02:54:38.424538Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Python Changes

## Python

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

Python-ast.hAdded #def DictCompAdded DictComp_kindAdded #def SetAdded #def SetCompAdded SetComp_kindAdded Set_kind__multiarray_api.hAdded #def NUMPY_IMPORT_ARRAY_RETVALAdded PyArrayNeighborhoodIter_Type (no architecture available)Added #def PyArray_Correlate2Added PyArray_Correlate2() (no architecture available)Added PyArray_GetEndianness() (no architecture available)Added #def PyArray_GetEndiannessAdded #def PyArray_GetNDArrayCFeatureVersionAdded PyArray_GetNDArrayCFeatureVersion() (no architecture available)Added #def PyArray_MultiIterFromObjectsAdded PyArray_MultiIterFromObjects() (no architecture available)Added PyArray_NeighborhoodIterNew() (no architecture available)Added #def PyArray_NeighborhoodIterNew__ufunc_api.hAdded PyUFunc_FromFuncAndDataAndSignature() (no architecture available)Added #def PyUFunc_FromFuncAndDataAndSignatureAdded #def PyUFunc_SetUsesArraysAsDataAdded PyUFunc_SetUsesArraysAsData() (no architecture available)_neighborhood_iterator_imp.hAdded PyArrayNeighborhoodIter_Next()Added PyArrayNeighborhoodIter_Reset()_numpyconfig.hAdded #def NPY_ABI_VERSIONAdded #def NPY_API_VERSIONAdded #def NPY_HAVE_COMPLEX_DOUBLEAdded #def NPY_HAVE_COMPLEX_FLOATAdded #def NPY_HAVE_COMPLEX_LONG_DOUBLEAdded #def NPY_HAVE_DECL_ISFINITEAdded #def NPY_HAVE_DECL_ISINFAdded #def NPY_HAVE_DECL_ISNANAdded #def NPY_HAVE_DECL_SIGNBITAdded #def NPY_SIZEOF_COMPLEX_DOUBLEAdded #def NPY_SIZEOF_COMPLEX_FLOATAdded #def NPY_SIZEOF_COMPLEX_LONGDOUBLEAdded #def NPY_USE_C99_COMPLEXAdded #def NPY_VISIBILITY_HIDDENabstract.hAdded indexcStringIO.hAdded #def PycStringIO_CAPSULE_NAMEcode.hAdded firstlinenoAdded funcnamecomplexobject.hModified format_spec_len

|  | Header |
| --- | --- |
| From | floatobject.h |
| To | complexobject.h |

datetime.hAdded #def PyDateTime_CAPSULE_NAMEdictobject.hAdded #def PyDictItems_CheckAdded #def PyDictKeys_CheckAdded #def PyDictValues_CheckAdded #def PyDictViewSet_Checkdtoa.hAdded decptAdded modeAdded rveAdded signModified ptr

|  | Header | 32/64-bit | Architectures |
| --- | --- | --- | --- |
| From | pystrtod.h | _Unknown_ | Unknown |
| To | dtoa.h | Both | i386,x86_64 |

floatobject.hAdded #def PyFloat_STR_PRECISIONAdded ndigitsfortranobject.hAdded #def ARRAY_ISALIGNEDAdded #def F2PY_ALIGN16Added #def F2PY_ALIGN4Added #def F2PY_ALIGN8Added #def F2PY_CHECK_ALIGNMENTAdded #def F2PY_GET_ALIGNMENTAdded #def F2PY_INTENT_ALIGNED16Added #def F2PY_INTENT_ALIGNED4Added #def F2PY_INTENT_ALIGNED8Added F2PyCapsule_AsVoidPtr()Added F2PyCapsule_Check()Added F2PyCapsule_FromVoidPtr()Modified #def PyInt_Check

|  | Header |
| --- | --- |
| From | intobject.h |
| To | fortranobject.h |

Modified #def Py_REFCNT

|  | Header |
| --- | --- |
| From | object.h |
| To | fortranobject.h |

Modified #def PyString_GET_SIZE

|  | Header |
| --- | --- |
| From | stringobject.h |
| To | fortranobject.h |

Modified #def PyInt_AS_LONG

|  | Header |
| --- | --- |
| From | intobject.h |
| To | fortranobject.h |

Modified #def Py_SIZE

|  | Header |
| --- | --- |
| From | object.h |
| To | fortranobject.h |

Modified #def Py_TYPE

|  | Header |
| --- | --- |
| From | object.h |
| To | fortranobject.h |

Modified #def PyString_AS_STRING

|  | Header |
| --- | --- |
| From | stringobject.h |
| To | fortranobject.h |

Modified #def PyString_Check

|  | Header |
| --- | --- |
| From | stringobject.h |
| To | fortranobject.h |

graminit.hAdded #def comp_forAdded #def comp_ifAdded #def comp_iterAdded #def dictorsetmakerAdded #def testlist_compAdded #def with_itemlongintrepr.hAdded sdigit (no architecture available)memoryobject.hAdded PyMemoryViewObjectAdded #def PyMemoryView_CheckAdded #def PyMemoryView_GET_BASEAdded #def PyMemoryView_GET_BUFFERAdded #def Py_MEMORYOBJECT_HAdded buffertypendarrayobject.hAdded NPY_DATETIMELTRAdded NPY_TIMEDELTALTRAdded #def PyArray_IsIntegerScalarndarraytypes.hAdded #def NDARRAYTYPES_HAdded NPY_DATETIMEUNITAdded #def NPY_DATETIME_DEFAULTUNITAdded #def NPY_DATETIME_NUMUNITSAdded NPY_FR_BAdded NPY_FR_DAdded NPY_FR_MAdded NPY_FR_WAdded NPY_FR_YAdded NPY_FR_asAdded NPY_FR_fsAdded NPY_FR_hAdded NPY_FR_mAdded NPY_FR_msAdded NPY_FR_nsAdded NPY_FR_psAdded NPY_FR_sAdded NPY_FR_usAdded #def NPY_METADATA_DTSTRAdded NPY_NEIGHBORHOOD_ITER_CIRCULAR_PADDINGAdded NPY_NEIGHBORHOOD_ITER_CONSTANT_PADDINGAdded NPY_NEIGHBORHOOD_ITER_MIRROR_PADDINGAdded NPY_NEIGHBORHOOD_ITER_ONE_PADDINGAdded NPY_NEIGHBORHOOD_ITER_ZERO_PADDINGAdded #def NPY_NO_EXPORTAdded #def NPY_STR_BAdded #def NPY_STR_DAdded #def NPY_STR_MAdded #def NPY_STR_WAdded #def NPY_STR_YAdded #def NPY_STR_asAdded #def NPY_STR_fsAdded #def NPY_STR_hAdded #def NPY_STR_mAdded #def NPY_STR_msAdded #def NPY_STR_nsAdded #def NPY_STR_psAdded #def NPY_STR_sAdded #def NPY_STR_usAdded PyArrayIterObject_tagAdded PyArrayNeighborhoodIterObjectAdded PyArrayNeighborhoodIter_Next2D() (no architecture available)Added npy_iter_get_dataptr_tModified PyArray_ArrFuncs

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArrayObject

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArrayInterface

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArray_Descr

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArrayMultiIterObject

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArrayFlagsObject

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArrayIterObject

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArrayMapIterObject

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArray_ArrayDescr

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArray_Dims

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

Modified PyArray_Chunk

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | ndarraytypes.h |

noprefix.hAdded #def BITSOF_DATETIMEAdded #def BITSOF_TIMEDELTAAdded #def MAX_DATETIMEAdded #def MAX_TIMEDELTAAdded #def MIN_DATETIMEAdded #def MIN_TIMEDELTAAdded #def SIZEOF_DATETIMEAdded #def SIZEOF_TIMEDELTAAdded #def datetimeAdded #def timedeltanpy_3kcompat.hAdded NpyCapsule_AsVoidPtr()Added NpyCapsule_Check()Added NpyCapsule_FromVoidPtr()Added NpyCapsule_FromVoidPtrAndDesc()Added NpyCapsule_GetDesc()Added PyInt_Check() (no architecture available)Added PyObject_Cmp() (no architecture available)Added #def PyUStringObjectAdded #def PyUString_CheckAdded #def PyUString_ConcatAdded #def PyUString_ConcatAndDelAdded #def PyUString_FormatAdded #def PyUString_FromFormatAdded #def PyUString_FromStringAdded #def PyUString_FromStringAndSizeAdded #def PyUString_GET_SIZEAdded #def PyUString_InternFromStringAdded #def PyUString_SizeAdded #def PyUString_TypeAdded PyUnicode_Concat2()Added PyUnicode_ConcatAndDel()Added #def npy_PyFile_CheckAdded npy_PyFile_Check() (no architecture available)Added #def npy_PyFile_DupAdded npy_PyFile_Dup() (no architecture available)Added npy_PyFile_DupClose() (no architecture available)Added #def npy_PyFile_DupCloseAdded npy_PyFile_OpenFile()Added simple_capsule_dtor()Modified #def PyBytes_GET_SIZE

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_AsString

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytesObject

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_AS_STRING

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_FromFormat

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_FromStringAndSize

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_AsStringAndSize

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_FromString

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_ConcatAndDel

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_Check

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_Type

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_Concat

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

Modified #def PyBytes_Size

|  | Header |
| --- | --- |
| From | bytesobject.h |
| To | npy_3kcompat.h |

npy_common.hAdded #def MyPyLong_AsInt64Added #def MyPyLong_FromInt64Added #def NPY_BITSOF_DATETIMEAdded #def NPY_BITSOF_TIMEDELTAAdded NPY_CPU_BIGAdded NPY_CPU_LITTLEAdded NPY_CPU_UNKNOWN_ENDIANAdded #def NPY_DATETIME_FMTAdded #def NPY_INLINEAdded #def NPY_MAX_DATETIMEAdded #def NPY_MAX_TIMEDELTAAdded #def NPY_MIN_DATETIMEAdded #def NPY_MIN_TIMEDELTAAdded #def NPY_SIZEOF_DATETIMEAdded #def NPY_SIZEOF_TIMEDELTAAdded #def NPY_TIMEDELTA_FMTAdded npy_datetimeAdded npy_timedeltaModified npy_cfloat

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | npy_common.h |

Modified npy_clongdouble

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | npy_common.h |

Modified npy_cdouble

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | npy_common.h |

npy_cpu.hAdded #def NPY_COPY_PYOBJECT_PTRAdded #def NPY_CPU_AMD64Added #def NPY_CPU_X86npy_endian.hAdded #def NPY_BIG_ENDIANAdded #def NPY_BYTE_ORDERAdded #def NPY_LITTLE_ENDIANnpy_math.hAdded #def NPY_1_PIAdded #def NPY_1_PIfAdded #def NPY_1_PIlAdded #def NPY_2_PIAdded #def NPY_2_PIfAdded #def NPY_2_PIlAdded #def NPY_EAdded #def NPY_EULERAdded #def NPY_EULERfAdded #def NPY_EULERlAdded #def NPY_EfAdded #def NPY_ElAdded #def NPY_INFINITYAdded #def NPY_INFINITYFAdded #def NPY_INFINITYLAdded #def NPY_LOG10EAdded #def NPY_LOG10EfAdded #def NPY_LOG10ElAdded #def NPY_LOG2EAdded #def NPY_LOG2EfAdded #def NPY_LOG2ElAdded #def NPY_LOGE10Added #def NPY_LOGE10fAdded #def NPY_LOGE10lAdded #def NPY_LOGE2Added #def NPY_LOGE2fAdded #def NPY_LOGE2lAdded #def NPY_NANAdded #def NPY_NANFAdded #def NPY_NANLAdded #def NPY_NZEROAdded #def NPY_NZEROFAdded #def NPY_NZEROLAdded #def NPY_PIAdded #def NPY_PI_2Added #def NPY_PI_2fAdded #def NPY_PI_2lAdded #def NPY_PI_4Added #def NPY_PI_4fAdded #def NPY_PI_4lAdded #def NPY_PIfAdded #def NPY_PIlAdded #def NPY_PZEROAdded #def NPY_PZEROFAdded #def NPY_PZEROLAdded #def NPY_SQRT1_2Added #def NPY_SQRT1_2fAdded #def NPY_SQRT1_2lAdded #def NPY_SQRT2Added #def NPY_SQRT2fAdded #def NPY_SQRT2lAdded npy_acos()Added npy_acosf()Added npy_acosh()Added npy_acoshf()Added npy_acoshl()Added npy_acosl()Added npy_aexp()Added npy_afabs()Added npy_alog()Added npy_asin()Added npy_asinf()Added npy_asinh()Added npy_asinhf()Added npy_asinhl()Added npy_asinl()Added npy_asqrt()Added npy_atan()Added npy_atan2()Added npy_atan2f()Added npy_atan2l()Added npy_atanf()Added npy_atanh()Added npy_atanhf()Added npy_atanhl()Added npy_atanl()Added npy_cabs()Added npy_cabsf()Added npy_cabsl()Added npy_carg()Added npy_cargf()Added npy_cargl()Added npy_ccos()Added npy_ccosf()Added npy_ccosl()Added npy_ceil()Added npy_ceilf()Added npy_ceill()Added npy_cexp()Added npy_cexpf()Added npy_cexpl()Added npy_cimag()Added npy_cimagf()Added npy_cimagl()Added npy_clog()Added npy_clogf()Added npy_clogl()Added npy_copysign()Added npy_copysignf()Added npy_copysignl()Added npy_cos()Added npy_cosf()Added npy_cosh()Added npy_coshf()Added npy_coshl()Added npy_cosl()Added npy_cpack()Added npy_cpackf()Added npy_cpackl()Added npy_cpow()Added npy_cpowf()Added npy_cpowl()Added npy_creal()Added npy_crealf()Added npy_creall()Added npy_csin()Added npy_csinf()Added npy_csinl()Added npy_csqrt()Added npy_csqrtf()Added npy_csqrtl()Added npy_deg2rad()Added npy_deg2radf()Added npy_deg2radl()Added #def npy_degreesAdded #def npy_degreesfAdded #def npy_degreeslAdded npy_exp()Added npy_exp2()Added npy_exp2f()Added npy_exp2l()Added npy_expf()Added npy_expl()Added npy_expm1()Added npy_expm1f()Added npy_expm1l()Added npy_fabs()Added npy_fabsf()Added npy_fabsl()Added npy_floor()Added npy_floorf()Added npy_floorl()Added npy_fmod()Added npy_fmodf()Added npy_fmodl()Added npy_hypot()Added npy_hypotf()Added npy_hypotl()Added #def npy_isfiniteAdded #def npy_isinfAdded #def npy_isnanAdded npy_log()Added npy_log10()Added npy_log10f()Added npy_log10l()Added npy_log1p()Added npy_log1pf()Added npy_log1pl()Added npy_log2()Added npy_log2f()Added npy_log2l()Added npy_logaddexp()Added npy_logaddexp2()Added npy_logaddexp2f()Added npy_logaddexp2l()Added npy_logaddexpf()Added npy_logaddexpl()Added npy_logf()Added npy_logl()Added npy_modf()Added npy_modff()Added npy_modfl()Added npy_nextafter()Added npy_nextafterf()Added npy_nextafterl()Added npy_pow()Added npy_powf()Added npy_powl()Added npy_rad2deg()Added npy_rad2degf()Added npy_rad2degl()Added #def npy_radiansAdded #def npy_radiansfAdded #def npy_radianslAdded npy_rint()Added npy_rintf()Added npy_rintl()Added #def npy_signbitAdded npy_sin()Added npy_sinf()Added npy_sinh()Added npy_sinhf()Added npy_sinhl()Added npy_sinl()Added npy_spacing()Added npy_spacingf()Added npy_spacingl()Added npy_sqrt()Added npy_sqrtf()Added npy_sqrtl()Added npy_tan()Added npy_tanf()Added npy_tanh()Added npy_tanhf()Added npy_tanhl()Added npy_tanl()Added npy_trunc()Added npy_truncf()Added npy_truncl()npy_os.hAdded #def NPY_OS_DARWINold_defines.hAdded #def PyArray_DATETIMEAdded #def PyArray_DATETIMELTRAdded #def PyArray_TIMEDELTAAdded #def PyArray_TIMEDELTALTRopcode.hAdded #def BUILD_SETAdded #def JUMP_IF_FALSE_OR_POPAdded #def JUMP_IF_TRUE_OR_POPAdded #def MAP_ADDAdded #def POP_JUMP_IF_FALSEAdded #def POP_JUMP_IF_TRUEAdded #def SETUP_WITHAdded #def SET_ADDpy_curses.hAdded #def PyCurses_CAPSULE_NAMEpycapsule.hAdded PyCapsule_DestructorAdded PyCapsule_GetContext()Added PyCapsule_GetDestructor()Added PyCapsule_GetName()Added PyCapsule_GetPointer()Added PyCapsule_Import()Added PyCapsule_IsValid()Added PyCapsule_New()Added PyCapsule_SetContext()Added PyCapsule_SetDestructor()Added PyCapsule_SetName()Added PyCapsule_SetPointer()Added PyCapsule_TypeAdded #def Py_CAPSULE_HAdded context (no architecture available)Added destructor (no architecture available)Added no_block (no architecture available)Added pointer (no architecture available)pyconfig.hRemoved #def HAVE_CHFLAGSRemoved #def HAVE_ISINFRemoved #def HAVE_ISNANRemoved #def HAVE_LCHFLAGSRemoved #def WORDS_BIGENDIANAdded #def AC_APPLE_UNIVERSAL_BUILDAdded #def DOUBLE_IS_LITTLE_ENDIAN_IEEE754Added #def HAVE_BROKEN_SEM_GETVALUEAdded #def HAVE_DECL_ISFINITEAdded #def HAVE_DECL_ISINFAdded #def HAVE_DECL_ISNANAdded #def HAVE_ERFAdded #def HAVE_ERFCAdded #def HAVE_GAMMAAdded #def HAVE_GCC_ASM_FOR_X87Added #def HAVE_INITGROUPSAdded #def HAVE_LGAMMAAdded #def HAVE_PTHREAD_INITAdded #def HAVE_ROUNDAdded #def HAVE_SEM_GETVALUEAdded #def HAVE_SEM_OPENAdded #def HAVE_SEM_UNLINKAdded #def HAVE_SPAWN_HAdded #def HAVE_TGAMMAAdded #def HAVE_UTIL_HAdded #def PY_FORMAT_LONG_LONGpyctype.hAdded #def PYCTYPE_HAdded #def PY_CTF_ALNUMAdded #def PY_CTF_ALPHAAdded #def PY_CTF_DIGITAdded #def PY_CTF_LOWERAdded #def PY_CTF_SPACEAdded #def PY_CTF_UPPERAdded #def PY_CTF_XDIGITAdded #def Py_ISALNUMAdded #def Py_ISALPHAAdded #def Py_ISDIGITAdded #def Py_ISLOWERAdded #def Py_ISSPACEAdded #def Py_ISUPPERAdded #def Py_ISXDIGITAdded #def Py_TOLOWERAdded #def Py_TOUPPERpyerrors.hAdded PyErr_NewExceptionWithDoc()pyexpat.hAdded #def PyExpat_CAPSULE_NAMEpymactoolbox.hAdded #def PyMac_INIT_TOOLBOX_OBJECT_CONVERTpymath.hAdded #def Py_FORCE_DOUBLEAdded [round()](https://developer.apple.com/documentation/kernel/1557369-round) (no architecture available)pyobjc-api.hAdded #def MAC_OS_X_VERSION_10_1Added #def MAC_OS_X_VERSION_10_2Added #def MAC_OS_X_VERSION_10_3Added #def MAC_OS_X_VERSION_10_4Added #def MAC_OS_X_VERSION_10_5Added #def MAC_OS_X_VERSION_MAX_ALLOWEDAdded #def PYOBJC_API_NAMEAdded #def PYOBJC_API_VERSIONAdded #def PyObjCClass_CheckAdded #def PyObjCClass_GetClassAdded #def PyObjCClass_NewAdded #def PyObjCCreateOpaquePointerTypeAdded #def PyObjCErr_AsExcAdded #def PyObjCErr_FromObjCAdded #def PyObjCErr_ToObjCAdded #def PyObjCErr_ToObjCWithGILStateAdded #def PyObjCIMP_CheckAdded #def PyObjCIMP_GetIMPAdded #def PyObjCIMP_GetSelectorAdded #def PyObjCObject_CheckAdded #def PyObjCObject_ClearObjectAdded #def PyObjCObject_ConvertAdded #def PyObjCObject_GetObjectAdded #def PyObjCObject_IsUninitializedAdded #def PyObjCObject_NewAdded #def PyObjCObject_NewTransientAdded #def PyObjCObject_ReleaseTransientAdded #def PyObjCPointerWrapper_RegisterAdded #def PyObjCRT_AlignOfTypeAdded #def PyObjCRT_RemoveFieldNamesAdded #def PyObjCRT_SELNameAdded #def PyObjCRT_SimplifySignatureAdded #def PyObjCRT_SizeOfTypeAdded #def PyObjCSelector_CheckAdded #def PyObjCSelector_GetClassAdded #def PyObjCSelector_GetSelectorAdded #def PyObjCUnsupportedMethod_CallerAdded #def PyObjCUnsupportedMethod_IMPAdded PyObjC_APIAdded #def PyObjC_API_HAdded #def PyObjC_BEGIN_WITH_GILAdded #def PyObjC_CArrayToPythonAdded PyObjC_CreateInlineTab()Added #def PyObjC_DURINGAdded #def PyObjC_DepythonifyCArrayAdded #def PyObjC_ENDHANDLERAdded #def PyObjC_END_WITH_GILAdded #def PyObjC_FreeCArrayAdded PyObjC_Function_PointerAdded #def PyObjC_GIL_FORWARD_EXCAdded #def PyObjC_GIL_RETURNAdded #def PyObjC_GIL_RETURNVOIDAdded #def PyObjC_HANDLERAdded #def PyObjC_INITDONEAdded #def PyObjC_INITERRORAdded #def PyObjC_IdToPythonAdded PyObjC_ImportAPI()Added #def PyObjC_InitSuperAdded #def PyObjC_InitSuperClsAdded #def PyObjC_MODULE_CREATEAdded #def PyObjC_MODULE_INITAdded #def PyObjC_NULLAdded #def PyObjC_ObjCToPythonAdded #def PyObjC_PerformWeaklinkingAdded #def PyObjC_PythonToCArrayAdded #def PyObjC_PythonToIdAdded #def PyObjC_PythonToObjCAdded #def PyObjC_RegisterMethodMappingAdded #def PyObjC_RegisterSignatureMappingAdded #def PyObjC_RegisterStructTypeAdded #def PyObjC_STRAdded #def PyObjC_SizeOfTypeAdded #def PyObjC_VarList_NewAdded PyObjC_WeakLinkAdded #def PyObjC__STRAdded PyObjC_function_mapAdded #def PyObjC_is_ascii_prefixAdded #def PyObjC_is_ascii_stringAdded RegisterMethodMappingFunctionTypeAdded objc_api (no architecture available)Added pyobjc_apipyobjc-compat.hAdded #def CGFLOAT_DEFINEDAdded [#def CGFLOAT_IS_DOUBLE](https://developer.apple.com/documentation/coregraphics/cgfloat_is_double)Added [#def CGFLOAT_MAX](https://developer.apple.com/documentation/coregraphics/cgfloat_max)Added [#def CGFLOAT_MIN](https://developer.apple.com/documentation/coregraphics/cgfloat_min)Added [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) (no architecture available)Added #def LLONG_MAXAdded #def LLONG_MINAdded #def MAC_OS_X_VERSION_10_6Added #def NSINTEGER_DEFINEDAdded [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) (no architecture available)Added [#def NSIntegerMax](https://developer.apple.com/documentation/objectivec/nsintegermax)Added [#def NSIntegerMin](https://developer.apple.com/documentation/objectivec/nsintegermin)Added [NSUInteger](https://developer.apple.com/documentation/objectivec/nsuinteger) (no architecture available)Added [#def NSUIntegerMax](https://developer.apple.com/documentation/objectivec/nsuintegermax)Added PyBytes_InternFromString() (no architecture available)Added #def PyBytes_InternFromStringAdded #def PyBytes_InternFromStringAndSizeAdded PyBytes_InternFromStringAndSize() (no architecture available)Added #def PyCapsule_CheckExactAdded #def PyErr_FormatAdded PyObjCErr_Format()Added PyObjCString_InternFromStringAndSize()Added #def PyObjC_COMPAT_HAdded PyObjC_ClearIntern()Added PyObjC_IntFromLong()Added PyObjC_IntFromString()Added PyObjC_InternValue()Added #def PyText_AppendAdded #def PyText_AsStringAdded #def PyText_CheckAdded #def PyText_FromFormatAdded #def PyText_FromStringAdded #def PyText_FromStringAndSizeAdded #def PyText_InternFromStringAdded #def PyText_InternInPlaceAdded #def Py_ARG_BYTESAdded #def Py_ARG_NSIntegerAdded #def Py_ARG_NSUIntegerAdded #def Py_ARG_SIZE_TAdded #def ULLONG_MAXAdded #def likelyAdded #def unlikelypyport.hAdded #def HAVE_INT32_TAdded #def HAVE_INT64_TAdded #def HAVE_PY_SET_53BIT_PRECISIONAdded #def HAVE_UINT32_TAdded #def HAVE_UINT64_TAdded #def PYLONG_BITS_IN_DIGITAdded #def PY_INT32_TAdded #def PY_INT64_TAdded #def PY_UINT32_TAdded #def PY_UINT64_TAdded #def Py_ALIGNEDAdded gethostname() (no architecture available)Modified #def toupper

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

Modified #def isalnum

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

Modified #def tolower

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

Modified #def islower

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

Modified #def isspace

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

Modified #def isupper

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

Modified #def DL_EXPORT

|  | Header |
| --- | --- |
| From | Python.h |
| To | pyport.h |

Modified #def isalpha

|  | Header |
| --- | --- |
| From | bytes_methods.h |
| To | pyport.h |

pystrtod.hAdded PyOS_double_to_string()Added PyOS_string_to_double()Added #def Py_DTSF_ADD_DOT_0Added #def Py_DTSF_ALTAdded #def Py_DTSF_SIGNAdded #def Py_DTST_FINITEAdded #def Py_DTST_INFINITEAdded #def Py_DTST_NANAdded endptr (no architecture available)Added format_code (no architecture available)Added overflow_exception (no architecture available)Added precision (no architecture available)sliceobject.hAdded PyEllipsis_Typestringobject.hAdded digits (no architecture available)Added grouping (no architecture available)Added min_width (no architecture available)Added thousands_sep (no architecture available)sysmodule.hAdded PySys_SetArgvEx()ucnhash.hAdded #def PyUnicodeData_CAPSULE_NAMEufuncobject.hAdded #def UFUNC_OBJ_ISOBJECTAdded #def UFUNC_OBJ_NEEDS_APIunicodeobject.hAdded base64SetO (no architecture available)Added base64WhiteSpace (no architecture available)utils.hAdded #def NPY_UNUSED

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
