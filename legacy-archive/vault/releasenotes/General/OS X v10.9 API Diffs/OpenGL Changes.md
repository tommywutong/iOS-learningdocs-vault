---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/OpenGL.html
archived_at: '2026-07-18T02:54:16.784902Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# OpenGL Changes

## OpenGL

CGLMacro.hAdded #def glGetObjectLabelEXTAdded #def glInsertEventMarkerEXTAdded #def glLabelObjectEXTAdded #def glPopGroupMarkerEXTAdded #def glPushGroupMarkerEXTAdded #def glTextureBarrierNVCGLRenderers.hRemoved #def kCGLRendererATIRadeon8500IDRemoved #def kCGLRendererATIRadeon9700IDRemoved #def kCGLRendererATIRadeonIDRemoved #def kCGLRendererATIRadeonX1000IDRemoved #def kCGLRendererATIRadeonX2000IDRemoved #def kCGLRendererATIRadeonX3000IDRemoved #def kCGLRendererATIRage128IDRemoved #def kCGLRendererATIRageProIDRemoved #def kCGLRendererAppleSWIDRemoved #def kCGLRendererGeForce2MXIDRemoved #def kCGLRendererGeForce3IDRemoved #def kCGLRendererGeForce8xxxIDRemoved #def kCGLRendererGeForceFXIDRemoved #def kCGLRendererGenericFloatIDRemoved #def kCGLRendererGenericIDRemoved #def kCGLRendererIntel900IDRemoved #def kCGLRendererIntelHD4000IDRemoved #def kCGLRendererIntelHDIDRemoved #def kCGLRendererIntelX3100IDRemoved #def kCGLRendererMesa3DFXIDRemoved #def kCGLRendererVTBladeXP2IDAdded kCGLRendererATIRadeon8500IDAdded kCGLRendererATIRadeon9700IDAdded kCGLRendererATIRadeonIDAdded kCGLRendererATIRadeonX1000IDAdded kCGLRendererATIRadeonX2000IDAdded kCGLRendererATIRadeonX3000IDAdded kCGLRendererATIRadeonX4000IDAdded kCGLRendererATIRage128IDAdded kCGLRendererATIRageProIDAdded kCGLRendererAppleSWIDAdded kCGLRendererGeForce2MXIDAdded kCGLRendererGeForce3IDAdded kCGLRendererGeForce8xxxIDAdded kCGLRendererGeForceFXIDAdded kCGLRendererGeForceIDAdded kCGLRendererGenericFloatIDAdded kCGLRendererGenericIDAdded kCGLRendererIntel900IDAdded kCGLRendererIntelHD4000IDAdded kCGLRendererIntelHD5000IDAdded kCGLRendererIntelHDIDAdded kCGLRendererIntelX3100IDAdded kCGLRendererMesa3DFXIDAdded kCGLRendererVTBladeXP2IDCGLTypes.hAdded kCGLOGLPVersion_GL3_CoreAdded kCGLOGLPVersion_GL4_CoreAdded kCGLRPMajorGLVersionModified CGLPBufferObj

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

Modified kCGLCPSurfaceTexture

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified kCGLGOResetLibrary

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.4 |

Modified kCGLGOUseErrorHandler

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

Modified kCGLPFACompliant

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified kCGLPFAFullScreen

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified kCGLPFAMPSafe

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified kCGLPFAMultiScreen

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified kCGLPFAOffScreen

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

Modified kCGLPFAPBuffer

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

Modified kCGLPFARemotePBuffer

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified kCGLPFARobust

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified kCGLPFASingleRenderer

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified kCGLPFAWindow

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified kCGLRPFullScreen

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified kCGLRPMPSafe

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified kCGLRPMultiScreen

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified kCGLRPRobust

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified kCGLRPTextureMemory

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

Modified kCGLRPVideoMemory

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

OpenGLAvailability.hAdded #def OPENGL_AVAILABLEAdded #def OPENGL_DEPRECATEDAdded #def OPENGL_DEPRECATED_MSGAdded #def OPENGL_ENUM_AVAILABLEAdded #def OPENGL_ENUM_DEPRECATEDAdded #def OPENGL_ENUM_DEPRECATED_MSGgl3.hRemoved GLbitfieldRemoved GLbooleanRemoved GLbyteRemoved GLcharRemoved GLclampdRemoved GLclampfRemoved GLdoubleRemoved GLenumRemoved GLfloatRemoved GLhalfRemoved GLintRemoved GLint64Removed GLintptrRemoved GLshortRemoved GLsizeiRemoved GLsizeiptrRemoved GLsyncRemoved GLubyteRemoved GLuintRemoved GLuint64Removed GLushortRemoved GLvoidAdded #def GL_ACTIVE_SUBROUTINESAdded #def GL_ACTIVE_SUBROUTINE_MAX_LENGTHAdded #def GL_ACTIVE_SUBROUTINE_UNIFORMSAdded #def GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONSAdded #def GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTHAdded #def GL_ARB_ES2_compatibilityAdded #def GL_ARB_blend_func_extendedAdded #def GL_ARB_draw_indirectAdded #def GL_ARB_get_program_binaryAdded #def GL_ARB_gpu_shader5Added #def GL_ARB_gpu_shader_fp64Added #def GL_ARB_shader_precisionAdded #def GL_ARB_shader_subroutineAdded #def GL_ARB_tessellation_shaderAdded #def GL_ARB_texture_buffer_object_rgb32Added #def GL_ARB_texture_query_lodAdded #def GL_ARB_transform_feedback2Added #def GL_ARB_transform_feedback3Added #def GL_ARB_vertex_attrib_64bitAdded #def GL_ARB_vertex_type_2_10_10_10_revAdded #def GL_ARB_viewport_arrayAdded #def GL_COMPATIBLE_SUBROUTINESAdded #def GL_DOUBLE_MAT2Added #def GL_DOUBLE_MAT2x3Added #def GL_DOUBLE_MAT2x4Added #def GL_DOUBLE_MAT3Added #def GL_DOUBLE_MAT3x2Added #def GL_DOUBLE_MAT3x4Added #def GL_DOUBLE_MAT4Added #def GL_DOUBLE_MAT4x2Added #def GL_DOUBLE_MAT4x3Added #def GL_DOUBLE_VEC2Added #def GL_DOUBLE_VEC3Added #def GL_DOUBLE_VEC4Added #def GL_DRAW_INDIRECT_BUFFERAdded #def GL_DRAW_INDIRECT_BUFFER_BINDINGAdded [#def GL_FIXED](https://developer.apple.com/documentation/opengles/gl_fixed)Added #def GL_FRACTIONAL_EVENAdded #def GL_FRACTIONAL_ODDAdded #def GL_FRAGMENT_INTERPOLATION_OFFSET_BITSAdded #def GL_GEOMETRY_SHADER_INVOCATIONSAdded [#def GL_HIGH_FLOAT](https://developer.apple.com/documentation/opengles/gl_high_float)Added [#def GL_HIGH_INT](https://developer.apple.com/documentation/opengles/gl_high_int)Added [#def GL_IMPLEMENTATION_COLOR_READ_FORMAT](https://developer.apple.com/documentation/opengles/gl_implementation_color_read_format)Added [#def GL_IMPLEMENTATION_COLOR_READ_TYPE](https://developer.apple.com/documentation/opengles/gl_implementation_color_read_type)Added #def GL_INT_2_10_10_10_REVAdded #def GL_INT_SAMPLER_CUBE_MAP_ARRAYAdded #def GL_ISOLINESAdded #def GL_LAYER_PROVOKING_VERTEXAdded [#def GL_LOW_FLOAT](https://developer.apple.com/documentation/opengles/gl_low_float)Added [#def GL_LOW_INT](https://developer.apple.com/documentation/opengles/gl_low_int)Added #def GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTSAdded #def GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTSAdded #def GL_MAX_DUAL_SOURCE_DRAW_BUFFERSAdded #def GL_MAX_FRAGMENT_INTERPOLATION_OFFSETAdded [#def GL_MAX_FRAGMENT_UNIFORM_VECTORS](https://developer.apple.com/documentation/opengles/gl_max_fragment_uniform_vectors)Added #def GL_MAX_GEOMETRY_SHADER_INVOCATIONSAdded #def GL_MAX_PATCH_VERTICESAdded #def GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSETAdded #def GL_MAX_SUBROUTINESAdded #def GL_MAX_SUBROUTINE_UNIFORM_LOCATIONSAdded #def GL_MAX_TESS_CONTROL_INPUT_COMPONENTSAdded #def GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTSAdded #def GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITSAdded #def GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTSAdded #def GL_MAX_TESS_CONTROL_UNIFORM_BLOCKSAdded #def GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTSAdded #def GL_MAX_TESS_EVALUATION_INPUT_COMPONENTSAdded #def GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTSAdded #def GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITSAdded #def GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKSAdded #def GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTSAdded #def GL_MAX_TESS_GEN_LEVELAdded #def GL_MAX_TESS_PATCH_COMPONENTSAdded #def GL_MAX_TRANSFORM_FEEDBACK_BUFFERSAdded [#def GL_MAX_VARYING_VECTORS](https://developer.apple.com/documentation/opengles/gl_max_varying_vectors)Added #def GL_MAX_VERTEX_STREAMSAdded [#def GL_MAX_VERTEX_UNIFORM_VECTORS](https://developer.apple.com/documentation/opengles/gl_max_vertex_uniform_vectors)Added #def GL_MAX_VIEWPORTSAdded [#def GL_MEDIUM_FLOAT](https://developer.apple.com/documentation/opengles/gl_medium_float)Added [#def GL_MEDIUM_INT](https://developer.apple.com/documentation/opengles/gl_medium_int)Added #def GL_MIN_FRAGMENT_INTERPOLATION_OFFSETAdded #def GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSETAdded #def GL_MIN_SAMPLE_SHADING_VALUEAdded #def GL_NUM_COMPATIBLE_SUBROUTINESAdded #def GL_NUM_PROGRAM_BINARY_FORMATSAdded [#def GL_NUM_SHADER_BINARY_FORMATS](https://developer.apple.com/documentation/opengles/gl_num_shader_binary_formats)Added #def GL_ONE_MINUS_SRC1_ALPHAAdded #def GL_ONE_MINUS_SRC1_COLORAdded #def GL_PATCHESAdded #def GL_PATCH_DEFAULT_INNER_LEVELAdded #def GL_PATCH_DEFAULT_OUTER_LEVELAdded #def GL_PATCH_VERTICESAdded #def GL_POLYGON_MODEAdded #def GL_PROGRAM_BINARY_FORMATSAdded #def GL_PROGRAM_BINARY_LENGTHAdded #def GL_PROGRAM_BINARY_RETRIEVABLE_HINTAdded #def GL_PROXY_TEXTURE_CUBE_MAP_ARRAYAdded #def GL_QUADSAdded [#def GL_RGB565](https://developer.apple.com/documentation/opengles/gl_rgb565)Added #def GL_SAMPLER_CUBE_MAP_ARRAYAdded #def GL_SAMPLER_CUBE_MAP_ARRAY_SHADOWAdded #def GL_SAMPLE_SHADINGAdded [#def GL_SHADER_BINARY_FORMATS](https://developer.apple.com/documentation/opengles/gl_shader_binary_formats)Added [#def GL_SHADER_COMPILER](https://developer.apple.com/documentation/opengles/gl_shader_compiler)Added #def GL_SRC1_ALPHAAdded #def GL_SRC1_COLORAdded #def GL_TESS_CONTROL_OUTPUT_VERTICESAdded #def GL_TESS_CONTROL_SHADERAdded #def GL_TESS_CONTROL_SHADER_BITAdded #def GL_TESS_EVALUATION_SHADERAdded #def GL_TESS_EVALUATION_SHADER_BITAdded #def GL_TESS_GEN_MODEAdded #def GL_TESS_GEN_POINT_MODEAdded #def GL_TESS_GEN_SPACINGAdded #def GL_TESS_GEN_VERTEX_ORDERAdded #def GL_TEXTURE_BINDING_CUBE_MAP_ARRAYAdded #def GL_TEXTURE_CUBE_MAP_ARRAYAdded #def GL_TRANSFORM_FEEDBACKAdded #def GL_TRANSFORM_FEEDBACK_BINDINGAdded #def GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVEAdded #def GL_TRANSFORM_FEEDBACK_BUFFER_PAUSEDAdded #def GL_UNDEFINED_VERTEXAdded #def GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADERAdded #def GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADERAdded #def GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAYAdded #def GL_VERSION_3_3Added #def GL_VERSION_4_0Added #def GL_VERSION_4_1Added #def GL_VERTEX_ATTRIB_ARRAY_DIVISORAdded #def GL_VIEWPORT_BOUNDS_RANGEAdded #def GL_VIEWPORT_INDEX_PROVOKING_VERTEXAdded #def GL_VIEWPORT_SUBPIXEL_BITSAdded PFNGLBEGINQUERYINDEXEDPROCAdded PFNGLBINDFRAGDATALOCATIONINDEXEDPROCAdded PFNGLBINDTRANSFORMFEEDBACKPROCAdded PFNGLBLENDEQUATIONIPROCAdded PFNGLBLENDEQUATIONSEPARATEIPROCAdded PFNGLBLENDFUNCIPROCAdded PFNGLBLENDFUNCSEPARATEIPROCAdded PFNGLCLEARDEPTHFPROCAdded PFNGLDELETETRANSFORMFEEDBACKSPROCAdded PFNGLDEPTHRANGEARRAYVPROCAdded PFNGLDEPTHRANGEFPROCAdded PFNGLDEPTHRANGEINDEXEDPROCAdded PFNGLDRAWARRAYSINDIRECTPROCAdded PFNGLDRAWELEMENTSINDIRECTPROCAdded PFNGLDRAWTRANSFORMFEEDBACKPROCAdded PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROCAdded PFNGLENDQUERYINDEXEDPROCAdded PFNGLGENTRANSFORMFEEDBACKSPROCAdded PFNGLGETACTIVESUBROUTINENAMEPROCAdded PFNGLGETACTIVESUBROUTINEUNIFORMIVPROCAdded PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROCAdded PFNGLGETDOUBLEI_VPROCAdded PFNGLGETFLOATI_VPROCAdded PFNGLGETFRAGDATAINDEXPROCAdded PFNGLGETPROGRAMBINARYPROCAdded PFNGLGETPROGRAMSTAGEIVPROCAdded PFNGLGETQUERYINDEXEDIVPROCAdded PFNGLGETSHADERPRECISIONFORMATPROCAdded PFNGLGETSUBROUTINEINDEXPROCAdded PFNGLGETSUBROUTINEUNIFORMLOCATIONPROCAdded PFNGLGETUNIFORMDVPROCAdded PFNGLGETUNIFORMSUBROUTINEUIVPROCAdded PFNGLGETVERTEXATTRIBLDVPROCAdded PFNGLISTRANSFORMFEEDBACKPROCAdded PFNGLMINSAMPLESHADINGPROCAdded PFNGLPATCHPARAMETERFVPROCAdded PFNGLPATCHPARAMETERIPROCAdded PFNGLPAUSETRANSFORMFEEDBACKPROCAdded PFNGLPROGRAMBINARYPROCAdded PFNGLPROGRAMUNIFORM1DPROCAdded PFNGLPROGRAMUNIFORM1DVPROCAdded PFNGLPROGRAMUNIFORM2DPROCAdded PFNGLPROGRAMUNIFORM2DVPROCAdded PFNGLPROGRAMUNIFORM3DPROCAdded PFNGLPROGRAMUNIFORM3DVPROCAdded PFNGLPROGRAMUNIFORM4DPROCAdded PFNGLPROGRAMUNIFORM4DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX2DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX2X3DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX2X4DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX3DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX3X2DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX3X4DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX4DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX4X2DVPROCAdded PFNGLPROGRAMUNIFORMMATRIX4X3DVPROCAdded PFNGLRELEASESHADERCOMPILERPROCAdded PFNGLRESUMETRANSFORMFEEDBACKPROCAdded PFNGLSCISSORARRAYVPROCAdded PFNGLSCISSORINDEXEDPROCAdded PFNGLSCISSORINDEXEDVPROCAdded PFNGLSHADERBINARYPROCAdded PFNGLUNIFORM1DPROCAdded PFNGLUNIFORM1DVPROCAdded PFNGLUNIFORM2DPROCAdded PFNGLUNIFORM2DVPROCAdded PFNGLUNIFORM3DPROCAdded PFNGLUNIFORM3DVPROCAdded PFNGLUNIFORM4DPROCAdded PFNGLUNIFORM4DVPROCAdded PFNGLUNIFORMMATRIX2DVPROCAdded PFNGLUNIFORMMATRIX2X3DVPROCAdded PFNGLUNIFORMMATRIX2X4DVPROCAdded PFNGLUNIFORMMATRIX3DVPROCAdded PFNGLUNIFORMMATRIX3X2DVPROCAdded PFNGLUNIFORMMATRIX3X4DVPROCAdded PFNGLUNIFORMMATRIX4DVPROCAdded PFNGLUNIFORMMATRIX4X2DVPROCAdded PFNGLUNIFORMMATRIX4X3DVPROCAdded PFNGLUNIFORMSUBROUTINESUIVPROCAdded PFNGLVERTEXATTRIBDIVISORPROCAdded PFNGLVERTEXATTRIBL1DPROCAdded PFNGLVERTEXATTRIBL1DVPROCAdded PFNGLVERTEXATTRIBL2DPROCAdded PFNGLVERTEXATTRIBL2DVPROCAdded PFNGLVERTEXATTRIBL3DPROCAdded PFNGLVERTEXATTRIBL3DVPROCAdded PFNGLVERTEXATTRIBL4DPROCAdded PFNGLVERTEXATTRIBL4DVPROCAdded PFNGLVERTEXATTRIBLPOINTERPROCAdded PFNGLVERTEXATTRIBP1UIPROCAdded PFNGLVERTEXATTRIBP1UIVPROCAdded PFNGLVERTEXATTRIBP2UIPROCAdded PFNGLVERTEXATTRIBP2UIVPROCAdded PFNGLVERTEXATTRIBP3UIPROCAdded PFNGLVERTEXATTRIBP3UIVPROCAdded PFNGLVERTEXATTRIBP4UIPROCAdded PFNGLVERTEXATTRIBP4UIVPROCAdded PFNGLVIEWPORTARRAYVPROCAdded PFNGLVIEWPORTINDEXEDFPROCAdded PFNGLVIEWPORTINDEXEDFVPROCAdded glBeginQueryIndexed()Added glBindFragDataLocationIndexed()Added glBindTransformFeedback()Added glBlendEquationSeparatei()Added glBlendEquationi()Added glBlendFuncSeparatei()Added glBlendFunci()Added [glClearDepthf()](https://developer.apple.com/documentation/opengles/1617581-glcleardepthf)Added glDeleteTransformFeedbacks()Added glDepthRangeArrayv()Added glDepthRangeIndexed()Added [glDepthRangef()](https://developer.apple.com/documentation/opengles/1617401-gldepthrangef)Added glDrawArraysIndirect()Added glDrawElementsIndirect()Added glDrawTransformFeedback()Added glDrawTransformFeedbackStream()Added glEndQueryIndexed()Added glGenTransformFeedbacks()Added glGetActiveSubroutineName()Added glGetActiveSubroutineUniformName()Added glGetActiveSubroutineUniformiv()Added glGetDoublei_v()Added glGetFloati_v()Added glGetFragDataIndex()Added glGetProgramBinary()Added glGetProgramStageiv()Added glGetQueryIndexediv()Added [glGetShaderPrecisionFormat()](https://developer.apple.com/documentation/opengles/1617276-glgetshaderprecisionformat)Added glGetSubroutineIndex()Added glGetSubroutineUniformLocation()Added glGetUniformSubroutineuiv()Added glGetUniformdv()Added glGetVertexAttribLdv()Added glIsTransformFeedback()Added glMinSampleShading()Added glPatchParameterfv()Added glPatchParameteri()Added glPauseTransformFeedback()Added glProgramBinary()Added glProgramUniform1d()Added glProgramUniform1dv()Added glProgramUniform2d()Added glProgramUniform2dv()Added glProgramUniform3d()Added glProgramUniform3dv()Added glProgramUniform4d()Added glProgramUniform4dv()Added glProgramUniformMatrix2dv()Added glProgramUniformMatrix2x3dv()Added glProgramUniformMatrix2x4dv()Added glProgramUniformMatrix3dv()Added glProgramUniformMatrix3x2dv()Added glProgramUniformMatrix3x4dv()Added glProgramUniformMatrix4dv()Added glProgramUniformMatrix4x2dv()Added glProgramUniformMatrix4x3dv()Added [glReleaseShaderCompiler()](https://developer.apple.com/documentation/opengles/1617304-glreleaseshadercompiler)Added glResumeTransformFeedback()Added glScissorArrayv()Added glScissorIndexed()Added glScissorIndexedv()Added [glShaderBinary()](https://developer.apple.com/documentation/opengles/1617514-glshaderbinary)Added glUniform1d()Added glUniform1dv()Added glUniform2d()Added glUniform2dv()Added glUniform3d()Added glUniform3dv()Added glUniform4d()Added glUniform4dv()Added glUniformMatrix2dv()Added glUniformMatrix2x3dv()Added glUniformMatrix2x4dv()Added glUniformMatrix3dv()Added glUniformMatrix3x2dv()Added glUniformMatrix3x4dv()Added glUniformMatrix4dv()Added glUniformMatrix4x2dv()Added glUniformMatrix4x3dv()Added glUniformSubroutinesuiv()Added glVertexAttribDivisor()Added glVertexAttribL1d()Added glVertexAttribL1dv()Added glVertexAttribL2d()Added glVertexAttribL2dv()Added glVertexAttribL3d()Added glVertexAttribL3dv()Added glVertexAttribL4d()Added glVertexAttribL4dv()Added glVertexAttribLPointer()Added glVertexAttribP1ui()Added glVertexAttribP1uiv()Added glVertexAttribP2ui()Added glVertexAttribP2uiv()Added glVertexAttribP3ui()Added glVertexAttribP3uiv()Added glVertexAttribP4ui()Added glVertexAttribP4uiv()Added glViewportArrayv()Added glViewportIndexedf()Added glViewportIndexedfv()Modified #def GL_ACTIVE_PROGRAM

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ALL_SHADER_BITS

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ANY_SAMPLES_PASSED

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_explicit_attrib_location

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_occlusion_query2

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_sampler_objects

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_separate_shader_objects

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_shader_bit_encoding

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_texture_rgb10_a2ui

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_texture_swizzle

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_timer_query

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_FRAGMENT_SHADER_BIT

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_GEOMETRY_SHADER_BIT

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_PROGRAM_PIPELINE_BINDING

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_PROGRAM_SEPARABLE

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_RGB10_A2UI

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_SAMPLER_BINDING

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_A

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_B

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_G

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_R

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_RGBA

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TIMESTAMP

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TIME_ELAPSED

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_VERTEX_SHADER_BIT

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLACTIVESHADERPROGRAMPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLBINDPROGRAMPIPELINEPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLBINDSAMPLERPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLCREATESHADERPROGRAMVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLDELETEPROGRAMPIPELINESPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLDELETESAMPLERSPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGENPROGRAMPIPELINESPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGENSAMPLERSPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETPROGRAMPIPELINEINFOLOGPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETPROGRAMPIPELINEIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETQUERYOBJECTI64VPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETQUERYOBJECTUI64VPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERFVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERIIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERIUIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLISPROGRAMPIPELINEPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLISSAMPLERPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMPARAMETERIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLQUERYCOUNTERPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERFPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERFVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIUIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLUSEPROGRAMSTAGESPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLVALIDATEPROGRAMPIPELINEPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glActiveShaderProgram()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glBindProgramPipeline()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glBindSampler()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glCreateShaderProgramv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glDeleteProgramPipelines()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glDeleteSamplers()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glDrawArraysInstanced()

|  | Declaration |
| --- | --- |
| From | void glDrawArraysInstanced ( GLenum mode, GLint first, GLsizei count, GLsizei primcount); |
| To | void glDrawArraysInstanced ( GLenum mode, GLint first, GLsizei count, GLsizei instancecount); |

Modified glDrawElementsInstanced()

|  | Declaration |
| --- | --- |
| From | void glDrawElementsInstanced ( GLenum mode, GLsizei count, GLenum type, const GLvoid \*indices, GLsizei primcount); |
| To | void glDrawElementsInstanced ( GLenum mode, GLsizei count, GLenum type, const GLvoid \*indices, GLsizei instancecount); |

Modified glDrawElementsInstancedBaseVertex()

|  | Declaration |
| --- | --- |
| From | void glDrawElementsInstancedBaseVertex ( GLenum mode, GLsizei count, GLenum type, const GLvoid \*indices, GLsizei primcount, GLint basevertex); |
| To | void glDrawElementsInstancedBaseVertex ( GLenum mode, GLsizei count, GLenum type, const GLvoid \*indices, GLsizei instancecount, GLint basevertex); |

Modified glGenProgramPipelines()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGenSamplers()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetProgramPipelineInfoLog()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetProgramPipelineiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetQueryObjecti64v()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetQueryObjectui64v()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameterIiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameterIuiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameterfv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameteriv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glIsProgramPipeline()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glIsSampler()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glMultiDrawArrays()

|  | Declaration |
| --- | --- |
| From | void glMultiDrawArrays ( GLenum mode, const GLint \*first, const GLsizei \*count, GLsizei primcount); |
| To | void glMultiDrawArrays ( GLenum mode, const GLint \*first, const GLsizei \*count, GLsizei drawcount); |

Modified glMultiDrawElements()

|  | Declaration |
| --- | --- |
| From | void glMultiDrawElements ( GLenum mode, const GLsizei \*count, GLenum type, const GLvoid \*const \*indices, GLsizei primcount); |
| To | void glMultiDrawElements ( GLenum mode, const GLsizei \*count, GLenum type, const GLvoid \*const \*indices, GLsizei drawcount); |

Modified glMultiDrawElementsBaseVertex()

|  | Declaration |
| --- | --- |
| From | void glMultiDrawElementsBaseVertex ( GLenum mode, const GLsizei \*count, GLenum type, const GLvoid \*const \*indices, GLsizei primcount, const GLint \*basevertex); |
| To | void glMultiDrawElementsBaseVertex ( GLenum mode, const GLsizei \*count, GLenum type, const GLvoid \*const \*indices, GLsizei drawcount, const GLint \*basevertex); |

Modified glProgramParameteri()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix2x3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix2x4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix3x2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix3x4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix4x2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix4x3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glQueryCounter()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterIiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterIuiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterf()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterfv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameteri()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameteriv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glUseProgramStages()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glValidateProgramPipeline()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

gl3ext.hRemoved PFNGLOBJECTUNPURGABLEAPPLEPROCRemoved PFNGLTEXTURERANGLEAPPLEPROCAdded #def GL_APPLE_flush_renderAdded #def GL_APPLE_row_bytesAdded #def GL_ARB_draw_buffers_blendAdded #def GL_ARB_internalformat_queryAdded #def GL_ARB_sample_shadingAdded #def GL_ARB_shading_language_includeAdded #def GL_ARB_texture_cube_map_arrayAdded #def GL_ARB_texture_gatherAdded #def GL_ARB_texture_storageAdded [#def GL_BUFFER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_buffer_object_ext)Added [#def GL_EXT_debug_label](https://developer.apple.com/documentation/opengles/gl_ext_debug_label)Added [#def GL_EXT_debug_marker](https://developer.apple.com/documentation/opengles/gl_ext_debug_marker)Added #def GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARBAdded #def GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARBAdded #def GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARBAdded #def GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARBAdded #def GL_MIN_SAMPLE_SHADING_VALUE_ARBAdded #def GL_NAMED_STRING_LENGTH_ARBAdded #def GL_NAMED_STRING_TYPE_ARBAdded #def GL_NUM_SAMPLE_COUNTSAdded #def GL_NV_texture_barrierAdded #def GL_PACK_IMAGE_BYTES_APPLEAdded #def GL_PACK_ROW_BYTES_APPLEAdded [#def GL_PROGRAM_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_object_ext)Added [#def GL_PROGRAM_PIPELINE_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_pipeline_object_ext)Added #def GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARBAdded [#def GL_QUERY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_query_object_ext)Added #def GL_SAMPLERAdded #def GL_SAMPLER_CUBE_MAP_ARRAY_ARBAdded #def GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARBAdded #def GL_SAMPLE_SHADING_ARBAdded #def GL_SHADER_INCLUDE_ARBAdded [#def GL_SHADER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_shader_object_ext)Added [#def GL_SYNC_OBJECT_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_object_apple)Added #def GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARBAdded #def GL_TEXTURE_CUBE_MAP_ARRAY_ARBAdded #def GL_TEXTURE_IMMUTABLE_FORMATAdded #def GL_UNPACK_IMAGE_BYTES_APPLEAdded #def GL_UNPACK_ROW_BYTES_APPLEAdded #def GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARBAdded [#def GL_VERTEX_ARRAY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_array_object_ext)Added PFNGLBLENDEQUATIONIARBPROCAdded PFNGLBLENDEQUATIONSEPARATEIARBPROCAdded PFNGLBLENDFUNCIARBPROCAdded PFNGLBLENDFUNCSEPARATEIARBPROCAdded PFNGLCOMPILESHADERINCLUDEARBPROCAdded PFNGLDELETENAMEDSTRINGARBPROCAdded PFNGLFINISHRENDERAPPLEPROCAdded PFNGLFLUSHRENDERAPPLEPROCAdded PFNGLGETINTERNALFORMATIVPROCAdded PFNGLGETNAMEDSTRINGARBPROCAdded PFNGLGETNAMEDSTRINGIVARBPROCAdded PFNGLGETOBJECTLABELEXTPROCAdded PFNGLINSERTEVENTMARKEREXTPROCAdded PFNGLISNAMEDSTRINGARBPROCAdded PFNGLLABELOBJECTEXTPROCAdded PFNGLMINSAMPLESHADINGARBPROCAdded PFNGLNAMEDSTRINGARBPROCAdded PFNGLOBJECTUNPURGEABLEAPPLEPROCAdded PFNGLPOPGROUPMARKEREXTPROCAdded PFNGLPUSHGROUPMARKEREXTPROCAdded PFNGLSWAPAPPLEPROCAdded PFNGLTEXSTORAGE1DPROCAdded PFNGLTEXSTORAGE2DPROCAdded PFNGLTEXSTORAGE3DPROCAdded PFNGLTEXTUREBARRIERNVPROCAdded PFNGLTEXTURERANGEAPPLEPROCAdded glBlendEquationSeparateiARB()Added glBlendEquationiARB()Added glBlendFuncSeparateiARB()Added glBlendFunciARB()Added glCompileShaderIncludeARB()Added glDeleteNamedStringARB()Added glFinishRenderAPPLE()Added glFlushRenderAPPLE()Added glGetInternalformativ()Added glGetNamedStringARB()Added glGetNamedStringivARB()Added [glGetObjectLabelEXT()](https://developer.apple.com/documentation/opengles/1614334-glgetobjectlabelext)Added [glInsertEventMarkerEXT()](https://developer.apple.com/documentation/opengles/1614284-glinserteventmarkerext)Added glIsNamedStringARB()Added [glLabelObjectEXT()](https://developer.apple.com/documentation/opengles/1614324-gllabelobjectext)Added glMinSampleShadingARB()Added glNamedStringARB()Added [glPopGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614338-glpopgroupmarkerext)Added [glPushGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614275-glpushgroupmarkerext)Added glSwapAPPLE()Added glTexStorage1D()Added glTexStorage2D()Added glTexStorage3D()Added glTextureBarrierNV()Modified #def GL_ACTIVE_PROGRAM

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ALL_SHADER_BITS

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ANY_SAMPLES_PASSED

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_explicit_attrib_location

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_occlusion_query2

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_sampler_objects

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_separate_shader_objects

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_shader_bit_encoding

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_texture_rgb10_a2ui

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_texture_swizzle

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_ARB_timer_query

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_FRAGMENT_SHADER_BIT

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_GEOMETRY_SHADER_BIT

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_PROGRAM_PIPELINE_BINDING

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_PROGRAM_SEPARABLE

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_RGB10_A2UI

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_SAMPLER_BINDING

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_A

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_B

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_G

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_R

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TEXTURE_SWIZZLE_RGBA

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TIMESTAMP

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_TIME_ELAPSED

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified #def GL_VERTEX_SHADER_BIT

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLACTIVESHADERPROGRAMPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLBINDPROGRAMPIPELINEPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLBINDSAMPLERPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLCREATESHADERPROGRAMVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLDELETEPROGRAMPIPELINESPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLDELETESAMPLERSPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGENPROGRAMPIPELINESPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGENSAMPLERSPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETPROGRAMPIPELINEINFOLOGPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETPROGRAMPIPELINEIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETQUERYOBJECTI64VPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETQUERYOBJECTUI64VPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERFVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERIIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERIUIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLGETSAMPLERPARAMETERIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLISPROGRAMPIPELINEPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLISSAMPLERPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMPARAMETERIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM1UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM2UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM3UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4FPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4IPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4IVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4UIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORM4UIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX4FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLQUERYCOUNTERPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERFPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERFVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIUIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLSAMPLERPARAMETERIVPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLUSEPROGRAMSTAGESPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified PFNGLVALIDATEPROGRAMPIPELINEPROC

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glActiveShaderProgram()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glBindProgramPipeline()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glBindSampler()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glCreateShaderProgramv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glDeleteProgramPipelines()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glDeleteSamplers()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGenProgramPipelines()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGenSamplers()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetProgramPipelineInfoLog()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetProgramPipelineiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetQueryObjecti64v()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetQueryObjectui64v()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameterIiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameterIuiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameterfv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glGetSamplerParameteriv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glIsProgramPipeline()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glIsSampler()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramParameteri()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform1uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform2uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform3uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4f()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4i()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4iv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4ui()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniform4uiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix2x3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix2x4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix3x2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix3x4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix4fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix4x2fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glProgramUniformMatrix4x3fv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glQueryCounter()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterIiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterIuiv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterf()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameterfv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameteri()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glSamplerParameteriv()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glUseProgramStages()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

Modified glValidateProgramPipeline()

|  | Header |
| --- | --- |
| From | OpenGL/gl3ext.h |
| To | OpenGL/gl3.h |

glext.hAdded [#def GL_BUFFER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_buffer_object_ext)Added [#def GL_EXT_debug_label](https://developer.apple.com/documentation/opengles/gl_ext_debug_label)Added [#def GL_EXT_debug_marker](https://developer.apple.com/documentation/opengles/gl_ext_debug_marker)Added #def GL_NV_texture_barrierAdded [#def GL_PROGRAM_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_object_ext)Added [#def GL_QUERY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_query_object_ext)Added #def GL_SAMPLERAdded [#def GL_SHADER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_shader_object_ext)Added [#def GL_SYNC_OBJECT_APPLE](https://developer.apple.com/documentation/opengles/gl_sync_object_apple)Added [#def GL_VERTEX_ARRAY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_array_object_ext)Added [glGetObjectLabelEXT()](https://developer.apple.com/documentation/opengles/1614334-glgetobjectlabelext)Added [glInsertEventMarkerEXT()](https://developer.apple.com/documentation/opengles/1614284-glinserteventmarkerext)Added [glLabelObjectEXT()](https://developer.apple.com/documentation/opengles/1614324-gllabelobjectext)Added [glPopGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614338-glpopgroupmarkerext)Added [glPushGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614275-glpushgroupmarkerext)Added glTextureBarrierNV()glu.hModified GLUnurbsObj

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified GLUquadricObj

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified GLUtesselatorObj

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified GLUtriangulatorObj

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBeginCurve()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBeginPolygon()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBeginSurface()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBeginTrim()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild1DMipmapLevels()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild1DMipmaps()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild2DMipmapLevels()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild2DMipmaps()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild3DMipmapLevels()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild3DMipmaps()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluCheckExtension()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluCylinder()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluDeleteNurbsRenderer()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluDeleteQuadric()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluDeleteTess()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluDisk()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluEndCurve()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluEndPolygon()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluEndSurface()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluEndTrim()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluErrorString()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluGetNurbsProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluGetString()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluGetTessProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluLoadSamplingMatrices()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluLookAt()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNewNurbsRenderer()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNewQuadric()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNewTess()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNextContour()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNurbsCallback()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNurbsCallbackData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNurbsCallbackDataEXT()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNurbsCurve()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNurbsProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNurbsSurface()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluOrtho2D()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluPartialDisk()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluPerspective()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluPickMatrix()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluProject()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluPwlCurve()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluQuadricCallback()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluQuadricDrawStyle()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluQuadricNormals()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluQuadricOrientation()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluQuadricTexture()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluScaleImage()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluSphere()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessBeginContour()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessBeginPolygon()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessCallback()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessEndContour()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessEndPolygon()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessNormal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluTessVertex()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluUnProject()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluUnProject4()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

gluContext.hAdded gluCylinderCTX()Added gluDiskCTX()Added gluPartialDiskCTX()Added gluSphereCTX()Modified gluBuild1DMipmapLevelsCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild1DMipmapsCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild2DMipmapLevelsCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild2DMipmapsCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild3DMipmapLevelsCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluBuild3DMipmapsCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluLookAtCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNewNurbsRendererCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNewQuadricCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluNewTessCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluOrtho2DCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluPerspectiveCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluPickMatrixCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified gluScaleImageCTX()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

gluMacro.hAdded #def gluCylinderAdded #def gluDiskAdded #def gluPartialDiskAdded #def gluSphere

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
