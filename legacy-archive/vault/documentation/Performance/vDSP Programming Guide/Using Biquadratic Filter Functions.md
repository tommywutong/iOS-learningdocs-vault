---
title: vDSP Programming Guide
apple_id: TP40005147
resource_type: Guide
platform: iOS|macOS
topic: Mathematical Computation
technology: Accelerate
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/UsingBiquadraticFilterFunctions/UsingBiquadraticFilterFunctions.html
archived_at: '2026-07-18T01:50:33.661471Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vDSP Programming Guide](Introduction.md)



# Using Biquadratic Filter Functions

The vDSP API provides two sets of functions to support single-channel and multichannel biquadratic (IIR) filtering of a signal. These are the [vDSP_biquad](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad) and [vDSP_biquadm](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm) families, respectively.

For an example of biquadratic filters in use, see _[SignalProcessing: Using Biquadratic Filter Functions](../../../samplecode/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrt)_. This chapter will make frequent references to this code sample.

In biquadratic filtering, we use a set of individual filter objects called _sections_. The filters are _cascaded_: that is, the filters are set up in a sequence, and the entire signal passes through each filter in turn.

To prepare for biquad filtering of a signal, we provide an array of filter coefficients, five for each section: three feedforward coefficients and two feedback coefficients. The layout of this array is described in _[vDSP Reference](https://developer.apple.com/documentation/accelerate/vdsp)_ and illustrated in _[SignalProcessing: Using Biquadratic Filter Functions](../../../samplecode/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrt)_.

A `CreateSetup` function takes the coefficients array and the number of sections as parameters, and returns a _setup_ object.

The setup object is passed into an execution function: either [vDSP_biquad](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad) for single-channel filtering, or [vDSP_biquadm](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm) for multichannel filtering. The execution function may be called repeatedly using the same setup object for a series of signals.

In single channel filtering, the direct-form 1 state values are explicitly specified to the execution function; whereas for multichannel filtering the state values are opaque to the user and modified by the execution function.

In multichannel filtering, a set of functions is provided for manipulating the state of the setup between calls to the execution function. This is illustrated in _[SignalProcessing: Using Biquadratic Filter Functions](../../../samplecode/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrt)_.

Finally, a setup is destroyed by one of the functions

- [vDSP_biquad_DestroySetup](https://developer.apple.com/documentation/accelerate/1450168-vdsp_biquad_destroysetup)
- [vDSP_biquad_DestroySetupD](https://developer.apple.com/documentation/accelerate/1450640-vdsp_biquad_destroysetupd)
- [vDSP_biquadm_DestroySetup](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup)
- [vDSP_biquadm_DestroySetupD](https://developer.apple.com/documentation/accelerate/1450779-vdsp_biquadm_destroysetupd)

A setup is an opaque object containing all the information needed to define a cascading biquadratic filter. In multichannel filtering it includes internal state information that can be altered by any function that the setup is passed to. A setup should only be used in one thread at a time.

There are four `CreateSetup` functions:

- [vDSP_biquad_CreateSetup](https://developer.apple.com/documentation/accelerate/1450374-vdsp_biquad_createsetup): single-channel, single precision; returns a setup of type `vDSP_biquad_Setup`.
- [vDSP_biquad_CreateSetupD](https://developer.apple.com/documentation/accelerate/1450239-vdsp_biquad_createsetupd): single-channel, double precision; returns a setup of type `vDSP_biquad_SetupD`.
- [vDSP_biquadm_CreateSetup](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup): multichannel, single precision; returns a setup of type `vDSP_biquadm_Setup`.
- [vDSP_biquadm_CreateSetupD](https://developer.apple.com/documentation/accelerate/1449719-vdsp_biquadm_createsetupd): multichannel, double precision; returns a setup of type `vDSP_biquadm_SetupD`.

Each of the single-channel functions takes two parameters: an array of filter coefficients, and the number of sections. For the multichannel functions, there is a third parameter, the number of channels.

The array of coefficients should have a length of 5 \* `M` \* `N`, where `M` is the number of channels and `N` is the number of sections. For the layout and interpretation of the coefficients, see [vDSP_biquad_CreateSetup](https://developer.apple.com/documentation/accelerate/1450374-vdsp_biquad_createsetup) or [vDSP_biquadm_CreateSetup](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup) in the reference manual.

Creating setups is a preparation step to be done when a program is starting, or is starting some new phase (e.g., when a communication channel is opened). It should never be done during real-time processing. The setup routine is slow and is called only once to prepare data that can be used many times.

Each section of a single-channel biquadratic cascade implements a direct-form 1 filter.

The cascade is applied to a signal by passing a setup of type `vDSP_biquad_Setup` or `vDSP_biquad_SetupD` to the [vDSP_biquad](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad) or [vDSP_biquadD](https://developer.apple.com/documentation/accelerate/1450359-vdsp_biquadd) function. The other parameters are pointers to input and output signal arrays and their strides, a pointer to an array of “delay” values, and the number of input samples to be processed.

The `Delay` array should have a length equal (2 \* `M`) + 2, where `M` is the number of sections. For further details, see [vDSP_biquad](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad) in the reference manual. After this function executes, this array contains the final state data of the filters.

`Delay` should be initialized to appropriate initial values if they are known, or to zeros otherwise.

After [vDSP_biquad](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad) or [vDSP_biquadD](https://developer.apple.com/documentation/accelerate/1450359-vdsp_biquadd) executes, the filtered signal data are left in the output array and the final state of the filters is left in `Delay`. Thus you can continue processing where you left off, if desired.

Each section of a multichannel biquadratic cascade implements a direct-form 2 filter for each channel.

The cascade is applied to a set of signals by passing a setup of type `vDSP_biquadm_Setup` or `vDSP_biquadm_SetupD` to the [vDSP_biquadm](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm) or [vDSP_biquadmD](https://developer.apple.com/documentation/accelerate/1450102-vdsp_biquadmd) function. The other parameters are pointers to input and output signal arrays and their strides, and the number of input samples to be processed. (In multichannel filtering, the filter’s internal state is managed automatically.)

In multichannel filtering, an additional set of functions is available for altering the filter’s internal state or its coefficients between executions:

- [vDSP_biquadm_CopyState](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate) or [vDSP_biquadm_CopyStateD](https://developer.apple.com/documentation/kernel/1580000-vdsp_biquadm_copystated) copies the internal state of one setup to another.
- [vDSP_biquadm_ResetState](https://developer.apple.com/documentation/accelerate/1449898-vdsp_biquadm_resetstate) or [vDSP_biquadm_ResetStateD](https://developer.apple.com/documentation/kernel/1579935-vdsp_biquadm_resetstated) resets the internal state of a setup to what it was when first initialized.
- [vDSP_biquadm_SetActiveFilters](https://developer.apple.com/documentation/kernel/1579973-vdsp_biquadm_setactivefilters) selects which sections of the filter cascade are active. Inactive sections will be skipped in processing the signal.
- [vDSP_biquadm_SetCoefficientsSingle](https://developer.apple.com/documentation/accelerate/1450128-vdsp_biquadm_setcoefficientssing) or [vDSP_biquadm_SetCoefficientsDouble](https://developer.apple.com/documentation/accelerate/1450453-vdsp_biquadm_setcoefficientsdoub) explicitly sets the values of a range of coefficients.
- [vDSP_biquadm_SetTargetsSingle](https://developer.apple.com/documentation/accelerate/1450077-vdsp_biquadm_settargetssingle) or [vDSP_biquadm_SetTargetsDouble](https://developer.apple.com/documentation/kernel/1580010-vdsp_biquadm_settargetsdouble) sets up a ramped change in the values of a range of filter coefficients, to be applied while the filter is iterating through the input samples. For each coefficient to be changed, a _target_ value, a _rate_ (between 0 and 1), and a _threshold_ (>0) are given. When the filter is applied, at each sample, each coefficient’s value is incremented until the difference between its value and _target_ is less than the specified _threshold_. The size of the increment is a function of _rate_ and the difference between _target_ and the initial value. For an example of this, see _[SignalProcessing: Using Biquadratic Filter Functions](../../../samplecode/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions/SignalProcessing-%20Using%20Biquadratic%20Filter%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrt)_.

After the execution function finishes, the filtered signal is left in the output array, and the state of the filter is preserved so that you can continue processing from where you left off, or reset the state if desired.

