---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/renderer_cpp.html
archived_at: '2026-07-18T03:06:12.303396Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](Document%20Revision%20History.md)[Previous](DeferredShadingAppDelegate.m.md)

# renderer.cpp

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The renderer class creates and draws the OpenGL shaders.
 */


#include "renderer.h"

extern "C" {
#include "matrixUtil.h"
}
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "teapot.h"

static inline const char * GetGLErrorString(GLenum error)
{
    const char *str;
    switch( error )
    {
        case GL_NO_ERROR:
            str = "GL_NO_ERROR";
            break;
        case GL_INVALID_ENUM:
            str = "GL_INVALID_ENUM";
            break;
        case GL_INVALID_VALUE:
            str = "GL_INVALID_VALUE";
            break;
        case GL_INVALID_OPERATION:
            str = "GL_INVALID_OPERATION";
            break;
#if defined __gl_h_ || defined __gl3_h_
        case GL_OUT_OF_MEMORY:
            str = "GL_OUT_OF_MEMORY";
            break;
        case GL_INVALID_FRAMEBUFFER_OPERATION:
            str = "GL_INVALID_FRAMEBUFFER_OPERATION";
            break;
#endif
#if defined __gl_h_
        case GL_STACK_OVERFLOW:
            str = "GL_STACK_OVERFLOW";
            break;
        case GL_STACK_UNDERFLOW:
            str = "GL_STACK_UNDERFLOW";
            break;
        case GL_TABLE_TOO_LARGE:
            str = "GL_TABLE_TOO_LARGE";
            break;
#endif
        default:
            str = "(ERROR: Unknown Error Enum)";
            break;
    }
    return str;
}

#define glError() { \
GLenum err = glGetError(); \
while (err != GL_NO_ERROR) { \
__builtin_printf("glError: %s caught at %s:%u\n", (char *)GetGLErrorString(err), __FILE__, __LINE__); \
assert(0 && "Dying..."); \
} \
}

#define VERTEX_SHADER_TRANSFORM_NAME "vertexShaderTransform.vs"
#define FRAGMENT_SHADER_RECORD_GBUFFER_NAME "fragmentShaderRecordGBuffer.fs"
#define PASSTHROUGH_NAME "passthrough.vs"
#define DEFERRED_LIGHTNING_NAME "deferredLighting.fs"
#define BUFFER_DISPLAY_NAME "bufferDisplay.fs"

#define BUFFER_OFFSET(i) ((char *)NULL + (i))

enum {Quad_VAO, Teapot_VAO, NumVAOs}; // Vertex array object names
GLuint VAOs[NumVAOs];

// Indexes to bind user-defined varying out fragment shader variables
enum {
    FRAG_POS_ATTRIB_IDX,
    FRAG_COLOR_ATTRIB_IDX,
    FRAG_NORMAL_ATTRIB_IDX
};

// Indicies to which we will set vertex array attibutes
enum {
    POS_ATTRIB_IDX,
    NORMAL_ATTRIB_IDX,
    TEXCOORD_ATTRIB_IDX
};

GLboolean loadShader(GLenum shaderType, const GLchar** shaderText, GLint* shaderID);
GLboolean linkShaders(GLint* program, GLint vertShaderID, GLint fragShaderID);

#pragma mark Constructor/Destructor

OpenGLRenderer::OpenGLRenderer(const char* pathToResources, size_t len)
{
    resourcePath = (char*) malloc(len+1);
    bzero(resourcePath, len+1);
    strncpy(resourcePath, pathToResources, len);
    rendererString = glGetString(GL_RENDERER);
    showBuffer = kFinalImage;
    animate = GL_FALSE;
    animationStep = 0;
    animationDelta = 1.5;
    kAnimationLoopValue = 360.0 / animationDelta;
}

OpenGLRenderer::~OpenGLRenderer()
{
    glFinish();
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glDeleteBuffers(2, (const GLuint*) &quadID);
    glDeleteTextures(kNumTextures, tex);
    glDeleteFramebuffers(kNumFBO, fbos);
    free(resourcePath);
    glUseProgram(0);
    unsigned int i = 0;
    glDeleteProgram(recordGBufferDataPass);
    glDeleteProgram(deferredLightingPass);
    glDeleteProgram(displayTextureContentsPass);
    for (; i < kShaderCount; i++) {
        glDeleteShader(shaders[i]);
    }
}

#pragma mark Shader Loading

GLboolean OpenGLRenderer::loadShaderFromFile(const char* shaderName, GLenum shaderType, GLint* shaderID)
{
    char pathToShader[255];
    sprintf(&pathToShader[0], "%s/%s", resourcePath, shaderName);
    FILE* f = fopen(pathToShader, "rb");
    if(!f)
    {
        __builtin_printf("Could not open file %s\n", pathToShader);
        return NULL;
    }
    fseek(f, 0, SEEK_END);
    size_t shaderLen = ftell(f);
    fseek(f, 0, SEEK_SET);
    GLchar* code = (GLchar*) malloc(shaderLen+1);
    fread(code, sizeof(char), shaderLen, f);
    fclose(f);
    code[shaderLen] = '\0';
    GLboolean r = loadShader(shaderType, (const GLchar**) &code, shaderID);
    if(!r)
    {
        __builtin_printf("Failed to load %s\n", shaderName);
    }
    free(code);
    return r;
}

GLboolean loadShader(GLenum shaderType, const GLchar** shaderText, GLint* shaderID)
{
    GLint status = 0;

    // Create a shader object
    *shaderID = glCreateShader(shaderType);
    // Set the source code in the shader object
    glShaderSource(*shaderID, 1, shaderText, NULL);
    // Compile the shader object
    glCompileShader(*shaderID);
    // Verify compile status
    glGetShaderiv(*shaderID, GL_COMPILE_STATUS, &status);
    if(status == GL_FALSE)
    {
        GLint logLength = 0;
        glGetShaderiv(*shaderID, GL_INFO_LOG_LENGTH, &logLength);
        GLcharARB *log = (GLcharARB*) malloc(logLength);
        glGetShaderInfoLog(*shaderID, logLength, &logLength, log);
        __builtin_printf("Shader compile log\n %s", log);
        free(log);
        return GL_FALSE;
    }
    return GL_TRUE;
}

void OpenGLRenderer::attachShadersToProgram(GLint program, GLint vertShaderID, GLint fragShaderID)
{
    // Attach the shader to our program
    glAttachShader(program, vertShaderID);
    glAttachShader(program, fragShaderID);
}

GLboolean OpenGLRenderer::linkAndValidateProgram(GLint program, GLint vertShaderID, GLint fragShaderID)
{
    GLint logLength;

    glLinkProgram(program);
    glGetProgramiv(program, GL_INFO_LOG_LENGTH, &logLength);
    if (logLength > 0) {
        GLchar *log = (GLchar*) malloc(logLength);
        glGetProgramInfoLog(program, logLength, &logLength, log);
        printf("Program link log:\n%s\n", log);
        free(log);
        glDeleteShader(vertShaderID);
        glDeleteShader(fragShaderID);
        return GL_FALSE;
    }
    glValidateProgram(program);
    glGetProgramiv(program, GL_INFO_LOG_LENGTH, &logLength);
    if (logLength > 0) {
        GLchar *log = (GLchar*)malloc(logLength);
        glGetProgramInfoLog(program, logLength, &logLength, log);
        printf("Program validate log:\n%s\n", log);
        free(log);
        return GL_FALSE;
    }

    GLint status = 0;
    glGetProgramiv(program, GL_VALIDATE_STATUS, &status);
    if (status == 0)
    {
        printf("Failed to validate program %d\n", program);
        return GL_FALSE;
    }
    return GL_TRUE;
}

GLshort OpenGLRenderer::loadShaders()
{
    if(!loadShaderFromFile(VERTEX_SHADER_TRANSFORM_NAME, GL_VERTEX_SHADER, &shaders[0]))
        return 1;

    if(!loadShaderFromFile(FRAGMENT_SHADER_RECORD_GBUFFER_NAME, GL_FRAGMENT_SHADER, &shaders[1]))
        return 2;

    // Create a program object
    recordGBufferDataPass = glCreateProgram();

    // Indicate the attribute indicies on which vertex arrays will be
    //  set with glVertexAttribPointer
    glBindAttribLocation(recordGBufferDataPass, POS_ATTRIB_IDX, "inPosition");
    glBindAttribLocation(recordGBufferDataPass, NORMAL_ATTRIB_IDX, "inNormal");
    glError();

    attachShadersToProgram(recordGBufferDataPass, shaders[0], shaders[1]);

    // Bind user-defined varying out variables to a fragment shader color number
    glBindFragDataLocation(recordGBufferDataPass, FRAG_COLOR_ATTRIB_IDX, "fragColor");
    glBindFragDataLocation(recordGBufferDataPass, FRAG_POS_ATTRIB_IDX, "fragPosition");
    glBindFragDataLocation(recordGBufferDataPass, FRAG_NORMAL_ATTRIB_IDX, "fragNormal");

    if (!linkAndValidateProgram(recordGBufferDataPass, shaders[0], shaders[1]))
    {
        return 3;
    }

    // Get the location of uniform variables. This location value will
    // then be passed to glUniform() to set the value of the variable
    projectionUniformIdx = glGetUniformLocation(recordGBufferDataPass, "projectionMatrix");
    orientationMatrixLocation = glGetUniformLocation(recordGBufferDataPass, "orientationMatrix");
    cameraTransformLocation = glGetUniformLocation(recordGBufferDataPass, "cameraMatrix");
    colorLocation = glGetUniformLocation(recordGBufferDataPass, "color");

    if(!loadShaderFromFile(PASSTHROUGH_NAME, GL_VERTEX_SHADER, &shaders[2]))
        return 1;

    if(!loadShaderFromFile(DEFERRED_LIGHTNING_NAME, GL_FRAGMENT_SHADER, &shaders[3]))
        return 2;

    // Create a program object
    deferredLightingPass = glCreateProgram();

    // Indicate the attribute indicies on which vertex arrays will be
    // set with glVertexAttribPointer
    glBindAttribLocation(deferredLightingPass, POS_ATTRIB_IDX, "inPosition");
    glBindAttribLocation(deferredLightingPass, TEXCOORD_ATTRIB_IDX, "inTexcoord");

    attachShadersToProgram(deferredLightingPass, shaders[2], shaders[3]);

    if (!linkAndValidateProgram(deferredLightingPass, shaders[2], shaders[3]))
    {
        return 3;
    }

    // Get the location of uniform variables. This location value will
    // then be passed to glUniform() to set the value of the variable
    normTexLocation = glGetUniformLocation(deferredLightingPass, "normalTex");
    positionTexLocation = glGetUniformLocation(deferredLightingPass, "posTex");
    colorTexLocation = glGetUniformLocation(deferredLightingPass, "colorTex");

    light1Pos = glGetUniformLocation(deferredLightingPass, "light1Pos");
    light1Color = glGetUniformLocation(deferredLightingPass, "light1Color");
    light2Pos = glGetUniformLocation(deferredLightingPass, "light2Pos");
    light2Color = glGetUniformLocation(deferredLightingPass, "light2Color");
    light3Pos = glGetUniformLocation(deferredLightingPass, "light3Pos");
    light3Color = glGetUniformLocation(deferredLightingPass, "light3Color");
    light4Pos = glGetUniformLocation(deferredLightingPass, "light4Pos");
    light4Color = glGetUniformLocation(deferredLightingPass, "light4Color");

    if(!loadShaderFromFile(BUFFER_DISPLAY_NAME, GL_FRAGMENT_SHADER, &shaders[4]))
    {
        return 2;
    }

    // Create a program object
    displayTextureContentsPass = glCreateProgram();

    // Indicate the attribute indicies on which vertex arrays will be
    //  set with glVertexAttribPointer
    glBindAttribLocation(displayTextureContentsPass, POS_ATTRIB_IDX, "inPosition");
    glBindAttribLocation(displayTextureContentsPass, TEXCOORD_ATTRIB_IDX, "inTexcoord");

    attachShadersToProgram(displayTextureContentsPass, shaders[2], shaders[4]);

    if (!linkAndValidateProgram(displayTextureContentsPass, shaders[2], shaders[4]))
    {
        return 3;
    }

    displayTexLocation = glGetUniformLocation(displayTextureContentsPass, "displayTex");

    glError();

    return 0;
}

#pragma mark Geometry Setup

bool OpenGLRenderer::setupQuad()
{
    // Quad vertex positions
    GLfloat quad[] =
    {
    //     x    y    s    t
        -1.0,-1.0, 0.0, 0.0,
         1.0,-1.0, 1.0, 0.0,
         1.0, 1.0, 1.0, 1.0,
        -1.0, 1.0, 0.0, 1.0, 
    };
    // Quad vertex indices
    GLushort indexes[] =
    {
        0,1,3,2,
    };

    glBindVertexArray( VAOs[Quad_VAO] );

    // Create a vertex buffer object (VBO) to store positions
    glGenBuffers(1, &quadID);
    glBindBuffer(GL_ARRAY_BUFFER, quadID);
    glBufferData(GL_ARRAY_BUFFER, sizeof(GLfloat)*16, &quad[0], GL_STATIC_DRAW);

    // Enable the position attribute for this VAO
    glEnableVertexAttribArray(POS_ATTRIB_IDX);

    // Set up parmeters for position attribute in the VAO including,
    //  size, type, stride, and offset in the currenly bound VAO
    // This also attaches the position VBO to the VAO
    glVertexAttribPointer(POS_ATTRIB_IDX,   // What attibute index will this array feed in the vertex shader
                          4,    // How many elements are there per position?
                          GL_FLOAT, // What is the type of this data?
                          GL_FALSE,             // Do we want to normalize this data (0-1 range for fixed-pont types)
                          4*sizeof(GLfloat), // What is the stride (i.e. bytes between positions)?
                          BUFFER_OFFSET(0));    // What is the offset in the VBO to the position data?

    // Create a VBO to store vertex array elements
    // This also attaches the element array buffer to the VAO
    glGenBuffers(1, &quadElementID);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, quadElementID);
    // Allocate and load vertex array element data into VBO
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(GLushort)*4, &indexes[0], GL_STATIC_DRAW);

    return true;
}

bool OpenGLRenderer::setupTeapot()
{
    // Create vertex buffer objects (VBOs) to store the teapot vertex positions, normals and indices
    glGenBuffers(1, &teapotVertexId);
    glGenBuffers(1, &teapotNormalId);
    glGenBuffers(1, &teapotElementId);

    glBindVertexArray( VAOs[Teapot_VAO] );

    // teapot vertices
    glBindBuffer(GL_ARRAY_BUFFER, teapotVertexId);
    // Allocate and load position data into the VBO
    glBufferData(GL_ARRAY_BUFFER, num_teapot_vertices*3*sizeof(GLfloat), teapot_vertices, GL_STATIC_DRAW);

    // Enable the position attribute for this VAO
    glEnableVertexAttribArray(POS_ATTRIB_IDX);

    // Set up parmeters for position attribute in the VAO including,
    //  size, type, stride, and offset in the currenly bound VAO
    // This also attaches the position VBO to the VAO
    glVertexAttribPointer(POS_ATTRIB_IDX,       // What attibute index will this array feed in the vertex shader
                          3,    // How many elements are there per position?
                          GL_FLOAT, // What is the type of this data?
                          GL_FALSE,             // Do we want to normalize this data (0-1 range for fixed-pont types)
                          3*sizeof(GLfloat), // What is the stride (i.e. bytes between positions)?
                          BUFFER_OFFSET(0));    // What is the offset in the VBO to the position data?

    // normals
    glBindBuffer(GL_ARRAY_BUFFER, teapotNormalId);
    // Allocate and load normal data into the VBO
    glBufferData(GL_ARRAY_BUFFER, num_teapot_vertices*3*sizeof(GLfloat), teapot_normals, GL_STATIC_DRAW);

    // Enable the position attribute for this VAO
    glEnableVertexAttribArray(NORMAL_ATTRIB_IDX);
    glError();

    // Set up parmeters for normal attribute in the VAO including,
    //  size, type, stride, and offset in the currenly bound VAO
    // This also attaches the normal VBO to the VAO
    glVertexAttribPointer(NORMAL_ATTRIB_IDX,        // What attibute index will this array feed in the vertex shader
                          3,    // How many elements are there per position?
                          GL_FLOAT, // What is the type of this data?
                          GL_FALSE,             // Do we want to normalize this data (0-1 range for fixed-pont types)
                          3*sizeof(GLfloat), // What is the stride (i.e. bytes between positions)?
                          BUFFER_OFFSET(0));    // What is the offset in the VBO to the position data?

    // Create a VBO to store vertex array elements
    // This also attaches the element array buffer to the VAO
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, teapotElementId);
    // Allocate and load vertex array element data into VBO
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, num_teapot_indices*sizeof(GLushort), teapot_indices, GL_STATIC_DRAW);

    return true;
}

#pragma mark General Setup


bool OpenGLRenderer::setupGL()
{
    // Create vertex array objects (VAO) to cache model parameters
    glGenVertexArrays( NumVAOs, VAOs);
    glBindVertexArray(VAOs[Teapot_VAO]);

    int error = 0;
    error = loadShaders();
    if(error != 0)
    {
        __builtin_printf("Got err loading shaders %u\n", error);
        return false;
    }

    if(!setupQuad())
    {
        return false;
    }

    if(!setupTeapot())
    {
        return false;
    }

    //set up a default camera matrix
    memcpy(&cameraMatrix, &IdentityMatrix, sizeof(mat4));
    cameraMatrix.columns[3].z = -6.0;   

    //Deferred Shading needs an FBO and various color attachments
    glGenTextures(kNumTextures, tex);
    glGenFramebuffers(kNumFBO, fbos);

    glBindFramebuffer(GL_FRAMEBUFFER, fbos[0]);

    //the position of the pixel in world space
    glBindTexture(GL_TEXTURE_2D, tex[0]);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_FLOAT, NULL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, tex[0], 0);
    buffers[0] = GL_COLOR_ATTACHMENT0;

    //the albedo (reflectivity) of the pixel
    glBindTexture(GL_TEXTURE_2D, tex[1]);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_FLOAT, NULL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT1, GL_TEXTURE_2D, tex[1], 0);
    buffers[1] = GL_COLOR_ATTACHMENT1;

    //the pixel's normal. we will store 2 components and reconstruct the 3rd in the fragment shader
    glBindTexture(GL_TEXTURE_2D, tex[2]);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RG32F, width, height, 0, GL_RG, GL_FLOAT, NULL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT2, GL_TEXTURE_2D, tex[2], 0);
    buffers[2] = GL_COLOR_ATTACHMENT2;

    //depth
    glBindTexture(GL_TEXTURE_2D, tex[3]);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT24, width, height, 0, GL_DEPTH_COMPONENT, GL_UNSIGNED_INT, NULL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, tex[3], 0);

    GLenum status = glCheckFramebufferStatus(GL_FRAMEBUFFER);
    if (status != GL_FRAMEBUFFER_COMPLETE)
    {
        __builtin_printf("FBO status expected complete but got 0x%04X", status);
        glDeleteTextures(kNumTextures, tex);
        glDeleteFramebuffers(kNumFBO, fbos);
        return false;
    }

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_CULL_FACE);
    glViewport(0, 0, width, height);

    l1Pos.x = 10.0; l1Pos.y =  0.0; l1Pos.z = 6.0; l1Pos.w = 1.0;
    l2Pos.x =-10.0; l2Pos.y =  0.0; l2Pos.z = 6.0; l2Pos.w = 1.0;
    l3Pos.x =  0.0; l3Pos.y = 10.0; l3Pos.z = 6.0; l3Pos.w = 1.0;
    l4Pos.x =  0.0; l4Pos.y =-10.0; l4Pos.z = 6.0; l4Pos.w = 1.0;

    l1Color.x=0.0; l1Color.y=0.5; l1Color.z=0.0;
    l2Color.x=0.75;l2Color.y=0.5; l2Color.z=0.0;
    l3Color.x=0.0; l3Color.y=0.5; l3Color.z=0.75;
    l4Color.x=0.75;l4Color.y=0.0; l4Color.z=0.0;

    glError();

    return true;
}

#pragma mark Draw

void OpenGLRenderer::resizeViewport(uint32_t w, uint32_t h)
{
    width = w;
    height = h;
    glViewport(0, 0, width, height);
}

void OpenGLRenderer::updateGBufferContents()
{
    // Set up the modelview and projection matricies
    GLfloat modelView[16];
    GLfloat projection[16];

    //First pass
    //Record data into G-buffer
    glBindFramebuffer(GL_FRAMEBUFFER, fbos[0]);
    glDrawBuffers(kNumMRT, buffers);
    //If your scene covers every pixel, you won't actually need to clear here.
    //Most scenes will have some sort of skybox, so each pixel should have data.
    //In that case, this clear is redundant.
    glClearColor(0.0,0.0,0.0,0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glEnable(GL_DEPTH_TEST);

    mtxLoadPerspective(projection, 90, (float)width / (float)height,0.1, 35.0);
    mtxLoadIdentity(modelView);

    // add an initial rotation to teapot for a better point of view
    mtxRotateApply(modelView, 30.0, 1.0, 0.0, 0.0);
    mtxRotateApply(modelView, animationStep*animationDelta, 1.0, 0.0, 1.0);

    float scale = 15.0;
    mtxScaleApply(modelView, scale, scale, scale);

    glUseProgram(recordGBufferDataPass);
    glUniformMatrix4fv(projectionUniformIdx, 1, GL_FALSE, projection);
    glUniformMatrix4fv(cameraTransformLocation, 1, GL_FALSE, (const GLfloat*) &cameraMatrix);
    glUniformMatrix4fv(orientationMatrixLocation, 1, GL_FALSE, modelView);
    glUniform4f(colorLocation, 0.25, 0.25, 0.25, 1.0);

    // Bind our teapot vertex array object (VAO)
    glBindVertexArray(VAOs[Teapot_VAO]);

    // Enable the position attribute for this VAO
    glEnableVertexAttribArray(POS_ATTRIB_IDX);
    // Enable the normal attribute for this VAO
    glEnableVertexAttribArray(NORMAL_ATTRIB_IDX);

    glBindBuffer(GL_ARRAY_BUFFER, teapotVertexId);
    glVertexAttribPointer(POS_ATTRIB_IDX, 3, GL_FLOAT, GL_FALSE, 0, NULL);
    glBindBuffer(GL_ARRAY_BUFFER, teapotNormalId);
    glVertexAttribPointer(NORMAL_ATTRIB_IDX, 3, GL_FLOAT, GL_FALSE, 0, NULL);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, teapotElementId);

    //Draw the teapot
    int start = 0, i = 0;
    while(i < num_teapot_indices) {
        if(teapot_indices[i] == -1) {
            glDrawElements(GL_TRIANGLE_STRIP, i - start, GL_UNSIGNED_SHORT, BUFFER_OFFSET(start*sizeof(ushort)));
            start = i + 1;
        }
        i++;
    }
    if(start < num_teapot_indices)
        glDrawElements(GL_TRIANGLE_STRIP, i - start - 1, GL_UNSIGNED_SHORT, BUFFER_OFFSET(start*sizeof(ushort)));

    glDisableVertexAttribArray(POS_ATTRIB_IDX);
    glDisableVertexAttribArray(NORMAL_ATTRIB_IDX);

}

void OpenGLRenderer::updateAnimations()
{
    // Animate the model when the user presses the <space> key
    if(animate)
    {
        animationStep = (animationStep+1) % kAnimationLoopValue;
    }
}

void OpenGLRenderer::showPositionBuffer()
{
    glUseProgram(displayTextureContentsPass);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, tex[0]);
    glUniform1i(displayTexLocation, 0);
}

void OpenGLRenderer::showNormalBuffer()
{
    glUseProgram(displayTextureContentsPass);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, tex[2]);
    glUniform1i(displayTexLocation, 0);
}

void OpenGLRenderer::showAlbedoBuffer()
{
    glUseProgram(displayTextureContentsPass);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, tex[1]);
    glUniform1i(displayTexLocation, 0);
}

void OpenGLRenderer::showFinalImage()
{
    //move lights into eye space
    vec4 light1Position,light2Position,light3Position,light4Position;
    matVecMul(&cameraMatrix, &l1Pos, &light1Position);
    matVecMul(&cameraMatrix, &l2Pos, &light2Position);
    matVecMul(&cameraMatrix, &l3Pos, &light3Position);
    matVecMul(&cameraMatrix, &l4Pos, &light4Position);

    glUseProgram(deferredLightingPass);
    //draw all 3 buffers as textures
    //set up multitexturing
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, tex[0]);
    glActiveTexture(GL_TEXTURE1);
    glBindTexture(GL_TEXTURE_2D, tex[1]);
    glActiveTexture(GL_TEXTURE2);
    glBindTexture(GL_TEXTURE_2D, tex[2]);

    glUniform1i(positionTexLocation, 0);
    glUniform1i(colorTexLocation, 1);
    glUniform1i(normTexLocation, 2);
    glUniform3fv(light1Pos, 1, (const GLfloat*) &light1Position);
    glUniform3fv(light1Color, 1, (const GLfloat*) &l1Color);
    glUniform3fv(light2Pos, 1, (const GLfloat*) &light2Position);
    glUniform3fv(light2Color, 1, (const GLfloat*) &l2Color);
    glUniform3fv(light3Pos, 1, (const GLfloat*) &light3Position);
    glUniform3fv(light3Color, 1, (const GLfloat*) &l3Color);
    glUniform3fv(light4Pos, 1, (const GLfloat*) &light4Position);
    glUniform3fv(light4Color, 1, (const GLfloat*) &l4Color);
}

void OpenGLRenderer::drawQuad()
{
    glBindVertexArray( VAOs[Quad_VAO] );

    glEnableVertexAttribArray(POS_ATTRIB_IDX);
    glEnableVertexAttribArray(TEXCOORD_ATTRIB_IDX);

    glBindBuffer(GL_ARRAY_BUFFER, quadID);
    glVertexAttribPointer(POS_ATTRIB_IDX, 2, GL_FLOAT, GL_FALSE, 4*sizeof(GLfloat), NULL);
    glVertexAttribPointer(TEXCOORD_ATTRIB_IDX, 2, GL_FLOAT, GL_FALSE, 4*sizeof(GLfloat),  BUFFER_OFFSET(2*sizeof(GLfloat)));

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, quadElementID);
    // draw quad
    glDrawElements(GL_TRIANGLE_STRIP, 4, GL_UNSIGNED_SHORT, NULL);

    glDisableVertexAttribArray(POS_ATTRIB_IDX);
    glDisableVertexAttribArray(TEXCOORD_ATTRIB_IDX);
}

void OpenGLRenderer::draw()
{
    updateAnimations();

    updateGBufferContents();

    //draw to window
    glFrontFace(GL_CCW);
    glDisable(GL_DEPTH_TEST);
    glBindFramebuffer(GL_FRAMEBUFFER,0);
    glDrawBuffer(GL_BACK);

    //A note about this clear:
    //This is also a redundant clear. Normally, you'd be drawing a full screen
    //quad here, so every pixel will be touched.
    //However, I'm dropping out in the fragment shader based on alpha
    //so if you don't clear here, you'll get VRAM garbage where there's no color/normal/pos 
    //info in the G-buffer.
    glClearColor(1.0,1.0,1.0,0.0);
    glClear(GL_COLOR_BUFFER_BIT);

    switch (showBuffer) {
        case kPositionBuffer:
            showPositionBuffer();
            break;
        case kAlbedoBuffer:
            showAlbedoBuffer();
            break;
        case kNormalBuffer:
            showNormalBuffer();
            break;
        default:
        case kFinalImage:
            //draw the final image
            showFinalImage();
            break;
    }

    drawQuad();

    glError();
    // unbind existing shader program
    glUseProgram(0);
}
```

[Next](Document%20Revision%20History.md)[Previous](DeferredShadingAppDelegate.m.md)

