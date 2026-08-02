---
title: DeviceSelectCLGL
apple_id: DTS40014358
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2014-04-18'
source_url: https://developer.apple.com/library/archive/samplecode/sc1989/Listings/DeviceSelectCLGL_kernel_cl.html
archived_at: '2026-07-26T19:54:14.343038Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeviceSelectCLGL](DeviceSelectCLGL.md)


[Next](DeviceSelectCLGL-main.m.md)[Previous](DeviceSelectCLGL-AppDelegate.m.md)

# DeviceSelectCLGL/kernel.cl

```
/*
     File: kernel.cl
 Abstract:
 OpenCL compute kernel image filter.

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

#define READ_PIXEL(x,y) read_imagef(input_img,CLK_FILTER_NEAREST|CLK_ADDRESS_CLAMP,coord+(int2)((x),(y)))
#define READ_PIXEL_LUM(x,y) convert_to_lum(READ_PIXEL((x),(y)))

float convert_to_lum(const float4 pixel);

kernel void processImage(read_only image2d_t input_img, write_only image2d_t output_img)
{
  const int2 coord = (int2)(get_global_id(0),get_global_id(1));

  const float p0 = READ_PIXEL_LUM(-1,-1);
  const float p1 = READ_PIXEL_LUM( 0,-1);
  const float p2 = READ_PIXEL_LUM( 1,-1);
  const float p3 = READ_PIXEL_LUM(-1, 0);
  const float p4 = READ_PIXEL_LUM( 1, 0);
  const float p5 = READ_PIXEL_LUM(-1,-1);
  const float p6 = READ_PIXEL_LUM( 0,-1);
  const float p7 = READ_PIXEL_LUM( 1,-1);

  const float Gx = p0 - p2 + 2.0f*p3 -2.0f*p4 + p5 - p6;
  const float Gy = p0 + 2.0f*p1 + p2 -p5 -2.0f*p6 - p7;

  const float g = sqrt(Gx*Gx + Gy*Gy);

  float4 pixel = READ_PIXEL(0,0);
  pixel.rgb = g * 8.0f;

  write_imagef(output_img,coord,pixel);
}

float convert_to_lum(const float4 pixel)
{
  return pixel.r*0.2126f + pixel.g*0.7152f + pixel.b*0.0722f;
}
```

[Next](DeviceSelectCLGL-main.m.md)[Previous](DeviceSelectCLGL-AppDelegate.m.md)

