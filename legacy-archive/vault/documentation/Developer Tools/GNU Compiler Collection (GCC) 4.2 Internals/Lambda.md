---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Lambda.html
archived_at: '2026-07-15T07:31:02.193901Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Dependency analysis](Dependency-analysis.md#apple-irsxazlomrsw4y3zfvqw4ylmpfzws4y),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.9 Linear loop transformations framework

Lambda is a framework that allows transformations of loops using
non-singular matrix based transformations of the iteration space and
loop bounds. This allows compositions of skewing, scaling, interchange,
and reversal transformations. These transformations are often used to
improve cache behavior or remove inner loop dependencies to allow
parallelization and vectorization to take place.

To perform these transformations, Lambda requires that the loopnest be
converted into a internal form that can be matrix transformed easily.
To do this conversion, the function
`gcc_loopnest_to_lambda_loopnest` is provided. If the loop cannot
be transformed using lambda, this function will return NULL.

Once a `lambda_loopnest` is obtained from the conversion function,
it can be transformed by using `lambda_loopnest_transform`, which
takes a transformation matrix to apply. Note that it is up to the
caller to verify that the transformation matrix is legal to apply to the
loop (dependence respecting, etc). Lambda simply applies whatever
matrix it is told to provide. It can be extended to make legal matrices
out of any non-singular matrix, but this is not currently implemented.
Legality of a matrix for a given loopnest can be verified using
`lambda_transform_legal_p`.

Given a transformed loopnest, conversion back into gcc IR is done by
`lambda_loopnest_to_gcc_loopnest`. This function will modify the
loops so that they match the transformed loopnest.
