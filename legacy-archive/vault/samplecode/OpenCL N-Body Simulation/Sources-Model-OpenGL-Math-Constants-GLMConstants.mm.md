---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Math_Constants_GLMConstants_mm.html
archived_at: '2026-07-18T03:17:42.307409Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Math-Constants-GLMConstants.h.md)[Previous](Sources-Model-OpenGL-Math-Sizes-GLMSizes.mm.md)

# Sources/Model/OpenGL/Math/Constants/GLMConstants.mm

```objc
/*
 <codex>
 <import>GLMConstants.h</import>
 </codex>
 */

#import <cmath>

#import "GLMConstants.h"

GLfloat GLM::kPi_f       = GLfloat(M_PI);
GLfloat GLM::kTwoPi_f    = 2.0f * GLM::kPi_f;
GLfloat GLM::kHalfPi_f   = 0.5f * GLM::kPi_f;
GLfloat GLM::kPiDiv4_f   = 0.25f * GLM::kPi_f;
GLfloat GLM::kPiDiv6_f   = GLM::kPi_f / 6.0f;
GLfloat GLM::k3PiDiv4_f  = (3.0f * GLM::kPi_f) / 4.0f;
GLfloat GLM::k4PiDiv3_f  = (4.0f * GLM::kPi_f) / 3.0f;
GLfloat GLM::k180DivPi_f = 180.0f / GLM::kPi_f;
GLfloat GLM::kPiDiv180_f = GLM::kPi_f / 180.0f;
GLfloat GLM::k360DivPi_f = 360.0f / GLM::kPi_f;
GLfloat GLM::kPiDiv360_f = GLM::kPi_f / 360.0f;
GLfloat GLM::kRadians_f  = GLM::kPi_f / 180.0f;

GLdouble GLM::kPi_d       = GLdouble(M_PI);
GLdouble GLM::kTwoPi_d    = 2.0f * GLM::kPi_d;
GLdouble GLM::kHalfPi_d   = 0.5f * GLM::kPi_d;
GLdouble GLM::kPiDiv4_d   = 0.25f * GLM::kPi_d;
GLdouble GLM::kPiDiv6_d   = GLM::kPi_d / 6.0f;
GLdouble GLM::k3PiDiv4_d  = (3.0f * GLM::kPi_d) / 4.0f;
GLdouble GLM::k4PiDiv3_d  = (4.0f * GLM::kPi_d) / 3.0f;
GLdouble GLM::k180DivPi_d = 180.0f / GLM::kPi_d;
GLdouble GLM::kPiDiv180_d = GLM::kPi_d / 180.0f;
GLdouble GLM::k360DivPi_d = 360.0f / GLM::kPi_d;
GLdouble GLM::kPiDiv360_d = GLM::kPi_d / 360.0f;
GLdouble GLM::kRadians_d  = GLM::kPi_d / 180.0;
```

[Next](Sources-Model-OpenGL-Math-Constants-GLMConstants.h.md)[Previous](Sources-Model-OpenGL-Math-Sizes-GLMSizes.mm.md)

