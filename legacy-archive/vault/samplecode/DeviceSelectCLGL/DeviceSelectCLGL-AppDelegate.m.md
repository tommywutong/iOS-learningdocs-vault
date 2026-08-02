---
title: DeviceSelectCLGL
apple_id: DTS40014358
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2014-04-18'
source_url: https://developer.apple.com/library/archive/samplecode/sc1989/Listings/DeviceSelectCLGL_AppDelegate_m.html
archived_at: '2026-07-26T19:54:14.334612Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeviceSelectCLGL](DeviceSelectCLGL.md)


[Next](DeviceSelectCLGL-kernel.cl.md)[Previous](DeviceSelectCLGL-AppDelegate.h.md)

# DeviceSelectCLGL/AppDelegate.m

```objc
/*
     File: AppDelegate.m
 Abstract:
 App delegate for instantiating CL+GL sharing and applying an image filter.

  Version: 1.0

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

#import "AppDelegate.h"

#import <OpenGL/gl.h>
#import <OpenCL/opencl.h>

#import <mach/mach_time.h>

enum
{
  UNIFORM_TEX,
  NUM_UNIFORMS
};
GLint uniforms[NUM_UNIFORMS];

enum
{
  ATTRIB_VERTEX,
  NUM_ATTRIBUTES
};

@interface AppDelegate ()
{
  GLuint screenFillingQuadBuffer;
  GLuint screenFillingQuadIndexBuffer;

  GLuint screenFillingQuadProgram;
  GLuint texture;

  cl_device_id     device;
  cl_context       ctx;
  cl_program       program;
  cl_kernel        kernel;
  cl_command_queue queue;
  cl_mem           input;
  cl_mem           output;

  size_t           width;
  size_t           height;
}

@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
  [self.view.openGLContext makeCurrentContext];

  // Get ther OpenGL renderer
  const char *renderer = (const char *)glGetString(GL_RENDERER);

  if(renderer != NULL)
  {
    // Is this a AMD D300 renderer?
    const char *isD300 = strstr(renderer, "D300");

    // Is this a AMD D500 renderer?
    const char *isD500 = strstr(renderer, "D500");

    // Is this a AMD D700 renderer?
    const char *isD700 = strstr(renderer, "D700");

    // Is this one of the AMD renderers?
    BOOL isAMD = (isD300 != NULL) || (isD500 != NULL) || (isD700 != NULL);

    // Check to see if we have more than 2 renderers?
    // The first is typically a software renderer and
    // the second is the hardware (GPU) renderer.
    BOOL               isDualGPU = NO;
    GLint              count     = 0;
    CGLRendererInfoObj info      = NULL;

    // Get the number of renderers
    CGLError err = CGLQueryRendererInfo(0xFFFFFFFF, &info, &count);

    // If the query returned without an error then check
    // renderer count.
    if(err == kCGLNoError)
    {
      // Make certain  that we've more than 2 renderers
      isDualGPU = count > 2;

      // Release the renderer infor object data reference
      CGLDestroyRendererInfo(info);
    } // if

    // Do we have a dual GPU MacPro?
    BOOL isMacPro = isDualGPU && isAMD;

    // Are we running on a MacPro?
    if(!isMacPro)
    {
      // This is not a MacPro!

      // Create a new alert
      NSAlert *alert = [NSAlert new];

      if(alert)
      {
        // Set the button title for this alert
        [alert addButtonWithTitle:@"OK"];

        // Set the text message for this alert
        [alert setMessageText:@"Requires a MacPro!"];

        // Set the alert style
        [alert setAlertStyle:NSCriticalAlertStyle];

        // Run the laert a a modal dialog
        NSModalResponse response = [alert runModal];

        // Once OK button was clicked, log the message
        // to the standard error output
        if(response == NSAlertFirstButtonReturn)
        {
          fprintf(stderr, ">> MESSAGE: Requires a MacPro!\n");
        } // if
      } // if

      // Since the MacPro requirements are not meet,
      // exit from this application
      exit(-1);
    } // if
  } // if

  //
  // SDK Example showing how to choose a GPU device for compute in an
  // application that shares resources between CL and GL
  //

  // Obtain the CGL Sharegroup for the view
  CGLShareGroupObj sharegroup = CGLGetShareGroup(self.view.openGLContext.CGLContextObj);

  // Create a CL context from the sharegroup. The NSOpenGLView is setup in
  // InterfaceBuilder to allow offline renderers. This will cause both the display
  // and non-display connected GPU to be included in the group.
  cl_context_properties props[] =
  {
    CL_CONTEXT_PROPERTY_USE_CGL_SHAREGROUP_APPLE,
    (cl_context_properties)sharegroup,
    0
  };

  // This context will contain all GPUs, but not the CPU CL device. If you want
  // to include the CPU in the context, pass the CPU cl_device_id in the third
  // parameter of clCreateContext
  cl_int err = 0;

  ctx = clCreateContext(props, 0, NULL, NULL, NULL, &err);

  // Create the GL geometry and compile the shaders
  [self createGeometry];
  [self compileShaders];
  [self loadInputMem];
  [self createOutputMem];

  // Query the devices in the context
  size_t len;

  clGetContextInfo(ctx, CL_CONTEXT_DEVICES, 0, NULL, &len);

  int num_devices = (int)len/sizeof(cl_device_id);

  cl_device_id devices[num_devices];

  clGetContextInfo(ctx, CL_CONTEXT_DEVICES, sizeof(devices), devices, NULL);

  //
  // Look up the device for the current virtual screen.
  //
  cl_device_id displayDevice;

  clGetGLContextInfoAPPLE(ctx, self.view.openGLContext.CGLContextObj, CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE, sizeof(displayDevice), &displayDevice, NULL);

  // Look for the other device in the context
  for (int i=0;i!=num_devices;++i)
  {
    if (devices[i] != displayDevice)
    {
      device = devices[i];
      break;
    }
  }

  clGetDeviceInfo(device, CL_DEVICE_NAME, 0, NULL, &len);

  char device_name[len];
  clGetDeviceInfo(device, CL_DEVICE_NAME, sizeof(device_name), device_name, NULL);
  printf("Using device (%p) %s\n",device,device_name);

  queue = clCreateCommandQueue(ctx, device, 0, &err);

  // Compile the CL kernel
  [self compileKernel];

  self.view.needsDisplay = YES;
}

- (void)loadInputMem
{
  // Load the input file
  NSURL* url = [[NSBundle mainBundle] URLForImageResource:@"Zebra"];

  if(url)
  {
    CGImageSourceRef source = CGImageSourceCreateWithURL( (__bridge CFURLRef)url, NULL);

    if(source != NULL)
    {
      NSDictionary *options = [NSDictionary dictionaryWithObject: (id)kCFBooleanTrue
                                                          forKey: (id)kCGImageSourceShouldCache];

      if(options)
      {
        CGImageRef image  = CGImageSourceCreateImageAtIndex(source, 0, (__bridge CFDictionaryRef)options);

        if(image != NULL)
        {
          CFDataRef input_data = CGDataProviderCopyData(CGImageGetDataProvider(image));

          if(input_data != NULL)
          {
            const UInt8* input_ptr  = CFDataGetBytePtr(input_data);

            width  = CGImageGetWidth(image);
            height = CGImageGetHeight(image);

            size_t       bits_component = CGImageGetBitsPerComponent(image);
            size_t       row_bytes      = width;
            CGBitmapInfo info           = CGImageGetBitmapInfo(image);

            // Determine a CL format to use
            cl_image_format fmt = { 0 };

            switch (info&kCGBitmapAlphaInfoMask)
            {
              case kCGImageAlphaNone:
                fmt.image_channel_order = CL_RGB;
                row_bytes *= 3;
                break;
              case kCGImageAlphaPremultipliedLast:
              case kCGImageAlphaLast:
              case kCGImageAlphaNoneSkipLast:
                fmt.image_channel_order = CL_RGBA;
                row_bytes *= 4;
                break;
              case kCGImageAlphaPremultipliedFirst:
              case kCGImageAlphaFirst:
                fmt.image_channel_order = CL_ARGB;
                row_bytes *= 4;
                break;
              default:
                fmt.image_channel_order = 0;
            };

            switch (bits_component)
            {
              case 32:
                fmt.image_channel_data_type = (info&kCGBitmapFloatComponents) ? CL_FLOAT : CL_UNSIGNED_INT32;
                row_bytes *= sizeof(float);
                break;
              case 16:
                fmt.image_channel_data_type = (info&kCGBitmapFloatComponents) ? CL_HALF_FLOAT : CL_UNORM_INT16;
                row_bytes *= sizeof(short);
                break;
              case 8:
                fmt.image_channel_data_type = CL_UNORM_INT8;
                break;
            }

            // Create a CL mem for the input image
            cl_int err = 0;

            cl_image_desc desc =
            {
              .image_type        = CL_MEM_OBJECT_IMAGE2D,
              .image_width       = width,
              .image_height      = height,
              .image_depth       = 0,
              .image_array_size  = 0,
              .image_row_pitch   = row_bytes,
              .image_slice_pitch = 0,
              .num_mip_levels    = 0,
              .num_samples       = 0,
              .buffer            = NULL,
            };

            input = clCreateImage(ctx, CL_MEM_READ_ONLY|CL_MEM_COPY_HOST_PTR, &fmt, &desc, (void*)input_ptr, &err);

            CFRelease(input_data);
          } // if

          CFRelease(image);
        } // if
      } // if

      CFRelease(source);
    } // if
  } // if
}

- (void)createOutputMem
{
  glGenTextures(1, &texture);
  glBindTexture(GL_TEXTURE_2D, texture);
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, (GLsizei)width, (GLsizei)height, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);

  cl_int err = 0;
  output = clCreateFromGLTexture(ctx, CL_MEM_WRITE_ONLY, GL_TEXTURE_2D, 0, texture, &err);

  glBindTexture(GL_TEXTURE_2D, 0);
}

- (void)createGeometry
{
  // Screen filling quad
  float screenFillingQuadVertices[] = {
    -1.0f, -1.0f, -0.5f, 1.0f,
    1.0f, -1.0f, -0.5f, 1.0f,
    1.0f,  1.0f, -0.5f, 1.0f,
    -1.0f,  1.0f, -0.5f, 1.0f,
  };
  unsigned int screenFillingQuadIndices[] = { 0, 1, 2, 0, 2, 3 };

  glGenBuffers(1, &screenFillingQuadBuffer);
  glBindBuffer(GL_ARRAY_BUFFER, screenFillingQuadBuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(screenFillingQuadVertices), screenFillingQuadVertices, GL_STATIC_DRAW);

  glGenBuffers(1, &screenFillingQuadIndexBuffer);
  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, screenFillingQuadIndexBuffer);
  glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(screenFillingQuadIndices), screenFillingQuadIndices, GL_STATIC_DRAW);

  glBindBuffer(GL_ARRAY_BUFFER,0);
  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,0);
}

- (void)compileShaders
{
  GLuint vertShader = 0, fragShader = 0;

  screenFillingQuadProgram = glCreateProgram();

  [self compileShader:&vertShader type:GL_VERTEX_SHADER
                 file:[[NSBundle mainBundle]
                       pathForResource:@"quad"
                       ofType:@"vsh"]];

  [self compileShader:&fragShader type:GL_FRAGMENT_SHADER
                 file:[[NSBundle mainBundle]
                       pathForResource:@"quad"
                       ofType:@"fsh"]];

  glAttachShader(screenFillingQuadProgram, vertShader);
  glAttachShader(screenFillingQuadProgram, fragShader);

  glBindAttribLocation(screenFillingQuadProgram, ATTRIB_VERTEX,   "position");
  [self linkProgram:screenFillingQuadProgram];

  uniforms[UNIFORM_TEX] = glGetUniformLocation(screenFillingQuadProgram, "tex");

  glDetachShader(screenFillingQuadProgram, vertShader);
  glDetachShader(screenFillingQuadProgram, fragShader);
  glDeleteShader(vertShader);
  glDeleteShader(fragShader);
}

- (void)compileShader:(GLuint *)shader type:(GLenum)type file:(NSString *)file
{
  GLint status;
  const GLchar *source;

  source = (GLchar *)[[NSString stringWithContentsOfFile:file encoding:NSUTF8StringEncoding error:nil] UTF8String];
  if (!source) {
    NSLog(@"Failed to load vertex shader");
    return;
  }

  *shader = glCreateShader(type);
  glShaderSource(*shader, 1, &source, NULL);
  glCompileShader(*shader);

  GLint logLength;
  glGetShaderiv(*shader, GL_INFO_LOG_LENGTH, &logLength);
  if (logLength > 0) {
    GLchar *log = (GLchar *)malloc(logLength);
    glGetShaderInfoLog(*shader, logLength, &logLength, log);
    NSLog(@"Shader compile log:\n%s", log);
    free(log);
  }

  glGetShaderiv(*shader, GL_COMPILE_STATUS, &status);
  if (status == 0) {
    glDeleteShader(*shader);
    return;
  }
}

- (void)linkProgram:(GLuint)prog
{
  GLint status;
  glLinkProgram(prog);

  GLint logLength;
  glGetProgramiv(prog, GL_INFO_LOG_LENGTH, &logLength);
  if (logLength > 0) {
    GLchar *log = (GLchar *)malloc(logLength);
    glGetProgramInfoLog(prog, logLength, &logLength, log);
    NSLog(@"Program link log:\n%s", log);
    free(log);
  }

  glGetProgramiv(prog, GL_LINK_STATUS, &status);
  if (!status) {
    NSLog(@"Link failed\n");
  }
}

- (void)compileKernel
{
  NSError* error = nil;
  NSString* source = [NSString stringWithContentsOfFile:[[NSBundle mainBundle] pathForResource:@"kernel" ofType:@"cl"] encoding:NSUTF8StringEncoding error:&error];
  const char* sourceStrings[] = { source.UTF8String };

  cl_int err;
  program = clCreateProgramWithSource(ctx, 1, sourceStrings, NULL, &err);

  if ((err = clBuildProgram(program, 1, &device, "-cl-fast-relaxed-math", NULL, NULL))) {

    size_t len;
    clGetProgramBuildInfo(program,device,CL_PROGRAM_BUILD_LOG,0,NULL,&len);
    char log[len];
    clGetProgramBuildInfo(program,device,CL_PROGRAM_BUILD_LOG,sizeof(log),log,NULL);

    printf("Build error:\n%s\n",log);
  }

  kernel = clCreateKernel(program, "processImage", &err);
  clSetKernelArg(kernel, 0, sizeof(input), &input);
  clSetKernelArg(kernel, 1, sizeof(output), &output);
}

- (void)processImage
{
  if (!kernel)
    return;

  // Render the image
  size_t global[] = { width, height };

  size_t max_size;
  clGetKernelWorkGroupInfo(kernel, device, CL_KERNEL_WORK_GROUP_SIZE, sizeof(max_size), &max_size, NULL);

  size_t local[] = { max_size/8, 8 };

#define USE_TIMER 0
#if USE_TIMER
  struct mach_timebase_info timebase = { 0, 0 };
  mach_timebase_info(&timebase);

  clFinish(queue);
  uint64_t start = mach_absolute_time();

  int num = 50;
  for (int i=0;i!=num;++i)
#endif

    clEnqueueNDRangeKernel(queue, kernel, 2, NULL, global, local, 0, NULL, NULL);

#if USE_TIMER
  clFinish(queue);
  float completed = (float)((mach_absolute_time() - start)*timebase.numer)/timebase.denom * 1e-9;

  printf("Kernel execution: %f\n",completed/(float)num);
#else
  clFlush(queue);
#endif

  cl_int err;
  size_t origin[] = { 0, 0, 0 };
  size_t region[] = { width, height, 1 };
  size_t row_pitch;
  size_t slice_pitch;
  void* mapped = clEnqueueMapImage(queue, output, CL_TRUE, CL_MAP_READ, origin, region, &row_pitch, &slice_pitch, 0, NULL, NULL, &err);

  clEnqueueUnmapMemObject(queue, output, mapped, 0, NULL, NULL);

  // Display the image
  glClearColor(0.65f, 0.65f, 0.85f, 1.0f);
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  glDisable(GL_DEPTH_TEST);

  // Draw the background
  glUseProgram(screenFillingQuadProgram);

  glBindTexture(GL_TEXTURE_2D, texture);
  glEnable(GL_TEXTURE_2D);
  glActiveTexture(GL_TEXTURE0);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
  glUniform1i(uniforms[UNIFORM_TEX],0);

  glBindBuffer(GL_ARRAY_BUFFER, screenFillingQuadBuffer);
  glVertexAttribPointer(ATTRIB_VERTEX, 4, GL_FLOAT, GL_FALSE, 0, 0);
  glEnableVertexAttribArray(ATTRIB_VERTEX);

  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, screenFillingQuadIndexBuffer);
  glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

  glFlush();

  [self.view.openGLContext flushBuffer];
}

- (void)dealloc
{
  if (ctx)     clReleaseContext(ctx);
  if (program) clReleaseProgram(program);
  if (kernel)  clReleaseKernel(kernel);
  if (queue)   clReleaseCommandQueue(queue);
  if (input)   clReleaseMemObject(input);
  if (output)  clReleaseMemObject(output);
}

@end
```

[Next](DeviceSelectCLGL-kernel.cl.md)[Previous](DeviceSelectCLGL-AppDelegate.h.md)

