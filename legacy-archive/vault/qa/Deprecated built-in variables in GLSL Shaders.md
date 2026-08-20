---
title: Deprecated built-in variables in GLSL Shaders
apple_id: DTS40010084
resource_type: QA
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2010-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1679/_index.html
archived_at: '2026-07-18T02:33:46.525338Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1679

# Deprecated built-in variables in GLSL Shaders

## Q:  What is the list of deprecated built-in variables in GLSL shaders?

A: What is the list of deprecated built-in variables in GLSL shaders?

Using generic attributes, varyings, and uniforms is preferred to depending on the fixed-function built-in variables, which are not available with OpenGL ES 2.0 on iPhone OS and not recommended for use on Mac OS X. For example, instead of using `gl_ModelViewProjectionMatrix`, create your own `modelViewProjectionMatrix` variable.

The following lists the deprecated fixed-function built-in variables in GLSL shaders.

__Listing 1__  DEPRECATED attributes and varyings

```
gl_Color gl_SecondaryColor gl_Normal gl_Vertex gl_MultiTexCoord0 gl_MultiTexCoord1 gl_MultiTexCoord2 gl_MultiTexCoord3 gl_MultiTexCoord4 gl_MultiTexCoord5 gl_MultiTexCoord6 gl_MultiTexCoord7 gl_FogCoord
```


__Listing 2__  DEPRECATED uniforms

```
gl_ModelViewMatrix gl_ProjectionMatrix gl_ModelViewProjectionMatrix gl_TextureMatrix gl_NormalMatrix gl_ModelViewMatrixInverse gl_ProjectionMatrixInverse gl_ModelViewProjectionMatrixInverse gl_TextureMatrixInverse gl_ModelViewMatrixTranspose gl_ProjectionMatrixTranspose gl_ModelViewProjectionMatrixTranspose gl_TextureMatrixTranspose gl_ModelViewMatrixInverseTranspose gl_ProjectionMatrixInverseTranspose gl_ModelViewProjectionMatrixInverseTranspose gl_TextureMatrixInverseTranspose gl_NormalScale gl_ClipPlane gl_Point gl_MaterialParameters gl_LightSource gl_FrontLightModelProduct gl_BackLightModelProduct; gl_FrontLightProduct gl_BackLightProduct gl_TextureEnvColor gl_EyePlaneS gl_EyePlaneT gl_EyePlaneR gl_EyePlaneQ gl_ObjectPlaneS gl_ObjectPlaneT gl_ObjectPlaneR gl_ObjectPlaneQ gl_Fog
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-06-04 | New document that lists the fixed-function built-in variables discouraged from being used in GLSL shaders. |

