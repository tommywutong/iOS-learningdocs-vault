---
title: Universal Binary Programming Guidelines, Second Edition
apple_id: TP40002217
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_matrix_a/universal_binary_matrix_a.html
archived_at: '2026-07-15T08:16:38.155194Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Universal Binary Programming Guidelines, Second Edition](Introduction.md)


[Next](32-Bit%20Application%20Binary%20Interface.md)[Previous](Rosetta.md)

# Architecture-Independent Vector-Based Code

The intention of this appendix is to show how to factor a mathematical calculation into architecture-independent and architecture-specific parts. Using matrix multiplication as an example, you’ll see how to write a function that works for both the PowerPC and the x86 architectures with a minimum of architecture-specific coding. You can then apply this approach to other, more complex mathematical calculations.

The following basic operations are available on both architectures:

- Vector loads and stores
- Multiplication
- Addition
- An instruction to splat a float across a vector

For other types of calculations, you may need to write separate versions of code. Because of the differences in the number of registers and the pipeline depths between the two architectures, it is often advantageous to provide separate versions.

[Listing B-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwtembsgm4de) shows the architecture-specific code you need to support matrix multiplication. The code calls the architecture-independent function `MyMatrixMultiply`, which is shown in [Listing B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwtembtg43de). The code shown in Listing B-1 works properly for both instruction set architectures only if you build the code as a universal binary. For more information, see [Building a Universal Binary](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywviucykjcummjqge).

__Listing B-1__  Architecture-specific code needed to support matrix multiplication

```c
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

// For each vector architecture...
#if defined( __VEC__ )
// AltiVec
    // Set up a vector type for a float[4] array for each vector  type
    typedef vector float vFloat;

    // Define some macros to map a virtual SIMD language to
    // each actual SIMD language. For matrix multiplication, the  tasks
    // you need to perform are essentially the same between the  two
    // instruction set architectures (ISA).
    #define vSplat( v, i )  ({ vFloat z = vec_splat( v, i );
                                /* return */ z; })
    #define vMADD                   vec_madd
    #define vLoad( ptr )        vec_ld( 0, ptr )
    #define vStore( v, ptr )    vec_st( v, 0, ptr )
    #define vZero() (vector float) vec_splat_u32(0)

#elif defined( __SSE__ )
// SSE
    // The header file xmmintrin.h defines C functions for using
    // SSE and SSE2 according to the Intel C programming interface
    #include <xmmintrin.h>

    // Set up a vector type for a float[4] array for each vector  type
    typedef __m128  vFloat;

    // Also define some macros to map a virtual SIMD language to
    // each actual SIMD language.

    // Note that because i MUST be an immediate, it is incorrect  here
    // to alias i to a stack based copy and replicate that 4 times.
    #define vSplat( v, i )({ __m128 a = v; a = _mm_shuffle_ps( a,  a, \
                             _MM_SHUFFLE(i,i,i,i) ); /* return */  a; })
    inline __m128 vMADD( __m128 a, __m128 b, __m128 c )
    {
        return _mm_add_ps( c, _mm_mul_ps( a, b ) );
    }
    #define vLoad( ptr )    _mm_load_ps( (float*) (ptr) )
    #define vStore( v, ptr )    _mm_store_ps( (float*) (ptr),  v )
    #define vZero()             _mm_setzero_ps()

#else
// Scalar
    #warning To compile vector code, you must specify -faltivec,
                -msse, or both- faltivec and -msse
    #warning Compiling for scalar code.

    // Some scalar equivalents to show what the above vector
    // versions accomplish

    // A vector, declared as a struct with 4 scalars
    typedef struct
    {
        float               a;
        float               b;
        float               c;
        float               d;
    }vFloat;

    // Splat element i across the whole vector and return it
    #define vSplat( v, i )  ({ vFloat z; z.a = z.b = z.c = z.d =  ((float*)
                             &v)[i]; /* return */ z; })

 // Perform a fused-multiply-add operation on architectures that  support it
    // result = X * Y + Z
    inline vFloat vMADD( vFloat X, vFloat Y, vFloat Z )
    {
        vFloat result;

        result.a = X.a * Y.a + Z.a;
        result.b = X.b * Y.b + Z.b;
        result.c = X.c * Y.c + Z.c;
        result.d = X.d * Y.d + Z.d;

        return result;
    }

    // Return a vector that starts at the given address
    #define vLoad( ptr )  ( (vFloat*) ptr )[0]

    // Write a vector to the given address
    #define vStore( v, ptr )    ( (vFloat*) ptr )[0] = v

    // Return a vector full of zeros
    #define vZero()     ({ vFloat z; z.a = z.b = z.c = z.
                            d = 0.0f; /* return */ z; })

#endif

// Prototype for a vector matrix multiply function
void MyMatrixMultiply( vFloat A[4], vFloat B[4], vFloat C[4] );

int main( void )
{
    // The vFloat type (defined previously) is a vector or scalar  array
    // that contains 4 floats
    // Thus each one of these is a 4x4 matrix, stored in the C storage  order.
    vFloat          A[4];
    vFloat          B[4];
    vFloat          C1[4];
    vFloat          C2[4];
    int i, j, k;

    // Pointers to the elements in A, B, C1 and C2
    float *a = (float*) &A;
    float *b = (float*) &B;
    float *c1 = (float*) &C1;
    float *c2 = (float*) &C2;

    // Initialize the data
    for( i = 0; i < 16; i++ )
    {
        a[i] = (double) (rand() - RAND_MAX/2) / (double) (RAND_MAX  );
        b[i] = (double) (rand() - RAND_MAX/2) / (double) (RAND_MAX  );
        c1[i] = c2[i] = 0.0;
    }

    // Perform the brute-force version of matrix multiplication
    // and use this later to check for correctness
    printf( "Doing simple matrix multiply...\n" );
    for( i = 0; i < 4; i++ )
        for( j = 0; j < 4; j++ )
        {
            float result = 0.0f;

            for( k = 0; k < 4; k++ )
                result += a[ i * 4 + k] * b[ k * 4 + j ];

            c1[ i * 4 + j ] = result;
        }

    // The vector version
    printf( "Doing vector matrix multiply...\n" );
    MyMatrixMultiply( A, B, C2 );

    // Make sure that the results are correct
    // Allow for some rounding error here
    printf( "Verifying results..." );
    for( i = 0 ; i < 16; i++ )
        if( fabs( c1[i] - c2[i] ) > 1e-6 )
            printf( "failed at %i,%i: %8.17g %8.17g\n",  i/4,
                         i&3, c1[i], c2[i] );

    printf( "done.\n" );

    return 0;
}
```

The 4x4 matrix multiplication algorithm shown in [Listing B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwtembtg43de) is a simple matrix multiplication algorithm performed with four columns in parallel. The basic calculation is as follows:

`C[i][j] = sum( A[i][k] * B[k][j], k = 0... width of A )`

It can be rewritten in mathematical vector notation for rows of C as the following:

`C[i][] = sum( A[i][k] * B[k][], k = 0... width of A )`

Where:

- `C[i][]` is the _i_th row of C
- `A[i][k]` is the element of _A_ at row _i_ and column _k_
- `B[k][]` is the _k_th row of _B_

An example calculation for `C[0][]` is as follows:

_C[0][] = A[0][0] \* B[0][] + A[0][1] \* B[1][] + A[0][2] \* B[2][] + A[0][3] \* B[3][]_

This calculation is simply a multiplication of a scalar times a vector, followed by addition of similar elements between two vectors, repeated four times, to get a vector that contains four sums of products. Performing the calculation in this way saves you from transposing B to obtain the B columns, and also saves you from adding across vectors, which is inefficient. All operations occur between similar elements of two different vectors.

[Listing B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwtembtg43de) shows architecture-independent vector code that performs matrix multiplication. This code compiles as scalar if you do not set up the appropriate compiler flags for PowerPC (`-faltivec`) or x86 (`-msse`), or if AltiVec is unavailable on the PowerPC. The matrices used in the `MyMatrixMultply` function assume the C storage order for 2D arrays, not the FORTRAN storage order.

__Listing B-2__  Architecture-independent code that performs matrix multiplication

```
void MyMatrixMultiply( vFloat A[4], vFloat B[4], vFloat C[4] )
{
    vFloat A1 = vLoad( A );         //Row 1 of A
    vFloat A2 = vLoad( A + 1 );     //Row 2 of A
    vFloat A3 = vLoad( A + 2 );     //Row 3 of A
    vFloat A4 = vLoad( A + 3);      //Row 4 of A
    vFloat C1 = vZero();         //Row 1 of C, initialized to zero
    vFloat C2 = vZero();         //Row 2 of C, initialized to zero
    vFloat C3 = vZero();         //Row 3 of C, initialized to zero
    vFloat C4 = vZero();         //Row 4 of C, initialized to zero

    vFloat B1 = vLoad( B );         //Row 1 of B
    vFloat B2 = vLoad( B + 1 );     //Row 2 of B
    vFloat B3 = vLoad( B + 2 );     //Row 3 of B
    vFloat B4 = vLoad( B + 3);      //Row 4 of B

    //Multiply the first row of B by the first column of A (do not  sum across)
    C1 = vMADD( vSplat( A1, 0 ), B1, C1 );
    C2 = vMADD( vSplat( A2, 0 ), B1, C2 );
    C3 = vMADD( vSplat( A3, 0 ), B1, C3 );
    C4 = vMADD( vSplat( A4, 0 ), B1, C4 );

    // Multiply the second row of B by the second column of A and
    // add to the previous result (do not sum across)
    C1 = vMADD( vSplat( A1, 1 ), B2, C1 );
    C2 = vMADD( vSplat( A2, 1 ), B2, C2 );
    C3 = vMADD( vSplat( A3, 1 ), B2, C3 );
    C4 = vMADD( vSplat( A4, 1 ), B2, C4 );

    // Multiply the third row of B by the third column of A and
    // add to the previous result  (do not sum across)
    C1 = vMADD( vSplat( A1, 2 ), B3, C1 );
    C2 = vMADD( vSplat( A2, 2 ), B3, C2 );
    C3 = vMADD( vSplat( A3, 2 ), B3, C3 );
    C4 = vMADD( vSplat( A4, 2 ), B3, C4 );

    // Multiply the fourth row of B by the fourth column of A and
    // add to the previous result (do not sum across)
    C1 = vMADD( vSplat( A1, 3 ), B4, C1 );
    C2 = vMADD( vSplat( A2, 3 ), B4, C2 );
    C3 = vMADD( vSplat( A3, 3 ), B4, C3 );
    C4 = vMADD( vSplat( A4, 3 ), B4, C4 );

    // Write out the result to the destination
    vStore( C1, C );
    vStore( C2, C + 1 );
    vStore( C3, C + 2 );
    vStore( C4, C + 3 );
}
```

[Next](32-Bit%20Application%20Binary%20Interface.md)[Previous](Rosetta.md)

