---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitGeneratorExample_Utility_ComplexNumber_h.html
archived_at: '2026-07-26T19:54:11.197604Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitGeneratorExample-Utility-Biquad.h.md)[Previous](AudioUnitGeneratorExample-Utility-Pink.h.md)

# AudioUnitGeneratorExample/Utility/ComplexNumber.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  ComplexNumber.h
//
//      a useful complex number class
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ifndef __CoreAudio_ComplexNumber
#define __CoreAudio_ComplexNumber

#include <math.h>
#include <stdio.h>

class Complex
{
public:
    Complex()
        : mReal(0.0), mImag(0.0) {};

    Complex(double inReal, double inImag )
        : mReal(inReal), mImag(inImag) {};

    Complex(float inReal)               // construct complex from real
        : mReal(inReal), mImag(0) {};

    double          GetReal() const {return mReal;};
    double          GetImag() const {return mImag;};
    void            SetReal(double inReal) {mReal = inReal;};
    void            SetImag(double inImag) {mImag = inImag;};

    double          Phase() const {return atan2(mImag, mReal);};
    double          GetPhase() const {return atan2(mImag, mReal);};
    double          Magnitude() const {return sqrt(mImag*mImag + mReal*mReal);};
    double          GetMagnitude() const {return sqrt(mImag*mImag + mReal*mReal);};

    void            SetMagnitudePhase(double inMagnitude, double inPhase)
    {
        mReal = inMagnitude * cos(inPhase);
        mImag = inMagnitude * sin(inPhase);
    };

    Complex         Pow(double inPower)
    {
        double mag = GetMagnitude();
        double phase = GetPhase();

        Complex result;
        result.SetMagnitudePhase(pow(mag, inPower), phase*inPower );

        return result;
    };

    Complex         GetConjugate() const {return Complex(mReal, -mImag);};

    Complex         inline operator += (const Complex &a);
    Complex         inline operator -= (const Complex &a);

    void            Print() {printf("(%f,%f)", mReal, mImag ); };
    void            PrintMagnitudePhase() {printf("(%f,%f)\n", GetMagnitude(), GetPhase() ); };

    double          mReal;
    double          mImag;
};

Complex         inline operator+ (const Complex &a, const Complex &b )
    {return Complex(a.GetReal() + b.GetReal(), a.GetImag() + b.GetImag() ); };

Complex         inline operator - (const Complex &a, const Complex &b )
    {return Complex(a.GetReal() - b.GetReal(), a.GetImag() - b.GetImag() ); };

Complex         inline operator * (const Complex &a, const Complex &b )
    {return Complex(    a.GetReal()*b.GetReal() - a.GetImag()*b.GetImag(),
                        a.GetReal()*b.GetImag() + a.GetImag()*b.GetReal() ); };

Complex         inline operator * (const Complex &a, double b)
    {return Complex(a.GetReal()*b, a.GetImag()*b );};

Complex         inline operator * (double b, const Complex &a )
    {return Complex(a.GetReal()*b, a.GetImag()*b );};

Complex         inline operator/(const Complex& a, const Complex& b)
{
    double mag1 = a.GetMagnitude();
    double mag2 = b.GetMagnitude();

    double phase1 = a.GetPhase();
    double phase2 = b.GetPhase();

    Complex c;
    c.SetMagnitudePhase(mag1/mag2, phase1 - phase2 );

    return c;
}

Complex         inline Complex::operator += (const Complex &a)
{
    *this = *this + a;
    return *this;
};

Complex         inline Complex::operator -= (const Complex &a)
{
    *this = *this - a;
    return *this;
};

bool            inline  operator == (const Complex &a, const Complex &b )
{
    return a.GetReal() == b.GetReal() && a.GetImag() == b.GetImag();
}

inline Complex      UnitCircle(double mag, double phase)
{
    return Complex(mag * cos(phase), mag * sin(phase) );
}

#endif // __ComplexNumber
```

[Next](AudioUnitGeneratorExample-Utility-Biquad.h.md)[Previous](AudioUnitGeneratorExample-Utility-Pink.h.md)

