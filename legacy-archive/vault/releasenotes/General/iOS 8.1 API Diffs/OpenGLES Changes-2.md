---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/OpenGLES.html
archived_at: '2026-07-18T02:56:15.371604Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# OpenGLES Changes

## OpenGLES

Modified EAGLContext.init(API: EAGLRenderingAPI)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(API api: EAGLRenderingAPI) ``` |
| To | ``` convenience init!(API api: EAGLRenderingAPI) ``` |

Modified EAGLContext.init(API: EAGLRenderingAPI, sharegroup: EAGLSharegroup!)

|  | Declaration |
| --- | --- |
| From | ``` init(API api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!) ``` |
| To | ``` init!(API api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!) ``` |

Modified EAGLContext.debugLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EAGLContext.multiThreaded

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified EAGLSharegroup.debugLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glActiveShaderProgramEXT(GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glAttachShader(GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBeginQuery(GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBeginQueryEXT(GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glBeginTransformFeedback(GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBindAttribLocation(GLuint, GLuint, UnsafePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBindBufferBase(GLenum, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBindBufferRange(GLenum, GLuint, GLuint, GLintptr, GLsizeiptr)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBindFramebuffer(GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBindProgramPipelineEXT(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glBindRenderbuffer(GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBindSampler(GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBindTransformFeedback(GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBindVertexArray(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glBindVertexArrayOES(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glBlendColor(GLfloat, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBlendEquation(GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBlendEquationSeparate(GLenum, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBlendEquationSeparateOES(GLenum, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified glBlendFuncSeparate(GLenum, GLenum, GLenum, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glBlendFuncSeparateOES(GLenum, GLenum, GLenum, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified glBlitFramebuffer(GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glCheckFramebufferStatus(GLenum) -> GLenum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glClearBufferfi(GLenum, GLint, GLfloat, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glClearBufferfv(GLenum, GLint, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glClearBufferiv(GLenum, GLint, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glClearBufferuiv(GLenum, GLint, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glClientWaitSync(GLsync, GLbitfield, GLuint64) -> GLenum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glClientWaitSyncAPPLE(GLsync, GLbitfield, GLuint64) -> GLenum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glCompileShader(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glCompressedTexImage3D(GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glCompressedTexSubImage3D(GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glCopyBufferSubData(GLenum, GLenum, GLintptr, GLintptr, GLsizeiptr)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glCopyTexSubImage3D(GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glCopyTextureLevelsAPPLE(GLuint, GLuint, GLint, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glCreateProgram() -> GLuint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glCreateShader(GLenum) -> GLuint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glCreateShaderProgramvEXT(GLenum, GLsizei, UnsafePointer<UnsafePointer<GLchar>>) -> GLuint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glDeleteFramebuffers(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glDeleteProgram(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glDeleteProgramPipelinesEXT(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glDeleteQueries(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDeleteQueriesEXT(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glDeleteRenderbuffers(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glDeleteSamplers(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDeleteShader(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glDeleteSync(GLsync)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDeleteSyncAPPLE(GLsync)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glDeleteTransformFeedbacks(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDeleteVertexArrays(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDeleteVertexArraysOES(GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glDetachShader(GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glDisableVertexAttribArray(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glDiscardFramebufferEXT(GLenum, GLsizei, UnsafePointer<GLenum>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glDrawArraysInstanced(GLenum, GLint, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDrawArraysInstancedEXT(GLenum, GLint, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDrawBuffers(GLsizei, UnsafePointer<GLenum>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDrawElementsInstanced(GLenum, GLsizei, GLenum, UnsafePointer<Void>, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDrawElementsInstancedEXT(GLenum, GLsizei, GLenum, UnsafePointer<Void>, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glDrawRangeElements(GLenum, GLuint, GLuint, GLsizei, GLenum, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glEnableVertexAttribArray(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glEndQuery(GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glEndQueryEXT(GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glEndTransformFeedback()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glFenceSync(GLenum, GLbitfield) -> GLsync

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glFenceSyncAPPLE(GLenum, GLbitfield) -> GLsync

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glFlushMappedBufferRange(GLenum, GLintptr, GLsizeiptr)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glFlushMappedBufferRangeEXT(GLenum, GLintptr, GLsizeiptr)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glFramebufferRenderbuffer(GLenum, GLenum, GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glFramebufferTexture2D(GLenum, GLenum, GLenum, GLuint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glFramebufferTextureLayer(GLenum, GLenum, GLuint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGenFramebuffers(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGenProgramPipelinesEXT(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGenQueries(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGenQueriesEXT(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGenRenderbuffers(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGenSamplers(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGenTransformFeedbacks(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGenVertexArrays(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGenVertexArraysOES(GLsizei, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glGenerateMipmap(GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetActiveAttrib(GLuint, GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLint>, UnsafeMutablePointer<GLenum>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetActiveUniform(GLuint, GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLint>, UnsafeMutablePointer<GLenum>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetActiveUniformBlockName(GLuint, GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetActiveUniformBlockiv(GLuint, GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetActiveUniformsiv(GLuint, GLsizei, UnsafePointer<GLuint>, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetAttachedShaders(GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetAttribLocation(GLuint, UnsafePointer<GLchar>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetBufferParameteri64v(GLenum, GLenum, UnsafeMutablePointer<GLint64>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetBufferPointerv(GLenum, GLenum, UnsafeMutablePointer<UnsafeMutablePointer<Void>>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetFragDataLocation(GLuint, UnsafePointer<GLchar>) -> GLint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetFramebufferAttachmentParameteriv(GLenum, GLenum, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetInteger64i_v(GLenum, GLuint, UnsafeMutablePointer<GLint64>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetInteger64v(GLenum, UnsafeMutablePointer<GLint64>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetInteger64vAPPLE(GLenum, UnsafeMutablePointer<GLint64>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glGetIntegeri_v(GLenum, GLuint, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetInternalformativ(GLenum, GLenum, GLenum, GLsizei, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetObjectLabelEXT(GLenum, GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGetProgramBinary(GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLenum>, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetProgramInfoLog(GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetProgramPipelineInfoLogEXT(GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGetProgramPipelineivEXT(GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGetProgramiv(GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetQueryObjectuiv(GLuint, GLenum, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetQueryObjectuivEXT(GLuint, GLenum, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGetQueryiv(GLenum, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetQueryivEXT(GLenum, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glGetRenderbufferParameteriv(GLenum, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetSamplerParameterfv(GLuint, GLenum, UnsafeMutablePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetSamplerParameteriv(GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetShaderInfoLog(GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetShaderPrecisionFormat(GLenum, GLenum, UnsafeMutablePointer<GLint>, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetShaderSource(GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetShaderiv(GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetStringi(GLenum, GLuint) -> UnsafePointer<GLubyte>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetSynciv(GLsync, GLenum, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetSyncivAPPLE(GLsync, GLenum, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glGetTransformFeedbackVarying(GLuint, GLuint, GLsizei, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLsizei>, UnsafeMutablePointer<GLenum>, UnsafeMutablePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetUniformBlockIndex(GLuint, UnsafePointer<GLchar>) -> GLuint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetUniformIndices(GLuint, GLsizei, UnsafePointer<UnsafePointer<GLchar>>, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetUniformLocation(GLuint, UnsafePointer<GLchar>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetUniformfv(GLuint, GLint, UnsafeMutablePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetUniformiv(GLuint, GLint, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetUniformuiv(GLuint, GLint, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetVertexAttribIiv(GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetVertexAttribIuiv(GLuint, GLenum, UnsafeMutablePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glGetVertexAttribPointerv(GLuint, GLenum, UnsafeMutablePointer<UnsafeMutablePointer<Void>>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetVertexAttribfv(GLuint, GLenum, UnsafeMutablePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glGetVertexAttribiv(GLuint, GLenum, UnsafeMutablePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glInsertEventMarkerEXT(GLsizei, UnsafePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glInvalidateFramebuffer(GLenum, GLsizei, UnsafePointer<GLenum>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glInvalidateSubFramebuffer(GLenum, GLsizei, UnsafePointer<GLenum>, GLint, GLint, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glIsFramebuffer(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glIsProgramPipelineEXT(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glIsQuery(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glIsQueryEXT(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glIsRenderbuffer(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glIsSampler(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glIsShader(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glIsSync(GLsync) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glIsSyncAPPLE(GLsync) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glIsTransformFeedback(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glIsVertexArray(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glIsVertexArrayOES(GLuint) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glLabelObjectEXT(GLenum, GLuint, GLsizei, UnsafePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glLinkProgram(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glMapBufferRange(GLenum, GLintptr, GLsizeiptr, GLbitfield) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glMapBufferRangeEXT(GLenum, GLintptr, GLsizeiptr, GLbitfield) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glPauseTransformFeedback()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glPopGroupMarkerEXT()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramBinary(GLuint, GLenum, UnsafePointer<Void>, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramParameteri(GLuint, GLenum, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramParameteriEXT(GLuint, GLenum, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform1fEXT(GLuint, GLint, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform1fvEXT(GLuint, GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform1iEXT(GLuint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform1ivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform1uiEXT(GLuint, GLint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform1uivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform2fEXT(GLuint, GLint, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform2fvEXT(GLuint, GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform2iEXT(GLuint, GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform2ivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform2uiEXT(GLuint, GLint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform2uivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform3fEXT(GLuint, GLint, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform3fvEXT(GLuint, GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform3iEXT(GLuint, GLint, GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform3ivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform3uiEXT(GLuint, GLint, GLuint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform3uivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform4fEXT(GLuint, GLint, GLfloat, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform4fvEXT(GLuint, GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform4iEXT(GLuint, GLint, GLint, GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform4ivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniform4uiEXT(GLuint, GLint, GLuint, GLuint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniform4uivEXT(GLuint, GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniformMatrix2fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniformMatrix2x3fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniformMatrix2x4fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniformMatrix3fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniformMatrix3x2fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniformMatrix3x4fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniformMatrix4fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glProgramUniformMatrix4x2fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glProgramUniformMatrix4x3fvEXT(GLuint, GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glPushGroupMarkerEXT(GLsizei, UnsafePointer<GLchar>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glReadBuffer(GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glReleaseShaderCompiler()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glRenderbufferStorage(GLenum, GLenum, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glRenderbufferStorageMultisample(GLenum, GLsizei, GLenum, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glRenderbufferStorageMultisampleAPPLE(GLenum, GLsizei, GLenum, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glResolveMultisampleFramebufferAPPLE()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified glResumeTransformFeedback()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glSamplerParameterf(GLuint, GLenum, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glSamplerParameterfv(GLuint, GLenum, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glSamplerParameteri(GLuint, GLenum, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glSamplerParameteriv(GLuint, GLenum, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glShaderBinary(GLsizei, UnsafePointer<GLuint>, GLenum, UnsafePointer<Void>, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glShaderSource(GLuint, GLsizei, UnsafePointer<UnsafePointer<GLchar>>, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glStencilFuncSeparate(GLenum, GLenum, GLint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glStencilMaskSeparate(GLenum, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glStencilOpSeparate(GLenum, GLenum, GLenum, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glTexImage3D(GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glTexStorage2D(GLenum, GLsizei, GLenum, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glTexStorage2DEXT(GLenum, GLsizei, GLenum, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified glTexStorage3D(GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glTexSubImage3D(GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glTransformFeedbackVaryings(GLuint, GLsizei, UnsafePointer<UnsafePointer<GLchar>>, GLenum)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform1f(GLint, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform1fv(GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform1i(GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform1iv(GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform1ui(GLint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform1uiv(GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform2f(GLint, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform2fv(GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform2i(GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform2iv(GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform2ui(GLint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform2uiv(GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform3f(GLint, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform3fv(GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform3i(GLint, GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform3iv(GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform3ui(GLint, GLuint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform3uiv(GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform4f(GLint, GLfloat, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform4fv(GLint, GLsizei, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform4i(GLint, GLint, GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform4iv(GLint, GLsizei, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniform4ui(GLint, GLuint, GLuint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniform4uiv(GLint, GLsizei, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformBlockBinding(GLuint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformMatrix2fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniformMatrix2x3fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformMatrix2x4fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformMatrix3fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniformMatrix3x2fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformMatrix3x4fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformMatrix4fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUniformMatrix4x2fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUniformMatrix4x3fv(GLint, GLsizei, GLboolean, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUnmapBuffer(GLenum) -> GLboolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glUseProgram(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glUseProgramStagesEXT(GLuint, GLbitfield, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glValidateProgram(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glValidateProgramPipelineEXT(GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified glVertexAttrib1f(GLuint, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib1fv(GLuint, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib2f(GLuint, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib2fv(GLuint, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib3f(GLuint, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib3fv(GLuint, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib4f(GLuint, GLfloat, GLfloat, GLfloat, GLfloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttrib4fv(GLuint, UnsafePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glVertexAttribDivisor(GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribDivisorEXT(GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribI4i(GLuint, GLint, GLint, GLint, GLint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribI4iv(GLuint, UnsafePointer<GLint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribI4ui(GLuint, GLuint, GLuint, GLuint, GLuint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribI4uiv(GLuint, UnsafePointer<GLuint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribIPointer(GLuint, GLint, GLenum, GLsizei, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glVertexAttribPointer(GLuint, GLint, GLenum, GLboolean, GLsizei, UnsafePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified glWaitSync(GLsync, GLbitfield, GLuint64)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified glWaitSyncAPPLE(GLsync, GLbitfield, GLuint64)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kEAGLColorFormatSRGBA8

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
