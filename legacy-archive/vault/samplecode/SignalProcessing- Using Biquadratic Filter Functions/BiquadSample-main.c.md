---
title: 'SignalProcessing: Using Biquadratic Filter Functions'
apple_id: TP40016163
resource_type: Sample Code
platform: macOS
topic: null
technology: Accelerate
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/SignalProcessing/Listings/BiquadSample_main_c.html
archived_at: '2026-07-18T03:23:46.539036Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SignalProcessing: Using Biquadratic Filter Functions](SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md)


[Next](README.md.md)[Previous](SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md)

# BiquadSample/main.c

```c
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    vDSP_biquadm usage example. This sample shows how to use vDSP_biquadm to process a stereo signal through an IIR filter consisting of 4 cascaded biquad sections. Half of the signal will be processed under one set of coefficients and the second half of the signal will be processed using a different set of coefficients. vDSP_biquadm_SetTargetsDouble will be used to update the filter coefficients. The input channels are interleaved.
*/

#include <stdlib.h>
#include <Accelerate/Accelerate.h>

// Filter coefficients for each channel (channel 0 and channel 1).
//  B coefficients are the feed-forward coefficients for each section (i.e. b0, b1, b2)
//  A coefficients are the feed-back coefficients for each section (i.e. a0 (always assumed to be 1), a1, a2)

// B coefficients for channel 0
static const float B0[] = {
    0.984764420,    -1.969528840,   0.984764420,
    0.977712906,    -1.955425811,   0.977712906,
    0.998549912,    -1.969041291,   0.986303756,
    0.990002419,    -0.908952874,   0.881103728
};

// A coefficients for channel 0
static const float A0[] = {
    1.000000000,    -1.969331359,   0.969726321,
    1.000000000,    -1.955243388,   0.955608234,
    1.000000000,    -1.969041291,   0.984853668,
    1.000000000,    -0.908952874,   0.871106147
};

// B coefficients for channel 1
static const float B1[] = {
    0.984764420,    -1.969528840,   0.984764420,
    0.977712906,    -1.955425811,   0.977712906,
    0.999262098,    -1.983019787,   0.993476599,
    0.983015517,    -1.728018843,   0.952885462
};

// A coefficients for channel 1
static const float A1[] = {
    1.000000000,    -1.969331359,   0.969726321,
    1.000000000,    -1.955243388,   0.955608234,
    1.000000000,    -1.983019787,   0.992738697,
    1.000000000,    -1.728018843,   0.935900979
};

/*
 We will use vDSP_biquadm_SetTargetsDouble to update the filter coefficients. We will update
 only the coefficients in the second channel (channel 1) for the two middle sections.  Unlike
 vDSP_biquadm_SetCoefficientsDouble, SetTargets does not update the coefficients immediately.
 The coefficients are updated during processing on a per-sample basis.
 */

// New coefficients for channel 1
static const float B1New[] = {
    /*B1[3*0+0],       B1[3*0+1],     B1[3*0+2],*/
    0.985741670,    -1.688906290,   0.953772625,
    0.959492493,    -1.800065496,   0.930225572,
    /*B1[3*3+0],       B1[3*3+1],     B1[3*3+2] */
};

static const float A1New[] = {
    /*A1[3*0+0],        A1[3*0+1],    A1[3*0+2],*/
    1.000000000,    -1.688906290,   0.939514295,
    1.000000000,    -1.800065496,   0.889718065,
    /*A1[3*3+0],        A1[3*3+1],    A1[3*3+2] */
};

/*
 The filter coefficients are updated incrementally so we need to know how close we want
 to get to our targets.  If we process a sufficiently large number of samples then all of
 the filter coefficients will be within this threshold of the targets.
 */
static const float threshold = 0.05;

/*
 We also need to know how 'fast' we want to iterate our filter coefficients towards the
 targets.  This number, between 0 and 1, will specify that.
 */
static const float rate = 0.4;

int main()
{
    // We're processing a stereo signal, so 2 channels.
    vDSP_Length Channels = 2;

    // Our filter consists of 4 cascaded sections using the filter coefficients specified
    //  above, and in the order specified above.
    vDSP_Length Sections = 4;

    //  An example input of length 1024, just use random data.
    vDSP_Length N = 1024;
    float *Input = malloc(N * Channels * sizeof *Input);

    // We're filling the input buffer sequentially for demonstration purposes, but conceptually the data is interleaved
    // i.e. Input[2*i], i=0:1023, is the channel 0 data and Input[2*i+1],i=0:1023 is the channel 1 data.
    for (vDSP_Length i = 0; i < N*Channels; ++i)
        Input[i] = (float)rand()/(float)RAND_MAX;

    //  A buffer to store our output
    float *Output = malloc(N * Channels * sizeof *Output);

    // vDSP_biquadm requires our filter coefficients in a particular format.
    // First, allocate some memory to hold the coefficients in the right format.  There are 5 coefficients
    // per section, 4 sections per channel, and 2 channels, so we need to hold 5*4*2 coefficients total.
    double *F = malloc(5*Channels*Sections*sizeof *F);

    // Coefficients are ordered by section, then channel, i.e. "section-major ordering".  Each section holds its coefficients as [b0 b1 b2 a1 a2]
    //  (as mentioned above, a0 is always assumed to be 1).  So, if you lay it out as a matrix:
    //
    //                      Channel 0           Channel 1
    //  Section0        [b0 b1 b2 a1 a2     b0 b1 b2 a1 a2
    //  Section1         b0 b1 b2 a1 a2     b0 b1 b2 a1 a2
    //  Section2         b0 b1 b2 a1 a2     b0 b1 b2 a1 a2
    //  Section3         b0 b1 b2 a1 a2     b0 b1 b2 a1 a2]

    // Lay out channel 0:
    for (vDSP_Length j = 0; j < Sections; ++j)
    {
        F[j*Channels*5 + 0*5 + 0] = B0[3*j + 0];    //b0
        F[j*Channels*5 + 0*5 + 1] = B0[3*j + 1];    //b1
        F[j*Channels*5 + 0*5 + 2] = B0[3*j + 2];    //b2
        F[j*Channels*5 + 0*5 + 3] = A0[3*j + 1];    //a1
        F[j*Channels*5 + 0*5 + 4] = A0[3*j + 2];    //a2
    }

    // Lay out channel 1:
    for (vDSP_Length j = 0; j < Sections; ++j)
    {
        F[j*Channels*5 + 1*5 + 0] = B1[3*j + 0];    //b0
        F[j*Channels*5 + 1*5 + 1] = B1[3*j + 1];    //b1
        F[j*Channels*5 + 1*5 + 2] = B1[3*j + 2];    //b2
        F[j*Channels*5 + 1*5 + 3] = A1[3*j + 1];    //a1
        F[j*Channels*5 + 1*5 + 4] = A1[3*j + 2];    //a2
    }

    // vDSP_biquadm takes an array of pointers to each input/output channel.  Since our data is
    // interleaved and it is set up so that channel 0 data is in Input[2*i] and channel 1 data is in
    // Input[2*i+1], i=0:1023, our pointer to channel 0 data is Input and our pointer to channel 1 data
    // is Input+1.  The stride between samples of a given channel is 2.

    // Set up pointers to input and output pointers as an array:
    float *pInputs[2] = {Input, Input+1};
    float *pOutputs[2] = {Output, Output+1};

    // Construct a vDSP_biquadm_Setup object using the filters 'F', the number of sections 'Sections' and
    //  the number of channels 'Channels':
    vDSP_biquadm_Setup Setup = vDSP_biquadm_CreateSetup(F, Sections, Channels);

    // We will process the input in three steps.
    //  1:  Process a portion of the input under the original coefficients which we
    //      just used to construct the filter.
    //  2:  Set the targets to the new coefficients B1New and A1New.  As noted
    //      above, these will apply only to channel 1 and sections 1 and 2.
    //  3:  Process the remaining input frames.  The coefficients will iterate towards
    //      the targets during processing.

    vDSP_Length NPart0 = 300;           // Number of frames to process under the original coefficients.
    vDSP_Length NPart1 = N - NPart0;    // Number of frames to process under the updated coefficients.

    // Execute the filter using the setup we just created 'Setup', the array of input pointers 'pInput', the
    // stride between samples (2), the array of output pointers 'pOutputs', the stride between output samples (2),
    // and the input sample length 'NPart0'.
    vDSP_biquadm(Setup, (const float**)pInputs, 2, pOutputs, 2, NPart0);

    // Now update the filter coefficients.  The coefficients need to be laid out in the same
    // pattern as expected by CreateSetup.  In practice we would already have the coefficients
    // laid out in this pattern for efficiency, but for this example we will re-use our 'F'
    // buffer to pass our new coefficients to SetCoefficientsDouble.

    // We also need some parameters to establish the set of channels and sections we are updating.
    vDSP_Length FirstSectionToUpdate        = 1;
    vDSP_Length NumberOfSectionsToUpdate    = 2;

    vDSP_Length FirstChannelToUpdate        = 1;
    vDSP_Length NumberOfChannelsToUpdate    = 1;

    // Note that the array of coefficients expected by SetCoefficientsDouble contains
    // only the updated coefficients, i.e. the original 'F' array passed to CreateSetup
    // began with coefficients for channel 0; this 'F' array will NOT begin with coefficients
    // for channel 0, but for channel 1.  And only for the updated sections, sections 1 and 2.
    for (vDSP_Length j = 0; j < NumberOfSectionsToUpdate; ++j)
    {
        F[j*NumberOfChannelsToUpdate*5 + 0*5 + 0] = B1New[3*j + 0];    //b0
        F[j*NumberOfChannelsToUpdate*5 + 0*5 + 1] = B1New[3*j + 1];    //b1
        F[j*NumberOfChannelsToUpdate*5 + 0*5 + 2] = B1New[3*j + 2];    //b2
        F[j*NumberOfChannelsToUpdate*5 + 0*5 + 3] = A1New[3*j + 1];    //a1
        F[j*NumberOfChannelsToUpdate*5 + 0*5 + 4] = A1New[3*j + 2];    //a2
    }

    // Now update the filter
    vDSP_biquadm_SetTargetsDouble(Setup, F, rate, threshold,
                                  FirstSectionToUpdate,
                                  FirstChannelToUpdate,
                                  NumberOfSectionsToUpdate,
                                  NumberOfChannelsToUpdate);

    // And complete the processing.  Minor detail here, we need to update
    // the pointers to point to the remaining frames
    pInputs[0] = Input + NPart0*2;
    pInputs[1] = pInputs[0] + 1;
    pOutputs[0] = Output + NPart0*2;
    pOutputs[1] = pOutputs[0] + 1;

    vDSP_biquadm(Setup, (const float**)pInputs, 2, pOutputs, 2, NPart1);

    // We're done with the filter so free any associated resources:
    vDSP_biquadm_DestroySetup(Setup);

    // Free our arrays:
    free(F);
    free(Input);
    free(Output);
}
```

[Next](README.md.md)[Previous](SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md)

