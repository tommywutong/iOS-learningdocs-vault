---
title: 'Quadrature: Computing the integral of functions using the Accelerate framework'
apple_id: TP40017326
resource_type: Sample Code
platform: iOS|macOS
topic: Mathematical Computation
technology: Accelerate
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuadratureSample/Listings/Quadrature_c.html
archived_at: '2026-07-18T03:21:24.834281Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quadrature: Computing the integral of functions using the Accelerate framework](Quadrature-%20Computing%20the%20integral%20of%20functions%20using%20the%20Accelerate%20framework.md)


[Next](README.md.md)[Previous](Quadrature-%20Computing%20the%20integral%20of%20functions%20using%20the%20Accelerate%20framework.md)

# Quadrature.c

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This sample shows how to use the Quadrature library to compute the definite integral of a function.
*/

// Quadrature is part of the Accelerate framework
#include <Accelerate/Accelerate.h>

// Function to integrate.
// It should compute Y[I] = F(X[I]) for I=0..N-1.
void sinx_over_x(void * arg,size_t n,const double * x,double * y)
{
  for (size_t i=0;i<n;i++)
  {
    double xi = x[i];
    y[i] = (xi == 0.0)?1.0:(sin(xi)/xi);             // sin(x)/x, or 1 at x=0
  }
}

int main(int argc, const char * argv[])
{
  // Function to integrate
  quadrature_integrate_function f;
  f.fun = sinx_over_x;                               // Called to evaluate the function to integrate
  f.fun_arg = NULL;                                  // Passed as first argument to the callback

  // Integration options
  quadrature_integrate_options options;
  bzero(&options,sizeof(options));
  options.integrator = QUADRATURE_INTEGRATE_QAGS;    // Use QAGS: adaptive subdivision with convergence acceleration
  options.abs_tolerance = 1.0e-8;                    // Requested absolute tolerance on result
  options.max_intervals = 20;                        // Max number of intervals

  // Receive status and absolute error
  quadrature_status status;
  double abs_error;

  // Compute the integral of F between 0 and 2*PI
  double result = quadrature_integrate(&f, 0, 2.0 * M_PI, &options, &status, &abs_error, 0, NULL);

  // Always check the status, because we may not have been able to reach the requested tolerance
  if (status != QUADRATURE_SUCCESS) fprintf(stderr,"Integration failed with error %d\n",status);

  printf("Result: %.14f  Abs. error: %.4g\n",result,abs_error);
  return 0;
}
```

[Next](README.md.md)[Previous](Quadrature-%20Computing%20the%20integral%20of%20functions%20using%20the%20Accelerate%20framework.md)

