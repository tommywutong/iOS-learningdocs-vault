---
title: From A View to A Movie
apple_id: DTS40009025
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2013-01-02'
source_url: https://developer.apple.com/library/archive/samplecode/From_A_View_to_A_Movie/Listings/Sources_Classes_Application_Model_Color_Sources_Color_Space_Profile_CProfile_mm.html
archived_at: '2026-07-18T03:09:17.102942Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [From A View to A Movie](From%20A%20View%20to%20A%20Movie.md)


[Next](Sources-Classes-Application-Model-Color-Sources-Color%20Space-Space-CSpace.h.md)[Previous](Sources-Classes-Application-Model-Color-Sources-Color%20Space-Profile-CProfile.h.md)

# Sources/Classes/Application/Model/Color/Sources/Color Space/Profile/CProfile.mm

```objc
/*
     File: CProfile.mm
 Abstract: 
 Utility class for getting the screen gamma, primary colors, and media white point form the display's ICC profile.

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
#import <string>

//---------------------------------------------------------------------------

#import "Vector3.h"

//---------------------------------------------------------------------------

#import "CFLogError.h"

#import "CEnums.h"

#import "CCIEXYZ.h"
#import "CProfile.h"

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Private - Data Structures

//---------------------------------------------------------------------------

template <typename Type>
struct Color::ProfileStruct
{
    Color::Matrix<Type> m_Colorants;

    Math::Vector2<Type> m_Chromaticity[Color::Index::kMax];

    Type  mnDisplayGamma;

    CFDictionaryRef mpDictionary;

    Color::CIE::XYZ<Type> *mp_CIE_XYZ;
}; // Color::ProfileStruct

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Private - Utilities - Accessors

//---------------------------------------------------------------------------

template <typename Type>
static inline void CProfileSetPrimary(const uint32_t nColorIndex,
                                      Color::ProfileStruct<Type> *pSProfile)
{
    Math::Vector3<Type> color(pSProfile->m_Colorants(nColorIndex,Color::Coordinate::kX),
                              pSProfile->m_Colorants(nColorIndex,Color::Coordinate::kY),
                              pSProfile->m_Colorants(nColorIndex,Color::Coordinate::kZ));

    Type sum = color.x + color.y + color.z;

    pSProfile->m_Chromaticity[nColorIndex].x = color.x / sum;
    pSProfile->m_Chromaticity[nColorIndex].y = color.y / sum;
} // CProfileSetPrimary

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetPrimaries(Color::ProfileStruct<Type> *pSProfile)
{
    CProfileSetPrimary<Type>(Color::Index::kRed, pSProfile);
    CProfileSetPrimary<Type>(Color::Index::kGreen, pSProfile);
    CProfileSetPrimary<Type>(Color::Index::kBlue, pSProfile);
    CProfileSetPrimary<Type>(Color::Index::kWhitePt, pSProfile);
} // CProfileSetPrimaries

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetGamma(ColorSyncProfileRef pProfile,
                             Color::ProfileStruct<Type> *pSProfile)
{
    CFErrorRef pError = NULL;

    if( pProfile == NULL )
    {
        CGDirectDisplayID nDisplayID = CGMainDisplayID();

        pSProfile->mnDisplayGamma = ColorSyncProfileEstimateGammaWithDisplayID( nDisplayID, &pError );

        std::cerr << ">> ERROR: Core Color - Profile - ColorSync profile reference is NULL!" << std::endl;
        std::cerr << ">> WARNING: Core Color - Profile - Returning gamma for the main display!" << std::endl;
    } // if
    else
    {
        pSProfile->mnDisplayGamma = ColorSyncProfileEstimateGamma( pProfile, &pError );
    } // else

    CFLogErrorDescription( CFSTR(">> ERROR: Color Profile:\n{\n%@\n}\n"), pError );
} // CProfileSetGamma

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetDisplay(const Color::Sync &rBase,
                               Color::ProfileStruct<Type> *pSProfile)
{
    ColorSyncProfileRef  pDisplayProfile = rBase.GetProfileRef();

    if( pDisplayProfile != NULL )
    {
        CProfileSetGamma<Type>(pDisplayProfile, pSProfile);
        CProfileSetPrimaries<Type>(pSProfile);
    } // if
} // CProfileSetDisplay

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetColorants(Color::ProfileStruct<Type> *pSProfile)
{
    pSProfile->m_Colorants = pSProfile->mp_CIE_XYZ->GetColorants();

    pSProfile->mpDictionary = pSProfile->mp_CIE_XYZ->GetColorantDictionary();
} // CProfileSetColorants

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetCIEXYZ(Color::ProfileStruct<Type> *pSProfile)
{
    pSProfile->mp_CIE_XYZ = new Color::CIE::XYZ<Type>;

    if( pSProfile->mp_CIE_XYZ != NULL )
    {
        CProfileSetColorants<Type>(pSProfile);
    } // if
} // CProfileSetCIEXYZ

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetCIEXYZ(const CGDirectDisplayID nDisplayID,
                              Color::ProfileStruct<Type> *pSProfile)
{
    pSProfile->mp_CIE_XYZ = new Color::CIE::XYZ<Type>(nDisplayID);

    if( pSProfile->mp_CIE_XYZ != NULL )
    {
        CProfileSetColorants<Type>(pSProfile);
    } // if
} // CProfileSetCIEXYZ

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileSetCIEXYZ(ColorSyncProfileRef pDisplayProfile,
                              Color::ProfileStruct<Type> *pSProfile)
{
    if( pDisplayProfile != NULL )
    {
        pSProfile->mp_CIE_XYZ = new Color::CIE::XYZ<Type>(pDisplayProfile);

        if( pSProfile->mp_CIE_XYZ != NULL )
        {
            CProfileSetColorants<Type>(pSProfile);
        } // if
    } // if
} // CProfileSetCIEXYZ

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Private - Utilities - Destructor

//---------------------------------------------------------------------------

template <typename Type>
static void CProfileDelete(Color::ProfileStruct<Type> *pSProfile)
{
    if( pSProfile != NULL )
    {
        if( pSProfile->mp_CIE_XYZ != NULL )
        {
            delete pSProfile->mp_CIE_XYZ;

            pSProfile->mp_CIE_XYZ = NULL;
        } // if

        delete pSProfile;

        pSProfile = NULL;
    } // if
} // CProfileDelete

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Private - Utilities - Constructors

//---------------------------------------------------------------------------

template <typename Type>
static Color::ProfileStruct<Type> *CProfileCreate(const Color::Sync &rBase)
{
    Color::ProfileStruct<Type> *pSProfile = new Color::ProfileStruct<Type>;

    if( pSProfile != NULL )
    {
        CProfileSetCIEXYZ<Type>(pSProfile);
        CProfileSetDisplay<Type>(rBase, pSProfile);
    } // if

    return pSProfile;
} // CProfileCreate

//---------------------------------------------------------------------------

template <typename Type>
static Color::ProfileStruct<Type> *CProfileCreate(const CGDirectDisplayID nDisplayID,
                                                  const Color::Sync &rBase)
{
    Color::ProfileStruct<Type> *pSProfile = new Color::ProfileStruct<Type>;

    if( pSProfile != NULL )
    {
        CProfileSetCIEXYZ<Type>(nDisplayID, pSProfile);
        CProfileSetDisplay<Type>(rBase, pSProfile);
    } // if

    return pSProfile;
} // CProfileCreate

//---------------------------------------------------------------------------

template <typename Type>
static Color::ProfileStruct<Type> *CProfileCreate(ColorSyncProfileRef pDisplayProfile,
                                                  const Color::Sync &rBase)
{
    Color::ProfileStruct<Type> *pSProfile = new Color::ProfileStruct<Type>;

    if( pSProfile != NULL )
    {
        CProfileSetCIEXYZ<Type>(pDisplayProfile, pSProfile);
        CProfileSetDisplay<Type>(pDisplayProfile, pSProfile);
    } // if

    return pSProfile;
} // CProfileCreate

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Private - Utilities - Copy Constructor

//---------------------------------------------------------------------------

template <typename Type>
static Color::ProfileStruct<Type> *CProfileCreateCopy(const Color::ProfileStruct<Type> * const pSProfileSrc)
{
    Color::ProfileStruct<Type> *pSProfileDst = NULL;

    if( pSProfileSrc != NULL )
    {
        pSProfileDst = new Color::ProfileStruct<Type>;

        if( pSProfileDst != NULL )
        {
            pSProfileDst->mnDisplayGamma = pSProfileSrc->mnDisplayGamma;

            *pSProfileDst->mp_CIE_XYZ = *pSProfileSrc->mp_CIE_XYZ;

            if( pSProfileDst->mp_CIE_XYZ != NULL )
            {
                CProfileSetColorants<Type>(pSProfileDst);
                CProfileSetPrimaries<Type>(pSProfileDst);
            } // if
        } // if
    } // if

    return( pSProfileDst );
} // CProfileCreateCopy

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Constructors

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type>::Profile()
: Color::Sync::Sync()
{
    mpSProfile = CProfileCreate<Type>(*this);
} // Constructor

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type>::Profile( const CGDirectDisplayID nDisplayID )
: Color::Sync::Sync(nDisplayID)
{
    mpSProfile = CProfileCreate<Type>(nDisplayID, *this);
} // Constructor

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type>::Profile( ColorSyncProfileRef pDisplayProfile )
: Color::Sync::Sync(pDisplayProfile)
{
    mpSProfile = CProfileCreate<Type>(pDisplayProfile, *this);
} // Constructor

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Destructor

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type>::~Profile()
{
    CProfileDelete<Type>(mpSProfile);
} // Destructor

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Copy Constructor

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type>::Profile( const Profile<Type> &rProfile )
: Color::Sync::Sync(rProfile)
{
    mpSProfile = CProfileCreateCopy<Type>(rProfile.mpSProfile);
} // Copy Constructor

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type>::Profile( const Profile<Type> * const pProfile )
: Color::Sync::Sync(pProfile)
{
    if( pProfile != NULL )
    {
        mpSProfile = CProfileCreateCopy<Type>(pProfile->mpSProfile);
    } // if
} // Copy Constructor

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Assignment Operator

//---------------------------------------------------------------------------

template <typename Type>
Color::Profile<Type> &Color::Profile<Type>::operator=(const Profile<Type> &rProfile)
{
    if( ( this != &rProfile ) && ( rProfile.mpSProfile != NULL ) )
    {
        CProfileDelete<Type>(mpSProfile);

        this->Color::Sync::operator=(rProfile);

        mpSProfile = CProfileCreateCopy<Type>(rProfile.mpSProfile);
    } // if

    return *this;
} // Profile::operator=

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Public - Accessors

//---------------------------------------------------------------------------

template <typename Type>
const Type Color::Profile<Type>::GetDisplayGamma() const
{
    if( mpSProfile != NULL )
    {
        return( mpSProfile->mnDisplayGamma );
    } // if

    return( Type(0) );
} // Profile::GetDisplayGamma

//---------------------------------------------------------------------------

template <typename Type>
const Math::Vector2<Type> &Color::Profile<Type>::GetChromaticityRed() const
{
    return mpSProfile->m_Chromaticity[Color::Index::kRed];
} // GetChromaticityRed

//---------------------------------------------------------------------------

template <typename Type>
const Math::Vector2<Type> &Color::Profile<Type>::GetChromaticityGreen() const
{
    return mpSProfile->m_Chromaticity[Color::Index::kGreen];
} // GetChromaticityGreen

//---------------------------------------------------------------------------

template <typename Type>
const Math::Vector2<Type> &Color::Profile<Type>::GetChromaticityBlue() const
{
    return mpSProfile->m_Chromaticity[Color::Index::kBlue];
} // GetChromaticityBlue

//---------------------------------------------------------------------------

template <typename Type>
const Math::Vector2<Type> &Color::Profile<Type>::GetChromaticityWhitePoint() const
{
    return mpSProfile->m_Chromaticity[Color::Index::kWhitePt];
} // GetChromaticityWhitePoint

//---------------------------------------------------------------------------

template <typename Type>
const Color::Matrix<Type> &Color::Profile<Type>::GetColorants() const
{
    return mpSProfile->m_Colorants;
} // GetColorantRed

//---------------------------------------------------------------------------

template <typename Type>
CFDictionaryRef Color::Profile<Type>::GetColorantDictionary() const
{
    return mpSProfile->mpDictionary;
} // GetDictionary

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------

#pragma mark -
#pragma mark Template - Implementations - ICC Profile

//---------------------------------------------------------------------------

template class Color::Profile<float>;
template class Color::Profile<double>;

//---------------------------------------------------------------------------

//---------------------------------------------------------------------------
```

[Next](Sources-Classes-Application-Model-Color-Sources-Color%20Space-Space-CSpace.h.md)[Previous](Sources-Classes-Application-Model-Color-Sources-Color%20Space-Profile-CProfile.h.md)

