---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/gle_gutil_h.html
archived_at: '2026-07-18T03:29:16.588351Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](gle-intersect.c.md)[Previous](gle-gleosx.h.md)

# gle/gutil.h

```

/*
 * gutil.h
 *
 * FUNCTION:
 * Provide utilities that allow rotation to occur 
 * around any axis.
 * 
 * HISTORY:
 * created by Linas Vepstas  1990
 * added single & double precision, June 1991, Linas Vepstas
 */

#ifndef __GUTIL_H__
#define __GUTIL_H__

#ifdef __GUTIL_DOUBLE
#define gutDouble double
#else
#define gutDouble float  
#endif


#ifdef _NO_PROTO        /* NO ANSI C PROTOTYPING */

/* Rotation Utilities */
extern void rot_axis_f ();
extern void rot_about_axis_f ();
extern void rot_omega_f ();
extern void urot_axis_f ();
extern void urot_about_axis_f ();
extern void urot_omega_f ();

/* double-precision versions */
extern void rot_axis_d ();
extern void rot_about_axis_d ();
extern void rot_omega_d ();
extern void urot_axis_d ();
extern void urot_about_axis_d ();
extern void urot_omega_d ();

/* viewpoint functions */
extern void uview_direction_d ();
extern void uview_direction_f ();
extern void uviewpoint_d ();
extern void uviewpoint_f ();

#else /* _NO_PROTO */       /* ANSI C PROTOTYPING */

/* Rotation Utilities */
extern void rot_axis_f (float omega, float axis[3]);
extern void rot_about_axis_f (float angle, float axis[3]);
extern void rot_omega_f (float axis[3]);
extern void urot_axis_f (float m[4][4], float omega, float axis[3]);
extern void urot_about_axis_f (float m[4][4], float angle, float axis[3]);
extern void urot_omega_f (float m[4][4], float axis[3]);

/* double-precision versions */
extern void rot_axis_d (double omega, double axis[3]);
extern void rot_about_axis_d (double angle, double axis[3]);
extern void rot_omega_d (double axis[3]);
extern void urot_axis_d (double m[4][4], double omega, double axis[3]);
extern void urot_about_axis_d (double m[4][4], double angle, double axis[3]);
extern void urot_omega_d (double m[4][4], double axis[3]);

/* viewpoint functions */
extern void uview_direction_d (double m[4][4],      /* returned */
                        double v21[3],      /* input */
                        double up[3]);      /* input */

extern void uview_direction_f (float m[4][4],       /* returned */
                        float v21[3],       /* input */
                        float up[3]);       /* input */

extern void uviewpoint_d (double m[4][4],       /* returned */
                   double v1[3],        /* input */
                   double v2[3],        /* input */
                   double up[3]);       /* input */

extern void uviewpoint_f (float m[4][4],        /* returned */
                   float v1[3],     /* input */
                   float v2[3],     /* input */
                   float up[3]);        /* input */

#endif /* _NO_PROTO */

#endif /* _GUTIL_H__ */

/* ------------------- end of file ---------------------- */
```

[Next](gle-intersect.c.md)[Previous](gle-gleosx.h.md)

