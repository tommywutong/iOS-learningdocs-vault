---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/renderer_h.html
archived_at: '2026-07-18T03:06:12.570046Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](fragmentShaderRecordGBuffer.fs.md)[Previous](matrixUtil.h.md)

# renderer.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The renderer class creates and draws the OpenGL shaders.
 */


#ifndef __RENDERER__
#define __RENDERER__

#import <OpenGL/gl3.h>
#import <OpenGL/gl3ext.h>
#import <GLKit/GLKMath.h>
#import <GLKit/GLKMatrixStack.h>
#include <stdint.h>
#include <stdio.h>
#include "GeoUtils.h"

const uint32_t kShaderCount = 5;
const uint32_t kNumMRT = 3; // multiple render targets (MRT)
const uint32_t kNumFBO = 1;
const uint32_t kNumTextures = 4;

enum
{
    kFinalImage,
    kPositionBuffer,
    kAlbedoBuffer,
    kNormalBuffer,
};

class OpenGLRenderer
{
    const GLubyte* rendererString;
    char* resourcePath;
    uint32_t width, height;
    mat4 cameraMatrix;
    GLint shaders[kShaderCount];
    GLint recordGBufferDataPass, deferredLightingPass, displayTextureContentsPass;
    GLuint fbos[kNumFBO];
    GLuint tex[kNumTextures];
    GLuint orientationMatrixLocation, cameraTransformLocation, colorLocation,
            normTexLocation, positionTexLocation,
            colorTexLocation,
            light1Pos, light1Color,
            light2Pos, light2Color,
            light3Pos, light3Color,
            light4Pos, light4Color;
    GLint projectionUniformIdx;


    //for visualization of the buffers
    GLint displayTexLocation;
    GLuint quadID, quadElementID;
    GLuint teapotVertexId, teapotNormalId, teapotElementId; //Lili

    GLuint cube_vertices, cube_indices;
    GLenum buffers[kNumMRT];
    uint8_t showBuffer;
    uint8_t animationStep, animate;
    float animationDelta;
    uint32_t kAnimationLoopValue;
    vec4 l1Pos, l2Pos, l3Pos, l4Pos;
    vec3 l1Color, l2Color, l3Color, l4Color;

public:
    OpenGLRenderer();
    OpenGLRenderer(const char* pathToResources, size_t len);
    ~OpenGLRenderer();
    const char* getRendererString()
    {
        return (const char*) rendererString;
    }
    bool setupQuad();
    bool setupTeapot();
    bool setupGL();
    void resizeViewport(uint32_t w, uint32_t h);
    void draw();
    void updateAnimations();
    void updateGBufferContents();
    void showPositionBuffer();
    void showNormalBuffer();
    void showAlbedoBuffer();
    void showFinalImage();
    void drawQuad();
    void attachShadersToProgram(GLint program, GLint vertShaderID, GLint fragShaderID);
    GLboolean linkAndValidateProgram(GLint program, GLint vertShaderID, GLint fragShaderID);
    GLshort loadShaders();
    GLboolean loadShaderFromFile(const char* shaderName, GLenum shaderType, GLint* shaderID);
    void setShowBuffer(uint8_t buf) 
    { 
        showBuffer = buf; 
    }
    void toggleAnimation()
    {
        animate = !animate;
    }
    void resetAnimation()
    {
        animationStep = 0;
    }
    void setAnimationDelta(float d)
    {
        animationDelta = d;
        kAnimationLoopValue = 360.0 / animationDelta;
    }
};

#endif
```

[Next](fragmentShaderRecordGBuffer.fs.md)[Previous](matrixUtil.h.md)

