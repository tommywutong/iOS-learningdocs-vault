---
title: 'Basic Neural Network Subroutines: Using The Accelerate Framework''s Convolution
  Filters'
apple_id: TP40017299
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/BasicNeuralNetworkSubroutines/Listings/main_c.html
archived_at: '2026-07-18T03:01:49.830789Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Basic Neural Network Subroutines: Using The Accelerate Framework's Convolution Filters](Basic%20Neural%20Network%20Subroutines-%20Using%20The%20Accelerate%20Framework%27s%20Convolution%20F.md)


[Next](README.md.md)[Previous](Basic%20Neural%20Network%20Subroutines-%20Using%20The%20Accelerate%20Framework%27s%20Convolution%20F.md)

# main.c

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This sample creates a random image stack and a convolution filter, then applies the convolution filter to obtain a second image stack.
*/

// BNNS is part of the Accelerate framework
#include <Accelerate/Accelerate.h>
#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
#include <string.h>

// Fill BUF[N] with random values in [-1,+1]
void random_buffer(size_t n, float * buf)
{
  const float k = 2.0f / (float)RAND_MAX;
  for (size_t i=0;i<n;i++) buf[i] = (float)rand() * k - 1.0f;
}

// Return wall clock time
double get_time()
{
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return (double)tv.tv_sec + 1.0e-6 * (double)tv.tv_usec;
}

int main(int argc, const char * argv[])
{
  // Description of the input image stack
  // Input image stack has 80 channels of 200x200 pix images
  BNNSImageStackDescriptor i_desc;
  bzero(&i_desc,sizeof(i_desc));
  i_desc.width = 100;                           // image width: 100 pix
  i_desc.height = 100;                          // image height: 100 pix
  i_desc.channels = 80;                         // number of channels: 80
  i_desc.row_stride = 120;                      // each row is stored on 120 pix
  i_desc.image_stride = 120*120;                // each channel is stored on 120*120 pix
  i_desc.data_type = BNNSDataTypeFloat32;       // pixels values are 'float'
  printf("Input image stack: %zu x %zu x %zu\n",i_desc.width,i_desc.height,i_desc.channels);

  // Description of the output image stack
  // Output image stack has 120 channels of 196x196 pix images
  BNNSImageStackDescriptor o_desc;
  bzero(&o_desc, sizeof(o_desc));
  o_desc.width = 96;                            // image width: 96 pix
  o_desc.height = 96;                           // image height: 96 pix
  o_desc.channels = 120;                        // number of channels: 120
  o_desc.row_stride = 96;                       // each row is stored on 96 pix
  o_desc.image_stride = 96*96;                  // each channel is stored on 96*96 pix
  o_desc.data_type = BNNSDataTypeFloat32;       // pixels values are 'float'
  printf("Output image stack: %zu x %zu x %zu\n",o_desc.width,o_desc.height,o_desc.channels);

  // Description of the convolution layer
  BNNSConvolutionLayerParameters layer_params;
  bzero(&layer_params, sizeof(layer_params));
  layer_params.k_width = 5;                     // convolution kernel width: 5 pix
  layer_params.k_height = 5;                    // convolution kernel height: 5 pix
  layer_params.in_channels = i_desc.channels;   // input channels
  layer_params.out_channels = o_desc.channels;  // output channels
  layer_params.x_stride = 1;                    // x stride: 1 pix
  layer_params.y_stride = 1;                    // y stride: 1 pix
  layer_params.x_padding = 0;                   // x padding: 0 pix
  layer_params.y_padding = 0;                   // y padding: 0 pix
  printf("Convolution kernel: %zu x %zu\n",layer_params.k_width,layer_params.k_height);

  // Number of floating point ops
  double n_flops = 2.0 * layer_params.k_width * layer_params.k_height * i_desc.channels * o_desc.channels * o_desc.width * o_desc.height;
  printf("Convolution floating point operations: %.2f millions\n",n_flops * 1.0e-6);

  // Allocate weights buffer. For a 5x5 convolution, we need 5 * 5 * input channels * output channels weights.
  size_t n_weights = layer_params.k_width * layer_params.k_height * layer_params.in_channels * layer_params.out_channels;
  float * weights = (float *)calloc(n_weights,sizeof(float));

  // Initialize weights to random values
  random_buffer(n_weights, weights);

  // Attach weight buffer to layer parameters
  layer_params.weights.data = weights;
  layer_params.weights.data_type = BNNSDataTypeFloat32;

  // Common filter parameters
  BNNSFilterParameters filter_params;
  bzero(&filter_params, sizeof(filter_params));

  // Create a new convolution layer filter
  BNNSFilter filter = BNNSFilterCreateConvolutionLayer(&i_desc,&o_desc,&layer_params,&filter_params);
  if (filter == NULL) { fprintf(stderr,"BNNSFilterCreateConvolutionLayer failed\n"); exit(1); }

  // Allocate input stack
  float * i_stack = (float *)calloc(i_desc.image_stride * i_desc.channels, sizeof(float));

  // Initialize input stack to random values
  for (size_t channel = 0; channel < i_desc.channels; channel++)  // loop on stack channels
  {
    for (size_t row = 0; row < i_desc.height; row++)  // loop on image row
    {
      random_buffer(i_desc.width,i_stack + row * i_desc.row_stride + channel * i_desc.image_stride);  // fill one row
    }
  }

  // Allocate output stack
  float * o_stack = (float *)calloc(o_desc.image_stride * o_desc.channels, sizeof(float));

  // Get initial time
  double t0 = get_time();

  // Apply filter to input stack. Result is written in output stack.
  int status = BNNSFilterApply(filter, i_stack, o_stack);
  if (status != 0) fprintf(stderr,"BNNSFilterApply failed\n");

  // Get final time and report
  double t1 = get_time();
  printf("T = %.1f ms: %.1f Gflop/s\n",(t1 - t0)*1e3,n_flops*1e-9/(t1-t0));

  // Release resources
  BNNSFilterDestroy(filter);
  free(i_stack);
  free(o_stack);
  free(weights);

  return 0;
}
```

[Next](README.md.md)[Previous](Basic%20Neural%20Network%20Subroutines-%20Using%20The%20Accelerate%20Framework%27s%20Convolution%20F.md)

