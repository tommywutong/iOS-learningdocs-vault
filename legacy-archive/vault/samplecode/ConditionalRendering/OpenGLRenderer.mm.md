---
title: ConditionalRendering
apple_id: DTS40010087
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/ConditionalRendering/Listings/OpenGLRenderer_mm.html
archived_at: '2026-07-18T03:04:13.954553Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ConditionalRendering](ConditionalRendering.md)


[Next](TriToothedGearFlatModel.h.md)[Previous](OpenGLRenderer.h.md)

# OpenGLRenderer.mm

```objc
/*
     File: OpenGLRenderer.mm
 Abstract: The renderer class creates and draws the OpenGL shaders. This is where we demonstrate how to do conditional rendering based on an occlusion query.
  Version: 1.1

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

#import "OpenGLRenderer.h"
#import "TriToothedGearFlatModel.h"

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

#define glError() { \
GLenum err = glGetError(); \
while (err != GL_NO_ERROR) { \
__builtin_printf("glError: %s caught at %s:%u\n", (char *)gluErrorString(err), __FILE__, __LINE__); \
err = glGetError(); \
exit(-1); \
} \
}

typedef struct {
    const char *vert, *frag;
} programInfo_t;

programInfo_t programFileName[kProgramCount] = {
    { "ConditionalRender.vs",   "ConditionalRender.fs"     },
    { "color.vs",              "color.fs"     },
};

GLboolean loadShader(GLenum shaderType, const GLchar** shaderText, GLint* shaderID);
GLboolean linkShaders(GLint* program, GLint vertShaderID, GLint fragShaderID);


@implementation OpenGLRenderer

#pragma mark General Setup

- (id)init
{
    if (self = [super init])
    {
        animationDelta = 1.5;
        animationStep = 0.0;
        kAnimationLoopValue = 360.0 / animationDelta;
        animate = YES;
        xAxisAngle = 0.0;
        zAxisAngle = 0.0;
    }
    return self;
}

- (void)dealloc
{
    glFinish();
    glBindVertexArray(0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    glDeleteBuffers(4, &triToothedGearFlat->vertsID);
    free(triToothedGearFlat);
    glDeleteBuffers(1, &quadID);
    glDeleteBuffers(1, &quadElementID);
    glDeleteVertexArrays(1, &gearVAOId);
    glDeleteVertexArrays(1, &quadVAOId);

    glUseProgram(0);
    int i = 0;
    for (; i < kProgramCount; i++) {
        glDeleteProgram(programs[i]);
    }
    for (; i < kShaderCount; i++) {
        glDeleteShader(shaders[i]);
    }
    [super dealloc];
}

- (BOOL)setupScene
{
    lightPos.x = 0.0; lightPos.y = 5.0; lightPos.z = 0.0; lightPos.w = 1.0;
    lightColor.x = 0.15; lightColor.y = 0.15; lightColor.z = 0.15;

    GLfloat quad[] =
    {
        //     x    y    z    s    t
        -1.0,-1.0, 1.0, 0.0, 0.0,
        1.0,-1.0, 1.0, 1.0, 0.0,
        1.0, 1.0, 1.0, 1.0, 1.0,
        -1.0, 1.0, 1.0, 0.0, 1.0,
    };
    GLushort indexes[] =
    {
        0,1,3,2,
    };

    // gear model
    glGenVertexArrays(1, &gearVAOId);
    glBindVertexArray(gearVAOId);

    triToothedGearFlat = (quadric*) malloc(sizeof(quadric));
    triToothedGearFlat->vertCount = GEAR_VERTEX_COUNT;
    triToothedGearFlat->indexCount = GEAR_INDEX_COUNT;

    glGenBuffers(4, &triToothedGearFlat->vertsID);
    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->vertsID);
    glBufferData(GL_ARRAY_BUFFER, triToothedGearFlat->vertCount*3*sizeof(GLfloat), vertices, GL_STATIC_DRAW);
    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->colorsID);
    glBufferData(GL_ARRAY_BUFFER, triToothedGearFlat->vertCount*3*sizeof(GLfloat), colors, GL_STATIC_DRAW);
    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->normalsID);
    glBufferData(GL_ARRAY_BUFFER, triToothedGearFlat->vertCount*3*sizeof(GLfloat), normals, GL_STATIC_DRAW);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, triToothedGearFlat->indicesID);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, triToothedGearFlat->indexCount*sizeof(GLuint), indices, GL_STATIC_DRAW);

    // quad
    glGenVertexArrays(1, &quadVAOId);
    glBindVertexArray(quadVAOId);

    glGenBuffers(1, &quadID);
    glGenBuffers(1, &quadElementID);
    glBindBuffer(GL_ARRAY_BUFFER, quadID);
    glBufferData(GL_ARRAY_BUFFER, sizeof(quad), &quad[0], GL_STATIC_DRAW);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, quadElementID);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indexes), &indexes[0], GL_STATIC_DRAW);

    return YES;
}

- (BOOL)setupGL
{
    if(![self setupScene])
    {
        return NO;
    }

    if([self loadShaders])
    {
        return NO;
    }

    //set up a default camera matrix
    [self regenCameraMatrix];

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_CULL_FACE);
    glViewport(0, 0, width, height);

    glGenQueries(1, &query);
    //the gear's normals use that of the first vertex
    glProvokingVertexEXT(GL_FIRST_VERTEX_CONVENTION_EXT);

    return YES;
}

- (void)reshapeToWidth:(GLsizei)w height:(GLsizei)h
{
    width = w;
    height = h;
    glViewport(0, 0, width, height);
}

#pragma mark Rendering

- (void)draw
{
    if(animate)
    {
        animationStep = (animationStep+1) % kAnimationLoopValue;
    }

    glClearColor(0.0,0.0,0.0,0.0);
    /*
     if you can guarantee you'll touch every pixel, you don't need to clear
     the color buffer. However, this demo can't guarantee that!
     */
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glEnable(GL_DEPTH_TEST);

    glBindVertexArray(gearVAOId);

    glUseProgram(programs[0]);

    GLKMatrix4 projectionMatrix = GLKMatrix4MakePerspective(75.0 * (M_PI/180.0), ((GLdouble) width) / ((GLdouble) height), 0.1, 100.0);
    glUniformMatrix4fv(projectionMatrixLocation, 1, GL_FALSE, (const GLfloat*) &projectionMatrix);

    GLKVector4 lightPosition = GLKMatrix4MultiplyVector4(cameraMatrix, lightPos);
    GLKMatrix4 rotMatrix = GLKMatrix4MakeRotation(animationStep*animationDelta * (M_PI/180.0), 1.0, 0.0, 1.0);

    glUniformMatrix4fv(cameraMatrixLocation, 1, GL_FALSE, (const GLfloat*) &cameraMatrix);
    glUniform3fv(lightPosLocation, 1, (const GLfloat*) &lightPosition);
    glUniform3fv(lightColorLocation, 1, (const GLfloat*) &lightColor);

    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->vertsID);
    glVertexAttribPointer(attribPosition, 3, GL_FLOAT, GL_FALSE, 0, NULL);
    glEnableVertexAttribArray(attribPosition);

    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->normalsID);
    glVertexAttribPointer(attribNormal, 3, GL_FLOAT, GL_FALSE, 0, NULL);
    glEnableVertexAttribArray(attribNormal);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, triToothedGearFlat->indicesID);

    int cols = 7, rows = 4, slices = 20;
    float initialx = 1.25*-(cols / 2.0);
    float initialy = -(rows / 2.0);
    int i,j,k;

    //seeding every frame so the colors don't jump around
    srand(0);
    for (k = 0; k < slices/3.0; k++) {
        GLKVector4 color = {(rand()%255) / 255.0, (rand()%255) / 255.0, (rand()%255) / 255.0, 1.0};
        glUniform4fv(colorLocation, 1, (const GLfloat*) &color);
        for (i=0; i < cols; i++) {
            for (j = 0; j < rows; j++) {
                GLKMatrix4 tm, f;
                tm = GLKMatrix4MakeTranslation(initialx+i*1.5, initialy+(j), -k*1.5);
                f = GLKMatrix4Multiply(tm, rotMatrix);
                glUniformMatrix4fv(modelTransformMatrixLocation, 1, GL_FALSE, (const GLfloat*) &f);
                glUniform1f(scaleLocation, 0.25);
                glDrawElements(GL_TRIANGLES, triToothedGearFlat->indexCount, GL_UNSIGNED_INT, NULL);
            }
        }
    }

    //draw the covering plane
    glBindVertexArray(quadVAOId);

    glUseProgram(programs[1]);

    GLKMatrix4 scaleMatrix = GLKMatrix4MakeScale(9.0, 7.0, -9.0);
    GLKMatrix4 MVPMatrix = GLKMatrix4Multiply(projectionMatrix, scaleMatrix);
    glUniformMatrix4fv(MVPLocation, 1, GL_FALSE, (const GLfloat*) &MVPMatrix);
    glUniform4f(constantColorLocation, 1.0, 1.0, 1.0, 1.0);

    glBindBuffer(GL_ARRAY_BUFFER, quadID);
    glVertexAttribPointer(inVertexLocation, 3, GL_FLOAT, GL_FALSE, sizeof(GLfloat)*5, NULL);
    glEnableVertexAttribArray(inVertexLocation);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, quadElementID);
    glDrawElements(GL_TRIANGLE_STRIP, 4, GL_UNSIGNED_SHORT, NULL);

    /*
     This should be a bounding volume on the conditionally rendered objects.
     We don't actually want to draw the volume, so we turn writes off.
     */
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE);
    glDepthMask(GL_FALSE);
    glBeginQuery(GL_SAMPLES_PASSED_ARB, query);

    scaleMatrix = GLKMatrix4MakeScale(8.0, 6.0, -11.0);
    MVPMatrix = GLKMatrix4Multiply(projectionMatrix, scaleMatrix);
    glUniformMatrix4fv(MVPLocation, 1, GL_FALSE, (const GLfloat*) &MVPMatrix);

    glDrawElements(GL_TRIANGLE_STRIP, 4, GL_UNSIGNED_SHORT, NULL);

    glEndQuery(GL_SAMPLES_PASSED_ARB);
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE);
    glDepthMask(GL_TRUE);

    //reset state
    glBindVertexArray(gearVAOId);
    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->vertsID);
    glVertexAttribPointer(attribPosition, 3, GL_FLOAT, GL_FALSE, 0, NULL);
    glBindBuffer(GL_ARRAY_BUFFER, triToothedGearFlat->normalsID);
    glVertexAttribPointer(attribNormal, 3, GL_FLOAT, GL_FALSE, 0, NULL);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, triToothedGearFlat->indicesID);

    //do the conditional render
    glUseProgram(programs[0]);
    glBeginConditionalRenderNV(query, GL_QUERY_WAIT_NV);
    for (; k < slices; k++) {
        GLKVector4 color = {(rand()%255) / 255.0, (rand()%255) / 255.0, (rand()%255) / 255.0, 1.0};
        glUniform4fv(colorLocation, 1, (const GLfloat*) &color);
        for (i=0; i < cols; i++) {
            for (j = 0; j < rows; j++) {
                GLKMatrix4 tm, f;
                tm = GLKMatrix4MakeTranslation(initialx+i*1.5, initialy+(j), -k*1.5);
                f = GLKMatrix4Multiply(tm, rotMatrix);
                glUniformMatrix4fv(modelTransformMatrixLocation, 1, GL_FALSE, (const GLfloat*) &f);
                glUniform1f(scaleLocation, 0.25);
                glDrawElements(GL_TRIANGLES, triToothedGearFlat->indexCount, GL_UNSIGNED_INT, NULL);
            }
        }
    }
    glEndConditionalRenderNV();
}

- (void)toggleAnimation
{
    animate = !animate;
}

#pragma mark Camera Utility

- (void)regenCameraMatrix
{
    // set up a default camera matrix
    GLKMatrix4 modelView = GLKMatrix4MakeTranslation(0, 0, -6.0);
    modelView = GLKMatrix4Rotate(modelView, xAxisAngle, 1, 0, 0);
    cameraMatrix = GLKMatrix4Rotate(modelView, zAxisAngle, 0, 0, 1);
}

- (void)applyCameraMovementWdx:(float)dx dy:(float)dy
{
    xAxisAngle += dy/3 * (M_PI/180.0);
    zAxisAngle += dx/3 * (M_PI/180.0);
    [self regenCameraMatrix];
}

#pragma mark Shader Loading

- (GLshort)loadShaders
{
    for (int i=0; i < kProgramCount; i++)
    {
        // vertex shader
        GLchar* shader = [self loadShaderFromFile:programFileName[i].vert];
        if (!shader) {
            return 1;
        }
        if(!loadShader(GL_VERTEX_SHADER, (const GLchar**) &shader, &shaders[i*2])) {
            return 1;
        }
        free(shader);

        // fragment shader
        shader = [self loadShaderFromFile:programFileName[i].frag];
        if (!shader) {
            return 2;
        }
        if(!loadShader(GL_FRAGMENT_SHADER, (const GLchar**) &shader, &shaders[i*2+1])) {
            return 2;
        }
        free(shader);

        if(!linkShaders(&programs[i], shaders[i*2], shaders[i*2+1]))
        {
            return 3;
        }
    }

    scaleLocation = glGetUniformLocation(programs[0], "scale");
    cameraMatrixLocation = glGetUniformLocation(programs[0], "cameraMatrix");
    modelTransformMatrixLocation = glGetUniformLocation(programs[0], "modelTransformMatrix");
    projectionMatrixLocation = glGetUniformLocation(programs[0], "projectionMatrix");
    colorLocation = glGetUniformLocation(programs[0], "color");
    lightPosLocation = glGetUniformLocation(programs[0], "lightPos");
    lightColorLocation = glGetUniformLocation(programs[0], "lightColor");
    attribNormal = glGetAttribLocation(programs[0], "attribNormal");
    attribPosition = glGetAttribLocation(programs[0], "attribPosition");


    MVPLocation = glGetUniformLocation(programs[1], "MVP");
    constantColorLocation = glGetUniformLocation(programs[1], "constantColor");
    inVertexLocation = glGetAttribLocation(programs[1], "inVertex");

    glError();

    return 0;
}

- (GLchar*)loadShaderFromFile:(const char*)shaderName
{
    const char* resourcePath = [[[NSBundle mainBundle] resourcePath] cStringUsingEncoding:NSASCIIStringEncoding];
    char pathToShader[255];
    sprintf(&pathToShader[0], "%s/%s", resourcePath, shaderName);

    FILE* f = fopen(pathToShader, "rb");
    if(!f)
    {
        return NULL;
    }
    fseek(f, 0, SEEK_END);
    size_t shaderLen = ftell(f);
    fseek(f, 0, SEEK_SET);
    GLchar* code = (GLchar*) malloc(shaderLen+1);
    fread(code, sizeof(char), shaderLen, f);
    fclose(f);
    code[shaderLen] = '\0';
    return code;
}

GLboolean loadShader(GLenum shaderType, const GLchar** shaderText, GLint* shaderID)
{
    GLint status = 0;

    *shaderID = glCreateShader(shaderType);
    glShaderSource(*shaderID, 1, shaderText, NULL);
    glCompileShader(*shaderID);
    glGetShaderiv(*shaderID, GL_COMPILE_STATUS, &status);
    if(status == GL_FALSE)
    {
        GLint logLength = 0;
        glGetShaderiv(*shaderID, GL_INFO_LOG_LENGTH, &logLength);
        GLcharARB *log = (GLcharARB*) malloc(logLength);
        glGetShaderInfoLog(*shaderID, logLength, &logLength, log);
        printf("Shader compile log\n %s", log);
        free(log);
        return GL_FALSE;
    }
    return GL_TRUE;
}

GLboolean linkShaders(GLint* program, GLint vertShaderID, GLint fragShaderID)
{
    GLint status = 0;
    *program = glCreateProgram();
    glAttachShader(*program, vertShaderID);
    glAttachShader(*program, fragShaderID);

    GLint logLength;

    glLinkProgram(*program);
    glGetProgramiv(*program, GL_INFO_LOG_LENGTH, &logLength);
    if (logLength > 0) {
        GLchar *log = (GLchar*) malloc(logLength);
        glGetProgramInfoLog(*program, logLength, &logLength, log);
        printf("Program link log:\n%s\n", log);
        free(log);
        glDeleteShader(vertShaderID);
        glDeleteShader(fragShaderID);
        return GL_FALSE;
    }
    glValidateProgram(*program);
    glGetProgramiv(*program, GL_INFO_LOG_LENGTH, &logLength);
    if (logLength > 0) {
        GLchar *log = (GLchar*)malloc(logLength);
        glGetProgramInfoLog(*program, logLength, &logLength, log);
        printf("Program validate log:\n%s\n", log);
        free(log);
        return GL_FALSE;
    }

    glGetProgramiv(*program, GL_VALIDATE_STATUS, &status);
    if (status == 0)
    {
        printf("Failed to validate program %d\n", *program);
        return GL_FALSE;
    }
    return GL_TRUE;
}


@end
```

[Next](TriToothedGearFlatModel.h.md)[Previous](OpenGLRenderer.h.md)

