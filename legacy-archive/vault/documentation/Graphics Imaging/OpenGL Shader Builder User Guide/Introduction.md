---
title: OpenGL Shader Builder User Guide
apple_id: TP40006476
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLShaderBuilderUserGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:37:04.542862Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Getting%20Started.md)

# Introduction

OpenGL Shader Builder is a tool for developing and debugging programs for the graphics processing unit (GPU). It can help you visualize and preview shader objects without the complexity of surrounding code. Using it, you can:

- Get immediate feedback as you enter and modify GPU programs
- Explore the effect of changing texture parameters
- Track down link and compile errors
- Observe the effect of making changes to symbol values

Developers who are writing GPU programs will want to read this document to find out how to use OpenGL Shader Builder. You can use the shader builder with programs written with OpenGL Shading Language or with older-style ARB vertex and fragment programs. OpenGL Shader Builder also supports geometry shaders, a recent addition to the OpenGL specification.

This document is organized into the following chapters:

- [Getting Started](Getting%20Started.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzwfvbuqmrnknltc) gives an overview of the user interface and the main features of OpenGL Shader Builder.
- [Building Shaders](Building%20Shaders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzwfvbuqmznknltc) provides step-by-step instructions for the most common tasks you can accomplish.

You may want to consult these documents as you develop shaders for the GPU:

- [OpenGL Shading Language (PDF)](http://www.opengl.org/registry/doc/GLSLangSpec.Full.1.20.8.pdf) provides an overview of shaders and a complete reference to the language.
- [OpenGL Shading Language (GLSl) Quick Reference Guide (PDF)](http://www.opengl.org/sdk/libs/OpenSceneGraph/glsl_quickref.pdf) is a two-page list of symbols that includes cross-references to the full specification.

The following OpenGL specifications define the extensions that support GPU programs:

- [GL_EXT_geometry_shader4](http://developer.download.nvidia.com/opengl/specs/GL_EXT_geometry_shader4.txt) is for generating primitives.
- [GL_ARB_fragment_program](http://oss.sgi.com/projects/ogl-sample/registry/ARB/fragment_program.txt) is for processing fragments.
- [GL_ARB_vertex_program](http://oss.sgi.com/projects/ogl-sample/registry/ARB/vertex_program.txt) is for processing vertices.
[Next](Getting%20Started.md)

