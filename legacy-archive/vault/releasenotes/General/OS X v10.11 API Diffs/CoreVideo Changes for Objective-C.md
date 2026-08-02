---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreVideo.html
archived_at: '2026-07-18T02:53:01.361691Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreVideo Changes for Objective-C

### CoreVideo

#### CVBase.h

Added #def COREVIDEO_DECLARE_NULLABILITYAdded #def COREVIDEO_SUPPORTS_IOSURFACE_PREFETCHAdded #def COREVIDEO_USE_DERIVED_ENUMS_FOR_CONSTANTSAdded #def CV_BRIDGED_TYPEAdded #def CV_NONNULLAdded #def CV_NULLABLEAdded #def CV_RELEASES_ARGUMENTAdded #def CV_RETURNS_RETAINED_PARAMETER

#### CVBuffer.h

Modified [CVBufferGetAttachment()](https://developer.apple.com/documentation/corevideo/1457103-cvbuffergetattachment)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CVBufferGetAttachment (     CVBufferRef buffer,     CFStringRef key,     CVAttachmentMode *attachmentMode ); ``` |
| To | ``` CFTypeRef _Nullable CVBufferGetAttachment (     CVBufferRef _Nonnull buffer,     CFStringRef _Nonnull key,     CVAttachmentMode * _Nullable attachmentMode ); ``` |

Modified [CVBufferGetAttachments()](https://developer.apple.com/documentation/corevideo/1457272-cvbuffergetattachments)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVBufferGetAttachments (     CVBufferRef buffer,     CVAttachmentMode attachmentMode ); ``` |
| To | ``` CFDictionaryRef _Nullable CVBufferGetAttachments (     CVBufferRef _Nonnull buffer,     CVAttachmentMode attachmentMode ); ``` |

Modified [CVBufferPropagateAttachments()](https://developer.apple.com/documentation/corevideo/1457132-cvbufferpropagateattachments)

|  | Declaration |
| --- | --- |
| From | ``` void CVBufferPropagateAttachments (     CVBufferRef sourceBuffer,     CVBufferRef destinationBuffer ); ``` |
| To | ``` void CVBufferPropagateAttachments (     CVBufferRef _Nonnull sourceBuffer,     CVBufferRef _Nonnull destinationBuffer ); ``` |

Modified [CVBufferRelease()](https://developer.apple.com/documentation/corevideo/1535816-cvbufferrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVBufferRelease (     CVBufferRef buffer ); ``` |
| To | ``` void CVBufferRelease (     CVBufferRef _Nullable buffer ); ``` |

Modified [CVBufferRemoveAllAttachments()](https://developer.apple.com/documentation/corevideo/1457268-cvbufferremoveallattachments)

|  | Declaration |
| --- | --- |
| From | ``` void CVBufferRemoveAllAttachments (     CVBufferRef buffer ); ``` |
| To | ``` void CVBufferRemoveAllAttachments (     CVBufferRef _Nonnull buffer ); ``` |

Modified [CVBufferRemoveAttachment()](https://developer.apple.com/documentation/corevideo/1456862-cvbufferremoveattachment)

|  | Declaration |
| --- | --- |
| From | ``` void CVBufferRemoveAttachment (     CVBufferRef buffer,     CFStringRef key ); ``` |
| To | ``` void CVBufferRemoveAttachment (     CVBufferRef _Nonnull buffer,     CFStringRef _Nonnull key ); ``` |

Modified [CVBufferRetain()](https://developer.apple.com/documentation/corevideo/1535810-cvbufferretain)

|  | Declaration |
| --- | --- |
| From | ``` CVBufferRef CVBufferRetain (     CVBufferRef buffer ); ``` |
| To | ``` CVBufferRef _Nullable CVBufferRetain (     CVBufferRef _Nullable buffer ); ``` |

Modified [CVBufferSetAttachment()](https://developer.apple.com/documentation/corevideo/1456974-cvbuffersetattachment)

|  | Declaration |
| --- | --- |
| From | ``` void CVBufferSetAttachment (     CVBufferRef buffer,     CFStringRef key,     CFTypeRef value,     CVAttachmentMode attachmentMode ); ``` |
| To | ``` void CVBufferSetAttachment (     CVBufferRef _Nonnull buffer,     CFStringRef _Nonnull key,     CFTypeRef _Nonnull value,     CVAttachmentMode attachmentMode ); ``` |

Modified [CVBufferSetAttachments()](https://developer.apple.com/documentation/corevideo/1457076-cvbuffersetattachments)

|  | Declaration |
| --- | --- |
| From | ``` void CVBufferSetAttachments (     CVBufferRef buffer,     CFDictionaryRef theAttachments,     CVAttachmentMode attachmentMode ); ``` |
| To | ``` void CVBufferSetAttachments (     CVBufferRef _Nonnull buffer,     CFDictionaryRef _Nonnull theAttachments,     CVAttachmentMode attachmentMode ); ``` |

#### CVDisplayLink.h

Added [CVDisplayLinkOutputHandler](https://developer.apple.com/documentation/corevideo/cvdisplaylinkoutputhandler)Added [CVDisplayLinkSetOutputHandler()](https://developer.apple.com/documentation/corevideo/1456927-cvdisplaylinksetoutputhandler)Modified [CVDisplayLinkCreateWithActiveCGDisplays()](https://developer.apple.com/documentation/corevideo/1456863-cvdisplaylinkcreatewithactivecgd)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkCreateWithActiveCGDisplays (     CVDisplayLinkRef *displayLinkOut ); ``` |
| To | ``` CVReturn CVDisplayLinkCreateWithActiveCGDisplays (     CVDisplayLinkRef  _Nullable * _Nonnull displayLinkOut ); ``` |

Modified [CVDisplayLinkCreateWithCGDisplay()](https://developer.apple.com/documentation/corevideo/1456981-cvdisplaylinkcreatewithcgdisplay)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkCreateWithCGDisplay (     CGDirectDisplayID displayID,     CVDisplayLinkRef *displayLinkOut ); ``` |
| To | ``` CVReturn CVDisplayLinkCreateWithCGDisplay (     CGDirectDisplayID displayID,     CVDisplayLinkRef  _Nullable * _Nonnull displayLinkOut ); ``` |

Modified [CVDisplayLinkCreateWithCGDisplays()](https://developer.apple.com/documentation/corevideo/1456752-cvdisplaylinkcreatewithcgdisplay)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkCreateWithCGDisplays (     CGDirectDisplayID *displayArray,     CFIndex count,     CVDisplayLinkRef *displayLinkOut ); ``` |
| To | ``` CVReturn CVDisplayLinkCreateWithCGDisplays (     CGDirectDisplayID * _Nonnull displayArray,     CFIndex count,     CVDisplayLinkRef  _Nullable * _Nonnull displayLinkOut ); ``` |

Modified [CVDisplayLinkCreateWithOpenGLDisplayMask()](https://developer.apple.com/documentation/corevideo/1456966-cvdisplaylinkcreatewithopengldis)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkCreateWithOpenGLDisplayMask (     CGOpenGLDisplayMask mask,     CVDisplayLinkRef *displayLinkOut ); ``` |
| To | ``` CVReturn CVDisplayLinkCreateWithOpenGLDisplayMask (     CGOpenGLDisplayMask mask,     CVDisplayLinkRef  _Nullable * _Nonnull displayLinkOut ); ``` |

Modified [CVDisplayLinkGetActualOutputVideoRefreshPeriod()](https://developer.apple.com/documentation/corevideo/1457155-cvdisplaylinkgetactualoutputvide)

|  | Declaration |
| --- | --- |
| From | ``` double CVDisplayLinkGetActualOutputVideoRefreshPeriod (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` double CVDisplayLinkGetActualOutputVideoRefreshPeriod (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkGetCurrentCGDisplay()](https://developer.apple.com/documentation/corevideo/1456835-cvdisplaylinkgetcurrentcgdisplay)

|  | Declaration |
| --- | --- |
| From | ``` CGDirectDisplayID CVDisplayLinkGetCurrentCGDisplay (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` CGDirectDisplayID CVDisplayLinkGetCurrentCGDisplay (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkGetCurrentTime()](https://developer.apple.com/documentation/corevideo/1457044-cvdisplaylinkgetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkGetCurrentTime (     CVDisplayLinkRef displayLink,     CVTimeStamp *outTime ); ``` |
| To | ``` CVReturn CVDisplayLinkGetCurrentTime (     CVDisplayLinkRef _Nonnull displayLink,     CVTimeStamp * _Nonnull outTime ); ``` |

Modified [CVDisplayLinkGetNominalOutputVideoRefreshPeriod()](https://developer.apple.com/documentation/corevideo/1456870-cvdisplaylinkgetnominaloutputvid)

|  | Declaration |
| --- | --- |
| From | ``` CVTime CVDisplayLinkGetNominalOutputVideoRefreshPeriod (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` CVTime CVDisplayLinkGetNominalOutputVideoRefreshPeriod (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkGetOutputVideoLatency()](https://developer.apple.com/documentation/corevideo/1456783-cvdisplaylinkgetoutputvideolaten)

|  | Declaration |
| --- | --- |
| From | ``` CVTime CVDisplayLinkGetOutputVideoLatency (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` CVTime CVDisplayLinkGetOutputVideoLatency (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkIsRunning()](https://developer.apple.com/documentation/corevideo/1456999-cvdisplaylinkisrunning)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CVDisplayLinkIsRunning (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` Boolean CVDisplayLinkIsRunning (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkRelease()](https://developer.apple.com/documentation/corevideo/1574569-cvdisplaylinkrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVDisplayLinkRelease (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` void CVDisplayLinkRelease (     CVDisplayLinkRef _Nullable displayLink ); ``` |

Modified [CVDisplayLinkRetain()](https://developer.apple.com/documentation/corevideo/1574570-cvdisplaylinkretain)

|  | Declaration |
| --- | --- |
| From | ``` CVDisplayLinkRef CVDisplayLinkRetain (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` CVDisplayLinkRef _Nullable CVDisplayLinkRetain (     CVDisplayLinkRef _Nullable displayLink ); ``` |

Modified [CVDisplayLinkSetCurrentCGDisplay()](https://developer.apple.com/documentation/corevideo/1456768-cvdisplaylinksetcurrentcgdisplay)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkSetCurrentCGDisplay (     CVDisplayLinkRef displayLink,     CGDirectDisplayID displayID ); ``` |
| To | ``` CVReturn CVDisplayLinkSetCurrentCGDisplay (     CVDisplayLinkRef _Nonnull displayLink,     CGDirectDisplayID displayID ); ``` |

Modified [CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext()](https://developer.apple.com/documentation/corevideo/1457164-cvdisplaylinksetcurrentcgdisplay)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext (     CVDisplayLinkRef displayLink,     CGLContextObj cglContext,     CGLPixelFormatObj cglPixelFormat ); ``` |
| To | ``` CVReturn CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext (     CVDisplayLinkRef _Nonnull displayLink,     CGLContextObj _Nonnull cglContext,     CGLPixelFormatObj _Nonnull cglPixelFormat ); ``` |

Modified [CVDisplayLinkSetOutputCallback()](https://developer.apple.com/documentation/corevideo/1457096-cvdisplaylinksetoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkSetOutputCallback (     CVDisplayLinkRef displayLink,     CVDisplayLinkOutputCallback callback,     void *userInfo ); ``` |
| To | ``` CVReturn CVDisplayLinkSetOutputCallback (     CVDisplayLinkRef _Nonnull displayLink,     CVDisplayLinkOutputCallback _Nonnull callback,     void * _Nullable userInfo ); ``` |

Modified [CVDisplayLinkStart()](https://developer.apple.com/documentation/corevideo/1457193-cvdisplaylinkstart)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkStart (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` CVReturn CVDisplayLinkStart (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkStop()](https://developer.apple.com/documentation/corevideo/1457281-cvdisplaylinkstop)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkStop (     CVDisplayLinkRef displayLink ); ``` |
| To | ``` CVReturn CVDisplayLinkStop (     CVDisplayLinkRef _Nonnull displayLink ); ``` |

Modified [CVDisplayLinkTranslateTime()](https://developer.apple.com/documentation/corevideo/1456882-cvdisplaylinktranslatetime)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVDisplayLinkTranslateTime (     CVDisplayLinkRef displayLink,     const CVTimeStamp *inTime,     CVTimeStamp *outTime ); ``` |
| To | ``` CVReturn CVDisplayLinkTranslateTime (     CVDisplayLinkRef _Nonnull displayLink,     const CVTimeStamp * _Nonnull inTime,     CVTimeStamp * _Nonnull outTime ); ``` |

#### CVImageBuffer.h

Added [kCVImageBufferColorPrimaries_DCI_P3](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_dci_p3)Added [kCVImageBufferColorPrimaries_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_itu_r_2020)Added [kCVImageBufferColorPrimaries_P3_D65](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_p3_d65)Added [kCVImageBufferTransferFunction_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_itu_r_2020)Added [kCVImageBufferYCbCrMatrix_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_itu_r_2020)Modified [CVImageBufferCreateColorSpaceFromAttachments()](https://developer.apple.com/documentation/corevideo/1418288-cvimagebuffercreatecolorspacefro)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CVImageBufferCreateColorSpaceFromAttachments (     CFDictionaryRef attachments ); ``` |
| To | ``` CGColorSpaceRef _Nullable CVImageBufferCreateColorSpaceFromAttachments (     CFDictionaryRef _Nonnull attachments ); ``` |

Modified [CVImageBufferGetCleanRect()](https://developer.apple.com/documentation/corevideo/1418328-cvimagebuffergetcleanrect)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CVImageBufferGetCleanRect (     CVImageBufferRef imageBuffer ); ``` |
| To | ``` CGRect CVImageBufferGetCleanRect (     CVImageBufferRef _Nonnull imageBuffer ); ``` |

Modified [CVImageBufferGetColorSpace()](https://developer.apple.com/documentation/corevideo/1418281-cvimagebuffergetcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CVImageBufferGetColorSpace (     CVImageBufferRef imageBuffer ); ``` |
| To | ``` CGColorSpaceRef _Nullable CVImageBufferGetColorSpace (     CVImageBufferRef _Nonnull imageBuffer ); ``` |

Modified [CVImageBufferGetDisplaySize()](https://developer.apple.com/documentation/corevideo/1418303-cvimagebuffergetdisplaysize)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CVImageBufferGetDisplaySize (     CVImageBufferRef imageBuffer ); ``` |
| To | ``` CGSize CVImageBufferGetDisplaySize (     CVImageBufferRef _Nonnull imageBuffer ); ``` |

Modified [CVImageBufferGetEncodedSize()](https://developer.apple.com/documentation/corevideo/1418350-cvimagebuffergetencodedsize)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CVImageBufferGetEncodedSize (     CVImageBufferRef imageBuffer ); ``` |
| To | ``` CGSize CVImageBufferGetEncodedSize (     CVImageBufferRef _Nonnull imageBuffer ); ``` |

Modified [CVImageBufferIsFlipped()](https://developer.apple.com/documentation/corevideo/1418308-cvimagebufferisflipped)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CVImageBufferIsFlipped (     CVImageBufferRef imageBuffer ); ``` |
| To | ``` Boolean CVImageBufferIsFlipped (     CVImageBufferRef _Nonnull imageBuffer ); ``` |

#### CVMetalTexture.h (Added)

Added [CVMetalTextureGetCleanTexCoords()](https://developer.apple.com/documentation/corevideo/1457089-cvmetaltexturegetcleantexcoords)Added [CVMetalTextureGetTexture()](https://developer.apple.com/documentation/corevideo/1456868-cvmetaltexturegettexture)Added [CVMetalTextureGetTypeID()](https://developer.apple.com/documentation/corevideo/1457175-cvmetaltexturegettypeid)Added [CVMetalTextureIsFlipped()](https://developer.apple.com/documentation/corevideo/1456841-cvmetaltextureisflipped)Added [CVMetalTextureRef](https://developer.apple.com/documentation/corevideo/cvmetaltextureref)

#### CVMetalTextureCache.h (Added)

Added [CVMetalTextureCacheCreate()](https://developer.apple.com/documentation/corevideo/1456774-cvmetaltexturecachecreate)Added [CVMetalTextureCacheCreateTextureFromImage()](https://developer.apple.com/documentation/corevideo/1456754-cvmetaltexturecachecreatetexture)Added [CVMetalTextureCacheFlush()](https://developer.apple.com/documentation/corevideo/1457001-cvmetaltexturecacheflush)Added [CVMetalTextureCacheGetTypeID()](https://developer.apple.com/documentation/corevideo/1456680-cvmetaltexturecachegettypeid)Added [CVMetalTextureCacheRef](https://developer.apple.com/documentation/corevideo/cvmetaltexturecache)Added [kCVMetalTextureCacheMaximumTextureAgeKey](https://developer.apple.com/documentation/corevideo/kcvmetaltexturecachemaximumtextureagekey)

#### CVOpenGLBuffer.h

Modified [CVOpenGLBufferAttach()](https://developer.apple.com/documentation/corevideo/1457237-cvopenglbufferattach)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVOpenGLBufferAttach (     CVOpenGLBufferRef openGLBuffer,     CGLContextObj cglContext,     GLenum face,     GLint level,     GLint screen ); ``` |
| To | ``` CVReturn CVOpenGLBufferAttach (     CVOpenGLBufferRef _Nonnull openGLBuffer,     CGLContextObj _Nonnull cglContext,     GLenum face,     GLint level,     GLint screen ); ``` |

Modified [CVOpenGLBufferCreate()](https://developer.apple.com/documentation/corevideo/1457145-cvopenglbuffercreate)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVOpenGLBufferCreate (     CFAllocatorRef allocator,     size_t width,     size_t height,     CFDictionaryRef attributes,     CVOpenGLBufferRef *bufferOut ); ``` |
| To | ``` CVReturn CVOpenGLBufferCreate (     CFAllocatorRef _Nullable allocator,     size_t width,     size_t height,     CFDictionaryRef _Nullable attributes,     CVOpenGLBufferRef  _Nullable * _Nonnull bufferOut ); ``` |

Modified [CVOpenGLBufferGetAttributes()](https://developer.apple.com/documentation/corevideo/1456838-cvopenglbuffergetattributes)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVOpenGLBufferGetAttributes (     CVOpenGLBufferRef openGLBuffer ); ``` |
| To | ``` CFDictionaryRef _Nullable CVOpenGLBufferGetAttributes (     CVOpenGLBufferRef _Nonnull openGLBuffer ); ``` |

Modified [CVOpenGLBufferRelease()](https://developer.apple.com/documentation/corevideo/1519779-cvopenglbufferrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVOpenGLBufferRelease (     CVOpenGLBufferRef buffer ); ``` |
| To | ``` void CVOpenGLBufferRelease (     CVOpenGLBufferRef _Nullable buffer ); ``` |

Modified [CVOpenGLBufferRetain()](https://developer.apple.com/documentation/corevideo/1519777-cvopenglbufferretain)

|  | Declaration |
| --- | --- |
| From | ``` CVOpenGLBufferRef CVOpenGLBufferRetain (     CVOpenGLBufferRef buffer ); ``` |
| To | ``` CVOpenGLBufferRef _Nullable CVOpenGLBufferRetain (     CVOpenGLBufferRef _Nullable buffer ); ``` |

#### CVOpenGLBufferPool.h

Modified [CVOpenGLBufferPoolCreate()](https://developer.apple.com/documentation/corevideo/1456995-cvopenglbufferpoolcreate)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVOpenGLBufferPoolCreate (     CFAllocatorRef allocator,     CFDictionaryRef poolAttributes,     CFDictionaryRef openGLBufferAttributes,     CVOpenGLBufferPoolRef *poolOut ); ``` |
| To | ``` CVReturn CVOpenGLBufferPoolCreate (     CFAllocatorRef _Nullable allocator,     CFDictionaryRef _Nullable poolAttributes,     CFDictionaryRef _Nullable openGLBufferAttributes,     CVOpenGLBufferPoolRef  _Nullable * _Nonnull poolOut ); ``` |

Modified [CVOpenGLBufferPoolCreateOpenGLBuffer()](https://developer.apple.com/documentation/corevideo/1457251-cvopenglbufferpoolcreateopenglbu)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVOpenGLBufferPoolCreateOpenGLBuffer (     CFAllocatorRef allocator,     CVOpenGLBufferPoolRef openGLBufferPool,     CVOpenGLBufferRef *openGLBufferOut ); ``` |
| To | ``` CVReturn CVOpenGLBufferPoolCreateOpenGLBuffer (     CFAllocatorRef _Nullable allocator,     CVOpenGLBufferPoolRef _Nonnull openGLBufferPool,     CVOpenGLBufferRef  _Nullable * _Nonnull openGLBufferOut ); ``` |

Modified [CVOpenGLBufferPoolGetAttributes()](https://developer.apple.com/documentation/corevideo/1456668-cvopenglbufferpoolgetattributes)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVOpenGLBufferPoolGetAttributes (     CVOpenGLBufferPoolRef pool ); ``` |
| To | ``` CFDictionaryRef _Nullable CVOpenGLBufferPoolGetAttributes (     CVOpenGLBufferPoolRef _Nonnull pool ); ``` |

Modified [CVOpenGLBufferPoolGetOpenGLBufferAttributes()](https://developer.apple.com/documentation/corevideo/1457266-cvopenglbufferpoolgetopenglbuffe)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVOpenGLBufferPoolGetOpenGLBufferAttributes (     CVOpenGLBufferPoolRef pool ); ``` |
| To | ``` CFDictionaryRef _Nullable CVOpenGLBufferPoolGetOpenGLBufferAttributes (     CVOpenGLBufferPoolRef _Nonnull pool ); ``` |

Modified [CVOpenGLBufferPoolRelease()](https://developer.apple.com/documentation/corevideo/1557376-cvopenglbufferpoolrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVOpenGLBufferPoolRelease (     CVOpenGLBufferPoolRef openGLBufferPool ); ``` |
| To | ``` void CVOpenGLBufferPoolRelease (     CVOpenGLBufferPoolRef _Nullable openGLBufferPool ); ``` |

Modified [CVOpenGLBufferPoolRetain()](https://developer.apple.com/documentation/corevideo/1557377-cvopenglbufferpoolretain)

|  | Declaration |
| --- | --- |
| From | ``` CVOpenGLBufferPoolRef CVOpenGLBufferPoolRetain (     CVOpenGLBufferPoolRef openGLBufferPool ); ``` |
| To | ``` CVOpenGLBufferPoolRef _Nullable CVOpenGLBufferPoolRetain (     CVOpenGLBufferPoolRef _Nullable openGLBufferPool ); ``` |

#### CVOpenGLTexture.h

Modified [CVOpenGLTextureGetCleanTexCoords()](https://developer.apple.com/documentation/corevideo/1457224-cvopengltexturegetcleantexcoords)

|  | Declaration |
| --- | --- |
| From | ``` void CVOpenGLTextureGetCleanTexCoords (     CVOpenGLTextureRef image,     GLfloat lowerLeft[2],     GLfloat lowerRight[2],     GLfloat upperRight[2],     GLfloat upperLeft[2] ); ``` |
| To | ``` void CVOpenGLTextureGetCleanTexCoords (     CVOpenGLTextureRef _Nonnull image,     GLfloat lowerLeft[2],     GLfloat lowerRight[2],     GLfloat upperRight[2],     GLfloat upperLeft[2] ); ``` |

Modified [CVOpenGLTextureGetName()](https://developer.apple.com/documentation/corevideo/1456682-cvopengltexturegetname)

|  | Declaration |
| --- | --- |
| From | ``` GLuint CVOpenGLTextureGetName (     CVOpenGLTextureRef image ); ``` |
| To | ``` GLuint CVOpenGLTextureGetName (     CVOpenGLTextureRef _Nonnull image ); ``` |

Modified [CVOpenGLTextureGetTarget()](https://developer.apple.com/documentation/corevideo/1456970-cvopengltexturegettarget)

|  | Declaration |
| --- | --- |
| From | ``` GLenum CVOpenGLTextureGetTarget (     CVOpenGLTextureRef image ); ``` |
| To | ``` GLenum CVOpenGLTextureGetTarget (     CVOpenGLTextureRef _Nonnull image ); ``` |

Modified [CVOpenGLTextureIsFlipped()](https://developer.apple.com/documentation/corevideo/1456725-cvopengltextureisflipped)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CVOpenGLTextureIsFlipped (     CVOpenGLTextureRef image ); ``` |
| To | ``` Boolean CVOpenGLTextureIsFlipped (     CVOpenGLTextureRef _Nonnull image ); ``` |

Modified [CVOpenGLTextureRelease()](https://developer.apple.com/documentation/corevideo/1585810-cvopengltexturerelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVOpenGLTextureRelease (     CVOpenGLTextureRef texture ); ``` |
| To | ``` void CVOpenGLTextureRelease (     CVOpenGLTextureRef _Nullable texture ); ``` |

Modified [CVOpenGLTextureRetain()](https://developer.apple.com/documentation/corevideo/1585809-cvopengltextureretain)

|  | Declaration |
| --- | --- |
| From | ``` CVOpenGLTextureRef CVOpenGLTextureRetain (     CVOpenGLTextureRef texture ); ``` |
| To | ``` CVOpenGLTextureRef _Nullable CVOpenGLTextureRetain (     CVOpenGLTextureRef _Nullable texture ); ``` |

#### CVOpenGLTextureCache.h

Modified [CVOpenGLTextureCacheCreate()](https://developer.apple.com/documentation/corevideo/1420172-cvopengltexturecachecreate)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVOpenGLTextureCacheCreate (     CFAllocatorRef allocator,     CFDictionaryRef cacheAttributes,     CGLContextObj cglContext,     CGLPixelFormatObj cglPixelFormat,     CFDictionaryRef textureAttributes,     CVOpenGLTextureCacheRef *cacheOut ); ``` |
| To | ``` CVReturn CVOpenGLTextureCacheCreate (     CFAllocatorRef _Nullable allocator,     CFDictionaryRef _Nullable cacheAttributes,     CGLContextObj _Nonnull cglContext,     CGLPixelFormatObj _Nonnull cglPixelFormat,     CFDictionaryRef _Nullable textureAttributes,     CVOpenGLTextureCacheRef  _Nullable * _Nonnull cacheOut ); ``` |

Modified [CVOpenGLTextureCacheCreateTextureFromImage()](https://developer.apple.com/documentation/corevideo/1420178-cvopengltexturecachecreatetextur)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVOpenGLTextureCacheCreateTextureFromImage (     CFAllocatorRef allocator,     CVOpenGLTextureCacheRef textureCache,     CVImageBufferRef sourceImage,     CFDictionaryRef attributes,     CVOpenGLTextureRef *textureOut ); ``` |
| To | ``` CVReturn CVOpenGLTextureCacheCreateTextureFromImage (     CFAllocatorRef _Nullable allocator,     CVOpenGLTextureCacheRef _Nonnull textureCache,     CVImageBufferRef _Nonnull sourceImage,     CFDictionaryRef _Nullable attributes,     CVOpenGLTextureRef  _Nullable * _Nonnull textureOut ); ``` |

Modified [CVOpenGLTextureCacheFlush()](https://developer.apple.com/documentation/corevideo/1420184-cvopengltexturecacheflush)

|  | Declaration |
| --- | --- |
| From | ``` void CVOpenGLTextureCacheFlush (     CVOpenGLTextureCacheRef textureCache,     CVOptionFlags options ); ``` |
| To | ``` void CVOpenGLTextureCacheFlush (     CVOpenGLTextureCacheRef _Nonnull textureCache,     CVOptionFlags options ); ``` |

Modified [CVOpenGLTextureCacheRelease()](https://developer.apple.com/documentation/corevideo/1420186-cvopengltexturecacherelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVOpenGLTextureCacheRelease (     CVOpenGLTextureCacheRef textureCache ); ``` |
| To | ``` void CVOpenGLTextureCacheRelease (     CVOpenGLTextureCacheRef _Nullable textureCache ); ``` |

Modified [CVOpenGLTextureCacheRetain()](https://developer.apple.com/documentation/corevideo/1420180-cvopengltexturecacheretain)

|  | Declaration |
| --- | --- |
| From | ``` CVOpenGLTextureCacheRef CVOpenGLTextureCacheRetain (     CVOpenGLTextureCacheRef textureCache ); ``` |
| To | ``` CVOpenGLTextureCacheRef _Nullable CVOpenGLTextureCacheRetain (     CVOpenGLTextureCacheRef _Nullable textureCache ); ``` |

#### CVPixelBuffer.h

Removed CVPixelBufferLockFlagsAdded [CVPixelBufferLockFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)Added [kCVPixelBufferMetalCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbuffermetalcompatibilitykey)Added [kCVPixelBufferOpenGLTextureCacheCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopengltexturecachecompatibilitykey)Modified [CVPixelBufferCreate()](https://developer.apple.com/documentation/corevideo/1456758-cvpixelbuffercreate)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferCreate (     CFAllocatorRef allocator,     size_t width,     size_t height,     OSType pixelFormatType,     CFDictionaryRef pixelBufferAttributes,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` CVReturn CVPixelBufferCreate (     CFAllocatorRef _Nullable allocator,     size_t width,     size_t height,     OSType pixelFormatType,     CFDictionaryRef _Nullable pixelBufferAttributes,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [CVPixelBufferCreateResolvedAttributesDictionary()](https://developer.apple.com/documentation/corevideo/1457233-cvpixelbuffercreateresolvedattri)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferCreateResolvedAttributesDictionary (     CFAllocatorRef allocator,     CFArrayRef attributes,     CFDictionaryRef *resolvedDictionaryOut ); ``` |
| To | ``` CVReturn CVPixelBufferCreateResolvedAttributesDictionary (     CFAllocatorRef _Nullable allocator,     CFArrayRef _Nullable attributes,     CFDictionaryRef  _Nullable * _Nonnull resolvedDictionaryOut ); ``` |

Modified [CVPixelBufferCreateWithBytes()](https://developer.apple.com/documentation/corevideo/1456979-cvpixelbuffercreatewithbytes)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferCreateWithBytes (     CFAllocatorRef allocator,     size_t width,     size_t height,     OSType pixelFormatType,     void *baseAddress,     size_t bytesPerRow,     CVPixelBufferReleaseBytesCallback releaseCallback,     void *releaseRefCon,     CFDictionaryRef pixelBufferAttributes,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` CVReturn CVPixelBufferCreateWithBytes (     CFAllocatorRef _Nullable allocator,     size_t width,     size_t height,     OSType pixelFormatType,     void * _Nonnull baseAddress,     size_t bytesPerRow,     CVPixelBufferReleaseBytesCallback _Nullable releaseCallback,     void * _Nullable releaseRefCon,     CFDictionaryRef _Nullable pixelBufferAttributes,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [CVPixelBufferCreateWithPlanarBytes()](https://developer.apple.com/documentation/corevideo/1456731-cvpixelbuffercreatewithplanarbyt)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferCreateWithPlanarBytes (     CFAllocatorRef allocator,     size_t width,     size_t height,     OSType pixelFormatType,     void *dataPtr,     size_t dataSize,     size_t numberOfPlanes,     void *planeBaseAddress[],     size_t planeWidth[],     size_t planeHeight[],     size_t planeBytesPerRow[],     CVPixelBufferReleasePlanarBytesCallback releaseCallback,     void *releaseRefCon,     CFDictionaryRef pixelBufferAttributes,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` CVReturn CVPixelBufferCreateWithPlanarBytes (     CFAllocatorRef _Nullable allocator,     size_t width,     size_t height,     OSType pixelFormatType,     void * _Nullable dataPtr,     size_t dataSize,     size_t numberOfPlanes,     void * _Nullable planeBaseAddress[],     size_t planeWidth[],     size_t planeHeight[],     size_t planeBytesPerRow[],     CVPixelBufferReleasePlanarBytesCallback _Nullable releaseCallback,     void * _Nullable releaseRefCon,     CFDictionaryRef _Nullable pixelBufferAttributes,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [CVPixelBufferFillExtendedPixels()](https://developer.apple.com/documentation/corevideo/1457265-cvpixelbufferfillextendedpixels)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferFillExtendedPixels (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` CVReturn CVPixelBufferFillExtendedPixels (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetBaseAddress()](https://developer.apple.com/documentation/corevideo/1457115-cvpixelbuffergetbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` void * CVPixelBufferGetBaseAddress (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` void * _Nullable CVPixelBufferGetBaseAddress (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetBaseAddressOfPlane()](https://developer.apple.com/documentation/corevideo/1456821-cvpixelbuffergetbaseaddressofpla)

|  | Declaration |
| --- | --- |
| From | ``` void * CVPixelBufferGetBaseAddressOfPlane (     CVPixelBufferRef pixelBuffer,     size_t planeIndex ); ``` |
| To | ``` void * _Nullable CVPixelBufferGetBaseAddressOfPlane (     CVPixelBufferRef _Nonnull pixelBuffer,     size_t planeIndex ); ``` |

Modified [CVPixelBufferGetBytesPerRow()](https://developer.apple.com/documentation/corevideo/1456964-cvpixelbuffergetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetBytesPerRow (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` size_t CVPixelBufferGetBytesPerRow (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetBytesPerRowOfPlane()](https://developer.apple.com/documentation/corevideo/1456711-cvpixelbuffergetbytesperrowofpla)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetBytesPerRowOfPlane (     CVPixelBufferRef pixelBuffer,     size_t planeIndex ); ``` |
| To | ``` size_t CVPixelBufferGetBytesPerRowOfPlane (     CVPixelBufferRef _Nonnull pixelBuffer,     size_t planeIndex ); ``` |

Modified [CVPixelBufferGetDataSize()](https://developer.apple.com/documentation/corevideo/1457195-cvpixelbuffergetdatasize)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetDataSize (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` size_t CVPixelBufferGetDataSize (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetExtendedPixels()](https://developer.apple.com/documentation/corevideo/1457029-cvpixelbuffergetextendedpixels)

|  | Declaration |
| --- | --- |
| From | ``` void CVPixelBufferGetExtendedPixels (     CVPixelBufferRef pixelBuffer,     size_t *extraColumnsOnLeft,     size_t *extraColumnsOnRight,     size_t *extraRowsOnTop,     size_t *extraRowsOnBottom ); ``` |
| To | ``` void CVPixelBufferGetExtendedPixels (     CVPixelBufferRef _Nonnull pixelBuffer,     size_t * _Nullable extraColumnsOnLeft,     size_t * _Nullable extraColumnsOnRight,     size_t * _Nullable extraRowsOnTop,     size_t * _Nullable extraRowsOnBottom ); ``` |

Modified [CVPixelBufferGetHeight()](https://developer.apple.com/documentation/corevideo/1456666-cvpixelbuffergetheight)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetHeight (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` size_t CVPixelBufferGetHeight (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetHeightOfPlane()](https://developer.apple.com/documentation/corevideo/1456698-cvpixelbuffergetheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetHeightOfPlane (     CVPixelBufferRef pixelBuffer,     size_t planeIndex ); ``` |
| To | ``` size_t CVPixelBufferGetHeightOfPlane (     CVPixelBufferRef _Nonnull pixelBuffer,     size_t planeIndex ); ``` |

Modified [CVPixelBufferGetPixelFormatType()](https://developer.apple.com/documentation/corevideo/1456851-cvpixelbuffergetpixelformattype)

|  | Declaration |
| --- | --- |
| From | ``` OSType CVPixelBufferGetPixelFormatType (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` OSType CVPixelBufferGetPixelFormatType (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetPlaneCount()](https://developer.apple.com/documentation/corevideo/1456976-cvpixelbuffergetplanecount)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetPlaneCount (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` size_t CVPixelBufferGetPlaneCount (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetWidth()](https://developer.apple.com/documentation/corevideo/1457241-cvpixelbuffergetwidth)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetWidth (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` size_t CVPixelBufferGetWidth (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferGetWidthOfPlane()](https://developer.apple.com/documentation/corevideo/1456830-cvpixelbuffergetwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` size_t CVPixelBufferGetWidthOfPlane (     CVPixelBufferRef pixelBuffer,     size_t planeIndex ); ``` |
| To | ``` size_t CVPixelBufferGetWidthOfPlane (     CVPixelBufferRef _Nonnull pixelBuffer,     size_t planeIndex ); ``` |

Modified [CVPixelBufferIsPlanar()](https://developer.apple.com/documentation/corevideo/1456805-cvpixelbufferisplanar)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CVPixelBufferIsPlanar (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` Boolean CVPixelBufferIsPlanar (     CVPixelBufferRef _Nonnull pixelBuffer ); ``` |

Modified [CVPixelBufferLockBaseAddress()](https://developer.apple.com/documentation/corevideo/1457128-cvpixelbufferlockbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferLockBaseAddress (     CVPixelBufferRef pixelBuffer,     CVOptionFlags lockFlags ); ``` |
| To | ``` CVReturn CVPixelBufferLockBaseAddress (     CVPixelBufferRef _Nonnull pixelBuffer,     CVPixelBufferLockFlags lockFlags ); ``` |

Modified [CVPixelBufferRelease()](https://developer.apple.com/documentation/corevideo/1563589-cvpixelbufferrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVPixelBufferRelease (     CVPixelBufferRef texture ); ``` |
| To | ``` void CVPixelBufferRelease (     CVPixelBufferRef _Nullable texture ); ``` |

Modified [CVPixelBufferRetain()](https://developer.apple.com/documentation/corevideo/1563590-cvpixelbufferretain)

|  | Declaration |
| --- | --- |
| From | ``` CVPixelBufferRef CVPixelBufferRetain (     CVPixelBufferRef texture ); ``` |
| To | ``` CVPixelBufferRef _Nullable CVPixelBufferRetain (     CVPixelBufferRef _Nullable texture ); ``` |

Modified [CVPixelBufferUnlockBaseAddress()](https://developer.apple.com/documentation/corevideo/1456843-cvpixelbufferunlockbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferUnlockBaseAddress (     CVPixelBufferRef pixelBuffer,     CVOptionFlags unlockFlags ); ``` |
| To | ``` CVReturn CVPixelBufferUnlockBaseAddress (     CVPixelBufferRef _Nonnull pixelBuffer,     CVPixelBufferLockFlags unlockFlags ); ``` |

#### CVPixelBufferIOSurface.h

Modified [CVPixelBufferCreateWithIOSurface()](https://developer.apple.com/documentation/corevideo/1456968-cvpixelbuffercreatewithiosurface)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferCreateWithIOSurface (     CFAllocatorRef allocator,     IOSurfaceRef surface,     CFDictionaryRef pixelBufferAttributes,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` CVReturn CVPixelBufferCreateWithIOSurface (     CFAllocatorRef _Nullable allocator,     IOSurfaceRef _Nonnull surface,     CFDictionaryRef _Nullable pixelBufferAttributes,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [CVPixelBufferGetIOSurface()](https://developer.apple.com/documentation/corevideo/1456690-cvpixelbuffergetiosurface)

|  | Declaration |
| --- | --- |
| From | ``` IOSurfaceRef CVPixelBufferGetIOSurface (     CVPixelBufferRef pixelBuffer ); ``` |
| To | ``` IOSurfaceRef _Nullable CVPixelBufferGetIOSurface (     CVPixelBufferRef _Nullable pixelBuffer ); ``` |

#### CVPixelBufferPool.h

Added [CVPixelBufferPoolFlush()](https://developer.apple.com/documentation/corevideo/1457177-cvpixelbufferpoolflush)Added [CVPixelBufferPoolFlushFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)Added [kCVPixelBufferPoolFlushExcessBuffers](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags/kcvpixelbufferpoolflushexcessbuffers)Modified [CVPixelBufferPoolCreate()](https://developer.apple.com/documentation/corevideo/1457094-cvpixelbufferpoolcreate)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferPoolCreate (     CFAllocatorRef allocator,     CFDictionaryRef poolAttributes,     CFDictionaryRef pixelBufferAttributes,     CVPixelBufferPoolRef *poolOut ); ``` |
| To | ``` CVReturn CVPixelBufferPoolCreate (     CFAllocatorRef _Nullable allocator,     CFDictionaryRef _Nullable poolAttributes,     CFDictionaryRef _Nullable pixelBufferAttributes,     CVPixelBufferPoolRef  _Nullable * _Nonnull poolOut ); ``` |

Modified [CVPixelBufferPoolCreatePixelBuffer()](https://developer.apple.com/documentation/corevideo/1456992-cvpixelbufferpoolcreatepixelbuff)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferPoolCreatePixelBuffer (     CFAllocatorRef allocator,     CVPixelBufferPoolRef pixelBufferPool,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` CVReturn CVPixelBufferPoolCreatePixelBuffer (     CFAllocatorRef _Nullable allocator,     CVPixelBufferPoolRef _Nonnull pixelBufferPool,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [CVPixelBufferPoolCreatePixelBufferWithAuxAttributes()](https://developer.apple.com/documentation/corevideo/1456899-cvpixelbufferpoolcreatepixelbuff)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferPoolCreatePixelBufferWithAuxAttributes (     CFAllocatorRef allocator,     CVPixelBufferPoolRef pixelBufferPool,     CFDictionaryRef auxAttributes,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` CVReturn CVPixelBufferPoolCreatePixelBufferWithAuxAttributes (     CFAllocatorRef _Nullable allocator,     CVPixelBufferPoolRef _Nonnull pixelBufferPool,     CFDictionaryRef _Nullable auxAttributes,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [CVPixelBufferPoolGetAttributes()](https://developer.apple.com/documentation/corevideo/1456983-cvpixelbufferpoolgetattributes)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVPixelBufferPoolGetAttributes (     CVPixelBufferPoolRef pool ); ``` |
| To | ``` CFDictionaryRef _Nullable CVPixelBufferPoolGetAttributes (     CVPixelBufferPoolRef _Nonnull pool ); ``` |

Modified [CVPixelBufferPoolGetPixelBufferAttributes()](https://developer.apple.com/documentation/corevideo/1457222-cvpixelbufferpoolgetpixelbuffera)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVPixelBufferPoolGetPixelBufferAttributes (     CVPixelBufferPoolRef pool ); ``` |
| To | ``` CFDictionaryRef _Nullable CVPixelBufferPoolGetPixelBufferAttributes (     CVPixelBufferPoolRef _Nonnull pool ); ``` |

Modified [CVPixelBufferPoolRelease()](https://developer.apple.com/documentation/corevideo/1577602-cvpixelbufferpoolrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CVPixelBufferPoolRelease (     CVPixelBufferPoolRef pixelBufferPool ); ``` |
| To | ``` void CVPixelBufferPoolRelease (     CVPixelBufferPoolRef _Nullable pixelBufferPool ); ``` |

Modified [CVPixelBufferPoolRetain()](https://developer.apple.com/documentation/corevideo/1577601-cvpixelbufferpoolretain)

|  | Declaration |
| --- | --- |
| From | ``` CVPixelBufferPoolRef CVPixelBufferPoolRetain (     CVPixelBufferPoolRef pixelBufferPool ); ``` |
| To | ``` CVPixelBufferPoolRef _Nullable CVPixelBufferPoolRetain (     CVPixelBufferPoolRef _Nullable pixelBufferPool ); ``` |

#### CVPixelFormatDescription.h

Added [kCVPixelFormatComponentRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange)Added [kCVPixelFormatComponentRange_FullRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_fullrange)Added [kCVPixelFormatComponentRange_VideoRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_videorange)Added [kCVPixelFormatComponentRange_WideRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_widerange)Modified [CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes()](https://developer.apple.com/documentation/corevideo/1456798-cvpixelformatdescriptionarraycre)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes (     CFAllocatorRef allocator ); ``` |
| To | ``` CFArrayRef _Nullable CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [CVPixelFormatDescriptionCreateWithPixelFormatType()](https://developer.apple.com/documentation/corevideo/1456807-cvpixelformatdescriptioncreatewi)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CVPixelFormatDescriptionCreateWithPixelFormatType (     CFAllocatorRef allocator,     OSType pixelFormat ); ``` |
| To | ``` CFDictionaryRef _Nullable CVPixelFormatDescriptionCreateWithPixelFormatType (     CFAllocatorRef _Nullable allocator,     OSType pixelFormat ); ``` |

Modified [CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType()](https://developer.apple.com/documentation/corevideo/1456721-cvpixelformatdescriptionregister)

|  | Declaration |
| --- | --- |
| From | ``` void CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType (     CFDictionaryRef description,     OSType pixelFormat ); ``` |
| To | ``` void CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType (     CFDictionaryRef _Nonnull description,     OSType pixelFormat ); ``` |

#### CVReturn.h

Added [kCVReturnUnsupported](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnunsupported)

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
