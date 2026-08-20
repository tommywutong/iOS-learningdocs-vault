---
title: DeviceSelectCL
apple_id: DTS40014356
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2014-04-18'
source_url: https://developer.apple.com/library/archive/samplecode/sc1245/Listings/DeviceSelectCL_AppDelegate_m.html
archived_at: '2026-07-26T19:54:14.143147Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeviceSelectCL](DeviceSelectCL.md)


[Next](DeviceSelectCL-kernel.cl.md)[Previous](DeviceSelectCL-AppDelegate.h.md)

# DeviceSelectCL/AppDelegate.m

```objc
/*
     File: AppDelegate.m
 Abstract:
 App delegate for instantiating i/o surface backed CA layer for OpenCL image filter.

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

#import <QuartzCore/QuartzCore.h>
#import <IOSurface/IOSurface.h>
#import <OpenCL/opencl.h>

#import <mach/mach_time.h>

@interface AppDelegate ()
{
  IOSurfaceRef     surface;

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
  cl_int err = 0;

  //
  // SDK example showing to to choose the device not connected to the display
  // on the 2013 Mac Pro
  //

  // Create a CL context with all devices
  ctx = clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL, NULL, NULL, &err);

  // Load the input file and initialize a cl_mem
  [self loadInputMem];

  // Create an IOSurface for output
  [self createOutputMem];

  // Look for the GPU not connected to the display to use as a compute device.
  CGLRendererInfoObj rend = NULL;

  GLint nrend = 0;
  GLint nonDisplayGPURendererID = 0x0;

  BOOL isDualGPU = NO;

  //
  // Iterate over the renderers, look for one that is not "online" (i.e. not
  // connected to a display), and also supports accelerated compute (i.e. not
  // the software GL renderer)
  //
  CGLError cgl_err = CGLQueryRendererInfo(0xffffffff, &rend, &nrend);

  if(cgl_err == kCGLNoError)
  {
    // Make certain  that we've more than 2 renderers
    isDualGPU = nrend > 2;

    // Iterate through all renderers (i.e., GPUs)
    for(GLint idx=0; idx<nrend; idx++)
    {
      GLint online = 1;

      CGLDescribeRenderer(rend, idx, kCGLRPOnline, &online);

      // To use the display connected GPU, reverse this conditional
      if(!online)
      {
        GLint accelerated = 0;

        CGLDescribeRenderer(rend, idx, kCGLRPAcceleratedCompute, &accelerated);

        if(accelerated)
        {
          CGLDescribeRenderer(rend, idx, kCGLRPRendererID, &nonDisplayGPURendererID);
          break;
        } // if
      } // if
    } // for

    CGLDestroyRendererInfo(rend);
  } // if

  //
  // Transform the renderer ID into a cl_device_id by masking away the lower byte
  //
  cl_device_id nonDisplayCLDeviceId = (cl_device_id)(intptr_t)(nonDisplayGPURendererID&~0xff);

  device = nonDisplayCLDeviceId;

  //
  // Create a command queue on this device
  //
  queue = clCreateCommandQueue(ctx, device, 0, &err);

  // Get the device name length
  size_t len = 0;

  clGetDeviceInfo(device, CL_DEVICE_NAME, 0, NULL, &len);

  // Get the device name c-string
  char device_name[len];

  clGetDeviceInfo(device, CL_DEVICE_NAME, sizeof(device_name), device_name, NULL);

  // Is this a AMD D300 cl compute device?
  const char *isD300 = strstr(device_name, "D300");

  // Is this a AMD D500 cl compute device?
  const char *isD500 = strstr(device_name, "D500");

  // Is this a AMD D700 cl compute device?
  const char *isD700 = strstr(device_name, "D700");

  // Is this one of the AMD cl compute device?
  BOOL isAMD = (isD300 != NULL) || (isD500 != NULL) || (isD700 != NULL);

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

    // Release all valid OpenCL resources
    if (ctx)     clReleaseContext(ctx);
    if (queue)   clReleaseCommandQueue(queue);
    if (input)   clReleaseMemObject(input);
    if (output)  clReleaseMemObject(output);

    // Since the MacPro requirements are not meet,
    // exit from this application
    exit(-1);
  } // if

  fprintf(stdout, ">> Using: OpenCL device id %p\n",device);
  fprintf(stdout, ">> Using: OpenCL device \"%s\"\n",device_name);

  // Load the CL kernel
  [self compileKernel];

  // Process the output image
  [self processImage];
}

- (void)loadInputMem
{
  // Load the input file
  NSURL* url = [[NSBundle mainBundle] URLForImageResource:@"Zebra"];

  if(url)
  {
    CGImageSourceRef source = CGImageSourceCreateWithURL( (__bridge CFURLRef)url, NULL);

    if (source != NULL)
    {
      NSDictionary *options = [NSDictionary dictionaryWithObject: (id)kCFBooleanTrue
                                                          forKey: (id) kCGImageSourceShouldCache];

      if(options)
      {
        CGImageRef image = CGImageSourceCreateImageAtIndex(source, 0, (__bridge CFDictionaryRef)options);

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

#define SET_INT_VALUE(dict,key,exp)\
{\
int val = (exp);\
CFNumberRef n = CFNumberCreate(kCFAllocatorMallocZone,kCFNumberIntType,&(val));\
CFDictionarySetValue(dict,key,n);\
CFRelease(n);\
}

- (void)createOutputMem
{
  CFMutableDictionaryRef dict = CFDictionaryCreateMutable(kCFAllocatorMallocZone, 8,
                                                          &kCFTypeDictionaryKeyCallBacks,
                                                          &kCFTypeDictionaryValueCallBacks);

  size_t pixel_size = 4;

  SET_INT_VALUE(dict,kIOSurfaceWidth,(int)width);
  SET_INT_VALUE(dict,kIOSurfaceHeight,(int)height);
  SET_INT_VALUE(dict,kIOSurfaceBytesPerRow,(int)(width*pixel_size));
  SET_INT_VALUE(dict,kIOSurfaceBytesPerElement,(int)pixel_size);
  SET_INT_VALUE(dict,kIOSurfacePixelFormat,(int)kCVPixelFormatType_32ARGB);

  surface = IOSurfaceCreate(dict);

  CFRelease(dict);

  // Create a mem for the incoming IOSurface
  cl_int err = 0;

  cl_image_format fmt =
  {
    .image_channel_order     = CL_ARGB,
    .image_channel_data_type = CL_UNORM_INT8
  };

  output = clCreateImageFromIOSurface2DAPPLE(ctx, CL_MEM_WRITE_ONLY, &fmt, width, height, surface, &err);
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

  // Display the image
  self.view.wantsLayer = YES;
  CALayer* layer = self.view.layer;

  [CATransaction begin];

  layer.backgroundColor      = CGColorGetConstantColor(kCGColorBlack);
  layer.edgeAntialiasingMask = 0;
  layer.masksToBounds        = YES;

  [layer insertSublayer:[CALayer layer] atIndex:0];

  CALayer* outputLayer = [[layer sublayers] objectAtIndex:0];

  [outputLayer setFrame:[layer frame]];
  [outputLayer setContents:(__bridge id)(surface)];
  [outputLayer setContentsGravity:kCAGravityResizeAspect];
  [outputLayer setAutoresizingMask:kCALayerWidthSizable|kCALayerHeightSizable];

  [CAConstraint constraintWithAttribute:kCAConstraintMidX relativeTo:@"superlayer" attribute:kCAConstraintMidX];
  [CAConstraint constraintWithAttribute:kCAConstraintMidY relativeTo:@"superlayer" attribute:kCAConstraintMidY];
  [CAConstraint constraintWithAttribute:kCAConstraintWidth relativeTo:@"superlayer" attribute:kCAConstraintWidth];
  [CAConstraint constraintWithAttribute:kCAConstraintHeight relativeTo:@"superlayer" attribute:kCAConstraintHeight];

  [layer setContentsGravity:kCAGravityResizeAspect];

  [CATransaction commit];

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

[Next](DeviceSelectCL-kernel.cl.md)[Previous](DeviceSelectCL-AppDelegate.h.md)

