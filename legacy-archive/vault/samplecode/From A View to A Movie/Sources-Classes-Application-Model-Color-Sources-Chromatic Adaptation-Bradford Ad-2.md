---
title: From A View to A Movie
apple_id: DTS40009025
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2013-01-02'
source_url: https://developer.apple.com/library/archive/samplecode/From_A_View_to_A_Movie/Listings/Sources_Classes_Application_Model_Color_Sources_Chromatic_Adaptation_Bradford_Adaptation_CBradfordAdaptation_mm.html
archived_at: '2026-07-18T03:09:16.190339Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [From A View to A Movie](From%20A%20View%20to%20A%20Movie.md)


[Next](Sources-Classes-Application-Model-Color-Sources-Chromatic%20Adaptation-Chromatic%20A.md)[Previous](Sources-Classes-Application-Model-Color-Sources-Chromatic%20Adaptation-Bradford%20Ad.md)

# Sources/Classes/Application/Model/Color/Sources/Chromatic Adaptation/Bradford Adaptation/CBradfordAdaptation.mm

```objc
/*
     File: CBradfordAdaptation.mm
 Abstract: 
 Utility for getting the screen gamma, primary colors, and media white point form the display's ICC profile.

  Version: 1.2

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2013 Apple Inc. All Rights Reserved.

 */

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#import <iostream>

//---------------------------------------------------------------------------

#import "CBradfordAdaptation.h"

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Constructor

//---------------------------------------------------------------------------

template <typename Type>
Color::BradfordAdaptation<Type>::BradfordAdaptation(const long nDir)
{
    switch( nDir )
    {
        case -1:
        {
            const Type v[9] =
            {
                Type( 0.9870), Type(-0.1471), Type( 0.1600),
                Type( 0.4323), Type( 0.5184), Type( 0.0493),
                Type(-0.0085), Type( 0.0400), Type( 0.9685)
            };

            m_Matrix.SetMatrix(true,v);

            break;
        }

        case 1:
        default:
        {
            const Type v[9] =
            {
                Type( 0.8951), Type( 0.2664), Type(-0.1614),
                Type(-0.7502), Type( 1.7135), Type( 0.0367),
                Type( 0.0389), Type(-0.0685), Type( 1.0296)
            };

            m_Matrix.SetMatrix(true,v);

            break;
        }
    } // switch
} // BradfordAdaptation

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Destructor

//---------------------------------------------------------------------------

template <typename Type>
Color::BradfordAdaptation<Type>::~BradfordAdaptation()
{
} // Destructor

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Copy Constructors

//---------------------------------------------------------------------------

template <typename Type>
Color::BradfordAdaptation<Type>::BradfordAdaptation(const Color::BradfordAdaptation<Type> &rBA)
{
    m_Matrix = rBA.m_Matrix;
} // Copy Constructor

//---------------------------------------------------------------------------

template <typename Type>
Color::BradfordAdaptation<Type>::BradfordAdaptation( const Color::BradfordAdaptation<Type> * const pBA )
{
    if( pBA != NULL )
    {
        m_Matrix = pBA->m_Matrix;
    } // if
} // Copy Constructor

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Assignment Operator

//---------------------------------------------------------------------------

template <typename Type>
Color::BradfordAdaptation<Type> &Color::BradfordAdaptation<Type>::operator=(const Color::BradfordAdaptation<Type> &rBA)
{
    if( this != &rBA )
    {
        m_Matrix = rBA.m_Matrix;
    } // if

    return *this;
} // BradfordAdaptation::operator=

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Accessor

//---------------------------------------------------------------------------

template <typename Type>
const Math::Matrix3<Type> &Color::BradfordAdaptation<Type>::GetBradfordAdaptation() const
{
    return m_Matrix;
} // Chromaticity::GetChromaticity

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

template class Color::BradfordAdaptation<float>;
template class Color::BradfordAdaptation<double>;

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------
```

[Next](Sources-Classes-Application-Model-Color-Sources-Chromatic%20Adaptation-Chromatic%20A.md)[Previous](Sources-Classes-Application-Model-Color-Sources-Chromatic%20Adaptation-Bradford%20Ad.md)

