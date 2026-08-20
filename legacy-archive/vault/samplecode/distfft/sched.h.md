---
title: dist_fft
apple_id: DTS10003377
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2004-08-23'
source_url: https://developer.apple.com/library/archive/samplecode/dist_fft/Listings/sched_h.html
archived_at: '2026-07-18T03:29:06.340212Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [dist_fft](distfft.md)


[Next](testmain.c.md)[Previous](sched.c.md)

# sched.h

```
/*
 * Copyright (c) 1997-1999, 2003 Massachusetts Institute of Technology
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 */

#ifndef SCHED_H
#define SCHED_H

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

extern void free_comm_schedule(int **sched, int npes);
extern void empty_comm_schedule(int **sched, int npes);
extern int **make_comm_schedule(int npes);
extern void fill_comm_schedule(int **sched, int npes);
extern int check_comm_schedule(int **sched, int npes);
extern void invert_comm_schedule(int **sched, int npes);
extern void sort_comm_schedule(int **sched, int npes, int sort_pe);
extern void print_comm_schedule(int **sched, int npes);

#ifdef __cplusplus
} /* extern "C" */
#endif /* __cplusplus */

#endif /* SCHED_H */
```

[Next](testmain.c.md)[Previous](sched.c.md)

